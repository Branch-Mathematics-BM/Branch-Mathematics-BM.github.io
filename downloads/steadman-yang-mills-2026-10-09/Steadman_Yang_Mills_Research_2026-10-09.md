# Steadman model and Yang–Mills: exact reduced dynamics and certified spectral completion at a finite regulator

**Date:** 9 October 2026  
**Project:** Branch Mathematics / GURF  
**Relationship to the frozen work:** Additive continuation of the 8 October checked manuscript and the 22 September V1.4.10-F record. The Branch Mathematics V1 foundation and existing freeze records are unchanged. This is not a V1.5 declaration.  
**Overall status:** The universal Steadman physical model and the four-dimensional continuum Yang–Mills existence and mass-gap problem are **not completed**. The finite-regulator statements proved here have their stated scope. No novelty or independent peer review is claimed.

## 1. Outcome in plain language

The work recovered from 8 October had already defined the regulated dynamics, proved a positive gap on every finite lattice, and identified a failure in promoting individual block response bounds to a bound on the whole system. This continuation does not present those results as new.

The additional result is a rigorous way to turn a finite calculation into lower and upper bounds for the actual, infinite-dimensional finite-lattice Hamiltonian. The states omitted from the calculation are explicitly controlled. Their effects are not assumed to vanish.

Three developments are completed here:

1. **Exact reduced evolution.** Eliminating a sector leaves a memory term and a term carrying its initial state. These equations specify how omitted distinctions and returning responses remain in the model.
2. **Certified spectral bounds.** A finite retained matrix, a proved energy floor for the omitted sector, and the actual coupling between the two yield a rigorous gap interval. The method does not require knowing the true vacuum in advance.
3. **Fixed-regulator completeness.** For each fixed finite lattice and finite coupling, sufficiently large electric cutoffs make the certificate positive and its gap interval converge to the true gap. This is a mathematical convergence result; it is not a claim of computational practicality at large volume.

The implementation verifies 12 cases for a single square plaquette, using both SU(2) and SU(3), including the earlier trial couplings 0.00333 and 0.00348. Every certification step uses rational arithmetic. The SU(2) calculation with nine basis functions uses nine irreducible characters; it is not a nine-loop perturbative calculation.

The remaining obstruction is not a request for more conceptual input from the user. It is a mathematical obligation: obtain a positive bound in physical energy units along an appropriate infinite-volume and continuum trajectory, and construct the corresponding nontrivial relativistic theory.

## 2. Recovered sources and canonical scope

The following manuscripts were read in full for this continuation:

- `Steadman_Hypothesis_V1_1_Strict_Review_Freeze_2026-09-21(1).md`.
- `Steadman_Yang_Mills_V1_4_10_F_CANONICAL_FROZEN_2026-09-22.md`.
- `Steadman_Yang_Mills_Checked_Continuation_2026-10-08.md`.

The September record reports a volume-uniform SU(2) strong-coupling construction in the normalization below for

\[
|\beta|<\beta_{\rm vac}=\frac{3}{128(e+2)}\simeq0.00496738025665,
\]

with the recorded direct curvature estimate

\[
\frac{\Delta}{c_K}\ge2-\eta(\beta),\qquad
\eta(\beta)\le\frac{3}{e+2}
\left(1-\sqrt{1-|\beta|/\beta_{\rm vac}}\right).
\]

Those are retained as the source's frozen statements. Their full supporting cluster-construction chain is not independently re-proved here. The theorems and calculations below do not depend on that cluster estimate. The threshold is an endpoint of that proof method, not an established physical phase boundary.

The October record supplies the controlling interpretation: **Frame responds; fibre smooths into the Response.** Efficiency is emergent in this regulated branch; an independent Efficiency Force is not inserted into pure Yang–Mills. RD is used below as the project's abbreviation without imposing a new terminology change.

## 3. One consistent regulated equation set

Let \(\Lambda\) be a finite connected spatial lattice with links \(\mathcal E\), plaquettes \(\mathcal P\), and compact connected gauge group \(G\). For the computations, \(G=SU(2)\) or \(SU(3)\). Put

\[
X=G^{\mathcal E},\qquad
\mathcal H_{\rm phys}=L^2(X,dU)^{\mathcal G},
\]

where \(dU\) is normalized product Haar measure and \(\mathcal G\) is the vertex gauge action. In link variables,

