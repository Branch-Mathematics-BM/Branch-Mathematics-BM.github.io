#!/usr/bin/env python3
"""Exact finite causal minimax synthesis; Python 3.10+, standard library only.

Inputs use integer or rational-string task coordinates. The output error is
squared Euclidean error, not error. Algorithms are exponential reference methods.
Modes: history (overlapping invariant covers), closed_encoder (partitions).
Run: python BM_Exact_Causal_Completion_2026-10-20.py examples.json
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import deque
import json
import sys


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, str, Q)):
        raise ValueError('rational values must be integers or fraction strings')
    return Q(value)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def distance_squared(a, b):
    return sum(((x-y)**2 for x, y in zip(a, b)), Q(0))


def solve_linear(matrix, rhs):
    n = len(rhs)
    a = [list(map(Q, row)) + [Q(v)] for row, v in zip(matrix, rhs)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [x/divisor for x in a[col]]
        for i in range(n):
            if i != col:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[col])]
    return tuple(row[-1] for row in a)


def smallest_ball(points):
    """Rational center, radius squared, and convex-support optimality witness."""
    if not points or not points[0]:
        raise ValueError('nonempty points of positive dimension required')
    dimension = len(points[0])
    if any(len(p) != dimension for p in points):
        raise ValueError('point dimensions differ')
    points = tuple(tuple(rational(x) for x in p) for p in points)
    for size in range(1, min(dimension + 1, len(points)) + 1):
        for selected in combinations(range(len(points)), size):
            p0 = points[selected[0]]
            directions = [tuple(x-y for x, y in zip(points[i], p0))
                          for i in selected[1:]]
            coefficients = solve_linear(
                [[dot(u, v) for v in directions] for u in directions],
                [dot(u, u)/2 for u in directions])
            if coefficients is None:
                continue
            weights = (1-sum(coefficients),) + coefficients
            if any(w < 0 for w in weights):
                continue
            center = tuple(p0[j] + sum((a*v[j] for a, v in
                           zip(coefficients, directions)), Q(0))
                           for j in range(dimension))
            radius_squared = distance_squared(center, p0)
            if all(distance_squared(center, p) <= radius_squared for p in points):
                return {'center': center, 'radius_squared': radius_squared,
                        'support': selected, 'weights': weights}
    raise AssertionError('finite Euclidean minimum ball must have a support')


def validate(native, task, max_states, initial, legacy, mode):
    if not native or len(task) != len(native) or not task or not task[0]:
        raise ValueError('nonempty finite native system and matching vector tasks required')
    n, actions, dimension = len(native), len(native[0]), len(task[0])
    if any(len(row) != actions for row in native):
        raise ValueError('native table must be rectangular')
    if any(y is not None and (isinstance(y, bool) or not isinstance(y, int)
           or not 0 <= y < n) for row in native for y in row):
        raise ValueError('native successor outside carrier')
    if any(len(row) != dimension for row in task):
        raise ValueError('task dimensions differ')
    task = tuple(tuple(rational(x) for x in row) for row in task)
    if isinstance(max_states, bool) or not isinstance(max_states, int) or max_states < 1:
        raise ValueError('max_states must be a positive integer')
    initial = list(range(n)) if initial is None else list(initial)
    if not initial or len(set(initial)) != len(initial) or any(
        isinstance(x, bool) or not isinstance(x, int) or not 0 <= x < n for x in initial):
        raise ValueError('initial must be a nonempty set of native state indices')
    if legacy is not None and len(legacy) != n:
        raise ValueError('legacy must have one label per native state')
    if mode not in ('history', 'closed_encoder'):
        raise ValueError('mode must be history or closed_encoder')
    return task, sorted(initial)


def synthesize(native, task, max_states, initial=None, legacy=None,
               mode='history', epsilon_squared=None):
    """Globally optimal finite predictor frontier, with unrestricted real outputs.

    Availability is preserved exactly. The history mode permits the same native
    state in several predictor cells. closed_encoder requires disjoint cells.
    Optional legacy labels are retained exactly at every reachable predictor state.
    """
    task, initial = validate(native, task, max_states, initial, legacy, mode)
    if epsilon_squared is not None:
        epsilon_squared = rational(epsilon_squared)
        if epsilon_squared < 0:
            raise ValueError('epsilon_squared must be nonnegative')
    n, actions = len(native), len(native[0])
    reachable = set(initial)
    queue = deque(initial)
    while queue:
        x = queue.popleft()
        for y in native[x]:
            if y is not None and y not in reachable:
                reachable.add(y)
                queue.append(y)
    states = sorted(reachable)
    full_mask = sum(1 << x for x in states)
    initial_mask = sum(1 << x for x in initial)
    cells = []
    for small_mask in range(1, 1 << len(states)):
        members = [x for j, x in enumerate(states) if small_mask & (1 << j)]
        first = members[0]
        if any(any((native[x][a] is None) != (native[first][a] is None)
                   for a in range(actions)) for x in members[1:]):
            continue
        if legacy is not None and any(legacy[x] != legacy[first] for x in members[1:]):
            continue
        mask = sum(1 << x for x in members)
        successors = [None if native[first][a] is None else
                      sum(1 << y for y in {native[x][a] for x in members})
                      for a in range(actions)]
        ball = smallest_ball([task[x] for x in members])
        ball['support'] = tuple(members[i] for i in ball['support'])
        cells.append({'mask': mask, 'members': members,
                      'successor_masks': successors, 'ball': ball})
    frontier, best, total_checked, total_feasible = [], None, 0, 0
    limit = min(max_states, len(states))
    minimum = None
    for size in range(1, limit + 1):
        checked = feasible = 0
        for indices in combinations(range(len(cells)), size):
            chosen = [cells[i] for i in indices]
            checked += 1
            union = 0
            disjoint = True
            for cell in chosen:
                disjoint = disjoint and not (union & cell['mask'])
                union |= cell['mask']
            if union & initial_mask != initial_mask:
                continue
            if mode == 'closed_encoder' and (not disjoint or union != full_mask):
                continue
            transitions = []
            for cell in chosen:
                row = []
                for target in cell['successor_masks']:
                    if target is None:
                        row.append(None)
                    else:
                        q = next((i for i, other in enumerate(chosen)
                                  if target & other['mask'] == target), None)
                        if q is None:
                            break
                        row.append(q)
                if len(row) != actions:
                    break
                transitions.append(row)
            if len(transitions) != size:
                continue
            feasible += 1
            error_squared = max(cell['ball']['radius_squared'] for cell in chosen)
            if best is None or error_squared < best['error_squared']:
                best = {
                    'error_squared': error_squared, 'states': size,
                    'cells': [cell['members'] for cell in chosen],
                    'predictor': transitions,
                    'output': [cell['ball']['center'] for cell in chosen],
                    'initialization': {str(x): next(i for i, cell in enumerate(chosen)
                                       if cell['mask'] & (1 << x)) for x in initial},
                    'cell_certificates': [cell['ball'] for cell in chosen],
                    'legacy_output': None if legacy is None else
                                     [legacy[cell['members'][0]] for cell in chosen]
                }
        total_checked += checked
        total_feasible += feasible
        frontier.append({'state_budget': size, 'feasible': best is not None,
                         'optimal_error_squared': None if best is None else best['error_squared'],
                         'witness_states': None if best is None else best['states'],
                         'witness': best, 'covers_checked': checked,
                         'valid_covers': feasible})
        if (minimum is None and epsilon_squared is not None and best is not None
                and best['error_squared'] <= epsilon_squared):
            minimum = size
        if best is not None and best['error_squared'] == 0:
            break
    return {'mode': mode, 'frontier': frontier, 'best': best,
            'requested_budget': max_states, 'minimum_states_for_threshold': minimum,
            'epsilon_squared': epsilon_squared,
            'zero_error_from_budget': frontier[-1]['state_budget']
                                    if best is not None and best['error_squared'] == 0 else None,
            'statistics': {'reachable_native_states': states, 'admissible_cells': len(cells),
                           'covers_checked': total_checked, 'valid_covers': total_feasible},
            'scope': 'finite deterministic partial actions; Euclidean tasks; exact availability; '
                     'infinite histories; unrestricted real predictor outputs; stated memory budget'}


def default(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python BM_Exact_Causal_Completion_2026-10-20.py examples.json')
    with open(sys.argv[1], encoding='utf-8') as stream:
        data = json.load(stream)
    problems = data if isinstance(data, list) else [data]
    results = [synthesize(**p) for p in problems]
    print(json.dumps(results if isinstance(data, list) else results[0], indent=2, default=default))
