#!/usr/bin/env python3
"""Independent finite oracles and exact certificates for the BM continuation.

Run beside BM_Finite_Solvers_2026-10-18.py. Writes a reproducible JSON report.
Proofs of infinite/general assertions are in the accompanying development note;
the finite checks here do not replace them.
"""
from collections import deque
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import platform
import random
import time

HERE = Path(__file__).resolve().parent
ENGINE = HERE / 'BM_Finite_Solvers_2026-10-18.py'
spec = importlib.util.spec_from_file_location('bm_solver', ENGINE)
bm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bm)
RNG = random.Random(20261018)
REPORT = {'title': 'BM exact finite verification', 'seed': 20261018,
          'python': platform.python_version(), 'groups': {},
          'limitations': ['Internal verification, not independent peer review.',
                         'Finite tests do not establish unrestricted continuous, PDE or quantum claims.']}


def brute_fragmentation(matrix, weights=None):
    weights = weights or [1] * len(matrix)
    costs = set()
    for order in permutations(range(len(matrix[0]))):
        counts = []
        for row in matrix:
            word = ''.join(str(row[j]) for j in order)
            counts.append(sum(bool(run) for run in word.split('0')))
        costs.add((sum(w for c, w in zip(counts, weights) if c > 1),
                   sum(w * (c - 1) for c, w in zip(counts, weights))))
    return sorted(p for p in costs if not any(q != p and q[0] <= p[0] and q[1] <= p[1]
                                              for q in costs))


def test_fragmentation():
    start = time.perf_counter()
    checked = 0
    for n in range(1, 5):
        possible_rows = [row for row in product((0, 1), repeat=n) if any(row)]
        for r in range(1, 4):
            for matrix in product(possible_rows, repeat=r):
                result = bm.fragmentation(matrix)
                actual = [(p['B'], p['D']) for p in result['frontier']]
                assert actual == brute_fragmentation(matrix)
                for p in result['frontier']:
                    assert sorted(p['order']) == list(range(n))
                checked += 1
    for _ in range(24):
        n, r = RNG.randrange(2, 8), RNG.randrange(1, 6)
        matrix = []
        for _ in range(r):
            row = [RNG.randrange(2) for _ in range(n)]
            row[RNG.randrange(n)] = 1
            matrix.append(row)
        weights = [RNG.randrange(1, 4) for _ in range(r)]
        result = bm.fragmentation(matrix, weights)
        assert [(p['B'], p['D']) for p in result['frontier']] == brute_fragmentation(matrix, weights)
        checked += 1
    gaps = []
    for n in range(5, 10):
        matrix = [[int(j in (i, i + 1)) for j in range(n)] for i in range(n - 1)]
        matrix += [[int(j % 2 == 0) for j in range(n)] for _ in range(n - 4)]
        result = bm.fragmentation(matrix)
        phi = min(p['B'] for p in result['frontier'])
        delta = min(p['D'] for p in result['frontier'])
        d_phi = result['D_k'][phi]['D']
        assert (phi, delta, d_phi) == (n - 4, n - 3, (n - 4) * (math.ceil(n / 2) - 1))
        gaps.append({'n': n, 'phi': phi, 'delta': delta, 'D_phi': d_phi})
    benchmarks = []
    for r, n in [(4, 8), (5, 9), (6, 10)]:
        matrix = [[RNG.randrange(2) for _ in range(n)] for _ in range(r)]
        for row in matrix:
            row[RNG.randrange(n)] = 1
        t = time.perf_counter()
        result = bm.fragmentation(matrix)
        benchmarks.append({'matrix': matrix, **result['statistics'],
                           'seconds': time.perf_counter() - t,
                           'frontier': result['frontier']})
    REPORT['groups']['fragmentation'] = {'passed': True, 'independent_brute_force_instances': checked,
        'gap_family': gaps, 'benchmarks': benchmarks, 'seconds': time.perf_counter() - start}


def oracle_interface(legal, family, task, action):
    cells = {}
    for i, x in enumerate(legal):
        code = tuple(family[j][x[j]] for j in range(len(x)))
        cells.setdefault(code, []).append(i)
    for cell in cells.values():
        if len({task[i] for i in cell}) != 1:
            return False
        destinations = []
        for i in cell:
            if action[i] is None:
                destinations.append(None)
            else:
                x = legal[action[i]]
                destinations.append(tuple(family[j][x[j]] for j in range(len(x))))
        if len(set(destinations)) != 1:
            return False
    return True