\[
U_{xy}\mapsto g_xU_{xy}g_y^{-1}.
\]

The retained Hamiltonian, written without an irrelevant additive constant, is

\[
\boxed{
H=c_Kh,\qquad
h=K+V_\beta=K-\beta\mathcal P_0,\qquad
K=-\sum_e\Delta_e,\qquad
\mathcal P_0=\sum_p\frac1N\operatorname{ReTr}U_p.
}
\tag{1}
\]

Here \(c_K>0\) is an energy coefficient. For other compact groups, choose a declared finite-dimensional unitary representation for the bounded real plaquette function; the abstract results only use boundedness and gauge invariance. The equations are

\[
\boxed{
i\hbar\partial_t\Psi=H\Psi,\quad
\Psi\in\mathcal H_{\rm phys},\quad
h\Omega=\varepsilon_0\Omega,\quad
\Omega>0,\quad \|\Omega\|=1.
}
\tag{2}
\]

Use the same Casimir normalization as the recovered work: on an SU(2) link, the irrep indexed by \(n=2j\) has electric eigenvalue \(n(n+2)\). On an SU(3) link, the irrep \((p,q)\) has

\[
\lambda_{p,q}=\frac43(p^2+q^2+pq+3p+3q).
\tag{3}
\]

Thus the one-link first eigenvalues are 3 and \(16/3\), respectively. These are not physical one-plaquette gaps; gauge constraints and the number of links matter.

With \(W=-2\log\Omega\), the exact vacuum and transformed equations are

\[
\boxed{
\frac12\Delta W-\frac14|\nabla W|^2-\beta\mathcal P_0=\varepsilon_0,
\qquad
\Omega^{-1}(h-\varepsilon_0)\Omega
=\mathcal A_W=-\Delta+\nabla W\cdot\nabla.
}
\tag{4}
\]

Multiplication by \(\Omega\) is unitary from \(L^2(\Omega^2dU)\) to \(L^2(dU)\). Consequently,

\[
\frac{\Delta_{\rm phys}}{c_K}
=\inf_{\substack{f\in\mathcal H_{\rm phys}\cap H^1\!,\ f\ne0\\
\int f\Omega^2dU=0}}
\frac{\int|\nabla f|^2\Omega^2dU}
{\int|f|^2\Omega^2dU}.
\tag{5}
\]

In (5), gauge invariance is understood in the weighted space as well. The positive weight is part of the Hilbert-space formulation; no primitive probabilistic ontology is needed to state these identities.

Equation (1) is the standard Hamiltonian lattice branch, organized with the project's terminology. These equations alone do not supply a new empirical prediction beyond that branch [R2].

| Steadman object | Exact realization and limit of the claim |
|---|---|
| Frame | Configuration space, gauge constraints, metric, inner product and Hamiltonian |
| Response | Evolution under (2), or variation under a specified perturbation of \(H\) |
| RD persistence | Unitary preservation of inner products and therefore specified state distinctions |
| Completion fibre | All full states compatible with a declared receiver output |
| Smoothing | A specified analytic or reduced-state operation, retaining its discarded sector or reconstruction data |
| Efficiency | A task-relative comparison, such as \(\eta_R=R_{\rm useful}/R_{\rm ideal}\), using identical constraints for numerator and denominator |

For normalized rays, the specified distinction

\[
D([\psi],[\phi])=1-|\langle\psi,\phi\rangle|^2
\]

is invariant under their common unitary evolution. This is a proved invariant. It is not a derivation of a universal additive RD density or a local RD conservation current. Equally, \(\eta_R\) is not an extra field equation.

## 4. Exact elimination retains the returning response

Let \(\Pi\) be a finite electric spectral projector in the physical Hilbert space and \(Q=I-\Pi\). This is a division into retained and omitted energy states, not a claim that the sectors are spatially separated blocks. Write

\[
h=\begin{pmatrix}A&B^*\\B&C\end{pmatrix},\qquad
\Psi=\begin{pmatrix}x\\y\end{pmatrix}.
\tag{6}
\]

Because \(\Pi\) commutes with \(K\), \(B=QV_\beta\Pi\) is bounded. Use dimensionless evolution parameter \(\tau=c_Kt/\hbar\). Then

\[
i\dot x=Ax+B^*y,\qquad i\dot y=Bx+Cy.
\]

Variation of constants gives

