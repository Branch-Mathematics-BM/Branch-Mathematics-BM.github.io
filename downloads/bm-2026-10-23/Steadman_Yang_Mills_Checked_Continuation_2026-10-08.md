# Steadman model and Yang–Mills: checked continuation

**Date:** 8 October 2026  
**Project:** Branch Mathematics / GURF  
**Scope:** Complete finite-regulator realization, response-bridge audit, explicit finite-volume estimates, and the exact remaining continuum obligations.  
**Completion status:** The regulated construction and the results proved below are complete within their stated assumptions. A complete universal Steadman physical theory and the four-dimensional continuum Yang–Mills existence and mass-gap theorem are **not established**.

The frozen Branch Mathematics V1 foundation is unchanged. Efficiency remains emergent; no separate Efficiency Force is introduced. The retained conceptual statement is: **Frame responds; fibre smooths into the Response.** Its mathematical meaning must be specified in each physical branch.

## 1. What this continuation actually establishes

The October 8 endpoint proposed a Hilbert Response Bridge from conditional block responses to the spectral quantity

\[
\mathscr R(E)=
\left\|(C-E)^{-1/2}B(A-E)^{-1/2}\right\|^2.
\]

This continuation settles the proposed bridge in two parts:

1. The proposed square-sum inequality is valid for a **single receiving block**.
2. Promoting that inequality to a uniform bound for the **whole coupled system** is invalid without additional operator control. Section 6 gives a local, exactly solvable counterexample.

A valid global bridge is proved in Section 8 using the actual vacuum, the exact ground-state transform, and the global weighted operator on gradient fields. It retains the full collective coupling.

There is also a concrete construction result at arbitrary finite coupling. In the normalizations specified below, every finite lattice with a nontrivial physical excited sector satisfies

\[
\boxed{
\Delta^{SU(2)}_{\beta,\Lambda}
\ge
3c_K
\left(\frac{797}{1203}\right)^{2n_e}
e^{-4|\beta|n_p}>0
}
\tag{1}
\]

and

\[
\boxed{
\Delta^{SU(3)}_{\beta,\Lambda}
\ge
\frac{16}{3}c_K
\left(\frac{57}{68}\right)^{2n_e}
e^{-4|\beta|n_p}>0.
}
\tag{2}
\]

Here \(n_e\) and \(n_p\) are the numbers of links and plaquettes. These bounds use the true Hamiltonian and do not assume that an approximate vacuum is exact. They deteriorate with volume and therefore do not establish a continuum mass gap.

The exact remaining problem is to replace such deteriorating estimates with control along a physically normalized continuum trajectory, and to construct the corresponding nontrivial quantum field theory. No amount of relabeling a conditional estimate as a final theorem supplies those steps.

### Evidence and version handling

| Recovered material | Use in this continuation |
|---|---|
| September 20 block-Poincaré module, full text | Exact vacuum measure, conditional metrics, and the distinction between physical and auxiliary generators |
| September 21 Steadman V1.1 review, full text | Frozen conceptual constraints and previously proved conditional identities |
| September 22 response recurrence and cluster certificate, full text | Definition of the conditional Poisson response and its input/output spaces |
| September 22 V1.4 strong-coupling freeze record, full text | Retained normalization and prior strong-coupling module |
| September 23 V1.4.10-F and October 8 endpoint, recovered conversation excerpts | Continuity and the latest target; the complete V1.4.10-F proof text was not recovered |

The prior strong-coupling package is retained in its recorded scope. Its full cluster proof is not independently re-certified by this document. The proofs of (1)–(2), the counterexample, and the global bridge below do not depend on promoting an unrecovered cluster estimate.

## 2. A precise regulated realization of the Steadman description

Let \(\Lambda\) be a finite connected spatial lattice, with link set \(\mathcal E\), plaquette set \(\mathcal P\), and gauge group \(G=SU(2)\) or \(SU(3)\). Use the link configuration space

\[
X=G^{\mathcal E}
\]

with product normalized Haar measure and the product bi-invariant metric specified below. A link configuration is \(U=(U_e)_{e\in\mathcal E}\). A vertex gauge transformation acts by

\[
U_{xy}\longmapsto g_xU_{xy}g_y^{-1}.
\]

The physical Hilbert space is

\[
\mathcal H_{\rm phys}=L^2(X,dU)^{\mathcal G},
\]

the gauge-invariant subspace. This keeps boundary compatibility explicit; it does not independently quotient neighboring blocks.

Define

\[
K=-\Delta_X,\qquad
p_p(U)=\frac1N\operatorname{ReTr}(U_p),\qquad
P(U)=\sum_{p\in\mathcal P}p_p(U),
\]

and

\[
\boxed{H=c_K(K-\beta P),\qquad c_K>0,\quad \beta\in\mathbb R.}
\tag{3}
\]

An additive constant may be included without changing the gap. The coefficient \(c_K\) has units of energy; it is not the speed of light.

For SU(2), use the existing unit-three-sphere metric:

\[
K_e\text{ has eigenvalues }4j(j+1),\quad
\lambda_{\rm Haar}=3,\quad \operatorname{Ric}=2I.
\]

For the SU(3) extension, choose the same Casimir scaling: \(K_e\) is four times the conventional quadratic Casimir. An irrep with highest-weight labels \((p,q)\) has

\[
d_{p,q}=\frac{(p+1)(q+1)(p+q+2)}2,
\]

\[
\lambda_{p,q}=\frac43(p^2+q^2+pq+3p+3q).
\tag{4}
\]

Consequently its first nonzero one-link eigenvalue is \(16/3\). No SU(2) cluster constants are transferred to SU(3) by substitution.

The closed regulated equation of physical evolution, in units \(\hbar=1\), is

\[
\boxed{i\,\partial_t\Psi=H\Psi,\qquad \Psi(t)\in\mathcal H_{\rm phys}.}
\tag{5}
\]

The Hamiltonian lattice construction is standard Yang–Mills mathematics [R2]. Organizing it through Steadman terminology does not, by itself, change its predictions.

| Steadman term | Precise object in this regulated branch |
|---|---|
| Frame | Link geometry, gauge action, constraints, metric, physical inner product, and Hamiltonian |
| Response influence | The evolving field state and the effect of specified perturbations of the Hamiltonian |
| Completion fibre | The states compatible with a declared receiver output; it is task-relative |
| Smoothing | A declared reorganization or analytic smoothing operation, with its metric and retained information accounted for |
| RD | Retained distinctions, with the invariant actually used stated explicitly |
| Efficiency | A response/cost comparison within a fixed admissible task |