def test_interfaces():
    start, checked, contexts, universal_positive = time.perf_counter(), 0, 0, 0
    states = list(product(range(2), repeat=2))
    families = bm.interface_families([2, 2])
    for mask in range(1, 1 << 4):
        legal = [x for i, x in enumerate(states) if mask >> i & 1]
        n = len(legal)
        property_holds = bm.join_lifting([2, 2], legal)['holds']
        every_instance_has_greatest = True
        for task in bm.partitions(n):
            for action in product([None] + list(range(n)), repeat=n):
                feasible = [e for e in families if oracle_interface(legal, e, task, action)]
                greatest = [e for e in feasible if all(
                    all(bm.refines(f[i], e[i]) for i in range(2)) for f in feasible)]
                answer = bm.optimize_interfaces([2, 2], legal, task, actions=[action])
                assert answer['feasible_count'] == len(feasible)
                assert answer['greatest_exists'] == bool(greatest)
                assert answer['optimal_cost'] == min(sum(len(set(p)) for p in f) for f in feasible)
                every_instance_has_greatest &= bool(greatest)
                checked += 1
        assert property_holds == every_instance_has_greatest
        contexts += 1
        universal_positive += property_holds
    diagonal = bm.join_lifting([2, 2], [(0, 0), (1, 1)])
    assert not diagonal['holds']
    witness = bm.optimize_interfaces([2, 2], [(0, 0), (1, 1)], diagonal['counterexample_task'])
    assert not witness['greatest_exists']
    assert bm.join_lifting([2, 2], [(0, 0), (0, 1), (1, 0)])['holds']
    # Nontrivial legacy bound: the first coordinate must remain injective.
    assert bm.join_lifting([2, 2], [(0, 0), (1, 1)], [(0, 1), (0, 0)])['holds']
    REPORT['groups']['correlated_interfaces'] = {'passed': True, 'contexts': contexts,
        'exhaustive_task_and_single_partial_action_instances': checked,
        'contexts_with_universal_greatestness': universal_positive,
        'diagonal_counterexample': diagonal, 'seconds': time.perf_counter() - start}


def bfs_safe(native, predictor, task, output, epsilon, x, q):
    queue, visited = deque([(x, q)]), set()
    while queue:
        x, q = queue.popleft()
        if (x, q) in visited:
            continue
        visited.add((x, q))
        if abs(Q(task[x]) - Q(output[q])) > epsilon:
            return False
        for y, p in zip(native[x], predictor[q]):
            if (y is None) != (p is None):
                return False
            if y is not None:
                queue.append((y, p))
    return True


def check_safety_instance(native, predictor, task, output, epsilon):
    answer = bm.causal_safety(native, predictor, task, output, epsilon)
    expected = {(x, q) for x in range(len(native)) for q in range(len(predictor))
                if bfs_safe(native, predictor, task, output, epsilon, x, q)}
    assert set(map(tuple, answer['safe_relation'])) == expected
    for failure in answer['failures']:
        x, q = failure['native'], failure['predictor']
        assert len(failure['word']) < len(native) * len(predictor)
        for a in failure['word']:
            x, q = native[x][a], predictor[q][a]
            assert x is not None and q is not None
        bad_output = abs(Q(task[x]) - Q(output[q])) > epsilon
        bad_availability = any((a is None) != (b is None) for a, b in zip(native[x], predictor[q]))
        assert bad_output or bad_availability