\[
y(\tau)=e^{-i\tau C}y(0)
-i\int_0^\tau e^{-i(\tau-s)C}Bx(s)\,ds.
\tag{7}
\]

Substitution proves the exact retained equation

\[
\boxed{
i\dot x(\tau)=Ax(\tau)+B^*e^{-i\tau C}y(0)
-i\int_0^\tau B^*e^{-i(\tau-s)C}Bx(s)\,ds.
}
\tag{8}
\]

The equation is first proved for domain-valued initial states and extends in its mild formulation. The two additional terms have distinct roles: the first carries the initial omitted state; the integral carries excursions into the omitted sector and their subsequent return. Dropping either term changes the dynamics unless it vanishes or an error estimate justifies the approximation.

The exact total norm satisfies

\[
\|x(\tau)\|^2+\|y(\tau)\|^2=\|\Psi(0)\|^2.
\]

More strongly, inner products between any two full solutions remain invariant. A fixed receiver that sees only \(x\) need not retain all distinctions. The reconstruction (7) identifies where its missing state information resides.

The kernel in (8) is retarded in this evolution parameter. It does not by itself establish a spacetime light cone or relativistic locality. Those are additional continuum properties.

For a stationary eigenstate with energy \(E<\inf\sigma(C)\), elimination instead gives

\[
y=-(C-E)^{-1}Bx,
\qquad
S(E)x=0,
\]

\[
\boxed{S(E)=A-E-B^*(C-E)^{-1}B.}
\tag{9}
\]

The full norm becomes

\[
\|\Psi\|^2=\langle x,M(E)x\rangle,
\qquad M(E)=I+B^*(C-E)^{-2}B=-S'(E).
\tag{10}
\]

Thus eliminating the fibre/omitted sector changes both the effective operator and its state norm. A response argument cannot keep only a convenient effective energy and discard the norm response. Since the subtraction in (9) is nonnegative, excursions into the omitted sector can lower spectral energies. A local restoring scale does not automatically prevent soft collective states.

These are standard exact elimination identities, with the connection to the project made explicit; novelty is not asserted [R3].

## 5. Finite-regulator existence without assuming a mass gap

**Proposition 1.** On a finite connected product of compact connected Lie groups, \(h=K+V\) with smooth real bounded \(V\) is self-adjoint on \(D(K)\), bounded below, and has compact resolvent. It has a unique strictly positive smooth ground state. If \(V\) is gauge invariant, this ground state is gauge invariant. Whenever the physical Hilbert space has a nontrivial excited sector, its first gap is strictly positive.

**Proof.** The Laplacian on a compact manifold has compact resolvent. A bounded real multiplication perturbation preserves self-adjointness and compact resolvent. The connected heat kernel is strictly positive, and adding a bounded real potential preserves positivity improvement, for example by its positive product-kernel construction. Hence the ground eigenfunction is strictly positive and its eigenvalue simple. Elliptic regularity gives smoothness. A gauge transformation commutes with the Hamiltonian and preserves positivity and normalization; uniqueness therefore fixes the ground state. Compact resolvent and ground-state simplicity isolate the next energy above it. Restriction to a nontrivial invariant physical sector cannot add lower excitations. \(\square\)

This proposition is a finite-volume statement. It has no uniform lower constant as written. It also covers a broader class of bounded potentials than Yang–Mills; its truth does not solve the continuum question.

## 6. A certified gap from a retained matrix and its omitted sector

All energies in this section are eigenvalues of \(h\), hence dimensionless; multiply final gaps by \(c_K\).

Let the ordered retained eigenvalues be \(a_0\le a_1\le\cdots\). Suppose

\[
C\ge dI,\qquad \|B\|\le b.
\tag{11}
\]

For electric cutoff projectors one may always take

\[
v=\|V\|\le|\beta|\,|\mathcal P|,
\qquad d=\kappa-v,\qquad b\le v,
\tag{12}
\]

where \(QKQ\ge\kappa Q\). These conservative bounds require no guessed vacuum. Exact representation structure can give much smaller \(b\).

**Theorem 2 — scalar enclosure.** For \(j\) in the retained range, define

\[
\ell_j=\frac{a_j+d-\sqrt{(d-a_j)^2+4b^2}}2.
\tag{13}
\]

When \(a_j<d\),

\[
\boxed{\ell_j\le E_j(h)\le a_j.}
\tag{14}
\]

In particular,

