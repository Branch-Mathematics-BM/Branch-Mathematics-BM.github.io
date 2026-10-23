# Steadman Hypothesis V1.2 — Conditional Poisson Response Verification Addendum

**Date:** 21 September 2026  
**Baseline:** Steadman Hypothesis V1.1  
**Status:** Canonical mathematical addendum  
**Governance:** SH V1 physical hypotheses, BM V1 foundation, and the frozen block-Poincaré module remain unchanged.

---

## 1. Executive status

The conditional Poisson response refinement is accepted as a mathematically valid strengthening of the V1.1 boundary-score route under the stated finite-product, smooth-density, disjoint-block, and boundary-uniform conditional Poincaré assumptions.

It does not establish:
- a new fundamental force,
- a conserved scalar RD,
- a Yang–Mills continuum mass gap,
- or a replacement for the frozen block engine.

It does establish a strictly sharper sufficient response coefficient that can succeed when the V1.1 score comparison fails.

---

# 2. SH-T15 — Conditional Poisson response coefficient

For fixed exterior configuration \(\eta\), let
\[
A_B^\eta=-L_B^\eta
\]
on the centered subspace of \(L^2(\nu_B^\eta)\).

For a unit boundary tangent \(v\in T_{\eta_C}X_C\), \(C\neq B\), define
\[
s_{BC}^{\eta,v}
=
\partial_vW-E_B[\partial_vW].
\]

Let the unique centered weak solution satisfy
\[
A_B^\eta u_{BC}^{\eta,v}
=
s_{BC}^{\eta,v}.
\]

Define
\[
q_{BC}(\eta,v)^2
=
E_B|\nabla_Bu_{BC}^{\eta,v}|^2
=
\left\langle
s_{BC}^{\eta,v},
(A_B^\eta)^{-1}s_{BC}^{\eta,v}
\right\rangle_B,
\]
and
\[
\boxed{
\mathcal Q_{BC}
=
\sup_{\eta,\|v\|=1}
q_{BC}(\eta,v).
}
\]

\(\mathcal Q_{BC}\) is an auxiliary response norm, not a physical time evolution and not a conserved RD scalar.

---

# 3. SH-T16 — Sharpened response hierarchy

For the frozen normalized geodesic Wasserstein influence,
\[
\boxed{
C_{BC}
\le
\mathcal Q_{BC}
\le
\frac{\mathcal S_{BC}}{\sqrt{\lambda_B}}
\le
\frac{K^{(2)}_{BC}}{\lambda_B}
\le
\frac{K_{BC}}{\lambda_B}.
}
\]

The first inequality follows directly from:
1. conditional differentiation,
2. the Poisson equation,
3. weighted integration by parts,
4. Cauchy–Schwarz,
5. and Wasserstein-1 duality.

The second inequality follows from the conditional spectral lower bound
\[
A_B^\eta\ge\lambda_B
\]
on centered functions.

This makes \(\mathcal Q\) the preferred response coefficient whenever it can be controlled.

---

# 4. SH-T17 — Spectral/variational representation

At fixed boundary and direction,
\[
\boxed{
q^2
=
\sum_{k\ge1}
\frac{|\langle s,e_k\rangle_B|^2}{\mu_k}
=
\int_0^\infty
\langle s,e^{-tA_B}s\rangle_B\,dt,
}
\]
where
\[
A_Be_k=\mu_ke_k,\qquad\mu_k>0.
\]

Equivalently,
\[
\boxed{
q=
\sup_{E_B|\nabla_Bf|^2\le1}
|E_B[fs]|.
}
\]

Thus \(\mathcal Q\) preserves the actual conditional relaxation rate of each score component rather than charging all score components at the minimum gap \(\lambda_B\).

The parameter \(t\) in this semigroup representation is conditional diffusion time, not physical real time.

---

# 5. SH-T18 — Unchanged local-to-global engine with Poisson response

Define
\[
\theta_Q
=
\sup_B
\frac1{w_B}
\sum_{C\ne B}\mathcal Q_{BC}w_C.
\]

