# Gauge-invariant holonomy blocking and a controlled excitation remainder

**Steadman / Branch Mathematics research continuation — 11 October 2026**

This continuation completes the proposed **one-step blocking lemma** under
explicit finite-lattice hypotheses. It supplies a geometric blocking map, an
exact vacuum-conditioned projection, a bound on its omitted sector, a
volume-independent relative bound on the returning response, and an explicit
positive excitation margin. A separate exact calculation identifies the first
interaction induced on a coarse square.

It does **not** establish an iterated weak-coupling renormalization theorem,
construct four-dimensional continuum Yang–Mills theory, or prove its mass gap.
The previously frozen BM foundation and Steadman version declarations are not
changed. This is a mathematical research derivation for review, not an
independently reviewed completion of either universal model.

The construction combines ordinary gauge-equivariant conditional expectation,
weighted Bochner estimates, and Schur/Feshbach elimination. No novelty claim is
made for those tools. The work here is to specify a usable blocking map and
derive its constants without a global-volume interaction norm.

## 1. Normalization and the starting Hilbert space

Let the fine configuration space be

\[
 \mathcal X=SU(2)^{\mathcal E},\qquad
 K=-\sum_{e\in\mathcal E}\Delta_e.
 \tag{1}
\]

Every link has the unit-three-sphere metric. Its spin label \(n=2j\) has
electric energy \(n(n+2)\), its Ricci tensor is \(2g\), and the Lie bracket in
an orthonormal left frame satisfies \(|[a,b]|\le2|a||b|\).
Normalized product Haar measure is denoted by \(dU\).

For the SU(2) model already studied,

\[
 h=K-\beta T,\qquad T=\sum_p\tfrac12\operatorname{Tr}U_p,
 \qquad H=c_Kh.
 \tag{2}
\]

Suppose its actual positive, normalized vacuum is

\[
 \Omega=Z^{-1/2}e^{-W/2},\qquad d\nu=\Omega^2dU,
 \qquad h\Omega=e_0\Omega.
 \tag{3}
\]

The ground transform is the unitary map \(f\mapsto\Omega f\) from
\(L^2(\nu)\) to \(L^2(dU)\). It gives

\[
 L=\Omega^{-1}(h-e_0)\Omega
   =K+\sum_{e,a}(X_e^aW)X_e^a,
 \qquad
 \mathcal E(f)=\sum_{e,a}\int|X_e^af|^2d\nu.
 \tag{4}
\]

The vacuum of \(L\) is the constant function 1. Excitations are orthogonal
to 1 in \(L^2(\nu)\), rather than orthogonal to the electric vacuum in Haar
space. The form in (4), with its closed Sobolev domain, defines the operators
used below.

Assume \(W\) is real, smooth and gauge invariant and that, pointwise,

\[
 \|\operatorname{Hess}W\|_{\mathrm{op}}\le k<1,
 \qquad \max_e|\nabla_eW|\le d.
 \tag{5}
\]

These are explicit quantitative hypotheses. Relevant Distinguishability,
persistence, smoothing and efficiency by themselves do not imply (5).
Section 8 supplies \(k,d\) from the earlier strong-coupling vacuum series,
without using a previously assumed excitation gap.

## 2. The blocking map is specified geometrically

Choose \(M\) oriented paths of **two fine links each**, with no fine link
used in two different paths. The paths may meet at vertices. After inverting
link coordinates when necessary, write the variables on path \(\ell\) as
\((u_\ell,v_\ell)\), and define

\[
 q_\ell=u_\ell v_\ell,\qquad
 q:\mathcal X\longrightarrow\bar{\mathcal X}=SU(2)^M.
 \tag{6}
\]

All fine links outside the chosen paths remain in the fibre. Coordinate
inversion is an isometry, so the original fine electric metric is retained.
There is no replacement of the continuous gauge group by a finite group.

For a path from fine vertex \(s\) through \(m\) to \(t\), a fine gauge
transformation acts as

\[
 u\mapsto g_su g_m^{-1},\quad
 v\mapsto g_mv g_t^{-1},\quad
 q_\ell\mapsto g_s q_\ell g_t^{-1}.
 \tag{7}
\]

The gauge element at the middle vertex cancels exactly. The retained variables
are consequently legitimate coarse links. Product Haar measure pushes forward
to product Haar measure: change coordinates on every pair from \((u,v)\)
to \((u,q=uv)\), for which \(du\,dv=du\,dq\).

The coarse vacuum density and its log potential are defined by

