"""Exact low-electric-energy SU(2) assembler on small open cubic graphs.

The finite tetrahedral subgroup is used ONLY as a proved degree-four Haar
cubature, not as a replacement gauge group. All matrix entries and spectral
certificates are rational. NumPy integer arrays accelerate finite sums.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import argparse
import json
import time
import numpy as np
from single_plaquette_certificates import (inertia, eigen_interval,
    schur_lower_interval, su2_matrix, pair)

BASE = Path(__file__).resolve().parent


def geometry(lengths, reverse_tree=False):
    vertices = list(product(*(range(n+1) for n in lengths)))
    vid = {v:i for i,v in enumerate(vertices)}
    edges = []
    for v in vertices:
        for axis in range(3):
            if v[axis] < lengths[axis]:
                w = list(v); w[axis] += 1
                edges.append(tuple(sorted((vid[v], vid[tuple(w)]))))
    edges = sorted(set(edges))
    index = {e:i for i,e in enumerate(edges)}
    faces = []
    for v in vertices:
        for a,b in combinations(range(3),2):
            if v[a] < lengths[a] and v[b] < lengths[b]:
                va=list(v); va[a]+=1
                vb=list(v); vb[b]+=1
                vab=list(va); vab[b]+=1
                faces.append(tuple(vid[tuple(x)] for x in (v,va,vab,vb)))
    adj = [[] for _ in vertices]
    for i,(u,v) in enumerate(edges):
        adj[u].append((v,i)); adj[v].append((u,i))
    cycles=[]
    for start in range(len(vertices)):
        def dfs(path):
            for nxt,e in adj[path[-1]]:
                if nxt == start:
                    if len(path) in (4,6) and path[1] < path[-1]:
                        cycles.append(tuple(path))
                elif nxt > start and nxt not in path and len(path)<6:
                    dfs(path+[nxt])
        dfs([start])
    def edgeword(cycle):
        return tuple((index[tuple(sorted((u,v)))]+1)*(1 if u<v else -1)
                     for u,v in zip(cycle,cycle[1:]+cycle[:1]))
    def mask(word):
        return sum(1<<(abs(e)-1) for e in word)
    cycles=sorted(cycles,key=lambda c:(len(c),mask(edgeword(c))))
    words=[edgeword(c) for c in cycles]
    masks=[0]+[mask(w) for w in words]
    assert len(set(masks))==len(masks)
    face_words=[edgeword(c) for c in faces]
    face_masks=[mask(w) for w in face_words]
    degrees=[sum(abs(e)-1==i for w in face_words for e in w) for i in range(len(edges))]
    # A spanning tree serves integration only. K is kept in the original link metric.
    visited={0}; tree=set(); frontier=[0]
    while frontier:
        u=frontier.pop(0)
        for v,e in (list(reversed(adj[u])) if reverse_tree else adj[u]):
            if v not in visited:
                visited.add(v); tree.add(e); frontier.append(v)
    chords=[e for e in range(len(edges)) if e not in tree]
    chord_index={e:i for i,e in enumerate(chords)}
    def chordword(word):
        return tuple((chord_index[abs(e)-1]+1)*(1 if e>0 else -1)
                     for e in word if abs(e)-1 in chord_index)
    return {'lengths':lengths, 'vertices':vertices,'edges':edges,'adj':adj,
            'words':words,'masks':masks,'faces':face_words,'face_masks':face_masks,
            'energies':[0]+[3*len(w) for w in words],
            'tree':sorted(tree),'chords':chords,'chordwords':[chordword(w) for w in words],
            'plaquette_indices':[masks.index(m) for m in face_masks],
            'max_plaquettes_per_link':max(degrees)}


def check_complete_low_sector(g):
    """Exhaust all SU(2) irrep labels n=2j with total electric energy <24.

    At a vertex a singlet exists iff sum(n) is even and max(n)<=sum(other n).
    All allowed nonvacuum assignments here have two n=1 edges at each active
    vertex, hence a unique intertwiner and exactly one simple loop.
    """
    edges=g['edges']; labels=[0]*len(edges)
    incident=[[e for _,e in adj] for adj in g['adj']]
    last=[max(es) for es in incident]
    completed_at=[[v for v in range(len(incident)) if last[v]==e]
                  for e in range(len(edges))]
    found=[]; visited=0
    def visit(k,energy):
        nonlocal visited
        visited+=1
        if k==len(edges):
            if any(labels):
                assert all(n in (0,1) for n in labels)
                assert all(sum(labels[e]>0 for e in es) in (0,2) for es in incident)
                mask=sum(1<<e for e,n in enumerate(labels) if n)
                assert mask in g['masks']
            else:
                mask=0
            found.append(mask)
            return
        for n in range(4):
            ee=energy+n*(n+2)
            if ee>=24:
                break
            labels[k]=n
            valid=True
            for v in completed_at[k]:
                ns=[labels[e] for e in incident[v]]
                if sum(ns)%2 or 2*max(ns)>sum(ns):
                    valid=False; break
            if valid:
                visit(k+1,ee)
        labels[k]=0
    visit(0,0)
    assert sorted(found)==sorted(g['masks'])
    return {'electric_threshold':24,'allowed_assignments':len(found),
            'unique_intertwiner_each':True,'search_nodes':visited,
            'complete_low_sector_verified':True}


def tetrahedral_group():
    elements=[]
    for a in range(4):
        for sign in (-1,1):
            q=[0]*4; q[a]=2*sign; elements.append(tuple(q))
    elements+=list(product((-1,1),repeat=4))
    index={q:i for i,q in enumerate(elements)}
    ident=index[(2,0,0,0)]
    inv=np.array([index[(q[0],-q[1],-q[2],-q[3])] for q in elements],dtype=np.int64)
    table=np.empty((24,24),dtype=np.int64)
    for i,a in enumerate(elements):
        for j,b in enumerate(elements):
            raw=(a[0]*b[0]-sum(a[k]*b[k] for k in range(1,4)),
                 a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
                 a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
                 a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])
            assert all(x%2==0 for x in raw)
            table[i,j]=index[tuple(x//2 for x in raw)]
    # All coordinate monomials through degree four, compared to Haar on unit S^3.
    for degree in range(5):
        for indices in product(range(4),repeat=degree):
            total=F(sum(np.prod([q[i] for i in indices],dtype=np.int64)
                        for q in elements),24*(2**degree))
            if degree==0:
                target=F(1)
            elif degree%2:
                target=F(0)
            elif degree==2:
                target=F(indices[0]==indices[1],4)
            else:
                a,b,c,d=indices
                target=F(int(a==b and c==d)+int(a==c and b==d)+int(a==d and b==c),24)
            assert total==target
    traces=np.array([q[0] for q in elements],dtype=np.int64)
    return table,inv,traces,ident


def exact_matrices(g, batch=65536):
    table,inv,traces,ident=tetrahedral_group()
    r=len(g['chords']); count=24**r; dim=len(g['masks'])
    faces=set(g['face_masks'])
    even_faces={a^b for a in faces for b in faces}
    wpairs=[(i,j) for i in range(dim) for j in range(i,dim)
            if g['masks'][i]^g['masks'][j] in faces]
    upairs=[(i,j) for i in range(dim) for j in range(i,dim)
            if g['masks'][i]^g['masks'][j] in even_faces]
    ws=[0]*len(wpairs); us=[0]*len(upairs); norms=[0]*dim
    started=time.time()
    for begin in range(0,count,batch):
        n=min(batch,count-begin)
        seq=np.arange(begin,begin+n,dtype=np.int64)
        digits=[]
        for _ in range(r):
            digits.append(seq%24); seq=seq//24
        f=np.ones((dim,n),dtype=np.int64)
        for row,word in enumerate(g['chordwords'],1):
            state=np.full(n,ident,dtype=np.int64)
            for e in word:
                factor=digits[abs(e)-1]
                if e<0:
                    factor=inv[factor]
                state=table[state,factor]
            f[row]=traces[state]
        s=f[g['plaquette_indices']].sum(axis=0,dtype=np.int64)
        s2=s*s
        for i in range(dim):
            norms[i]+=int(np.dot(f[i],f[i]))
        for k,(i,j) in enumerate(wpairs):
            ws[k]+=int(np.dot(f[i]*f[j],s))
        for k,(i,j) in enumerate(upairs):
            us[k]+=int(np.dot(f[i]*f[j],s2))
    assert norms==[count]*dim
    w=[[F(0) for _ in range(dim)] for _ in range(dim)]
    u=[[F(0) for _ in range(dim)] for _ in range(dim)]
    for (i,j),value in zip(wpairs,ws):
        w[i][j]=w[j][i]=F(value,2*count)
    for (i,j),value in zip(upairs,us):
        u[i][j]=u[j][i]=F(value,4*count)
    gram=[[u[i][j]-sum(w[i][k]*w[k][j] for k in range(dim))
           for j in range(dim)] for i in range(dim)]
    assert all(x==0 for x in gram[0]) # the first plaquette excitations were retained
    for i in g['plaquette_indices']:
        assert w[0][i]==F(1,2)
    return w,gram,{'chord_count':r,'cubature_configurations':count,
                   'coordinate_moments_through_degree_four':True,
                   'orthonormality_diagonal_checks':True,
                   'zero_entries_by_original_link_center_parity':True,
                   'interaction_nonzero_candidates':len(wpairs),
                   'second_moment_candidates':len(upairs),
                   'seconds':round(time.time()-started,3)}


def frac_matrix(m):
    return [[str(x) for x in row] for row in m]


def localized_floor(beta,np_,z,kappa=F(24)):
    """Allocate a fraction of K to exact single-plaquette ground-energy floors."""
    beta=abs(beta)
    best=kappa-beta*np_; record={'type':'global potential norm'}
    # Fixed rational choices; all resulting floors are rigorous.
    for t in (F(1,50),F(1,20),F(1,10),F(1,5),F(3,10),F(1,2)):
        alpha=t/z; blocal=beta/alpha
        n=max(9,int((float(blocal)+50)**0.5)+3)
        a,d,b,gram=su2_matrix(blocal,n)
        lo,hi=eigen_interval(a,0,abs(blocal),tolerance=F(1,10**10))
        scalar=lo-b*b/(d-lo)
        e0lo=schur_lower_interval(a,gram,d,scalar-1,hi,0,tolerance=F(1,10**10))[0]
        floor=(1-t)*kappa+np_*alpha*e0lo
        if floor>best:
            best=floor;record={'type':'local plaquette energy allocation',
                              't':str(t),'alpha':str(alpha),
                              'local_beta':str(blocal),'local_cutoff':n,
                              'local_ground_lower':str(e0lo)}
    return best,record


def certify(g,w,gram0,beta_text):
    beta=F(beta_text); dim=len(w); np_=len(g['faces'])
    a=[[-beta*w[i][j]+(g['energies'][i] if i==j else 0)
        for j in range(dim)] for i in range(dim)]
    gram=[[beta*beta*x for x in row] for row in gram0]
    v=abs(beta)*np_
    a0=eigen_interval(a,0,v,tolerance=F(1,10**11))
    a1=eigen_interval(a,1,v,tolerance=F(1,10**11))
    d,local=localized_floor(beta,np_,g['max_plaquettes_per_link'])
    base={'beta':beta_text,'ritz_ground':pair(*a0),'ritz_first':pair(*a1),
          'crude_tail_floor':str(F(24)-v),'improved_tail_floor':pair(d,d),
          'local_floor_certificate':local}
    if d<=a1[1]:
        return dict(base,certified=False,reason='Tail floor below retained first-excited upper bound')
    b2=max(sum(abs(x) for x in row) for row in gram)
    scalar=a0[0]-b2/(d-a0[0])
    l0=schur_lower_interval(a,gram,d,scalar-1,a0[1],0,tolerance=F(1,10**11))[0]
    l1=schur_lower_interval(a,gram,d,scalar-1,a1[1],1,tolerance=F(1,10**11))[0]
    lower,upper=l1-a0[1],a1[1]-l0
    return dict(base,certified=lower>0,gap_interval=pair(lower,upper),
                ground_interval=pair(l0,a0[1]),first_interval=pair(l1,a1[1]),
                cross_norm_squared_upper=str(b2),
                witness={'tail_floor':str(d),'ground_ritz_lower':str(a0[0]),
                         'ground_ritz_upper':str(a0[1]),'first_ritz_lower':str(a1[0]),
                         'first_ritz_upper':str(a1[1]),'ground_schur_lower':str(l0),
                         'first_schur_lower':str(l1)})


def run(name,lengths,betas):
    g=geometry(lengths)
    audit=check_complete_low_sector(g)
    print(name,'basis',len(g['energies']),'loops',len(g['words']),audit,flush=True)
    cache=BASE/(name+'_matrices.json')
    if cache.exists():
        raw=json.loads(cache.read_text())
        assert raw['geometry']['lengths']==list(lengths)
        w=[[F(x) for x in row] for row in raw['W']]
        gram=[[F(x) for x in row] for row in raw['gram_B_over_beta_squared']]
        quadrature=raw['quadrature']
    else:
        w,gram,quadrature=exact_matrices(g)
        raw={'geometry':{k:g[k] for k in ('lengths','vertices','edges','words','faces',
                  'energies','masks','tree','chords','max_plaquettes_per_link')},
             'basis_audit':audit,'quadrature':quadrature,
             'W':frac_matrix(w),'gram_B_over_beta_squared':frac_matrix(gram)}
        cache.write_text(json.dumps(raw,indent=2)+'\n')
    print(name,'exact matrices assembled',quadrature,flush=True)
    cases=[]
    for beta in betas:
        result=certify(g,w,gram,beta);cases.append(result)
        print(name,beta,result.get('gap_interval',result.get('reason')),
              'd=',result['improved_tail_floor'],flush=True)
    result={'name':name,'group':'SU(2)','boundary':'open','energy_units':'c_K',
            'links':len(g['edges']),'vertices':len(g['vertices']),
            'plaquettes':len(g['faces']),'retained_dimension':len(g['energies']),
            'omitted_electric_floor':24,'basis_audit':audit,
            'quadrature':quadrature,'cases':cases}
    (BASE/(name+'_certificates.json')).write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--geometry',default='all',
        choices=['all','single','strip','patch','cube'])
    parser.add_argument('--beta',nargs='*',default=['0.00348','0.1','0.5','1','2','3'])
    args=parser.parse_args()
    specs={'single':(1,1,0),'strip':(2,1,0),'patch':(2,2,0),'cube':(1,1,1)}
    for name,lengths in specs.items():
        if args.geometry in ('all',name):
            run(name,lengths,args.beta)
