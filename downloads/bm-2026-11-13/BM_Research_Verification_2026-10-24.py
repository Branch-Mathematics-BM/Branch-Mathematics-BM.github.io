#!/usr/bin/env python3
"""Reproduce the BM research note's exact witnesses and numerical diagnostics.

Requires Python 3.10+, numpy, scipy, matplotlib. Run with an output directory:
  python BM_Research_Verification_2026-10-24.py .
Seeded checks are internal verification, not independent review or formal proof.
"""
from collections import deque
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import math
import random
import sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def colors(values):
    table = {}
    return [table.setdefault(x, len(table)) for x in values]


def future_classes(tasks, actions):
    n = len(tasks)
    c = colors([(0, t) for t in tasks] + [(1, None)])
    while True:
        d = colors([(c[x], tuple(c[n if x == n or a[x] is None else a[x]]
                                for a in actions)) for x in range(n + 1)])
        if c == d:
            return c[:n]
        c = d


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        for k in range(max(p, default=-1) + 2):
            yield p + (k,)


def compatible_partition(p, tasks, actions, gamma):
    for x in range(len(tasks)):
        for y in range(x):
            if gamma[x] & gamma[y] and p[x] != p[y]:
                return False
            if p[x] != p[y]:
                continue
            if tasks[x] != tasks[y]:
                return False
            for a in actions:
                if (a[x] is None) != (a[y] is None):
                    return False
                if a[x] is not None and p[a[x]] != p[a[y]]:
                    return False
    return True


def separating_word(tasks, actions, x, y):
    start = (x, y)
    todo = deque([(x, y, [])])
    seen = {start}
    def observation(s):
        return (1, None) if s is None else (0, tasks[s])
    while todo:
        x, y, w = todo.popleft()
        if observation(x) != observation(y):
            return w
        for i, a in enumerate(actions):
            xx = None if x is None else a[x]
            yy = None if y is None else a[y]
            if (xx, yy) not in seen:
                seen.add((xx, yy))
                todo.append((xx, yy, w + [i]))
    raise AssertionError('No separating word')


def noisy_cases():
    cases = []
    gset = [{0}, {1}, {0, 1}]
    for tasks in product(range(2), repeat=2):
        for a in product([None, 0, 1], repeat=2):
            for g in product(gset, repeat=2):
                cases.append((tasks, [a], g))
    rng = random.Random(20261024)
    for _ in range(200):
        n = rng.randrange(1, 5)
        tasks = [rng.randrange(3) for _ in range(n)]
        actions = [[rng.choice([None] + list(range(n))) for _ in range(n)]
                   for _ in range(rng.randrange(1, 4))]
        gamma = [{z for z in range(3) if rng.getrandbits(1)} or {rng.randrange(3)}
                 for _ in range(n)]
        cases.append((tasks, actions, gamma))
    positive = negative = witnesses = 0
    for tasks, actions, gamma in cases:
        c = future_classes(tasks, actions)
        bad = [(x, y) for x in range(len(c)) for y in range(x)
               if c[x] != c[y] and gamma[x] & gamma[y]]
        feasible_sizes = [len(set(p)) for p in partitions(len(c))
                          if compatible_partition(p, tasks, actions, gamma)]
        assert bool(feasible_sizes) == (not bad)
        if feasible_sizes:
            positive += 1
            assert min(feasible_sizes) == len(set(c))
        else:
            negative += 1
            x, y = bad[0]
            assert gamma[x] & gamma[y]
            w = separating_word(tasks, actions, x, y)
            for i in w:
                x = None if x is None else actions[i][x]
                y = None if y is None else actions[i][y]
            assert ((x is None) != (y is None) or
                    (x is not None and y is not None and tasks[x] != tasks[y]))
            witnesses += 1
    return dict(instances=len(cases), exhaustive_two_state=324, seeded=200,
                feasible=positive, infeasible=negative, replayed_witnesses=witnesses,
                oracle='enumeration of native congruence partitions, without refinement')