\[
 d\bar\nu=q_*d\nu=e^{-\bar W(q)}d\bar U,
 \qquad
 e^{-\bar W(q)}
 =\frac{\int_{q^{-1}(q)}e^{-W(U)}d\lambda_q(U)}
        {\int_{\mathcal X}e^{-W(U)}dU}.
 \tag{8}
\]

Here \(d\lambda_q\) is normalized Haar measure in the independent fibre
coordinates, including unused fine links. The additive constant in \(\bar W\)
is fixed by normalization. Its derivatives do not depend on that constant.

Define

\[
 Jf=f\circ q,
 \qquad J^*F(q)=\mathbb E_\nu[F\mid q],
 \qquad P=JJ^*,\quad Q=I-P.
 \tag{9}
\]

Then \(J:L^2(\bar\nu)\to L^2(\nu)\) is an isometry and \(P\) is an
orthogonal projection. In particular \(P1=1\), so \(Q\) contains no vacuum
component. Gauge invariance of \(\nu\) and equivariance of \(q\) imply that
\(P,Q\) commute with fine gauge transformations. The coarse gauge-invariant
subspace maps into the fine physical subspace, and all bounds below restrict
to those subspaces.

This projection uses the **interacting vacuum measure**. Replacing it by Haar
conditional expectation at nonzero \(\beta\) would define a different
projection and would not prove the stated excitation estimates.

## 3. Exact coarse metric and a conditional omitted-sector floor

For one pair and a coarse left-frame vector \(a\), the fine horizontal
vector field which occurs in the gradient of a pulled-back function is

\[
 Z_a=(\operatorname{Ad}_v a,a).
 \tag{10}
\]

The differential of the multiplication map sends a fine tangent vector
\((\xi,\zeta)\) to \(\operatorname{Ad}_{v^{-1}}\xi+\zeta\).
It sends \(Z_a\) to \(2a\). A vertical vector has the form

\[
 V_b=(b,-\operatorname{Ad}_{v^{-1}}b),
 \qquad |Z_a|^2=2|a|^2,\quad |V_b|^2=2|b|^2,
 \quad \langle Z_a,V_b\rangle=0.
 \tag{11}
\]

Therefore the exact compressed Dirichlet form is

\[
 \mathcal E(Jf)=2\int_{\bar{\mathcal X}}|\bar\nabla f|^2d\bar\nu,
 \qquad
 A=J^*LJ=2\bigl(\bar K+
                   \bar\nabla\bar W\cdot\bar\nabla\bigr).
 \tag{12}
\]

The factor 2 is forced by the original link metric; it is not an adjustable
parameter. Formula (12) is an exact compression. It does not assert that
\(A\) alone generates the full projected time evolution.

For fixed \(q_\ell\), the pair fibre is
\(u\mapsto(u,u^{-1}q_\ell)\). Inversion followed by translation is an
isometry of SU(2). The graph of this isometry is totally geodesic in the
product, with induced metric \(2g\). Its Ricci lower bound, measured in that
metric, is 1. An unused-link factor has Ricci lower bound 2. Thus the whole
fibre is a totally geodesic product with Ricci lower bound 1.

The restriction of \(\operatorname{Hess}W\) to its tangent space is its
intrinsic Hessian. With (5), the conditional weighted Bochner estimate gives

\[
 \operatorname{Var}_{\nu_q}(F)
 \le\frac1\gamma
       \int|\nabla_{\mathrm{fib}}F|^2d\nu_q,
 \qquad \gamma=1-k>0.
 \tag{13}
\]

The conditional measure \(\nu_q\) has smooth positive density on a connected
compact product fibre. Consequently the Bochner/Poincare argument applies on
each fibre. Its constant in (13) is independent of \(M\), the number of
unused links, and the number of plaquettes.

Explicitly, for the positive conditional generator
\(L_{\mathrm{fib}}=-\Delta_{\mathrm{fib}}+
\nabla_{\mathrm{fib}}W\cdot\nabla_{\mathrm{fib}}\), integration of the
weighted Bochner identity gives

\[
 \int(L_{\mathrm{fib}}f)^2d\nu_q
 =\int\!\left(|\operatorname{Hess}_{\mathrm{fib}}f|^2+
 (\operatorname{Ric}_{\mathrm{fib}}+
       \operatorname{Hess}_{\mathrm{fib}}W)(\nabla f,\nabla f)\right)d\nu_q
 \ge\gamma\int|\nabla_{\mathrm{fib}}f|^2d\nu_q.
\]

Apply this to a nonconstant eigenfunction on the compact connected fibre to
obtain an eigenvalue at least \(\gamma\); spectral expansion gives (13).

