"""Verify the supplied Jordan bound with exact rational arithmetic only.

Usage: python BM_Jordan_Exact_Verifier_2026-10-21.py CERTIFICATE.json
No numerical optimization library is needed. The certificate is a rational
Gram matrix; this program verifies its polynomial identity and an exact LDL
decomposition with strictly positive pivots.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json

N=5
ZERO=(0,)*N
def mono(*indices):
    return tuple(indices.count(i) for i in range(N))
def add(*polys):
    result=defaultdict(F)
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent]+=coefficient
    return {e:c for e,c in result.items() if c}
def mul(left,right):
    result=defaultdict(F)
    for e,c in left.items():
        for f,d in right.items():
            result[tuple(x+y for x,y in zip(e,f))]+=c*d
    return {e:c for e,c in result.items() if c}
def scale(value,poly):
    return {e:value*c for e,c in poly.items() if value*c}
def lie(poly):
    """Lie derivative for a'=b, b'=c, c'=d, d'=e'=0."""
    result=defaultdict(F)
    for exponent,c in poly.items():
        for i in range(3):
            if exponent[i]:
                new=list(exponent);new[i]-=1;new[i+1]+=1
                result[tuple(new)]+=c*exponent[i]
    return {e:c for e,c in result.items() if c}

def positive_ldl(matrix):
    n=len(matrix)
    if any(len(row)!=n for row in matrix):
        raise ValueError('Gram matrix is not square')
    if any(matrix[i][j]!=matrix[j][i] for i in range(n) for j in range(n)):
        raise ValueError('Gram matrix is not symmetric')
    lower=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    pivots=[]
    for j in range(n):
        pivot=matrix[j][j]-sum(lower[j][k]**2*pivots[k] for k in range(j))
        if pivot<=0:
            raise ValueError('Nonpositive exact LDL pivot at '+str(j))
        pivots.append(pivot)
        for i in range(j+1,n):
            lower[i][j]=(matrix[i][j]-sum(lower[i][k]*lower[j][k]*pivots[k] for k in range(j)))/pivot
    # Check the decomposition independently of the recurrence.
    if any(matrix[i][j]!=sum(lower[i][k]*pivots[k]*lower[j][k] for k in range(n)) for i in range(n) for j in range(n)):
        raise ValueError('LDL reconstruction failed')
    return pivots

def verify(data):
    bound=F(data['bound_squared'])
    theta=list(map(F,data['encoder_coefficients']))
    if bound!=F(12949,10000) or theta!=[F(1969,10000),F(8757,10000),F(-7014,10000),F(159,10000)]:
        raise ValueError('Certificate does not match the stated encoder and bound')
    if data['decoder']!='(1+t/2)*z' or data['gram_variables']!=['a','b','c','d','e']:
        raise ValueError('Unexpected decoder or variable convention')
    basis=[tuple(e) for e in data['gram_monomials']]
    expected=[mono(*indices) for indices in combinations_with_replacement(range(N),3)]
    if basis!=expected:raise ValueError('Unexpected monomial basis')
    denominator=int(data['gram_denominator'])
    if denominator<=0:raise ValueError('Denominator must be positive')
    gram=[[F(int(x),denominator) for x in row] for row in data['gram_numerators']]
    if len(gram)!=35 or any(len(row)!=35 for row in gram):raise ValueError('Wrong Gram shape')

    norm={mono(i,i):F(1) for i in range(N)}
    invariant_i={mono(2,2,2):F(1),mono(1,2,3):F(-3),mono(0,3,3):F(3)}
    invariant_q={mono(2,2):F(1),mono(1,3):F(-2)}
    actual_encoder=add({mono(3):theta[0]},scale(theta[1],invariant_i),scale(theta[2],mul({mono(3):F(1)},invariant_q)),{mono(3,3,3):theta[3]})
    if lie(invariant_i) or lie(invariant_q) or lie(actual_encoder):
        raise ValueError('Encoder is not an exact first integral')
    homogeneous_encoder=add(scale(theta[0],mul({mono(3):F(1)},norm)),scale(theta[1],invariant_i),scale(theta[2],mul({mono(3):F(1)},invariant_q)),{mono(3,3,3):theta[3]})
    # Integrate (a+b*t+c*t^2/2+d*t^3/6 - (1+t/2)*R)^2.
    G=[[F(1,factorial(i)*factorial(j)*(i+j+1)) for j in range(4)] for i in range(4)]
    energy=add(*[{mono(i,j):G[i][j]} for i in range(4) for j in range(4)])
    cross={mono(i):G[i][0]+G[i][1]/2 for i in range(4)}
    decoder_energy=G[0][0]+G[0][1]+G[1][1]/4
    target=add(scale(bound,mul(mul(norm,norm),norm)),scale(-1,mul(energy,mul(norm,norm))),scale(2,mul(mul(homogeneous_encoder,cross),norm)),scale(-decoder_energy,mul(homogeneous_encoder,homogeneous_encoder)))
    represented=add(*[{tuple(x+y for x,y in zip(basis[i],basis[j])):gram[i][j]} for i in range(35) for j in range(35)])
    if represented!=target:raise ValueError('Exact polynomial coefficient identity failed')
    pivots=positive_ldl(gram)
    vector=[87,47,16]
    linear_rayleigh=sum(F(vector[i]*vector[j],factorial(i)*factorial(j)*(i+j+1)) for i in range(3) for j in range(3))/sum(x*x for x in vector)
    if not linear_rayleigh>bound:raise ValueError('Strict comparison with the linear optimum failed')
    return {'verified':True,'arithmetic':'exact fractions; no floating-point acceptance test','gram_dimension':35,
            'polynomial_coefficients_checked':len({tuple(x+y for x,y in zip(a,b)) for a in basis for b in basis}),
            'positive_ldl_pivots':len(pivots),'ldl_reconstruction_checked':True,
            'encoder_lie_derivative_zero':True,'bound_squared':str(bound),
            'linear_rayleigh_lower_bound':str(linear_rayleigh),
            'squared_improvement_at_least':str(linear_rayleigh-bound)}