A completion fibre is not automatically a particle, a spatial tube, or a gauge-bundle fibre. Identifying any of these objects requires an additional mathematical map. Creating a second particle is not established by creating a second mathematical fibre.

### Exact distinction preservation in this realization

The physical propagator \(U_t=e^{-itH}\) is unitary. For normalized states,

\[
D([\psi],[\phi])=1-|\langle\psi,\phi\rangle|^2
\]

is invariant under their common evolution:

\[
D([U_t\psi],[U_t\phi])=D([\psi],[\phi]).
\tag{6}
\]

This proves preservation of this specified ray distinction. It does not prove an additive universal RD density or a conservation current for every receiver-dependent measure of information.

For a receiver \(r\), let

\[
\mathfrak C_r(y)=\{[\psi]:r([\psi])=y\}.
\]

The transported receiver \(r_t=r\circ U_{-t}\) satisfies

\[
U_t\mathfrak C_r(y)=\mathfrak C_{r_t}(y).
\tag{7}
\]

Thus complete receiver fibres are transported bijectively. A fixed subsystem receiver can still lose access to distinctions that move into correlations or other degrees of freedom.

### Actual response and efficiency

For a bounded gauge-invariant perturbing observable \(O\), replace \(H\) by \(H+J(t)O\). At \(J=0\), the state response is exactly

\[
\delta\Psi(t)
=-i\int_0^t
U_{t-s}O\,U_s\Psi(0)\,\delta J(s)\,ds.
\tag{8}
\]

This gives a defined response, with a declared source and observable. A static inverse operator used later is not a claim of instantaneous signal propagation.

The retained efficiency definition is

\[
\eta_R=\frac{R_{\rm useful}}{R_{\rm ideal}},\qquad
R_{\rm ideal}>0,
\]

where the ideal is the maximum under the same constraints and metric. It is then a dimensionless accounting quantity in \([0,1]\). It supplies no extra force term in (3).

The measure used below is a positive Hilbert-space weight. These calculations do not require probability to be a primitive physical ontology.

## 3. Finite-regulator existence and the exact physical bridge

**Theorem 1.** For every finite lattice and every finite real \(\beta\), (3) is self-adjoint on the domain of \(K\), bounded below, and has compact resolvent. Its ground state is unique and can be chosen smooth and strictly positive. That ground state is gauge invariant.

**Proof.** \(X\) is compact and connected. The Laplace operator has compact resolvent. The smooth real potential \(-c_K\beta P\) is bounded, so bounded perturbation preserves self-adjointness, lower boundedness, and compact resolvent. The heat kernel on connected \(X\) is strictly positive; bounded-potential semigroup domination, or its Trotter-product construction, gives a positivity-improving Schrödinger semigroup. The lowest eigenvalue is therefore simple with a positive eigenfunction. Elliptic regularity makes it smooth. Gauge transformations commute with \(H\) and preserve positivity and normalization, so uniqueness makes the normalized positive ground state gauge invariant. \(\square\)

Write this state as \(\Omega>0\), with \(\|\Omega\|_2=1\), and its eigenvalue as \(E_0\). Define

\[
W=-2\log\Omega,\qquad d\nu=\Omega^2dU,
\]

\[
\mathcal A=-\Delta_X+\nabla W\cdot\nabla.
\]

Multiplication \(\mathcal U f=\Omega f\) is unitary from \(L^2(\nu)\) to \(L^2(dU)\). Direct differentiation proves

\[
\boxed{\mathcal U^{-1}(H-E_0)\mathcal U=c_K\mathcal A.}
\tag{9}
\]

On a smooth core, integration by parts gives

\[
\langle f,\mathcal Af\rangle_\nu
=\int|\nabla f|^2\,d\nu.
\]

Closing the forms yields the exact physical gap identity

\[
\boxed{
\Delta_{\rm phys}
=c_K
\inf_{\substack{f\ {\rm gauge\ invariant}\\
f\ne0,\;\int f\,d\nu=0}}
\frac{\int|\nabla f|^2\,d\nu}
{\int|f|^2\,d\nu}.
}
\tag{10}
\]

This resolves the Hamiltonian identification at the regulated level **when \(W\) is obtained from the actual ground state of (3)**. Substituting an arbitrary Wilson Gibbs density or a convenient guessed \(W\) does not preserve (9).

The equivalent vacuum equation is

\[
\frac12\Delta W-\frac14|\nabla W|^2-\beta P
=\frac{E_0}{c_K}.
\tag{11}
\]

The auxiliary smoothing \(e^{-\tau\mathcal A}\) is related to imaginary-time evolution by (9). It is not the physical propagator in (5). For every finite \(\tau>0\) it is injective, but its inverse is unbounded on the full infinite-dimensional Hilbert space. Keeping finite link coordinates does not make the representation space finite-dimensional.

## 4. Explicit finite-volume bounds at all finite couplings

The following argument constructs a gap estimate without knowing \(\Omega\) explicitly.

Let \(k_\tau(x,y)\) be the one-link heat kernel, normalized relative to Haar measure. Suppose

\[
0<a_\tau\le k_\tau(x,y)\le b_\tau.
\]

The product heat kernel on \(n_e\) links is bounded between \(a_\tau^{n_e}\) and \(b_\tau^{n_e}\). Set \(\widehat V=-\beta P\). Positivity and the Trotter product give, for \(f\ge0\),

\[
e^{-\tau\sup\widehat V}e^{-\tau K}f
\le e^{-\tau(K+\widehat V)}f
\le e^{-\tau\inf\widehat V}e^{-\tau K}f.
\tag{12}
\]

Apply (12) to \(\Omega\), use its eigenfunction equation, and compare the maximum and minimum over \(X\). The common integral of \(\Omega\) and the eigenvalue factor cancel:

\[
\frac{\max\Omega}{\min\Omega}
\le e^{\tau\,\operatorname{osc}\widehat V}
\left(\frac{b_\tau}{a_\tau}\right)^{n_e}.
\tag{13}
\]

Because \(|p_p|\le1\),

\[
\operatorname{osc}\widehat V\le2|\beta|n_p.
\tag{14}
\]

For completeness, if \(\rho=\Omega^2\), normalized Haar Poincaré and minimization over constants give

\[
\begin{aligned}
\operatorname{Var}_\nu(f)
&\le \rho_{\max}
\int|f-\textstyle\int f\,dU|^2dU\\
&\le\frac{\rho_{\max}}{\lambda_{\rm Haar}}
\int|\nabla f|^2dU\\
&\le\frac{\rho_{\max}}
{\lambda_{\rm Haar}\rho_{\min}}
\int|\nabla f|^2d\nu.
\end{aligned}
\tag{15}
\]