\[
\boxed{
c_K(\ell_1-a_0)\le\Delta_{\rm phys}
\le c_K(a_1-\ell_0).
}
\tag{15}
\]

A nonpositive lower endpoint is an inconclusive certificate, not evidence of a zero or negative physical gap.

**Proof.** For \(E<d\), completing the square gives the form identity

\[
\langle(x,y),(h-E)(x,y)\rangle
=\langle x,S(E)x\rangle
+\|(C-E)^{1/2}(y+(C-E)^{-1}Bx)\|^2.
\tag{16}
\]

The corresponding triangular change is invertible on the form domain, so the number of eigenvalues of \(h\) strictly below \(E\) equals the negative inertia of \(S(E)\). Moreover,

\[
S(E)\ge A-E-\frac{b^2}{d-E}I.
\tag{17}
\]

Whenever \(E+b^2/(d-E)\le a_j\), the right side has at most \(j\) negative eigenvalues. Thus \(E_j(h)\ge E\). Solving the equality gives (13). The upper bound is the ordinary min–max/Ritz bound. Applying the bounds separately to ground and first-excited energies proves (15). \(\square\)

If rational matrix calculations give intervals \([a_j^-,a_j^+]\), a convenient entirely rational lower bound is

\[
L_j=a_j^- -\frac{b^2}{d-a_j^-},\qquad d>a_j^+.
\tag{18}
\]

Indeed \(L_j+b^2/(d-L_j)\le a_j^-\le a_j\). Consequently

\[
c_K(L_1-a_0^+)\le\Delta_{\rm phys}
\le c_K(a_1^+-L_0).
\tag{19}
\]

This bound controls the true Hamiltonian, including its ground-energy shift. Subtracting two uncontrolled Ritz values would not give it.

### Keeping the actual omitted-sector coupling

The scalar bound can lose most of the available accuracy. Retain the coupling Gram matrix

\[
G_B=B^*B.
\]

Then (9) and (11) give the sharper finite-matrix inequality

\[
\boxed{
S(E)\ge F_d(E):=A-EI-\frac{G_B}{d-E},\qquad E<d.
}
\tag{20}
\]

**Corollary 2.1 — matrix enclosure.** If the exactly calculated negative inertia of \(F_d(L_j)\) is at most \(j\), then \(E_j(h)\ge L_j\). Combine with the Ritz upper endpoints to obtain (19).

The comparison matrix decreases strictly as energy increases:

\[
F_d'(E)=-I-\frac{G_B}{(d-E)^2}\prec0.
\]

Its inertia can therefore be bracketed by bisection. For rational inputs, exact rational symmetric elimination supplies a certificate without any floating-point sign decisions. If a leading pivot vanishes, another rational test point is used. This is the method behind the table in Section 8.

For finite representation cutoffs and a Wilson plaquette potential, the image of \(B\) is also contained in a finite set of representations. Thus \(G_B\) can be computed without replacing the omitted Hilbert space by a finite one. The rest of that Hilbert space is controlled by \(C\ge dI\).

## 7. Completion theorem at a fixed finite regulator

**Theorem 3 — eventual certification.** Fix the finite lattice, compact group, finite coupling and physical energy normalization in Proposition 1. Let \(\Pi_R\) be increasing physical electric spectral projectors whose union is a form core for \(K\), and whose omitted electric floor \(\kappa_R\) tends to infinity. Then the gap intervals (19) converge to the strictly positive finite-regulator gap. In particular, a sufficiently large finite cutoff gives a positive certified lower bound.

**Proof.** Since \(V\) is bounded, electric spectral truncation converges in the form norm of \(h\). The min–max principle, applied to truncated spans of its first eigenfunctions, gives

\[
a_{j,R}\downarrow E_j(h),\qquad j=0,1.
\]

Meanwhile \(v=\|V\|\) is fixed,

\[
d_R=\kappa_R-v\to\infty,\qquad b_R\le v.
\]

Therefore \(b_R^2/(d_R-a_{j,R})\to0\). The lower endpoints in (18) and the Ritz upper endpoints converge to the same corresponding energies. Choose matrix-arithmetic enclosure widths tending to zero as well. The resulting lower and upper gap endpoints both converge to \(E_1-E_0>0\). Eventually the lower endpoint is positive. The matrix refinement (20) can only improve the lower estimates. \(\square\)

As an algorithmic statement, this assumes that the specified coupling and finite matrix entries admit certified computation; rational couplings in the implemented character bases satisfy that requirement. It is not a computability assertion for arbitrary noncomputable real input.

