"""Exact Jordan long-return bridges, for every positive chain length.

Input JSON: {"n":4,"start_head":[1,2],"end_head":[-1,3],"tau":"10"}.
For even n=2m, both heads have m entries. For odd n=2m+1,
start_head has m+1 entries, end_head has m; the remaining endpoint
middle coordinate converges to (-1)^m times the initial middle coordinate.

Numbers must be integers or exact rational strings. Run --verify for exact
Laurent-polynomial checks; negative powers certify convergence at infinity.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import json
import random

def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,str,F)):
        raise ValueError('Use an integer or rational string, not a floating-point number')
    return F(value)
def clean(poly):return {e:c for e,c in poly.items() if c}
def add(*polys):
    result={}
    for poly in polys:
        for e,c in poly.items():result[e]=result.get(e,F(0))+c
    return clean(result)
def scale(c,poly):return clean({e:c*v for e,v in poly.items()})
def shift(poly,power):return {e+power:c for e,c in poly.items()}
def solve(matrix,rhs):
    n=len(matrix);a=[list(row) for row in matrix];b=[dict(poly) for poly in rhs]
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:raise ValueError('Singular Hermite matrix')
        a[k],a[pivot]=a[pivot],a[k];b[k],b[pivot]=b[pivot],b[k]
        q=a[k][k];a[k]=[v/q for v in a[k]];b[k]=scale(1/q,b[k])
        for i in range(n):
            if i!=k and a[i][k]:
                q=a[i][k];a[i]=[u-q*v for u,v in zip(a[i],a[k])]
                b[i]=add(b[i],scale(-q,b[k]))
    return b
def bridge_laurent(n,start_head,end_head):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:raise ValueError('n must be a positive integer')
    m=n//2;head=m+n%2
    if len(start_head)!=head or len(end_head)!=m:raise ValueError('Wrong endpoint-head lengths')
    u=list(map(rational,start_head));v=list(map(rational,end_head))
    right=[]
    for k in range(m):
        right.append(add({k:v[k]},*[{j:-u[j]/factorial(j-k)} for j in range(k,head)]))
    matrix=[[F(1,factorial(j-k)) for j in range(head,n)] for k in range(m)]
    scaled_tail=solve(matrix,right)
    source=[clean({0:value}) for value in u]+[shift(poly,-j) for j,poly in zip(range(head,n),scaled_tail)]
    endpoint=[add(*[scale(F(1,factorial(j-k)),shift(source[j],j-k)) for j in range(k,n)]) for k in range(n)]
    start_limit=u+[F(0)]*(n-head)
    end_limit=v+([(-1)**m*u[-1]] if n%2 else [])+[F(0)]*(n-head)
    for actual,limit in zip(source+endpoint,start_limit+end_limit):
        if any(e>0 for e in actual) or actual.get(0,F(0))!=limit:
            raise AssertionError('Endpoint-limit coefficient identity failed')
    for k in range(m):
        if endpoint[k]!=clean({0:v[k]}):raise AssertionError('Prescribed endpoint derivative mismatch')
    return source,endpoint,start_limit,end_limit
def evaluate(poly,tau):return sum((c*tau**e for e,c in poly.items()),F(0))
def bridge(n,start_head,end_head,tau):
    tau=rational(tau)
    if not tau:raise ValueError('tau must be nonzero')
    source,endpoint,sl,el=bridge_laurent(n,start_head,end_head)
    serialize=lambda polys:[{str(e):str(c) for e,c in sorted(p.items())} for p in polys]
    return {'n':n,'tau':str(tau),'source':[str(evaluate(p,tau)) for p in source],
            'endpoint':[str(evaluate(p,tau)) for p in endpoint],
            'source_limit':[str(v) for v in sl],'endpoint_limit':[str(v) for v in el],
            'source_laurent':serialize(source),'endpoint_laurent':serialize(endpoint)}
def verify_implementation():
    rng=random.Random(20261021);families=0;numeric=0
    for n in range(1,13):
        m=n//2;head=m+n%2
        for _ in range(4):
            u=[F(rng.randint(-4,4),rng.randint(1,4)) for _ in range(head)]
            v=[F(rng.randint(-4,4),rng.randint(1,4)) for _ in range(m)]
            source,endpoint,sl,el=bridge_laurent(n,u,v);families+=1
            reverse_source,reverse_endpoint,rsl,rel=bridge_laurent(n,el[:head],sl[:m])
            if rsl!=el or rel!=sl:raise AssertionError('Reverse limiting bridge failed')
            for tau in [F(-7),F(-2),F(-1),F(1),F(2),F(7)]:
                x=[evaluate(p,tau) for p in source]
                y=[sum((x[j]*tau**(j-k)/factorial(j-k) for j in range(k,n)),F(0)) for k in range(n)]
                if y!=[evaluate(p,tau) for p in endpoint]:raise AssertionError('Jordan flow check failed')
                numeric+=1
    return {'verified':True,'arithmetic':'exact fractions and Laurent polynomials',
            'chain_lengths':list(range(1,13)),'symbolic_families':families,
            'reverse_families':families,'evaluated_flow_identities':numeric,
            'no_positive_laurent_powers':True,'limiting_coefficients_checked':True,
            'scope':'finite implementation checks; all-n theorem proved in BM21-J1'}
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',nargs='?',type=Path)
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.verify:result=verify_implementation()
    elif args.input:
        request=json.loads(args.input.read_text());result=bridge(**request)
    else:parser.error('Supply an input JSON file or --verify')
    text=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
if __name__=='__main__':main()
