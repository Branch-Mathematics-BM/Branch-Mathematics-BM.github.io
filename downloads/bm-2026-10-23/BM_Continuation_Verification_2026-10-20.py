#!/usr/bin/env python3
"""Independent exact checks for the 20 October BM continuation.

The structural oracle enumerates transition tables and initializations; it does
not enumerate covers. Its scalar output optimum uses interval midpoints, not the
production minimum-ball implementation. This is not a formal proof assistant.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import deque, defaultdict
import importlib.util
import json
import random
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bm20_solver',
       HERE / 'BM_Exact_Causal_Completion_2026-10-20.py')
bm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bm)


def scalar_oracle(native, task, budget, initial=None, legacy=None, closed=False):
    """Enumerate all bounded partial predictors and their initializations."""
    n, na = len(native), len(native[0])
    initial = list(range(n)) if initial is None else list(initial)
    best = None
    candidates = 0
    for nq in range(1, budget + 1):
        for flat in product([None] + list(range(nq)), repeat=nq*na):
            g = [flat[q*na:(q+1)*na] for q in range(nq)]
            for choices in product(range(nq), repeat=len(initial)):
                candidates += 1
                reached = set(zip(initial, choices))
                queue = deque(reached)
                valid = True
                while queue and valid:
                    x, q = queue.popleft()
                    for a in range(na):
                        y, p = native[x][a], g[q][a]
                        if (y is None) != (p is None):
                            valid = False
                            break
                        if y is not None and (y, p) not in reached:
                            reached.add((y, p))
                            queue.append((y, p))
                if not valid:
                    continue
                if closed and any(len({q for y, q in reached if y == x}) > 1
                                  for x in range(n)):
                    continue
                by_q = [{x for x, p in reached if p == q} for q in range(nq)]
                if legacy is not None and any(len({legacy[x] for x in cell}) > 1
                                               for cell in by_q):
                    continue
                error = max((((max(task[x][0] for x in cell)
                               -min(task[x][0] for x in cell))/2)**2
                             for cell in by_q if cell), default=Q(0))
                if best is None or error < best:
                    best = error
                    if not best:
                        return best, candidates
    return best, candidates


def check_ball(points, cert):
    center = cert['center']
    weights, support = cert['weights'], cert['support']
    assert all(w >= 0 for w in weights) and sum(weights) == 1
    assert all(sum(w*points[i][j] for i, w in zip(support, weights)) == center[j]
               for j in range(len(center)))
    ds = lambda p: sum((a-b)**2 for a, b in zip(center, p))
    assert all(ds(points[i]) == cert['radius_squared'] for i in support)
    assert all(ds(p) <= cert['radius_squared'] for p in points)


def check_predictor(native, task, result, initial=None, legacy=None):
    initial = list(range(len(native))) if initial is None else initial
    for row in result['frontier']:
        model = row['witness']
        if model is None:
            continue
        for cell, cert in zip(model['cells'], model['cell_certificates']):
            assert set(cert['support']) <= set(cell)
            local = dict(cert)
            local['support'] = tuple(cell.index(x) for x in cert['support'])
            check_ball([task[x] for x in cell], local)
        reached = set((x, model['initialization'][str(x)]) for x in initial)
        queue = deque(reached)
        while queue:
            x, q = queue.popleft()
            assert x in model['cells'][q]
            assert sum((a-b)**2 for a, b in zip(task[x], model['output'][q])) <= row['optimal_error_squared']
            if legacy is not None:
                assert legacy[x] == model['legacy_output'][q]
            for a in range(len(native[x])):
                y, p = native[x][a], model['predictor'][q][a]
                assert (y is None) == (p is None)
                if y is not None and (y, p) not in reached:
                    reached.add((y, p)); queue.append((y, p))
        if result['mode'] == 'closed_encoder':
            assert all(len({q for y, q in reached if y == x}) <= 1
                       for x in range(len(native)))


def compare(native, task, budget, initial=None, legacy=None):
    task = [[Q(v) for v in row] for row in task]
    checked = candidates = 0
    for mode in ('history', 'closed_encoder'):
        result = bm.synthesize(native, task, budget, initial=initial, legacy=legacy, mode=mode)
        check_predictor(native, task, result, initial, legacy)
        for row in result['frontier']:
            exact, count = scalar_oracle(native, task, row['state_budget'], initial,
                                        legacy, mode == 'closed_encoder')
            assert exact == row['optimal_error_squared'], (native, task, mode, row, exact)
            candidates += count; checked += 1
    return checked, candidates


def main():
    rng = random.Random(20261020)
    report = {'date': '2026-10-20', 'arithmetic': 'exact rational',
              'scope': 'finite implementation and algebraic identities; not independent peer review'}
    balls = 0
    known = [([[0], [2]], Q(1)),
             ([[0, 0], [2, 0], [1, 2]], Q(25, 16)),
             ([[0, 0], [4, 0], [1, 1]], Q(4)),
             ([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]], Q(1)),
             ([[1, 2], [1, 2], [1, 2]], Q(0))]
    for points, radius in known:
        cert = bm.smallest_ball(points); check_ball(points, cert)
        assert cert['radius_squared'] == radius; balls += 1
    for _ in range(200):
        dimension = rng.randrange(1, 5)
        points = [tuple(Q(rng.randrange(-8, 9), rng.randrange(1, 5))
                        for _ in range(dimension)) for j in range(rng.randrange(1, 8))]
        cert = bm.smallest_ball(points); check_ball(points, cert); balls += 1
    report['minimum_ball_certificates'] = balls

    cases = comparisons = oracle_candidates = 0
    for n in range(1, 4):
        for update in product([None] + list(range(n)), repeat=n):
            native = [[y] for y in update]
            for values in product([0, 2], repeat=n):
                c, q = compare(native, [[v] for v in values], min(n, 2))
                cases += 1; comparisons += c; oracle_candidates += q
    for _ in range(24):
        n, na = 4, 2
        native = [[rng.choice([None] + list(range(n))) for a in range(na)] for x in range(n)]
        task = [[rng.randrange(-3, 5)] for x in range(n)]
        initial = None if rng.randrange(2) else [0]
        legacy = None if rng.randrange(2) else [rng.randrange(2) for x in range(n)]
        c, q = compare(native, task, 2, initial, legacy)
        cases += 1; comparisons += c; oracle_candidates += q
    example = {'native': [[3], [1], [1], [2]], 'task': [[2], [2], [3], [0]], 'max_states': 2}
    h = bm.synthesize(**example)
    c = bm.synthesize(**example, mode='closed_encoder')
    assert h['best']['error_squared'] == 1 and c['best']['error_squared'] == Q(9, 4)
    extra, q = compare(example['native'], example['task'], 2)
    cases += 1; comparisons += extra; oracle_candidates += q
    report['causal_structural_oracle'] = {'native_task_cases': cases,
        'mode_budget_comparisons': comparisons, 'transition_initialization_candidates': oracle_candidates,
        'history_example_squared_errors': {'history': '1', 'closed_encoder': '9/4'}}

    bridge_checks = 0
    for _ in range(100):
        a, target, b = [Q(rng.randrange(-5, 6), rng.randrange(1, 5)) for i in range(3)]
        epsilon = rng.choice([Q(1), Q(-1), Q(2, 3), Q(-3, 2)])
        h = Q(rng.randrange(1, 5), 3); m = rng.randrange(1, 30)
        tau = 2*m*epsilon*h
        tail = 2*(target-a-tau*b)/tau**2
        assert a+tau*b+tau**2*tail/2 == target
        assert b+tau*tail == -b+2*(target-a)/tau
        bridge_checks += 1
    # Symbolic Lie derivative of I=c^3-3bcd+3ad^2 in the four-state chain.
    polynomial = {(0, 0, 3, 0): Q(1), (0, 1, 1, 1): Q(-3), (1, 0, 0, 2): Q(3)}
    derivative = defaultdict(Q)
    for exponents, coefficient in polynomial.items():
        for i in range(3):
            if exponents[i]:
                power = list(exponents); power[i] -= 1; power[i+1] += 1
                derivative[tuple(power)] += coefficient*exponents[i]
    assert all(v == 0 for v in derivative.values())
    r2 = Q(60, 97); r3 = (Q(1, 6)+r2/8)/(Q(19, 15)-Q(1, 20))
    assert r3 < Q(21, 100) and 1+r2*r2+r3*r3 < Q(36, 25)
    assert Q(5, 6)/(6*Q(83, 60)) > Q(1, 10)
    assert 2*Q(19, 15)-Q(83, 60) > 1
    assert Q(1, 24)**2+Q(1, 30)**2+Q(1, 72)**2 < Q(1, 16)**2
    assert Q(49, 252) < Q(1, 5)
    eta, b0 = Q(1, 300000), Q(1, 28800)
    margin = 2*b0*eta-9*eta*eta
    assert margin > Q(1, 10**10)
    report['Jordan'] = {'exact_bridge_identities': bridge_checks,
        'invariant_Lie_derivative_zero': True, 'nonlinear_parameter': str(eta),
        'certified_squared_error_improvement': str(margin),
        'conservative_claim': '> 1/10000000000'}

    identities = 0
    for d in range(2, 21):
        for c in (Q(j, 20) for j in range(21)):
            frobenius_squared = 1-2*c*c/d+2*c*c/(d*d)
            determinant_absolute = c*c*(d-1)/(d*d)
            assert frobenius_squared+2*determinant_absolute == 1
            assert 1+Q(d-2, d)*c <= 2-Q(2, d)
            identities += 1
    report['quantum_trace_projection_identities'] = identities
    report['infinite_diagonal_example'] = {
        'epsilon': '1/2', 'L': '1/2', 'C': '1', 'b_i': '1/i', 'N': 3, 'K': 24,
        'grid_states_bound': 49**3,
        'squared_error_bound': str(Q(1, 16)+Q(3, 24**2)/Q(1, 2)**2)}
    assert Q(report['infinite_diagonal_example']['squared_error_bound']) < Q(1, 4)

    invalid = [dict(native=[[0]], task=[[0]], max_states=0),
               dict(native=[[1]], task=[[0]], max_states=1),
               dict(native=[[0]], task=[[0.5]], max_states=1),
               dict(native=[[0]], task=[[True]], max_states=1),
               dict(native=[[0]], task=[[0]], max_states=True),
               dict(native=[[0]], task=[[0]], max_states=1, initial=[]),
               dict(native=[[0]], task=[[0]], max_states=1, mode='unknown'),
               dict(native=[[0]], task=[[0]], max_states=1, epsilon_squared='-1')]
    for kwargs in invalid:
        try:
            bm.synthesize(**kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid input was accepted')
    report['rejected_invalid_inputs'] = len(invalid)
    report['status'] = 'all checks passed'
    text = json.dumps(report, indent=2)
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(text+'\n', encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
