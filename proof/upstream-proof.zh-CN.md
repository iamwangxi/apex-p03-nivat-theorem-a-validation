[English](upstream-proof.md) | **简体中文**

# 完整上游证明与定理 A 接入 v1.0

日期：2026-09-30。范围：原论文 §§0–4，加上与复用代数模块 §§5–7 的逐项接入。本文只讨论星形配置的定理 A，不包含一般配置的归约。Claude 对全链的跨模型核对为 **pending**。

引用使用[官方 PDF](https://math.apexin.net/papers/convex-nivat.pdf)，发布日期 2026-09-12，SHA-256 为 `7fd67831155f4226c010fd6af32de558b76643771e6be12dea4eebafa21745a8`。下游证明为[代数模块构造证明](expanded-proof.md)。两份证明共同建立所述定理；有限证书是独立的辅助证据。

## 1. 假设、周期和两种情形

固定素数 p。星形配置是 $\theta=\sum_{i=1}^mF_i:\mathbb Z^2\to\mathbb F_p$，其中 $m\ge2$；原始整向量 $v_i$ 两两不平行；$F_i$ 有周期 $k_iv_i$，其中 $k_i\ge1$，且不是双周期；存在双周期场 $L_i,R_i$ 和整数 $\ell_i\le r_i+1$，使 $F_i=L_i$ 于 $\pi_i<\ell_i$、$F_i=R_i$ 于 $\pi_i>r_i$，其中 $\pi_i(z)=\det(v_i,z)$。允许过渡带为空、左右尾不同、切向周期非原始。分量求和在 $\mathbb F_p$ 中；指标、编码、算子和维数全在特征零中。

令

$$
\Gamma=\bigcap_j(\operatorname{Per}(L_j)\cap\operatorname{Per}(R_j)).
$$

有限个有限指数子格的交仍有限指数，所以存在正整数 N 使 $N\mathbb Z^2\subseteq\Gamma$。取 $\kappa_i$ 为 $k_i$ 的正倍数且 $\kappa_iv_i\in\Gamma$，令 $H_i=\kappa_iv_i$。于是每个 $H_i$ 同时保持 $F_i$ 以及**全部** $L_j,R_j$。只保持尾场不够。最小正倍数不是证明必要条件；原文 §0.3 的选择满足这些条件。

记 $T^uf(z)=f(z+u)$、$D=\prod_i(T^{H_i}-1)$、$I_a=\mathbf1[\theta=a]$。Laurent 环是整环，每个因子非零，故 $D\ne0$。对 $C\subseteq[m]$，记 $H_C=\sum_{i\in C}H_i$。展开时按**子集 C**计项；即使 $H_C=H_{C'}$，仍保留原来的符号和重数。

Case A：存在 a 使 $DI_a\ne0$。Case B：所有 a 都满足 $DI_a=0$，从而任意单点颜色函数 g 都有 $Dg(\theta)=0$。下面分别闭合两案。

## 2. 局部函数、有限支撑与 Case A

### 2.1 Lemma 1.1 的全局支撑界

令 $h(z)=\varphi(\theta|_{z+W})$，W 有限。W 为空时 h 为常数，$Dh=0$。否则令 $E=\{H_C:C\subseteq[m]\}$、$M=E+W$、$a_i=\max_{s\in M}|\pi_i(s)|$，定义加宽条带

$$
\Sigma_i=\{z:\ell_i-a_i\le\pi_i(z)\le r_i+a_i\}.
$$

若 $z\notin\Sigma_i$，则 $F_i$ 在 $z+M$ 上全部等于同一侧尾场。若至多一个方向活跃，取该方向为 j；没有活跃方向时任取 j。$z+M$ 上的配置可写成 $G+B$，其中 G 是 $F_j$ 或零，B 是其余指定尾场之和，二者均被 $H_j$ 保持。在 D 的形式展开中把 C 与 $C\cup\{j\}$ 配对：两个窗口都在 $z+M$ 中，颜色模式逐点相同，两项相消。

因此

$$
\operatorname{supp}(Dh)\subseteq\bigcup_{i<j}(\Sigma_i\cap\Sigma_j).
$$

两个不平行方向的有界宽度条带之交有界：线性映射 $z\mapsto(\pi_i(z),\pi_j(z))$ 可逆。有限个此类交仅含有限格点。这个证明约束**所有锚点**，不依赖数值方框，也不要求形式子集和互不相同。

### 2.2 Lemma 1.2 的注入性

若 J 是非零有限支撑场，则 $\widehat J(X)=\sum_zJ(z)X^{-z}$ 是非零 Laurent 多项式。对非零 $f(T)=\sum_uc_uT^u$，换元给出

$$
\widehat{f(T)J}(X)=\left(\sum_uc_uX^u\right)\widehat J(X)\ne0.
$$

故非零 Laurent 算子不能消灭非零有限支撑场。指数是 $X^u$，不是 $X^{-u}$。

### 2.3 Proposition 1.3 单独闭合 Case A

对非空有限 S，令 $\mathcal L_S=\{\gamma_u:u\in\mathbb Z^2\}$，其中 $\gamma_u(s)=\theta(u+s)$，重复模式只留一份。若 $P_\theta(S)=|\mathcal L_S|\le|S|$，则其上的 $|S|+1$ 个有理函数 $1,\mathbf1[\gamma(s)=a]$ 线性相关。因此存在

$$
\sum_{s\in S}c_s I_a(u+s)=c_0\quad\text{for all }u\in\mathbb Z^2.
$$

令 $q(T)=\sum_sc_sT^s$。若 $q=0$，各 $c_s=0$，模式集非空又使 $c_0=0$，与非平凡关系矛盾。故 $q\ne0$。施加 D 得 $q(DI_a)=0$；但 $DI_a$ 非零且有限支撑，违背 §2.2。结论是 $P_\theta(S)\ge|S|+1$，对任意非空有限窗口成立，特别包括点、线段。Case A 到此结束，不借用后面的编码或二次见证。

若把各 $H_i$ 换成正倍数，D 被一个非零 Laurent 多项式乘上；Case A 的非零有限支撑和 Case B 的零性分别由 §2.2 及乘法保持。因此合法周期的放大不改变两案分类。

## 3. Case B：隔离极限、同一个保谱编码和整除

以下固定 Case B。

### 3.1 隔离配置与纯尾确实在轨道闭包内

固定 i。沿 $nH_i$，$F_i$ 不变，其他分量的法向坐标以非零速度 $\pi_j(H_i)$ 趋向一端。因为 $H_i$ 保持所有尾场，在每个固定有限集上不只是收敛，而是最终逐点稳定为

$$
\Xi_i^\sigma=F_i+B_i^\sigma,\qquad
B_i^\sigma=\sum_{j\ne i}\varepsilon_j^\sigma,
$$

其中 $\varepsilon_j^\sigma$ 取 $R_j$ 当 $\sigma\pi_j(v_i)>0$，否则为 $L_j$。所以 $\Xi_i^\sigma\in X_\theta$。

取格基 $(v_i,u_i)$，$\det(v_i,u_i)=1$。将 $\Xi_i^\sigma$ 沿 $\pm Nu_i\in\Gamma$ 推动，分别得到 $G_i^{\sigma,R}=R_i+B_i^\sigma$ 和 $G_i^{\sigma,L}=L_i+B_i^\sigma$。轨道闭包闭且平移不变，二者也在 $X_\theta$ 中。$\Xi_i^\sigma$ 被 $H_i$ 保持；所有纯尾 G 被每个 $H_j$ 保持。

### 3.2 谱的定义、非空性与统一编码

定义 $d_{i,\sigma,\epsilon,a}=\mathbf1[\Xi_i^\sigma=a]-\mathbf1[G_i^{\sigma,\epsilon}=a]$。它有周期 $H_i$，并在相应的整个左或右半平面为零。写 $z=sv_i+tu_i$。对 $\lambda^{\kappa_i}=1$，定义

$$
P_\lambda=\kappa_i^{-1}\sum_{k=0}^{\kappa_i-1}\lambda^{-k}T^{kv_i},\qquad
(P_\lambda d)(sv_i+tu_i)=\lambda^s\widehat d_t(\lambda).
$$

有限循环群 Fourier 分解给出 $\sum_\lambda P_\lambda d=d$、$T^{v_i}P_\lambda d=\lambda P_\lambda d$。所有投影与 Laurent 算子交换。令 $\Lambda_i$ 收集在某个差分场中非零出现的频率。若 $\Lambda_i$ 为空，则所有颜色差分为零，特别 $\Xi_i^+=G_i^{+,R}$，迫使 $F_i=R_i$ 双周期，矛盾。因此 $d_i=|\Lambda_i|\ge1$。

令 $A_i(t)=\prod_{\lambda\in\Lambda_i}(t-\lambda)$，$A(T)=\prod_iA_i(T^{v_i})$。每个 $A_i$ 整除 $t^{\kappa_i}-1$，首一、无重根、常数项非零，并消灭所有该方向的颜色差分场。Newton 乘积等号给出

$$
\operatorname{Newt}(A)=Z=\sum_i[0,d_iv_i].
$$

至少两个方向不平行，故 Z 有内点。

为每对 $(i,\lambda)$ **预先固定**一组 $\sigma,\epsilon,t$，使向量 $(\widehat d_{i,\sigma,\epsilon,a,t}(\lambda))_a$ 非零。条件

$$
\sum_aw(a)\widehat d_{i,\sigma,\epsilon,a,t}(\lambda)\ne0
$$

排除 $\mathbb Q^p$ 的一个真有理线性子空间：非零复线性形式在某个有理坐标向量上非零。另排除 $w(a)=w(a')$ 的有限个超平面。无限域上有限个真线性子空间不能覆盖整个有限维空间，所以可**一次选择**满足全部条件的有理 w，清分母后得到整数单射。这样，同一个 w 保留全部 $\Lambda_i$，不是每个频率另选编码，也不把单射性误认为保谱性。

固定此 w，$\eta=w(\theta)$。Case B 保证 $D\eta=0$，也保证 $D(\eta^2)=0$。不需要把 Galois 稳定性当作后续维数论证的前提。

### 3.3 单侧消失强迫一个素因子：Lemma 2.3

设差分场 d 有周期 $H_i$，在一侧半平面为零，且 $P_\lambda d\ne0$。若 $f(T)d=0$，则 $f(T)P_\lambda d=0$。在格基变量 $X=T^{v_i},Y=T^{u_i}$ 下，这是 $g(Y)c=0$，其中 $g(Y)=f(\lambda,Y)$、$c(t)=\widehat d_t(\lambda)\ne0$。

若 c 在右端为零，非空支撑在整数中有最大元 $t_0$；若 $g\ne0$，取其最小指数 $\beta_-$，在 $t_0-\beta_-$ 处只有 $g_{\beta_-}c(t_0)$ 存活，矛盾。左端为零时改取 c 的最小支撑点与 g 的最大指数。故 $g=0$。逐个 Y 系数看，一元 Laurent 多项式在非零 $\lambda$ 处为零意味着被 $X-\lambda$ 整除。因此 $(T^{v_i}-\lambda)\mid f$。这里允许法向支撑朝另一端无限延伸。

### 3.4 关系传到闭包，再相减与组装：Lemma 2.4

若 $f(T)\eta=c$ 是全平面常数关系，它对所有平移成立；每个锚点只涉及有限多个颜色，所以关系在产品拓扑下是闭条件，传到每个 $\chi\in X_\theta$。分别代入 $\Xi_i^\sigma$ 和 $G_i^{\sigma,\epsilon}$ 再相减，得到

$$
f(T)\bigl(w(\Xi_i^\sigma)-w(G_i^{\sigma,\epsilon})\bigr)=0.
$$

对每个 $\lambda\in\Lambda_i$，统一编码保证至少一组差分保留该频率，§3.3 给出 $T^{v_i}-\lambda\mid f$。

由于 $v_i$ 原始，可补成格基，商环 $\mathbb C[X^{\pm1},Y^{\pm1}]/(X-\lambda)\simeq\mathbb C[Y^{\pm1}]$ 是整环，因此每个因子为素元。不同方向若相伴，二点支撑必须平移相同，迫使 $v_i=\pm v_j$；同方向不同根也不相伴。唯一分解遂给出 **$A\mid f$**。未借用待证复杂度结论。

## 4. 仿射维数预算与退化窗口（Lemma 2.5）

固定非空有限 S；模式集 $\mathcal L_S$ 定义同 §2.3。令

$$
U_S=\operatorname{span}_{\mathbb Q}\{1,\gamma\mapsto w(\gamma(s)):s\in S\},\qquad
R_Z(S)=\{r\in\mathbb Z^2:r+Z\subseteq\operatorname{Conv}(S)\}.
$$

由于 $0\in Z$，$R_Z(S)\subseteq\operatorname{Conv}(S)\cap\mathbb Z^2$，是有限集。

有理关系空间由行向量 $(-1,(\eta(u+s))_{s\in S})$ 对所有整数锚点 u 的齐次方程定义。虽然锚点无限，行向量所在空间只有 $|S|+1$ 维；从实际行向量中选一个有理行空间基，最多 $|S|+1$ 行，其余实际行均是它们的有理线性组合。因此这些有限方程在 $\mathbb Q$ 和 $\mathbb C$ 上都等价于原系统。有限有理矩阵的秩由非零子式决定，扩域不改变秩，遂有

$$
\mathcal R_{\mathbb C}=\mathcal R\otimes_{\mathbb Q}\mathbb C,
\qquad \dim_{\mathbb C}\mathcal R_{\mathbb C}=\dim_{\mathbb Q}\mathcal R.
$$

对非零复关系 $(c_0,(c_s))$，多项式 $f=\sum_sc_sT^s$ 非零，且 $f\eta=c_0$。由 §3.4 写成 $f=Ag$。Newton 乘积等号给出 $Z+\operatorname{Newt}(g)=\operatorname{Newt}(f)\subseteq\operatorname{Conv}(S)$，故 $\operatorname{supp}(g)\subseteq R_Z(S)$。映射 $(c_0,f)\mapsto g$ 线性且单射：乘法无零因子，且 f 唯一决定 $c_0$。所以

$$
\dim\mathcal R\le|R_Z(S)|,\qquad
\dim U_S\ge |S|+1-|R_Z(S)|.
$$

这一预算本身只使用 $\operatorname{supp}(f)\subseteq S$，不使用 S 格凸；本文仅用它证明原定理，不主张更强下界。

若 $R_Z(S)=\varnothing$，则 $P_\theta(S)\ge\dim U_S\ge|S|+1$，不需要二次见证。点、线段的凸包至多一维，而 Z 有内点，因此它们均落入此分支。二维窗口也可能有空 $R_Z(S)$，同样处理。

## 5. 仅比较实际扇区，取得全局周期背景

### 5.1 Lemma 3.1

m 条互异过原点的直线把平面切成 $2m$ 个开扇区。每个扇区 K 的符号向量 $\epsilon(K)=(\operatorname{sign}\pi_i)_i$ 给出纯尾和 $\Theta_{\epsilon(K)}$。沿公共边界射线 $\sigma v_i$，相邻两扇区只改变第 i 个尾选择；其他分量的尾由 $\operatorname{sign}(\sigma\pi_j(v_i))$ 确定，恰好组成 $B_i^\sigma$。因此相邻两尾和就是 $G_i^{\sigma,L},G_i^{\sigma,R}$。

逐颜色有

$$
\mathbf1[G_i^{\sigma,R}=a]-\mathbf1[G_i^{\sigma,L}=a]
=d_{i,\sigma,L,a}-d_{i,\sigma,R,a},
$$

被 $A_i(T^{v_i})$、进而被 A 消灭。实际扇区按角序构成连通循环，所以 $Ae_{\Theta_{\epsilon(K)}}$ 对所有实际 K 相同，记为 b。它是双周期向量场，并被全部 $H_j$ 保持。这个结论完全不需要任意 $2^m$ 种尾组合都相等。

### 5.2 Lemma 3.2 的有限异常区域

令 $M_A=\operatorname{supp}(A)$。取整数 $c_i\ge1+\max(|\ell_i|,|r_i|)$，并置 $\rho_i=c_i+\max_{s\in M_A}|\pi_i(s)|>0$，$\Sigma_i^A=\{z:|\pi_i(z)|\le\rho_i\}$。这比原文许可下界稍宽，避免零宽条带的无关表述问题。

没有活跃方向时，$z+M_A$ 上每个分量都处于由 $\operatorname{sign}\pi_i(z)$ 决定的尾；z 自己属于一个实际扇区，故 $(Ae_\theta)(z)=b(z)$。

至少两个方向活跃的所有锚点包含于有限集 $\bigcup_{i<j}(\Sigma_i^A\cap\Sigma_j^A)\cap\mathbb Z^2$。

恰有 i 活跃时，写 $z=tv_i+qu_i$，$|q|\le\rho_i$。定义明确阈值

$$
B_i=\frac{\rho_i\max_{j\ne i}|\pi_j(u_i)|+\max_{j\ne i}\rho_j}
{\min_{j\ne i}|\pi_j(v_i)|}.
$$

分母严格正。若 $|t|>B_i$，则对所有 $j\ne i,s\in M_A$，

$$
|t|\,|\pi_j(v_i)|>|q|\,|\pi_j(u_i)|+\rho_j,
$$

进而 $|\pi_j(z+s)|>c_j$，符号为 $\operatorname{sign}(t\pi_j(v_i))$。故在整个 $z+M_A$ 上 $\theta=\Xi_i^{\operatorname{sign}(t)}$。由于 A 消灭它与任一相应纯尾的颜色差分，且该纯尾对应实际相邻扇区，得到 $(Ae_\theta)(z)=b(z)$。

因此下面是一个完整的有限异常包络：

$$
F=\bigcup_{i<j}(\Sigma_i^A\cap\Sigma_j^A)\cap\mathbb Z^2
\ \cup\ \bigcup_i\{tv_i+qu_i:t,q\in\mathbb Z,\ |q|\le\rho_i,\ |t|\le B_i\}.
$$

结论是 $\operatorname{supp}(Ae_\theta-b)\subseteq F$。无限长的单条带已经通过 t 阈值排除，只剩有限个锚点。

### 5.3 Proposition 3.3

Case B 给 $De_\theta=0$，而 $Db=0$。算子交换，所以 $D(Ae_\theta-b)=0$。§5.2 的余项有限支撑，§2.2 和 $D\ne0$ 迫使每个颜色坐标的余项均为零。因此

$$
Ae_\theta=b\quad\text{on all of }\mathbb Z^2,\qquad
A\eta=b_\eta=\sum_aw(a)b_a.
$$

$b_\eta$ 双周期且被**每个** $H_i$ 保持。背景允许非零；不能把本结论替换成未经证明的 $A\eta=0$。

## 6. 非零条带场与真实的非零二次见证

### 6.1 Lemma 4.1

令 $Q_i=\prod_{j\ne i}(T^{H_j}-1)$，$f_i=Q_i\eta$。Case B 使 $(T^{H_i}-1)f_i=0$。利用这一全局周期，再把 $T^{nH_i}\theta$ 推向 $\Xi_i^+$，有限算子逐点通过最终稳定极限，得到

$$
f_i=Q_iw(\Xi_i^+)=Q_i\delta_i=Q_i\delta_i',
$$

其中 $\delta_i=w(\Xi_i^+)-w(G_i^{+,R})$、$\delta_i'=w(\Xi_i^+)-w(G_i^{+,L})$。各平移 $T^{H_j}$ 出现在 $Q_i$ 中并保持纯尾，因此 $Q_i$ 消灭它们。这些等式全局成立。令 $a_i'=\max_{C\subseteq[m]\setminus\{i\}}|\pi_i(H_C)|$。两个单侧消失式给出

$$
\operatorname{supp}(f_i)\subseteq\{\ell_i-a_i'\le\pi_i\le r_i+a_i'\}.
$$

单射 w 和 $F_i$ 非双周期保证 $\delta_i\ne0$。其法向支撑上有最大值 $\pi^*$，取 $z^*$ 在此行且 $\delta_i(z^*)\ne0$。令

$$
C_{\min}=\{j\ne i:\pi_i(H_j)<0\}.
$$

每个 $\pi_i(H_j)\ne0$。对任何不同子集 C，$\pi_i(H_C)-\pi_i(H_{C_{\min}})>0$：差值是新增正项与删去负项的绝对值之和。故形式展开中这个最小投影项唯一。在 $z^*-H_{C_{\min}}$ 处，只有该项不超过最大非零行，得到 $f_i=\pm\delta_i(z^*)\ne0$。其他非极端子集和可发生碰撞；唯一极端项不可能与别项同点，因此不会被抵消。

### 6.2 Lemma 4.2

对每个固定 d，$J(d,z)=D_z[\eta(z)\eta(z+d)]$ 是有限窗口局部函数的差分，§2.1 保证有限支撑；不同 d 不需要共同支撑上界。

选 $i\ne j$ 和 $x_i,x_j$，使 $f_i(x_i)f_j(x_j)\ne0$。令 $d_0=x_j-x_i$，$C(z)=f_i(z)f_j(z+d_0)$。则 $C(x_i)\ne0$，且 C 支撑位于两个不平行条带之交，因而有限。§2.2 给出 $DC\ne0$。

将两个 Q 都按形式子集展开，有有限恒等式

$$
DC=\sum_{C_1,C_2}\pm T^{H_{C_1}}
J(d_0+H_{C_2}-H_{C_1},\cdot).
$$

若所有 J 都为零，右侧为零，矛盾。故存在真正的非零 J。由于 $J(0,\cdot)=D(\eta^2)=0$，这个见证位移非零。这里只得到某个 d；把 d 限制在 $Z-Z$ 内要接下游模块，不能提前假定。

## 7. 接入已有代数模块，闭合定理 A

下游 [代数模块构造证明](expanded-proof.md) 的配置前提在现在逐项解除：

| 模块输入 | 本文证明 | 边界 |
|---|---|---|
| 非平行整方向、$m\ge2$、$A_i\mid t^{\kappa_i}-1$、$d_i\ge1$ | §§1、3.2 | 本文仍使用原论文的原始方向 |
| 整数编码及全部单点函数被 D 消去 | §§1、3.2 | 仅 Case B；Case A 已单独结束 |
| 全局 $A\eta=b_\eta$，每个 $H_i$ 保持背景 | §5 | 不要求背景为零 |
| 每个 J 有限支撑，某个 J 非零 | §6 | 不把任意 d 当作非零见证 |
| 维数预算 $\dim U_S\ge\lvert S\rvert+1-\lvert R_Z(S)\rvert$ | §4 | 包括空平移集分支 |

为使接口可审阅，保留下游的关键逻辑，而不是只写“套用模块”。

**双递推与变换。** 由 $A\eta=b_\eta$ 及背景对每个形式平移 $H_C$ 不变，展开 D 后可把背景提出，得到

$$
\sum_sA_sJ(d+s,z)=0,\qquad
\sum_sA_sJ(d-s,z+s)=0.
$$

这里没有使用错误的差分 Leibniz 法则。令 $K=\mathbb C(X_1,X_2)$、$R=K[Y_1^{\pm1},Y_2^{\pm1}]$、$a=A(Y)$、$c=A(X/Y)$。对逐 d 有限的 $\widehat J(d;X)=\sum_zJ(d,z)X^{-z}$，定义 K 线性泛函 $L(Y^d)=\widehat J(d;X)$。第二递推的换元产生正号 $X^s$。递推对全部 d 成立，K 线性使 L 消灭 $(a,c)$ 的全部多项式倍数。

**商的张成。** 模块 §§2–5 给出三类单位理想、两次 CRT、以及

$$
R/(a,c)\simeq\prod_{i\ne j}R/(A_i(Y^{v_i}),A_j(X^{v_j}Y^{-v_j})).
$$

在有序方向对 $(i,j)$ 上取格余类半开平行四边形代表 r，指数 $r+\alpha v_i-\beta v_j$，$0\le\alpha<d_i,0\le\beta<d_j$，组成分量基，落在 $[0,d_iv_i]+[0,-d_jv_j]$。乘上 $E_{ij}=\prod_{k\ne i}a_k\prod_{l\ne j}c_l$ 后，在其他分量为零，在本分量可逆；这些向量的实际 Laurent 支撑都在 $Z-Z$。逆元只计算系数，不要求它的支撑在 $Z-Z$。因此 $d\in(Z-Z)\cap\mathbb Z^2$ 的单项式张成 $R/(a,c)$。

若这些 d 的 J 都为零，则 L 在商上为零，进而全部 J 为零，与 §6 矛盾。因此取得 $d\in(Z-Z)\cap\mathbb Z^2$、$d\ne0$、$J(d,\cdot)\ne0$。

**格点和同一见证。** Z 关于 $c_0/2$ 中心对称，$c_0=\sum_id_iv_i$，故 $Z-Z=2Z-c_0$。二维格多边形的单模三角剖分说明任意 $x\in2Z\cap\mathbb Z^2$ 可写成 Z 内两个格点之和：在包含 $x/2$ 的单模三角形中，两倍非基点重心坐标为非负整数且和至多二，六种可能逐一给出两个顶点之和。取 $x=d+c_0$ 得 $q,q+d\in Z\cap\mathbb Z^2$。详见模块 §7 的局部细分、终止和边界论证。

先固定这个非零见证 d，再固定 q，最后量化所有窗口 S。对格凸 S 和 $r\in R_Z(S)$，$r+q,r+q+d$ 都在 S，于是

$$
\Phi_r(\gamma)=w(\gamma(r+q))w(\gamma(r+q+d))
$$

是窗口模式函数。若非平凡组合 $\sum_rc_r\Phi_r$ 属于 $U_S$，代入全部平移模式并施加 D，得到

$$
\left(\sum_rc_rT^{r+q}\right)J(d,\cdot)=0.
$$

各指数不同，括号非零，J 非零且有限支撑，违反 §2.2。故这些二次观测模 $U_S$ 独立，

$$
P_\theta(S)\ge\dim U_S+|R_Z(S)|\ge|S|+1.
$$

这闭合 Case B 的非空平移集分支；结合 §2.3 的 Case A、§4 的空平移集及点/线段分支，得到定理 A 所有假设下的结论。量词顺序为 $\exists d\,\exists q\,\forall S$，而不是对任意几何合法 d 均宣称非零。

## 8. 验证边界

本证明使用 Laurent 唯一分解、Newton 乘积等号、有限维线性代数及已重建的代数模块；它是纸面数学验证，没有形式化认证。一般证明不以随机或有限方框实验代替。

两个既有全局实例和十二个代数输入为复用证据，不宣称新增覆盖。见[复现说明](../REPRODUCE.md)。单独的[附录 C 审计](appendix-c-audit.md)不参与本证明依赖。Claude 全链核对仍为 **pending**。
