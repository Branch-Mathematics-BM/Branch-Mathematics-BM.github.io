# Steadman Hypothesis — Strict Review and Version 1 Freeze Log

**Date:** 21 September 2026  
**Project:** Branch Mathematics / GURF  
**Status:** Canonical Steadman Hypothesis Version 1 working freeze  
**Governance:** Does not modify the frozen Branch Mathematics Version 1 foundation.

## 1. Executive judgment

The Steadman Hypothesis (SH) is coherent enough to preserve as a three-part research hypothesis, but it is not yet a proved universal law, a new fundamental force, a Yang–Mills solution, or a replacement for the Standard Model.

The canonical structure is:

1. **Relativistic-Determination (RD):** persistence/redistribution constraint.
2. **Smoothing:** redistribution/regularization mechanism or tendency.
3. **Efficiency:** response-cost/transmission selection principle.

Only partial mathematical support is currently proved. In particular, injective evolution transports complete relational distinctions, but this does not prove conservation of every receiver-dependent RD scalar.

---

# 2. Frozen terminology and definitions

## SH-D1 — Relativistic-Determination (RD)
**Status: FROZEN NAME; universal invariant still open.**

The canonical name is **Relativistic-Determination (RD)**. Earlier project usage of “Relative-Determination” is terminologically superseded without changing the mathematics already derived.

RD is intended to refer to physically relevant distinctions/relations that remain present somewhere in a complete lawful description even when they are no longer visible to a chosen receiver, subsystem, scale, or coarse representation.

The statement

> **RD cannot be destroyed; it can only be redistributed**

is frozen as the central physical hypothesis, not as a theorem.

No universal scalar \(D_{\rm total}\) has yet been defined and proved invariant.

If “Relativistic” is meant literally, any eventual local conservation law must be relativistically covariant. A candidate form such as
\[
\partial_\mu J^\mu_{\rm RD}=0
\]
is therefore a research target, not an established equation.

## SH-D2 — Smoothing
**Status: FROZEN CONCEPT.**

Smoothing is the process by which accessible/local structure becomes more regular or less fine-grained while distinctions may move into other scales, correlations, carriers, or completion fibres.

Smoothing is not automatically entropy, dissipation, real time, Euclidean time, gradient flow, or a mass gap.

Any application must state:
- the smoothing map/evolution,
- whether it is injective,
- the receiver/scale,
- where omitted distinctions go,
- and how the physical energy metric transforms.

## SH-D3 — Physical Transmission Domain (PTD)
**Status: FROZEN TERMINOLOGY.**

A PTD fixes the system, constraints, admissible inputs and outputs, receiver, units/metric, and transmission task within which an efficiency comparison is meaningful.

## SH-D4 — Response Channel
**Status: FROZEN TERMINOLOGY.**

A Response Channel is a specified lawful route by which an input/disturbance produces a response inside a PTD.

## SH-D5 — Response efficiency
**Status: FROZEN DEFINITION.**

\[
\boxed{
\eta_R=
\frac{\text{actual useful transmitted response}}
{\text{ideal admissible transmitted response}}
}
\]

and

\[
\boxed{R_{\rm out}=\eta_R R_{\rm ideal}.}
\]

If the ideal response is truly the maximum admissible response under the same constraints, then \(0\le\eta_R\le1\). A result above 1 means the reference/domain/channel was misdefined or the certification failed.

This is an accounting definition, not yet a force law.

---

# 3. Core Steadman Hypothesis V1

## SH-H1 — RD Persistence / Redistribution
**Status: FROZEN HYPOTHESIS.**

A closed lawful physical description does not fundamentally annihilate complete Relativistic-Determination; RD may be redistributed among local state, correlations, fields, radiation, scales, precision, environment/internal sectors, or other lawful carriers.

A future complete theory may use a schematic decomposition
\[
\mathscr D_{\rm total}
=
\mathscr D_{\rm local}
+\mathscr D_{\rm corr}
+\mathscr D_{\rm field}
+\mathscr D_{\rm radiation}
+\cdots,
\]
but this is not yet a proved additive conservation law.

