#!/usr/bin/env python3
"""Nivat frozen-boundary certificate checker; Python standard library only.

Usage: python3 -B code/check_boundary.py certificates/boundary/B01.json --case B01 --self-test
输入目标来自单独冻结并固定 SHA-256 的清单，不接受证书重新定义目标。
未读取、导入或调用生成器；不搜索 Bezout 系数，不作数值正面验收。
所有证书恒等式均逐项在 Q[X1^±1,X2^±1,Y1^±1,Y2^±1] 中比较。
程序只读取显式证书、冻结清单和自身文件；结果只写标准输出。
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import re
import sys

SCHEMA = "convex-nivat-gate-v1"
MANIFEST_SCHEMA = "convex-nivat-boundary-inputs-v1"
FROZEN_MANIFEST_SHA256 = "f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6"
VARIABLES = ["X1", "X2", "Y1", "Y2"]
ONE = {(0, 0, 0, 0): Fraction(1)}
COEFF_RE = re.compile(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z")


class Rejected(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Rejected(message)


def keys_exact(obj, keys, label):
    require(type(obj) is dict, label + ": 必须是对象")
    require(set(obj) == set(keys), label + ": 字段集合不符")


def integer(value, label):
    require(type(value) is int, label + ": 必须是整数，拒绝bool/float")
    return value


def integer_vector(value, dimension, label):
    require(type(value) is list and len(value) == dimension, label + ": 向量长度不符")
    return tuple(integer(x, label) for x in value)


def integer_tree(value, label):
    if type(value) is list:
        for item in value:
            integer_tree(item, label)
    else:
        integer(value, label)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON含重复字段: " + key)
        result[key] = value
    return result


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def polynomial_division(dividend, divisor):
    """低阶在前的 Q[t] 长除法；只检查输入假设，不寻找证书乘子。"""
    remainder = [Fraction(c) for c in dividend]
    divisor = [Fraction(c) for c in divisor]
    while remainder and not remainder[-1]:
        remainder.pop()
    require(bool(divisor) and divisor[-1] != 0, "除式的最高项必须非零")
    quotient = [Fraction(0)] * max(0, len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[shift] += coefficient
        for k, c in enumerate(divisor):
            remainder[shift + k] -= coefficient * c
        while remainder and not remainder[-1]:
            remainder.pop()
    return quotient, remainder


def validate_case(case):
    """独立检查清单前提及维数，返回内部目标；不从证书获取输入。"""
    keys_exact(case, ["id", "vectors", "A_coefficients", "kappa", "expected_dimension", "purpose"],
               "manifest.case")
    require(type(case["id"]) is str and bool(case["id"]), "case.id必须是非空字符串")
    require(type(case["purpose"]) is str, "case.purpose必须是字符串")
    require(type(case["vectors"]) is list and len(case["vectors"]) >= 2, "m必须至少为2")
    vectors = [integer_vector(v, 2, "case.vectors") for v in case["vectors"]]
    m = len(vectors)
    require(all(v != (0, 0) for v in vectors), "方向必须非零")
    require(all(det(vectors[i], vectors[j]) != 0 for i in range(m) for j in range(i + 1, m)),
            "方向必须两两不平行")
    require(type(case["A_coefficients"]) is list and len(case["A_coefficients"]) == m,
            "A_coefficients数量不符")
    require(type(case["kappa"]) is list and len(case["kappa"]) == m, "kappa数量不符")
    degrees = []
    divisibility = []
    for i, coefficients in enumerate(case["A_coefficients"]):
        require(type(coefficients) is list and len(coefficients) >= 2, f"A{i}必须为正次数多项式")
        integer_tree(coefficients, f"A{i}.coefficients")
        require(coefficients[-1] == 1, f"A{i}必须首一")
        require(coefficients[0] != 0, f"A{i}常数项必须非零")
        kappa = integer(case["kappa"][i], f"kappa[{i}]")
        require(kappa > 0, "kappa必须为正整数")
        degree = len(coefficients) - 1
        require(degree <= kappa, f"A{i}次数大于kappa")
        target = [-1] + [0] * (kappa - 1) + [1]
        quotient, remainder = polynomial_division(target, coefficients)
        require(not remainder, f"A{i}不整除t^{kappa}-1")
        degrees.append(degree)
        divisibility.append({"i": i, "degree": degree, "kappa": kappa,
                             "quotient_coefficients": [str(c) for c in quotient], "verified": True})
    dimension = sum(abs(det(vectors[i], vectors[j])) * degrees[i] * degrees[j]
                    for i in range(m) for j in range(m) if i != j)
    require(integer(case["expected_dimension"], "case.expected_dimension") == dimension,
            "清单预期维数与独立计算不符")
    return {"case": copy.deepcopy(case), "m": m, "vectors": vectors, "degrees": degrees,
            "dimension": dimension, "divisibility": divisibility,
            "all_directions_primitive": all(gcd(abs(v[0]), abs(v[1])) == 1 for v in vectors),
            "support_bounds": [sum(degrees[j] * abs(det(vectors[i], vectors[j])) for j in range(m))
                               for i in range(m)]}


def load_manifest(raw):
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == FROZEN_MANIFEST_SHA256, "冻结输入清单SHA-256不符；禁止修改或替换清单")
    manifest = json.loads(raw, object_pairs_hook=unique_keys)
    keys_exact(manifest, ["schema", "frozen_at", "selection", "case_count", "scope", "cases"], "manifest")
    require(manifest["schema"] == MANIFEST_SCHEMA, "清单schema不符")
    require(type(manifest["cases"]) is list, "清单cases必须是列表")
    require(integer(manifest["case_count"], "manifest.case_count") == len(manifest["cases"]),
            "清单case_count不符")
    targets = {}
    for case in manifest["cases"]:
        target = validate_case(case)
        require(case["id"] not in targets, "清单case id重复")
        targets[case["id"]] = target
    return targets


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
            if not result[exponent]:
                del result[exponent]
    return result


def multiply(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            exponent = tuple(x + y for x, y in zip(a, b))
            result[exponent] = result.get(exponent, Fraction(0)) + ca * cb
            if not result[exponent]:
                del result[exponent]
    return result


def product(polynomials):
    result = dict(ONE)
    for polynomial in polynomials:
        result = multiply(result, polynomial)
    return result


def monomial(exponent, coefficient=1):
    return {tuple(exponent): Fraction(coefficient)} if coefficient else {}


def parse_poly(value, label):
    require(type(value) is list, label + ": 多项式必须是列表")
    result = {}
    for index, row in enumerate(value):
        where = label + f"[{index}]"
        require(type(row) is list and len(row) == 5, where + ": 项长度必须为5")
        coefficient = row[0]
        require(type(coefficient) is str and COEFF_RE.fullmatch(coefficient),
                where + ": 系数必须为整数或有理数字符串")
        coefficient = Fraction(coefficient)
        require(coefficient != 0, where + ": 稀疏格式不得含零系数项")
        exponent = tuple(integer(e, where) for e in row[1:])
        require(exponent not in result, where + ": 重复单项式")
        result[exponent] = coefficient
    return result


def serialize_poly(polynomial):
    return [[str(coefficient), *exponent] for exponent, coefficient in sorted(polynomial.items())]


def reconstruct_generators(target):
    generators = {}
    for i, (v1, v2) in enumerate(target["vectors"]):
        coefficients = target["case"]["A_coefficients"][i]
        generators[f"a{i}"] = add(*(monomial((0, 0, k * v1, k * v2), c)
                                    for k, c in enumerate(coefficients)))
        generators[f"c{i}"] = add(*(monomial((k * v1, k * v2, -k * v1, -k * v2), c)
                                    for k, c in enumerate(coefficients)))
    return generators


def required_units(m):
    records = {}
    for i in range(m):
        records[f"diagonal_{i}"] = [f"a{i}", f"c{i}"]
    for i in range(m):
        for k in range(i + 1, m):
            for j in range(m):
                records[f"aac_{i}_{k}_{j}"] = [f"a{i}", f"a{k}", f"c{j}"]
    for i in range(m):
        for j in range(m):
            for ell in range(j + 1, m):
                records[f"acc_{i}_{j}_{ell}"] = [f"a{i}", f"c{j}", f"c{ell}"]
    return records


def check_identity(record, target_polynomials, label):
    require(type(record["multipliers"]) is list
            and len(record["multipliers"]) == len(target_polynomials), label + ": 乘子数量不符")
    denominator = parse_poly(record["denominator"], label + ".denominator")
    require(bool(denominator), label + ": 清分母必须非零")
    require(all(e[2:] == (0, 0) for e in denominator), label + ": 分母必须只含独立参数X1、X2")
    multipliers = [parse_poly(p, label + f".multipliers[{i}]")
                   for i, p in enumerate(record["multipliers"])]
    left = add(*(multiply(p, g) for p, g in zip(multipliers, target_polynomials)))
    if left != denominator:
        difference = add(left, {e: -c for e, c in denominator.items()})
        first = next(iter(sorted(difference.items())))
        raise Rejected(label + ": Laurent恒等式不成立；首个差项=" + str((first[0], str(first[1]))))
    return {"id": label, "multiplier_terms": [len(p) for p in multipliers],
            "denominator_terms": len(denominator), "verified": True}


def lattice_coordinates(point, first, second):
    determinant = det(first, second)
    require(determinant != 0, "方向对必须非平行")
    return (Fraction(det(point, second), determinant), Fraction(det(first, point), determinant))


def check_representatives(raw, i, j, target):
    label = f"component_{i}_{j}.representatives"
    require(type(raw) is list, label + ": 必须是列表")
    representatives = [integer_vector(r, 2, label) for r in raw]
    first = target["vectors"][i]
    second = tuple(-x for x in target["vectors"][j])
    lattice_index = abs(det(first, second))
    require(len(representatives) == lattice_index, label + ": 陪集代表数量不符")
    for r in representatives:
        coordinates = lattice_coordinates(r, first, second)
        require(all(0 <= x < 1 for x in coordinates), label + ": 不在指定半开平行四边形")
    for k, r in enumerate(representatives):
        for s in representatives[k + 1:]:
            coordinates = lattice_coordinates((r[0] - s[0], r[1] - s[1]), first, second)
            require(not all(x.denominator == 1 for x in coordinates), label + ": 同一格陪集重复")
    return representatives, lattice_index


def point_in_difference_zonotope(point, target):
    # 满维二维zonotope的全部边平行于输入方向；下列正负法向即完整面不等式。
    return all(abs(det(v, point)) <= bound
               for v, bound in zip(target["vectors"], target["support_bounds"]))


def check_gate(certificate, target):
    required_fields = {"schema", "variables", "vectors", "A_coefficients", "kappa",
                       "units", "components", "expected_dimension"}
    require(type(certificate) is dict and required_fields <= set(certificate), "根对象缺少必备字段")
    require(set(certificate) <= required_fields | {"construction_lattice_relations", "limitations"},
            "根对象含未知字段")
    require(certificate["schema"] == SCHEMA, "schema不符")
    require(certificate["variables"] == VARIABLES, "必须保留四个具名独立变量")
    for name in ["vectors", "A_coefficients", "kappa"]:
        require(certificate[name] == target["case"][name], name + ": 与冻结case不符")
        integer_tree(certificate[name], name)
    require(integer(certificate["expected_dimension"], "expected_dimension") == target["dimension"],
            "证书预期维数与独立计算不符")
    m, vectors, degrees = target["m"], target["vectors"], target["degrees"]
    generators = reconstruct_generators(target)
    expected_units = required_units(m)
    units = certificate["units"]
    require(type(units) is list and len(units) == len(expected_units),
            f"必须恰有{len(expected_units)}条基本单位证书")
    unit_ids = set()
    identity_results = []
    for record in units:
        keys_exact(record, ["id", "generators", "multipliers", "denominator"], "unit")
        label = record["id"]
        require(type(label) is str and label in expected_units, "未知的unit id")
        require(label not in unit_ids, label + ": 重复unit")
        unit_ids.add(label)
        require(record["generators"] == expected_units[label], label + ": 目标生成元不符")
        identity_results.append(check_identity(record, [generators[n] for n in expected_units[label]], label))
    require(unit_ids == set(expected_units), "unit集合不完整")
    components = certificate["components"]
    require(type(components) is list and len(components) == m * (m - 1),
            f"必须恰有{m * (m - 1)}个有序分量")
    pairs = set()
    component_results = []
    total_dimension = 0
    support_point_checks = 0
    for component in components:
        keys_exact(component, ["i", "j", "representatives", "basis_exponents", "inverse_E"], "component")
        i = integer(component["i"], "component.i")
        j = integer(component["j"], "component.j")
        require(0 <= i < m and 0 <= j < m and i != j, "非法分量索引")
        require((i, j) not in pairs, "重复分量")
        pairs.add((i, j))
        representatives, lattice_index = check_representatives(component["representatives"], i, j, target)
        expected_exponents = {
            (r[0] + alpha * vectors[i][0] - beta * vectors[j][0],
             r[1] + alpha * vectors[i][1] - beta * vectors[j][1])
            for r in representatives for alpha in range(degrees[i]) for beta in range(degrees[j])
        }
        dimension = lattice_index * degrees[i] * degrees[j]
        require(len(expected_exponents) == dimension, "构造的局部基指数碰撞")
        require(type(component["basis_exponents"]) is list, "basis_exponents必须是列表")
        supplied = [integer_vector(e, 2, "basis_exponents") for e in component["basis_exponents"]]
        require(len(supplied) == dimension and set(supplied) == expected_exponents,
                f"component_{i}_{j}: 局部基指数集合不完整或含额外项")
        E = product([generators[f"a{k}"] for k in range(m) if k != i]
                    + [generators[f"c{ell}"] for ell in range(m) if ell != j])
        inverse = component["inverse_E"]
        keys_exact(inverse, ["multipliers", "denominator"], "inverse_E")
        identity_results.append(check_identity(inverse, [E, generators[f"a{i}"], generators[f"c{j}"]],
                                               f"E_inverse_{i}_{j}"))
        support = set()
        per_basis_support = []
        for e in sorted(expected_exponents):
            vector = multiply(E, monomial((0, 0, e[0], e[1])))
            y_support = {term[2:] for term in vector}
            require(all(point_in_difference_zonotope(p, target) for p in y_support),
                    f"E_{i}{j}Y^{e}: 支撑超出Z-Z")
            support_point_checks += len(y_support)
            support.update(y_support)
            per_basis_support.append({"exponent": list(e), "Y_support_size": len(y_support)})
        component_results.append({"pair": [i, j], "signed_det_vi_vj": det(vectors[i], vectors[j]),
                                  "lattice_index": lattice_index, "dimension": dimension,
                                  "representatives": [list(r) for r in representatives],
                                  "basis_exponents": [list(e) for e in sorted(expected_exponents)],
                                  "E_terms": len(E), "Y_support_union_size": len(support),
                                  "basis_support_checks": per_basis_support})
        total_dimension += dimension
    require(pairs == {(i, j) for i in range(m) for j in range(m) if i != j}, "有序分量集合不完整")
    require(total_dimension == target["dimension"], "分量维数之和不符")
    return {"status": "PASS", "case_id": target["case"]["id"], "schema": SCHEMA,
            "exact_coefficient_domain": "Q", "variables": VARIABLES, "m": m,
            "input_divisibility": target["divisibility"],
            "all_directions_primitive": target["all_directions_primitive"],
            "unit_identity_count": len(expected_units), "E_inverse_identity_count": len(pairs),
            "component_count": len(pairs), "spanning_vector_count": total_dimension,
            "dimension_from_structure": total_dimension, "support_point_checks": support_point_checks,
            "support_inequalities": [{"v": list(v), "bound": b}
                                     for v, b in zip(vectors, target["support_bounds"])],
            "dimension_dependency": "依赖格陪集自由模、两个单变量商的张量基和两次CRT的一般证明；不是逻辑内核形式化证明。",
            "scope": "冻结有理输入上的Lemma 5.2代数实现；不声明对应星形配置，不代表整篇论文获证。B06非原始方向仅属代数扩展。",
            "ignored_metadata": sorted(set(certificate) - required_fields),
            "identities": identity_results, "components": sorted(component_results, key=lambda x: x["pair"])}


def specialize_polynomial(value):
    polynomial = parse_poly(value, "负控专门化输入")
    result = {}
    for (x1, x2, y1, y2), coefficient in polynomial.items():
        coefficient *= Fraction(2) ** x1 * Fraction(3) ** x2
        exponent = (0, 0, y1, y2)
        result[exponent] = result.get(exponent, Fraction(0)) + coefficient
        if not result[exponent]:
            del result[exponent]
    return serialize_poly(result)


def self_test(valid_certificate, target, manifest_raw):
    """负控只改内存副本。所有拒绝均须由明确的 Rejected 产生。"""
    results = []

    def must_reject(name, action):
        try:
            action()
        except Rejected as error:
            results.append({"test": name, "status": "REJECTED_AS_REQUIRED", "reason": str(error)})
        else:
            raise Rejected("负控未被拒绝: " + name)

    def rejected_mutation(name, mutate):
        altered = copy.deepcopy(valid_certificate)
        mutate(altered)
        must_reject(name, lambda: check_gate(altered, target))

    def add_one_to_multiplier(record, index=0):
        polynomial = parse_poly(record["multipliers"][index], "负控")
        record["multipliers"][index] = serialize_poly(add(polynomial, ONE))

    def specialize_all(certificate):
        records = certificate["units"] + [c["inverse_E"] for c in certificate["components"]]
        for record in records:
            record["denominator"] = specialize_polynomial(record["denominator"])
            record["multipliers"] = [specialize_polynomial(p) for p in record["multipliers"]]

    def wrong_negative_det_representative(certificate):
        component = next(c for c in certificate["components"]
                         if det(target["vectors"][c["i"]], target["vectors"][c["j"]]) < 0)
        v = target["vectors"][component["i"]]
        r = component["representatives"][0]
        component["representatives"][0] = [r[0] + v[0], r[1] + v[1]]

    def half_open_endpoint(certificate):
        component = certificate["components"][0]
        component["representatives"][0] = list(target["vectors"][component["i"]])

    rejected_mutation("改动一个单位乘子系数", lambda c: add_one_to_multiplier(c["units"][0]))
    rejected_mutation("改动E逆元乘子", lambda c: add_one_to_multiplier(c["components"][0]["inverse_E"]))
    rejected_mutation("漏掉一条单位证书", lambda c: c["units"].pop())
    rejected_mutation("重复单位替代缺失单位",
                      lambda c: c["units"].__setitem__(1, copy.deepcopy(c["units"][0])))
    rejected_mutation("漏掉一个局部基元素", lambda c: c["components"][0]["basis_exponents"].pop())
    rejected_mutation("重复局部基指数", lambda c: c["components"][0]["basis_exponents"].append(
        copy.deepcopy(c["components"][0]["basis_exponents"][0])))
    rejected_mutation("负行列式分量使用错误平移的陪集代表", wrong_negative_det_representative)
    rejected_mutation("半开代表误含端点alpha等于1", half_open_endpoint)
    rejected_mutation("将全部证书X真正代入2和3但保留声明", specialize_all)
    rejected_mutation("分母含Y变量", lambda c: c["units"][0].__setitem__("denominator", [["1", 0, 0, 1, 0]]))
    rejected_mutation("零分母", lambda c: c["units"][0].__setitem__("denominator", []))
    rejected_mutation("重复分量替代缺失分量",
                      lambda c: c["components"].__setitem__(1, copy.deepcopy(c["components"][0])))
    rejected_mutation("篡改vectors元数据", lambda c: c["vectors"][0].__setitem__(0, c["vectors"][0][0] + 1))
    rejected_mutation("篡改A系数元数据", lambda c: c["A_coefficients"][0].__setitem__(0, c["A_coefficients"][0][0] + 1))
    rejected_mutation("篡改kappa元数据", lambda c: c["kappa"].__setitem__(0, c["kappa"][0] + 1))
    rejected_mutation("篡改预期维数", lambda c: c.__setitem__("expected_dimension", c["expected_dimension"] + 1))
    rejected_mutation("替换独立变量声明", lambda c: c["variables"].__setitem__(0, "2"))
    rejected_mutation("错误有理系数类型float", lambda c: c["units"][0]["denominator"][0].__setitem__(0, 1.0))
    rejected_mutation("错误整数指数类型bool", lambda c: c["units"][0]["denominator"][0].__setitem__(1, True))
    rejected_mutation("有理系数分母为零", lambda c: c["units"][0]["denominator"][0].__setitem__(0, "1/0"))
    rejected_mutation("稀疏表示重复单项式", lambda c: c["units"][0]["denominator"].append(
        copy.deepcopy(c["units"][0]["denominator"][0])))
    must_reject("JSON重复字段", lambda: json.loads('{"schema":1,"schema":2}', object_pairs_hook=unique_keys))
    must_reject("修改冻结清单字节", lambda: load_manifest(manifest_raw + b"\n"))

    def invalid_case(name, mutate):
        case = copy.deepcopy(target["case"])
        mutate(case)
        must_reject(name, lambda: validate_case(case))

    invalid_case("输入方向为零", lambda c: c["vectors"].__setitem__(0, [0, 0]))
    invalid_case("输入方向平行", lambda c: c["vectors"].__setitem__(1, copy.deepcopy(c["vectors"][0])))
    invalid_case("输入kappa非正", lambda c: c["kappa"].__setitem__(0, 0))
    invalid_case("输入A非首一", lambda c: c["A_coefficients"][0].__setitem__(-1, 2))
    invalid_case("输入A常数项为零", lambda c: c["A_coefficients"][0].__setitem__(0, 0))
    invalid_case("输入A不整除单位根多项式", lambda c: c["A_coefficients"].__setitem__(0, [2, 1]))

    # 直接校准几何检查核：错误绝对值分母应产生 (-1/2,-1/2)。
    point, first, second = (0, -1), (1, 0), (-1, -2)
    require(lattice_coordinates(point, first, second) == (Fraction(1, 2), Fraction(1, 2)),
            "负行列式坐标自检失败")
    vertices = {(0, 0)}
    for v, degree in zip(target["vectors"], target["degrees"]):
        vertices = {(p[0] + sign * degree * v[0], p[1] + sign * degree * v[1])
                    for p in vertices for sign in [-1, 1]}
    require(all(point_in_difference_zonotope(p, target) for p in vertices), "zonotope顶点检查失败")
    # 任意第一个方向的独立法向取足够大的整数倍，必越过已知支持线。
    v = target["vectors"][0]
    scale = target["support_bounds"][0] + 1
    outside = (-scale * v[1], scale * v[0])
    require(not point_in_difference_zonotope(outside, target), "zonotope外点未被拒绝")
    return results, {"negative_signed_determinant_coordinates": "PASS",
                     "all_signed_endpoint_sums_inside_Z_minus_Z": len(vertices),
                     "known_outside_point_rejected": list(outside)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).resolve().parent.parent / "certificates/boundary/frozen-inputs.json")
    parser.add_argument("--case", required=True, help="冻结清单中的case id")
    parser.add_argument("--self-test", action="store_true", help="验收通过后执行内存负控")
    args = parser.parse_args()
    try:
        manifest_raw = args.manifest.read_bytes()
        targets = load_manifest(manifest_raw)
        require(args.case in targets, "指定case不在冻结清单中")
        raw = args.certificate.read_bytes()
        certificate = json.loads(raw, object_pairs_hook=unique_keys)
        result = check_gate(certificate, targets[args.case])
        result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
        result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        result["manifest_sha256"] = hashlib.sha256(manifest_raw).hexdigest()
        result["manifest_case_count"] = len(targets)
        if args.self_test:
            controls, kernels = self_test(certificate, targets[args.case], manifest_raw)
            result["negative_controls"] = controls
            result["negative_control_count"] = len(controls)
            result["kernel_positive_checks"] = kernels
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Rejected, OSError, json.JSONDecodeError, UnicodeDecodeError) as error:
        print(json.dumps({"status": "FAIL", "case_id": args.case, "reason": str(error)},
                         ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
