#!/usr/bin/env python3
"""Finite BM tree-network and seed examples, with independently checked outputs.

Python 3.10+ standard library. Run with the output directory as the only argument.
These are model-dependent mathematical examples, not experimental physics.
"""
from collections import Counter, deque
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json
import math
import random
import sys


def encode(x):
    return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',',':'))


def validate(problem):
    if set(problem) != {'variables','frames'}:
        raise ValueError('expected variables and frames')
    variables,frames=problem['variables'],problem['frames']
    if not isinstance(variables,dict) or not variables or len(variables)>12:
        raise ValueError('1..12 finite variables required')
    for name,domain in variables.items():
        if not isinstance(name,str) or not name or not isinstance(domain,list) or not 1<=len(domain)<=16:
            raise ValueError('invalid variable or domain')
        if any(type(x) not in (str,int,bool,type(None)) for x in domain):
            raise ValueError('domains must contain exact JSON scalars')
        if len({encode(x) for x in domain})!=len(domain):
            raise ValueError('duplicate domain label')
    if math.prod(map(len,variables.values()))>1000000:
        raise ValueError('reference implementation limit: at most 1,000,000 assignments')
    if not isinstance(frames,list) or len(frames)>40:
        raise ValueError('at most 40 frames required')
    seen=set()
    for f in frames:
        if not isinstance(f,dict) or set(f)!={'id','scope','allowed'}:
            raise ValueError('frame needs id, scope and allowed')
        ident,scope,allowed=f['id'],f['scope'],f['allowed']
        if not isinstance(ident,str) or not ident or ident in seen:
            raise ValueError('frame identifiers must be unique')
        seen.add(ident)
        if not isinstance(scope,list) or any(x not in variables for x in scope) or len(set(scope))!=len(scope):
            raise ValueError('scope must name distinct existing variables')
        if not isinstance(allowed,list):raise ValueError('allowed must be a list')
        for row in allowed:
            if not isinstance(row,list) or len(row)!=len(scope):raise ValueError('bad relation tuple')
            if any(encode(v) not in {encode(x) for x in variables[name]} for name,v in zip(scope,row)):
                raise ValueError('relation value outside domain')
        if len({encode(row) for row in allowed})!=len(allowed):raise ValueError('duplicate relation tuple')
    return problem


def enumerate_completions(problem):
    """Backtracking with safe pruning; assignments represented in variable order."""
    validate(problem)
    names=list(problem['variables']); frames=problem['frames']
    allowed={f['id']:{encode(row) for row in f['allowed']} for f in frames}
    current={};out=[]
    def visit(i):
        for f in frames:
            if all(v in current for v in f['scope']):
                if encode([current[v] for v in f['scope']]) not in allowed[f['id']]:return
        if i==len(names):
            out.append([current[n] for n in names]);return
        name=names[i]
        for value in problem['variables'][name]:
            current[name]=value;visit(i+1)
        current.pop(name,None)
    visit(0)
    return out


def brute_completions(problem):
    """Independent full-product oracle; no shared pruning or completion routine."""
    names=list(problem['variables']);out=[]
    for values in product(*(problem['variables'][k] for k in names)):
        assignment=dict(zip(names,values))
        if all(any(encode(row)==encode([assignment[n] for n in f['scope']]) for row in f['allowed'])
               for f in problem['frames']):out.append(list(values))
    return out


def projection(frame, variables):
    indexes=[frame['scope'].index(v) for v in variables]
    return {encode([row[i] for i in indexes]) for row in frame['allowed']}


def graph_components(nodes,edges):
    adj={n:set() for n in nodes}
    for a,b in edges:
        if a not in adj or b not in adj or a==b:raise ValueError('invalid edge')
        adj[a].add(b);adj[b].add(a)
    if len({tuple(sorted(e)) for e in edges})!=len(edges):raise ValueError('duplicate edge')
    components=0;seen=set()
    for x in nodes:
        if x in seen:continue
        components+=1;todo=[x];seen.add(x)
        while todo:
            for y in adj[todo.pop()]:
                if y not in seen:seen.add(y);todo.append(y)
    return components


