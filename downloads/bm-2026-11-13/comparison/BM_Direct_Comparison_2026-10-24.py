#!/usr/bin/env python3
"""Controlled BM/native comparison. See the fixed protocol and README.

python BM_Direct_Comparison_2026-10-24.py generate DIRECTORY
python BM_Direct_Comparison_2026-10-24.py run DIRECTORY

Run requires numpy, scipy, sympy, matplotlib and the pinned CLUE source on
PYTHONPATH. Existing BM sources in DIRECTORY/sources are not modified.
"""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import importlib.metadata
import json
import logging
import math
import platform
import random
import statistics
import sys
import time
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp, minimize_scalar
import sympy as sp


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def save(path, value):
    path.write_text(json.dumps(value, indent=2, default=str) + '\n')


def partition_labels(pairs, n):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in pairs:
        parent[root(x)] = root(y)
    labels, seen = [], {}
    for x in range(n):
        labels.append(seen.setdefault(root(x), len(seen)))
    return labels


def native_future(p, witnesses=False):
    """Classical distinguishable-pair propagation, independently implemented."""
    n = len(p['states'])
    obs = [('available', tuple((type(p['tasks'][k][x]).__name__, p['tasks'][k][x])
                               for k in sorted(p['tasks']))) for x in range(n)]
    obs.append(('unavailable',))
    actions = {k: [n if v is None else v for v in a]+[n] for k,a in p['actions'].items()}
    pairs = list(combinations(range(n+1), 2))
    parents = defaultdict(list)
    for x,y in pairs:
        for k,a in actions.items():
            if a[x] != a[y]:
                parents[tuple(sorted((a[x],a[y])))].append(((x,y),k))
    marked = {(x,y) for x,y in pairs if obs[x] != obs[y]}
    words = {pair: [] for pair in marked} if witnesses else {}
    todo = deque(sorted(marked))
    while todo:
        child = todo.popleft()
        for parent,action in parents[child]:
            if parent not in marked:
                marked.add(parent)
                if witnesses:
                    words[parent] = [action]+words[child]
                todo.append(parent)
    equal_pairs = [(x,y) for x,y in pairs if y<n and (x,y) not in marked]
    return partition_labels(equal_pairs,n), words


def sensor_problem(p, labels):
    names = sorted(p['observations'])
    pairs = [(x,y) for x,y in combinations(range(len(labels)),2) if labels[x]!=labels[y]]
    matrix = [[int((type(p['observations'][k][x]).__name__,p['observations'][k][x]) !=
                   (type(p['observations'][k][y]).__name__,p['observations'][k][y]))
               for k in names] for x,y in pairs]
    costs = [F(p.get('feature_costs',{}).get(k,1)) for k in names]
    def feasible(indices):
        return all(any(row[i] for i in indices) for row in matrix)
    full = feasible(range(len(names)))
    essential = [name for i,name in enumerate(names)
                 if full and not feasible([j for j in range(len(names)) if j!=i])]
    if 'candidates' in p:
        allowed = [[names.index(k) for k in subset] for subset in p['candidates']]
        legal = [s for s in allowed if feasible(s)]
        choice = min(legal,key=lambda s:sum(costs[i] for i in s),default=None)
        route = 'exact supplied-catalogue scan'
    elif not full:
        choice,route = None,'uncovered separating pair'
    elif not matrix:
        choice,route = [],'no distinctions required'
    else:
        denom = math.lcm(*(x.denominator for x in costs))
        objective = np.array([int(x*denom) for x in costs],dtype=float)
        fit = milp(objective,integrality=np.ones(len(names)),bounds=Bounds(0,1),
                   constraints=LinearConstraint(np.array(matrix,dtype=float),1,np.inf),
                   options={'mip_rel_gap':0})
        if not fit.success:
            raise RuntimeError(f'sensor MILP: {fit.message}')
        choice = [i for i,v in enumerate(fit.x) if v>.5]
        assert feasible(choice)
        assert max(abs(v-round(v)) for v in fit.x)<1e-7
        route = 'SciPy/HiGHS binary weighted set cover'
    return {'full_feasible':full,'essential':essential,'minimum_cost':None if choice is None else str(sum((costs[i] for i in choice),F())),
            'selected':None if choice is None else [names[i] for i in choice], 'route':route}