The theorem applies at each fixed finite regulator for SU(2), SU(3), and other compact connected groups with the stated hypotheses. **The implemented calculations below are single-plaquette calculations; a many-plaquette spin-network assembler was not implemented or run.**

The quantifiers are decisive:

\[
\forall(a,L,\beta)\text{ fixed},\ \exists R\text{ giving a positive certificate}
\]

does not imply

\[
\exists m_*>0,\ \forall(a,L)\text{ along a continuum trajectory},\
\Delta_{a,L}\ge m_*.
\]

There is no volume-uniform complexity bound or continuum gap bound in Theorem 3.

## 8. Exact SU(2) and SU(3) calculations

### The physical single-plaquette space

Take a graph consisting of one square and its four distinct links, imposing gauge invariance at every vertex. Gauge-invariant states are class functions of the plaquette holonomy. The ordinary irreducible characters \(\chi_r=\operatorname{Tr}_r\), without division by representation dimension, form an orthonormal basis under normalized Haar measure. Each of the four link Laplacians acts as the holonomy Laplacian, so the electric operator is four times the one-link operator.

This is an exactly specified compact gauge system. It is not a spatially extended four-dimensional continuum theory.

### SU(2)

Let \(\chi_n\), \(n=0,1,\ldots\), denote the SU(2) characters. The identity

\[
\chi_1\chi_n=\chi_{n+1}+\chi_{n-1},\qquad\chi_{-1}=0,
\]

gives the exact infinite Jacobi matrix

\[
h_{nn}=4n(n+2),\qquad h_{n,n+1}=h_{n+1,n}=-\beta/2.
\tag{21}
\]

Keeping \(n=0,\ldots,N-1\),

\[
d_N=4N(N+2)-|\beta|,\quad
b_N=|\beta|/2,\quad
G_B=\frac{\beta^2}{4}|N-1\rangle\langle N-1|.
\tag{22}
\]

The unretained sector is still infinite. Its electric floor and bounded potential prove the first bound in (22).

### SU(3)

Use the orthonormal characters \(\chi_{p,q}\), \(p,q\ge0\). The diagonal electric energy is

\[
h^{\rm electric}_{(p,q),(p,q)}
=\frac{16}{3}(p^2+q^2+pq+3p+3q).
\tag{23}
\]

The real plaquette potential is \(-\beta(\chi_{1,0}+\chi_{0,1})/6\). Fundamental tensor multiplication connects

\[
(p,q)\longrightarrow(p+1,q),\ (p-1,q+1),\ (p,q-1),
\]

and antifundamental multiplication connects

\[
(p,q)\longrightarrow(p,q+1),\ (p+1,q-1),\ (p-1,q),
\]

with negative labels omitted. Each allowed matrix entry is \(-\beta/6\).

Retain \(p+q\le s\), a space of dimension \((s+1)(s+2)/2\). For \(t=s+1\),

\[
\kappa_s=\frac{16}{3}\left(t^2+3t-\left\lfloor t^2/4\right\rfloor\right),
\qquad d_s=\kappa_s-|\beta|.
\tag{24}
\]

**Proof of the tail floor.** At fixed \(p+q=t\), the Casimir polynomial equals \(t^2-pq+3t\), minimized when \(pq=\lfloor t^2/4\rfloor\). The resulting minimum increases with \(t\), so the first omitted shell supplies the minimum over every omitted representation.

Only the shell \(p+q=s+1\) couples directly to the retained space. Every row and column of this boundary coupling contains at most two entries of magnitude \(|\beta|/6\). The row/column norm bound therefore gives

\[
\|B\|\le |\beta|/3.
\tag{25}
\]

The implementation computes the exact boundary matrix and \(G_B=B^*B\), rather than using only (25). No SU(2) cluster constants are reused for SU(3).

### Certified intervals

The following bounds are for the **full infinite-character single-plaquette Hamiltonians**, not just their retained matrices. All entries are in units of \(c_K\). Decimal endpoints are rounded outwards. At the same numerical \(\beta\), the two gauge groups are not assumed to share a matched physical coupling or energy scale.