If positive comparison weights satisfy
\[
\boxed{\theta_Q<1,}
\]
then the frozen block-Poincaré/Dobrushin machinery gives
\[
\boxed{
\Delta
\ge
c\lambda_{\min}(1-\theta_Q).
}
\]

No new tensorization theorem is required.

Because
\[
\mathcal Q_{BC}
\le
\mathcal S_{BC}/\sqrt{\lambda_B},
\]
the \(\mathcal Q\)-criterion is a weaker sufficient requirement than the V1.1 score criterion.

---

# 6. SH-T19 — Exact source representation inside the Poisson inverse

The V1.1 score equation remains
\[
(A_B+\operatorname{Ric}_C)s_{BC}=G_{BC},
\]
where
\[
G_{BC}
=
(I-E_B)
\left[
\frac2c\nabla_CV
+
L_{B^c}^{\nabla}\nabla_CW
\right].
\]

Therefore
\[
\boxed{
A_B^{-1/2}s_{BC}
=
A_B^{-1/2}
(A_B+\operatorname{Ric}_C)^{-1}
G_{BC}.
}
\]

When
\[
\operatorname{Ric}_C=r_CI,
\]
the mode-by-mode formula is
\[
\boxed{
q_{BC}(\eta,v)^2
=
\sum_{k\ge1}
\frac{
|\langle G_{BC}^v,e_k\rangle_B|^2
}{
\mu_k(\mu_k+r_C)^2
}.
}
\]

This is now the preferred form for studying the actual vacuum source.

---

# 7. SH-T20 — Slow/fast source split

For \(M\ge\lambda_B\), define
\[
P_{\rm low}=1_{(0,M)}(A_B),
\qquad
P_{\rm high}=1_{[M,\infty)}(A_B).
\]

Then
\[
\boxed{
q_{BC}^2
\le
\frac{\|P_{\rm low}G_{BC}^v\|_2^2}
{\lambda_B(\lambda_B+r_C)^2}
+
\frac{\|P_{\rm high}G_{BC}^v\|_2^2}
{M(M+r_C)^2}.
}
\]

This localizes the difficult estimate: the source projection onto slow conditional modes matters much more strongly than source power in fast modes.

The spectral projectors themselves remain part of the unknown true conditional vacuum problem.

---

# 8. SH-T21 — Residual enclosure for approximate Poisson solves

For any smooth trial function \(\widetilde u\), define
\[
r=s-A_B\widetilde u,
\]
and
\[
\mathscr J(\widetilde u)
=
2E_B[s\widetilde u]
-
E_B|\nabla_B\widetilde u|^2.
\]

Then
\[
\boxed{
q^2
=
\mathscr J(\widetilde u)
+
\langle r,A_B^{-1}r\rangle_B,
}
\]
and hence
\[
\boxed{
\mathscr J(\widetilde u)
\le
q^2
\le
\mathscr J(\widetilde u)
+
\frac{\|r\|_{2,B}^2}{\lambda_B}.
}
\]

This converts an approximate local solve into a rigorous upper response certificate once the residual and \(\lambda_B\) are rigorously enclosed uniformly over exterior configurations and directions.

A Galerkin/trial value without the residual term gives only a lower estimate and cannot certify contraction.

---

# 9. SH-N12 — Score magnitude can falsely signal a response obstruction

The compact family
\[
W_n(x,y)
=
\varepsilon\sin(nx)\sin y
\]
on a fixed two-torus supplies a strict verification example.

For every \(n\), the conditional Poincaré constants satisfy
\[
\lambda_B\ge e^{-2\varepsilon}.
\]

The score comparison obeys
\[
\rho(M_{\rm score})
\ge
\varepsilon\sqrt{n/2},
\]
so it eventually fails to contract as \(n\to\infty\).

However, the Poisson coefficients satisfy
\[
\mathcal Q_{xy}
\le
\frac{\varepsilon e^\varepsilon}{n},
\qquad
\mathcal Q_{yx}
\le
\varepsilon n e^\varepsilon.
\]

With comparison weights
\[
w_x=1,\qquad w_y=n,
\]
one obtains
\[
\boxed{
\theta_Q
\le
\varepsilon e^\varepsilon,
}
\]
independent of \(n\).