def verify_family_lower(data):
    states=[list(map(F,x)) for x in data['states']]
    weights=list(map(F,data['weights']))
    if len(states)!=2 or len(weights)!=2 or any(len(x)!=4 for x in states):
        raise ValueError('Expected two four-dimensional states')
    if any(w<=0 for w in weights) or sum(weights)!=1:
        raise ValueError('Weights are not a positive probability vector')
    if any(sum(v*v for v in x)!=1 or x[3]!=0 for x in states):
        raise ValueError('Lower-certificate states must lie on the unit sphere with d=0')
    G=[[F(1,factorial(i)*factorial(j)*(i+j+1)) for j in range(4)] for i in range(4)]
    k=[G[i][0]+G[i][1]/2 for i in range(4)]
    norm_v=F(19,12)
    aa=sum(w*norm_v*x[2]**6 for w,x in zip(weights,states))
    bb=sum(w*x[2]**3*sum(k[i]*x[i] for i in range(4)) for w,x in zip(weights,states))
    cc=sum(w*sum(x[i]*G[i][j]*x[j] for i in range(4) for j in range(4)) for w,x in zip(weights,states))
    if aa<=0:raise ValueError('Weighted quadratic must be strictly convex')
    exact=cc-bb*bb/aa
    if exact!=F(data['exact_weighted_minimum']) or bb/aa!=F(data['quadratic_minimizer']):
        raise ValueError('Weighted minimum or minimizer mismatch')
    lower=F(data['lower_bound_squared'])
    if lower!=F(3237,2500) or exact<=lower:
        raise ValueError('Claimed lower bound is not certified')
    return {'verified':True,'arithmetic':'exact fractions',
            'scope':'invariant polynomials of degree at most three; fixed decoder (1+t/2)*z',
            'antipodal_state_pairs':2,'unit_sphere_identities_checked':2,
            'positive_weights_sum_to_one':True,'lower_bound_squared':str(lower),
            'exact_weighted_minimum':str(exact),
            'certified_family_squared_gap':str(F(12949,10000)-lower)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--family-lower',type=Path)
    args=parser.parse_args()
    raw=args.certificate.read_bytes();result=verify(json.loads(raw))
    result['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    if args.family_lower:
        family_raw=args.family_lower.read_bytes()
        result['family_lower']=verify_family_lower(json.loads(family_raw))
        result['family_lower']['certificate_sha256']=hashlib.sha256(family_raw).hexdigest()
    text=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
if __name__=='__main__':main()