## SH-H2 — Smoothing Hypothesis
**Status: FROZEN HYPOTHESIS.**

Lawful dynamics or lawful re-expression may make accessible structure smoother while complete distinctions are redistributed rather than automatically erased.

Smoothing alone cannot imply a mass gap.

## SH-H3 — Efficiency Principle
**Status: FROZEN HYPOTHESIS.**

Among dynamically admissible response channels, physical transmission may be constrained or selected by cost/efficiency.

The presently frozen object is \(\eta_R\), not a new force.

Historical candidate notation included a context
\[
\Xi=(D,T,\mathcal C,\mathcal R)
\]
and a possible effective law
\[
F_\eta=-\nabla V_\Xi.
\]
This remains conjectural.

---

# 4. Frozen mathematical support

## SH-T1 — Transport of complete relational structure
Under an injective map \(\Phi:S\to S'\), transported receivers
\[
r_i^\Phi=r_i\circ\Phi^{-1}
\]
carry joint receiver fibres bijectively. Complete distinctions are transported.

This does not imply conservation of a fixed receiver-dependent scalar.

## SH-T2 — Uniform contraction gap criterion
On the excited sector
\[
A=(H-E_0)|_{\Omega^\perp},
\]
\[
\|e^{-\tau A}\|=e^{-\tau\Delta}.
\]
Therefore a valid uniform bound
\[
\|e^{-\tau A}\|\le q<1
\]
implies
\[
\boxed{\Delta\ge-\frac{\log q}{\tau}>0.}
\]

## SH-T3 — Direct quadratic-form certificate
If
\[
h[\psi_r]\ge d_r\|\psi_r\|^2,
\]
\[
|h(\psi_r,\psi_s)|\le t_{rs}\|\psi_r\|\|\psi_s\|,
\]
and positive weights satisfy
\[
\mu=
\inf_r\left[
d_r-\sum_{s\ne r}t_{rs}\frac{w_s}{w_r}
\right]>0,
\]
then
\[
\boxed{A\ge\mu I,\qquad\Delta\ge\mu.}
\]

## SH-T4 — Conditional Yang–Mills block engine
For the true regulated vacuum measure
\[
d\nu_{a,L}=\Omega_{a,L}^2dU,
\]
the validated disjoint-block module is
\[
\boxed{
\Delta_{a,L}\ge
c(a)\lambda_{\rm loc}(a,L)(1-\theta_{a,L}).
}
\]

With
\[
K_{BC}
=
\sup_U\|\nabla_B\nabla_C(-2\log\Omega)\|_{\rm op},
\]
the conditional response bound is
\[
\boxed{C_{BC}\le\frac{K_{BC}}{\lambda_B}.}
\]

This is a sufficient certificate, not a continuum Yang–Mills proof.

## SH-T5 — Boundary-score refinement
Define
\[
s_{BC}^{v}
=
\partial_vW-E_B[\partial_vW],
\qquad W=-2\log\Omega,
\]
and
\[
S_{BC}
=
\sup_{\eta,\|v\|=1}
\|s_{BC}^{v}\|_{L^2(\nu_B)}.
\]
Then, under the conditional Poincaré assumptions,
\[
\boxed{
C_{BC}\le
\frac{S_{BC}}{\sqrt{\lambda_B}}
\le
\frac{K^{(2)}_{BC}}{\lambda_B}
\le
\frac{K^{(\infty)}_{BC}}{\lambda_B}.
}
\]

This freezes the strategy of targeting the weakest provable response quantity first.

## SH-T6 — Smoothing carries the physical energy metric
For an invertible change \(y=\Phi(x)\),
\[
\int\Gamma_X(f)d\nu
=
\int
\langle\nabla_Yg,\mathsf A\nabla_Yg\rangle d\bar\nu,
\qquad
\mathsf A=D\Phi D\Phi^*.
\]

A smoothing transformation is never allowed to discard this transformed energy metric.

## SH-T7 — Coarse-graining retains completion-fibre variation
For \(Y=\Pi(X)\),
\[
\operatorname{Var}(f)
=
E[\operatorname{Var}(f|Y)]
+
\operatorname{Var}(E[f|Y]).
\]

The completion-fibre term must remain controlled. With suitable fibre/coarse/derivative estimates,
\[
\boxed{
\Delta\ge
\frac{c}{C_{\rm fib}+K_\Pi C_{\rm coarse}}.
}
\]

## SH-T8 — Small-branch continuation lemma
If
\[
r(s)\le j(s)+\alpha r(s)^2,
\quad r(0)=0,
\quad j(s)\le j_*<\frac1{4\alpha},
\]
and \(r(s)\) is continuous, then
\[
\boxed{
r(s)\le
\frac{1-\sqrt{1-4\alpha j_*}}{2\alpha}.
}
\]

This fixes the earlier branch-selection mistake. A Yang–Mills application still requires deriving the inequality from the actual dynamics.

---

# 5. Frozen negative results

## SH-N1 — No universal conservation of a fixed receiver-dependent RD scalar
Complete distinctions may remain recoverable while a chosen scalar such as \(D(B|A)\) changes.

## SH-N2 — Smoothing plus persistence does not imply a mass gap
The model
\[
H\Omega=0,\qquad He_n=\frac1n e_n
\]
has strict damping of every fixed excitation but
\[
\Delta=0.
\]

The missing ingredient is uniform coercivity/contraction.

## SH-N3 — Local restoring strength alone does not prevent collective soft modes
The exact Gaussian test has uniform local conditional gaps while the global gap tends to zero as block influence tends to one.

This is the rigorous form of the capacitor-network dilution problem.

## SH-N4 — Positive finite Schur pivots are insufficient for a strict infinite-dimensional margin
Additional uniform triangular-factor/coercivity control is required.

## SH-N5 — Whole-block total variation can be too strong a response metric
It may approach 1 while normalized Wasserstein response and tensorization remain uniformly controlled.

## SH-N6 — Planck-length stepping is not a mass-gap proof
A minimum spatial step alone does not exclude collective configurations with energy approaching zero.

---

# 6. Efficiency Force status

\[
\boxed{\text{Efficiency Force is NOT frozen as a discovered fundamental force.}}
\]

No independent dynamical term, coupling constant, or distinguishing prediction has yet been derived.

What survives is:
- Efficiency Principle,
- PTD,
- Response Channel,
- \(\eta_R\).

“Efficiency Force” may be promoted only if an independent dynamical law is derived and experimentally distinguishable from known dynamics.

---

# 7. Electroweak blind reconstruction

## SH-EW1 — Blind reconstruction method
**Status: FROZEN AS METHOD, NOT NEW PHYSICS.**

For analysis, conventional group labels can be withheld and the minimum structure reconstructed from observed interaction behavior. The current reconstruction identifies paired charged conversion directions, independent neutral structure, handed selection, family mixing, and background response before comparison with the standard electroweak representation.

## SH-EW2 — Background-response mass matrix
**Status: STANDARD-QFT TRANSLATION.**

For interaction directions \(X_a\) acting on a background \(h_0\),
\[
\mathcal R_{h_0}:X_a\mapsto X_ah_0,
\]
\[
\boxed{
M^2_{ab}
=
\langle X_ah_0,X_bh_0\rangle
=
\mathcal R_{h_0}^\dagger\mathcal R_{h_0}.
}
\]

Thus
\[
M^2\ge0,
\qquad
\ker M^2=\ker\mathcal R_{h_0}.
\]

This is the ordinary coordinate-free Higgs-generated vector-boson mass-squared matrix. Calling its diagonalization “Efficiency” or its eigenvectors “Smoothing” does not create new physics.

## SH-EW3 — Real Steadman target
SH must work upstream of this matrix and explain or constrain something not already inserted, such as:
- why \(h_0\neq0\),
- the background scale,
- a coupling relation,
- neutral mixing,
- or another measurable relation.

## SH-EW4 — Fixed finite total RD vacuum model fails
If a finite total RD is spread uniformly through volume,
\[
|h_0|^2\propto D_0/V,
\]
so \(|h_0|\to0\) as \(V\to\infty\).

## SH-EW5 — Efficiency alone does not choose the standard vacuum orientation
At fixed scalar magnitude, the summed generator-response cost is Casimir-like/constant across gauge-equivalent orientations. Simple response minimization therefore does not derive the physical vacuum.

## SH-EW6 — Extensive RD density
**Status: OPEN CONJECTURE ONLY.**

An extensive RD density could avoid infinite-volume dilution, but no such physical density/current has been derived. It cannot simply be fitted to the electroweak scale.

---

# 8. Yang–Mills status

The valid Steadman/Yang–Mills engine is the block/Poincaré/response machinery above.

The current sufficient continuum target is of the form
\[
\liminf_{a\to0,L\to\infty}
c(a)\lambda_{\min}(a,L)
\left[
1-
\sup_B
\frac{\sum_{C\ne B}K_{BC}(a,L)w_C}
{\lambda_B(a,L)w_B}
\right]>0,
\]
or a weaker boundary-score/\(L^2\)-response version.

The required regulator-uniform estimates have not been derived from the actual Yang–Mills vacuum dynamics, and the continuum construction remains separate.

Therefore
\[
\boxed{\text{Steadman has not solved the Yang–Mills mass-gap problem.}}
\]

The central unresolved enemy is an arbitrarily soft collective mode.

---

# 9. Canonical Steadman Hypothesis V1 statement

> **Steadman Hypothesis V1.** A lawful closed physical description may preserve complete Relativistic-Determination while redistributing it among states, relations, correlations, scales, fields, radiation, or other admissible carriers. Smoothing describes reorganization of accessible structure but does not by itself destroy complete determination or imply a spectral gap. Efficiency describes the ratio/cost of admissible response transmission within a specified Physical Transmission Domain and Response Channel and is conjectured to constrain which lawful redistributions are dynamically favored. Any claimed universal RD conservation law, Efficiency Force, mass-gap mechanism, or vacuum-selection mechanism requires an explicit invariant/dynamics and independent validation.

This is the strongest current statement that survives the existing counterexamples.

---

# 10. Governance rules frozen with V1

1. Do not rename standard physics and count it as a Steadman prediction.
2. Do not call Efficiency a force without a distinct dynamical law.
3. Do not call a receiver-dependent RD scalar conserved merely because exact evolution is injective.
4. Do not infer a mass gap from qualitative Smoothing.
5. Do not infer a global gap from local restoring bounds without collective-response control.
6. Do not discard the energy metric under invertible smoothing.
7. Do not discard completion-fibre variation under coarse-graining.
8. Track physical units and regulator dependence.
9. Keep real time, Euclidean time, and auxiliary flow time distinct.
10. Preserve counterexamples and failed routes.
11. Label every new claim as Definition, Theorem, Conditional Theorem, Conjecture, Numerical Evidence, Interpretation, or Failure.
12. Do not alter the frozen BM Version 1 foundation unless a genuine contradiction forces repair.

---

# 11. Promotion gates

Steadman remains a hypothesis/framework until at least one major gate is crossed.

### Gate A — RD object
Define its exact mathematical type, normalization/dimensions, composition law, receiver dependence, gauge behavior, covariance, and conservation/transport law.

### Gate B — Smoothing law
Specify an actual physical evolution or functional with a proved nontrivial monotonic/extremal property.

### Gate C — Efficiency dynamics
Derive a predictive cost/efficiency evolution rather than re-expressing the original equations.

### Gate D — Independent prediction
Produce a relation, number, or selection rule not fitted from existing data.

### Gate E — Yang–Mills
Prove regulator-uniform physical response/restoring estimates and complete the required continuum theory.

### Gate F — Electroweak
Derive or constrain an upstream quantity such as the nonzero background scale or a coupling relation, rather than merely reproducing the known mass matrix.

---

# 12. Frozen today

## Core
- Relativistic-Determination terminology.
- RD persistence/redistribution hypothesis.
- Smoothing hypothesis.
- Efficiency Principle.
- Physical Transmission Domain.
- Response Channel.
- \(\eta_R\).
- strict separation of the three roles.

## Mathematical support
- injective transport of complete relations,
- uniform-contraction gap criterion,
- direct quadratic-form criterion,
- conditional Yang–Mills block engine,
- mixed-Hessian response estimate,
- boundary-score/\(L^2\) refinement,
- energy-metric requirement under smoothing,
- completion-fibre requirement under coarse-graining,
- small-branch continuation lemma.

## Permanent negative record
- no universal fixed-receiver RD scalar conservation,
- Smoothing + persistence does not imply a gap,
- local positivity does not exclude collective soft modes,
- finite Schur pivots do not ensure a strict infinite-dimensional margin,
- whole-block TV may be over-strong,
- Planck stepping is not a gap proof,
- Efficiency alone does not derive the electroweak vacuum,
- finite total RD dilutes in infinite volume.

## Logged but not frozen as physical law
- Efficiency Force,
- universal additive RD scalar,
- universal RD current,
- extensive RD density as vacuum origin,
- Steadman derivation of electroweak parameters,
- Steadman proof of Yang–Mills.

---

# 13. Source record

Primary audited internal records:

1. **BM_Steadman_Yang_Mills_Proof_Audit_2026-09-20(1).md**
   - claim/status table: lines 14–29,
   - transport of complete relations: lines 28–49,
   - smoothing-to-gap counterexample: lines 69–87 onward,
   - final status/no new force: lines 623–635.

2. **BM_Steadman_Yang_Mills_Block_Poincare_Module_2026-09-20(2).md**
   - block local-to-global certificate: lines 3–15,
   - collective soft-mode diagnostic: lines 276–290,
   - energy metric under smoothing: lines 341–358 onward,
   - completion-fibre accounting: lines 398–419 onward,
   - continuum Yang–Mills target: lines 470–491 onward.

This freeze also incorporates the subsequent September 21 blind electroweak reconstruction, while separating standard-QFT translation from actual Steadman conjectures.

---

## Final status

\[
\boxed{\text{Steadman Hypothesis V1 is frozen as a research hypothesis.}}
\]

\[
\boxed{\text{Its strongest present content is structural/conditional, not a new universal physical law.}}
\]

\[
\boxed{\text{The next legitimate target is an explicit RD object/dynamics or an independent prediction.}}
\]

---

# Version 1.1 Verification Addendum — Vacuum Hessian Bootstrap

**Date:** 21 September 2026  
**Status:** Canonical mathematical addendum to Steadman Hypothesis V1.  
**Governance:** This addendum does not alter the BM V1 foundation, does not alter the frozen block-Poincaré module, and does not promote any Yang–Mills conjecture to theorem.

## A. Newly frozen mathematical results

### SH-T9 — Exact vacuum Hamilton–Jacobi identity
For
\[
H=-c\Delta_X+V,\qquad H\Omega=E_0\Omega,\qquad \Omega>0,
\]
and
\[
W=-2\log\Omega,
\]
the exact identity is
\[
\boxed{
\frac c2\Delta W-\frac c4|\nabla W|^2+V=E_0.
}
\]

The ground-state transform is
\[
\boxed{
\Omega^{-1}(H-E_0)\Omega=-cL_W,
\qquad
L_W=\Delta-\nabla W\cdot\nabla.
}
\]

This fixes the normalization and makes the physical factor \(c\) explicit.

---

### SH-T10 — Exact covariant mixed vacuum-Hessian equation
On a finite product of compact connected Riemannian manifolds, for distinct disjoint blocks \(B,C\), define
\[
F_{BC}=\nabla_B\nabla_CW.
\]
Then
\[
\boxed{
L_W^\nabla F_{BC}
=
\operatorname{Ric}_B F_{BC}
+
F_{BC}\operatorname{Ric}_C
+
\sum_DF_{BD}F_{DC}
-
\frac2cV_{BC}.
}
\]

The Ricci and connection-Laplacian terms are part of the exact equation and may not be dropped.

---

### SH-T11 — Integrated Hessian bootstrap from conditional gaps
Let
\[
S_B=\operatorname{Ric}_B+F_{BB},
\]
and define
\[
\mathcal T_{BC}F
=
-L_W^\nabla F+S_BF+FS_C.
\]

Then
\[
\mathcal T_{BC}F_{BC}
=
\frac2cV_{BC}
-
\sum_{D\notin\{B,C\}}F_{BD}F_{DC}.
\]

Under the frozen conditional Poincaré hypotheses,
\[
\boxed{
\langle F_{BC},\mathcal T_{BC}F_{BC}\rangle
\ge
(\lambda_B+\lambda_C)
\|F_{BC}\|_{2,\mathrm{HS}}^2.
}
\]

Therefore
\[
\boxed{
(\lambda_B+\lambda_C)\|F_{BC}\|_{2,\mathrm{HS}}
\le
\frac2c\|V_{BC}\|_{2,\mathrm{HS}}
+
\sum_{D\notin\{B,C\}}
\|F_{BD}F_{DC}\|_{2,\mathrm{HS}}.
}
\]

This uses only conditional gaps and does not assume the global mass gap to be proved.

---

### SH-T12 — Exact centered boundary-score equation
For the centered score
\[
s_{BC}
=
(I-E_B)\nabla_CW,
\]
the exact conditional equation is
\[
\boxed{
(-L_B+\operatorname{Ric}_C)s_{BC}=G_{BC},
}
\]
with
\[
\boxed{
G_{BC}
=
(I-E_B)
\left[
\frac2c\nabla_CV
+
L_{B^c}^{\nabla}\nabla_CW
\right].
}
\]

If \(\operatorname{Ric}_C\ge r_CI\),
\[
\boxed{
\mathcal S_{BC}
\le
\frac{\mathcal E_{BC}}{\lambda_B+r_C},
}
\]
and therefore
\[
\boxed{
C_{BC}
\le
\frac{\mathcal E_{BC}}
{\sqrt{\lambda_B}(\lambda_B+r_C)}.
}
\]

The exterior source term \(L_{B^c}^{\nabla}\nabla_CW\) is essential and cannot be discarded.

---

### SH-T13 — Supremum bootstrap under pointwise block curvature
If
\[
\boxed{
S_B(U)
=
\operatorname{Ric}_B+\nabla_B^2W(U)
\ge
\gamma_BI,
\qquad \gamma_B>0,
}
\]
then for \(B\neq C\),
\[
\boxed{
K_{BC}
\le
\frac{
2J^V_{BC}/c+
\sum_{D\notin\{B,C\}}K_{BD}K_{DC}
}{
\gamma_B+\gamma_C
}.
}
\]

This is a genuine supremum estimate, but the pointwise Bakry–Émery assumption is stronger than the conditional Poincaré assumption.

---

### SH-T14 — Valid small-branch continuation theorem
Along a smooth finite-regulator path \(V_s\) beginning at a constant potential, assume
\[
S_B^{(s)}\ge\gamma_0I>0
\]
uniformly and
\[
\eta_*
=
\sup_s
\frac{\|J^{V_s}\|_w}
{c\gamma_0^2}
<
\frac12.
\]

Then
\[
\boxed{
\frac{\|K_s\|_w}{\gamma_0}
\le
1-\sqrt{1-2\eta_*}<1,
}
\]
and the frozen block module yields
\[
\boxed{
\Delta_s
\ge
c\gamma_0\sqrt{1-2\eta_*}>0.
}
\]

This is the correct branch-selection mechanism. Continuity selects the small branch because the path begins at the uncoupled solution \(K_0=0\).

---

## B. Newly frozen negative results / restrictions

### SH-N7 — Conditional scalar inverse is not enough
A conditional Poincaré gap controls the inverse of the centered scalar block generator in \(L^2\). It does not automatically control the supremum mixed Hessian \(K_{BC}\) because:
1. exterior derivatives produce a nonlocal source,
2. the mixed Hessian need not be conditionally centered,
3. \(L^2\) control does not imply a regulator-uniform \(L^\infty\) bound.

---

### SH-N8 — A global \(L^2\) Hessian estimate cannot replace boundary-uniform conditional control
The integrated estimate averages over the full vacuum measure. The influence theorem needs a supremum over exterior configurations. Rare boundary conditions therefore remain relevant.

---

### SH-N9 — The scalar quadratic inequality does not choose the small branch
From
\[
r\le j+r^2
\]
alone, both a small and a large branch are allowed.

Branch selection requires a continuity/path argument plus a strict branch-separation condition.

---

### SH-N10 — Response-radius diagnostics are sufficient, not necessary
For a finite block scheme, quantities such as
\[
1-\rho(\Lambda^{-1}K)
\]
can certify a gap when positive under the frozen hypotheses, but a negative value does not prove the physical gap is absent.

The scalar comparison can lose coherent cancellation.

---

### SH-N11 — Improved influence under RG/smoothing does not imply an improved physical gap
A Gaussian convolution example can make the normalized influence parameter decrease while the actual spectral lower constant also decreases.

Therefore the complete physical expression, including the local restoring scale and transformed energy form, must always be tracked.

---

## C. Compact SU(2) verification model

The two-factor compact \(SU(2)\) model with
\[
W=\varepsilon uv
\]
provides a curved compact-group consistency check of the exact tensor equation and the continuation theorem.

For \(0<\varepsilon<2\),
\[
K_{12}=\varepsilon,
\qquad
S_1,S_2\ge(2-\varepsilon)I.
\]

At \(\varepsilon=0.1\), the continuation theorem gives a positive explicit lower bound. This is a verification model only: its potential is reverse-constructed from the chosen vacuum and is not the Wilson Yang–Mills potential.

---

## D. Preferred Yang–Mills target after V1.1

The **first preferred route** is now the boundary-score route, not the stronger pointwise Hessian-supremum route.

Define
\[
\theta_{\rm score}
=
\sup_B
\frac1{\sqrt{\lambda_B}w_B}
\sum_{C\ne B}\mathcal S_{BC}w_C.
\]

A sufficient target is
\[
\boxed{
\theta_{\rm score}<1,
}
\]
together with
\[
\boxed{
\liminf_{a\to0,\;L\to\infty}
c(a)\lambda_{\min}(a,L)
(1-\theta_{\rm score})
>0.
}
\]

Equivalent work may instead bound the explicit centered-score source \(G_{BC}\) appearing in SH-T12.

The **second, stronger route** is to prove a uniform pointwise block-curvature floor and small bare mixed-Hessian bound along a gauge-compatible path/RG flow.

Neither route has yet been established for the actual Yang–Mills vacuum through the required regulator limits.

---

## E. V1.1 status

The Steadman Hypothesis itself remains unchanged:

- RD persistence/redistribution — hypothesis.
- Smoothing — hypothesis.
- Efficiency — hypothesis.
- No fundamental Efficiency Force has been established.
- No universal conserved scalar RD has been established.
- No continuum Yang–Mills mass-gap proof has been established.

What V1.1 adds is a substantially sharper mathematical bridge:

\[
\boxed{
\text{vacuum equation}
\rightarrow
\text{mixed Hessian / centered score}
\rightarrow
\text{boundary influence}
\rightarrow
\text{block tensorization}
\rightarrow
\text{conditional gap certificate}.
}
\]

The unresolved step is now sharply localized to obtaining regulator-uniform, gauge-compatible control of the true vacuum response.
