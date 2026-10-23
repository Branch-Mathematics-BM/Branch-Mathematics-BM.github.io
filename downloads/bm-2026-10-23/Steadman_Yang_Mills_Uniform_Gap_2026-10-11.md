# Steadman–Yang–Mills: an all-orders local bound and a fixed-spacing limit

**Date:** 11 October 2026  
**Branch:** Additive continuation of the 9 October finite-lattice certificates. The frozen BM foundation and V1.4.10-F remain the prior baselines.  
**Scope:** SU(2), bipartite finite lattice graphs with distinct four-link plaquettes, and a subsequential ground-transform realization on the infinite three-dimensional spatial lattice at fixed spacing.  
**Review status:** Self-contained analytic derivation with exact arithmetic audits; not independently peer reviewed. No novelty or Millennium-problem completion claim.

## 1. Outcome and its boundary

The previous certificates bounded the infinite-dimensional Hamiltonian on several small finite graphs. Their omitted-state estimates did not stay useful as the volume grew. The other recovered continuation proposed star blocks and a Catalan majorant, but its higher-order constants had not been proved.

This note supplies a different, explicit all-orders estimate. It controls the logarithm of the actual vacuum by the links on which each interaction depends. The nonlinear bound uses an electric-energy weight, so summing over shared links does not introduce a volume factor.

For the existing normalization on any finite open three-dimensional cubic lattice,

\[
h=K-\beta T,\qquad H=c_Kh,\qquad
K=-\sum_e\Delta_e,\qquad
T=\sum_p\frac12\operatorname{Tr}U_p,
\]

the derivation gives

\[
\boxed{\quad
\frac{\Delta_{\rm phys}}{c_K}
\ge \frac12+\frac32\sqrt{1-\frac{64|\beta|}{3}}
\ge\frac12,
\qquad |\beta|\le\frac3{64}=0.046875.
\quad}
\tag{1}
\]

The bound is independent of the number of links and plaquettes. It also applies to the all-functions gap, which is a sufficient lower bound on the physical, gauge-invariant gap. It is deliberately conservative: at beta zero the actual physical gap on the previously tested graphs is 12, while (1) gives only 2.

At fixed spacing and strict inequality \(|\beta|<3/64\), the linked expansion also permits a subsequential infinite-volume probability measure and a closed, gapped ground-transform quadratic form. That construction is given in Section 9; it is not assumed as a gap-transfer hypothesis.

**This does not solve four-dimensional continuum Yang–Mills.** The parameter range remains electric strong coupling. No weak-coupling continuum trajectory, relativistic reconstruction, or continuum nontriviality is established here. Strong-coupling gap results already belong to established lattice theory; expanding this project's proved range is not evidence of a new solution to the Clay problem.

## 2. Exact setting

Let \(\Lambda=(V,E)\) be a finite bipartite graph with at least one plaquette. Each plaquette is a simple cycle of four distinct links, counted once. Assume that each link belongs to at most \(z\ge1\) plaquettes. Orient every link from its black endpoint to its white endpoint.

This orientation is a choice of coordinates. Reversing a previously chosen link orientation replaces \(U_e\) by \(U_e^{-1}\), an isometry of the unit-three-sphere SU(2) metric. It changes neither the original-link electric operator nor the gauge-invariant Hamiltonian.

Use normalized product Haar measure \(dU\) on

\[
\mathcal M_\Lambda=\operatorname{SU}(2)^E.
\]

The link irrep \(n=2j\) has electric eigenvalue

\[
\kappa_n=n(n+2).
\tag{2}
\]

Thus a fundamental four-link plaquette has electric eigenvalue 12. Impose gauge invariance at every vertex, including boundary vertices, with no external charges.

The potential is bounded at each finite regulator. The operator \(h=K-\beta T\) is self-adjoint on the usual Laplacian domain. The proof below constructs a positive smooth gauge-invariant ground state directly. It does not truncate the link representations or replace SU(2) by a finite group.

For an open three-dimensional cubic lattice, \(z\le4\). Even-period periodic cubic graphs are also bipartite, but the infinite-volume construction in this note uses open exhaustions. Four Euclidean coordinate directions are not substituted for three spatial directions in the Hamiltonian statement.

