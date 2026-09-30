#!/usr/bin/env python3
"""独立重建新族；只复用旧独立检查器的秩验收，不导入任何生成器。"""
import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import platform
import time

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "certificates/periodic-background"
HELPER = HERE / 'check_baseline.py'
spec = importlib.util.spec_from_file_location('old_independent_checker', HELPER)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
require = checker.require


def load(name):
    return json.loads((RESULTS/name).read_text(encoding='utf-8'))


def color(x, y):
    background = x % 2
    union = int(y == 0 or y-2*x == 1 or y-4*x == 2)
    return background + (1-2*background)*union


def at(u, window):
    return tuple(color(u[0]+x, u[1]+y) for x, y in window)


def verify_coverage(data):
    window = tuple(product(range(6), range(9)))
    require(data['column_order_S'] == [list(s) for s in window], '窗口/列顺序错误')
    offsets = [sorted({y-2*i*x for x, y in window}) for i in range(3)]
    require(data['normal_offsets'] == offsets, '法向偏移集错误')
    expected, events = set(), set()
    for phase in (0, 1):
        u = (phase, 1000)
        background = tuple((phase+x) % 2 for x, _ in window)
        require(at(u, window) == background, '零线相位锚点错误')
        expected.add(background)
        events.add(('zero_lines', phase, *u))
        for i in range(3):
            for b in offsets[i]:
                row = tuple(bg + (1-2*bg)*int(y-2*i*x == b)
                            for bg, (x, y) in zip(background, window))
                u = (1000+phase, i-b+2*i*(1000+phase))
                require(at(u, window) == row, '单线相位锚点错误')
                expected.add(row)
                events.add(('one_line', i, b, phase, *u))
    count_pair = 0
    for i, j in combinations(range(3), 2):
        require(Fraction(i-j, 2*j-2*i) == Fraction(-1, 2), '三直线不互斥')
        for b in offsets[i]:
            for c in offsets[j]:
                x = Fraction((i-b)-(j-c), 2*j-2*i)
                if x.denominator != 1:
                    continue
                u = (int(x), int(i-b+2*i*x))
                expected.add(at(u, window))
                events.add(('two_lines', i, j, b, c, u[0] % 2, *u))
                count_pair += 1
    actual = []
    for p in data['patterns']:
        row = tuple(p['bits'])
        require(len(row) == 54 and set(row) <= {0, 1}, '模式格式错误')
        require(p['phase'] == p['anchor'][0] % 2, '记录相位错误')
        require(at(p['anchor'], window) == row, '模式与真实锚点不符')
        actual.append(row)
    require(actual == sorted(set(actual)) and set(actual) == expected, '全局模式集不相等')
    recorded = set()
    for event in data['all_coverage_events']:
        kind = event['type']
        if kind == 'two_lines':
            out = (kind, *event['lines'], *event['offsets'], event['phase'], *event['anchor'])
        elif kind == 'one_line':
            out = (kind, event['line'], event['offset'], event['phase'], *event['anchor'])
        else:
            out = (kind, event['phase'], *event['anchor'])
        recorded.add(out)
    require(events == recorded, '覆盖事件缺失或多余')
    require(len(actual) == 401 and count_pair == 425 and len(events) == 541, '新族计数不符')
    return actual, window, {'global_patterns': len(actual), 'pair_events': count_pair,
                           'single_phase_events': 114, 'zero_phase_events': 2,
                           'all_events': len(events)}


def make_operator(vectors, constant):
    operator = {(0, 0): 1}
    for vx, vy in vectors:
        out = defaultdict(int)
        for (x, y), c in operator.items():
            out[(x+vx, y+vy)] += c
            out[(x, y)] += constant*c
        operator = {p: c for p, c in out.items() if c}
    return operator


def apply_to_twice_eta(operator):
    # 2 eta = 1-s + 2 sum_i s delta_i，s=(-1)^x。
    out = defaultdict(int)
    for (x, y), c in operator.items():
        phase = (-1)**x
        out[('constant',)] += c
        out[('parity',)] -= c*phase
        for i in range(3):
            out[('parity_times_line', i, i-(y-2*i*x))] += 2*c*phase
    return {key: value for key, value in out.items() if value}


