#!/usr/bin/env python3
"""Exact real-rational certificates for BM23-Q3. Python standard library only.

Verifies supplied certificates; it does not solve arbitrary SDPs or perform
quantifier elimination. No floating-point values or tolerances are accepted.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (str, int, F)):
        raise ValueError('Use integers or rational strings, never floats/bools.')
    return F(x)


def matrix(a, n=None):
    if not isinstance(a, list) or not a or any(not isinstance(r, list) for r in a):
        raise ValueError('Matrix must be a nonempty square list.')
    n = len(a) if n is None else n
    if len(a) != n or any(len(r) != n for r in a):
        raise ValueError('Matrix dimension mismatch.')
    return [[rational(x) for x in row] for row in a]


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def sub(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def trace_product(a, b):
    return sum((a[i][j]*b[j][i] for i in range(len(a))
                for j in range(len(a))), F(0))


def psd(a):
    """Exact symmetric LDL/Schur check, including singular PSD matrices."""
    n = len(a)
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise ValueError('Matrix is not symmetric.')
    s = [row[:] for row in a]
    pivots = []
    for k in range(n):
        d = s[k][k]
        if d < 0:
            raise ValueError('Negative PSD pivot.')
        if d == 0:
            if any(s[k][j] != 0 for j in range(k+1, n)):
                raise ValueError('Zero PSD pivot has a nonzero residual row.')
        else:
            for i in range(k+1, n):
                for j in range(i, n):
                    s[i][j] -= s[i][k]*s[k][j]/d
                    s[j][i] = s[i][j]
        pivots.append(str(d))
    return pivots


def verify(item):
    raw = item['states']
    if not isinstance(raw, list) or not raw:
        raise ValueError('At least one signal state is required.')
    states = [matrix(a) for a in raw]
    n = len(states[0]); r = len(states)
    if any(len(a) != n for a in states):
        raise ValueError('Signal dimensions differ.')
    state_pivots = [psd(a) for a in states]
    if any(trace(a) != 1 for a in states):
        raise ValueError('Signal states must have trace one.')
    if len(item['povm']) != r:
        raise ValueError('POVM outcome count mismatch.')
    povm = [matrix(a, n) for a in item['povm']]
    povm_pivots = [psd(a) for a in povm]
    if [[sum(a[i][j] for a in povm) for j in range(n)] for i in range(n)] != ident(n):
        raise ValueError('POVM does not sum to identity.')
    q = rational(item['success_lower'])
    if not 0 <= q <= 1:
        raise ValueError('Success lower bound outside [0,1].')
    success = [trace_product(a, b) for a, b in zip(states, povm)]
    if any(s < q for s in success):
        raise ValueError('POVM misses claimed worst-case success.')
    weights = [rational(x) for x in item['dual_weights']]
    if len(weights) != r or any(x < 0 for x in weights) or sum(weights) != 1:
        raise ValueError('Dual weights must be a probability vector.')
    y = matrix(item['dual_matrix'], n)
    slacks = [psd(sub(y, scale(w, a))) for w, a in zip(weights, states)]
    upper = trace(y)
    if upper < q:
        raise ValueError('Primal/dual bound contradiction.')
    result = {
        'name': item['name'], 'valid': True, 'dimension': n, 'signals': r,
        'success_interval': [str(q), str(upper)],
        'error_interval': [str(max(F(0), 2*(1-upper))), str(2*(1-q))],
        'exact_optimum': q == upper,
        'individual_success': [str(x) for x in success],
        'state_pivots': state_pivots, 'povm_pivots': povm_pivots,
        'dual_slack_pivots': slacks,
    }
    if 'expected_error' in item and q == upper and rational(item['expected_error']) != 2*(1-q):
        raise ValueError('Expected optimum disagrees with certificate.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificates', type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificates.read_text())
    results = [verify(c) for c in data['certificates']]
    print(json.dumps({'all_passed': True, 'count': len(results), 'results': results}, indent=2))

if __name__ == '__main__':
    main()