The product Haar gap equals the one-link gap. Combining (10), (13), and (15) proves

\[
\boxed{
\Delta_{\rm phys}
\ge c_K\lambda_{\rm Haar}
e^{-4\tau|\beta|n_p}
\left(\frac{a_\tau}{b_\tau}\right)^{2n_e}.
}
\tag{16}
\]

The all-functions inequality restricts to the gauge-invariant subspace. No independent gauge quotient of conditional blocks is used.

### SU(2) constants

At \(\tau=1\), character expansion and \(|\chi_n|\le n+1\) imply

\[
|k_1-1|
\le\delta_2
=\sum_{n\ge1}(n+1)^2e^{-n(n+2)}.
\]

The terms from \(n=3\) onward have consecutive ratio at most
\((25/16)e^{-9}\). Therefore

\[
\delta_2
\le4e^{-3}+9e^{-8}
+\frac{16e^{-15}}{1-(25/16)e^{-9}}
<0.203.
\tag{17}
\]

Take \(a_1=0.797\), \(b_1=1.203\), and \(\lambda_{\rm Haar}=3\). Equation (16) becomes (1).

### SU(3) constants

Using (4),

\[
|k_1-1|
\le\delta_3
=\sum_{(p,q)\ne(0,0)}
d_{p,q}^2e^{-\lambda_{p,q}}.
\]

Group the terms by \(s=p+q\). Since \(pq\le s^2/4\),

\[
\lambda_{p,q}\ge s^2+4s,\qquad
d_{p,q}\le\frac{(s+2)^3}{8}.
\]

There are \(s+1\) terms for each \(s\). The exact \(s=1,2\) contribution is

\[
18e^{-16/3}+72e^{-40/3}+64e^{-12}.
\]

For \(s\ge3\), bound the group by

\[
a_s=\frac{(s+1)(s+2)^6}{64}e^{-s^2-4s}.
\]

Its consecutive ratio is at most
\(r_3=(5/4)(6/5)^6e^{-11}<1\). Hence

\[
\delta_3
\le18e^{-16/3}+72e^{-40/3}+64e^{-12}
+\frac{(4\cdot5^6/64)e^{-21}}{1-r_3}
<0.088.
\tag{18}
\]

Take \(a_1=0.912\), \(b_1=1.088\), and
\(\lambda_{\rm Haar}=16/3\). Their ratio is \(57/68\), proving (2).

These are rigorous finite-volume estimates. The numerical evaluation of (17)–(18) checks the displayed rounded constants; the tail estimates supply the infinite-sum control.

## 5. The single-block Hilbert Response Bridge

Fix a block \(B\) and an exterior configuration \(\eta\). Let

\[
d\nu_B^\eta
=Z_B(\eta)^{-1}e^{-W(U_B,\eta)}dU_B,
\]

\[
\mathcal A_B^\eta
=-\Delta_B+\nabla_BW\cdot\nabla_B.
\]

For a tangent input \(v_C\) in an exterior block \(C\), define

\[
s_{BC}^{\eta,v_C}
=\partial_{v_C}W-\nu_B^\eta(\partial_{v_C}W),
\]

\[
\mathcal A_B^\eta u_{BC}^{\eta,v_C}
=s_{BC}^{\eta,v_C},\qquad
\nu_B^\eta(u_{BC}^{\eta,v_C})=0,
\]

\[
T_{BC}^\eta v_C=\nabla_Bu_{BC}^{\eta,v_C}.
\tag{19}
\]

The finite-regulator conditional gap makes this inverse well defined. The target is
\(\mathcal K_B^\eta=L^2(\nu_B^\eta;T_BX)\), with the physical gradient metric.

Form the exterior input direct sum

\[
\mathcal V_{B^c}^\eta=\bigoplus_{C\ne B}T_{\eta_C}X_C
\]

and the row operator

\[
\mathbb T_B^\eta(v_C)_C
=\sum_{C\ne B}T_{BC}^\eta v_C.
\]

**Theorem 2.**

\[
\boxed{
\|\mathbb T_B^\eta\|^2
\le\sum_{C\ne B}\|T_{BC}^\eta\|^2.
}
\tag{20}
\]

**Proof.** Its adjoint is the column
\((T_{BC}^{\eta *})_C\). Therefore

\[
\mathbb T_B^\eta\mathbb T_B^{\eta *}
=\sum_{C\ne B}T_{BC}^\eta T_{BC}^{\eta *}.
\]

Taking operator norms and applying the triangle inequality proves (20). For infinitely many blocks, square summability gives the bounded extension. \(\square\)

The outputs of the separate \(T_{BC}^\eta\) need not be orthogonal. The direct-sum **input** is sufficient for this row bound.

If

\[
\|T_{BC}^\eta\|\le q_\mu e^{-\mu d(B,C)},
\]

then

\[
\|\mathbb T_B^\eta\|^2
\le q_\mu^2G_{\rm geom}(2\mu),\qquad
G_{\rm geom}(s)=\sup_B\sum_{C\ne B}e^{-s d(B,C)}.
\tag{21}
\]

With the retained conditional estimate
\(q_\mu=h_\mu/(2-h_\mu)\), this proves the proposed
\(G_{\rm geom}(2\mu)[h_\mu/(2-h_\mu)]^2\) estimate **at the single-row level**.

The shell count must match the actual graph and metric. If one has separately proved \(a_n=10n^2+2\), then

\[
G(s)=\frac{2e^{-s}(6+3e^{-s}+e^{-2s})}{(1-e^{-s})^3}.
\]

That formula is not a substitute for checking the geometry of a particular block partition.

Equation (20) is not an estimate for the norm of the assembled operator with every receiving block present. The next section proves the distinction is essential.

## 6. A local counterexample to the proposed global promotion

Take an even periodic chain of \(N\ge6\) real variables. Let \(S_N\) be its cyclic shift matrix and choose

\[
0<\varepsilon<1,\qquad
q=\frac{1-\varepsilon}{2},
\]

\[
M_\varepsilon=I-q(S_N+S_N^*),\qquad
W(x)=\frac12x^TM_\varepsilon x.
\tag{22}
\]

The Fourier eigenvalues are

\[
\lambda_k
=1-(1-\varepsilon)\cos(2\pi k/N),
\]

so \(\lambda_{\min}(M_\varepsilon)=\varepsilon\). The weight
\(d\nu\propto e^{-W}dx\) is well defined.

Condition on every coordinate except \(x_i\). Its conditional weight has unit precision and mean