For \(QF=F\), the conditional mean is zero. Integrating (13) and using
\(|\nabla_{\mathrm{fib}}F|\le|\nabla F|\) gives, for the restricted closed
form and its Friedrichs operator,

\[
 C=QLQ\big|_{Q L^2(\nu)}\ge\gamma I.
 \tag{14}
\]

The notation in (14) denotes form compression. It does not presuppose that
\(Q\) commutes with \(L\).

## 4. The returning response has a relative, local bound

Write \(t=(t_\ell)\) for an arbitrary coarse tangent vector at a fixed
coarse configuration. The drift which acts on pulled-back coarse functions is

\[
 b\cdot t=Z_tW,\qquad
 Z_t=\sum_\ell Z_{t_\ell},\qquad |Z_t|^2=2|t|^2.
 \tag{15}
\]

Since \(KJf=2J\bar K f\), the off-diagonal block is exactly

\[
 B=QLJ,\qquad
 Bf=\bigl(b-\mathbb E_\nu[b\mid q]\bigr)
                        \cdot\bar\nabla f(q).
 \tag{16}
\]

The vector \(\bar\nabla f(q)\) is constant along the fibre when expressed
in the coarse left frame. The conditional mean of \(b\) is
\(2\bar\nabla\bar W\), consistently with (12).

**The nonabelian connection contribution must be included.** Set
\(c=\operatorname{Ad}_{v^{-1}}b\). The Levi-Civita connection of the
bi-invariant unit-SU(2) metric gives

\[
 \nabla_{V_b}Z_a
   =\left(-\tfrac12[b,\operatorname{Ad}_v a],
           -\tfrac12[c,a]\right).
 \tag{17}
\]

For the first component, differentiate \(\operatorname{Ad}_v a\) along
the velocity \(-c\), then add \([b,\operatorname{Ad}_v a]/2\).
For the second component the frame coefficient is constant and the connection
contributes \([-c,a]/2\). This proves (17), including its signs.

For a vertical tangent \(V\) on all fibres, Cauchy–Schwarz over the disjoint
pairs, \(|[a,b]|\le2|a||b|\), and the per-link bound in (5) imply

\[
 \begin{aligned}
 |V(Z_tW)|
 &\le |\operatorname{Hess}W(V,Z_t)|
       +|\langle\nabla W,\nabla_VZ_t\rangle|\\
 &\le \sqrt2(k+d)|V|\,|t|.
 \end{aligned}
 \tag{18}
\]

Indeed the connection contribution on a pair is at most
\(2d|b_\ell||t_\ell|\); summing is at most
\(\sqrt2d|V|\,|t|\). Unused-link vertical directions have no connection
contribution. There is no summation factor equal to the total number of links.

Apply (13) to (15), then integrate (16). Define

\[
 \eta^2=\frac{(k+d)^2}{\gamma}.
 \tag{19}
\]

We obtain the covariance-matrix and operator-form bounds

\[
 \operatorname{Var}_{\nu_q}(b\cdot t)\le2\eta^2|t|^2,
 \qquad
 \boxed{\ \|Bf\|_{L^2(\nu)}^2
       \le\eta^2\langle f,Af\rangle_{L^2(\bar\nu)}\ }.
 \tag{20}
\]

This is the replacement for a global bound such as
\(\|\beta T\|\le|\beta||\mathcal P|\). It controls the actual off-diagonal
returning response relative to retained gradient energy. It does not bound an
extensive interaction by pretending its volume dependence has disappeared.

## 5. Coarse curvature is also bounded without using the fine gap

In fibre coordinates \((u,q)\), a coarse left derivative at fixed \(u\)
acts on the second fine link only. For coarse tangent \(t\), call that
fine vector field \(Y_t\). Then \(|Y_t|=|t|\).
Along a coarse geodesic, the corresponding second-link curves are fine
geodesics, while the first links and unused links stay fixed.

Differentiating (8) twice consequently gives the exact identity

\[
 \operatorname{Hess}\bar W(t,t)
 =\mathbb E_{\nu_q}\operatorname{Hess}W(Y_t,Y_t)
       -\operatorname{Var}_{\nu_q}(Y_tW).
 \tag{21}
\]

There is no variable Haar Jacobian in these coordinates. The normalization in
(8) is independent of \(q\).

On a pair, \(\nabla_{V_b}Y_a=(0,-[c,a]/2)\). Thus

\[
 |\nabla_{\mathrm{fib}}(Y_tW)|
 \le (k+d/\sqrt2)|t|\le(k+d)|t|.
 \tag{22}
\]

By (13), \(\operatorname{Var}_{\nu_q}(Y_tW)\le\eta^2|t|^2\).
Combining this with (21) gives