def native_interfaces(p):
    """MILP over local equivalence pairs; does not enumerate local partitions."""
    sizes,legal,task = p['sizes'],p['legal'],p['task']
    weights = p.get('weights',[1]*len(sizes))
    pair_vars,rep_vars = {},{}
    for i,n in enumerate(sizes):
        for x,y in combinations(range(n),2):
            pair_vars[i,x,y] = len(pair_vars)
    offset = len(pair_vars)
    for i,n in enumerate(sizes):
        for x in range(n):
            rep_vars[i,x] = offset+len(rep_vars)
    count = offset+len(rep_vars)
    rows,lower,upper = [],[],[]
    def add(terms,lo=-np.inf,hi=np.inf):
        row = np.zeros(count)
        for index,coefficient in terms:
            row[index] += coefficient
        rows.append(row);lower.append(lo);upper.append(hi)
    def eq(i,x,y):
        return pair_vars[(i,min(x,y),max(x,y))]
    for i,n in enumerate(sizes):
        for a,b,c in combinations(range(n),3):
            ab,ac,bc = eq(i,a,b),eq(i,a,c),eq(i,b,c)
            for neg in [ab,ac,bc]:
                add([(v,-1 if v==neg else 1) for v in [ab,ac,bc]],hi=1)
        add([(rep_vars[i,0],1)],lo=1,hi=1)
        for x in range(1,n):
            es = [eq(i,j,x) for j in range(x)]
            add([(rep_vars[i,x],1)]+[(v,1) for v in es],lo=1)
            for v in es:
                add([(rep_vars[i,x],1),(v,1)],hi=1)
    bounds=p.get('bounds',[[0]*n for n in sizes])
    for (i,x,y),v in pair_vars.items():
        if bounds[i][x] != bounds[i][y]:
            add([(v,1)],hi=0)
    for x,y in combinations(range(len(legal)),2):
        inputs = [eq(i,a,b) for i,(a,b) in enumerate(zip(legal[x],legal[y])) if a!=b]
        if task[x]!=task[y]:
            add([(v,1) for v in inputs],hi=len(inputs)-1)
        for action in p.get('actions',[]):
            xx,yy=action[x],action[y]
            if (xx is None)!=(yy is None):
                add([(v,1) for v in inputs],hi=len(inputs)-1)
            elif xx is not None:
                for i,(a,b) in enumerate(zip(legal[xx],legal[yy])):
                    if a!=b:
                        add([(v,1) for v in inputs]+[(eq(i,a,b),-1)],hi=len(inputs)-1)
    objective=np.zeros(count)
    for (i,x),v in rep_vars.items():objective[v]=weights[i]
    fit=milp(objective,integrality=np.ones(count),bounds=Bounds(0,1),
             constraints=LinearConstraint(np.array(rows),lower,upper),options={'mip_rel_gap':0})
    if not fit.success:raise RuntimeError(f'interface MILP: {fit.message}')
    assert max(abs(v-round(v)) for v in fit.x)<1e-7
    family=[]
    for i,n in enumerate(sizes):
        family.append(partition_labels([(x,y) for x,y in combinations(range(n),2)
                                       if fit.x[eq(i,x,y)]>.5],n))
    exact_cost=sum(F(w)*len(set(row)) for w,row in zip(weights,family))
    assert abs(float(exact_cost)-fit.fun)<1e-7
    return {'family':family,'cost':str(exact_cost),'binary_variables':count,'constraints':len(rows)}


