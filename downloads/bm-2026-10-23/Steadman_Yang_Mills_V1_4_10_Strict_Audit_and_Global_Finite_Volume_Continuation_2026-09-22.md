# Steadman–Yang–Mills V1.4.10
## Strict Audit of Hilbert Tensorization and Global Finite-Volume Vacuum Continuation

**Date:** 22 September 2026  
**Baseline:** V1.4.9 Hilbert approximate tensorization  
**Status:** V1.4.9 survives strict audit with one operator-identification repair. New exact finite-volume continuation and susceptibility results are added. No continuum Yang–Mills claim.

---

# 1. Audit target

V1.4.9 had two delicate steps:

1. converting gradient contraction of the averaged heat-bath operator into an \(L^2\) spectral gap;
2. identifying the operator in the sweeping identity with the stacked conditional-response operator.

The first step is valid.

The second requires a notation correction: the sweeping operator is a conditional-averaged adjoint of the pointwise Witten response, not literally the raw pointwise response matrix.

Its norm is nevertheless bounded by the stacked Witten-response norm, so all final inequalities survive.

---

# 2. SH-T90 — Audited heat-bath spectral argument

Let

\[
P_B=E_B
\]

be conditional expectation over block \(B\), and

\[
P=\frac1m\sum_B P_B.
\]

Each \(P_B\) is an orthogonal projection on \(L^2(\nu)\).

Hence \(P\) is self-adjoint, positive, and

\[
0\preceq P\preceq I.
\]

Moreover,

\[
\boxed{
\langle f,(I-P)f\rangle
=
\frac1m
\sum_B
E_\nu\operatorname{Var}_B(f).
}
\]

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
r^n\|\nabla f\|_{\mathcal H}.
\]

At every fixed finite regulator, \(\nu\) has a smooth strictly positive density on a compact connected configuration manifold, so some finite global Poincaré constant \(C_{\rm fin}\) exists:

\[
\|g-E_\nu g\|_2^2
\le
C_{\rm fin}
\|\nabla g\|_{\mathcal H}^2.
\]

For centered smooth \(f\),

\[
\|P^nf\|_2^2
\le
C_{\rm fin}r^{2n}
\|\nabla f\|_{\mathcal H}^2.
\]

If the spectral measure of \(P\) on \(f\) had positive mass in
\((r+\varepsilon,1]\), the spectral theorem would give a lower bound growing as
\((r+\varepsilon)^{2n}\), contradicting the preceding estimate.

Therefore

\[
\boxed{
\sigma(P|_{L_0^2})\subset[0,r].
}
\]

Hence

\[
\boxed{
I-P\succeq(1-r)I
}
\]

on centered functions.

The finite-volume Poincaré constant disappears from the final inequality.

---

# 3. The exact sweeping operator

For \(B\ne C\),

\[
\nabla_CP_Bf
=
P_B(\nabla_Cf)
-
\mathcal S_{CB}(\nabla_Bf),
\]

where \(\mathcal S_{CB}\) is defined by

\[
\boxed{
\langle v,\mathcal S_{CB}F_B\rangle
=
E_B
\langle F_B,\nabla_Bu_{B,C,v}\rangle.
}
\]

Here

\[
A_Bu_{B,C,v}
=
\partial_vW-E_B[\partial_vW].
\]

The operator \(\mathcal S_{CB}\) already contains the conditional integration over \(B\).

It is not literally the raw pointwise response map

\[
v\mapsto\nabla_Bu_{B,C,v}.
\]

---

# 4. SH-T91 — Sweeping norm is bounded by the Witten response norm

Let

\[
\widetilde{\mathscr R}
\]

denote the stacked fiberwise Witten-response operator acting from exterior block tangent sources to internal block gradient fields.

Let

\[
\mathcal S
=
(\mathcal S_{CB})_{C\ne B}
\]

be the operator occurring in the sweeping identity.

Conditional Jensen and the fact that conditional expectation is an \(L^2\) contraction give

\[
\boxed{
\|\mathcal S\|_{\mathcal H\to\mathcal H}
\le
\|\widetilde{\mathscr R}\|_{\mathcal H\to\mathcal H}.
}
\]

Thus V1.4.9 should use

\[
\sigma:=\|\mathcal S\|
\]

for the exact heat-bath influence norm, with the computable bound

\[
\sigma\le\rho
\]

from the Witten response.

No final constant worsens.

---

# 5. SH-T92 — Audited Hilbert approximate tensorization

The averaged sweeping estimate is

\[
\|\nabla Pf\|_{\mathcal H}
\le
\frac{m-1+\sigma}{m}
\|\nabla f\|_{\mathcal H}.
\]

If

\[
\boxed{\sigma<1,}
\]

then SH-T90 gives

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

the sufficient criterion

\[
\boxed{\rho<1}
\]

and the bound