\[
 \operatorname{Hess}\bar W\ge-(k+\eta^2)I.
 \tag{23}
\]

Product coarse SU(2) has Ricci lower bound 2. The factor 2 in (12) scales the
generator, so weighted Bochner yields

\[
 A\ge a(I-|1\rangle\langle1|),\qquad
 a=2(2-k-\eta^2),
 \tag{24}
\]

provided \(a>0\). This estimate uses the vacuum derivative bounds, conditional
fibre coercivity, and the exact coarse metric. It does not use the original
fine gap as an input to prove that same gap.

### Form domains and the block decomposition

For smooth \(F\), differentiating its conditional average at fixed first-link
coordinates gives

\[
 \bar\nabla J^*F
   =\mathbb E_{\nu_q}[\nabla_2 F]
      -\operatorname{Cov}_{\nu_q}(F,YW).
 \tag{25}
\]

Here \(\nabla_2\) consists of the selected second-link gradients. The
covariance estimate following (22) implies
\(|\operatorname{Cov}(F,YW)|^2\le\eta^2\operatorname{Var}(F)\).
Consequently

\[
 \mathcal E(PF)\le4\mathcal E(F)+4\eta^2\|F\|^2.
 \tag{26}
\]

Thus \(P\) and \(Q\) preserve the closed form domain; smooth projected
functions are dense in their respective restricted form domains. The
off-diagonal map in (20) extends from smooth functions to
\(D(A^{1/2})\), with values in \(QL^2(\nu)\).
The matrix decomposition used next is therefore a decomposition of the
original closed form and its self-adjoint operator, not just a finite matrix
analogy.

At this finite regulator, \(A\) has compact resolvent. The form domain of
\(C\) is a closed subspace of the fine Sobolev form domain, whose embedding
in \(L^2\) is compact, so \(C\) also has compact resolvent. For every real
\(E<\gamma\),
\((C-E)^{-1/2}B(A+I)^{-1/2}\) is therefore compact. Splitting the coarse
space into finite and high spectral subspaces of \(A\) shows that
\(\Sigma(E)\) is infinitesimally form bounded relative to \(A\).
The forms \(F(E)\) below are consequently closed and semibounded on
\(D(A^{1/2})\). Retained equations may equivalently be read in their weak
form on that domain.

## 6. Blocking lemma: exact elimination and its preserved margin

Restrict to the excitation space \(1^\perp\). Identify the retained sector
with \(L^2_0(\bar\nu)\) by \(J\). The fine operator has blocks

\[
 \widehat L=
 \begin{pmatrix} A&B^*\\ B&C\end{pmatrix},
 \qquad A\ge aI,\quad C\ge\gamma I,
 \quad B^*B\le\eta^2 A.
 \tag{27}
\]

The inequalities involving \(B\) are form inequalities. If the fine physical
space is used, the same decomposition applies with retained physical coarse
states and physical omitted states.

**Theorem 1 — One-step excitation blocking.** Under (5), assume
\(a>0\) and \(\eta^2<\gamma\). Then:

1. For \(0\le E<\gamma\), the exact reduced eigenvalue equation is

   \[
    F(E)f=0,\qquad
    F(E)=A-E-\Sigma(E),\qquad
    \Sigma(E)=B^*(C-E)^{-1}B.
    \tag{28}
   \]

   A retained solution reconstructs the omitted state as
   \(h=-(C-E)^{-1}Bf\). An eigenstate below \(\gamma\) cannot have its
   retained part zero.

2. The returning self-energy is positive and obeys

   \[
    0\le\Sigma(E)\le\frac{\eta^2}{\gamma-E}A.
    \tag{29}
   \]

3. The full excitation gap has the explicit lower bound

   \[
    \boxed{\quad
    m=\frac{a+\gamma-
       \sqrt{(a-\gamma)^2+4a\eta^2}}2>0,\qquad
    \widehat L\ge mI.
    \quad}
    \tag{30}
   \]

4. For \(0\le E<\min(a,\gamma)\), the normalized coupling satisfies

   \[
    \left\|(C-E)^{-1/2}B(A-E)^{-1/2}\right\|^2
    \le\frac{a\eta^2}{(a-E)(\gamma-E)}.
    \tag{31}
   \]

   The right-hand side is strictly less than 1 for \(0\le E<m\).

**Proof.** Solving the omitted component of the block eigenvalue equation is
legitimate for \(E<\gamma\), and gives (28). Bound (29) follows from
\((C-E)^{-1}\le(\gamma-E)^{-1}\) and (20). The spectral calculus of
\(A\ge aI\) gives
\(A(A-E)^{-1}\le a/(a-E)\), proving (31).