\[
m_i=q(x_{i-1}+x_{i+1}).
\]

Thus every one-site conditional gradient gap is exactly **1**. The centered score for either neighboring input is
\(-q(x_i-m_i)\). Solving (19) gives a constant gradient response \(-q\). All other responses vanish.

Consequently

\[
\boxed{
\sum_{j\ne i}\|T_{ij}\|^2=2q^2
=\frac{(1-\varepsilon)^2}{2}<\frac12
}
\tag{23}
\]

uniformly over every site and every exterior configuration.

But the full generator is

\[
\mathcal A=-\Delta+(M_\varepsilon x)\cdot\nabla,
\]

and its gap is exactly \(\varepsilon\). Diagonalizing \(M_\varepsilon\) gives independent one-dimensional generators whose positive eigenvalues are integer multiples of its eigenvalues. Alternatively the collective linear function
\(f(x)=N^{-1/2}\sum_i x_i\) satisfies \(\mathcal Af=\varepsilon f\), and the Gaussian Poincaré inequality gives the matching lower bound.

This has an exact physical Schrödinger realization:

\[
H=-\Delta+\frac14|M_\varepsilon x|^2
-\frac12\operatorname{tr}M_\varepsilon,\qquad
\Omega\propto e^{-x^TM_\varepsilon x/4}.
\tag{24}
\]

Its unique ground energy is zero and its gap is also \(\varepsilon\).

Taking \(\varepsilon=N^{-2}\) produces arbitrarily small global gaps while local gaps stay at 1 and the row-square bound stays below \(1/2\). Even fixed \(N\) and \(\varepsilon\downarrow0\) rule out any universal positive lower bound inferred only from those local numbers.

| \(N\) | Local gap | Single-row norm squared | Exact global gap |
|---:|---:|---:|---:|
| 8 | 1 | 0.4844970703 | 0.015625 |
| 32 | 1 | 0.4990239143 | 0.0009765625 |
| 128 | 1 | 0.4999389667 | 0.00006103515625 |
| 256 | 1 | 0.4999847413 | 0.0000152587890625 |

The full influence matrix has norm \(2q=1-\varepsilon\). Its square approaches 1, not \(1/2\). On the invariant constant-vector part of the corresponding one-form operator, split sites into even and odd sets. Its diagonal blocks are \(I\), its cross block has norm \(2q\), and the actual Feshbach quantity at zero is

\[
\mathscr R(0)=(1-\varepsilon)^2.
\tag{25}
\]

The missing collective mode is therefore detected by the true spectral response.

This counterexample disproves the unrestricted local-to-global inference. It does not disprove a Yang–Mills mass gap. A Yang–Mills-specific improvement would need an extra property proved for its actual vacuum.

## 7. The exact spectral response theorem

Let \(\mathcal H_1\oplus\mathcal H_2\) carry a self-adjoint operator specified by the closed block form

\[
\mathsf H=
\begin{pmatrix}A&B^*\\B&C\end{pmatrix}.
\]

If this is the original physical Hamiltonian shifted by \(E_0\), work on its excited sector; otherwise the vacuum makes any strictly positive full-space lower bound impossible.

For a proposed energy \(E\), assume

\[
A_E=A-E\ge\alpha_E I>0,\qquad
C_E=C-E\ge\gamma_E I>0,
\]

and that the normalized cross form defines a bounded operator

\[
T_E=C_E^{-1/2}BA_E^{-1/2},\qquad
r_E=\|T_E\|^2.
\tag{26}
\]

These domain and boundedness assumptions are part of the theorem, not consequences of naming the blocks.

**Theorem 3.** If \(r_E<1\), then

\[
\boxed{
\mathsf H\ge
\left[E+(1-\sqrt{r_E})\min(\alpha_E,\gamma_E)\right]I.
}
\tag{27}
\]

The normalized Schur complement on the first sector is

\[
A_E-B^*C_E^{-1}B
=A_E^{1/2}(I-T_E^*T_E)A_E^{1/2}
\ge(1-r_E)A_E.
\tag{28}
\]

**Proof.** Put \(u=A_E^{1/2}x\), \(v=C_E^{1/2}y\). The full quadratic form is

\[
\|u\|^2+\|v\|^2+
2\operatorname{Re}\langle v,T_Eu\rangle.
\]

It is at least
\((1-\|T_E\|)(\|u\|^2+\|v\|^2)\), proving (27). Completing the square in \(y\) proves (28). These computations hold on the form core and extend by closure. \(\square\)

The factor \(1-r_E\) controls the **Schur complement**; the displayed bound for the **full form** uses \(1-\sqrt{r_E}\). A claim transferring the former factor directly to the full Hilbert-space norm requires further norm control on the elimination map.

This is standard Schur/Feshbach mathematics, with a proof included here; no novelty claim is made [R3].

### Where a square-sum spectral bound really is valid

Let \(\Pi_j\) be orthogonal projections resolving the **target of the fully normalized** \(T_E\). Then

\[
W_j=\Pi_jT_E,\qquad
T_E^*T_E=\sum_jW_j^*W_j,
\]

\[
\boxed{r_E\le\sum_j\|W_j\|^2.}
\tag{29}
\]

The square-sum step is sound. The important point is the operator being split:

\[
W_j=\Pi_j(C-E)^{-1/2}B(A-E)^{-1/2}.
\]

Replacing these terms by unnormalized shell couplings, separate conditional responses, or a diagonal approximation to \(C\) is an additional claim. The full resolvent already contains the internal mixing. No independent fundamental coherence factor is introduced.

## 8. A valid global Hilbert Response Bridge

There are two valid routes. They use different hypotheses and should not be conflated.

### 8.1 The conditional metric route

For a 1-Lipschitz test \(\phi\) of block \(B\), differentiation of its conditional average gives

\[
\partial_v\nu_B^\eta(\phi)
=-\langle\phi,s_{BC}^{\eta,v}\rangle_{\nu_B^\eta}
=-\langle\nabla_B\phi,T_{BC}^\eta v\rangle_{\nu_B^\eta}.
\]

Hence its magnitude is at most \(\|T_{BC}^\eta v\|\). Integrating along exterior geodesics and using Wasserstein duality bounds the metric influence coefficient by

\[
Q_{BC}=\sup_\eta\|T_{BC}^\eta\|,\qquad Q_{BB}=0.
\]

For disjoint compact product blocks with conditional scalar Poincaré gaps at least \(\lambda_{\rm loc}>0\), the established Dobrushin variance-factorization theorem gives

\[
\boxed{
\Delta_{\rm phys}\ge
c_K\lambda_{\rm loc}(1-\rho(Q)),
\qquad \rho(Q)<1.
}
\tag{30}
\]

