#!/usr/bin/env python3
"""Independently replay mathematical outcomes from the BM comparison bundle.

Uses exact integer/rational arithmetic for finite witnesses, interface families,
and linear bases. No SciPy or CLUE installation is needed for this replay.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from collections import deque
import json,math,sys


def rref(rows,n):
    a=[[F(v) for v in row] for row in rows];r=0
    for j in range(n):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];div=a[r][j];a[r]=[x/div for x in a[r]]
        for i in range(len(a)):
            if i==r or not a[i][j]:continue
            v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
    return a[:r]


def replay(root):
    bench=root/'comparison';d=json.loads((bench/'BM_Comparison_Results_2026-10-24.json').read_text())
    inputs=json.loads((bench/'BM_Comparison_Inputs_2026-10-24.json').read_text())
    native_witnesses=0
    for row in d['finite']:
        p=inputs['finite'][row['name']];n=len(p['states'])
        def obs(x):
            if x is None:return ('unavailable',)
            return ('available',tuple((type(p['tasks'][key][x]).__name__,p['tasks'][key][x]) for key in sorted(p['tasks'])))
        parents=list(range(n))
        def root(x):
            while parents[x]!=x:
                parents[x]=parents[parents[x]];x=parents[x]
            return x
        for x,y in combinations(range(n),2):
            todo=deque([(x,y)]);seen={(x,y)};distinguished=False
            while todo:
                xx,yy=todo.popleft()
                if obs(xx)!=obs(yy):distinguished=True;break
                for key,action in p['actions'].items():
                    a=None if xx is None else action[xx];b=None if yy is None else action[yy]
                    if (a,b) not in seen:seen.add((a,b));todo.append((a,b))
            if distinguished:native_witnesses+=1
            else:parents[root(x)]=root(y)
        assert len({root(x) for x in range(n)})==row['code_states']
    assert native_witnesses==d['summary']['native_witnesses_replayed']
    for row in d['interfaces']:
        p=inputs['interfaces'][row['name']];fam=row['native']['family']
        legal=p['legal'];tasks=p['task'];actions=p.get('actions',[])
        code=lambda x:tuple(fam[i][v] for i,v in enumerate(legal[x]))
        for x,y in combinations(range(len(legal)),2):
            if code(x)!=code(y):continue
            assert tasks[x]==tasks[y]
            for a in actions:
                xx,yy=a[x],a[y]
                assert (xx is None)==(yy is None)
                if xx is not None:assert code(xx)==code(yy)
        for f,bound in zip(fam,p.get('bounds',[[0]*n for n in p['sizes']])):
            assert all(f[x]!=f[y] or bound[x]==bound[y] for x,y in combinations(range(len(f)),2))
        cost=sum(F(w)*len(set(f)) for w,f in zip(p.get('weights',[1]*len(fam)),fam))
        assert str(cost)==row['bm_cost']==row['native']['cost']
    for row in d['linear']:
        p=inputs['linear'][row['name']];a=[[F(x) for x in z] for z in p['A']]
        l=[[F(x) for x in z] for z in p['L']];n=len(a);stack=[];layer=l
        for _ in range(n):
            stack.extend(layer)
            layer=[[sum(v[k]*a[k][j] for k in range(n)) for j in range(n)] for v in layer]
        assert rref(stack,n)==[[F(v) for v in z] for z in row['basis']]
        assert len(rref(stack,n))==row['bm_dimension']==row['clue_dimension']
    worst_gap=0.
    for row in d['robust']:
        theta,eta=row['theta'],row['eta'];c,s=abs(math.cos(theta)),abs(math.sin(theta))
        if eta>=c:
            v=(c,s);a=0.
        else:
            v=(eta,math.sqrt(1-eta*eta))
            a=c-s*eta/math.sqrt(1-eta*eta)
        assert v[0]<=eta+1e-12 and math.hypot(*v)<=1+1e-12
        lower=c*v[0]+s*v[1]
        upper=math.hypot(c-a,s)+eta*abs(a)
        gap=max(abs(lower-upper),abs(lower-row['bm_error']),abs(upper-row['optimal_recovery_error']))
        assert gap<1e-8
        worst_gap=max(worst_gap,gap)
    return {'status':'passed','finite_distinguishing_words':native_witnesses,
            'interface_families':len(d['interfaces']),'linear_bases':len(d['linear']),
            'scalar_primal_dual_certificates':len(d['robust']),'maximum_float_gap':worst_gap,
            'scope':'Independent replay of outputs; does not rerun CLUE or prove general optimality.'}


if __name__=='__main__':
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve();out=replay(root)
    (root/'BM_Comparison_Replay_2026-10-29.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