Alternatively, completion of squares in the closed form of
\(\widehat L-E\) gives the Schur complement \(F(E)\). By (29),

\[
 F(E)\ge\left(1-\frac{\eta^2}{\gamma-E}\right)A-E.
 \tag{32}
\]

For \(E<m\), its retained lower bound is positive because
\((a-E)(\gamma-E)>a\eta^2\); that inequality also makes the coefficient
of \(A\) in (32) positive. The same completion proves
\(\widehat L\ge EI\). Passing to \(E\uparrow m\) proves (30).
The smaller root is positive exactly when \(\eta^2<\gamma\), assuming
\(a>0\). This proof applies on the full form domain by (26). □

The constants in this theorem have no volume factor. The hypothesis
\(2k+d<1\) is a convenient sufficient condition: it gives
\(k+d<1-k=\gamma\), hence \(\eta^2<\gamma\), and then
\(a>2>\gamma\).

## 7. The omitted response, its energy dependence, and state norm

The coarse compression \(A\) must not be mistaken for the exact reduced
Hamiltonian. The exact response remains \(\Sigma(E)\).
For \(0\le E<\gamma\), functional calculus gives

\[
 \begin{aligned}
 \Sigma(E)&=\Sigma_0+E\Sigma_1+R_2(E),\\
 \Sigma_0&=B^*C^{-1}B,\qquad
 \Sigma_1=B^*C^{-2}B,\\
 0&\le R_2(E)
    =E^2B^*C^{-2}(C-E)^{-1}B\\
  &\le\frac{E^2\eta^2}{\gamma^2(\gamma-E)}A.
 \end{aligned}
 \tag{33}
\]

Thus \(A-\Sigma_0-E(I+\Sigma_1)\) has a rigorously bounded remaining
quadratic response. This is an estimate of a quadratic form relative to
\(A\), rather than a claimed bounded operator remainder on all high-energy
states. Also

\[
 0\le\Sigma_0\le\frac{\eta^2}{\gamma}A,
 \qquad 0\le\Sigma_1\le\frac{\eta^2}{\gamma^2}A.
 \tag{34}
\]

For an exact retained eigenvector \(f\), reconstruction changes its norm:

\[
 \|Jf+h\|^2=\langle f,M(E)f\rangle,\qquad
 M(E)=I+B^*(C-E)^{-2}B=-F'(E),
 \tag{35}
\]

with

\[
 I\le M(E)\le I+\frac{\eta^2}{(\gamma-E)^2}A.
 \tag{36}
\]

The plus sign in this norm correction and the minus sign in the self-energy
are both retained. For sufficiently regular initial data, eliminating the
omitted component in time yields the corresponding exact identity, or its
weak form on form-domain states,

\[
 i\dot f(t)=Af(t)+B^*e^{-itC}h(0)
       -i\int_0^t B^*e^{-i(t-s)C}Bf(s)\,ds.
 \tag{37}
\]

Discarding the initial omitted state and the returning memory integral would
be an additional approximation. Nothing in (12) authorizes that omission.

## 8. Explicit SU(2) strong-coupling application

The accompanying prior note,
`reference/Steadman_Yang_Mills_Uniform_Gap_2026-10-11.md`, constructs the
finite-lattice log vacuum from the convergent linked interaction series
on a bipartite graph with simple four-link plaquettes. If each link meets
at most \(z\) plaquettes, its local electric-Fourier norm is bounded by

\[
 x_z(b)=\frac32\left(1-\sqrt{1-\frac{16zb}{3}}\right),
 \qquad b=|\beta|\le\frac3{16z}.
 \tag{38}
\]

For clarity, the source equation is
\(x=4zb+x^2/3\). The four-original-link Fourier norm of
\(\tfrac12\operatorname{Tr}U_p\) is 2, and the original link electric
energy of its fundamental character is 12. The one-group Fourier norm of a
holonomy character cannot be substituted for the original four-link norm.

That note proves the global Hessian bound \(\|\operatorname{Hess}W\|\le x_z\).
For a unit tangent on link \(e\), a representation derivative has norm at
most \(n_e\), while \(n_e\le n_e(n_e+2)/3\). Summing its local Fourier
coefficients therefore also gives \(|\nabla_eW|\le x_z/3\).
Consequently (5) holds with

\[
 k=x_z(b),\quad d=x_z(b)/3,\quad
 \gamma=1-x_z(b),\quad
 \eta^2=\frac{16x_z(b)^2}{9(1-x_z(b))},\quad
 a=4-2x_z(b)-2\eta^2.
 \tag{39}
\]