## 3. A Fourier norm that keeps the representation normalization

For each product-group irrep \(\rho\), write the canonical coefficient expansion

\[
f(U)=\sum_\rho\operatorname{Tr}\bigl(C_\rho\rho(U)\bigr),
\qquad
\|f\|_{\mathcal F}=\sum_\rho\|C_\rho\|_1,
\tag{3}
\]

where \(\|\cdot\|_1\) is the matrix trace norm. The factors normally written as representation dimensions in Fourier inversion are absorbed into \(C_\rho\). This is the compact-group Fourier-algebra norm [R1].

The required elementary properties are

\[
\|f\|_\infty\le\|f\|_{\mathcal F},\qquad
\|fg\|_{\mathcal F}\le\|f\|_{\mathcal F}\|g\|_{\mathcal F}.
\tag{4}
\]

Here is a direct justification of the product estimate. A product of two coefficient terms is a coefficient of \(\rho\otimes\sigma\), with matrix \(C_\rho\otimes C_\sigma\) and trace norm \(\|C_\rho\|_1\|C_\sigma\|_1\). Decompose the representation by a unitary into its irreducible summands and multiplicity spaces. Pinching to the summands is trace-norm contractive. Taking the partial trace over a multiplicity space is also trace-norm contractive, by duality with \(B\mapsto B\otimes I\). Summing the irreducible coefficient norms therefore does not increase this bound. Sum over \(\rho,\sigma\) and pass to absolutely convergent series. The supremum estimate follows from unitarity and trace-norm duality.

Let \(P_0 f=f-\int f\,dU\). It removes just the trivial coefficient and is contractive in \(\mathcal F\).

For a function with zero Haar mean, set

\[
\mu_e(f)=\|K_ef\|_{\mathcal F}
=\sum_\rho\kappa_{\rho,e}\|C_\rho\|_1,
\]

\[
\mu(f)=\|Kf\|_{\mathcal F}
=\sum_e\mu_e(f).
\tag{5}
\]

The equality in (5) uses the nonnegative scalar Casimir eigenvalues; it is not an equality of arbitrary norms of sums. Since the least nonzero full-product electric eigenvalue is 3,

\[
\|f\|_{\mathcal F}\le\frac13\mu(f)
\quad\text{for Haar-centered }f.
\tag{6}
\]

### The four-link plaquette norm is 2, not 1

It would be incorrect to use the Fourier norm of a function on a single holonomy variable in (3). Here the group has four independent original-link factors.

For a square oriented in checkerboard coordinates, write

\[
p(U)=\frac12\operatorname{Tr}
\left(U_1U_2^{-1}U_3U_4^{-1}\right).
\]

Use the product representation
\(\rho=U_1\otimes\overline U_2\otimes U_3\otimes\overline U_4\).
In its coefficient space, define

\[
v=\sum_{j,l=1}^2|j,j,l,l\rangle,
\qquad
w=\sum_{i,k=1}^2|i,k,k,i\rangle.
\]

Then

\[
p(U)=\operatorname{Tr}\left(\frac12|v\rangle\langle w|\,\rho(U)\right).
\]

Both vectors have norm 2. The coefficient has rank one and trace norm 2. The product representation is irreducible for the four-factor product group, so

\[
\boxed{\|p\|_{\mathcal F}=2.}
\tag{7}
\]

The conjugate fundamental representation is unitarily equivalent to the usual SU(2) fundamental representation. Choosing that equivalent representative preserves the trace norm. No finite-dimensional gauge-field truncation is involved.

For later auditing, the analogous four-link character \(\chi_n(U_p)\) has Fourier norm \((n+1)^2\), rather than the one-group value \(n+1\).

## 4. The nonlinear estimate, with its constant proved

Choose an orthonormal left-invariant frame \(X_e^a\), \(a=1,2,3\), on each unit-S3 link. The operator norm of \(d\rho_n(X^a)\) is \(n\). This follows from the weights \(n,n-2,\ldots,-n\) of a unit-axis generator and rotational conjugacy of the three generators.

For \(n\ge1\),

\[
n\le\frac13n(n+2).
\]

Consequently,

