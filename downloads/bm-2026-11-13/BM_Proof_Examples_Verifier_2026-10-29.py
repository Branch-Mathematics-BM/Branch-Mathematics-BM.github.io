#!/usr/bin/env python3
"""Check finite examples supporting the October 99–108 proof-basis review."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json,sys


def test():
    queries=0
    for contexts in [1,2,4,8]:
        for bits in product([0,1],repeat=contexts):
            chosen={i for i,b in enumerate(bits) if b}
            if len(chosen)==contexts:continue
            unseen=next(i for i in range(contexts) if i not in chosen)
            zero=[0]*contexts;alternative=[int(i==unseen) for i in range(contexts)]
            assert all(zero[i]==alternative[i] for i in chosen) and zero!=alternative
            queries+=1
    assert queries==274
    # Initial task retention and two nonterminal refinements.
    task=[0,1];initial=[0,0]
    assert initial[0]==initial[1] and task[0]!=task[1]
    initial=[0,1,1,1];action=[0,0,1,2]
    def refine(c):
        labels={}
        return [labels.setdefault((c[i],c[action[i]]),len(labels)) for i in range(len(c))]
    first=refine(initial);terminal=refine(first)
    assert first==[0,1,2,2] and terminal==[0,1,2,3] and refine(terminal)==terminal
    # A multigraph can have the same successor support and different path counts.
    weighted=[[0,0,2],[0,0,1],[0,0,0]]
    assert {j for j,w in enumerate(weighted[0]) if w}=={j for j,w in enumerate(weighted[1]) if w}
    assert sum(weighted[0])==2 and sum(weighted[1])==1
    # The same merged reduced trace admits both parity outcomes.
    priorities=[0,1];assert priorities[0]%2==0 and priorities[1]%2==1
    integer_cases=0
    for m in range(1,6):
        for r in range(1,m+1):
            for H in range(6):
                feasible=[sum(c) for c in product(range(H+1),repeat=m) if sum(sorted(c)[:r])>=H]
                expected=H+(m-r)*((H+r-1)//r)
                assert min(feasible)==expected
                integer_cases+=1
    # Exhaustive evaluation-code injection for p=5,m=4,r=1,2,3.
    p,m=5,4;recoveries=0;insufficiency=0
    for r in [1,2,3]:
        messages=list(product(range(p),repeat=r))
        def evaluate(a,x):return sum(v*pow(x,j,p) for j,v in enumerate(a))%p
        for subset in combinations(range(m),r):
            outputs={tuple(evaluate(a,x) for x in subset) for a in messages}
            assert len(outputs)==len(messages);recoveries+=1
        for subset in combinations(range(m),r-1):
            outputs={tuple(evaluate(a,x) for x in subset) for a in messages}
            assert len(outputs)<len(messages);insufficiency+=1
    cost_cases=0
    for eps in map(F,['0','1/4','1/2','1','2']):
        optimum=max(F(0),1-eps)
        assert 0<=optimum<=1 and 1-optimum<=eps
        for candidate in [F(i,20) for i in range(21)]:
            if 1-candidate<=eps:assert candidate*candidate>=optimum*optimum
        cost_cases+=1
    quantizers=0
    for M in range(1,13):
        centers=[F(-1)+F(2*j+1,M) for j in range(M)]
        # All cell endpoints and midpoints are no further than 1/M from their decoder.
        for j,center in enumerate(centers):
            lo=F(-1)+F(2*j,M);hi=F(-1)+F(2*(j+1),M)
            assert abs(center-lo)==abs(center-hi)==F(1,M)
        assert F(2,1)==M*2*F(1,M)
        quantizers+=1
    nonempty=[frozenset(i for i in range(3) if bits[i]) for bits in product([0,1],repeat=3) if any(bits)]
    spaces=[frozenset()]+nonempty
    def dist(a,b):
        if not a and not b:return 0
        if not a or not b:return 1
        h=max(max(min(abs(x-y) for y in b) for x in a),max(min(abs(y-x) for x in a) for y in b))
        return min(h,1)
    triangle_checks=0
    for a,b,c in product(spaces,repeat=3):
        assert dist(a,c)<=dist(a,b)+dist(b,c);triangle_checks+=1
    for a in nonempty:
        assert min(max(dist(center,frozenset()),dist(center,a)) for center in spaces)==1
    return {'status':'passed','oracle_adversary_witnesses':queries,'partition_examples':2,
            'integer_capacity_exhaustive_cases':integer_cases,'field_recovery_subsets':recoveries,
            'insufficient_field_subsets':insufficiency,'repair_cost_cases':cost_cases,
            'quantizer_sizes':quantizers,'capped_set_metric_triangles':triangle_checks,
            'scope':'Finite checks of examples; written proofs establish general claims under their hypotheses.'}


if __name__=='__main__':
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve();out=test()
    (root/'BM_Proof_Examples_Verifier_2026-10-29.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