def verify_witness(data):
    v = ((1, 0), (1, 2), (1, 4))
    h = ((2, 0), (2, 4), (2, 8))
    require(data['V'] == [list(x) for x in v] and data['H'] == [list(x) for x in h], '方向/周期错误')
    require(data['A_i'] == ['t+1']*3 and data['A_eta_constant'] == 4, '异常谱/常数声明错误')
    a = make_operator(v, 1)
    d2 = make_operator(h, -1)
    require(data['A_operator'] == [{'shift': list(p), 'coefficient': c} for p, c in sorted(a.items())], 'A 多项式错误')
    require(data['D2_operator'] == [{'shift': list(p), 'coefficient': c} for p, c in sorted(d2.items())], 'D2 多项式错误')
    require(apply_to_twice_eta(a) == {('constant',): 8}, '全局 A eta = 4 恒等式不成立')
    require(apply_to_twice_eta(d2) == {}, '全局 D2 eta = 0 恒等式不成立')
    z = [(x, y) for x in range(4) for y in range(7) if checker.in_z(x, y)]
    require(data['Z_lattice_points'] == [list(p) for p in z], 'Z 整点不符')
    r = list(product(range(3), range(3)))
    require(data['R_Z_S'] == [list(p) for p in r], 'R_Z(S) 错误')
    q0, q1, delta = map(tuple, (data['q0'], data['q1'], data['d']))
    require(q0 in z and q1 in z and delta == (q1[0]-q0[0], q1[1]-q0[1]), '见证定位错误')
    require(delta != (0, 0), 'd 为零')
    weight = 1 if delta[0] % 2 == 0 else -1
    require(data['cross_weight'] == weight, '交叉项符号错误')
    cross, solutions = defaultdict(int), []
    for i in range(3):
        # B、s 与 delta_i 及其平移都被 2vi 保持，因此所有非交叉项消去。
        require(h[i][0] % 2 == 0 and h[i][1]-2*i*h[i][0] == 0, '消非交叉项的周期不合法')
        for j in range(3):
            if i == j:
                continue
            right1, right2 = i, j-delta[1]+2*j*delta[0]
            x = Fraction(right1-right2, 2*j-2*i)
            y = right1+2*i*x
            sol = {'i': i, 'j': j, 'numerator': right1-right2, 'denominator': 2*j-2*i,
                   'integer_solution': None}
            if x.denominator == y.denominator == 1:
                p = (int(x), int(y))
                cross[p] += 1
                sol['integer_solution'] = list(p)
            solutions.append(sol)
    require(data['ordered_cross_pair_solutions'] == solutions, '交点记录错误')
    require(data['unweighted_cross_support'] == [{'point': list(p), 'value': c} for p, c in sorted(cross.items())], '交叉项支撑错误')
    jfield = {p: weight*c for p, c in cross.items()}
    for vx, vy in h:
        out = defaultdict(int)
        for (x, y), c in jfield.items():
            out[(x-vx, y-vy)] += c
            out[(x, y)] -= c
        jfield = {p: c for p, c in out.items() if c}
    require(data['entire_J_support'] == [{'point': list(p), 'value': c} for p, c in sorted(jfield.items())], 'J 全支撑错误')
    candidates = {(x-sx, y-sy) for x, y in cross for sx, sy in d2}
    for x, y in candidates:
        direct = sum(c*color(x+sx, y+sy)*color(x+sx+delta[0], y+sy+delta[1])
                     for (sx, sy), c in d2.items())
        require(direct == jfield.get((x, y), 0), '原始像素公式与 J 不符')
    require(len(jfield) == 32, 'J 支撑规模未复现')
    return q0, q1, r, {'entire_J_support_size': len(jfield), 'all_candidate_support_size': len(candidates),
                      'A_eta_equals_4_globally': True, 'D2_eta_equals_0_globally': True,
                      'global_identity_method': '形式展开 2eta=1-s+2sum(s delta_i)，精确合并平移原子'}


def verify_matrices(matrix, certs, patterns, window, q0, q1, r):
    index = {p: k for k, p in enumerate(window)}
    linear = [[1, *row] for row in patterns]
    extended = []
    for row in patterns:
        additional = [row[index[(x+q0[0], y+q0[1])]]*row[index[(x+q1[0], y+q1[1])]] for x, y in r]
        extended.append([1, *row, *additional])
    require(matrix == {'linear': linear, 'extended': extended}, '精确矩阵与模式/见证不符')
    result = {key: checker.verify_rank(matrix[key], certs[key]) for key in ('linear', 'extended')}
    require(result['linear']['exact_rational_rank'] == 46 and result['extended']['exact_rational_rank'] == 55, '有理秩不符')
    return result


def main():
    global RESULTS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=RESULTS)
    args = parser.parse_args()
    RESULTS = args.results
    start = time.perf_counter()
    patterns_data = load('patterns.json')
    witness_data = load('witness.json')
    matrices = load('matrices.json')
    certificates = load('rank-certificates.json')
    rows, window, coverage = verify_coverage(patterns_data)
    q0, q1, r, witness = verify_witness(witness_data)
    rank_result = verify_matrices(matrices, certificates, rows, window, q0, q1, r)
    negatives = []

    def reject(name, callback):
        try:
            callback()
        except ValueError as error:
            negatives.append({'case': name, 'rejected': True, 'reason': str(error)})
        else:
            raise ValueError('负控未被拒绝：'+name)

    bad = copy.deepcopy(patterns_data)
    bad['patterns'][0]['phase'] ^= 1
    reject('改锚点相位', lambda: verify_coverage(bad))
    bad = copy.deepcopy(patterns_data)
    bad['patterns'].pop()
    reject('删真实模式', lambda: verify_coverage(bad))
    bad = copy.deepcopy(witness_data)
    bad['cross_weight'] *= -1
    reject('把交叉项相位符号改错', lambda: verify_witness(bad))
    bad = copy.deepcopy(witness_data)
    bad['A_eta_constant'] = 0
    reject('误称周期尾被 A 消成零', lambda: verify_witness(bad))
    bad = copy.deepcopy(witness_data)
    bad['entire_J_support'][0]['value'] += 1
    reject('改 J 系数', lambda: verify_witness(bad))
    bad = copy.deepcopy(certificates['linear'])
    bad['upper_bound']['integer_right_kernel_basis'][0][0] += 1
    reject('改上界核向量', lambda: checker.verify_rank(matrices['linear'], bad))
    names = ['patterns.json', 'witness.json',
             'matrices.json', 'rank-certificates.json']
    result = {'all_checks_passed': True, 'python_version': platform.python_version(),
              'generator_imported': False, 'generator_read': False,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'external_packages': [],
              'elapsed_seconds': round(time.perf_counter()-start, 6),
              'coverage': coverage, 'witness': witness, 'rank_certificates': rank_result,
              'negative_controls': negatives,
              'checker_helper_sha256': hashlib.sha256(HELPER.read_bytes()).hexdigest(),
              'artifact_sha256': {name: hashlib.sha256((RESULTS/name).read_bytes()).hexdigest() for name in names}}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
