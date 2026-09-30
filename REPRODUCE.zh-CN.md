[English](REPRODUCE.md) | **简体中文**

# 复现定理 A 的复用证书

这里运行的是复用的代数与全局配置检查，不执行或认证 `proof/upstream-proof.md` 中新增的一般上游证明。Claude 对定理 A 全链的核对仍为 **pending**。本包不宣称新增配置样本。

在包根目录使用 Python 3.9 或更新版本运行。不要使用 `-O`：断言参与验证。验收仅需 Python 标准库，无需网络。

## 完整性与验收

```sh
shasum -a 256 -c MANIFEST.sha256
python3 -B code/verify_all.py
```

安装了 GNU coreutils 的系统可用 `sha256sum -c MANIFEST.sha256`。清单通过只说明字节完整性。验收命令须退出零并报告全部 15 项作业成功：符号闸门、12 个边界输入及两个全局实例。边界预期总数为 163 条基本单位恒等式、46 条局部逆元恒等式和 128 个基／张成向量。预期负控拒绝为边界输入 348 次、其余检查 20 次，共 368 次。

冻结输入清单为 `certificates/boundary/frozen-inputs.json`，SHA-256 `f988d2c2f79c155535cebe9afafb0bd513cea0d8d69f4456ddcfbc89e01dc2f6`。检查器从这些输入重建目标表达式，拒绝不完整的恒等式／分量集合以及错误的分母、代表、基数据或支撑。检查器不导入或调用生成器。

两个全局实例须分别恢复 347 和 401 个模式，每例秩均为 $46\to55$。见 `certificates/global-configurations.md`，其中论证有限枚举为何覆盖无限格上的全部平移；只有有限窗口采样并不充分。

## 可选重新生成

生成与验收分开。生成使用 `code/requirements.txt` 中的版本：`sympy==1.14.0` 和 `mpmath==1.3.0`。若本地已有这些包，重新生成可保持离线；否则依赖安装需要另行授权联网。核查随包证书无需运行生成器或安装依赖。

使用新的目的目录，并按生成器帮助操作；保留失败尝试，不替换冻结输入：

```sh
python3 -B code/regenerate_all.py --help
python3 -B code/regenerate_all.py --output reproduced
python3 -B code/verify_all.py --results reproduced
```

生成结果须经独立检查器通过才可接受。重新生成耗时和机器专属路径不属于证书有效性。最初边界生成耗时 121.202406 秒；这只是历史观察，不是运行时间上界。随包 12 个边界证书合计 1,583,170 字节。`B09.json` 与 `certificates/symbolic-gate.json` 逐字节一致。