\[
\|X_e^af\|_{\mathcal F}\le\frac13\mu_e(f).
\tag{8}
\]

Define the real bilinear carré du champ

\[
\Gamma(f,g)=\sum_{e,a}(X_e^af)(X_e^ag).
\]

Using (4), (8), and the three frame directions gives

\[
\boxed{\quad
\|\Gamma(f,g)\|_{\mathcal F}
\le\frac13\sum_e\mu_e(f)\mu_e(g).
\quad}
\tag{9}
\]

This estimate is conservative. It is sufficient to make the complete nonlinear series converge.

### Labeled local interactions

Represent a centered function by a family \(F=(f_S)\), indexed by nonempty finite sets of links. Require each \(f_S\) to depend only on \(S\), be real and gauge invariant, and have zero Haar mean. The label is allowed to be larger than the actual surviving Fourier support; retaining parent labels prevents artificial loss of the connected-support information.

Define

\[
\|F\|_{\rm loc}
=\max_{e\in E}\sum_{S\ni e}\mu(f_S).
\tag{10}
\]

At a finite regulator this is a Banach norm on the centered interaction families. There are finitely many possible labels, and each centered component is complete in its electric-weighted Fourier norm. Equation (6) controls the unweighted function norm as well.

Let

\[
\bigl(\mathfrak B(F,G)\bigr)_U
=K^{-1}P_0\sum_{S\cup T=U}\Gamma(f_S,g_T),
\tag{11}
\]

where \(K^{-1}\) acts on Haar-centered functions. Contributions with disjoint labels vanish because there is no shared differentiable link. This inverse is the full free electric inverse; a diagonal approximation to an interacting omitted sector is not being made.

**Lemma 1.**

\[
\boxed{\|\mathfrak B(F,G)\|_{\rm loc}
\le\frac23\|F\|_{\rm loc}\|G\|_{\rm loc}.}
\tag{12}
\]

**Proof.** Fix an anchor link \(a\). Applying \(K\) to (11) leaves \(P_0\Gamma\), whose Fourier norm is bounded by (9). Since
\(\mathbf1_{a\in S\cup T}\le\mathbf1_{a\in S}+\mathbf1_{a\in T}\), the part anchored in \(S\) is bounded by

\[
\frac13\sum_{S\ni a}\sum_{e\in S}
\mu_e(f_S)\sum_{T\ni e}\mu_e(g_T)
\le\frac13\|G\|_{\rm loc}
\sum_{S\ni a}\sum_{e\in S}\mu_e(f_S)
\le\frac13\|F\|_{\rm loc}\|G\|_{\rm loc}.
\]

The part anchored in \(T\) obeys the same bound. Use \(\sum_e\mu_e(f_S)=\mu(f_S)\) and then maximize over \(a\). This proves (12). In particular, no factor equal to the number of links, plaquettes, or support size has been dropped. The energy weight absorbs the shared-link sum. \(\square\)

All operations preserve gauge invariance: each \(K_e\) commutes with vertex left and right actions, and its product rule gives the gauge invariance of \(\Gamma_e(f,g)\).

## 5. The complete logarithmic vacuum series

Write \(\Omega=Z^{-1/2}e^{-W/2}\), fixing the additive constant in \(W\) by zero Haar mean. The exact ground-state equation is

\[
KW=-2\beta T-\frac12P_0\Gamma(W,W).
\tag{13}
\]

Do not assume a vacuum in deriving a solution of (13). Construct it by

\[
W=\sum_{n\ge1}\beta^n w_n,
\qquad
w_1=-2K^{-1}T=-\frac16T,
\]

\[
w_n=-\frac12K^{-1}P_0
\sum_{j=1}^{n-1}\Gamma(w_j,w_{n-j}),\qquad n\ge2,
\tag{14}
\]

with the labeled version (11) used at each step. Each first-order label is a plaquette. Higher-order labels are unions of overlapping parent labels. They therefore arise from connected plaquette clusters using at most \(n\) plaquettes, counting repetitions.

For the source, (7) gives

\[
\|K(-p/6)\|_{\mathcal F}=\|-2p\|_{\mathcal F}=4.
\]

Thus \(\|w_1\|_{\rm loc}\le4z\). Lemma 1 gives an explicit scalar majorant:

\[
a_1=4z,\qquad
a_n=\frac13\sum_{j=1}^{n-1}a_ja_{n-j},\qquad
\|w_n\|_{\rm loc}\le a_n.
\tag{15}
\]

Solving the recurrence yields

\[
a_n=\operatorname{Cat}_{n-1}
\frac{(4z)^n}{3^{n-1}},
\qquad
\operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m}.
\tag{16}
\]

For \(b=|\beta|\), its generating function is

\[
\boxed{\quad
x_z(b)=\sum_{n\ge1}a_nb^n
=\frac32\left(1-\sqrt{1-\frac{16zb}{3}}\right),
\qquad 0\le b\le\frac3{16z}.
\quad}
\tag{17}
\]

This is the small root of \(x=4zb+x^2/3\). The constant \(1/3\) and the source constant \(4z\) have both been derived; they are not fitted to a few computed coefficients.

The scalar series also converges at its endpoint, with sum \(3/2\), by monotone convergence from below of the Catalan generating function. Thus the interaction series converges absolutely in (10) on the closed interval in (17). At each finite regulator it solves (13), since the bilinear map is continuous. It is analytic in beta on the open interval.

### Regularity and identification of the vacuum

Finite electric-weighted Fourier norm controls first and second derivatives. For example, on a product geodesic with tangent \(v=(v_e)\), a product irrep contributes a generator of operator norm at most \(\sum_e n_e|v_e|\), whose square is bounded by its total Casimir times \(\sum_e|v_e|^2\). Absolute coefficient convergence therefore gives a C2 function and justifies (13) pointwise. Uniform convergence of second derivatives and polarization give the mixed derivatives as well.

Define

\[
e_0=-\frac14\int\Gamma(W,W)\,dU.
\tag{18}
\]

Since \(\int T\,dU=0\), substitution into the exact identity

\[
\frac{h e^{-W/2}}{e^{-W/2}}
=-\frac12KW-\frac14\Gamma(W,W)-\beta T
\]

gives \(h\Omega=e_0\Omega\). This is the original Hamiltonian equation. Elliptic regularity makes \(\Omega\), and hence \(W\), smooth at each finite regulator.

The positive normalized function \(\Omega\) is the actual ground state. Indeed, its ground transform has quadratic form

\[
\langle\Omega f,(h-e_0)\Omega f\rangle_{dU}
=\int|\nabla f|^2\,d\nu,\qquad
d\nu=Z^{-1}e^{-W}dU.
\tag{19}
\]

The form is nonnegative, with kernel the constants on the connected product manifold. This identifies the bottom energy and its uniqueness without assuming a gap during construction. The constructed vacuum is gauge invariant.

## 6. The Hessian bound and the volume-independent gap

**Lemma 2.** For a component depending on \(S\),

\[
|\operatorname{Hess}f_S(v,v)|
\le\mu(f_S)\sum_{e\in S}|v_e|^2.
\tag{20}
\]

**Proof.** The bi-invariant metric makes a product of one-parameter group curves a geodesic. In a product irrep the directional generator has operator norm at most \(\sum_{e\in S}n_e|v_e|\). Thus

\[
\left(\sum_{e\in S}n_e|v_e|\right)^2
\le\left(\sum_e n_e^2\right)\sum_{e\in S}|v_e|^2
\le\left(\sum_e n_e(n_e+2)\right)
\sum_{e\in S}|v_e|^2.
\]

Multiply by the coefficient trace norm and sum over irreps. \(\square\)

Summing (20) over the labels gives

\[
|\operatorname{Hess}W(v,v)|
\le\sum_e|v_e|^2\sum_{S\ni e}\mu(w_S)
\le x_z(b)|v|^2.
\]

In particular,

\[
\boxed{\operatorname{Hess}W\ge-x_z(b)I.}
\tag{21}
\]

The product of unit S3 factors has Ricci tensor \(2I\). The weighted Bochner identity for

\[
\mathcal A=-\Delta+\nabla W\cdot\nabla
\]

and \(d\nu=Z^{-1}e^{-W}dU\) therefore gives a Poincaré gap at least \(2-x_z(b)\). Explicitly, for a nonconstant smooth eigenfunction \(\mathcal Af=\lambda f\), the integrated identity is