def generate(root):
    rng=random.Random(241001)
    finite=json.loads((root/'sources/BM_Necessity_Examples_2026-10-23.json').read_text())
    for k in range(48):
        n=rng.randrange(4,25);m=rng.randrange(1,8)
        actions={f'a{i}':[rng.choice([None]+list(range(n))) for _ in range(n)]
                 for i in range(rng.randrange(4))}
        tasks={'output':[rng.randrange(1+(k%4)) for _ in range(n)]}
        observations={f's{i}':[rng.randrange(2+(i%3)) for _ in range(n)] for i in range(m)}
        if k%3==0:observations['s0']=list(range(n))
        finite[f'seeded_{k:02}']={'states':[str(i) for i in range(n)],'actions':actions,
                                'tasks':tasks,'observations':observations,
                                'feature_costs':{name:rng.randrange(1,10) for name in observations}}
    full2=list(map(list,product(range(2),repeat=2)))
    full3=list(map(list,product(range(2),repeat=3)))
    interfaces={
        'full_xor':{'sizes':[2,2],'legal':full2,'task':[a^b for a,b in full2]},
        'diagonal_copy':{'sizes':[2,2],'legal':[[0,0],[1,1]],'task':[0,1],'weights':[1,2]},
        'three_way_parity':{'sizes':[2,2,2],'legal':full3,'task':[a^b^c for a,b,c in full3]},
        'correlated_parity':{'sizes':[2,2,2],'legal':[[a,b,a^b] for a,b in full2],'task':[a for a,b in full2]},
        'availability':{'sizes':[2,2],'legal':full2,'task':[0]*4,'actions':[[None,None,0,1]]},
        'retained_legacy':{'sizes':[3,2],'legal':list(map(list,product(range(3),range(2)))),
                           'task':[a%2 for a,b in product(range(3),range(2))],'bounds':[[0,1,2],[0,0]]}}
    rng=random.Random(241002)
    for k in range(30):
        sizes=[rng.choice([2,3]) for _ in range(rng.choice([2,3]))]
        states=list(product(*(range(n) for n in sizes)))
        legal=sorted(rng.sample(states,rng.randrange(2,len(states)+1)))
        actions=[[rng.choice([None]+list(range(len(legal)))) for _ in legal] for _ in range(k%3)]
        interfaces[f'seeded_{k:02}']={'sizes':sizes,'legal':legal,'task':[rng.randrange(1+k%3) for _ in legal],
                                     'actions':actions,'weights':[rng.randrange(1,4) for _ in sizes]}
    linear={
        'oscillator':{'A':[[0,1],[-1,0]],'L':[[1,0]]},
        'shear':{'A':[[0,1],[0,0]],'L':[[1,0]]},
        'diagonal':{'A':[[-1,0,0],[0,-2,0],[0,0,-3]],'L':[[1,0,0]]},
        'repeated_eigenvalue':{'A':[[-1,0,0],[0,-1,0],[0,0,-2]],'L':[[1,1,0]]},
        'zero':{'A':[[0]*3 for _ in range(3)],'L':[[1,0,0]]},
        'chain7':{'A':[[int(j==i+1) for j in range(7)] for i in range(7)],'L':[[1]+[0]*6]}}
    rng=random.Random(241003)
    for k in range(12):
        n=rng.randrange(2,7)
        linear[f'dense_{k:02}']={'A':[[rng.randrange(-2,3) for _ in range(n)] for _ in range(n)],
                                'L':[[1]+[0]*(n-1)]}
    for k in range(12):
        n=rng.randrange(2,7);r=rng.randrange(1,n)
        a=sp.zeros(n)
        for i in range(r):
            a[i,i]=-1
            if i+1<r:a[i,i+1]=1
        for i in range(r,n):
            for j in range(r,n):a[i,j]=rng.randrange(-2,3)
        s=sp.eye(n)
        for i in range(n):
            for j in range(i+1,n):s[i,j]=rng.randrange(-2,3)
        native=s.inv()*a*s
        linear[f'reducible_{k:02}']={'A':[[str(native[i,j]) for j in range(n)] for i in range(n)],
                                    'L':[[str(s[0,j]) for j in range(n)]], 'constructed_dimension':r}
    phases=[0,math.pi/12,math.pi/6,math.pi/4,math.pi/3,math.pi/2,2*math.pi/3,math.pi]
    robust=[{'theta':t,'eta':eta} for t in phases for eta in [0,.01,.1,.5,1]]
    data={'finite':finite,'interfaces':interfaces,'linear':linear,'robust':robust}
    save(root/'BM_Comparison_Inputs_2026-10-24.json',data)
    print(json.dumps({k:len(v) for k,v in data.items()}))


