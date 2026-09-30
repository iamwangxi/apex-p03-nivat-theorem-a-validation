#!/usr/bin/env python3
"""Nivat fixed symbolic-gate checker: standard library only; no generator is read or imported.

所有恒等式均在 Q[X1^±1,X2^±1,Y1^±1,Y2^±1] 中展开后精确比较。
不搜索 Bézout 系数，不调用 Gröbner 基，不对 X 作数值代入。
--self-test 的 X 专门化仅是必须失败的负控。
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys

SCHEMA = "convex-nivat-gate-v1"
VARIABLES = ["X1", "X2", "Y1", "Y2"]
VECTORS = [[1, 0], [0, 1], [1, 2]]
A_COEFFICIENTS = [[-1, 1], [1, 1], [1, 0, 1]]
KAPPA = [1, 2, 4]
DEGREES = [1, 1, 2]
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


def reconstruct_generators():
    """直接由任务书固定输入重建，绝不读取证书里的自由表达式。"""
    generators = {}
    for i, (v1, v2) in enumerate(VECTORS):
        generators[f"a{i}"] = add(*(monomial((0, 0, k*v1, k*v2), c)
                                    for k, c in enumerate(A_COEFFICIENTS[i])))
        generators[f"c{i}"] = add(*(monomial((k*v1, k*v2, -k*v1, -k*v2), c)
                                    for k, c in enumerate(A_COEFFICIENTS[i])))
    return generators


def required_units():
    records = {}
    for i in range(3):
        records[f"diagonal_{i}"] = [f"a{i}", f"c{i}"]
    for i in range(3):
        for k in range(i+1, 3):
            for j in range(3):
                records[f"aac_{i}_{k}_{j}"] = [f"a{i}", f"a{k}", f"c{j}"]
    for i in range(3):
        for j in range(3):
            for ell in range(j+1, 3):
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
        raise Rejected(label + ": Laurent恒等式不成立；首个差项="
                       + str((first[0], str(first[1]))))
    return {"id": label, "multiplier_terms": [len(p) for p in multipliers],
            "denominator_terms": len(denominator), "verified": True}


def det(u, v):
    return u[0]*v[1] - u[1]*v[0]


def lattice_coordinates(point, first, second):
    determinant = det(first, second)
    require(determinant != 0, "方向对必须非平行")
    return (Fraction(det(point, second), determinant), Fraction(det(first, point), determinant))


def check_representatives(raw, i, j):
    label = f"component_{i}_{j}.representatives"
    require(type(raw) is list, label + ": 必须是列表")
    representatives = [integer_vector(r, 2, label) for r in raw]
    first = VECTORS[i]
    second = [-x for x in VECTORS[j]]
    lattice_index = abs(det(first, second))
    require(len(representatives) == lattice_index, label + ": 陪集代表数量不符")
    for r in representatives:
        coordinates = lattice_coordinates(r, first, second)
        require(all(0 <= x < 1 for x in coordinates), label + ": 不在指定半开平行四边形")
    for k, r in enumerate(representatives):
        for s in representatives[k+1:]:
            coordinates = lattice_coordinates((r[0]-s[0], r[1]-s[1]), first, second)
            require(not all(x.denominator == 1 for x in coordinates), label + ": 同一格陪集重复")
    return representatives, lattice_index


def check_gate(certificate):
    required_fields = {"schema", "variables", "vectors", "A_coefficients", "kappa",
                       "units", "components", "expected_dimension"}
    require(type(certificate) is dict and required_fields <= set(certificate),
            "根对象缺少必备字段")
    require(set(certificate) <= required_fields | {"construction_lattice_relations", "limitations"},
            "根对象含未知字段")
    require(certificate["schema"] == SCHEMA, "schema不符")
    require(certificate["variables"] == VARIABLES, "必须保留四个具名独立变量")
    for name, expected in [("vectors", VECTORS), ("A_coefficients", A_COEFFICIENTS), ("kappa", KAPPA)]:
        require(certificate[name] == expected, name + ": 固定闸门输入不符")
        def check_int_tree(value):
            if type(value) is list:
                for item in value:
                    check_int_tree(item)
            else:
                integer(value, name)
        check_int_tree(certificate[name])
    require(integer(certificate["expected_dimension"], "expected_dimension") == 14,
            "固定预期维数必须为14")
    generators = reconstruct_generators()
    expected_units = required_units()
    units = certificate["units"]
    require(type(units) is list and len(units) == 21, "必须恰有21条基本单位证书")
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
    require(type(components) is list and len(components) == 6, "必须恰有六个有序分量")
    pairs = set()
    component_results = []
    total_dimension = 0
    for component in components:
        keys_exact(component, ["i", "j", "representatives", "basis_exponents", "inverse_E"], "component")
        i = integer(component["i"], "component.i")
        j = integer(component["j"], "component.j")
        require(0 <= i < 3 and 0 <= j < 3 and i != j, "非法分量索引")
        require((i, j) not in pairs, "重复分量")
        pairs.add((i, j))
        representatives, lattice_index = check_representatives(component["representatives"], i, j)
        expected_exponents = {
            (r[0]+alpha*VECTORS[i][0]-beta*VECTORS[j][0],
             r[1]+alpha*VECTORS[i][1]-beta*VECTORS[j][1])
            for r in representatives for alpha in range(DEGREES[i]) for beta in range(DEGREES[j])
        }
        dimension = lattice_index * DEGREES[i] * DEGREES[j]
        require(len(expected_exponents) == dimension, "构造的局部基指数碰撞")
        require(type(component["basis_exponents"]) is list, "basis_exponents必须是列表")
        supplied = [integer_vector(e, 2, "basis_exponents") for e in component["basis_exponents"]]
        require(len(supplied) == dimension and set(supplied) == expected_exponents,
                f"component_{i}_{j}: 局部基指数集合不完整或含额外项")
        E = product([generators[f"a{k}"] for k in range(3) if k != i]
                    + [generators[f"c{ell}"] for ell in range(3) if ell != j])
        inverse = component["inverse_E"]
        keys_exact(inverse, ["multipliers", "denominator"], "inverse_E")
        identity_results.append(check_identity(inverse, [E, generators[f"a{i}"], generators[f"c{j}"]],
                                               f"E_inverse_{i}_{j}"))
        support = set()
        per_basis_support = []
        for e in sorted(expected_exponents):
            vector = multiply(E, monomial((0, 0, e[0], e[1])))
            y_support = {term[2:] for term in vector}
            # Z-Z=[-1,1](1,0)+[-1,1](0,1)+[-2,2](1,2)，恰为下列交集。
            require(all(abs(x) <= 3 and abs(y) <= 5 and abs(2*x-y) <= 3
                        for x, y in y_support), f"E_{i}{j}Y^{e}: 支撑超出Z-Z")
            support.update(y_support)
            per_basis_support.append({"exponent": list(e), "Y_support_size": len(y_support)})
        component_results.append({"pair": [i, j], "lattice_index": lattice_index, "dimension": dimension,
                                  "representatives": [list(r) for r in representatives],
                                  "basis_exponents": [list(e) for e in sorted(expected_exponents)],
                                  "E_terms": len(E), "Y_support_union_size": len(support),
                                  "basis_support_checks": per_basis_support})
        total_dimension += dimension
    require(pairs == {(i, j) for i in range(3) for j in range(3) if i != j}, "六分量不完整")
    require(total_dimension == 14, "分量维数之和不为14")
    return {"status": "PASS", "schema": SCHEMA, "exact_coefficient_domain": "Q", "variables": VARIABLES,
            "unit_identity_count": 21, "E_inverse_identity_count": 6, "component_count": 6,
            "spanning_vector_count": 14, "dimension_from_structure": total_dimension,
            "dimension_dependency": "依赖格陪集自由模、两个单变量商的张量基以及两次CRT的一般证明；不是穷举验证任意输入。",
            "scope": "Lemma 5.2固定闸门实现；不声明已构造对应星形配置，不代表整个定理A获证。",
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


def self_test(valid_certificate):
    """在内存中破坏已通过的证书，要求每种破坏都被拒绝。"""
    results = []
    def rejected_mutation(name, mutate):
        altered = copy.deepcopy(valid_certificate)
        mutate(altered)
        try:
            check_gate(altered)
        except Rejected as error:
            results.append({"test": name, "status": "REJECTED_AS_REQUIRED", "reason": str(error)})
        else:
            raise Rejected("负控未被拒绝: " + name)
    def alter_coefficient(certificate):
        polynomial = parse_poly(certificate["units"][0]["multipliers"][0], "负控")
        certificate["units"][0]["multipliers"][0] = serialize_poly(add(polynomial, ONE))
    def specialize_all(certificate):
        records = certificate["units"] + [c["inverse_E"] for c in certificate["components"]]
        for record in records:
            record["denominator"] = specialize_polynomial(record["denominator"])
            record["multipliers"] = [specialize_polynomial(p) for p in record["multipliers"]]
    def denominator_with_y(certificate):
        certificate["units"][0]["denominator"] = [["1", 0, 0, 1, 0]]
    rejected_mutation("改动一个乘子系数", alter_coefficient)
    rejected_mutation("漏掉一条单位证书", lambda c: c["units"].pop())
    rejected_mutation("漏掉一个局部基元素", lambda c: c["components"][0]["basis_exponents"].pop())
    rejected_mutation("将全部证书X真正代入2和3但保留声明", specialize_all)
    rejected_mutation("分母含Y变量", denominator_with_y)
    rejected_mutation("零分母", lambda c: c["units"][0].__setitem__("denominator", []))
    rejected_mutation("重复分量替代缺失分量",
                      lambda c: c["components"].__setitem__(1, copy.deepcopy(c["components"][0])))
    rejected_mutation("错误有理系数类型float",
                      lambda c: c["units"][0]["denominator"][0].__setitem__(0, 1.0))
    return results


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON含重复字段: " + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent / "certificates/symbolic-gate.json")
    parser.add_argument("--self-test", action="store_true", help="通过后执行八项内存负控")
    args = parser.parse_args()
    try:
        raw = args.certificate.read_bytes()
        certificate = json.loads(raw, object_pairs_hook=unique_keys)
        result = check_gate(certificate)
        result["certificate_sha256"] = hashlib.sha256(raw).hexdigest()
        result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        if args.self_test:
            result["negative_controls"] = self_test(certificate)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (Rejected, OSError, json.JSONDecodeError, UnicodeDecodeError) as error:
        print(json.dumps({"status": "FAIL", "reason": str(error)}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