\[
\lambda\int|\nabla f|^2\,d\nu
=\int\left(|\operatorname{Hess}f|^2
+(\operatorname{Ric}+\operatorname{Hess}W)(\nabla f,\nabla f)\right)d\nu
\ge(2-x_z(b))\int|\nabla f|^2\,d\nu.
\]

The gradient is nonzero, so \(\lambda\ge2-x_z(b)\). Compact ellipticity supplies the complete eigenfunction basis and the corresponding quadratic-form inequality. Equation (19) transfers it to \(h-e_0\).

**Theorem 1: finite-volume bound.** In the setting of Section 2,

\[
\boxed{\quad
\frac{\Delta_{\rm phys}}{c_K}
\ge2-x_z(|\beta|)
=\frac12+\frac32\sqrt{1-\frac{16z|\beta|}{3}}
\ge\frac12,
\qquad |\beta|\le\frac3{16z}.
\quad}
\tag{22}
\]

The gauge-invariant restriction contains the same vacuum and a subset of the possible excited states, so an all-functions lower bound remains valid there. Taking \(z=4\) proves (1).

Neither \(\|T\|\le N_p\) nor an extensive lower bound on the absolute vacuum energy is used to estimate the gap. Extensive energy is absorbed in \(e_0\); the local vacuum derivative, rather than the size of \(e_0\), controls (22).

The number \(3/(16z)\) is a convergence endpoint for this sufficient estimate. It is not a claimed critical coupling, confinement boundary, or point where the true gap vanishes.

## 7. A proved all-orders remainder for the star oscillation

This section addresses one part of the previously proposed star-block continuation. It does not assert the earlier proposed full star-response certificate.

On the three-dimensional checkerboard lattice, let \(B\) contain the six links incident on one interior black vertex. These black-endpoint stars partition the links. At most twelve plaquettes meet a star. Let

\[
R_B=\sup_\eta\operatorname{osc}_B W(\cdot,\eta).
\]

The first-order term \(-\beta T/6\) has block oscillation at most \(4b\), since each of the at most twelve relevant plaquette functions has oscillation at most 2.

For any centered interaction family \(F\), (6) gives

\[
\operatorname{osc}_B\sum_S f_S
\le\frac23\sum_{S:S\cap B\ne\varnothing}\mu(f_S)
\le\frac23|B|\|F\|_{\rm loc}
\le4\|F\|_{\rm loc}.
\]

Apply this to the tail of (14), using the z = 4 majorant:

\[
\boxed{\quad
R_B\le R_\star(b):=4b+4\left[x_4(b)-16b\right].
\quad}
\tag{23}
\]

This bound is uniform in volume and exterior configuration. It replaces the unspecified \(O(\beta^2)\) in the star oscillation by a convergent, explicit all-orders remainder.

There is also a precise conditional implication. The free six-link Haar Laplacian, restricted to functions invariant under the gauge action at the central black vertex, has first nonzero eigenvalue 6. A single nontrivial link cannot form a singlet under that action. Two fundamental links can, with total electric energy 3 + 3. This proves both the lower bound and its attainment.

The conditional weighted measure on the star is invariant under that interior gauge action. A bounded-density comparison of its conditional variance and Dirichlet form therefore gives

\[
\lambda_B^{\rm int}\ge6e^{-R_\star(b)}.
\tag{24}
\]

**Equation (24) is a conditional scalar gap.** It is not a coercivity bound of 6 on all block vector fields, and it is not by itself a global gap theorem. An application of the previously proposed expression \(6e^{-R}(1-A)\) still needs a valid global influence/response argument on the relevant spaces. The independently proved global result here is (22). No leading-order response coefficient is substituted for that missing theorem.

## 8. Numeric values of the analytic lower bound

The following numbers refer to \(z=4\). The gap column is a conservative decimal **lower bound**, not an enclosure of the true gap. The star column bounds the oscillation used in (24).