def timed(fn):
    fn()
    readings=[]
    for _ in range(3):
        start=time.perf_counter_ns();fn();readings.append((time.perf_counter_ns()-start)/1e6)
    return statistics.median(readings)


def run(root):
    bm=load_module(root/'sources/BM_Necessity_Analyzer_2026-10-23.py','bm_finite')
    bmif=load_module(root/'sources/BM_Finite_Solvers_2026-10-18.py','bm_interfaces')
    bmresearch=load_module(root/'sources/BM_Research_Verification_2026-10-24.py','bm_research')
    data=json.loads((root/'BM_Comparison_Inputs_2026-10-24.json').read_text())
    result={'scope':'internal controlled comparison; same contracts; no independent peer review',
            'inputs_sha256':hashlib.sha256((root/'BM_Comparison_Inputs_2026-10-24.json').read_bytes()).hexdigest(),
            'finite':[],'interfaces':[],'linear':[],'robust':[]}
    for name,p in data['finite'].items():
        start=time.perf_counter();b=bm.analyze(p);elapsed=(time.perf_counter()-start)*1000
        assert bm.verify_result(p,b)
        c,w=native_future(p,True);native=sensor_problem(p,c)
        assert c==b['quotient']['code_of_state'],name
        assert native['full_feasible']==b['full_observation']['feasible'],name
        assert native['minimum_cost']==b['minimum_feature_cost'],name
        assert native['essential']==b['essential_features'],name
        for (x,y),word in w.items():
            if y==len(c):continue
            xx,yy=x,y
            for a in word:
                xx=None if xx is None else p['actions'][a][xx]
                yy=None if yy is None else p['actions'][a][yy]
            assert bm.task_key(p,xx)!=bm.task_key(p,yy)
        result['finite'].append({'name':name,'states':len(c),'code_states':len(set(c)),
             'bm_cost':b['minimum_feature_cost'],'native':native,'agreement':True,
             'native_pair_witnesses':sum(y<len(c) for x,y in w),
             'bm_full_analyzer_ms':elapsed,'bm_partition_ms':timed(lambda:bm.future_partition(p)),
             'native_partition_ms':timed(lambda:native_future(p))})
    print('Finite suite passed',flush=True)
    for name,p in data['interfaces'].items():
        start=time.perf_counter();b=bmif.optimize_interfaces(**p);btime=(time.perf_counter()-start)*1000
        start=time.perf_counter();native=native_interfaces(p);ntime=(time.perf_counter()-start)*1000
        assert native['cost']==str(b['optimal_cost']),name
        assert bmif.interface_feasible(p['legal'],native['family'],p['task'],p.get('actions',[])),name
        for row,bound in zip(native['family'],p.get('bounds',[[0]*n for n in p['sizes']])):
            assert bmif.refines(row,bound)
        result['interfaces'].append({'name':name,'bm_cost':str(b['optimal_cost']),'native':native,
              'agreement':True,'bm_families_enumerated':b['enumerated'],'bm_greatest_exists':b['greatest_exists'],
              'bm_full_report_ms':btime,'native_minimum_only_ms':ntime})
    print('Interface suite passed',flush=True)
    from clue import FODESystem,SparsePolynomial,SparseRowMatrix,SparseVector
    import clue.linalg as clinalg
    logging.getLogger('clue').setLevel(logging.ERROR)
    def basis(a,l):
        stack=[];layer=l
        for _ in range(len(a)):
            stack+=layer;layer=bmresearch.multiply(layer,a)
        return bmresearch.row_basis(stack,len(a))
    for name,p in data['linear'].items():
        a=[[F(v) for v in row] for row in p['A']];l=[[F(v) for v in row] for row in p['L']]
        n=len(a);names=[f'x{i}' for i in range(n)]
        poly=lambda row:SparsePolynomial.from_vector([sp.QQ(str(v)) for v in row],names,sp.QQ)
        ode=FODESystem([poly(row) for row in a],variables=names)
        reduced=ode.lumping([poly(row) for row in l],method='polynomial')
        q=basis(a,l)
        nativeq=[[F(str(v)) for v in row] for row in reduced.lumping_matrix.to_list()]
        assert bmresearch.row_basis(nativeq,n)==q,name
        assert reduced.is_consistent(how='exact'),name
        if 'constructed_dimension' in p:assert len(q)==p['constructed_dimension'],name
        # SparseVector.apply_matrix uses column vectors, hence transpose A.
        matrix=SparseRowMatrix.from_list([[sp.QQ(str(a[j][i])) for j in range(n)] for i in range(n)])
        vectors=tuple(SparseVector.from_list([sp.QQ(str(v)) for v in row]) for row in l)
        def clue_core():
            clinalg.__dict__['__CACHE_FSCS'].clear()
            return clinalg.find_smallest_common_subspace((matrix,),vectors).matrix().to_list()
        core=[[F(str(v)) for v in row] for row in clue_core()]
        assert bmresearch.row_basis(core,n)==q,name
        result['linear'].append({'name':name,'native_dimension':n,'bm_dimension':len(q),
            'clue_dimension':reduced.size,'same_row_space':True,'clue_exact_consistency':True,
            'basis':[[str(v) for v in row] for row in q],
            'bm_core_ms':timed(lambda:basis(a,l)),'clue_core_ms':timed(clue_core)})
    names=['x1','x2','x3'];poly=lambda s:SparsePolynomial.from_string(s,names,sp.QQ)
    ode=FODESystem([poly('x2^2+4*x2*x3+4*x3^2'),poly('4*x3-2*x1'),poly('x1+x2')],variables=names)
    nl=ode.lumping([poly('x1')],method='polynomial')
    assert nl.size==2 and nl.is_consistent(how='exact')
    x1,x2,x3=sp.symbols('x1 x2 x3')
    assert sp.expand((4*x3-2*x1)+2*(x1+x2)-2*(x2+2*x3))==0
    assert sp.expand(x2*x2+4*x2*x3+4*x3*x3-(x2+2*x3)**2)==0
    result['nonlinear_clue']={'dimension':nl.size,'observables':[str(v) for v in nl.old_vars],
                             'equations':[str(v) for v in nl.equations],'exact_consistency':True,
                             'bm_general_nonlinear_reducer_ran':False}
    print('CLUE suite passed',flush=True)
    for p in data['robust']:
        theta,eta=p['theta'],p['eta'];c,s=abs(math.cos(theta)),abs(math.sin(theta))
        objective=lambda a:math.hypot(c-a,s)+eta*a
        fit=minimize_scalar(objective,bounds=(0,c),method='bounded',options={'xatol':1e-14})
        assert fit.success
        native=min(objective(0),objective(c),fit.fun)
        b=bmresearch.position_error(theta,eta)
        assert abs(b-native)<1e-8,p
        result['robust'].append({**p,'bm_error':b,'optimal_recovery_error':native,'difference':abs(b-native)})
    # The integration study asks the same complete contract of each workflow.
    oscillator_basis=[[F(1),F(0)],[F(0),F(1)]]
    sensor=[[F(1),F(0)]]
    initialized=len(bmresearch.row_basis(sensor+oscillator_basis,2))==len(bmresearch.row_basis(sensor,2))
    assert not initialized
    # Exact rank says recoverable; the stated noise/tolerance contract says otherwise.
    alpha=.02*math.pi;eta=.1;tolerance=.2
    bmat=np.array([[1.,0.],[math.cos(alpha),-math.sin(alpha)]])
    native_error=min(1,eta/np.linalg.svd(bmat,compute_uv=False)[-1])
    bm_error=bmresearch.history_error(alpha,eta)
    assert abs(native_error-bm_error)<1e-10 and native_error>tolerance
    # Global binary constraints: a=b, b=c, a+c=1.
    cmat=np.array([[1,-1,0],[0,1,-1],[1,0,1]],dtype=float)
    fit=milp(np.zeros(3),integrality=np.ones(3),bounds=Bounds(0,1),
              constraints=LinearConstraint(cmat,[0,0,1],[0,0,1]))
    candidates=[z for z in product([0,1],repeat=3) if z[0]==z[1] and z[1]==z[2] and z[0]!=z[2]]
    bm_completions=bmif.finite_seed([[0,1]]*3,{},allowed=candidates)
    assert not bm_completions and fit.status==2
    result['integration']=[
        {'case':'initialize oscillator from position only','bm':'infeasible','complete_native_workflow':'infeasible',
         'incomplete_stage':'CLUE reduction alone supplies a two-dimensional state; initialization is outside that call'},
        {'case':'two near-coincident samples; noise .1; tolerance .2','bm':'infeasible','complete_native_workflow':'infeasible',
         'error':bm_error,'incomplete_stage':'rank alone passes; bounded-noise recovery is an additional obligation'},
        {'case':'three jointly contradictory Boolean constraints','bm':'infeasible','complete_native_workflow':'infeasible',
         'incomplete_stage':'each single constraint and each pair is satisfiable'}]
    # A negative control: a future-closure criterion can be unnecessary for a present-only task.
    result['negative_control']={'case':'oscillator position at initialization only',
        'required_code_dimension':1,'full_future_code_dimension':2,
        'interpretation':'Overstating the task makes either workflow retain unnecessary information.'}
    result['environment']={'python':sys.version.split()[0],'platform':platform.platform(),
        'packages':{p:importlib.metadata.version(p) for p in ['numpy','scipy','sympy','matplotlib','natsort','requests','beautifulsoup4']},
        'clue_commit':'0576e9b8477bc511e3fea29a3c296c5d30b688aa','clue_version_from_setup':'1.7.3',
        'clue_core_cache_cleared_each_call':True,'timing_repetitions':3}
    result['summary']={'finite_cases':len(result['finite']),'interface_cases':len(result['interfaces']),
        'linear_cases':len(result['linear']),'noisy_cases':len(result['robust']),
        'mathematical_disagreements':0,'native_witnesses_replayed':sum(r['native_pair_witnesses'] for r in result['finite']),
        'maximum_noisy_error_difference':max(r['difference'] for r in result['robust']),
        'finite_core_median_ms':{'bm':statistics.median(r['bm_partition_ms'] for r in result['finite']),
                                 'native':statistics.median(r['native_partition_ms'] for r in result['finite'])},
        'linear_core_median_ms':{'bm':statistics.median(r['bm_core_ms'] for r in result['linear']),
                                 'clue':statistics.median(r['clue_core_ms'] for r in result['linear'])}}
    result['status']='passed'
    save(root/'BM_Comparison_Results_2026-10-24.json',result)
    print(json.dumps(result['summary'],indent=2),flush=True)


if __name__=='__main__':
    mode=sys.argv[1];root=Path(sys.argv[2]).resolve()
    if mode=='generate':generate(root)
    elif mode=='run':run(root)
    else:raise SystemExit('Use generate or run')