The positive-margin condition follows from

\[
 x_z(b)<\frac37
 \quad\Longleftrightarrow\quad
 b<\frac9{98z}.
 \tag{40}
\]

The inversion in (40) uses \(b=(x-x^2/3)/(4z)\). For the three-dimensional
cubic spatial lattice, \(z\le4\), and the sufficient one-step window is

\[
 |\beta|<\frac9{392}=0.022959183673469\ldots.
 \tag{41}
\]

The prior direct weighted-curvature estimate gave a stronger fine gap bound
\(2-x_4\) on the larger window \(|\beta|\le3/64\).
The present lemma is useful because it controls a specified spatial blocking
and its response. Its conservative lower gap bound is **not** an improvement
of the earlier direct gap estimate, and neither window is a critical coupling
or a weak-coupling continuum result.

The following display uses \(z=4\), even though the isolated 2×2 patch itself
has \(z=2\). The first three parameter columns are rounded displays;
the last column is an exact terminating-decimal rational lower witness.

| \(|\beta|\) | fibre parameter \(\gamma\) | coupling parameter \(\eta^2\) | coarse parameter \(a\) | certified \(\Delta(H)/c_K\) lower witness |
|---:|---:|---:|---:|---:|
| 0.00348 | 0.9432463407 | 0.0060707183 | 3.8743512448 | 0.9352438787 |
| 0.01000 | 0.8304134696 | 0.0615695243 | 3.5376878905 | 0.7522170799 |
| 0.02000 | 0.6357816692 | 0.3709309489 | 2.5297014406 | 0.2280912011 |
| 0.02290 | 0.5727534666 | 0.5665873085 | 2.0123323161 | 0.0048089254 |

The checker stores rational upper witnesses for \(x,\eta^2\), lower witnesses
for \(\gamma,a\), and positive exact values of
\((a-m)(\gamma-m)-a\eta^2\). It also runs the corresponding four cases with
the actual patch value \(z=2\). Floating point is used only for display;
the certificate decisions use `Fraction` and integer square-root isolation.

## 9. A complete geometric test: the 2×2 square

The test patch has 9 fine vertices, 12 fine links and 4 plaquettes. Retain the
four corner-to-corner boundary paths, each with two fine links, and put the
four interior spokes in the fibre. The coarse graph is one square.

At \(\beta=0\), its first physical coarse excitation is the fundamental
character of the eight-fine-link perimeter:

\[
 \psi_{\partial}=\operatorname{Tr}(q_1q_2q_3q_4),
 \qquad K\psi_{\partial}=24\psi_{\partial}.
 \tag{42}
\]

Signs are included in the oriented definitions of the four paths. Equivalently
the usual inverse-link convention may be used around the coarse square.
The earlier patch assembler retained the **complete** fine physical sector
of electric energy strictly below 24: vacuum, four face traces, and four
six-link traces. It therefore did not contain (42). Its nine-state matrix
cannot by itself test nonvacuum holonomy blocking.

The new ten-state matrix adds exactly (42). Exact degree-four Haar cubature
on the four original non-tree links reproduces every old interaction and
cross-Gram entry. Its boundary interaction row vanishes, while its magnetic
cross-Gram diagonal is 1 before multiplying by \(\beta^2\).
This enlarged basis is not claimed to be a complete cutoff at energy 24.

This is a basis test of the geometry and normalization. At nonzero coupling
the exact retained functions live in the vacuum-weighted Hilbert space;
the new Haar matrix is not substituted for that interacting projection.

## 10. The first induced coarse interaction is computed exactly

Let \(\rho_{\mathrm{coarse}}=e^{-\bar W}\) be the normalized density in (8)
for this patch. Near \(\beta=0\),

\[
 \boxed{\quad
 \rho_{\mathrm{coarse}}(q)
   =1+\frac{35}{2985984}\beta^4\psi_{\partial}(q)
           +O(\beta^6),
 \qquad
 \bar W(q)
   =-\frac{35}{2985984}\beta^4\psi_{\partial}(q)
           +O(\beta^6).
 \quad}
 \tag{43}
\]

The error notation is in the uniform norm on the fixed compact coarse
configuration space as \(\beta\to0\). This is a certified Taylor coefficient;
it is not an assertion that the displayed term dominates the finite-coupling
potential throughout the window (41).

### Derivation of the coefficient

Use intermediate Haar normalization for the positive eigenfunction,
\(\Phi=1+\sum_{n\ge1}\beta^n\phi_n\), with
\(\int\phi_n dU=0\). Its squared, normalized density is the same as that of
\(\Omega\). Each potential insertion is \(\chi_1(U_p)/2\).