def row_basis(rows, n):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        a[r] = [x / v for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                v = a[i][j]
                a[i] = [x - v*y for x, y in zip(a[i], a[r])]
        r += 1
    return a[:r]


def multiply(rows, a):
    n = len(a)
    return [[sum(F(row[k])*a[k][j] for k in range(n)) for j in range(n)] for row in rows]


def linear_checks():
    rng = random.Random(24102026)
    counts = []
    for _ in range(60):
        n = rng.randrange(1, 5)
        a = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        b = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(rng.randrange(4))]
        l = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        stack, layer = [], l
        for _ in range(n):
            stack += layer
            layer = multiply(layer, a)
        q = row_basis(stack, n)
        assert len(row_basis(q + multiply(q, a), n)) == len(q)
        expected = len(row_basis(b + stack, n)) - len(row_basis(b, n))
        oracle = None
        for k in range(len(stack) + 1):
            for subset in combinations(stack, k):
                aug = b + list(subset)
                if len(row_basis(aug + stack, n)) == len(row_basis(aug, n)):
                    oracle = k
                    break
            if oracle is not None:
                break
        assert oracle == expected
        counts.append(expected)
    # Position of a harmonic oscillator needs exactly one additional linear channel.
    a = [[F(0), F(1)], [F(-1), F(0)]]
    b = [[F(1), F(0)]]
    stack = b + multiply(b, a)
    assert len(row_basis(stack, 2)) == 2
    return dict(random_rational_systems=60, exact_oscillator=1,
                additional_channels_histogram={str(i): counts.count(i) for i in sorted(set(counts))})


def position_error(theta, eta):
    c, s = abs(math.cos(theta)), abs(math.sin(theta))
    if eta >= c:
        return 1.0
    return c*eta + s*math.sqrt(1-eta*eta)


def history_error(alpha, eta):
    if not math.isfinite(alpha) or not math.isfinite(eta) or eta < 0:
        raise ValueError('finite phase and finite nonnegative noise bound required')
    reduced = math.remainder(alpha, math.pi)
    if reduced == 0:
        return 1.0
    # Stable evaluation of sqrt(1-|cos(alpha)|), without a numerical rank cutoff.
    sigma = math.sqrt(2)*abs(math.sin(reduced/2))
    return min(1, eta/sigma)


