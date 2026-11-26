#!/usr/bin/env python3
"""BM finite reference solvers, Research Edition continuation 2026-10-18.

Python 3.10+, standard library only. No floating-point optimality certificates.
Run: python BM_Finite_Solvers_2026-10-18.py problem.json
The examples file contains a list of supported problem objects.
Exponential algorithms are deliberate; this is a reference implementation.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json
import sys


def canonical(labels):
    lookup = {}
    return tuple(lookup.setdefault(x, len(lookup)) for x in labels)


def partitions(n):
    """All equivalence relations on a labelled n-element set, once each."""
    if n == 0:
        yield ()
        return
    def visit(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for x in range(maximum + 2):
            yield from visit(prefix + [x], max(maximum, x))
    yield from visit([0], 0)


def refines(p, q):
    return all(p[i] != p[j] or q[i] == q[j]
               for i in range(len(p)) for j in range(i))


def join(*relations):
    if not relations:
        raise ValueError('join needs at least one relation')
    n = len(relations[0])
    if any(len(p) != n for p in relations):
        raise ValueError('relations must have the same carrier')
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for p in relations:
        first = {}
        for i, label in enumerate(p):
            if label in first:
                parent[root(i)] = root(first[label])
            else:
                first[label] = i
    return canonical(root(i) for i in range(n))


def family_join(e, f):
    return tuple(join(p, q) for p, q in zip(e, f))


def gamma(legal, family):
    return canonical(tuple(p[x] for p, x in zip(family, state))
                     for state in legal)


def interface_families(sizes, bounds=None):
    if not sizes or any(not isinstance(n, int) or n < 1 for n in sizes):
        raise ValueError('positive finite coordinate sizes required')
    if bounds is None:
        bounds = [tuple(0 for _ in range(n)) for n in sizes]
    if len(bounds) != len(sizes) or any(len(b) != n for b, n in zip(bounds, sizes)):
        raise ValueError('legacy bounds have the wrong shape')
    choices = [[p for p in partitions(n) if refines(p, b)]
               for n, b in zip(sizes, bounds)]
    return list(product(*choices))


def validate_context(sizes, legal):
    if not legal or len(set(map(tuple, legal))) != len(legal):
        raise ValueError('legal context must be nonempty and have no duplicates')
    if any(len(x) != len(sizes) or any(not isinstance(v, int) or not 0 <= v < n
           for v, n in zip(x, sizes)) for x in legal):
        raise ValueError('legal state is outside the declared product')


def join_lifting(sizes, legal, bounds=None):
    """Universal greatestness criterion, with an exact negative witness."""
    validate_context(sizes, legal)
    families = interface_families(sizes, bounds)
    relations = [gamma(legal, e) for e in families]
    checked = 0
    for i, e in enumerate(families):
        for j in range(i, len(families)):
            f = families[j]
            checked += 1
            lhs = gamma(legal, family_join(e, f))
            rhs = join(relations[i], relations[j])
            if lhs != rhs:
                pair = next((a, b) for a in range(len(legal)) for b in range(a)
                            if lhs[a] == lhs[b] and rhs[a] != rhs[b])
                return {'holds': False, 'families': len(families),
                        'checked_pairs': checked, 'E': e, 'F': f,
                        'bad_legal_pair': pair, 'counterexample_task': rhs}
    return {'holds': True, 'families': len(families), 'checked_pairs': checked}


def interface_feasible(legal, family, task, actions=()):
    rel = gamma(legal, family)
    for i in range(len(legal)):
        for j in range(i):
            if rel[i] != rel[j]:
                continue
            if task[i] != task[j]:
                return False
            for action in actions:
                a, b = action[i], action[j]
                if (a is None) != (b is None):
                    return False
                if a is not None and rel[a] != rel[b]:
                    return False
    return True


def optimize_interfaces(sizes, legal, task, bounds=None, actions=(), weights=None, cost=None):
    """Exact finite optimization for an explicitly supplied, evaluable cost.

    Default cost is the weighted sum of local alphabet sizes, not bit length.
    The Python API accepts an arbitrary cost(family); CLI uses rational weights.
    """
    validate_context(sizes, legal)
    if len(task) != len(legal):
        raise ValueError('task needs one value per legal state')
    if any(len(a) != len(legal) or any(v is not None and
           (not isinstance(v, int) or not 0 <= v < len(legal)) for v in a)
           for a in actions):
        raise ValueError('each action must map legal indices to legal indices or null')
    if weights is None:
        weights = [1] * len(sizes)
    if len(weights) != len(sizes):
        raise ValueError('one weight per coordinate required')
    weights = list(map(Q, weights))
    if any(w < 0 for w in weights):
        raise ValueError('default alphabet weights must be nonnegative')
    if cost is None:
        cost = lambda family: sum(w * len(set(p)) for w, p in zip(weights, family))
    families = interface_families(sizes, bounds)
    feasible = [e for e in families if interface_feasible(legal, e, task, actions)]
    # The discrete family is always feasible for a well-formed deterministic model.
    greatest_candidate = feasible[0]
    for e in feasible[1:]:
        greatest_candidate = family_join(greatest_candidate, e)
    exists = interface_feasible(legal, greatest_candidate, task, actions)
    best = min(feasible, key=cost)
    return {'feasible_count': len(feasible), 'enumerated': len(families),
            'greatest_exists': exists,
            'greatest': greatest_candidate if exists else None,
            'join_of_feasible': greatest_candidate, 'optimal_family': best,
            'optimal_cost': cost(best), 'cost_name': 'caller-supplied or weighted alphabet size'}


def row_costs(matrix, order, weights=None):
    weights = weights if weights is not None else [1] * len(matrix)
    blocks = []
    for row in matrix:
        previous, count = 0, 0
        for j in order:
            count += bool(row[j] and not previous)
            previous = row[j]
        blocks.append(count)
    return (sum(w for b, w in zip(blocks, weights) if b > 1),
            sum(w * max(0, b - 1) for b, w in zip(blocks, weights)))


def fragmentation(matrix, weights=None):
    """Exact full (broken rows, extra blocks) frontier with order witnesses."""
    if not matrix or not matrix[0]:
        raise ValueError('a nonempty binary matrix is required')
    n = len(matrix[0])
    if any(len(row) != n or any(v not in (0, 1) for v in row) or not any(row)
           for row in matrix):
        raise ValueError('rectangular binary matrix with no empty rows required')
    weights = [1] * len(matrix) if weights is None else list(weights)
    if len(weights) != len(matrix) or any(not isinstance(w, int) or w <= 0 for w in weights):
        raise ValueError('positive integer row multiplicities required')
    # Compress identical rows and collect their multiplicities.
    rows = {}
    for row, weight in zip(matrix, weights):
        row = tuple(row)
        rows[row] = rows.get(row, 0) + weight
    patterns, multiplicities = list(rows), list(rows.values())
    r = len(patterns)
    # Group identical columns; a Pareto witness can always be expanded adjacently.
    columns = {}
    for j in range(n):
        bits = sum(patterns[i][j] << i for i in range(r))
        columns.setdefault(bits, []).append(j)
    ones, groups = list(columns), list(columns.values())
    q = len(ones)
    mask_weight = [sum(w for i, w in enumerate(multiplicities) if mask >> i & 1)
                   for mask in range(1 << r)]
    seen = [0] * (1 << q)
    for s in range(1, 1 << q):
        low = s & -s
        seen[s] = seen[s ^ low] | ones[low.bit_length() - 1]
    # A record stores (best D, previous (last,F)); previous subset removes last.
    layers = [dict() for _ in range(1 << q)]
    layers[0][(-1, 0)] = (0, None)
    transitions = 0
    for s in range(1 << q):
        for (last, broken), (d, _) in list(layers[s].items()):
            old_ones = 0 if last == -1 else ones[last]
            for j in range(q):
                if s >> j & 1:
                    continue
                restarts = (ones[j] & ~old_ones) & seen[s]
                key = (j, broken | restarts)
                new_s, new_d = s | (1 << j), d + mask_weight[restarts]
                transitions += 1
                if key not in layers[new_s] or new_d < layers[new_s][key][0]:
                    layers[new_s][key] = (new_d, (last, broken))
    full = (1 << q) - 1
    best_by_b = {}
    for key, (d, _) in layers[full].items():
        b = mask_weight[key[1]]
        if b not in best_by_b or d < best_by_b[b][0]:
            best_by_b[b] = (d, key)
    def witness(key):
        s, compressed = full, []
        while s:
            j, _ = key
            compressed.append(j)
            key = layers[s][key][1]
            s ^= 1 << j
        return [j for group in reversed(compressed) for j in groups[group]]
    frontier, smallest_d = [], None
    for b, (d, key) in sorted(best_by_b.items()):
        if smallest_d is None or d < smallest_d:
            order = witness(key)
            assert row_costs(matrix, order, weights) == (b, d)
            frontier.append({'B': b, 'D': d, 'order': order})
            smallest_d = d
    budgets = []
    for k in range(sum(weights) + 1):
        feasible = [point for point in frontier if point['B'] <= k]
        budgets.append({'k': k, 'D': min(p['D'] for p in feasible) if feasible else None})
    return {'frontier': frontier, 'D_k': budgets,
            'statistics': {'original_rows': len(matrix), 'original_columns': n,
                           'distinct_rows': r, 'distinct_columns': q,
                           'states': sum(map(len, layers)), 'transitions': transitions}}


def causal_safety(native, predictor, task, output, epsilon, metric=None, initial=None):
    """Largest safe relation for finite deterministic partial labelled systems.

    native[x][a], predictor[q][a] are successor indices or None (disabled).
    The returned failure words include [] for an immediate output/availability fault.
    """
    nx, nq = len(native), len(predictor)
    if not nx or not nq or len(task) != nx or len(output) != nq:
        raise ValueError('nonempty carriers and matching outputs required')
    na = len(native[0])
    if any(len(row) != na for row in native + predictor):
        raise ValueError('all states must use the same action alphabet')
    for table, size in ((native, nx), (predictor, nq)):
        if any(v is not None and (not isinstance(v, int) or not 0 <= v < size)
               for row in table for v in row):
            raise ValueError('successor outside carrier')
    if epsilon < 0:
        raise ValueError('epsilon must be nonnegative')
    metric = metric or (lambda a, b: abs(Q(a) - Q(b)))
    initial = list(range(nx)) if initial is None else list(initial)
    if any(not 0 <= x < nx for x in initial):
        raise ValueError('initial state outside carrier')
    safe, failures = set(), {}
    for x, q in product(range(nx), range(nq)):
        if metric(task[x], output[q]) > epsilon:
            failures[x, q] = {'word': [], 'reason': 'output error'}
        elif any((a is None) != (b is None) for a, b in zip(native[x], predictor[q])):
            failures[x, q] = {'word': [], 'reason': 'availability mismatch'}
        else:
            safe.add((x, q))
    rounds = 0
    while True:
        removed = {}
        for x, q in safe:
            for a, (y, p) in enumerate(zip(native[x], predictor[q])):
                if y is not None and (y, p) not in safe:
                    failure = failures[y, p]
                    removed[x, q] = {'word': [a] + failure['word'],
                                     'reason': failure['reason']}
                    break
        if not removed:
            break
        safe.difference_update(removed)
        failures.update(removed)
        rounds += 1
    initialization = {str(x): next((q for q in range(nq) if (x, q) in safe), None)
                      for x in initial}
    return {'safe_relation': sorted(safe),
            'initialization_exists': all(q is not None for q in initialization.values()),
            'initialization': initialization, 'deletion_rounds': rounds,
            'failures': [{'native': x, 'predictor': q, **f}
                         for (x, q), f in sorted(failures.items())]}


def solve_linear(matrix, vector):
    """Exact square linear solve. None denotes singularity."""
    n = len(vector)
    a = [list(map(Q, row)) + [Q(v)] for row, v in zip(matrix, vector)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        factor = a[col][col]
        a[col] = [x / factor for x in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[col])]
    return tuple(row[-1] for row in a)


def synthesize_predictor(native, task, output_catalogue, max_states, epsilon, initial=None):
    """Minimum-state predictor in a finite catalogue and bounded state budget.

    Exhaustively enumerates partial transition tables and output assignments.
    A negative result applies only to the supplied catalogue and budget.
    """
    if not native or not output_catalogue or not isinstance(max_states, int) or max_states < 1:
        raise ValueError('nonempty native system/catalogue and positive budget required')
    na = len(native[0])
    checked = 0
    for nq in range(1, max_states + 1):
        for flat in product([None] + list(range(nq)), repeat=nq * na):
            predictor = [list(flat[q * na:(q + 1) * na]) for q in range(nq)]
            for output in product(output_catalogue, repeat=nq):
                checked += 1
                result = causal_safety(native, predictor, task, output, epsilon, initial=initial)
                if result['initialization_exists']:
                    return {'feasible': True, 'minimum_states': nq, 'predictor': predictor,
                            'output': output, 'verification': result,
                            'candidates_checked': checked}
    return {'feasible': False, 'max_states': max_states, 'candidates_checked': checked,
            'scope': 'specified finite output catalogue and state budget only'}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def pauli_recovery(probabilities):
    """Optimal unamplified full-algebra qubit recovery, rational LP certificate."""
    p = tuple(map(Q, probabilities))
    if len(p) != 4 or any(x < 0 for x in p) or sum(p) != 1:
        raise ValueError('four nonnegative rational Pauli probabilities summing to one required')
    p0, px, py, pz = p
    lam = (p0 + px - py - pz, p0 - px + py - pz, p0 - px - py + pz)
    # Variables z=(q0,qx,qy,t), qz=1-q0-qx-qy. Inequalities A z <= b.
    a = [(-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0),
         (1, 1, 1, 0), (0, 0, 0, -1), (0, 0, 0, 1)]
    b = [Q(0), Q(0), Q(0), Q(1), Q(0), Q(2)]
    for l, coeff, constant in zip(lam, [(2, 2, 0), (2, 0, 2), (0, -2, -2)], [-1, -1, 1]):
        a.append(tuple(-l * v for v in coeff) + (-1,))
        b.append(l * constant - 1)
    vertices = []
    for selected in combinations(range(len(a)), 4):
        z = solve_linear([a[i] for i in selected], [b[i] for i in selected])
        if z is not None and all(dot(row, z) <= rhs for row, rhs in zip(a, b)):
            vertices.append(z)
    z = min(vertices, key=lambda x: x[3])
    active = [i for i in range(len(a)) if dot(a[i], z) == b[i]]
    certificate = None
    for selected in combinations(active, 4):
        transposed = [[a[i][j] for i in selected] for j in range(4)]
        mu = solve_linear(transposed, [0, 0, 0, -1])
        if mu is not None and all(v >= 0 for v in mu):
            lower = -sum(mu[j] * b[i] for j, i in enumerate(selected))
            assert lower == z[3]
            certificate = {'active_inequalities': selected, 'multipliers': mu,
                           'proven_lower_bound': lower}
            break
    assert certificate is not None
    q = z[:3] + (1 - sum(z[:3]),)
    return {'noise': p, 'bloch_multipliers': lam, 'recovery': q,
            'optimal_error': z[3], 'certificate': certificate,
            'inequality_matrix': a, 'inequality_rhs': b}


def finite_seed(domains, partial, allowed=None):
    """Explicit finite operational convention; no canonical completion selector."""
    if any(i < 0 or i >= len(domains) or v not in domains[i] for i, v in partial.items()):
        raise ValueError('partial assignment violates a declared type')
    allowed = None if allowed is None else set(map(tuple, allowed))
    return [x for x in product(*domains)
            if all(x[i] == v for i, v in partial.items()) and (allowed is None or x in allowed)]


def rooting(state, export, applicable, admissible):
    value = export(state)
    status = ('not applicable' if not applicable(value)
              else 'accepted' if admissible(value) else 'rejected')
    return {'export': value, 'status': status}


def check_rebranching(source, target, transport, source_task, target_task):
    target = set(target)
    for x in source:
        y = transport(x)
        if y not in target:
            return {'valid': False, 'witness': x, 'reason': 'target obligations fail'}
        if source_task(x) != target_task(y):
            return {'valid': False, 'witness': x, 'reason': 'task square fails'}
    return {'valid': True, 'checked_realizations': len(source)}


def dispatch(problem):
    p = dict(problem)
    operation = p.pop('operation')
    functions = {'fragmentation': fragmentation, 'interfaces': optimize_interfaces,
                 'join_lifting': join_lifting, 'causal_safety': causal_safety,
                 'synthesize_predictor': synthesize_predictor, 'pauli_recovery': pauli_recovery}
    if operation not in functions:
        raise ValueError('unknown operation: ' + operation)
    if operation in ('causal_safety', 'synthesize_predictor'):
        p['epsilon'] = Q(p['epsilon'])
    return functions[operation](**p)


def json_default(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python BM_Finite_Solvers_2026-10-18.py problem.json')
    with open(sys.argv[1], encoding='utf-8') as stream:
        problem = json.load(stream)
    result = [dispatch(p) for p in problem] if isinstance(problem, list) else dispatch(problem)
    print(json.dumps(result, indent=2, default=json_default))