A centre flip on a boundary fine link of any given face implies that a
fundamental perimeter character can only arise if each of the four faces is
inserted an odd number of times. Each face owns two boundary links which no
other face touches. Thus the first possible order is four, and every minimal
path inserts each face exactly once. Ground-energy counterterms and
normalization corrections have no perimeter component at this order.

For a subset \(S\) of faces, let \(\partial S\) be its original-link
centre-parity boundary and let

\[
 k(S)=3|\partial S|.
 \tag{44}
\]

When an interior link has already been used by both its incident faces, its
non-singlet component can be projected out: no remaining insertion on a
minimal path touches that link, the Haar-singlet projection commutes with
\(K\), and the final perimeter observable is independent of it. This is a
projection for calculating this coefficient, not a removal of those states
from the full Hamiltonian.

After these projections the remaining function has fundamental electric
label on each boundary link and zero label on projected links. Even when
two opposite faces touch at the central vertex, their chosen singlet
intertwiner does not change the electric eigenvalue. The function is an
eigenfunction of \(K\) with eigenvalue (44).

The coefficients for minimal paths therefore obey the exact finite recursion

\[
 D(\varnothing)=1,\qquad
 D(S)=\frac1{2k(S)}\sum_{p\in S}D(S\setminus\{p\}).
 \tag{45}
\]

For this square the values are

| face subset | electric eigenvalue | \(D(S)\) |
|---|---:|---:|
| one face | 12 | \(1/24\) |
| two adjacent faces | 18 | \(1/432\) |
| two opposite faces | 24 | \(1/576\) |
| three faces | 24 | \(11/82944\) |
| all four faces | 24 | \(11/995328\) |

Integrating the product of the four face characters over the interior spokes
at fixed retained boundary gives

\[
 \mathbb E_{\mathrm{Haar}}\!left[
        \prod_{p=1}^4\chi_1(U_p)\mid q\right]
       =\frac18\psi_{\partial}(q).
 \tag{46}
\]

For example, fix one interior spoke by its central-vertex gauge transformation,
then successively use matrix-element orthogonality on the other three to merge
the four faces. Each merge contributes \(1/2\). This preserves the actual
continuous SU(2) integral. The scalar integral of (46) against
\(\psi_{\partial}\) is also independently checked by exact Haar cubature.

Splitting the four insertions between the two wavefunction factors yields

\[
 [\beta^4\psi_{\partial}]\rho_{\mathrm{coarse}}
 =\frac18\sum_{S\subseteq\{1,2,3,4\}}
                 D(S)D(S^c)
 =\frac{35}{2985984}.
 \tag{47}
\]

The perimeter wavefunction coefficient itself is
\(D(\{1,2,3,4\})/8=11/7962624\); using twice this number for the density
would omit the cross terms in (47).

A centre flip on two appropriately chosen unused interior links changes the
sign of **every** face character while leaving all retained pair holonomies
fixed. Uniqueness of the positive vacuum then implies that the coarse density
is even in \(\beta\). There is no order-five term. There is also no order-two
nonconstant coarse term: a perimeter fundamental character needs four face
insertions, and higher perimeter representations need still more insertions.
The analytic finite-lattice vacuum series supplies the uniform Taylor remainder.
Taking its logarithm proves the second formula in (43).

### A separate matrix check of the coefficient

The checker also assembles a 16-state basis indexed by all face subsets:
vacuum; face loops; adjacent-pair six-link loops; opposite-pair products;
three-face eight-link loops; and the full perimeter. All its states have norm
1, and distinct subsets have distinct original-link centre parity. Their
electric eigenvalues are (44).

It integrates both the potential matrix and the perimeter-observable matrix
exactly, then runs ordinary matrix Rayleigh–Schrodinger recursion to order
four. It reproduces the old nine-state interaction matrix and returns exactly
\(11/7962624\) for the perimeter wavefunction coefficient and
\(35/2985984\) for the perimeter density coefficient. The minimal-path
projection argument above is what makes these two coefficients valid for the
full Hamiltonian.

The 16-state Ritz system is not a complete electric cutoff. It does not certify
its other Taylor coefficients as coefficients of the full Hamiltonian.
In particular, additional intertwiner states and higher link representations
must be kept when their paths can return to the observable being calculated.

## 11. What has and has not been completed

The specific one-step task is now concrete:

- The retained variables are products on specified disjoint two-link paths.
- The projection is conditioned on the actual interacting vacuum.
- Gauge symmetry and the excitation/vacuum separation are exact.
- The compressed metric is calculated rather than guessed.
- The omitted floor \(\gamma\), relative drift response \(\eta^2\), coarse
  margin \(a\), and preserved fine margin \(m\) are explicit.