A sufficient, computable condition is
\(\sup_Bw_B^{-1}\sum_CQ_{BC}w_C\le\theta<1\).
The theorem and its metric hypotheses are those of Wu [R4]. Compactness supplies the required finite moments. The square-sum row bound cannot replace this global influence condition.

### 8.2 The global gradient-field route

Let \(\mathcal A\) be the exact operator in (9). Its weighted operator on one-forms is

\[
\mathcal L^{(1)}
=\mathcal A^\nabla+\operatorname{Ric}+\operatorname{Hess}W,
\tag{31}
\]

where \(\mathcal A^\nabla\) is the nonnegative weighted covariant-gradient operator. The weighted Bochner identity gives

\[
d\mathcal A=\mathcal L^{(1)}d.
\tag{32}
\]

For each nonconstant eigenfunction \(\mathcal Af=\lambda f\),
\(df\ne0\) and \(\mathcal L^{(1)}df=\lambda df\). Equivalently,
\(d\mathcal A^{-1/2}\) is an isometry from centered scalar functions onto the closed exact-gradient subspace and intertwines the operators there.

Therefore

\[
\boxed{
\mathcal L^{(1)}\ge mI
\quad\Longrightarrow\quad
\Delta_{\rm phys}\ge c_Km.
}
\tag{33}
\]

A lower bound on all one-forms is sufficient; it can be stronger than necessary. Gauge-invariant scalar functions map to their corresponding exact-gradient subspace. No physical excitations are added by using a sufficient all-forms estimate.

Partition the link tangent components into disjoint blocks. All components now live over the **same global weight \(\nu\)**. Let
\(\mathcal D_B=P_B\mathcal L^{(1)}P_B\).
The cross block is the mixed Hessian:

\[
P_B\mathcal L^{(1)}P_C
=\operatorname{Hess}_{BC}W,\quad B\ne C.
\tag{34}
\]

Suppose each conditional vector-field form obeys

\[
\mathcal A_B^{\nabla,\eta}
+\operatorname{Ric}_B+\operatorname{Hess}_{BB}W
\ge\kappa_B I>0
\tag{35}
\]

for **all** block vector fields, uniformly in \(\eta\). The global diagonal block also includes nonnegative covariant derivatives in exterior coordinates. Integrating (35) therefore gives
\(\mathcal D_B\ge\kappa_B I\).

Define

\[
k_{BC}=\sup_U\|\operatorname{Hess}_{BC}W(U)\|_{\rm op},
\]

\[
M_{BC}=
\frac{k_{BC}}{\sqrt{\kappa_B\kappa_C}},
\qquad M_{BB}=0.
\tag{36}
\]

The scalar matrix \(M\) is symmetric and nonnegative. Assume positive weights satisfy

\[
\sup_B\frac{\sum_CM_{BC}w_C}{w_B}\le\theta<1.
\tag{37}
\]

**Theorem 4.**

\[
\boxed{
\Delta_{\rm phys}
\ge c_K\bigl(\min_B\kappa_B\bigr)(1-\theta).
}
\tag{38}
\]

**Proof.** For a global vector field \(v=(v_B)\), set
\(z_B=\sqrt{\langle v_B,\mathcal D_Bv_B\rangle_\nu}\).
Then \(\|v_B\|\le z_B/\sqrt{\kappa_B}\), so the magnitude of each cross term is at most \(M_{BC}z_Bz_C\). A nonnegative symmetric \(M\) satisfying (37) has \(\|M\|_2=\rho(M)\le\theta\). Consequently

\[
\begin{aligned}
\langle v,\mathcal L^{(1)}v\rangle
&\ge\sum_Bz_B^2-\sum_{B\ne C}M_{BC}z_Bz_C\\
&\ge(1-\theta)\sum_Bz_B^2\\
&\ge(1-\theta)\min_B\kappa_B\,\|v\|^2.
\end{aligned}
\]

Apply (33). \(\square\)

A conditional **scalar** gap alone does not automatically supply (35) on all vector fields. One may instead use a pointwise curvature lower bound to prove (35). For example, in the SU(2) normalization, a global Hessian lower bound \(\operatorname{Hess}W\ge-hI\), \(h<2\), immediately gives
\(\Delta_{\rm phys}\ge c_K(2-h)\), recovering the direct-curvature mechanism in the retained strong-coupling module.

### Why the conditional and spectral responses are not identical

Differentiating (19) gives the conditional equation

\[
\left(\mathcal A_B^{\nabla,\eta}
+\operatorname{Ric}_B+\operatorname{Hess}_{BB}W\right)
T_{BC}^\eta v
=\operatorname{Hess}_{BC}W\,v.
\tag{39}
\]

This involves a full inverse on the receiving block and boundary inputs fixed in the interior coordinates. By contrast, the spectral operator in (26) has inverse square roots on **both** sides, acts on global Hilbert spaces, and includes the complete eliminated-sector dynamics.

Equation (39), the Bochner identity, and the estimates (35)–(38) provide a justified bridge. Simply setting \(T_{BC}^\eta=(C-E)^{-1/2}B(A-E)^{-1/2}\) is not justified.

## 9. Continuation in coupling and certified approximate vacua

### An exact continuation equation

At fixed finite regulator, the simple ground state is locally real analytic in \(\beta\). Hold \(c_K\) fixed when differentiating the dimensionless problem, and put

\[
e_\beta=E_0/c_K,\qquad
S_\beta=\partial_\beta W_\beta,\qquad
P_0=P-\nu_\beta(P).
\]

Differentiating (11), and using normalization, gives

\[
\boxed{
\mathcal A_\beta S_\beta=-2P_0,\qquad
\nu_\beta(S_\beta)=0.
}
\tag{40}
\]

The energy identities are

\[
e_\beta'=-\nu_\beta(P),
\]

\[
\boxed{
e_\beta''=-2\langle P_0,\mathcal A_\beta^{-1}P_0\rangle_{\nu_\beta}
\le0.
}
\tag{41}
\]

These are exact finite-regulator susceptibility relations. They do not supply a volume-uniform bound on \(S_\beta\) or its Hessian. An estimate using
\(\|\mathcal A_\beta^{-1}\|\le1/\lambda_\beta\)
is conditional on a lower bound for the very gap being continued.

Thus the finite-volume analytic continuation closes; uniform control of its locality and response margin remains a separate estimate.

### A residual certificate that does not confuse trial values with lower bounds

Let \(\widetilde W\) be any smooth real gauge-invariant trial function and define