def join_tree_report(problem,edges):
    """Verify the sufficient running-intersection/equal-projection contract."""
    validate(problem)
    fs={f['id']:f for f in problem['frames']};ids=list(fs)
    if not ids or len(edges)!=len(ids)-1 or graph_components(ids,edges)!=1:
        raise ValueError('frame edges must form a nonempty tree')
    adj={i:set() for i in ids}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    running=True
    for v in problem['variables']:
        containing={i for i in ids if v in fs[i]['scope']}
        if not containing:continue
        start=next(iter(containing));reached={start};todo=[start]
        while todo:
            for n in adj[todo.pop()] & containing:
                if n not in reached:reached.add(n);todo.append(n)
        running &= reached==containing
    edge_checks=[]
    order=list(problem['variables'])
    for a,b in edges:
        overlap=[v for v in order if v in fs[a]['scope'] and v in fs[b]['scope']]
        edge_checks.append({'edge':[a,b],'overlap':overlap,
                            'equal_projections':projection(fs[a],overlap)==projection(fs[b],overlap)})
    return {'running_intersection':running,'all_relations_nonempty':all(f['allowed'] for f in fs.values()),
            'edges':edge_checks,'sufficient_condition':bool(running and all(f['allowed'] for f in fs.values())
                                                             and all(e['equal_projections'] for e in edge_checks))}


def seed_field(contributions, threshold, site_edges):
    if not contributions:raise ValueError('supply a nonempty seed catalogue')
    sites=tuple(contributions[0]['weights'])
    if any(tuple(s['weights'])!=sites for s in contributions):raise ValueError('same ordered sites required')
    if len({s['id'] for s in contributions})!=len(contributions):raise ValueError('duplicate seed id')
    values={site:sum((Q(s['weights'][site]) for s in contributions),Q()) for site in sites}
    if any(Q(w)<0 for s in contributions for w in s['weights'].values()):raise ValueError('negative weight')
    active={x for x in sites if values[x]>=Q(threshold)}
    edges=[list(e) for e in site_edges if e[0] in active and e[1] in active]
    components=graph_components(sorted(active),edges)
    return {'contributions':{k:str(v) for k,v in values.items()},'active_sites':sorted(active),
            'active_edges':edges,'components':components,'cycle_rank':len(edges)-len(active)+components,
            'seed_to_seed_edges':[],'threshold':str(Q(threshold))}


def exact_accumulation(rho,u,s0,t):
    rho,u,s0=map(Q,(rho,u,s0))
    if not 0<=rho<=1 or u<0 or s0<0 or not isinstance(t,int) or t<0:
        raise ValueError('requires 0<=rho<=1, nonnegative inputs and integer time')
    return rho**t*s0+sum((rho**(t-1-j)*u for j in range(t)),Q())


