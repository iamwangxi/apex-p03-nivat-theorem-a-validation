#!/usr/bin/env python3
"""用单变量扩展 Euclid 和有符号格关系生成闸门证书；不调用检查器。

SymPy 仅用于生成。证书所有分母清为非零 X-Laurent 多项式；
独立标准库检查器负责验收。无函数域参数专门化。
"""
from pathlib import Path
from itertools import combinations, product
from math import gcd
import argparse
import hashlib
import json
import platform
import time

import sympy as s

BASE = Path(__file__).resolve().parent
X1, X2, Y1, Y2, t, q = s.symbols('X1 X2 Y1 Y2 t q')
VARIABLES = (X1, X2, Y1, Y2)
FROZEN_INPUT_SHA256 = 'f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6'
V = KAPPA = AC = AP = D = AY = CY = ()
GENS = {}
M = 0


def configure(case):
    """Validate the frozen input and initialize this one-case process."""
    global V, KAPPA, AC, AP, D, AY, CY, GENS, M
    V = tuple(tuple(v) for v in case['vectors'])
    KAPPA = tuple(case['kappa'])
    AC = tuple(tuple(s.Rational(c) for c in cs) for cs in case['A_coefficients'])
    M = len(V)
    assert M >= 2 and len(KAPPA) == len(AC) == M
    assert all(len(v) == 2 and all(type(e) is int for e in v) and v != (0, 0) for v in V)
    assert all(det(V[i], V[j]) != 0 for i, j in combinations(range(M), 2))
    assert all(type(k) is int and k > 0 for k in KAPPA)
    assert all(len(cs) >= 2 and cs[-1] == 1 and cs[0] != 0 for cs in AC)
    AP = tuple(sum(c*t**k for k, c in enumerate(cs)) for cs in AC)
    D = tuple(len(cs)-1 for cs in AC)
    for a, k in zip(AP, KAPPA):
        assert s.div(t**k-1, a, t)[1] == 0
        assert s.gcd(a, s.diff(a, t)) == 1
    AY = tuple(a.subs(t, mon(v, (Y1, Y2))) for a, v in zip(AP, V))
    CY = tuple(a.subs(t, mon(v, (X1/Y1, X2/Y2))) for a, v in zip(AP, V))
    GENS = {**{'a'+str(i): AY[i] for i in range(M)},
            **{'c'+str(i): CY[i] for i in range(M)}}
    dimension = sum(abs(det(V[i], V[j]))*D[i]*D[j]
                    for i, j in product(range(M), repeat=2) if i != j)
    assert dimension == case['expected_dimension']
    return dimension


def mon(v, xx):
    return xx[0]**v[0] * xx[1]**v[1]


def det(u, v):
    return u[0]*v[1] - u[1]*v[0]




def normalize_fraction(expr):
    """Return Laurent numerator and a denominator in X alone."""
    num, den = s.fraction(s.cancel(expr))
    dp = s.Poly(den, Y1, Y2)
    powers = dp.monoms()
    y1 = min(e[0] for e in powers)
    y2 = min(e[1] for e in powers)
    ym = Y1**y1 * Y2**y2
    denx = s.cancel(den / ym)
    assert not denx.has(Y1, Y2)
    return s.expand(num / ym), denx


def clear(expressions):
    fractions = [normalize_fraction(e) for e in expressions]
    denominator = s.S.One
    for _, den in fractions:
        denominator = s.lcm(denominator, den)
    out = [s.expand(num*s.cancel(denominator/den)) for num, den in fractions]
    assert not denominator.has(Y1, Y2) and denominator != 0
    return out, s.expand(denominator)


def poly(expr):
    """Serialize Q-Laurent polynomial, rejecting hidden expressions."""
    terms = {}
    for term in s.Add.make_args(s.expand(expr)):
        if term == 0:
            continue
        powers = term.as_powers_dict()
        exponents = tuple(int(powers.get(v, 0)) for v in VARIABLES)
        assert all(powers.get(v, 0) == e for v, e in zip(VARIABLES, exponents))
        coeff = s.cancel(term/s.prod(v**e for v, e in zip(VARIABLES, exponents)))
        assert coeff.is_Rational, (term, coeff)
        terms[exponents] = terms.get(exponents, s.S.Zero) + coeff
    return [[str(c), *e] for e, c in sorted(terms.items()) if c]