| Group | Coupling beta | Retained dimension | Certified lower gap | Certified upper gap |
|---|---:|---:|---:|---:|
| SU(2) | 0 | 9 | 12.0000000000 | 12.0000000000 |
| SU(2) | 0.00333 | 9 | 12.0000003234 | 12.0000003235 |
| SU(2) | 0.00348 | 9 | 12.0000003532 | 12.0000003533 |
| SU(2) | 1 | 9 | 12.0291212439 | 12.0291212440 |
| SU(2) | 10 | 9 | 14.5487594916 | 14.5487594917 |
| SU(2) | 100 | 9 | 51.1224651073 | 51.1224712712 |
| SU(2) | 100 | 18 | 51.1224666160 | 51.1224666161 |
| SU(3) | 0 | 15 | 21.3333333333 | 21.3333333334 |
| SU(3) | 0.00333 | 15 | 21.3327783583 | 21.3327783584 |
| SU(3) | 0.00348 | 15 | 21.3327533606 | 21.3327533607 |
| SU(3) | 1 | 15 | 21.1689602267 | 21.1689602268 |
| SU(3) | 10 | 15 | 19.9292933184 | 19.9292933197 |

For SU(2) at \(\beta=100\), nine retained characters already bound the gap within approximately \(6.2\times10^{-6}c_K\); eighteen characters narrow the displayed enclosure to \(10^{-10}c_K\). The omitted sector remains infinite in both certificates.

The behavior differs between groups: in this single-plaquette normalization the small-coupling SU(2) gap increases, whereas the SU(3) first gap decreases initially because its fundamental/antifundamental excited pair splits. This is a useful check against assuming that stronger coupling or smoothing must monotonically increase every gap. It is not a continuum phase prediction.

As an independent analytic check, ordinary isolated-level perturbation theory in (21) yields

\[
E_0=-\beta^2/48+O(\beta^4),\quad
E_1=12+\beta^2/120+O(\beta^4),\quad
\Delta/c_K=12+7\beta^2/240+O(\beta^4).
\]

For SU(3), diagonalizing the first-order perturbation in the two-dimensional first-excited space gives

\[
\Delta/c_K=64/3-\beta/6+O(\beta^2),\qquad\beta\downarrow0.
\]

These expansions agree with the exact enclosures; the certified calculations do not depend on truncating either expansion.

## 9. What the calculations prove, and what they cannot prove

The exact finite-matrix inertia, the analytic tail floor, and the exact coupling Gram matrix jointly prove the numerical gap intervals. Ordinary numerical eigenvalues of larger matrices were also checked for consistency; those floating-point checks are diagnostics, not the certificate.

The method completes an omitted-state control problem at a finite regulator. It does not establish a regulator-uniform response bound. Even an arbitrarily accurate finite-volume gap can shrink to zero with increasing volume.

The October counterexample remains decisive for the existing response route: local conditional gaps can stay at 1 while a collective mode has energy \(\varepsilon\to0\). A small square-sum for each receiving block does not exclude that collective mode. The present method avoids that inference by bounding the full omitted-sector resolvent through a valid operator inequality.

For a continuum application, denote certified dimensionless endpoints by \(L_1(a,L,R)\) and \(U_0(a,L,R)\). A sufficient spectral target is

\[
\boxed{
\liminf_{\substack{a\to0\\L\to\infty}}
c_K(a,L)\bigl[L_1(a,L,R(a,L))-U_0(a,L,R(a,L))\bigr]
\ge m_*>0.
}
\tag{26}
\]

All quantities must be evaluated on a physically matched coupling and observable trajectory. In the conventional Hamiltonian normalization, the coefficient ratio represented here by \(\beta\) grows toward weak bare coupling; the small-\(\beta\) frozen interval is the electric strong-coupling regime. The exact conversion depends on metric, trace and plaquette conventions. It is not licensed to identify this \(\beta\) with every Euclidean Wilson coupling called beta.

The crude general omitted-sector estimates have

\[
v\le|\beta|\,|\mathcal P|,\quad b\le v,\quad d=\kappa-v.
\]

Their correction is of order \(v^2/(d-a_1)\). Because \(v\) can grow with volume and along the coupling trajectory, fixed-volume convergence does not give (26). A local or scale-dependent estimate must overcome this growth and control the actual lowest collective energies.

Even proving (26) is not the entire construction problem. One must establish the appropriate limits and observables, relativistic/Euclidean axioms, and nontriviality. The official Yang–Mills problem requires the resulting quantum field theory and its positive mass gap, rather than only finite lattice positivity [R1].