- Equations (29), (33), and (36) bound the self-energy, its remaining energy
  dependence, and the reconstructed norm.
- A many-plaquette calculation supplies an exact induced coarse coefficient
  rather than assuming that a coarse plaquette has the original coupling.

These statements have analytic proofs in this note and accompanying
arithmetic checks. They have not been independently peer reviewed.

The obstacle is now more precise. The coarse density, the coarse compression,
and the exact energy-dependent reduced operator are different objects:

\[
 \boxed{\quad
 q_*\nu\ \longrightarrow\ A,
 \qquad
 \text{full projected spectrum}\ \longrightarrow\ A-\Sigma(E).
 \quad}
 \tag{48}
\]

Iterating the first arrow alone does not iterate the full quantum Hamiltonian.
One must propagate the response and norm corrections, as well as the induced
multi-loop interactions. The estimates in (5) and (39) are strong-coupling
estimates; they have not been established along a continuum bare-coupling
trajectory. The first induced coefficient (43) does not furnish that
trajectory.

To turn this lemma into a continuum argument, the remaining proof obligations
are:

1. **Closed renormalized dynamics:** carry exact response kernels, induced
   operators and state metrics through subsequent blocks, or prove a controlled
   representation of them in a specified operator class.
2. **Uniform physical margins:** after the prescribed energy/length rescaling,
   prove retained and omitted excitation floors above a fixed physical target,
   and a relative coupling strictly below the corresponding Schur margin at
   every scale. A finite number of positive one-step estimates cannot supply
   this.
3. **Control of accumulating error:** a summable sequence of suitably
   normalized losses would be a useful sufficient mechanism in an appropriate
   iterative theorem. Summability alone is not such a theorem and does not
   establish items 1 or 2.
4. **Continuum construction:** construct nontrivial gauge-invariant observables,
   their continuum correlations and a vacuum/Hilbert-space realization with
   the required axioms and energy normalization. Establish the gap in that
   constructed theory, rather than transferring it to an unspecified limit.
5. **Steadman constitutive content:** derive the quantitative response bounds
   from the model's stated dynamics, or supply a testable constitutive law.
   RD language by itself still does not select a unique Hamiltonian or prove
   those bounds.

The general theorem indicates a mathematical route around the former global
volume norm: estimate **conditional fibre coercivity and mixed drift
fluctuations**. This works for the present one-step strong-coupling model.
What remains open is extending that mechanism, with an exact dynamical
description, through the weak-coupling scales needed for continuum Yang–Mills.

## 12. Reproducibility and provenance

Run `python3 verify_blocking.py` with NumPy installed. The script creates
`blocking_audit.json`, `patch_boundary_matrices.json`, and
`patch_filling_basis_matrices.json`.

The checks include:

- 216 exact quaternion/Lie-frame checks of the cometric, orthogonality and
  nonabelian connection in (17).
- 1,024 exact coarse gauge-covariance comparisons, including noncommuting
  test configurations. These regression checks supplement the algebraic proof
  (7); sampling is not its proof.
- Exact original-link degree-four Haar cubature on 331,776 non-tree-link
  configurations for the enlarged boundary basis and the filling basis.
  The finite tetrahedral group is a proved integration rule at the required
  degree, not a substituted gauge group.
- Independent subset recursion, 120 ordered-path/split terms, and the
  separately integrated 16-state Ritz calculation of (47).
- Eight exact rational Schur-margin witnesses using \(z=2\) and \(z=4\).

`reference/` contains the unchanged earlier assembler, its single-plaquette
helper, original patch matrix data, and the prior uniform-gap derivation and
checker. Source hashes are included. The earlier entire 24-case certificate
suite was not rerun for this continuation: only the relevant patch data were
reconstructed and compared, because no old certificate code was changed.

The checks do not mechanically prove the analytic lemma, establish convergence
of an iterated renormalization scheme, or check a four-dimensional continuum
limit. The proof obligations and test coverage are kept distinct.

Primary background references, not substitutes for the derivations above:

- J. Kogut and L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge
  theories*, Physical Review D 11 (1975), 395.
  <https://doi.org/10.1103/PhysRevD.11.395>
- G. Dusson, I. M. Sigal and B. Stamm, *The Feshbach–Schur map and perturbation
  theory* (2021). <https://arxiv.org/abs/2105.02058>
- A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official problem
  description. <https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>

This note is additive to the September freeze, October continuation, and the
finite-lattice certificates. It does not declare a solved Millennium problem
or a new universal Steadman version.
