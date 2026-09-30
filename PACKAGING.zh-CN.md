[English](PACKAGING.md) | **简体中文**

# 打包、来源与审阅边界

配套归档 [GitHub v1.1](https://github.com/iamwangxi/apex-p03-nivat-theorem-a-validation/tree/v1.1) 的正文版本为 `v1.2`，保存在 `proof/submission.md`。尚未向悬赏平台提交表单。Claude（Opus 5.5）依据论文独立重推了上游链的五个关键接口，未发现错误，但未逐行核对本稿。

v1.1 只修正配套文件中的核对状态句，数学内容与证书不变，v1.0 保留不动。

## 数学来源

`proof/upstream-proof.md` 是新增一般上游证明的英文打包改编，配有中文版。它解除模块此前接受的前提，并与 `proof/expanded-proof.md` 一起闭合定理 A。后者保留既有模块修订版 `v1.1` 及其历史审阅归属，新增范围说明。`proof/appendix-c-audit.md` 是独立的附录 C 声明审计。Case B 下的全部尾组合一般推广仍未判定。Section 8 和 Appendix D 排除在外。

引用使用[官方 PDF](https://math.apexin.net/papers/convex-nivat.pdf)，发布日期 2026-09-12，SHA-256 为 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`。以定理编号和印刷页码替代私有文本行号。不分发目标 PDF 或私有讨论。

## 复用的科学材料

此前本地归档 `apex-p03-nivat-module-validation` 提供 `certificates/symbolic-gate.json`、`certificates/boundary/`、两个全局实例证书目录及其全局覆盖说明、全部检查器和生成器代码、依赖版本与许可。复制采用明确文件白名单，未导入仓库元数据、环境、缓存或历史日志。证书和代码字节保持不变。模块证明和复现文档新增了范围说明，不被称为逐字节复制。

12 个固定代数输入和两个全局实例都是复用证据，不是新增配置或覆盖。独立检查器不是本轮新编写的。原有独立上下文来源仍成立，但打包不增加新的独立性主张。验收运行检查复制的证书和规定负控，不执行一般上游证明。生成器供可选复现使用，本次准备没有运行。

Claude Opus 5.5 此前审阅了模块并复跑历史验收入口；该审阅未覆盖新增上游证明。Claude（Opus 5.5）依据论文独立重推了上游链的五个关键接口，未发现错误，但未逐行核对本稿。Codex/GPT 准备与新 GPT 对抗审阅不等于跨模型通过。

## 双语文档与完整性

`README.md`、`REPRODUCE.md`、`PACKAGING.md`、`proof/upstream-proof.md`、`proof/expanded-proof.md`、`proof/appendix-c-audit.md`、`proof/submission.md` 和 `certificates/global-configurations.md` 各配 `.zh-CN.md` 对应版本。英文为准。双语比较排除导航行，按顺序比较公式、行内代码、代码块、链接目标和数字，同时进行语义复核。英文投稿稿没有导航行，须与外部源稿逐字节一致。

`MANIFEST.sha256` 覆盖除自身以外的全部发布文件。验收输出在发布清单之外保存。不包含环境、缓存、第三方 PDF 或对话。本地发布脚本仅复制 manifest 所列文件，校验哈希并扫描敏感信息。发布、匿名获取核验和表单提交是独立操作。

代码采用 MIT 许可；原创文字和证书在适用权利存在的范围内采用 CC BY 4.0。其他材料保留各自条款。任何发布前，须同步投稿稿、译本、表单文件与 manifest。实际标签 `v1.0` 发布后，实质修改须使用新版本。