\[
H_0=K+\frac14|\nabla\widetilde W|^2
-\frac12\Delta\widetilde W.
\]

Its exact positive ground state is proportional to \(e^{-\widetilde W/2}\), with ground energy zero. Suppose a gap \(\gamma>0\) for \(H_0\) has been independently proved.

Define the residual multiplication operator

\[
\mathcal R
=-\beta P-\frac14|\nabla\widetilde W|^2
+\frac12\Delta\widetilde W.
\tag{42}
\]

Then \(H/c_K=H_0+\mathcal R\). The min–max principle gives

\[
E_1(H/c_K)\ge\gamma+\inf\mathcal R,\qquad
E_0(H/c_K)\le\sup\mathcal R.
\]

Therefore

\[
\boxed{
\Delta_{\rm phys}\ge c_K\left(\gamma-\operatorname{osc}\mathcal R\right)
}
\tag{43}
\]

whenever the right side is positive, using the corresponding physical-sector gap for \(H_0\) or a sufficient all-functions gap.

This is a genuine lower-bound certificate. A finite matrix of trial states by itself supplies Ritz upper bounds, not the missing lower bound. In an extensive lattice, a global residual can grow with volume; a continuum application must control that growth or replace it by a justified local form estimate.

## 10. Scale, regulator, and continuum passage

Let \(a\) be the spatial lattice spacing and \(L\) the physical box size. The finite lattice depends on both. Fix the physical energy normalization before taking any limit.

For the valid block route, the sufficient target is

\[
\boxed{
m_*=
\liminf_{\substack{a\to0\\L\to\infty}}
c_K(a,L)\lambda_{\rm loc}(a,L)
\bigl[1-\theta(a,L)\bigr]>0.
}
\tag{44}
\]

For (38), replace \(\lambda_{\rm loc}\) by \(\min_B\kappa_B\) and use its corresponding \(\theta\). The liminf is along a specified, physically matched trajectory, including its gauge coupling and regulator conventions.

It is the product in physical energy units that must remain positive. Requiring each factor separately to have a uniform positive lower bound can be unnecessarily strong. Conversely, positivity at each fixed \(a,L\) says nothing by itself about the liminf.

For the Schur route, one can target
\(E_{a,L}=m_*/c_K(a,L)\) in the dimensionless operator, and prove the hypotheses of Section 7 at that energy uniformly enough to obtain the desired physical bound.

In conventional Hamiltonian lattice normalization in three spatial dimensions, the electric coefficient is proportional to \(g^2/a\), and the magnetic/electric ratio is proportional to \(g^{-4}\). Consequently, a small interval in the present \(\beta\) is the electric strong-coupling regime. It does not cover the weak-bare-coupling continuum trajectory merely because every finite-volume vacuum can be analytically continued. Exact numerical conversions depend on the fixed trace, metric, and plaquette-counting conventions.

Equations (1)–(2) contain factors exponentially small in link count and plaquette count. They do not provide (44).

### A precise gap-transfer theorem

**Theorem 5.** Suppose nonnegative Hamiltonians \(\widehat H_n\) have already been identified on a common Hilbert space, converge in strong resolvent sense to a self-adjoint \(\widehat H\), and have normalized vacuum vectors \(\Omega_n\to\Omega\) in norm. Suppose

\[
\widehat H_n\Omega_n=0,\qquad
\widehat H_n\ge m(I-P_n),\qquad
P_n=|\Omega_n\rangle\langle\Omega_n|,\quad m>0.
\tag{45}
\]

Then, with \(P=|\Omega\rangle\langle\Omega|\),

\[
\widehat H\Omega=0,\qquad
\boxed{\widehat H\ge m(I-P).}
\tag{46}
\]

**Proof.** Strong resolvent convergence of nonnegative self-adjoint operators implies strong convergence of their heat semigroups. Since \(P_n\to P\) strongly, the bounds

\[
\|e^{-t\widehat H_n}(I-P_n)v\|
\le e^{-mt}\|(I-P_n)v\|
\]

pass to the limit for every vector. The vacuum identity passes to the limit as well. The spectral theorem then gives (46). \(\square\)

The analogous argument can be formulated through convergent reconstructed correlation functions when the Hilbert spaces vary. Either way, the convergence and reconstruction are hypotheses to prove, not consequences of having named a continuum.

### Construction obligations

The official problem requires a nontrivial four-dimensional quantum Yang–Mills theory with a positive mass gap for compact simple gauge groups [R1]. A lattice bound is only one part of that task.

| Obligation | What is required | Status here |
|---|---|---|
| Physical response strength | Control of the actual vacuum response, including collective modes | Exact identities and sufficient criteria proved; continuum-uniform estimate absent |
| Scaling | Matched coupling, energy units, observables, and regulator trajectory | Target specified; trajectory estimates absent |
| Infinite volume | Limits with appropriate locality and vacuum structure | Not constructed here |
| Continuum | Convergent renormalized gauge-invariant observables with sufficient regularity | Not constructed here |
| Reconstruction | Reflection positivity and the remaining Euclidean axioms, or an equally strong direct relativistic construction | Not established by the finite Hamiltonian argument |
| Nontriviality | Surviving, nonzero physical observables/excitations in the limit | Not established by finite-volume positivity |
| Positive limiting gap | A bound such as (44), passed through a justified limit | Not proved |
| Gauge-group scope | Appropriate argument for the required groups, with group-dependent constants | Finite SU(2)/SU(3) results; no general continuum theorem |

The existing mathematical identities do not eliminate these obligations. They identify exactly where a further estimate must enter.

## 11. What is and is not complete in the physical model

The regulated Yang–Mills realization (3)–(5) is a defined dynamical model. Its existence, exact vacuum transform, and finite-volume gap estimates are established above.

The wider Steadman description is not yet a uniquely specified new physical dynamics. Its latest retained concepts organize a frame and an embedded response field, with smoothing understood through native dynamics and efficiency emergent. Earlier proposed collapse coefficients, halo behavior, or fibre Lagrangians cannot be promoted to universal equations solely because they appeared in exploratory discussion.

There is a mathematical reason this underdetermination matters. On the same Hilbert space
\(\mathbb C\Omega\oplus L^2((0,\infty),d\lambda)\), consider two self-adjoint Hamiltonians with the same unique vacuum \(\Omega\):

\[
H_{\rm gap}(z,f)=(0,(1+\lambda)f(\lambda)),
\]

\[
H_{\rm soft}(z,f)=(0,\lambda f(\lambda)).
\]

