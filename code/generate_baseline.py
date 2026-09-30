#!/usr/bin/env python3
"""Regenerate the three-line baseline Case B using exact standard-library arithmetic."""
import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import platform
import time

HERE = Path(__file__).resolve().parent
OUTPUT = None
A, T = (0, 2, 4), (0, 1, 2)
V = tuple((1, a) for a in A)
S = tuple(product(range(6), range(9)))
INDEX = {s: i for i, s in enumerate(S)}


def write(name, data):
    (OUTPUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def normal(i, p):
    return p[1] - A[i] * p[0]


def field(p):
    c = sum(normal(i, p) == T[i] for i in range(3))
    assert c <= 1
    return c


def profile(u):
    return tuple(field((u[0] + s[0], u[1] + s[1])) for s in S)


def minus(p, q):
    return p[0] - q[0], p[1] - q[1]


def plus(p, q):
    return p[0] + q[0], p[1] + q[1]


def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def hull(pts):
    pts = sorted(set(pts))
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def determinant_mod(matrix, p):
    mat = [[x % p for x in row] for row in matrix]
    determinant = 1
    for c in range(len(mat)):
        k = next((r for r in range(c, len(mat)) if mat[r][c]), None)
        if k is None:
            return 0
        if k != c:
            mat[c], mat[k] = mat[k], mat[c]
            determinant = -determinant
        pivot = mat[c][c]
        determinant = determinant * pivot % p
        inverse = pow(pivot, -1, p)
        for r in range(c + 1, len(mat)):
            f = mat[r][c] * inverse % p
            if f:
                mat[r] = [(x-f*y) % p for x, y in zip(mat[r], mat[c])]
    return determinant % p


def certify_rank(matrix):
    """整数消元找独立原始行；有理回代输出整数化右核基。"""
    pivots, original_rows = {}, []
    for row_index, raw in enumerate(matrix):
        row = list(raw)
        for c, pivot in sorted(pivots.items()):
            if row[c]:
                a, b = row[c], pivot[c]
                divisor = gcd(a, b)
                row = [(b//divisor)*x-(a//divisor)*y for x, y in zip(row, pivot)]
                common = reduce(gcd, row)
                if common:
                    row = [x//common for x in row]
        column = next((c for c, v in enumerate(row) if v), None)
        if column is not None:
            if row[column] < 0:
                row = [-v for v in row]
            pivots[column] = row
            original_rows.append(row_index)
    columns = sorted(pivots)
    free = [c for c in range(len(matrix[0])) if c not in pivots]
    kernel = []
    for f in free:
        vector = [Fraction(0) for _ in matrix[0]]
        vector[f] = Fraction(1)
        for c in reversed(columns):
            row = pivots[c]
            vector[c] = -sum((row[j]*vector[j] for j in range(c+1, len(row))), Fraction(0)) / row[c]
        denominator = lcm(*(v.denominator for v in vector))
        integer = [int(v*denominator) for v in vector]
        common = reduce(gcd, integer)
        kernel.append([v//common for v in integer])
    minor = [[matrix[r][c] for c in columns] for r in original_rows]
    prime = 1000003
    residue = determinant_mod(minor, prime)
    assert residue != 0
    return {
        'rank': len(columns), 'row_count': len(matrix), 'column_count': len(matrix[0]),
        'lower_bound': {'minor_rows': original_rows, 'minor_columns': columns,
                        'modulus_prime': prime, 'determinant_mod_prime': residue},
        'upper_bound': {'free_columns': free, 'integer_right_kernel_basis': kernel,
                        'independence_reason': '在 free_columns 上为非零对角矩阵'},
    }


def main():
    global OUTPUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='New output directory; must not exist')
    args = parser.parse_args()
    OUTPUT = args.output
    shipped = (HERE.parent/'certificates').resolve()
    if OUTPUT.resolve() == shipped or shipped in OUTPUT.resolve().parents:
        raise ValueError('Regeneration must not write into shipped certificates')
    OUTPUT.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    disjointness = []
    for i, j in combinations(range(3), 2):
        x = Fraction(T[i] - T[j], A[j] - A[i])
        assert x.denominator != 1
        disjointness.append({'i': i, 'j': j, 'intersection_x': str(x)})
    offsets = [sorted({normal(i, s) for s in S}) for i in range(3)]
    patterns, events = {}, []
    for i, j in combinations(range(3), 2):
        for bi, bj in product(offsets[i], offsets[j]):
            numerator = bj-bi-(T[j]-T[i])
            denominator = A[j]-A[i]
            if numerator % denominator:
                continue
            x = numerator // denominator
            u = (x, T[i] + A[i]*x-bi)
            row = profile(u)
            patterns.setdefault(row, u)
            events.append({'type': 'two_lines', 'lines': [i, j],
                           'offsets': [bi, bj], 'anchor': u})
    pair_count = len(events)
    for i in range(3):
        for b in offsets[i]:
            u = (1000, T[i]-b+A[i]*1000)
            row = tuple(int(normal(i, s) == b) for s in S)
            assert row == profile(u)
            patterns.setdefault(row, u)
            events.append({'type': 'one_line', 'line': i, 'offset': b, 'anchor': u})
    zero = (0, 1000)
    assert not any(profile(zero))
    patterns.setdefault((0,)*len(S), zero)
    events.append({'type': 'zero_lines', 'anchor': zero})
    rows = sorted(patterns)
    write('patterns.json', {
        'column_order_S': S,
        'patterns': [{'bits': row, 'anchor': patterns[row]} for row in rows],
        'all_coverage_events': events,
        'normal_offsets': offsets,
    })

    difference = Counter()
    subset_vertices = []
    for bits in product((0, 1), repeat=3):
        h = tuple(sum(bits[i]*V[i][k] for i in range(3)) for k in range(2))
        subset_vertices.append(h)
        difference[h] += (-1)**(3-sum(bits))
    polygon = hull(subset_vertices)
    zpoints = sorted(p for p in product(range(4), range(7))
                     if all(cross(polygon[k], polygon[(k+1) % len(polygon)], p) >= 0
                            for k in range(len(polygon))))
    translations = sorted(r for r in product(range(3), range(3))
                          if all(plus(r, z) in INDEX for z in zpoints))

    def entire_j(d):
        intersections = Counter()
        solutions = []
        for i, j in product(range(3), repeat=2):
            if i == j:
                continue
            bi, bj = T[i], T[j]-normal(j, d)
            numerator, denominator = bi-bj, A[j]-A[i]
            if numerator % denominator:
                solutions.append({'i': i, 'j': j, 'integer_solution': None,
                                  'numerator': numerator, 'denominator': denominator})
                continue
            x = numerator//denominator
            w = (x, bi+A[i]*x)
            solutions.append({'i': i, 'j': j, 'integer_solution': w,
                              'numerator': numerator, 'denominator': denominator})
            intersections[w] += 1
        witness = Counter()
        for w, value in intersections.items():
            for h, coefficient in difference.items():
                witness[minus(w, h)] += value*coefficient
        return intersections, {p: value for p, value in witness.items() if value}, solutions

    for q0, q1 in product(zpoints, repeat=2):
        d = minus(q1, q0)
        intersections, witness, solutions = entire_j(d)
        if d != (0, 0) and witness:
            break
    assert witness
    write('witness.json', {
        'V': V, 'q0': q0, 'q1': q1, 'd': d,
        'difference_operator': [{'shift': h, 'coefficient': c} for h, c in sorted(difference.items())],
        'ordered_cross_pair_solutions': solutions,
        'cross_term_support': [{'point': p, 'value': c} for p, c in sorted(intersections.items())],
        'entire_J_support': [{'point': p, 'value': c} for p, c in sorted(witness.items())],
        'Z_vertices_ccw': polygon, 'Z_lattice_points': zpoints, 'R_Z_S': translations,
    })
    linear = [[1, *row] for row in rows]
    extended = [base + [row[INDEX[plus(r, q0)]]*row[INDEX[plus(r, q1)]]
                       for r in translations] for base, row in zip(linear, rows)]
    matrices = {'linear': linear, 'extended': extended}
    write('matrices.json', matrices)
    certificates = {name: certify_rank(matrix) for name, matrix in matrices.items()}
    write('rank-certificates.json', certificates)
    expected = {
        'global_exhaustive_pattern_count': len(rows),
        'pair_anchor_enumerations_before_deduplication': pair_count,
        'normal_offset_counts': list(map(len, offsets)),
        'linear_rank': certificates['linear']['rank'],
        'extended_rank': certificates['extended']['rank'],
    }
    assert list(expected.values()) == [347, 425, [9, 19, 29], 46, 55]
    write('generation-summary.json', {
        'schema_version': '1.0', 'python_version': platform.python_version(),
        'stdlib_only': True, 'elapsed_seconds': round(time.perf_counter()-started, 6),
        'slopes': A, 'offsets': T, 'line_disjointness': disjointness,
        'counts_and_ranks': expected,
        'J_support_size': len(witness), 'Z_lattice_point_count': len(zpoints),
        'R_Z_S_count': len(translations), 'coverage_events_total': len(events),
    })
    print(json.dumps(expected, ensure_ascii=False))


if __name__ == '__main__':
    main()
