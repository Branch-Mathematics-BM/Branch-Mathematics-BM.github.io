# Steadman–Yang–Mills V1.4.10-F
## Canonical Frozen Strong-Coupling Hamiltonian Edition

**Freeze date:** 22 September 2026  
**Canonical version:** **V1.4.10-F**  
**Status:** Frozen finite-regulator / volume-uniform strong-coupling theorem package.  
**Supersedes for current use:** V1.4, V1.4.1 through V1.4.10 as separate current-status documents.  
**Preserves:** all earlier files as provenance, audit history, failed routes, and superseded bounds.  
**Does not claim:** novelty, continuum Yang–Mills construction, weak-coupling control, or a Clay mass-gap solution.

---

# 0. Freeze decision

The V1.4.x chain has now undergone repeated internal correction and an external-style review of the most delicate downstream step.

The canonical freeze retains only the statements that remain load-bearing after those corrections.

The freeze is intentionally called **V1.4.10-F**, not V1.5.

A future V1.5 should require a substantive new regime or theorem, for example:

- regulator-uniform continuation beyond the present rooted-cluster radius;
- a proved weak-bare-coupling continuation mechanism;
- a rigorously controlled continuum trajectory;
- or another result of comparable mathematical significance.

Sharpening constants inside the currently proved regime is not enough by itself to justify V1.5.

---

# 1. Formulation fixed permanently for this edition

Work on a finite three-dimensional spatial cubic lattice with link set \(E\),

\[
X=SU(2)^E.
\]

Use the continuous-time Hamiltonian

\[
\boxed{
H/c=K-\beta P,
}
\]

with

\[
\boxed{
K=-\sum_{e\in E}\Delta_e,
\qquad
P=\sum_p p_p,
\qquad
p_p=\frac12\operatorname{Tr}U_p.
}
\]

Each \(SU(2)\) link carries the unit-three-sphere metric. Therefore

\[
\boxed{
\lambda_{\text{one-link},1}=3,
\qquad
\operatorname{Ric}=2I.
}
\]

Let the normalized positive ground state be

\[
H\Omega_\beta=E_0(\beta)\Omega_\beta,
\qquad
\Omega_\beta>0,
\]

and define

\[
\boxed{
W_\beta=-2\log\Omega_\beta.
}
\]

The measure used throughout the response, Poincaré, and block analysis is

\[
\boxed{
d\nu_\beta=\Omega_\beta^2\,dU=e^{-W_\beta}dU.
}
\]

## Terminology correction

Throughout this frozen edition, **“Wilson vacuum” means the positive ground state of the Hamiltonian \(H/c=K-\beta P\)**.

It does **not** mean the four-dimensional Euclidean Wilson Gibbs measure.

“Rooted vacuum” means the rooted connected-activity representation of

\[
W=-2\log\Omega.
\]

No reflection-positivity or Euclidean transfer-matrix reconstruction is used to define \(\Omega\) in the V1.4.x theorem chain.

---

# 2. Exact ground-state transform

The vacuum equation is

\[
\boxed{
\frac12\Delta W
-\frac14|\nabla W|^2
-\beta P
=
\varepsilon_0,
\qquad
\varepsilon_0=E_0/c.
}
\]

The exact transformed generator is

\[
\boxed{
A_W
=
-\Delta+\nabla W\cdot\nabla,
}
\]

with

\[
\boxed{
\Omega^{-1}(H-E_0)\Omega
=
cA_W.
}
\]

Hence the physical finite-regulator gap is exactly the Poincaré gap of \(A_W\) on the gauge-invariant excited sector, multiplied by \(c\).

No Euclidean Gibbs-measure identification is needed for this statement.

---

# 3. Frozen rooted-activity norm

For a connected nonempty set of plaquettes \(\Gamma\), let \(\ell(\Gamma)\) be its link union.

For an activity family

\[
\mathbf F=(F_\Gamma),
\]

define