Both generate unitary distinction-preserving dynamics and injective analytic smoothing semigroups; for positive smoothing parameter, the images lie in the domain of every power of the respective Hamiltonian. The first has gap 1; the second has gap 0. Thus the qualitative RD/smoothing rules do not determine the spectrum. The local counterexample in Section 6 supplies a stronger version directly in a conditional-response setting.

For other physical sectors, the following distinctions remain necessary:

- A response can carry energy and momentum without having positive invariant rest mass. The presence of a response is not itself a mass-generation theorem.
- Information accounting and an elapsed-time variable do not supply the energy, charges, or interaction law needed for matter creation.
- A task completion fibre has no automatic causal trajectory. A physical carrier model must specify one.
- The recovered horizon restriction remains a proposed physical rule in its own branch; neither a Hawking-radiation derivation nor a gravity constitutive law follows from the Yang–Mills estimates here.

These statements leave the frozen core intact. They prevent a formal mathematical carrier from silently acquiring physical properties that have not been derived.

## 12. Result ledger

| Result | Mathematical status |
|---|---|
| Complete regulated Hamiltonian and physical evolution | Established in the stated branch |
| Unitary preservation of the specified distinction and receiver-fibre transport | Proved |
| Exact ground-state transform of the actual regulated Hamiltonian | Proved |
| All-finite-coupling finite-volume SU(2) and SU(3) positive gap bounds | Proved, with explicit constants |
| Single-block Hilbert square-sum inequality | Proved |
| Square-sum row bound as a sufficient global gap criterion | False in general; explicit local counterexample |
| Exact Schur/Feshbach response criterion with form domains and energy floors | Proved under the stated hypotheses |
| Global gradient-field response bridge | Proved under its coercivity and mixed-Hessian bounds |
| Finite-regulator coupling susceptibility and residual certificates | Proved |
| Gap passage under constructed strong resolvent and vacuum convergence | Proved as a conditional transfer theorem |
| Regulator-uniform Yang–Mills response estimate on the continuum trajectory | Open |
| Nontrivial four-dimensional continuum construction and mass gap | Not established |
| Universal new Steadman physical law | Not established |

**The work has reached a complete finite-regulator mathematical realization and a corrected global proof route. The full requested continuum and universal-physics completion cannot be claimed from these results. No further routine user input is needed to identify the remaining mathematical problem.**

## 13. Verification and provenance

The analytic arguments above supply the proofs. A deterministic calculation checks:

- the exact collective-mode counterexample at four lattice sizes;
- the distinction between single-row and full Feshbach response;
- completion of squares for a nonscalar block matrix;
- the certified heat-kernel constants for SU(2) and SU(3);
- the archived shell generating function under its stated shell counts.

The calculations passed. The rounded heat-kernel bounds were additionally checked with exact rational arithmetic: the reciprocal of a positive degree-100 Taylor sum for \(e^x\) bounds \(e^{-x}\) from above. These checks certify the stated \(0.203\) and \(0.088\) constants. They do not constitute a numerical proof of continuum Yang–Mills.

### Primary references

