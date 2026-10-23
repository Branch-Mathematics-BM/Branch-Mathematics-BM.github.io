from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
import ast, copy, importlib.util, json, sys
OUT=Path(__file__).resolve().parent

def module(name, filename):
    spec=importlib.util.spec_from_file_location(name, OUT/filename)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod)
    return mod
qv=module('quantum','BM_Quantum_Certificate_Verifier_2026-10-23.py')
pred=module('predictor','BM_Decay_Profile_Predictor_2026-10-23.py')

def dumpable(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:dumpable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [dumpable(v) for v in x]
    return x

def save(name,x):
    (OUT/name).write_text(json.dumps(dumpable(x),indent=2)+'\n')

def diag(v):return [[F(v[i]) if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def sc(c,a):return [[c*x for x in row] for row in a]
def sub(a,b):return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
certs=[]
certs.append({'name':'Two nonorthogonal pure signals',
 'states':[[[1,0],[0,0]],[[F(9,25),F(12,25)],[F(12,25),F(16,25)]]],
 'povm':[[[F(9,10),F(-3,10)],[F(-3,10),F(1,10)]],[[F(1,10),F(3,10)],[F(3,10),F(9,10)]]],
 'success_lower':F(9,10),'dual_weights':[F(1,2)]*2,
 'dual_matrix':[[F(27,50),F(3,25)],[F(3,25),F(9,25)]],'expected_error':F(1,5)})
bb=[diag([1,0]),diag([0,1]),[[F(1,2)]*2 for _ in range(2)],[[F(1,2),F(-1,2)],[F(-1,2),F(1,2)]]]
certs.append({'name':'Four BB84 signal states', 'states':bb,'povm':[sc(F(1,2),a) for a in bb],
 'success_lower':F(1,2),'dual_weights':[F(1,4)]*4,'dual_matrix':diag([F(1,4)]*2),'expected_error':1})
for r in range(2,7):
    sigma=diag([F(1,3),F(2,3)])
    certs.append({'name':f'{r} identical signal states','states':[sigma]*r,'povm':[diag([F(1,r)]*2)]*r,
     'success_lower':F(1,r),'dual_weights':[F(1,r)]*r,'dual_matrix':sc(F(1,r),sigma),'expected_error':2-2*F(1,r)})
for r in range(2,6):
    states=[diag([int(i==j) for j in range(r)]) for i in range(r)]
    certs.append({'name':f'{r} orthogonal signal states','states':states,'povm':states,
     'success_lower':1,'dual_weights':[F(1,r)]*r,'dual_matrix':diag([F(1,r)]*r),'expected_error':0})
    p=F(3,4);b=(1-p)/(r-1)
    noisy=[diag([p if i==j else b for j in range(r)]) for i in range(r)]
    certs.append({'name':f'{r}-symbol symmetric classical channel','states':noisy,'povm':states,
     'success_lower':p,'dual_weights':[F(1,r)]*r,'dual_matrix':diag([p/r]*r),'expected_error':F(1,2)})
certs=dumpable(certs)
save('BM_Quantum_Certificates_2026-10-23.json',{'theorem':'BM23-Q3','arithmetic':'exact real rationals','certificates':certs})
qresults=[qv.verify(c) for c in certs]
assert all(c['exact_optimum'] for c in qresults)

# Independent exact principal-minor oracle for the critical PSD checker.
def determinant(a):
    a=[list(map(F,row)) for row in a];n=len(a);d=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:a[pivot],a[k]=a[k],a[pivot];d=-d
        x=a[k][k];d*=x
        for i in range(k+1,n):
            f=a[i][k]/x
            for j in range(k+1,n):a[i][j]-=f*a[k][j]
    return d

def principal_psd(a):
    n=len(a)
    for size in range(1,n+1):
        for inds in combinations(range(n),size):
            if determinant([[a[i][j] for j in inds] for i in inds])<0:return False
    return True
psd_count=0
for n,values in [(2,range(-2,3)),(3,range(-1,2))]:
    positions=[(i,j) for i in range(n) for j in range(i,n)]
    for vector in product(values,repeat=len(positions)):
        a=[[F(0) for _ in range(n)] for _ in range(n)]
        for (i,j),v in zip(positions,vector):a[i][j]=a[j][i]=F(v)
        try:qv.psd(a);accepted=True
        except ValueError:accepted=False
        assert accepted==principal_psd(a),(a,accepted)
        psd_count+=1

rejections=[]
def reject(name, mutate):
    c=copy.deepcopy(certs[0]);mutate(c)
    try:qv.verify(c)
    except (ValueError,KeyError,ZeroDivisionError) as e:
        rejections.append({'name':name,'rejected':True,'reason':str(e)});return
    raise AssertionError(name+' was accepted')
reject('non-unit-trace signal',lambda c:c['states'][0][0].__setitem__(0,'2'))
reject('indefinite signal',lambda c:c['states'].__setitem__(0,[['1','1'],['1','0']]))
reject('asymmetric signal',lambda c:c['states'][1][0].__setitem__(1,'0'))
reject('incomplete POVM',lambda c:c['povm'][0][0].__setitem__(0,'4/5'))
reject('invalid probability weights',lambda c:c.__setitem__('dual_weights',['1','1']))
reject('infeasible dual matrix',lambda c:c.__setitem__('dual_matrix',[['0','0'],['0','0']]))
reject('overclaimed primal success',lambda c:c.__setitem__('success_lower','1'))
reject('floating-point input',lambda c:c.__setitem__('success_lower',0.9))
reject('Boolean input',lambda c:c.__setitem__('success_lower',True))

# Infinite Hilbert-space witness uses finitely supported rational vectors.
# These maps are restrictions of 1/2 times the unilateral shifts on l2(N0).
def native_step(x,action):
    if action==0:return {i+1:v/2 for i,v in x.items() if v}
    return {i-1:v/2 for i,v in x.items() if i>0 and v}
def native_output(x):return (x.get(0,F(0)),x.get(1,F(0)))
p=pred.parameters(2,2,1,'1/2','1/8')
assert p['K']==4 and p['tail_bound']==F(1,16)
x0={0:F(1)}
assert native_step(native_step(x0,0),1)=={0:F(1,4)}
assert native_step(native_step(x0,1),0)=={}
starts=[{i:F(s)} for i in range(10) for s in [-1,1]]
starts += [{0:F(3,5),1:F(4,5)},{0:F(-3,5),4:F(4,5)},
           {1:F(1,2),3:F(1,2),5:F(1,2),7:F(1,2)},{}]
checks=0;worst=F(0);max_prefix=F(0);max_tail=F(0)
for start in starts:
    assert sum(v*v for v in start.values())<=1
    for perturb in [False,True]:
        def profile(word):
            x=start
            for a in word:x=native_step(x,a)
            y=native_output(x)
            if perturb:
                err=p['oracle_coordinate_error_allowed']
                return tuple(v + (err if (sum(word)+j)%2 else -err) for j,v in enumerate(y))
            return y
        tree=pred.build(profile,p)
        stack=[((),start,tree)]
        while stack:
            word,x,q=stack.pop();truth=native_output(x);estimate=pred.output(q,p)
            err2=sum((a-b)**2 for a,b in zip(truth,estimate))
            assert err2<=(p['epsilon']/2)**2
            if len(word)<p['K']:
                assert err2<=p['dimension']*(p['h']/2+p['oracle_coordinate_error_allowed'])**2
                max_prefix=max(max_prefix,err2)
            else:
                assert q is None
                assert err2<=p['M']**2*p['L']**(2*len(word))
                max_tail=max(max_tail,err2)
            worst=max(worst,err2);checks+=1
            if len(word)<9:
                for a in range(2):stack.append((word+(a,),native_step(x,a),pred.update(q,a,p)))

predictor_rejections=[]
for name,args in [('noncontractive',(2,2,1,1,'1/8')),('negative decay',(2,2,1,'-1/2','1/8')),
                  ('zero accuracy',(2,2,1,'1/2',0)),('float decay',(2,2,1,0.5,'1/8')),
                  ('no actions',(0,2,1,'1/2','1/8'))]:
    try:pred.parameters(*args)
    except ValueError as e:predictor_rejections.append({'name':name,'rejected':True,'reason':str(e)})
    else:raise AssertionError(name)
for bad in [-1,2,True]:
    try:pred.update(None,bad,p)
    except ValueError as e:predictor_rejections.append({'name':f'invalid action {bad!r}','rejected':True,'reason':str(e)})
    else:raise AssertionError('bad action')
for m in [0,F(1,32)]:
    pp=pred.parameters(2,2,m,'1/2','1/8')
    assert pp['K']==0 and pred.build(lambda _:(_ for _ in ()).throw(AssertionError()),pp) is None
for a in [1,2,3]:
    pp=pred.parameters(a,1,1,0,'1/8');assert pp['K']==1

# The undecidability argument is a mathematical reduction, not a numerical test.
# Check only its finite witnesses and its half-gap arithmetic here.
for halt in [1,2,10,100]:
    sequence=[int(n>=halt) for n in range(halt+1)]
    assert min(sequence)==0 and max(sequence)==1
    assert max(abs(F(x)-F(1,2)) for x in sequence)==F(1,2)
assert F(1,5)<F(1,4)<F(3,10)
for file in OUT.glob('*.py'):ast.parse(file.read_text())
results={'all_passed':True,'quantum':{'certificate_count':len(qresults),'all_exact':True,'certificates':qresults,
 'independent_psd_comparisons':psd_count,'rejection_checks':rejections},
 'infinite_prediction':{'initial_states':len(starts),'oracle_modes':['exact','bounded rational perturbation'],
 'all_words_through_length':9,'trajectory_checks':checks,'worst_squared_error':str(worst),
 'largest_prefix_squared_error':str(max_prefix),'largest_tail_squared_error':str(max_tail),
 'parameters':pred.certificate(p),'noncommutation_verified':True,'rejection_checks':predictor_rejections,
 'universal_tail_evidence':'Analytic shift norm and coordinate-observation bounds in BM23-I1; finite replay is additional implementation evidence.'},
 'quantifier_elimination_executed':False,'undecidability_claim':'Proved by halting reduction, not by finite tests.'}
save('BM_Completion_Verification_2026-10-23.json',results)
print(json.dumps({'all_passed':True,'exact_quantum_certificates':len(qresults),'psd_oracle_comparisons':psd_count,
 'quantum_rejections':len(rejections),'trajectory_checks':checks,'predictor_rejections':len(predictor_rejections),
 'worst_squared_error':str(worst),'codebook_state_bound':p['codebook_state_bound']},indent=2))