def test_causal_safety():
    count, start = 0, time.perf_counter()
    for f, g in product(product([None, 0, 1], repeat=2), repeat=2):
        for task, output in product(product([0, 1], repeat=2), repeat=2):
            check_safety_instance([[x] for x in f], [[x] for x in g], task, output, Q(0))
            count += 1
    for _ in range(80):
        f = [[RNG.choice([None, 0, 1, 2]) for _ in range(2)] for _ in range(3)]
        g = [[RNG.choice([None, 0, 1, 2]) for _ in range(2)] for _ in range(3)]
        task, output = [[Q(RNG.randrange(5), 3) for _ in range(3)] for _ in range(2)]
        check_safety_instance(f, g, task, output, Q(1, 3))
        count += 1
    one = bm.synthesize_predictor([[1], [0]], [0, 1], [0, 1], 1, Q(0))
    two = bm.synthesize_predictor([[1], [0]], [0, 1], [0, 1], 2, Q(0))
    coarse = bm.synthesize_predictor([[1], [0]], [0, 1], [0], 1, Q(1))
    assert not one['feasible']
    assert two['feasible'] and two['minimum_states'] == 2
    assert coarse['feasible'] and coarse['minimum_states'] == 1
    REPORT['groups']['infinite_horizon_finite_verifier'] = {
        'passed': True, 'independent_reachability_instances': count,
        'all_failure_words_replayed': True, 'bounded_synthesis_cases': 3,
        'alternating_predictor': two, 'seconds': time.perf_counter() - start}


def verify_lp_certificate(answer):
    q, t = answer['recovery'], answer['optimal_error']
    assert sum(q) == 1 and all(x >= 0 for x in q)
    z = q[:3] + (t,)
    a, b = answer['inequality_matrix'], answer['inequality_rhs']
    assert all(bm.dot(row, z) <= rhs for row, rhs in zip(a, b))
    certificate = answer['certificate']
    indices, mu = certificate['active_inequalities'], certificate['multipliers']
    assert all(x >= 0 for x in mu)
    assert [sum(mu[j] * a[i][k] for j, i in enumerate(indices)) for k in range(4)] == [0, 0, 0, -1]
    assert -sum(mu[j] * b[i] for j, i in enumerate(indices)) == t


def test_quantum():
    start, count = time.perf_counter(), 0
    examples = []
    for denominator in (1, 2, 3, 4, 6):
        for p0 in range(denominator + 1):
            for px in range(denominator - p0 + 1):
                for py in range(denominator - p0 - px + 1):
                    p = [Q(p0, denominator), Q(px, denominator), Q(py, denominator),
                         Q(denominator - p0 - px - py, denominator)]
                    answer = bm.pauli_recovery(p)
                    verify_lp_certificate(answer)
                    # Full qubit algebra: nontrivial normalized defect is two.
                    assert answer['optimal_error'] <= 1
                    count += 1
    for lam in [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]:
        answer = bm.pauli_recovery([(1 + 3 * lam) / 4] + [(1 - lam) / 4] * 3)
        assert answer['optimal_error'] == 1 - lam
        examples.append({'lambda': lam, 'error': answer['optimal_error'],
                         'recovery': answer['recovery']})
    # Strictly monotone secular equation for the ellipsoid example, exact bracket.
    a2, u2 = [Q(1, 4), Q(1)], [Q(9, 25), Q(16, 25)]
    secular = lambda m: sum(a * u / (a + m) ** 2 for a, u in zip(a2, u2)) - 1
    lo, hi = Q(0), Q(1)
    assert secular(lo) > 0 and secular(hi) < 0
    for _ in range(90):
        mid = (lo + hi) / 2
        if secular(mid) > 0:
            lo = mid
        else:
            hi = mid
    error2 = lambda m: sum(m * m * u / (a + m) ** 2 for a, u in zip(a2, u2))
    REPORT['groups']['quantum_recovery'] = {'passed': True,
        'exact_primal_dual_certificates': count, 'depolarizing_examples': examples,
        'sharp_qubit_upper_bound_checked_on_all_Pauli_instances': True,
        'tilted_dephasing': {'lambda': '1/2', 'u': ['3/5', '0', '4/5'],
            'mu_lower': lo, 'mu_upper': hi, 'error_squared_lower': error2(lo),
            'error_squared_upper': error2(hi),
            'error_approximation_only': math.sqrt(float(error2((lo + hi) / 2)))},
        'seconds': time.perf_counter() - start}


def poly_add(*polys):
    result = {}
    for p in polys:
        for monomial, c in p.items():
            result[monomial] = result.get(monomial, Q(0)) + c
    return {m: c for m, c in result.items() if c}


def poly_scale(p, a):
    return {m: a * c for m, c in p.items() if a * c}


def poly_mul(p, q):
    result = {}
    for m, a in p.items():
        for n, b in q.items():
            key = tuple(x + y for x, y in zip(m, n))
            result[key] = result.get(key, Q(0)) + a * b
    return {m: c for m, c in result.items() if c}


