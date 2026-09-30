#!/usr/bin/env python3
"""独立检查器：不导入生成器，以整数、Fraction 和 Bareiss 行列式验收。"""
import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import copy
import hashlib
import json
import platform
import time

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "certificates/baseline"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(name):
    return json.loads((RESULTS/name).read_text(encoding='utf-8'))


def pixel(x, y):
    return int(y == 0 or y-2*x == 1 or y-4*x == 2)


def evaluate(u, window):
    return tuple(pixel(u[0]+x, u[1]+y) for x, y in window)


def verify_patterns(data):
    window = [(x, y) for x in range(6) for y in range(9)]
    require(data['column_order_S'] == [list(s) for s in window], '窗口或列顺序不符')
    offsets = [sorted({y-a*x for x, y in window}) for a in (0, 2, 4)]
    require(data['normal_offsets'] == offsets, '法向偏移集不完整')
    for i, j in combinations(range(3), 2):
        # y-2*i*x=i and y-2*j*x=j meet only at noninteger x=-1/2.
        require(Fraction(i-j, 2*j-2*i) == Fraction(-1, 2), '三直线不互斥')
    coverage = {(0,)*54}
    for i in range(3):
        for b in offsets[i]:
            coverage.add(tuple(int(y-2*i*x == b) for x, y in window))
    pair_anchors = set()
    pair_count = 0
    for i, j in combinations(range(3), 2):
        for bi in offsets[i]:
            for bj in offsets[j]:
                # 用两个线性方程消元，Fraction 检查整点条件。
                x = Fraction((i-bi)-(j-bj), 2*j-2*i)
                y = 2*i*x+i-bi
                if x.denominator == y.denominator == 1:
                    u = (int(x), int(y))
                    pair_anchors.add(u)
                    pair_count += 1
                    coverage.add(evaluate(u, window))
    actual = []
    for item in data['patterns']:
        bits = tuple(item['bits'])
        require(len(bits) == 54 and set(bits) <= {0, 1}, '模式不是 54 位二进制')
        require(evaluate(item['anchor'], window) == bits, '实现锚点与模式不符')
        actual.append(bits)
    require(actual == sorted(set(actual)), '模式未唯一化或排序错误')
    require(set(actual) == coverage, '模式集未恰好覆盖全部零/单/多线类别')
    require(len(actual) == 347 and pair_count == 425, '旧基线计数未复现')
    expected_events = set()
    for i, j in combinations(range(3), 2):
        for bi, bj in product(offsets[i], offsets[j]):
            x = Fraction((i-bi)-(j-bj), 2*j-2*i)
            if x.denominator == 1:
                expected_events.add(('two_lines', i, j, bi, bj, int(x), int(2*i*x+i-bi)))
    for i in range(3):
        for b in offsets[i]:
            expected_events.add(('one_line', i, b, 1000, i-b+2*i*1000))
    expected_events.add(('zero_lines', 0, 1000))
    recorded = set()
    for item in data['all_coverage_events']:
        kind = item['type']
        if kind == 'two_lines':
            event = (kind, *item['lines'], *item['offsets'], *item['anchor'])
        elif kind == 'one_line':
            event = (kind, item['line'], item['offset'], *item['anchor'])
        else:
            event = (kind, *item['anchor'])
        recorded.add(event)
    require(recorded == expected_events, '覆盖事件记录缺失或多余')
    return actual, window, {'pattern_count': len(actual), 'pair_events': pair_count,
                           'all_coverage_events': len(expected_events),
                           'distinct_pair_anchors': len(pair_anchors)}


def in_z(x, y):
    # alpha2=t, alpha1=y/2-2t, alpha0=x-y/2+t; 三个系数同时在 [0,1]。
    lower = max(Fraction(0), (Fraction(y, 2)-1)/2, Fraction(y, 2)-x)
    upper = min(Fraction(1), Fraction(y, 4), 1-x+Fraction(y, 2))
    return lower <= upper