| beta | Lower bound on gap / c_K | Upper bound on star oscillation |
|---:|---:|---:|
| 0.00348 | 1.9432463407 | 0.0182146372 |
| 0.01 | 1.8304134695 | 0.0783461218 |
| 0.02 | 1.6357816691 | 0.2568733234 |
| 0.04 | 1.0744562646 | 1.3021749414 |
| 0.046875 | 0.5000000000 | 3.1875000000 |

The older project window was approximately 0.00496738 under the retained normalization. Equation (22) supplies a separate all-orders derivation on the stated bipartite SU(2) graphs over a larger interval. It does not retroactively re-prove every archived cluster or block statement. The small-graph rational Schur certificates remain much sharper for their specified finite geometries and couplings, including beta = 3 on the cube.

All rounding in this table is backed by rational square-root witnesses in `uniform_gap_audit.json`. An upper endpoint appearing in an audit interval encloses the **formula for the lower bound**; it must not be read as an upper bound on the true lattice gap.

## 9. An infinite-volume ground-transform realization at fixed spacing

This section constructs a limited but explicit infinite-volume object, rather than assuming convergence of continuum Hamiltonians. Fix \(c_K>0\), a lattice spacing, and

\[
|\beta|<3/64.
\]

Let the infinite spatial lattice be \(\mathbb Z^3\), with its checkerboard link orientation and its elementary square plaquettes. Exhaust it by finite open boxes \(\Lambda\). For each box use the actual vacuum constructed above, and extend

\[
d\nu_\Lambda=Z_\Lambda^{-1}e^{-W_\Lambda}dU_\Lambda
\]

to the other links by independent Haar measure.

### 9.1 Local coefficients stabilize before taking a limit

At order \(n\), each labeled coefficient comes from connected plaquette clusters with at most \(n\) plaquettes. The operators \(K^{-1}\) and \(P_0\), when applied to a function on a finite set of links, are independent of any unused exterior Haar factors. Thus the order-n coefficients near a fixed link become identical once the box contains their n-plaquette neighborhood.

Set

\[
q=64|\beta|/3<1.
\]

Since \(\operatorname{Cat}_{n-1}\le4^{n-1}\), (16) gives the uniform tail estimate

\[
\sum_{n>N}a_n|\beta|^n
\le\frac{16|\beta|q^N}{1-q}.
\tag{25}
\]

For a fixed link and frame direction, (8) bounds the corresponding derivative tail by one third of (25). The finite-order stabilization and this uniform tail prove uniform convergence

\[
b_e^a(U)=\lim_{\Lambda\uparrow\mathbb Z^3}X_e^aW_\Lambda(U).
\tag{26}
\]

Each \(b_e^a\) is a bounded continuous function on the infinite compact product configuration space: it is a uniform limit of functions of finitely many links. It is not necessary to define the generally extensive sum \(W_\infty(U)\) itself.

### 9.2 Existence and nonzero regulated observables

The countable product configuration space is compact and metrizable. The probability measures \(\nu_\Lambda\) therefore have a weakly convergent subsequence; call its limit \(\nu\).

For any finite set \(A\) of links, the same estimate used in Section 7 bounds the conditional oscillation by

\[
\operatorname{osc}_A W_\Lambda\le\frac23|A|x_4(|\beta|)=:r_A.
\]

Consequently the conditional density, and then the marginal density on \(A\), lie between \(e^{-r_A}\) and \(e^{r_A}\) relative to product Haar measure. These measure inequalities pass to the weak limit against continuous nonnegative tests. Every finite marginal of \(\nu\) is therefore equivalent to Haar measure, with these same bounds.

In particular, a local plaquette function remains nonconstant in \(L^2(\nu)\). Its centered version has strictly positive norm. This is nontriviality of a **regulated** local observable, not continuum nontriviality.

### 9.3 Integration by parts and a closed form

For a smooth cylinder function \(f\) and a link eventually contained in the box, finite-volume integration by parts gives

\[
\int X_e^af\,d\nu_\Lambda
=\int f\,X_e^aW_\Lambda\,d\nu_\Lambda.
\]

The left-hand integrand is a continuous cylinder function. On the right, use the uniform convergence in (26), then weak convergence of the measures. Hence

\[
\int X_e^af\,d\nu=\int f\,b_e^a\,d\nu.
\tag{27}
\]

On the dense space of smooth cylinder functions in \(L^2(\nu)\), define