## 10. The universal Steadman model remains underdetermined

The finite regulated realization is fully specified by (1)–(4), and its exact reduced response is (8)–(10). Its mathematical status is separate from whether the wider physical interpretation has independent empirical support.

RD preservation, smoothing and efficiency do not uniquely select a physical Hamiltonian. For example, on \(\mathbb C\Omega\oplus L^2((0,\infty),d\lambda)\), both

\[
H_+(z,f)=(0,(1+\lambda)f),\qquad
H_0(z,f)=(0,\lambda f)
\]

have unitary distinction-preserving evolution, a unique zero-energy vacuum, and injective analytic smoothing semigroups. Their gaps are respectively 1 and 0. This is a counterexample to deducing a gap from those qualitative properties alone, not a counterexample to Yang–Mills.

To complete a universal Steadman theory would require an explicit dynamical or constitutive law beyond these descriptors, or a proved derivation identifying them with existing physical equations and their limits. A universal RD current, an independent efficiency interaction, a gravity law, and a unique prediction have not been derived here. Introducing an adjustable extra mass or interaction merely to guarantee a positive gap would change the pure Yang–Mills target.

No new universal equation is silently assumed in this report. The absence of the missing derivation is stated as a mathematical limitation, not converted into a request for the user to supply the proof.

## 11. Completion ledger

| Item | Status and scope |
|---|---|
| Frozen Branch Mathematics V1 foundation | Preserved |
| September V1.4.10-F strong-coupling package | Recovered; retained within its recorded scope; supporting cluster chain not independently re-certified here |
| Defined finite-lattice evolution and true-vacuum transform | Established; inherited formulas with explicit normalization |
| Exact state elimination, memory and reconstruction | Derived here for the retained/omitted sector split |
| Gap bounds with explicit omitted-sector control | Proved in Theorem 2 and Corollary 2.1 |
| Eventual positive certification at each fixed finite regulator | Proved in Theorem 3 under its computable-input qualification for an algorithm |
| SU(2)/SU(3) single-plaquette certificates | 12 exact rational cases passed |
| Large multi-plaquette numerical calculations | Not run |
| Regulator-uniform continuation to weak bare coupling | Not proved |
| Nontrivial four-dimensional continuum Yang–Mills construction | Not established |
| Positive physical mass gap in that continuum theory | Not established |
| Universal Steadman physical dynamics | Not uniquely completed |
| Clay solution, novelty or independent validation | Not claimed |

The requested complete universal model and continuum proof have therefore not been achieved. The completed contribution is a reproducible finite-regulator certification method and an exact account of the returning response, with no omitted spectral sector treated as harmless by assumption.

## 12. Reproducibility and references

The accompanying files are:

- `verify_certificates.py`: Python 3 standard-library implementation. It builds the declared character matrices, computes retained eigenvalue intervals by exact rational inertia, computes the omitted coupling Gram matrix, and brackets the comparison eigenvalues from (20).
- `certificate_results.json`: complete numerical record, including both the coarse scalar certificate and the sharper matrix certificate.

Run:

```bash
python3 verify_certificates.py
```

The script recreates the JSON beside itself. The certificate uses no external numerical packages and no floating-point eigenvalue decisions. Fractions represent the specified couplings exactly. Bisection widths are at most \(10^{-13}\); reported decimal endpoints are rounded outward to ten decimal places.

The verification also checks exact inertia against a known two-by-two spectrum, the SU(3) first omitted-shell energy minima on sample cutoffs, and the algebraic Schur lower-endpoint inequalities. The proof of (24) supplies control of every omitted shell, beyond those sample checks.

The exact computations and included analytic proofs are internal verification. They are not a substitute for independent scrutiny of a submitted mathematical result.

**[R1]** A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official problem description, [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf). The [current Clay problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) was also checked on 9 October 2026. Used to identify the requested construction and spectral target.

**[R2]** J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Physical Review D 11, 395 (1975), [publisher record](https://link.aps.org/doi/10.1103/PhysRevD.11.395). Context for the established Hamiltonian lattice formulation, not a claim that the present interpretation is new physics.

**[R3]** G. Dusson, I. M. Sigal and B. Stamm, *The Feshbach–Schur map and perturbation theory* (2021), [arXiv:2105.02058](https://arxiv.org/abs/2105.02058). Context for the standard operator-elimination method. The specific bounds used in this report are proved explicitly in Sections 6–7.