def tests():
    rng=random.Random(20261029);tree_cases=0;tree_extensions=0
    for _ in range(250):
        bags=rng.randrange(2,6); names=[f'x{i}' for i in range(bags+1)]
        all_assignments=list(product([0,1],repeat=bags+1))
        sample=rng.sample(all_assignments,rng.randrange(1,len(all_assignments)+1))
        frames=[]
        for i in range(bags):
            pairs=sorted({(v[i],v[i+1]) for v in sample})
            frames.append({'id':f'f{i}','scope':[names[i],names[i+1]],'allowed':[list(x) for x in pairs]})
        p={'variables':{n:[0,1] for n in names},'frames':frames}
        edges=[[f'f{i}',f'f{i+1}'] for i in range(bags-1)]
        check=join_tree_report(p,edges);assert check['sufficient_condition']
        found=enumerate_completions(p);assert found==brute_completions(p) and found
        for f in frames:
            ids=[names.index(n) for n in f['scope']]
            actual={encode([r[i] for i in ids]) for r in found}
            assert actual=={encode(row) for row in f['allowed']}
            tree_extensions+=len(f['allowed'])
        tree_cases+=1
    parity={'satisfiable':0,'unsatisfiable':0,'edge_deletion_checks':0}
    for bits in product([0,1],repeat=3):
        frames=[]
        for i,(a,b) in enumerate([('a','b'),('b','c'),('a','c')]):
            frames.append({'id':str(i),'scope':[a,b],
                           'allowed':[[x,y] for x,y in product([0,1],repeat=2) if (x^y)==bits[i]]})
        p={'variables':{x:[0,1] for x in ['a','b','c']},'frames':frames}
        got=enumerate_completions(p);assert got==brute_completions(p)
        assert all(projection(f,[v])=={'[0]','[1]'} for f in frames for v in f['scope'])
        if got:parity['satisfiable']+=1
        else:
            parity['unsatisfiable']+=1
            for k in range(3):
                reduced={'variables':p['variables'],'frames':[f for i,f in enumerate(frames) if i!=k]}
                assert enumerate_completions(reduced);parity['edge_deletion_checks']+=1
    assert parity=={'satisfiable':4,'unsatisfiable':4,'edge_deletion_checks':12}
    # Positive additive monoid K={0,2,3,...}: equal total weight is not a joint witness.
    k_values=[0,2,3,4,5,6]
    row_options=[(a,b) for a,b in product(k_values,repeat=2) if a+b==2]
    annotated_candidates=list(product(row_options,repeat=3))
    annotated_joint=[m for m in annotated_candidates if sum(row[0] for row in m)==3
                     and sum(row[1] for row in m)==3]
    assert len(row_options)==2 and len(annotated_candidates)==8 and not annotated_joint
    standard_joint=[[1,1],[1,1],[1,1]]
    assert [sum(row) for row in standard_joint]==[2,2,2]
    assert [sum(row[j] for row in standard_joint) for j in range(2)]==[3,3]
    accumulation_checks=0;crossings=0
    for rho,u,s0 in product([Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)],
                            [Q(0),Q(1,4),Q(1,2),Q(1)], [Q(0),Q(1,2),Q(1)]):
        value=s0
        for t in range(13):
            assert value==exact_accumulation(rho,u,s0,t)
            value=rho*value+u;accumulation_checks+=1
        if 0<rho<1:
            limit=u/(1-rho)
            if s0<limit:
                threshold=(s0+limit)/2
                exact=next(t for t in range(101) if exact_accumulation(rho,u,s0,t)>=threshold)
                ratio=(limit-threshold)/(limit-s0)
                assert rho**exact<=ratio and (exact==0 or rho**(exact-1)>ratio)
                assert all(exact_accumulation(rho,u,s0,t)<limit for t in range(40))
                crossings+=1
    edges=[['A','B'],['B','C'],['C','D'],['D','A']]
    def seedset(rows):return [{'id':f'seed{i+1}','weights':dict(zip(['A','B','C','D'],map(str,row)))} for i,row in enumerate(rows)]
    path=seed_field(seedset([[2,1,0,0],[0,1,1,0],[1,1,1,0]]),2,edges)
    cycle=seed_field(seedset([[1,1,1,0],[1,0,0,1],[0,1,1,1]]),2,edges)
    assert (path['active_sites'],path['cycle_rank'])==(['A','B','C'],0)
    assert (cycle['active_sites'],cycle['cycle_rank'])==(['A','B','C','D'],1)
    assert sum(Q(x) for x in path['contributions'].values())==sum(Q(x) for x in cycle['contributions'].values())==8
    # Two subthreshold readings with a common update force different subsequent outputs.
    x,y,rho,u,threshold=Q(3,5),Q(9,10),Q(1,2),Q(3,5),Q(1)
    assert x<threshold and y<threshold and rho*x+u<threshold<=rho*y+u
    negative=0
    valid={'variables':{'a':[0,1]},'frames':[{'id':'f','scope':['a'],'allowed':[[0],[1]]}]}
    bad=[{'variables':{'a':[]},'frames':[]},
         {'variables':{'a':[0,0]},'frames':[]},
         {'variables':{'a':[0,1]},'frames':[{'id':'f','scope':['a'],'allowed':[[2]]}]},
         {'variables':{'a':[0,1]},'frames':[{'id':'f','scope':['a'],'allowed':[[0],[0]]}]}]
    validate(valid)
    for problem in bad:
        try:validate(problem)
        except ValueError:negative+=1
        else:raise AssertionError('malformed example accepted')
    return {'join_tree':{'random_models':tree_cases,'local_tuples_with_global_extensions':tree_extensions},
            'cycle_parity':parity,'recurrence':{'exact_equalities':accumulation_checks,'finite_crossing_checks':crossings},
            'annotated_counterexample':{'coefficient_monoid':'{0} union {integers >= 2}',
                'left_masses':[2,2,2],'right_masses':[3,3],'both_total':6,
                'row_valid_matrices_checked':len(annotated_candidates),'joint_matrices':len(annotated_joint),
                'ordinary_nonnegative_integer_joint':standard_joint},
            'spatial_example':{'path':path,'cycle':cycle},
            'coarse_memory_witness':{'current_values':[str(x),str(y)],'current_outputs':[0,0],
                                      'next_values':[str(rho*x+u),str(rho*y+u)],'next_outputs':[0,1]},
            'malformed_inputs_rejected':negative}


def main():
    out=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve();out.mkdir(parents=True,exist_ok=True)
    d={'date':'2026-10-29','status':'passed','scope':'finite declared mathematical models; internal checks only',
       'tests':tests()}
    (out/'BM_Network_Seed_Results_2026-10-29.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(d,indent=2))


if __name__=='__main__':main()