\[
\mathcal E(f,g)
=\sum_{e,a}\int\overline{X_e^af}\,X_e^ag\,d\nu.
\tag{28}
\]

The sum is finite on cylinder functions. The gradient into \(\bigoplus_{e,a}L^2(\nu)\) is closable. To see this, suppose \(f_j\to0\) in \(L^2(\nu)\) and \(\nabla f_j\to v\) in the direct sum. Test a component against a smooth cylinder function \(\phi\). Equation (27) gives

\[
\langle v_e^a,\phi\rangle
=\lim_j\langle f_j,-X_e^a\phi+b_e^a\phi\rangle=0.
\]

The function on the right is bounded and in \(L^2(\nu)\). Cylinder functions are dense, so every component of \(v\) vanishes. This proves closability.

The closed nonnegative form has a self-adjoint operator \(\mathcal A_\infty\) by the Friedrichs form construction. On smooth cylinder functions its expression is

\[
\mathcal A_\infty f
=-\sum_{e,a}(X_e^a)^2f
+\sum_{e,a}b_e^aX_e^af.
\tag{29}
\]

The constant function is in its kernel. Real-time unitary evolution \(e^{-itc_K\mathcal A_\infty}\) is well defined.

### 9.4 The gap passes directly through the forms

For a smooth cylinder function whose support is inside a sufficiently large box, Theorem 1 gives

\[
\sum_{e,a}\int|X_e^af|^2\,d\nu_\Lambda
\ge m\left(\int|f|^2\,d\nu_\Lambda
-\left|\int f\,d\nu_\Lambda\right|^2\right),
\]

where

\[
m=\frac12+\frac32\sqrt{1-64|\beta|/3}.
\]

Every integrand here is a continuous cylinder function, so the inequality passes to \(\nu\). It extends from cylinder functions to the closed form domain. Thus

\[
\boxed{\quad
\mathcal A_\infty\ge m(I-P_1),\qquad
P_1f=\left(\int f\,d\nu\right)1.
\quad}
\tag{30}
\]

The vacuum is unique in this weighted Hilbert space, and the excitation gap is at least \(c_Km\).

Each finite measure and the limit measure are invariant under gauge transformations supported at finitely many vertices. The form is invariant too. The corresponding gauge-invariant subspace reduces \(\mathcal A_\infty\), contains the vacuum and the nonzero centered local plaquette functions, and obeys the same gap bound.

**Theorem 2: fixed-spacing subsequential realization.** At fixed \(c_K>0\) and \(|\beta|<3/64\), at least one infinite-volume weighted ground-transform realization described by (26)–(30) exists on the spatial cubic lattice and has the stated positive gap, also in its gauge-invariant subspace.

The construction is intentionally specified as a subsequential Dirichlet-form realization. It identifies limits of the configuration vacuum measures, their local logarithmic derivatives, and their ground-transform forms. No uniqueness of the thermodynamic measure, identification with a separately prescribed quasi-local quantum representation of all electric observables, or strong-resolvent convergence on a preassigned continuum Hilbert space is asserted. Those are additional claims requiring their own proofs. In particular, this theorem is not a relativistic four-dimensional continuum construction.

## 10. What was actually audited

The proof of the uniform estimate is the analytic argument in Sections 3–6. The computations audit specific places where a normalization or recurrence error could invalidate it:

1. The rank-one coefficient of the original four-link plaquette has exact trace norm 2. The coefficient expression and direct holonomy expression agree in 1,296 rational SU(2) configurations, including genuinely noncommuting matrices.
2. Forty Catalan coefficients obey the exact scalar recurrence. The general formula is proved in (15)–(17), not inferred from these finite checks.
3. The one-plaquette logarithmic expansion is calculated through order 12 using exact character products and the electric product rule. Independently exponentiating the result yields a zero residual through order 12 in the original tridiagonal Hamiltonian equation.
4. That calculation uses the four-link Fourier norm \((n+1)^2\). Its coefficients obey the proved majorant; it reproduces \(w_1=-\chi_1/12\), \(w_2=\chi_2/2304\), and \(e_0=-\beta^2/48+O(\beta^4)\).
5. Every reported square root is enclosed by rational witnesses whose squares are compared exactly. Table rounding is outward in the required direction.
6. The previous 24 multi-plaquette rational spectral witnesses and auxiliary local-floor witnesses were rechecked and passed. Their alternate-tree integrations were already audited in the preceding bundle and were not repeated for this different theorem.