def unit_record(name, labels, coefficients):
    multipliers, denominator = clear(coefficients)
    # Generator's local self-check is auxiliary; final checker is independent.
    residual = s.expand(sum(c*GENS[g] for c, g in zip(multipliers, labels))-denominator)
    assert residual == 0, (name, residual)
    return {'id': name, 'generators': labels,
            'multipliers': [poly(c) for c in multipliers],
            'denominator': poly(denominator)}


def euclid(p, r):
    a, b, h = s.gcdex(p, r, t, domain=s.QQ.frac_field(q))
    assert h == 1
    assert s.cancel(a*p+b*r-1) == 0
    return a, b


def geom(u, n):
    if n >= 0:
        return sum(u**r for r in range(n))
    return -sum(u**r for r in range(n, 0))


def aac(i, k, j):
    """1 = coefficients dot (a_i,a_k,c_j), with i<k."""
    delta = det(V[i], V[k])
    N = KAPPA[i]*KAPPA[k]//gcd(KAPPA[i], KAPPA[k])*abs(delta)
    pi_num = N*det(V[j], V[k])
    pk_num = N*det(V[i], V[j])
    assert pi_num % (delta*KAPPA[i]) == 0
    assert pk_num % (delta*KAPPA[k]) == 0
    pi = pi_num//(delta*KAPPA[i])
    pk = pk_num//(delta*KAPPA[k])
    ui, uk = mon(V[i], (Y1, Y2)), mon(V[k], (Y1, Y2))
    U, W = ui**KAPPA[i], uk**KAPPA[k]
    hi = s.div(t**KAPPA[i]-1, AP[i], t)[0].subs(t, ui)
    hk = s.div(t**KAPPA[k]-1, AP[k], t)[0].subs(t, uk)
    li = geom(U, pi)*W**pk*hi
    lk = geom(W, pk)*hk
    u = mon(V[j], (Y1, Y2))
    assert s.expand(li*AY[i]+lk*AY[k]-(u**N-1)) == 0
    reciprocal = s.expand(t**D[j]*AP[j].subs(t, q/t))
    h, b = euclid(t**N-1, reciprocal)
    sub = {t: u, q: mon(V[j], (X1, X2))}
    h, b = h.subs(sub, simultaneous=True), b.subs(sub, simultaneous=True)
    return [s.cancel(h*li), s.cancel(h*lk), s.cancel(b*u**D[j])], {
        'i': i, 'k': k, 'j': j, 'N': N, 'p': pi, 'r': pk}


def sigma(expr):
    return s.cancel(expr.subs({Y1: X1/Y1, Y2: X2/Y2}, simultaneous=True))