\[
\boxed{
\operatorname{Var}_\nu(f)
\le
\frac1{1-\rho}
\sum_B
E_\nu\operatorname{Var}_B(f)
}
\]

remain valid.

Thus the V1.4.9 theorem survives the audit.

---

# 6. SH-T93 — Audited stacked-response estimate

Let

\[
H=\operatorname{Hess}W,
\qquad
\|H\|_{\rm op}\le\eta<2.
\]

Relative to the block decomposition,

\[
H=H_{\rm diag}+H_{\rm off}.
\]

Pinching gives

\[
\|H_{\rm diag}\|\le\eta,
\]

and therefore

\[
\boxed{
\|H_{\rm off}\|
\le
2\eta.
}
\]

For each block,

\[
\mathscr D_B=A_B^\nabla+2I\succeq2I,
\]

so

\[
\mathscr D_B+H_{BB}
\succeq
(2-\eta)I.
\]

The block-diagonal inverse therefore has norm at most

\[
\frac1{2-\eta}.
\]

Stacking the fiberwise response rows gives

\[
\boxed{
\rho
\le
\frac{2\eta}{2-\eta}.
}
\]

Hence

\[
\boxed{
\eta<\frac23
\Longrightarrow
\rho<1.
}
\]

Together with SH-T92,

\[
\boxed{
\Delta_{\rm phys}
\ge
c(2-3\eta).
}
\]

The V1.4.9 block closure is therefore retained.

---

# 7. Frozen strong-coupling conclusion after audit

The rooted-vacuum theorem gives

\[
\beta_{\rm vac}
=
\frac3{128(e+2)}
\approx0.00496738026,
\]

and

\[
\eta(\beta)
\le
\frac3{e+2}
\left[
1-\sqrt{1-\frac{|\beta|}{\beta_{\rm vac}}}
\right].
\]

Since

\[
\frac3{e+2}<\frac23,
\]

the audited Hilbert block theorem applies for every

\[
\boxed{
|\beta|<\beta_{\rm vac}.
}
\]

The complete block lower bound is

\[
\boxed{
\frac{\Delta_{\rm phys}}c
\ge
2-
\frac9{e+2}
\left[
1-\sqrt{1-\frac{|\beta|}{\beta_{\rm vac}}}
\right].
}
\]

Its limiting sufficient boundary value is

\[
\boxed{
\frac{2e-5}{e+2}c
\approx0.092526c.
}
\]

The direct curvature lower bound remains stronger.

---

# 8. A conceptual correction: finite-volume vacuum existence does not stop at \(\beta_{\rm vac}\)

At a fixed finite lattice, define

\[
H(\beta)
=
c(K-\beta P).
\]

The configuration space \(SU(2)^E\) is compact.

The multiplication operator \(P\) is bounded.

Therefore \(H(\beta)\) is a self-adjoint analytic family with common domain and compact resolvent.

The heat semigroup of the Laplace-type operator plus real bounded potential is positivity improving on the connected configuration manifold.

Hence the ground state is unique and strictly positive for every real \(\beta\).

Gauge invariance of \(H(\beta)\) and uniqueness imply that the ground state is gauge invariant.

---

# 9. SH-T94 — Global finite-volume analytic vacuum branch

For every fixed finite regulator and every real

\[
\boxed{\beta\in\mathbb R,}
\]

the ground-state eigenvalue \(E_0(\beta)\) is simple and isolated.

Standard analytic perturbation theory therefore gives a locally real-analytic normalized eigenvector.

Because the real parameter line is connected and the positive normalized ground state fixes the sign uniquely, the local branches patch to a global real-analytic ground-state branch

\[
\boxed{
\beta\mapsto\Omega_\beta>0.
}
\]

Consequently

\[
\boxed{
W_\beta=-2\log\Omega_\beta
}
\]

exists smoothly for every real \(\beta\) at fixed finite regulator.

The finite-volume excitation gap is also strictly positive for every fixed \(\beta\), because the spectrum is discrete and the ground state is simple.

No claim of a regulator-uniform gap follows from this statement.

---

# 10. What \(\beta_{\rm vac}\) actually means

The number

\[
\boxed{
\beta_{\rm vac}
\approx0.00496738
}
\]

is not a finite-volume existence boundary.

It is the endpoint of the present **volume-uniform rooted cluster contraction proof**.

Thus the correct statement is

\[
\boxed{
\text{finite-volume vacuum exists for all real }\beta;
}
\]

but

\[
\boxed{
\text{the current uniform cluster/locality theorem is proved only for }
|\beta|<\beta_{\rm vac}.
}
\]

This distinction is permanent.

---

# 11. SH-T95 — Exact coupling-derivative Poisson equation

Normalize

\[
\nu_\beta
=
\Omega_\beta^2\,dU
=
Z_\beta^{-1}e^{-W_\beta}dU.
\]

Let

\[
S_\beta=\partial_\beta W_\beta.
\]

