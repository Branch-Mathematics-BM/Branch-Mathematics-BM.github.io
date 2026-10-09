"""Exact finite-regulator certificates for the 2026-10-09 continuation.

Python standard library only. All spectral certification uses rational
arithmetic, including finite-matrix inertia. Decimal output is rounded
outwards. This verifies one-plaquette SU(2)/SU(3), not continuum Yang--Mills.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import json
from pathlib import Path


class ZeroPivot(Exception):
    pass


def inertia(matrix, x):
    """Number of strictly negative eigenvalues of matrix-xI by congruence."""
    n = len(matrix)
    a = [row.copy() for row in matrix]
    for i in range(n):
        a[i][i] -= x
    negatives = 0
    for k in range(n):
        pivot = a[k][k]
        if not pivot:
            raise ZeroPivot
        negatives += pivot < 0
        for i in range(k + 1, n):
            if not a[i][k]:
                continue
            factor = a[i][k] / pivot
            for j in range(i, n):
                a[i][j] -= factor * a[j][k]
                a[j][i] = a[i][j]
    return negatives


def eigen_interval(matrix, index, bound, tolerance=F(1, 10**13)):
    """Rational bracket, with eigenvalues indexed from zero."""
    low, high = -bound - 1, max(row[i] for i, row in enumerate(matrix)) + bound + 1
    assert inertia(matrix, low) == 0
    assert inertia(matrix, high) == len(matrix)
    while high - low > tolerance:
        midpoint = (low + high) / 2
        # A leading principal minor can vanish without x being an eigenvalue.
        # Use another rational point; there are only finitely many bad points.
        for attempt in range(len(matrix)**2 + 2):
            try:
                count = inertia(matrix, midpoint)
                break
            except ZeroPivot:
                midpoint = low + (high - low) * F(attempt + 1, attempt + 3)
        else:
            raise ArithmeticError("Could not avoid zero rational LDL pivot")
        if count <= index:
            low = midpoint
        else:
            high = midpoint
    assert inertia(matrix, low) <= index
    assert inertia(matrix, high) >= index + 1
    return low, high


def outward(x, direction, places=10):
    with localcontext() as ctx:
        ctx.prec = 100
        ctx.rounding = direction
        q = Decimal(1).scaleb(-places)
        return str((Decimal(x.numerator) / Decimal(x.denominator)).quantize(q))


def pair(a, b):
    return [outward(a, ROUND_FLOOR), outward(b, ROUND_CEILING)]


def schur_lower_interval(matrix, gram, d, low, high, index, tolerance=F(1, 10**13)):
    """Bracket a comparison eigenvalue below the omitted-sector floor d.

    The exact Schur complement dominates A-xI-B*B/(d-x). Its negative
    inertia therefore cannot exceed that of this finite rational matrix.
    """
    assert high < d
    def count(x):
        comparison = [[matrix[i][j] - gram[i][j]/(d-x)
                       for j in range(len(matrix))] for i in range(len(matrix))]
        return inertia(comparison, x)
    assert count(low) <= index
    assert count(high) >= index + 1
    while high - low > tolerance:
        midpoint = (low + high) / 2
        for attempt in range(len(matrix)**2 + 2):
            try:
                nneg = count(midpoint)
                break
            except ZeroPivot:
                midpoint = low + (high-low)*F(attempt+1, attempt+3)
        else:
            raise ArithmeticError('Could not avoid zero Schur pivot')
        if nneg <= index:
            low = midpoint
        else:
            high = midpoint
    assert count(low) <= index
    return low, high


def su2_matrix(beta, n):
    # Four links, one square plaquette, all vertex gauge constraints imposed.
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(n):
        a[k][k] = F(4 * k * (k + 2))
        if k:
            a[k - 1][k] = a[k][k - 1] = -beta / 2
    gram = [[F(0) for _ in range(n)] for _ in range(n)]
    gram[-1][-1] = beta*beta / 4
    return a, F(4 * n * (n + 2)) - abs(beta), abs(beta) / 2, gram


def su3_matrix(beta, s):
    labels = [(p, total - p) for total in range(s + 1) for p in range(total + 1)]
    index = {label: i for i, label in enumerate(labels)}
    a = [[F(0) for _ in labels] for _ in labels]
    for col, (p, q) in enumerate(labels):
        a[col][col] = F(16, 3) * (p*p + q*q + p*q + 3*p + 3*q)
        # Fundamental and antifundamental tensor-product rules, multiplicity one.
        neighbors = [(p + 1, q), (p, q + 1)]
        if p:
            neighbors += [(p - 1, q + 1), (p - 1, q)]
        if q:
            neighbors += [(p, q - 1), (p + 1, q - 1)]
        for label in neighbors:
            if label in index:
                a[index[label]][col] -= beta / 6
    assert all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))
    t = s + 1
    kappa = F(16, 3) * (t*t + 3*t - (t*t // 4))
    # Only the first omitted shell is reached from the retained space.
    outside = [(p, t-p) for p in range(t+1)]
    cross = [[F(0) for _ in labels] for _ in outside]
    for row, (p, q) in enumerate(outside):
        for neighbor in ((p-1, q), (p, q-1)):
            if neighbor in index:
                cross[row][index[neighbor]] = -beta/6
    gram = [[sum(row[i]*row[j] for row in cross) for j in range(len(labels))]
            for i in range(len(labels))]
    # Every row and column of the boundary adjacency has at most two entries.
    return a, kappa - abs(beta), abs(beta) / 3, gram


def certify(group, beta_text, cutoff):
    beta = F(beta_text)
    matrix, d, b, gram = (su2_matrix(beta, cutoff) if group == 'SU(2)'
                    else su3_matrix(beta, cutoff))
    assert max(sum(abs(x) for x in row) for row in gram) <= b*b
    if beta == 0:
        energies = sorted(row[i] for i, row in enumerate(matrix))
        a0 = (energies[0], energies[0])
        a1 = (energies[1], energies[1])
    else:
        a0 = eigen_interval(matrix, 0, abs(beta))
        a1 = eigen_interval(matrix, 1, abs(beta))
    assert d > a1[1], (group, beta, cutoff, d, a1)
    lower0 = a0[0] - b*b / (d - a0[0])
    lower1 = a1[0] - b*b / (d - a1[0])
    # Verify the rational lower endpoints satisfy the Schur-counting criterion.
    for lower, a in ((lower0, a0[0]), (lower1, a1[0])):
        assert lower < d
        assert lower + b*b / (d - lower) <= a
    scalar_gap_interval = pair(lower1-a0[1], a1[1]-lower0)
    if beta:
        search_low = lower0 - 1
        lower0 = schur_lower_interval(matrix, gram, d, search_low, a0[1], 0)[0]
        lower1 = schur_lower_interval(matrix, gram, d, search_low, a1[1], 1)[0]
    gap_lower, gap_upper = lower1 - a0[1], a1[1] - lower0
    assert 0 < gap_lower <= gap_upper
    result = {'group': group, 'beta': beta_text, 'cutoff': cutoff,
              'matrix_dimension': len(matrix),
              'tail_floor_d': pair(d, d), 'cross_norm_upper_b': pair(b, b),
              'ritz_ground': pair(*a0), 'ritz_first_excited': pair(*a1),
              'ground_interval': pair(lower0, a0[1]),
              'first_excited_interval': pair(lower1, a1[1]),
              'scalar_gap_interval': scalar_gap_interval,
              'gap_interval': pair(gap_lower, gap_upper),
              'certified_positive': True}
    print(json.dumps(result), flush=True)
    return result


def structural_checks():
    # Independent exact inertia check against a matrix with known spectrum {-1,3}.
    a = [[F(1), F(2)], [F(2), F(1)]]
    assert inertia(a, F(-2)) == 0
    assert inertia(a, F(0)) == 1
    assert inertia(a, F(4)) == 2
    for j, exact in enumerate((F(-1), F(3))):
        lo, hi = eigen_interval(a, j, F(4))
        assert lo < exact < hi
    # SU(3) tail minimum is attained at balanced labels at the first omitted shell.
    for s in range(1, 10):
        t = s + 1
        floor = F(16, 3)*(t*t + 3*t - (t*t // 4))
        energies = [F(16, 3)*(p*p+q*q+p*q+3*p+3*q)
                    for total in range(t, t+10) for p in range(total+1)
                    for q in (total-p,)]
        assert min(energies) == floor
    # Elementary bound is exact in a saturated 2x2 comparison test via sign criterion.
    for aa, dd, bb in ((F(3), F(9), F(2)), (F(-5), F(7), F(3))):
        low = aa - bb*bb/(dd-aa)
        assert (aa-low)*(dd-low) >= bb*bb
    return {'rational_inertia_known_spectrum': True,
            'su3_tail_shell_minima': True, 'schur_lower_endpoint_checks': True}


def main():
    checks = structural_checks()
    rows = []
    for beta in ('0', '0.00333', '0.00348', '1', '10', '100'):
        rows.append(certify('SU(2)', beta, 9))
    rows.append(certify('SU(2)', '100', 18))
    for beta in ('0', '0.00333', '0.00348', '1', '10'):
        rows.append(certify('SU(3)', beta, 4))
    output = {'scope': 'Single square plaquette; four links; gauge-invariant states; energies in c_K units.',
              'method': 'Exact rational LDL inertia, rational bisection and rigorous omitted-sector Schur bounds.',
              'not_claimed': 'No multi-plaquette or infinite-volume/continuum mass-gap computation.',
              'checks': checks, 'cases': rows, 'status': 'All exact rational certificates passed.'}
    Path(__file__).with_name('certificate_results.json').write_text(json.dumps(output, indent=2) + '\n')


if __name__ == '__main__':
    main()