def verify_witness(data):
    vectors = ((1, 0), (1, 2), (1, 4))
    require(data['V'] == [list(v) for v in vectors], '方向错误')
    zpoints = [(x, y) for x in range(4) for y in range(7) if in_z(x, y)]
    require(data['Z_lattice_points'] == [list(z) for z in zpoints], 'Z 整点枚举错误')
    require(data['Z_vertices_ccw'] == [[0, 0], [1, 0], [2, 2], [3, 6], [2, 6], [1, 4]], 'Z 顶点错误')
    translations = [(x, y) for x in range(3) for y in range(3)]
    require(data['R_Z_S'] == [list(r) for r in translations], 'R_Z(S) 错误')
    q0, q1, d = map(tuple, (data['q0'], data['q1'], data['d']))
    require(q0 in zpoints and q1 in zpoints, '两个观察点不在 Z')
    require(d == (q1[0]-q0[0], q1[1]-q0[1]) and d != (0, 0), 'd 不是合法差分')
    require((q0, q1, d) == ((0, 0), (1, 1), (1, 1)), '未复现旧见证')
    cross = defaultdict(int)
    solutions = []
    for i in range(3):
        for j in range(3):
            if i == j:
                # 同分量积沿对应 primitive 方向不变，因此被 D 的该因子消去。
                require(vectors[i][1]-2*i*vectors[i][0] == 0, '周期方向不符')
                continue
            rhs1, rhs2 = i, j-(d[1]-2*j*d[0])
            x = Fraction(rhs1-rhs2, 2*j-2*i)
            y = rhs1+2*i*x
            entry = {'i': i, 'j': j, 'integer_solution': None,
                     'numerator': rhs1-rhs2, 'denominator': 2*j-2*i}
            if x.denominator == y.denominator == 1:
                p = (int(x), int(y))
                cross[p] += 1
                entry['integer_solution'] = list(p)
            solutions.append(entry)
    require(data['ordered_cross_pair_solutions'] == solutions, '异分量交点记录错误')
    require(data['cross_term_support'] == [{'point': list(p), 'value': v} for p, v in sorted(cross.items())], '异分量积支撑错误')
    # 逐个施加 T^v-1；不复用生成器的全部子集平移卷积。
    sparse = dict(cross)
    for vx, vy in vectors:
        changed = defaultdict(int)
        for (x, y), value in sparse.items():
            changed[(x-vx, y-vy)] += value
            changed[(x, y)] -= value
        sparse = {p: v for p, v in changed.items() if v}
    expected = [{'point': list(p), 'value': v} for p, v in sorted(sparse.items())]
    require(data['entire_J_support'] == expected and len(sparse) == 12, 'J 全支撑错误')
    operator = {(0, 0): 1}
    for vx, vy in vectors:
        new = defaultdict(int)
        for (x, y), c in operator.items():
            new[(x+vx, y+vy)] += c
            new[(x, y)] -= c
        operator = {p: v for p, v in new.items() if v}
    require(data['difference_operator'] == [{'shift': list(p), 'coefficient': v}
                                           for p, v in sorted(operator.items())], 'D 系数错误')
    possible_support = {(w[0]-h[0], w[1]-h[1]) for w in cross for h in operator}
    for x, y in possible_support:
        direct = sum(c*pixel(x+hx, y+hy)*pixel(x+hx+d[0], y+hy+d[1])
                     for (hx, hy), c in operator.items())
        require(direct == sparse.get((x, y), 0), '有限全候选支撑上的直接公式不符')
    return q0, q1, translations, {'J_support_size': len(sparse),
                                 'entire_possible_support_size': len(possible_support),
                                 'Z_point_count': len(zpoints)}


