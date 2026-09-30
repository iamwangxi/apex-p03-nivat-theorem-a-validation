**English** | [简体中文](appendix-c-audit.zh-CN.md)

# Audit of Appendix C statements, v1.0

Date: 2026-09-30. This is a limited statement audit, without regenerated random configurations or repeated homogeneous experiments. Its conclusions are not dependencies of the general proof of Theorem A. Claude full-chain review is **pending**.

## 1. Remark 3.1′ and C.3: the example does not support the full-A counterexample

Source locations: Remark 3.1′, p.11; C.3, p.32 of the [official PDF](https://math.apexin.net/papers/convex-nivat.pdf).

The example takes $p=2$, $v_1=(1,0),v_2=(0,-1),v_3=(1,-1)$, all left tails zero, and right tails $R_1=\mathbf1[x\text{ is even}]$, $R_2=R_3=\mathbf1[3\mid x]$. Every tail depends only on x.

The second component has normal coordinate x and takes constant value 1 inside its width-one transition strip, so it too depends only on x. Its isolation background is a sum of other component tails and also depends only on x. All exceptional difference fields in this direction are therefore preserved by $T^{(0,-1)}$ and can contain only frequency 1. Non-double-periodicity and Lemma 2.1 ensure that at least one difference is nonzero. Hence

$$
\Lambda_2=\{1\},\qquad A_2(T^{v_2})=T^{(0,-1)}-1.
$$

All eight tail combinations $\Theta_\epsilon$ and all their color indicators depend only on x, so $A_2e_{\Theta_\epsilon}=0$. The full A is the product of all direction factors, and the operators commute. Thus

$$
Ae_{\Theta_\epsilon}=0\qquad\text{for all eight combinations.}
$$

The C.3 computation with the single factor $A_1=T^{(2,0)}-1$ is still correct. The mixed difference has values $(-1,0,1,0,1,0)$ for $x\bmod6$; applying $A_1$ gives $(2,0,0,0,-2,0)$, which is nonzero. This proves that one factor is insufficient, not that the full product A is insufficient.

Two conclusions must remain separate:

- **The stated example does not support the claimed counterexample for full A: confirmed.** It confuses A with the single factor $A_1$; floating-point precision is not the issue.
- **The general extension: undecided.** In particular, we neither prove nor refute the arbitrary-tail extension in the Case B setting adopted from §1 onward. A variant dropping Case B is not a counterexample to the stated setting. Failure of an example does not prove the extension.

The main proof needs only the actual $2m$ sectors, as reconstructed in [the upstream proof](upstream-proof.md), §5. This local explanatory error does not affect the Theorem A proof and is not treated as a substantive break.

The prior exact audit checked all 8 combinations, 6 horizontal phases and both colors. Vertical invariance follows from the definitions above, not from finite sampling in y. The full-A annihilation requires only its $A_2$ factor; reconstructing the remaining factors is unnecessary. No private execution log is required for this analytic argument.

## 2. Conditions and criterion in Observation C.1

Observation C.1 (pp.31–32) assumes $m=2$, $L_i=R_i$. Put $\delta_i=F_i-L_i$, supported in a bounded-width strip. Enlarge the legal periods $H_1,H_2$ so that each shifts across the other strip by more than its width. This does not change Case A/B; see upstream §2.3.

In the four-point stencil, $\delta_1$ is invariant under $H_1$, $\delta_2$ under $H_2$, and each is nonzero at at most one of the two positions across its strip. The background $L_1+L_2$ is the same at all corners. If both deviations occur in a stencil, some corner contains nonzero deviations $\alpha,\beta$ simultaneously; conversely any simultaneous-deviation point gives such a stencil.

Its color-vector difference, up to sign, is

$$
e_{b+\alpha+\beta}-e_{b+\alpha}-e_{b+\beta}+e_b.
$$

When $\alpha,\beta\ne0$, the coefficient at color b is $1+\mathbf1[\alpha+\beta=0]>0$. Coefficients are in characteristic zero, so even $p=2$ does not cancel coefficient 2. Thus Case B is equivalent to $\operatorname{supp}\delta_1\cap\operatorname{supp}\delta_2=\varnothing$. The criterion closes under its stated conditions.

## 3. What numerical experiments can establish

The claims in C.1–C.2 were read, but random seeds were not rerun, and the claimed auxiliary exact outputs for all 570 components were not independently checked.

| Claim type | Audit conclusion |
|---|---|
| Equal pattern counts in two boxes | Observed stability does not prove global exhaustion; the appendix acknowledges this |
| Ranks of sampled matrices modulo primes | Give lower bounds for global rational ranks; their difference alone does not establish the quotient increment |
| Some $DI_a$ nonzero in a finite box | Proves Case A |
| Every $DI_a$ zero in a finite box | Proves Case B only if the box covers the whole established support; the appendix claims further exact checks, which are not individually reproduced here |
| DFT spectra and a random injective encoding | A DFT threshold is numerical; injectivity alone does not preserve spectra. Claimed exact remainder checks are not treated as independently passed certificates |
| Tiny periodic residual | Does not prove global $A\eta=b_\eta$; the proof here uses finite exceptional support and Laurent injectivity |

The reused examples with 347/401 global patterns have independent anchor coverage, full J support and both lower and upper rational-rank certificates. Their evidence is stronger than a general finite-box experiment. Rechecking these old certificates adds no random-sample coverage and does not change the C.3 conclusion.