The new checker uses only the Python standard library. Its complete outputs are included. It does not check every line of an analytic proof, perform independent peer review, or establish continuum Yang–Mills by numerical computation.

## 11. Completion ledger

| Task | Status after this continuation |
|---|---|
| Finite-regulator SU(2)/SU(3) spectral certificates already supplied | Retained; 24 multi-plaquette witnesses rechecked |
| Volume-independent SU(2) strong-coupling estimate in the stated normalization | Derived, with explicit constants and an all-orders proof on the stated bipartite graphs |
| Missing higher-order star oscillation remainder | Closed by (23) |
| Proposed full star-response certificate with scale 6 | Not promoted; global influence and space-identification requirements remain |
| Infinite-volume object at fixed spacing | A subsequential weighted ground-transform form is constructed and gapped; broader representation and uniqueness claims are not asserted |
| Weak-coupling estimates along a continuum scaling trajectory | Not established |
| Nontrivial four-dimensional relativistic continuum quantum theory | Not constructed |
| Positive mass gap transferred to that continuum theory | Not proved |
| Required general compact simple gauge-group scope | Not established; this continuation is SU(2) |
| Independent Steadman constitutive law or new physical prediction | Not derived |

In conventional three-spatial-dimensional Hamiltonian normalization, \(c_K\) is proportional to \(g^2/a\) and the magnetic/electric ratio used here is proportional to \(g^{-4}\), with constants depending on the fixed trace and metric conventions [R2]. The weak-bare-coupling continuum direction therefore does not stay inside the bounded-beta interval of (1).

To finish the Clay problem one still needs a nontrivial continuum construction satisfying the required axioms, with consistent observables and physical units, and a positive gap in that theory [R3]. The new fixed-spacing uniform estimate cannot supply these missing obligations by analytic continuation alone.

RD preservation, smoothing, and task-relative efficiency remain interpretations within the existing mathematical carrier. This calculation provides an actual vacuum and excitation bound for a specified Hamiltonian; it does not show that those qualitative principles uniquely select that Hamiltonian or its continuum limit. The underdetermination examples in the earlier report remain valid.

No additional routine input from the user is needed to state these outstanding mathematical obligations. They are proof problems, not missing calculator settings or missing website inputs.

## 12. Reproduction and references

Run the self-contained exact audit:

```bash
python3 verify_uniform_gap.py
```

The output is `uniform_gap_audit.json`. The review bundle includes this note, the checker, its recorded output, a README, and a SHA-256 manifest. It is an additive companion to `Steadman_Yang_Mills_Multi_Plaquette_Review_Bundle_2026-10-09.zip`.

**[R1]** P. Eymard, *L'algèbre de Fourier d'un groupe localement compact*, Bulletin de la Société Mathématique de France 92 (1964), 181–236. [Primary paper](https://www.numdam.org/article/BSMF_1964__92__181_0.pdf). The elementary norm arguments needed here are also provided in Section 3.

**[R2]** J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, Physical Review D 11, 395 (1975). [Publisher record](https://link.aps.org/doi/10.1103/PhysRevD.11.395). The exact normalization for this project is stated in Section 2 rather than silently imported from another convention.

**[R3]** A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official problem description. [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf). The [current official problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) was checked on 11 October 2026 and still identifies the problem as unsolved.

**[R4]** D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*. [Primary preprint](https://arxiv.org/abs/math-ph/0412040). Context for established weak-perturbation gap stability. Its hypotheses are not invoked as a substitute for Sections 3–9, and no novelty claim is made here.

**Project predecessors:** `Steadman_Yang_Mills_Checked_Continuation_2026-10-08.md`, `Steadman_Yang_Mills_Research_2026-10-09.md`, and `Steadman_Yang_Mills_Multi_Plaquette_2026-10-09.md`. Recovered discussion of star blocks supplied the continuation target but was not treated as proof of an all-orders response estimate.