def determinant_bareiss(matrix):
    """无除尽误差的整系数 Bareiss 算法，与生成器的模素数消元独立。"""
    a = [row[:] for row in matrix]
    n, sign, previous = len(a), 1, 1
    if n == 0:
        return 1
    for k in range(n-1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k+1, n) if a[r][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        current = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = current*a[i][j]-a[i][k]*a[k][j]
                require(numerator % previous == 0, 'Bareiss 应整除处未整除')
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = current
    return sign*a[-1][-1]


def verify_rank(matrix, cert):
    m, n, rank = len(matrix), len(matrix[0]), cert['rank']
    require(all(len(row) == n and all(type(x) is int for x in row) for row in matrix), '矩阵非矩形或非整数')
    require((m, n) == (cert['row_count'], cert['column_count']), '秩证书维度不符')
    lower, upper = cert['lower_bound'], cert['upper_bound']
    ri, ci = lower['minor_rows'], lower['minor_columns']
    require(len(ri) == len(set(ri)) == len(ci) == len(set(ci)) == rank, 'minor 阶数或索引不符')
    require(all(0 <= r < m for r in ri) and all(0 <= c < n for c in ci), 'minor 索引越界')
    minor = [[matrix[r][c] for c in ci] for r in ri]
    det = determinant_bareiss(minor)
    require(det != 0, '秩下界 minor 为零')
    require(det % lower['modulus_prime'] == lower['determinant_mod_prime'], 'minor 模行列式不符')
    kernel, free = upper['integer_right_kernel_basis'], upper['free_columns']
    require(len(kernel) == len(free) == len(set(free)) == n-rank, '核维数不足或重复自由列')
    require(all(0 <= f < n for f in free), '自由列越界')
    for k, v in enumerate(kernel):
        require(len(v) == n and all(type(x) is int for x in v), '核向量格式错误')
        require(v[free[k]] != 0 and all(v[f] == 0 for j, f in enumerate(free) if j != k), '核向量独立性证书错误')
        require(all(sum(a*b for a, b in zip(row, v)) == 0 for row in matrix), 'A v 非零；核证书错误')
    return {'exact_rational_rank': rank, 'minor_exact_determinant': det,
            'kernel_basis_count': len(kernel), 'matrix_shape': [m, n]}


def verify_matrices(data, ranks, patterns, window, q0, q1, translations):
    index = {point: i for i, point in enumerate(window)}
    linear = [[1]+list(row) for row in patterns]
    extended = []
    for row in patterns:
        nonlinear = []
        for rx, ry in translations:
            nonlinear.append(row[index[(rx+q0[0], ry+q0[1])]]*row[index[(rx+q1[0], ry+q1[1])]])
        extended.append([1]+list(row)+nonlinear)
    require(data == {'linear': linear, 'extended': extended}, '证据矩阵与全局模式/观察点不符')
    result = {key: verify_rank(data[key], ranks[key]) for key in ('linear', 'extended')}
    require(result['linear']['exact_rational_rank'] == 46, '线性秩未复现')
    require(result['extended']['exact_rational_rank'] == 55, '扩展秩未复现')
    return result


def main():
    global RESULTS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=RESULTS)
    args = parser.parse_args()
    RESULTS = args.results
    start = time.perf_counter()
    pattern_data = load('patterns.json')
    witness_data = load('witness.json')
    matrix_data = load('matrices.json')
    ranks = load('rank-certificates.json')
    patterns, window, coverage_result = verify_patterns(pattern_data)
    q0, q1, translations, witness_result = verify_witness(witness_data)
    rank_result = verify_matrices(matrix_data, ranks, patterns, window, q0, q1, translations)
    negatives = []

    def rejected(name, callback):
        try:
            callback()
        except ValueError as error:
            negatives.append({'case': name, 'rejected': True, 'reason': str(error)})
        else:
            raise ValueError('负控未拒绝：'+name)

    bad = copy.deepcopy(pattern_data)
    bad['patterns'][0]['bits'][0] ^= 1
    rejected('改坏一个模式位', lambda: verify_patterns(bad))
    bad = copy.deepcopy(pattern_data)
    bad['patterns'].pop()
    rejected('删除一个真实模式', lambda: verify_patterns(bad))
    bad = copy.deepcopy(witness_data)
    bad['entire_J_support'][0]['value'] += 1
    rejected('改坏 J 系数', lambda: verify_witness(bad))
    bad = copy.deepcopy(ranks['linear'])
    bad['lower_bound']['determinant_mod_prime'] += 1
    rejected('改坏下界 minor 行列式', lambda: verify_rank(matrix_data['linear'], bad))
    bad = copy.deepcopy(ranks['linear'])
    bad['upper_bound']['integer_right_kernel_basis'][0][0] += 1
    rejected('改坏上界核向量', lambda: verify_rank(matrix_data['linear'], bad))
    bad = copy.deepcopy(matrix_data)
    bad['extended'][0][0] += 1
    rejected('改坏精确矩阵条目', lambda: verify_matrices(bad, ranks, patterns, window, q0, q1, translations))
    filenames = ['patterns.json', 'witness.json', 'matrices.json',
                 'rank-certificates.json']
    result = {'all_checks_passed': True, 'python_version': platform.python_version(),
              'generator_imported': False, 'generator_read': False,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'external_packages': [],
              'elapsed_seconds': round(time.perf_counter()-start, 6),
              'coverage': coverage_result, 'witness': witness_result,
              'rank_certificates': rank_result, 'negative_controls': negatives,
              'artifact_sha256': {name: hashlib.sha256((RESULTS/name).read_bytes()).hexdigest() for name in filenames}}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