Normalization gives

\[
E_{\nu_\beta}S_\beta=0.
\]

Differentiating the exact vacuum equation yields

\[
\boxed{
A_\beta S_\beta
=
-2
\left(
P-\langle P\rangle_{\nu_\beta}
\right),
}
\]

where

\[
A_\beta
=
-\Delta+\nabla W_\beta\cdot\nabla.
\]

Thus the actual motion of the vacuum along the coupling axis is itself an exact Poisson problem for the physical weighted generator.

---

# 12. SH-T96 — Ground-energy concavity and plaquette susceptibility

Let

\[
\varepsilon_0(\beta)=E_0(\beta)/c.
\]

Feynman--Hellmann gives

\[
\boxed{
\varepsilon_0'(\beta)
=
-\langle P\rangle_{\nu_\beta}.
}
\]

Since

\[
A_\beta S_\beta
=
-2P_0,
\qquad
P_0=P-\langle P\rangle,
\]

we obtain

\[
\operatorname{Cov}_{\nu_\beta}(P,S_\beta)
=
-\frac12
E_{\nu_\beta}|\nabla S_\beta|^2.
\]

Therefore

\[
\boxed{
\frac{d}{d\beta}
\langle P\rangle_{\nu_\beta}
=
\frac12
E_{\nu_\beta}|\nabla S_\beta|^2
=
2\langle P_0,A_\beta^{-1}P_0\rangle
\ge0.
}
\]

Equivalently,

\[
\boxed{
\varepsilon_0''(\beta)
=
-\frac12
E_{\nu_\beta}|\nabla S_\beta|^2
\le0.
}
\]

Thus the dimensionless ground energy is concave in \(\beta\), and the plaquette sum expectation is monotone increasing.

---

# 13. SH-T97 — Uniform susceptibility-density bound in the proved strong-coupling interval

Let

\[
\gamma(\beta)
\]

be any proved lower bound for the weighted-generator gap.

Then

\[
\langle P_0,A_\beta^{-1}P_0\rangle
\le
\frac{\operatorname{Var}(P)}{\gamma}.
\]

Poincaré again gives

\[
\operatorname{Var}(P)
\le
\frac{E|\nabla P|^2}{\gamma}.
\]

Every link belongs to at most four plaquettes, and for each plaquette

\[
|\nabla_ep_p|\le1.
\]

Therefore

\[
|\nabla_eP|^2\le16,
\]

and

\[
\boxed{
E|\nabla P|^2
\le
16|E|.
}
\]

Consequently

\[
\boxed{
0
\le
\frac1{|E|}
\frac{d}{d\beta}\langle P\rangle_{\nu_\beta}
\le
\frac{32}{\gamma(\beta)^2}.
}
\]

Equivalently,

\[
\boxed{
0
\le
-\frac{\varepsilon_0''(\beta)}{|E|}
\le
\frac{32}{\gamma(\beta)^2}.
}
\]

Inside the current audited strong-coupling interval, one may use the direct curvature bound

\[
\gamma(\beta)
\ge
2-\eta(\beta).
\]

Thus the plaquette susceptibility per link is uniformly bounded independently of finite lattice volume throughout the proved interval.

---

# 14. Path-specific derivative control

The exact identity

\[
A_\beta S_\beta=-2P_0
\]

shows that coupling continuation does not intrinsically require the full inverse of every direction in the activity Banach space.

For the physical path, the relevant forcing direction is the specific extensive plaquette observable \(P\).

The full inverse remains useful for an abstract implicit-function theorem, but a sharper continuation strategy may instead control

\[
\boxed{
S_\beta
=
-2A_\beta^{-1}P_0
}
\]

directly in a local analytic norm.

This is a weaker and more physical target than bounding the entire activity-space inverse.

---

# 15. Revised frontier

The current status is now:

### Fixed finite regulator

\[
\boxed{
\Omega_\beta
\text{ exists uniquely and analytically for all real }\beta.
}
\]

### Uniform strong-coupling control

For

\[
\boxed{
|\beta|<0.00496738,
}
\]

we have

- rooted cluster construction;
- uniform Hessian control;
- direct curvature gap;
- global Hilbert response contraction;
- Hilbert approximate tensorization;
- complete block gap;
- bounded susceptibility density.

### Actual remaining problem

Extend **volume- and regulator-uniform locality and gap estimates** beyond the present cluster radius.

The next most economical target is the forcing-direction local estimate

\[
\boxed{
\|A_\beta^{-1}
(P-\langle P\rangle)\|_{\rm local\ analytic}
}
\]

rather than an unnecessarily strong bound on every direction of
\(\mathsf M_\beta^{-1}\).

---

\[
\boxed{
\text{V1.4.9 survives strict audit. The finite-volume vacuum branch exists for all coupling; the true unresolved barrier is uniform locality as the regulator grows.}
}
\]