- **[R1]** A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official problem statement. [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf). The current [Clay problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) was also checked.
- **[R2]** J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Physical Review D 11, 395 (1975). [Publisher record](https://link.aps.org/doi/10.1103/PhysRevD.11.395).
- **[R3]** G. Dusson, I. M. Sigal, and B. Stamm, *The Feshbach–Schur map and perturbation theory* (2021). [arXiv:2105.02058](https://arxiv.org/abs/2105.02058).
- **[R4]** L. Wu, *Poincaré and transportation inequalities for Gibbs measures under the Dobrushin uniqueness condition*, Annals of Probability 34 (2006). [Primary paper](https://arxiv.org/pdf/math/0611635), Theorems 2.1–2.2.
- **[R5]** H. Shen, R. Zhu, and X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*. [arXiv:2204.12737](https://arxiv.org/abs/2204.12737). This is relevant strong-coupling literature; its auxiliary stochastic generator is not substituted for the physical Hamiltonian here.

### Project manuscripts consulted

- BM_Steadman_Yang_Mills_Block_Poincare_Module_2026-09-20.md
- Steadman_Hypothesis_V1_1_Strict_Review_Freeze_2026-09-21(1).md
- BM_Steadman_Yang_Mills_V1_4_Response_Recurrence_and_Cluster_Certificate_2026-09-22.md
- Steadman_Yang_Mills_V1_4_Uniform_Strong_Coupling_Theorem_Freeze_2026-09-22(1).md

These manuscripts and the recovered October 8 conversation target supply the project-specific definitions. External references provide standard mathematical context. No novelty, peer review, Clay acceptance, or solution status is inferred from a project freeze label.


## Appendix A. Reproducible deterministic verification

Run the following Python script with NumPy installed. The displayed numerical examples are supplementary to the analytic proofs.

```python
"""Deterministic arithmetic checks for the 2026-10-08 response continuation.

These checks validate examples and constants, not a continuum Yang--Mills proof.
Only NumPy and the Python standard library are required.
"""
import json
import math
from fractions import Fraction
import numpy as np


def spd_power(a, exponent):
    values, vectors = np.linalg.eigh(a)
    assert values.min() > 0
    return (vectors * values**exponent) @ vectors.T


rows = []
for n in (8, 32, 128, 256):
    eps = 1.0 / n**2
    q = (1.0 - eps) / 2.0
    shift = np.roll(np.eye(n), 1, axis=1)
    influence = q * (shift + shift.T)
    precision = np.eye(n) - influence
    gap = float(np.linalg.eigvalsh(precision)[0])
    assert abs(gap - eps) < 3e-14
    even, odd = np.arange(0, n, 2), np.arange(1, n, 2)
    cross = precision[np.ix_(odd, even)]
    r0 = float(np.linalg.norm(cross, ord=2)**2)
    assert abs(r0 - (1.0 - eps)**2) < 2e-14
    row_square = 2*q*q
    assert row_square < 0.5
    rows.append({"sites": n, "local_gap": 1.0,
                 "single_row_norm_squared": row_square,
                 "global_feshbach_response_at_zero": r0,
                 "exact_gap": eps, "computed_gap": gap})

# Exact completion-of-squares identity for a nonscalar block matrix.
a = np.array([[3.0, 0.2], [0.2, 2.0]])
c = np.array([[4.0, 0.1], [0.1, 2.5]])
b = np.array([[0.4, -0.2], [0.1, 0.5]])
energy = 0.3
ae, ce = a-energy*np.eye(2), c-energy*np.eye(2)
normalized = spd_power(ce, -0.5) @ b @ spd_power(ae, -0.5)
r = float(np.linalg.norm(normalized, 2)**2)
h = np.block([[a, b.T], [b, c]])
x = np.array([0.3, -0.8])
y = np.array([0.5, 0.2])
z = np.concatenate((x, y))
lhs = z @ (h-energy*np.eye(4)) @ z
effective = ae - b.T @ np.linalg.solve(ce, b)
shifted_y = y + np.linalg.solve(ce, b@x)
rhs = x@effective@x + shifted_y@ce@shifted_y
residual = float(abs(lhs-rhs))
assert residual < 2e-14
floor = energy+(1-math.sqrt(r))*min(np.linalg.eigvalsh(ae)[0],
                                   np.linalg.eigvalsh(ce)[0])
actual_floor = float(np.linalg.eigvalsh(h)[0])
assert floor <= actual_floor

# SU(2), unit-S^3 heat-kernel bound. Bound the infinite tail geometrically.
tail_ratio = (25.0/16.0)*math.exp(-9.0)
delta_upper = (4*math.exp(-3)+9*math.exp(-8)
               +16*math.exp(-15)/(1-tail_ratio))
delta_partial = sum((n+1)**2 * math.exp(-n*(n+2)) for n in range(1, 30))
assert delta_partial <= delta_upper < 0.203

# SU(3), K=4 times the conventional quadratic Casimir. Group by p+q=s.
su3_tail_ratio = (5/4)*(6/5)**6*math.exp(-11)
su3_tail_first = (4*5**6/64)*math.exp(-21)
su3_delta_upper = (18*math.exp(-16/3)+72*math.exp(-40/3)
                   +64*math.exp(-12)+su3_tail_first/(1-su3_tail_ratio))
su3_delta_partial = 0.0
for p in range(18):
    for q_label in range(18):
        if p == q_label == 0:
            continue
        dimension = (p+1)*(q_label+1)*(p+q_label+2)/2
        casimir4 = (4/3)*(p*p+q_label*q_label+p*q_label+3*p+3*q_label)
        su3_delta_partial += dimension**2*math.exp(-casimir4)
assert su3_delta_partial <= su3_delta_upper < 0.088

# Exact rational certificates for the rounded heat-kernel bounds.
# A positive Taylor sum bounds exp(x) from below, so its reciprocal
# bounds exp(-x) from above. All comparisons below use Fractions.
def exp_negative_upper(x, degree=100):
    x = Fraction(x)
    term = total = Fraction(1)
    for k in range(1, degree+1):
        term *= x / k
        total += term
    return 1 / total

u = exp_negative_upper
su2_rational_upper = (4*u(3)+9*u(8)
    +16*u(15)/(1-Fraction(25,16)*u(9)))
su3_rational_upper = (18*u(Fraction(16,3))+72*u(Fraction(40,3))
    +64*u(12)+(Fraction(4*5**6,64)*u(21))
    /(1-Fraction(5,4)*Fraction(6,5)**6*u(11)))
assert su2_rational_upper < Fraction(203,1000)
assert su3_rational_upper < Fraction(88,1000)

# Check the archived shell generating function only under its specified counts.
mu = 0.6
t = math.exp(-mu)
shell_sum = sum((10*n*n+2)*t**n for n in range(1, 1000))
shell_formula = 2*t*(6+3*t+t*t)/(1-t)**3
assert abs(shell_sum-shell_formula) < 2e-11

result = {
    "ring_counterexample": rows,
    "nonscalar_schur_identity": {
        "response_squared": r, "identity_error": residual,
        "proved_floor": float(floor), "smallest_eigenvalue": actual_floor},
    "su2_heat_kernel": {
        "delta_partial": delta_partial, "delta_geometric_upper": delta_upper,
        "certified_rounded_upper": 0.203,
        "certified_kernel_ratio": 797/1203},
    "su3_heat_kernel": {
        "delta_partial": su3_delta_partial, "delta_geometric_upper": su3_delta_upper,
        "certified_rounded_upper": 0.088,
        "certified_kernel_ratio": 57/68},
    "exact_rational_checks": {
        "su2_upper_below_203_over_1000": True,
        "su3_upper_below_88_over_1000": True,
        "method": "Reciprocals of positive degree-100 Taylor sums for exp(x)."},
    "shell_formula_error": abs(shell_sum-shell_formula),
    "status": "All deterministic arithmetic checks passed."
}
print(json.dumps(result, indent=2))
```

### Recorded output

```json
{
  "ring_counterexample": [
    {
      "sites": 8,
      "local_gap": 1.0,
      "single_row_norm_squared": 0.4844970703125,
      "global_feshbach_response_at_zero": 0.968994140625,
      "exact_gap": 0.015625,
      "computed_gap": 0.015625000000000125
    },
    {
      "sites": 32,
      "local_gap": 1.0,
      "single_row_norm_squared": 0.4990239143371582,
      "global_feshbach_response_at_zero": 0.9980478286743164,
      "exact_gap": 0.0009765625,
      "computed_gap": 0.000976562500000002
    },
    {
      "sites": 128,
      "local_gap": 1.0,
      "single_row_norm_squared": 0.49993896670639515,
      "global_feshbach_response_at_zero": 0.9998779334127905,
      "exact_gap": 6.103515625e-05,
      "computed_gap": 6.103515624985817e-05
    },
    {
      "sites": 256,
      "local_gap": 1.0,
      "single_row_norm_squared": 0.4999847413273528,
      "global_feshbach_response_at_zero": 0.9999694826547054,
      "exact_gap": 1.52587890625e-05,
      "computed_gap": 1.5258789062195429e-05
    }
  ],
  "nonscalar_schur_identity": {
    "response_squared": 0.07572723548399213,
    "identity_error": 0.0,
    "proved_floor": 1.5042668147512845,
    "smallest_eigenvalue": 1.650440632020962
  },
  "su2_heat_kernel": {
    "delta_partial": 0.20217233250351274,
    "delta_geometric_upper": 0.2021723325036721,
    "certified_rounded_upper": 0.203,
    "certified_kernel_ratio": 0.6625103906899418
  },
  "su3_heat_kernel": {
    "delta_partial": 0.0874131925033882,
    "delta_geometric_upper": 0.08741368097920602,
    "certified_rounded_upper": 0.088,
    "certified_kernel_ratio": 0.8382352941176471
  },
  "exact_rational_checks": {
    "su2_upper_below_203_over_1000": true,
    "su3_upper_below_88_over_1000": true,
    "method": "Reciprocals of positive degree-100 Taylor sums for exp(x)."
  },
  "shell_formula_error": 0.0,
  "status": "All deterministic arithmetic checks passed."
}
```