\[
\boxed{
\|\mathbf F\|_{\alpha,\kappa,\#}
=
\sup_{b\in E}
\sum_{\Gamma:\,b\in\ell(\Gamma)}
e^{\kappa|\Gamma|}
\|F_\Gamma\|_{\alpha,1}.
}
\]

The energy-analytic Fourier norm is

\[
\|f\|_{\alpha,1}
=
\sum_{\pi\ne1}
d_\pi
\sqrt{\lambda_\pi}
e^{\alpha\sqrt{\lambda_\pi}}
\|\widehat f(\pi)\|_{S_1}.
\]

All nonempty activities are Haar-centered on their full link support.

---

# 4. Frozen link-resolved bilinear theorem

For product-irrep energy

\[
\lambda_\pi=\sum_a\lambda_{\pi,a},
\]

the fundamental allocation identity is

\[
\boxed{
\sum_a
\frac{\sqrt{\lambda_{\pi,a}}}{\lambda_\pi}
\le
\frac1{\sqrt3}.
}
\]

This pays for all attachment links by electric Casimir energy rather than by cluster cardinality.

The provenance-preserving vacuum bilinear map satisfies

\[
\boxed{
\|\mathfrak B(\mathbf F,\mathbf G)\|_{\alpha,\kappa,\#}
\le
2J(\alpha)
\|\mathbf F\|_{\alpha,\kappa,\#}
\|\mathbf G\|_{\alpha,\kappa,\#},
}
\]

where

\[
\boxed{
J(\alpha)
=
\frac1{\sqrt3}
+
\frac1{3e\alpha}.
}
\]

This is a load-bearing theorem of the frozen edition.

---

# 5. Frozen uniform vacuum construction

The projected vacuum equation becomes

\[
\boxed{
\mathbf W
=
\mathbf S_\beta
-\frac12\mathfrak B(\mathbf W,\mathbf W),
}
\]

where

\[
\boxed{
(S_\beta)_{\{p\}}
=
-\frac{\beta}{6}p_p.
}
\]

The source obeys

\[
\boxed{
\|\mathbf S_\beta\|_{\alpha,\kappa,\#}
\le
S
=
\frac{32}{\sqrt3}
|\beta|
e^{\kappa+2\sqrt3\alpha}.
}
\]

If

\[
\boxed{
4J(\alpha)S<1,
}
\]

the map is a contraction on the small branch and constructs the actual positive Hamiltonian ground state.

For the canonical choice

\[
\boxed{
\alpha_*=\frac1{2\sqrt3},
\qquad
\kappa=0,
}
\]

one has

\[
J(\alpha_*)
=
\frac{e+2}{e\sqrt3},
\]

and therefore

\[
\boxed{
|\beta|<
\beta_{\rm vac}
:=
\frac3{128(e+2)}
\approx
0.00496738025665.
}
\]

This number is frozen as the endpoint of the **current volume-uniform rooted-cluster proof**.

It is **not** a finite-volume vacuum-existence boundary and is **not** asserted to be a physical phase transition.

---

# 6. Exact contraction-selected majorant

Let

\[
s=
\frac{32e}{\sqrt3}|\beta|.
\]

Then

\[
4J(\alpha_*)s
=
\frac{|\beta|}{\beta_{\rm vac}}.
\]

The contraction-selected quadratic majorant is

\[
\boxed{
R_{\rm maj}(\beta)
=
\frac{e\sqrt3}{2(e+2)}
\left[
1-
\sqrt{
1-\frac{|\beta|}{\beta_{\rm vac}}
}
\right].
}
\]

The frozen activity bound is

\[
\boxed{
\|\mathbf W_\beta\|_{\alpha_*,0,\#}
\le
R_{\rm maj}(\beta).
}
\]

---

# 7. Audited whole-Hessian operator theorem

For a nonconstant product-irrep Fourier component,

\[
\boxed{
\|\operatorname{Hess}f_\pi\|_{\rm op}
\le
\lambda_\pi
d_\pi
\|\widehat f(\pi)\|_{S_1}.
}
\]

The same-link covariant Hessian step has been explicitly audited.

On the bi-invariant \(SU(2)\) metric,

\[
\operatorname{Hess}f(X_i,X_j)
=
\frac12
(X_iX_j+X_jX_i)f,
\]

so the Levi-Civita connection does not create an additional uncontrolled term.

Hence

\[
\boxed{
\|\operatorname{Hess}f\|_{\infty,\rm op}
\le
C_{\rm op}(\alpha)
\|f\|_{\alpha,1},
}
\]

with

\[
\boxed{
C_{\rm op}(\alpha)
=
\frac1{e\alpha}.
}
\]

At the canonical analytic width,

\[
\boxed{
C_{\rm op}(\alpha_*)
=
\frac{2\sqrt3}{e}.
}
\]

For a rooted activity family,

\[
\boxed{
\|\operatorname{Hess}F\|_{\infty,\rm op}
\le
C_{\rm op}(\alpha)
\|\mathbf F\|_{\alpha,0,\#},
}
\]

uniformly in finite lattice volume.

This theorem supersedes the older Schur-Hessian constant for direct curvature estimates.

---

# 8. Frozen Hessian bound for the Yang–Mills vacuum

Define

\[
\eta(\beta)
=
\|\operatorname{Hess}W_\beta\|_{\infty,\rm op}.
\]

Then throughout the current uniform interval,

\[
\boxed{
\eta(\beta)
\le
\frac3{e+2}
\left[
1-
\sqrt{
1-\frac{|\beta|}{\beta_{\rm vac}}
}
\right].
}
\]

At the boundary,

\[
\boxed{
\eta_*
=
\frac3{e+2}
\approx
0.635824672851.
}
\]

In particular,

\[
\boxed{
\eta_*<\frac23<2.
}
\]

---

# 9. Frozen direct curvature gap

Because every \(SU(2)\) link contributes Ricci curvature \(2I\),

\[
\operatorname{Ric}+\operatorname{Hess}W
\succeq
(2-\eta)I.
\]

Therefore the Bakry–Émery estimate gives

\[
\boxed{
\lambda_B^{\rm int}
\ge
2-\eta(\beta)
}
\]

uniformly for the conditional blocks used here, and directly on the full finite-volume vacuum measure,

\[
\boxed{
\frac{\Delta_{\rm phys}}c
\ge
2-\eta(\beta).
}
\]

The limiting sufficient lower bound at the current uniform-cluster boundary is

\[
\boxed{
2-\frac3{e+2}
\approx
1.36417532715.
}
\]

This is the primary frozen gap certificate in the current strong-coupling regime.

---

# 10. Exact conditional Witten response

For a block \(B\), define

\[
A_B
=
-\Delta_B+\nabla_BW\cdot\nabla_B.
\]

For an exterior tangent source \(v\),

\[
A_Bu
=
\partial_vW
-
E_B[\partial_vW].
\]

Writing

\[
R=\nabla_Bu,
\]

covariant differentiation gives

\[
\boxed{
\left(
A_B^\nabla
+
2I
+
H_{BB}
\right)R
=
H_{B,B^c}v,
}
\]

up to the harmless sign convention associated with the exterior derivative.

This replaces the earlier false support-localization inference.

The raw scalar activity support does not by itself localize both endpoints of the response kernel.

That failed inference remains permanently retired.

---

# 11. Audited global Hilbert response estimate

Let

\[
H=\operatorname{Hess}W,
\qquad
\|H\|_{\rm op}\le\eta<2.
\]

Relative to a disjoint block decomposition,

\[
H=H_{\rm diag}+H_{\rm off}.
\]

Pinching gives

\[
\|H_{\rm diag}\|\le\eta,
\]

hence

\[
\boxed{
\|H_{\rm off}\|
\le
2\eta.
}
\]

Since

\[
A_B^\nabla+2I+H_{BB}
\succeq
(2-\eta)I,
\]

the stacked fiberwise Witten response obeys

\[
\boxed{
\rho
\le
\frac{2\eta}{2-\eta}.
}
\]

At the current uniform-cluster boundary,

\[
\boxed{
\rho_*
\le
\frac6{2e+1}
\approx
0.932174420982
<1.
}
\]

---

# 12. Corrected sweeping operator

The operator appearing in the heat-bath sweeping identity is not literally the raw pointwise Witten response.

For \(B\ne C\),

\[
\nabla_CP_Bf
=
P_B(\nabla_Cf)
-
\mathcal S_{CB}(\nabla_Bf),
\]

where \(\mathcal S_{CB}\) is the **conditionally averaged adjoint response**.

Conditional Jensen / orthogonal projection gives

\[
\boxed{
\|\mathcal S\|
\le
\|\widetilde{\mathscr R}\|
\le
\rho.
}
\]

This is the canonical formulation.

Any statement identifying \(\mathcal S\) exactly with the raw pointwise response matrix is superseded.

---

# 13. Audited Hilbert approximate tensorization

For disjoint blocks \(B_1,\dots,B_m\), define

\[
P_B=E_B,
\qquad
P=\frac1m\sum_B P_B.
\]

Each \(P_B\) is an orthogonal projection, and

\[
\boxed{
\langle f,(I-P)f\rangle
=
\frac1m
\sum_B
E_\nu\operatorname{Var}_B(f).
}
\]

Let

\[
\sigma=\|\mathcal S\|.
\]

The sweeping estimate gives

\[
\boxed{
\|\nabla Pf\|_{\mathcal H}
\le
r\|\nabla f\|_{\mathcal H},
\qquad
r=
\frac{m-1+\sigma}{m}.
}
\]

If

\[
\sigma<1,
\]

then

\[
\boxed{
\operatorname{Var}_\nu(f)
\le
\frac1{1-\sigma}
\sum_B
E_\nu\operatorname{Var}_B(f).
}
\]

Since

\[
\sigma\le\rho,
\]

the sufficient condition

\[
\boxed{
\rho<1
}
\]

gives

\[
\boxed{
\operatorname{Var}_\nu(f)
\le
\frac1{1-\rho}
\sum_B
E_\nu\operatorname{Var}_B(f).
}
\]

## Spectral-radius proof — frozen corrected form

The missing step in the earlier V1.4.9 draft is now included explicitly.

Suppose

\[
\|\nabla Pf\|_{\mathcal H}
\le
r\|\nabla f\|_{\mathcal H},
\qquad
r<1.
\]

Then

\[
\|\nabla P^nf\|_{\mathcal H}
\le
r^n
\|\nabla f\|_{\mathcal H}.
\]

At fixed finite regulator, smooth positive density on a compact connected manifold gives some finite Poincaré constant \(C_{\rm fin}\), hence for centered smooth \(f\),

\[
\|P^nf\|_2
\le
C_{\rm fin}^{1/2}
r^n
\|\nabla f\|_{\mathcal H}.
\]

Assume for contradiction that for some \(\varepsilon>0\),

\[
E_P((r+\varepsilon,1])
\ne0.
\]

Smooth centered functions are dense, so choose smooth \(f\) with

\[
g
=
E_P((r+\varepsilon,1])f
\ne0.
\]

The spectral subspace is \(P\)-invariant and orthogonal to its complement, so

\[
\boxed{
\|P^nf\|_2
\ge
\|P^ng\|_2
\ge
(r+\varepsilon)^n
\|g\|_2.
}
\]

This contradicts the \(O(r^n)\) upper bound as \(n\to\infty\).

Therefore

\[
\boxed{
\sigma(P|_{L_0^2})
\subset[0,r].
}
\]

This closes the proof-writing gap identified in external-style review.

---

# 14. Frozen full block certificate

Since

\[
\rho
\le
\frac{2\eta}{2-\eta},
\]

one has

\[
\eta<\frac23
\Longrightarrow
\rho<1.
\]

Throughout the current rooted-cluster interval,

\[
\eta(\beta)
<
\frac3{e+2}
<
\frac23.
\]

Therefore the complete block response / approximate-tensorization module closes for every

\[
\boxed{
|\beta|<
\beta_{\rm vac}
=
\frac3{128(e+2)}.
}
\]

Combining conditional curvature with approximate tensorization gives the conservative full-block lower bound

\[
\boxed{
\frac{\Delta_{\rm phys}}c
\ge
2-3\eta(\beta).
}
\]

At the current uniform-cluster boundary,

\[
\boxed{
\liminf
\frac{\Delta_{\rm phys}}c
\ge
\frac{2e-5}{e+2}
\approx
0.0925259814462.
}
\]

This full-block number is weaker than the direct curvature lower bound.

Its value is that it certifies the complete conditional-response and Hilbert tensorization architecture.

---

# 15. Finite-volume continuation — exact scope correction

At a fixed finite lattice,

\[
H(\beta)=c(K-\beta P)
\]

is a self-adjoint analytic family with common domain and compact resolvent.

The configuration manifold is compact and connected, and the real bounded plaquette potential preserves positivity improvement of the heat semigroup.

Hence the ground state is simple and strictly positive for every real \(\beta\).

Therefore

\[
\boxed{
\beta\mapsto\Omega_\beta
}
\]

can be chosen as a globally real-analytic positive normalized ground-state branch on the real line.

Thus

\[
\boxed{
W_\beta=-2\log\Omega_\beta
}
\]

exists at fixed finite regulator for every real \(\beta\).

This does **not** supply regulator-uniform locality or a regulator-uniform gap.

Therefore

\[
\boxed{
\beta_{\rm vac}
}
\]

is only the endpoint of the present volume-uniform rooted-cluster proof.

---

# 16. Frozen coupling-derivative identities

Let

\[
S_\beta
=
\partial_\beta W_\beta.
\]

With normalized

\[
d\nu_\beta=e^{-W_\beta}dU,
\]

one has

\[
E_{\nu_\beta}S_\beta=0
\]

and the exact Poisson equation

\[
\boxed{
A_\beta S_\beta
=
-2
\left(
P-\langle P\rangle_{\nu_\beta}
\right).
}
\]

Feynman–Hellmann gives

\[
\boxed{
\varepsilon_0'(\beta)
=
-\langle P\rangle_{\nu_\beta}.
}
\]

Furthermore,

\[
\boxed{
\frac{d}{d\beta}
\langle P\rangle_{\nu_\beta}
=
\frac12
E_{\nu_\beta}
|\nabla S_\beta|^2
=
2
\langle
P_0,
A_\beta^{-1}P_0
\rangle
\ge0,
}
\]

so

\[
\boxed{
\varepsilon_0''(\beta)
=
-\frac12
E_{\nu_\beta}
|\nabla S_\beta|^2
\le0.
}
\]

Thus the dimensionless finite-volume ground energy is concave in \(\beta\), and the plaquette-sum expectation is monotone increasing.

---

# 17. Frozen susceptibility-density estimate

If

\[
\gamma(\beta)
\]

is a proved weighted-generator gap, then

\[
\langle
P_0,
A_\beta^{-1}P_0
\rangle
\le
\frac{\operatorname{Var}(P)}{\gamma}.
\]

Poincaré gives

\[
\operatorname{Var}(P)
\le
\frac{E|\nabla P|^2}{\gamma}.
\]

Since every link lies in at most four plaquettes and each plaquette gradient has norm at most one,

\[
E|\nabla P|^2
\le
16|E|.
\]

Hence

\[
\boxed{
0
\le
\frac1{|E|}
\frac{d}{d\beta}
\langle P\rangle
\le
\frac{32}{\gamma(\beta)^2}.
}
\]

Inside the frozen uniform strong-coupling interval one may take

\[
\gamma(\beta)
\ge
2-\eta(\beta).
\]

---

# 18. Results retained as valid but non-load-bearing

The following intermediate developments may remain useful, but they are not needed to establish the canonical frozen theorem package:

- sharper cubic-block shell geometry
  \[
  a_n=10n^2+2;
  \]
- the explicit comparison factor
  \[
  G(\mu)
  =
  \frac{2e^{-\mu}(6+3e^{-\mu}+e^{-2\mu})}
  {(1-e^{-\mu})^3};
  \]
- exact first-order Wilson Hessian extraction;
- exact second-order connected Wilson-sector calculations;
- response-rooted single-source activity estimates;
- weighted exponential response estimates.

These are preserved as auxiliary modules and can be reused.

They no longer define the best frozen coupling interval.

---

# 19. Superseded or excluded from the freeze

## 19.1 False support localization — retired

The inference

\[
\text{scalar activity support}
\Longrightarrow
\text{both response-kernel endpoints lie in that support}
\]

is false.

The explicit counterexample from V1.4 remains part of the audit record.

Use the Witten/Bochner response equation instead.

---

## 19.2 Old response thresholds — superseded as canonical endpoints

The successive sufficient block thresholds

\[
10^{-4},
\quad
5\times10^{-4},
\quad
8\times10^{-4},
\quad
1.3\times10^{-3},
\quad
1.6\times10^{-3}
\]

were useful development milestones.

They are no longer the canonical block endpoint.

The Hilbert tensorization theorem closes the full block module throughout

\[
|\beta|<\beta_{\rm vac}.
\]

---

## 19.3 Old \(3.11\times10^{-3}\) curvature endpoint — superseded

The older direct-curvature endpoint arose from a Hessian estimate containing a spatial-width loss.

The audited whole-Hessian operator theorem supersedes it.

---

## 19.4 Numerical optimized endpoints — diagnostics only

Non-rational optimized decimals such as the previous

\[
5.85\times10^{-4},
\quad
8.72\times10^{-4},
\quad
1.33\times10^{-3},
\quad
1.72\times10^{-3}
\]

are retained only as historical diagnostics.

They have no canonical status.

---

## 19.5 Physical-activity quotient / full inverse continuation — not frozen as a theorem

The V1.4.3 quotient construction and the proposed full local-analytic inverse estimates remain promising, but they are not required for this frozen edition and have not received the same completed audit as the load-bearing chain above.

They remain **candidate continuation machinery**, not frozen theorems.

---

# 20. Prior-art and novelty status

The existence of a strong-coupling lattice Yang–Mills gap is established prior art.

Therefore the frozen claim is **not**

> “a new proof that strong-coupling lattice Yang–Mills has a mass gap”

as a novelty assertion.

The possible contribution is instead the particular quantitative architecture

\[
\boxed{
\text{rooted vacuum activities}
\to
\operatorname{Hess}W
\to
\text{conditional Witten response}
\to
\text{Hilbert block influence}
\to
\text{approximate tensorization / gap}.
}
\]

Whether this architecture, its norms, or its constants are genuinely novel requires a dedicated prior-art comparison.

Novelty is therefore frozen as

\[
\boxed{
\text{UNVERIFIED}.
}
\]

---

# 21. Explicit nonclaims

V1.4.10-F does **not** prove:

- four-dimensional continuum Yang–Mills existence;
- a regulator-uniform weak-bare-coupling mass gap;
- asymptotic-freedom-compatible continuum scaling;
- Osterwalder–Schrader reconstruction;
- equivalence to the four-dimensional Euclidean Wilson Gibbs theory by reflection positivity;
- a nontrivial continuum limit;
- the Clay Millennium Yang–Mills mass-gap problem;
- that \(\beta_{\rm vac}\) is a physical critical coupling;
- that the current proof is novel.

---

# 22. Current actual frontier

At fixed finite regulator:

\[
\boxed{
\Omega_\beta
\text{ exists as a unique positive ground state for all real }\beta.
}
\]

Uniformly in the finite lattice volume, the present rooted-locality machinery is proved for

\[
\boxed{
|\beta|
<
\frac3{128(e+2)}.
}
\]

Inside that interval, the frozen edition controls:

- the rooted vacuum activities;
- the whole vacuum Hessian;
- the direct curvature gap;
- conditional Witten response;
- the global Hilbert influence operator;
- approximate tensorization;
- the complete block gap;
- and plaquette susceptibility density.

Therefore the true next problem is

\[
\boxed{
\textbf{extend regulator-/volume-uniform locality and gap control beyond the current rooted-cluster radius.}
}
\]

The most economical continuation target is the physical forcing direction

\[
\boxed{
S_\beta
=
-2
A_\beta^{-1}
\left(
P-\langle P\rangle
\right),
}
\]

rather than an unnecessarily strong inverse bound in every activity-space direction.

---

# 23. Reopening rule

This frozen version is to be changed only if one of the following occurs:

1. a counterexample invalidates a frozen theorem;
2. an independent audit finds a missing hypothesis or proof gap;
3. a normalization error changes a frozen constant;
4. a stronger theorem strictly supersedes a frozen theorem and has itself passed strict audit;
5. a genuine continuation result justifies advancing to V1.5.

Ordinary exploratory calculations do not alter this freeze.

---

# 24. Canonical status statement

\[
\boxed{
\begin{array}{l}
\textbf{V1.4.10-F is frozen.}\\[1mm]
\text{It is a Hamiltonian finite-regulator / volume-uniform strong-coupling result.}\\[1mm]
\text{The direct gap certificate is positive throughout the current rooted-cluster interval.}\\[1mm]
\text{The full Hilbert block-response module also closes throughout that interval.}\\[1mm]
\text{Finite-volume vacuum existence itself continues for all real coupling.}\\[1mm]
\text{The unresolved frontier is regulator-uniform continuation toward the continuum regime.}\\[1mm]
\text{Novelty remains unverified.}\\[1mm]
\text{No Clay Yang--Mills solution is claimed.}
\end{array}
}
\]

---

## Frozen numerical constants

\[
\boxed{
\beta_{\rm vac}
=
\frac3{128(e+2)}
=
0.00496738025665\ldots
}
\]

\[
\boxed{
\eta_*
=
\frac3{e+2}
=
0.635824672851\ldots
}
\]

\[
\boxed{
\rho_*
\le
\frac6{2e+1}
=
0.932174420982\ldots
}
\]

\[
\boxed{
\left(\frac{\Delta_{\rm direct}}c\right)_{\rm boundary}
\ge
2-\frac3{e+2}
=
1.36417532715\ldots
}
\]

\[
\boxed{
\left(\frac{\Delta_{\rm block}}c\right)_{\rm boundary}
\ge
\frac{2e-5}{e+2}
=
0.0925259814462\ldots
}
\]

These are sufficient proof bounds in the stated normalization, not measured physical masses.