Thus
\[
\boxed{
\Delta_n
\ge
ce^{-2\varepsilon}
(1-\varepsilon e^\varepsilon)
}
\]
when \(\varepsilon e^\varepsilon<1\).

For \(\varepsilon=0.2\), this gives
\[
\Delta_n\ge0.50657389\,c
\]
uniformly in \(n\), while at \(n=100\) the score comparison radius is at least \(1.4142\).

**Frozen conclusion:**
\[
\boxed{
\text{large boundary-score norm does not necessarily mean a soft physical mode.}
}
\]

The conditional spectral location of that score matters.

---

# 10. SH-T22 — Genuine soft modes survive the refinement

For a positive Gaussian precision matrix \(P\),
\[
\boxed{
\mathcal Q_{BC}
=
\frac{|P_{BC}|}{P_{BB}},
}
\]
which equals the exact normalized conditional Wasserstein influence for translated Gaussian conditionals.

For
\[
P=m^2I+L_G
\]
on a finite connected regular graph,
\[
\theta_Q
=
\frac{d_G}{m^2+d_G},
\]
and
\[
\lambda_{\rm loc}(1-\theta_Q)=m^2.
\]

As \(m\downarrow0\),
\[
\theta_Q\uparrow1.
\]

Therefore the Poisson refinement does not manufacture a gap where a true collective soft mode exists.

---

# 11. New preferred Yang–Mills target

The V1.2 preferred sufficient target is
\[
\boxed{
\liminf_{a\to0,\;L\to\infty}
c(a)\lambda_{\min}(a,L)
\bigl(1-\theta_Q(a,L)\bigr)>0.
}
\]

This supersedes the score criterion only as the **preferred sharp sufficient response target**. The score criterion remains valid and useful when easier to prove.

The most concrete next program is:

1. Construct conditional trial solutions of
   \[
   A_Bu=s_{BC}.
   \]
2. Obtain rigorous residual enclosures.
3. Resolve or bound the projection of the exact source
   \[
   G_{BC}
   \]
   onto slow conditional modes.
4. Keep the exterior source
   \[
   L_{B^c}^{\nabla}\nabla_CW.
   \]
5. Make every bound uniform over exterior configurations.
6. Track the true physical metric, block size, lattice spacing, volume, and units.
7. Retain transformed energy tensors and completion-fibre terms at any coarse/RG scale.
8. Only then invoke the frozen local-to-global block engine.

---

# 12. External mathematical status

The weighted negative-Sobolev interpretation used by \(\mathcal Q\) is established optimal-transport mathematics. The role of the present work is not to claim novelty for the general \(H^{-1}\)/Wasserstein machinery, but to insert the exact conditional Poisson norm into the already-frozen Steadman/Yang–Mills boundary-response architecture.

---

# 13. V1.2 freeze judgment

### Frozen as new mathematical results
- conditional Poisson coefficient \(\mathcal Q_{BC}\),
- hierarchy \(C\le\mathcal Q\le\mathcal S/\sqrt\lambda\),
- spectral and variational forms,
- unchanged block gap engine with \(\theta_Q\),
- exact source weighting by \(1/[\mu(\mu+r_C)^2]\),
- slow/fast source split,
- residual upper enclosure,
- compact torus separation example,
- Gaussian soft-mode preservation check.

### Frozen as new negative result
- raw boundary-score growth can falsely make the coarser score certificate fail when the relevant score lies in rapidly relaxing conditional modes.

### Still open
- regulator-uniform \(\mathcal Q_{BC}\) bounds for the true Yang–Mills vacuum,
- uniform knowledge/control of conditional slow spectral subspaces,
- gauge-compatible continuum/RG implementation,
- full continuum Yang–Mills construction.

### Physical SH status
Unchanged from V1/V1.1:
- RD persistence/redistribution: hypothesis,
- Smoothing: hypothesis,
- Efficiency: hypothesis,
- no independent Efficiency Force,
- no proved universal scalar RD,
- no Yang–Mills mass-gap solution.

---

\[
\boxed{
\text{V1.2 sharpens the response certificate; it does not alter the physical Steadman hypothesis.}
}
\]