def oscillator_checks():
    rng = random.Random(8675309)
    assert history_error(1e-15, 0) == 0
    assert history_error(0, 0) == 1
    assert history_error(math.pi, 0) == 1
    assert abs(history_error(1e-15, 1e-16)-math.sqrt(.02)) < 1e-15
    max_gap = 0.0
    for _ in range(160):
        theta, eta = rng.uniform(0, 2*math.pi), rng.uniform(0, 1.2)
        c, s = abs(math.cos(theta)), abs(math.sin(theta))
        bound = min(1, eta)
        fun = lambda u: c*u + s*math.sqrt(max(0, 1-u*u))
        fit = minimize_scalar(lambda u: -fun(u), bounds=(-bound, bound),
                              method='bounded', options={'xatol': 1e-13})
        assert fit.success
        value = max(fun(-bound), fun(bound), -fit.fun)
        gap = abs(value-position_error(theta, eta))
        assert gap < 1e-8
        max_gap = max(max_gap, gap)
    max_svd_gap = 0.0
    for _ in range(160):
        alpha = rng.uniform(.01, math.pi-.01)
        eta = rng.uniform(0, 1.1)
        b = np.array([[1., 0.], [math.cos(alpha), -math.sin(alpha)]])
        _, s, vt = np.linalg.svd(b)
        expected = history_error(alpha, eta)
        v = min(1, eta/s[-1])*vt[-1]
        assert np.linalg.norm(v) <= 1+1e-12
        assert np.linalg.norm(b@v) <= eta+1e-12
        # +/- v with noise -/+ Bv have the identical measured vector 0.
        max_svd_gap = max(max_svd_gap, abs(np.linalg.norm(v)-expected))
        assert abs(np.linalg.norm(v)-expected) < 1e-10
    # Exact primal/dual rational certificate for the scalar minimax value 24/25.
    ell, v, eta, weight = [F(4,5), F(3,5)], [F(3,5), F(4,5)], F(3,5), F(7,20)
    primal = sum(x*y for x,y in zip(ell,v))
    residual_squared = (ell[0]-weight)**2 + ell[1]**2
    assert sum(x*x for x in v) == 1 and abs(v[0]) == eta
    assert residual_squared == F(9,16)
    dual = F(3,4) + eta*weight
    assert primal == dual == F(24,25)
    # Two-sample matrix, weakest eigenvector w=(1,2), all equalities rational.
    b = [[F(1),F(0)], [F(3,5),F(-4,5)]]
    gram = [[sum(b[k][i]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    w = [F(1),F(2)]
    assert [sum(gram[i][j]*w[j] for j in range(2)) for i in range(2)] == [F(2,5)*x for x in w]
    assert F(1,100)/F(2,5) == F(1,40)
    rows = [{'phase_fraction_of_period': h, 'eta': .1,
             'worst_case_state_error': history_error(2*math.pi*h, .1)}
            for h in [0, .01, .05, .1, .25, .4, .49, .5]]
    return dict(scalar_optimization_comparisons=160, scalar_max_gap=max_gap, rank_and_small_phase_edge_checks=4,
                history_svd_witnesses=160, history_max_gap=max_svd_gap,
                exact_certificates={'scalar_value':'24/25', 'scalar_primal':'24/25',
                                    'scalar_dual':'24/25','history_error_squared':'1/40'},
                sampling_rows=rows)


def orbital_checks():
    mu, r, h, vr = F(1), F(1), F(1), F(1,2)
    eps = vr*vr/2+h*h/(2*r*r)-mu/r
    assert eps == F(-3,8)
    assert (-vr)**2/2+h*h/(2*r*r)-mu/r == eps
    ra, rp, va, vp = F(8,5), F(2,5), F(1,2), F(2)
    assert ra*va == rp*vp == F(4,5)
    ea, ep = va*va/2-1/ra, vp*vp/2-1/rp
    assert ea == ep == F(-1,2)
    assert vp*vp/2-va*va/2 == F(15,8)
    assert -1/rp+1/ra == F(-15,8)
    def rhs(t, z):
        radius = np.linalg.norm(z[:2])
        return [z[2], z[3], -z[0]/radius**3, -z[1]/radius**3]
    t = np.linspace(0, 1, 1001)
    curves, max_energy, max_momentum = [], 0., 0.
    for radial in [-.5,.5]:
        sol = solve_ivp(rhs, (0,1), [1,0,radial,1], method='DOP853',
                        t_eval=t, rtol=2e-13, atol=2e-14)
        assert sol.success
        x, y, vx, vy = sol.y
        radius = np.hypot(x,y)
        energy = (vx*vx+vy*vy)/2-1/radius
        angular = x*vy-y*vx
        max_energy = max(max_energy, float(np.max(np.abs(energy+.375))))
        max_momentum = max(max_momentum,float(np.max(np.abs(angular-1))))
        assert min(radius) > .4
        curves.append(radius)
    assert max_energy < 2e-11 and max_momentum < 2e-11
    gap = abs(float(curves[1][100]-curves[0][100]))
    # Sign is the required distinction. No future-fit procedure is being benchmarked.
    result = dict(exact_initial_specific_energy='-3/8', exact_initial_specific_angular_momentum='1',
                  radial_velocities=['-1/2','1/2'], radius_separation_at_t_point1=gap,
                  any_shared_predictor_error_lower_bound_at_t_point1=gap/2,
                  numeric_max_energy_drift=max_energy, numeric_max_angular_momentum_drift=max_momentum,
                  ellipse={'apoapsis':'8/5','periapsis':'2/5','apo_speed':'1/2','peri_speed':'2',
                           'specific_energy':'-1/2','specific_kinetic_gain':'15/8',
                           'specific_potential_change':'-15/8'})
    return result, (t, curves)


def other_witnesses():
    triples = list(product([0,1], repeat=3))
    predicates = [lambda a,b,c:a==b, lambda a,b,c:b==c, lambda a,b,c:a!=c]
    counts = {}
    for k in range(4):
        for subset in combinations(range(3),k):
            count = sum(all(predicates[i](*t) for i in subset) for t in triples)
            counts[str(subset)] = count
            assert (count == 0) == (k == 3)
    # Two deterministic SCMs: M1 X=U,Y=X; M2 Y=U,X=Y.
    observational = [[u,u] for u in [0,1]]
    interventions = [{'u':u, 'M1_Y_after_do_X_0':0,'M2_Y_after_do_X_0':u} for u in [0,1]]
    assert interventions[1]['M1_Y_after_do_X_0'] != interventions[1]['M2_Y_after_do_X_0']
    return dict(global_compatibility_assignment_counts=counts,
                causal_models={'same_observations':observational,'intervention_results':interventions},
                note='Exact classical examples, not a Bell experiment or a new causal law.')


def plot(out, orbit):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
                         'axes.spines.top':False,'axes.spines.right':False})
    fig, axes = plt.subplots(1, 2, figsize=(11,4.3), layout='constrained')
    phase = np.linspace(0,.5,1001)
    ax = axes[0]
    ax.plot(phase,[history_error(2*math.pi*p,.1) for p in phase],color='#0f766e',lw=2.5)
    ax.axhline(.1, color='#64748b',ls='--',lw=1)
    ax.scatter([.25],[.1],color='#0f766e',s=35,zorder=4)
    ax.set(xlabel='Spacing between two position samples / period',ylabel='Exact worst-case error',
           ylim=(0,1.06),xlim=(0,.5),title='Two samples can still miss the state')
    ax.text(.25,.17,'Best spacing: quarter period',ha='center',fontsize=9)
    ax.text(.25,.95,'Unit disk; total measurement-noise norm ≤ 0.1',ha='center',fontsize=8.5)
    t, curves = orbit
    ax = axes[1]
    ax.plot(t,curves[0],label='Initially inward: radial speed −0.5',color='#c2410c',lw=2.2)
    ax.plot(t,curves[1],label='Initially outward: radial speed +0.5',color='#1d4ed8',lw=2.2)
    ax.set(xlabel='Time (normalized)',ylabel='Distance from central mass',
           title='Same energy and angular momentum; different futures')
    ax.text(.03,.96,'Initial position (1, 0); μ = 1; h = 1; ε = −3/8',transform=ax.transAxes,
            ha='left',va='top',fontsize=8.4)
    ax.legend(loc='lower left',fontsize=8.4,frameon=False)
    fig.suptitle('BM necessity tests: missing distinctions have measurable consequences',fontsize=13)
    fig.savefig(out/'BM_Mechanical_Necessity_2026-10-24.png',dpi=180)
    plt.close(fig)


def main():
    out = Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    out.mkdir(parents=True, exist_ok=True)
    orbital, curves = orbital_checks()
    data = {'status':'passed','date':'2026-10-24','validation':'internal; not peer review or formal-kernel verification',
            'versions':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__,
                        'matplotlib':matplotlib.__version__},
            'finite_noisy_initialization':noisy_cases(),'linear_augmentation':linear_checks(),
            'oscillator':oscillator_checks(),'orbital':orbital,'other_witnesses':other_witnesses()}
    plot(out,curves)
    (out/'BM_Research_Verification_2026-10-24.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__ == '__main__':
    main()
