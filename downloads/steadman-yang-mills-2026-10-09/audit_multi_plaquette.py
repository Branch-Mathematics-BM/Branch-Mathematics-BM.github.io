"""Read-only exact witness audit; --attach-witnesses exports rounded witnesses.

--check-trees independently repeats the exact matrix integrals using another
spanning tree for the patch and cube. No floating eigenvalue decisions.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from multi_plaquette import (geometry, check_complete_low_sector, exact_matrices,
                             inertia, su2_matrix, pair)

BASE=Path(__file__).resolve().parent


def schur_count(a,g,d,x):
    assert x<d
    m=[[a[i][j]-g[i][j]/(d-x) for j in range(len(a))] for i in range(len(a))]
    return inertia(m,x)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--attach-witnesses',action='store_true')
    parser.add_argument('--check-trees',action='store_true')
    args=parser.parse_args()
    checked=0;trees=[];floor_gain=[]
    for name in ('single','strip','patch','cube'):
        raw=json.loads((BASE/(name+'_matrices.json')).read_text())
        g=geometry(tuple(raw['geometry']['lengths']))
        check_complete_low_sector(g)
        w=[[F(x) for x in row] for row in raw['W']]
        gram0=[[F(x) for x in row] for row in raw['gram_B_over_beta_squared']]
        if args.check_trees and name in ('patch','cube'):
            other=geometry(tuple(raw['geometry']['lengths']),reverse_tree=True)
            assert g['tree']!=other['tree']
            wo,go,qa=exact_matrices(other)
            assert wo==w and go==gram0
            trees.append(name)
            print(name,'alternate-tree exact matrices match',flush=True)
        path=BASE/(name+'_certificates.json')
        records=json.loads(path.read_text())
        for row in records['cases']:
            beta=F(row['beta']);np_=len(g['faces']);dim=len(w)
            a=[[-beta*w[i][j]+(g['energies'][i] if i==j else 0)
                for j in range(dim)] for i in range(dim)]
            gram=[[beta*beta*x for x in rr] for rr in gram0]
            loc=row['local_floor_certificate']
            if loc['type']=='global potential norm':
                d=F(24)-abs(beta)*np_
            else:
                t=F(loc['t']);alpha=F(loc['alpha']); elow=F(loc['local_ground_lower'])
                assert alpha==t/g['max_plaquettes_per_link']
                local_beta=F(loc['local_beta'])
                assert local_beta==abs(beta)/alpha
                la,ld,lb,lg=su2_matrix(local_beta,loc['local_cutoff'])
                assert schur_count(la,lg,ld,elow)==0
                d=(1-t)*24+np_*alpha*elow
            if not row.get('certified'):
                continue
            witness=row.get('witness')
            if witness is None:
                assert args.attach_witnesses
                witness={'tail_floor':str(d),
                         'ground_ritz_lower':row['ritz_ground'][0],
                         'ground_ritz_upper':row['ritz_ground'][1],
                         'first_ritz_lower':row['ritz_first'][0],
                         'first_ritz_upper':row['ritz_first'][1],
                         'ground_schur_lower':row['ground_interval'][0],
                         'first_schur_lower':row['first_interval'][0]}
                row['witness']=witness
            assert F(witness['tail_floor'])==d
            a0l=F(witness['ground_ritz_lower']);a0u=F(witness['ground_ritz_upper'])
            a1l=F(witness['first_ritz_lower']);a1u=F(witness['first_ritz_upper'])
            l0=F(witness['ground_schur_lower']);l1=F(witness['first_schur_lower'])
            assert inertia(a,a0l)==0 and inertia(a,a0u)>=1
            assert inertia(a,a1l)<=1 and inertia(a,a1u)>=2
            assert schur_count(a,gram,d,l0)==0
            assert schur_count(a,gram,d,l1)<=1
            assert l1-a0u>0
            certified=pair(l1-a0u,a1u-l0)
            if args.attach_witnesses:
                row['gap_interval']=certified
            else:
                assert F(row['gap_interval'][0])<=l1-a0u
                assert F(row['gap_interval'][1])>=a1u-l0
            if d>24-abs(beta)*np_:
                floor_gain.append((name,str(beta)))
            checked+=1
        if args.attach_witnesses:
            path.write_text(json.dumps(records,indent=2)+'\n')
        print(name,'all exact spectral and local-floor witnesses passed',flush=True)
    result={'exact_certificates_checked':checked,'alternate_tree_matches':trees,
            'local_tail_improved_cases':len(floor_gain),
            'status':'All requested exact audits passed.'}
    print(json.dumps(result),flush=True)
    if args.check_trees:
        (BASE/'audit_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