def test_jordan_and_native_examples():
    variables = [{tuple(int(i == j) for i in range(5)): Q(1)} for j in range(5)]
    x1, x2, x3, x4, t = variables
    mul = poly_mul
    t2, t3 = mul(t, t), mul(mul(t, t), t)
    y1 = poly_add(x1, mul(t, x2), poly_scale(mul(t2, x3), Q(1, 2)), poly_scale(mul(t3, x4), Q(1, 6)))
    y2 = poly_add(x2, mul(t, x3), poly_scale(mul(t2, x4), Q(1, 2)))
    y3 = poly_add(x3, mul(t, x4))
    invariant = lambda a, b, c, d: poly_add(mul(mul(c, c), c),
        poly_scale(mul(mul(b, c), d), -3), poly_scale(mul(mul(a, d), d), 3))
    assert invariant(y1, y2, y3, x4) == invariant(x1, x2, x3, x4)
    # n=3 invariant and scalar-polynomial lower-bound value.
    z1 = poly_add(x1, mul(t, x2), poly_scale(mul(t2, x3), Q(1, 2)))
    z2 = poly_add(x2, mul(t, x3))
    assert poly_add(poly_scale(mul(z1, x3), 2), poly_scale(mul(z2, z2), -1)) == \
        poly_add(poly_scale(mul(x1, x3), 2), poly_scale(mul(x2, x2), -1))
    # Largest Gram eigenvalue root: p(z)=z²-4z/3+1/12, z>2/3.
    p = lambda z: z * z - Q(4, 3) * z + Q(1, 12)
    lo, hi = Q(1), Q(2)
    assert p(lo) < 0 < p(hi)
    for _ in range(80):
        mid = (lo + hi) / 2
        if p(mid) < 0:
            lo = mid
        else:
            hi = mid
    # Dirichlet Green example x0=1/4, forcing 1 on [1/2,3/4].
    # G(x0,y)=x0(1-y); exact integral = 3/128 > 0, outside a local neighborhood.
    native_response = Q(1, 4) * ((Q(3, 4) - Q(3, 4) ** 2 / 2) - (Q(1, 2) - Q(1, 2) ** 2 / 2))
    assert native_response == Q(3, 128)
    REPORT['groups']['symbolic_and_native_examples'] = {'passed': True,
        'polynomial_flow_identities_checked_by_coefficients': 2,
        'jordan_n3_d1_error_squared_lower': lo, 'jordan_n3_d1_error_squared_upper': hi,
        'jordan_error_approximation_only': math.sqrt(float((lo + hi) / 2)),
        'quasistatic_nonlocal_response': native_response}


def test_operations():
    domains = [[0, 1], [0, 1]]
    assert bm.finite_seed(domains, {0: 1}, [(0, 0), (1, 1)]) == [(1, 1)]
    assert bm.finite_seed(domains, {0: 1, 1: 0}, [(0, 0), (1, 1)]) == []
    statuses = [bm.rooting(x, lambda x: x, lambda x: x >= 0, lambda x: x % 2 == 0)['status']
                for x in [-1, 1, 2]]
    assert statuses == ['not applicable', 'rejected', 'accepted']
    assert bm.check_rebranching([0, 1], [10, 11], lambda x: x + 10, lambda x: x,
                               lambda y: y - 10)['valid']
    assert not bm.check_rebranching([0, 1], [10, 11], lambda x: 10, lambda x: x,
                                   lambda y: y - 10)['valid']
    REPORT['groups']['finite_operational_conventions'] = {'passed': True, 'checks': 7}


if __name__ == '__main__':
    overall = time.perf_counter()
    for test in (test_fragmentation, test_interfaces, test_causal_safety,
                 test_quantum, test_jordan_and_native_examples, test_operations):
        test()
        print(test.__name__ + ': passed', flush=True)
    REPORT['all_passed'] = True
    REPORT['total_seconds'] = time.perf_counter() - overall
    REPORT['source_hashes'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (ENGINE, Path(__file__).resolve())}
    out = HERE / 'BM_Verification_Results_2026-10-18.json'
    out.write_text(json.dumps(REPORT, indent=2, default=bm.json_default) + '\n', encoding='utf-8')
    print('Saved ' + out.name)
