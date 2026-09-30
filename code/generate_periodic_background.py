#!/usr/bin/env python3
"""Regenerate the periodic-background configuration on the fixed 6-by-9 window."""
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import time

HERE = Path(__file__).resolve().parent
OUTPUT = None
RANK_HELPER = HERE / 'generate_baseline.py'
spec = importlib.util.spec_from_file_location('old_generator_rank_helper', RANK_HELPER)
rank_helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rank_helper)
S = tuple(product(range(6), range(9)))
V = ((1, 0), (1, 2), (1, 4))
H = tuple((2*x, 2*y) for x, y in V)
Z = ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
     (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6))
R = tuple(product(range(3), range(3)))
INDEX = {s: i for i, s in enumerate(S)}


def write(name, data):
    (OUTPUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def pixel(p):
    x, y = p
    count = sum(y-2*i*x == i for i in range(3))
    assert count <= 1
    return (x % 2) ^ count


def profile(u):
    return tuple(pixel((u[0]+x, u[1]+y)) for x, y in S)


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a, b):
    return a[0]-b[0], a[1]-b[1]


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
    start = time.perf_counter()
    offsets = [sorted({y-2*i*x for x, y in S}) for i in range(3)]
    profiles, events = {}, []
    for i, j in combinations(range(3), 2):
        for bi, bj in product(offsets[i], offsets[j]):
            num, den = bj-bi-(j-i), 2*(j-i)
            if num % den:
                continue
            x = num//den
            u = (x, i+2*i*x-bi)
            profiles.setdefault(profile(u), u)
            events.append({'type': 'two_lines', 'lines': [i, j], 'offsets': [bi, bj],
                           'anchor': u, 'phase': x % 2})
    pair_count = len(events)
    for i in range(3):
        for b in offsets[i]:
            for phase in (0, 1):
                x = 1000+phase
                u = (x, i-b+2*i*x)
                row = tuple(((phase+sx) % 2) ^ int(sy-2*i*sx == b) for sx, sy in S)
                assert row == profile(u)
                profiles.setdefault(row, u)
                events.append({'type': 'one_line', 'line': i, 'offset': b,
                               'phase': phase, 'anchor': u})
    for phase in (0, 1):
        u = (phase, 1000)
        row = tuple((phase+sx) % 2 for sx, _ in S)
        assert row == profile(u)
        profiles.setdefault(row, u)
        events.append({'type': 'zero_lines', 'phase': phase, 'anchor': u})
    rows = sorted(profiles)
    write('patterns.json', {'column_order_S': S, 'normal_offsets': offsets,
                                  'patterns': [{'bits': row, 'anchor': profiles[row],
                                                'phase': profiles[row][0] % 2} for row in rows],
                                  'all_coverage_events': events})
    difference = Counter()
    annihilator = Counter()
    for bits in product((0, 1), repeat=3):
        hd = tuple(sum(bits[i]*H[i][k] for i in range(3)) for k in range(2))
        ha = tuple(sum(bits[i]*V[i][k] for i in range(3)) for k in range(2))
        difference[hd] += (-1)**(3-sum(bits))
        annihilator[ha] += 1

    def witness(d):
        cross = Counter()
        solutions = []
        for i, j in product(range(3), repeat=2):
            if i == j:
                continue
            bi, bj = i, j-(d[1]-2*j*d[0])
            num, den = bi-bj, 2*j-2*i
            sol = {'i': i, 'j': j, 'numerator': num, 'denominator': den, 'integer_solution': None}
            if num % den == 0:
                x = num//den
                p = (x, bi+2*i*x)
                cross[p] += 1
                sol['integer_solution'] = p
            solutions.append(sol)
        weight = (-1)**d[0]
        out = Counter()
        for w, value in cross.items():
            for h, coefficient in difference.items():
                out[minus(w, h)] += weight*value*coefficient
        return cross, {p: v for p, v in out.items() if v}, solutions, weight

    for q0, q1 in product(Z, repeat=2):
        d = minus(q1, q0)
        cross, j, solutions, weight = witness(d)
        if d != (0, 0) and j:
            break
    assert j
    write('witness.json', {
        'V': V, 'H': H, 'A_i': ['t+1']*3, 'A_eta_constant': 4,
        'A_operator': [{'shift': h, 'coefficient': c} for h, c in sorted(annihilator.items())],
        'D2_operator': [{'shift': h, 'coefficient': c} for h, c in sorted(difference.items())],
        'q0': q0, 'q1': q1, 'd': d, 'cross_weight': weight,
        'ordered_cross_pair_solutions': solutions,
        'unweighted_cross_support': [{'point': p, 'value': v} for p, v in sorted(cross.items())],
        'entire_J_support': [{'point': p, 'value': v} for p, v in sorted(j.items())],
        'Z_lattice_points': Z, 'R_Z_S': R,
    })
    linear = [[1, *row] for row in rows]
    extended = [base + [row[INDEX[plus(r, q0)]]*row[INDEX[plus(r, q1)]] for r in R]
                for base, row in zip(linear, rows)]
    matrices = {'linear': linear, 'extended': extended}
    write('matrices.json', matrices)
    ranks = {name: rank_helper.certify_rank(matrix) for name, matrix in matrices.items()}
    write('rank-certificates.json', ranks)
    summary = {
        'schema_version': '1.0', 'family': 'B=x mod 2; F0=B xor delta0; F1=delta1; F2=delta2',
        'precommitted_window': {'x': [0, 5], 'y': [0, 8]},
        'python_version': platform.python_version(), 'external_packages': [],
        'elapsed_seconds': round(time.perf_counter()-start, 6),
        'pattern_count': len(rows), 'coverage_event_count': len(events),
        'pair_events': pair_count, 'single_phase_events': sum(len(o) for o in offsets)*2,
        'zero_phase_events': 2, 'J_support_size': len(j),
        'q0': q0, 'q1': q1, 'd': d,
        'linear_rank': ranks['linear']['rank'], 'extended_rank': ranks['extended']['rank'],
        'linear_bound': len(S)+1-len(R), 'extended_bound': len(S)+1,
        'rank_helper_sha256': hashlib.sha256(RANK_HELPER.read_bytes()).hexdigest(),
    }
    write('generation-summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
