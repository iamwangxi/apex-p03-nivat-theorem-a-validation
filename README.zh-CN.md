[English](README.md) | **简体中文**

# 星形配置定理 A 验证

本配套归档验证凸 Nivat 论文 §§0–7 中定理 A 的全链，保留原文的星形配置假设。新增书面论证闭合上游接口，并接入复用的代数构造模块。结论是：对每个非空有限格凸窗口，包括点和线段，均有 $`P_\theta(S)\ge |S|+1`$。Section 8、Appendix D、一般配置的归约和更强的窗口下界不属于本次投稿。

目标论文：Apex Intelligence，*The Convex Nivat Conjecture: A Complexity Lower Bound for Star Configurations, and a Reduction from Low Convex Complexity to Star Configurations*。[官方 PDF](https://math.apexin.net/papers/convex-nivat.pdf)，发布日期 2026-09-12；891,962 字节；SHA-256 为 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`。本包不附带 PDF。

配套归档：[GitHub v1.1](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.1)；投稿正文版本 `v1.2`。Claude（Opus 5.5）依据论文独立重推了上游链的五个关键接口，未发现错误，但未逐行核对本稿。

v1.1 只修正配套文件中的核对状态句，数学内容与证书不变，v1.0 保留不动。

## 阅读与复现

- [投稿正文](proof/submission.md) / [中文译本](proof/submission.zh-CN.md)
- [完整上游证明与下游接入](proof/upstream-proof.md) / [中文译本](proof/upstream-proof.zh-CN.md)
- [复用的代数模块构造证明](proof/expanded-proof.md) / [中文译本](proof/expanded-proof.zh-CN.md)
- [附录 C 声明审计](proof/appendix-c-audit.md) / [中文译本](proof/appendix-c-audit.zh-CN.md)
- [复现说明](REPRODUCE.md) / [中文译本](REPRODUCE.zh-CN.md)
- [打包与来源](PACKAGING.md) / [中文译本](PACKAGING.zh-CN.md)
- [全局配置覆盖](certificates/global-configurations.md) / [中文译本](certificates/global-configurations.zh-CN.md)

在包根目录运行，无需第三方依赖：

```sh
shasum -a 256 -c MANIFEST.sha256
python3 -B code/verify_all.py
```

## 新增论证与复用证据

新增上游证明覆盖共同周期、有限支撑与 Case A、单个保谱编码、整除与仿射维数预算、仅依赖实际扇区的全局周期背景，以及真实非零二次见证的存在。随后将同一见证接入下游商环和格点论证，量词顺序为 $`\exists d\,\exists q\,\forall S`$。附录 C 审计确认所述例子混淆了单因子与完整乘积；这既不否定定理 A，也未判定全部尾组合的一般推广。

符号闸门、12 个固定代数输入和两个全局实例均为复用，没有重新生成证书，也没有增加样本覆盖。边界集合检查 163 个基本恒等式、46 个逆元和 128 个张成向量。完整验收包含 15 项任务，拒绝 368 个负控，其中边界集合贡献 348 个。两个实例分别有 347 和 401 个完整全局模式，见证支撑分别含 12 和 32 点，有理秩均为 $`46\to55`$。这些代数输入不被宣称为星形配置。

检查器使用标准库整数和有理数运算。生成器仅为可选重生成使用固定版本的 SymPy。有限证书不能代替书面一般证明。本包没有证明内核认证或人类专家背书。

OpenAI Codex 与 GPT 上下文起草并复核了上游数学、包和译本。原始数学检查器由未读生成器的独立 GPT 上下文编写。Claude Opus 5.5 此前核对过复用模块的五个承重点并复跑其验收入口；这一历史审阅不认证新的全链。Claude（Opus 5.5）依据论文独立重推了上游链的五个关键接口，未发现错误，但未逐行核对本稿。 最终投稿稿和双语文档的新 GPT 复核另有记录。

英文文档为准。代码采用 MIT 许可；原创文字和证书在适用权利存在的范围内采用 CC BY 4.0。见 [LICENSE](LICENSE)。

## 版本说明

本版本与 `ddd11065ea33bea0385746f7b6f1f4bf35f73206` 相比，只改了公式的写法。GitHub 的 Markdown 处理会去掉 `$...$` 里的 `\{`、`\,` 等反斜杠转义，还有部分公式没被识别，所以全部公式改用 GitHub 的原样数学语法。另把 GitHub 公式渲染器禁用的宏（如 `\operatorname`）换成了等价写法。数学文字没有任何改动。