def representatives(i, j):
    v, w = V[i], tuple(-e for e in V[j])
    corners = [(0, 0), v, w, (v[0]+w[0], v[1]+w[1])]
    ans = []
    den = det(v, w)
    for x in range(min(c[0] for c in corners), max(c[0] for c in corners)+1):
        for y in range(min(c[1] for c in corners), max(c[1] for c in corners)+1):
            p = (x, y)
            alpha, beta = s.Rational(det(p, w), den), s.Rational(det(v, p), den)
            if 0 <= alpha < 1 and 0 <= beta < 1:
                ans.append(p)
    assert len(ans) == abs(det(V[i], V[j]))
    return ans


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-list', type=Path, default=BASE.parent/'certificates/boundary/frozen-inputs.json')
    parser.add_argument('--case', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--stats', type=Path, required=True)
    args = parser.parse_args()
    if s.__version__ != '1.14.0':
        raise RuntimeError('Regeneration requires sympy==1.14.0')
    if args.output.exists() or args.stats.exists():
        raise FileExistsError('Choose fresh output and statistics files')
    shipped = (BASE.parent/'certificates').resolve()
    for path in (args.output, args.stats):
        if path.resolve() == shipped or shipped in path.resolve().parents:
            raise ValueError('Regeneration must not write into shipped certificates')
    started = time.monotonic()
    input_bytes = args.input_list.read_bytes()
    assert hashlib.sha256(input_bytes).hexdigest() == FROZEN_INPUT_SHA256, 'Frozen input hash changed'
    manifest = json.loads(input_bytes)
    cases = [case for case in manifest['cases'] if case['id'] == args.case]
    assert len(cases) == 1
    case = cases[0]
    expected_dimension = configure(case)
    print('case', args.case, 'm', M, 'dimension', expected_dimension, flush=True)
    units, raw, lattice = [], {}, []
    for i in range(M):
        a, b = euclid(AP[i], s.expand(t**D[i]*AP[i].subs(t, q/t)))
        u = mon(V[i], (Y1, Y2))
        sub = {t: u, q: mon(V[i], (X1, X2))}
        coeffs = [a.subs(sub, simultaneous=True), b.subs(sub, simultaneous=True)*u**D[i]]
        units.append(unit_record('diagonal_'+str(i), ['a'+str(i), 'c'+str(i)], coeffs))
        print('generated', units[-1]['id'], flush=True)
    for i, k in combinations(range(M), 2):
        for j in range(M):
            coeffs, relation = aac(i, k, j)
            raw[i, k, j] = coeffs
            lattice.append(relation)
            units.append(unit_record(f'aac_{i}_{k}_{j}', [f'a{i}', f'a{k}', f'c{j}'], coeffs))
            print('generated', units[-1]['id'], flush=True)
    for i in range(M):
        for j, ell in combinations(range(M), 2):
            old = raw[j, ell, i]
            coeffs = [sigma(old[2]), sigma(old[0]), sigma(old[1])]
            raw['acc', i, j, ell] = coeffs
            units.append(unit_record(f'acc_{i}_{j}_{ell}', [f'a{i}', f'c{j}', f'c{ell}'], coeffs))
            print('generated', units[-1]['id'], flush=True)
    components = []
    for i, j in product(range(M), repeat=2):
        if i == j:
            continue
        # Maintain N*F+Q*a_i+R*c_j=D0. Multiplication is telescoped.
        N0, Q, R, D0, F = s.S.One, s.S.Zero, s.S.Zero, s.S.One, s.S.One
        factors = []
        for k in range(M):
            if k == i:
                continue
            lo, hi = sorted((i, k))
            co = raw[lo, hi, j]
            coeff_n, coeff_q = (co[1], co[0]) if i == lo else (co[0], co[1])
            factors.append((AY[k], [coeff_n, coeff_q, co[2]]))
        for ell in range(M):
            if ell == j:
                continue
            lo, hi = sorted((j, ell))
            co = raw['acc', i, lo, hi]
            coeff_n, coeff_r = (co[2], co[1]) if j == lo else (co[1], co[2])
            factors.append((CY[ell], [coeff_n, co[0], coeff_r]))
        for factor, co in factors:
            (n, qa, rc), den = clear(co)
            Q, R = s.expand(Q*den+N0*F*qa), s.expand(R*den+N0*F*rc)
            N0, D0, F = s.expand(N0*n), s.expand(D0*den), s.expand(F*factor)
        assert s.expand(N0*F+Q*AY[i]+R*CY[j]-D0) == 0
        # Remove common factors via a single rational normalization.
        multipliers, denominator = clear([N0/D0, Q/D0, R/D0])
        assert s.expand(multipliers[0]*F+multipliers[1]*AY[i]+multipliers[2]*CY[j]-denominator) == 0
        reps = representatives(i, j)
        basis = sorted((r[0]+a*V[i][0]-b*V[j][0], r[1]+a*V[i][1]-b*V[j][1])
                       for r in reps for a in range(D[i]) for b in range(D[j]))
        components.append({'i': i, 'j': j, 'representatives': reps, 'basis_exponents': basis,
                           'inverse_E': {'multipliers': [poly(c) for c in multipliers],
                                         'denominator': poly(denominator)}})
        print('generated E inverse', i, j, 'basis', len(basis), flush=True)
    cert = {'schema': 'convex-nivat-gate-v1', 'variables': [str(v) for v in VARIABLES],
            'vectors': V, 'A_coefficients': case['A_coefficients'], 'kappa': KAPPA,
            'units': units, 'components': components, 'expected_dimension': expected_dimension,
            'construction_lattice_relations': lattice,
            'limitations': ['Fixed algebraic input only; no associated star configuration is asserted.',
                           'Dimension uses the proved lattice-module and tensor-product basis theorem.']}
    text = json.dumps(cert, indent=2, ensure_ascii=False)+'\n'
    args.output.write_text(text, encoding='utf-8')
    stats = {'case_id': args.case, 'frozen_input_sha256': FROZEN_INPUT_SHA256, 'python': platform.python_version(), 'sympy': s.__version__,
             'elapsed_seconds': round(time.monotonic()-started, 4),
             'unit_identities': len(units), 'component_inverse_identities': len(components),
             'dimension': sum(len(c['basis_exponents']) for c in components),
             'certificate_sha256': hashlib.sha256(text.encode()).hexdigest(),
             'certificate_bytes': len(text.encode()), 'parameters_specialized': False}
    args.stats.write_text(json.dumps(stats, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(stats, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
