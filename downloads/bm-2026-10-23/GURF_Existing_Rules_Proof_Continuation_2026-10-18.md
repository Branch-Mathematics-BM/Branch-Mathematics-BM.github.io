# GURF — Proofs and contracts for existing rules

18 October 2026 · Continuation of the BM / GURF / Steadman completeness audit

This continuation supplies explicit statements, proofs, counterexamples and quantitative bounds for eight existing GURF rule families. It adds no primitive object or physical postulate. The original audit identifiers remain the points of reference. The frozen BM Foundation and the Steadman strong-coupling freeze are unchanged.

The main mathematical correction is precise: for a finite-valued monotone potential on a lattice, the existing meet discrepancy satisfies the triangle inequality exactly when that potential is supermodular. Strict monotonicity additionally makes it a metric. A generic monotone potential does not suffice.

| Existing family | Mathematical work completed here | Application condition that still needs evidence |
|---|---|---|
| G-CommonWitness | Exact marginal-baseline bound and an unbounded width ratio | A genuinely alignment-blind comparator and the actual joint constraints |
| G-Streaming | Complete Gaussian sufficient-statistic contract, singular minimizers and deletion limits | Correct dependence, covariance, record identity and normalizers |
| G-RRR | Nonnegative deterministic minimax decomposition and stability constants | The present carrier must be derived from the retained history |
| G-ModelMorph / G-Frames | Fibre inclusion/lifting and exact kernel-transport criterion with a conditioning bound | Actual compatible maps and quantitative frame/readout bounds |
| G-JetDepth | Monotone differential defect and regular local/global descent | A fixed task, retained history and the stated rank/fibre hypotheses |
| G-AlgebraBalance / G-Nullstellensatz | Explicit exact sequences, finite-pair realization and a real-field counterexample | A common ring, valid radical convention and finite length where subtracted |
| G-Curvature / G-Functor / G-ApproxFunctor / G-RouteError | Metric characterization, exact and approximate transport bounds | A valid metric/potential, compatible maps and certified error constants |
| G-ArcOrder | Necessary Hölder exponent, writer/postprocessing rules and a sharp family | Exact factorization, admissible arcs and well-defined positive orders |

A proof under an explicit native contract can be complete while a particular physical deployment remains conditional. The audit therefore keeps the existing application entries conditional and adds separate entries for the scoped results proved here. These are internal mathematical proofs with reproducible finite checks. They are not independent peer review or a novelty determination.

## 1. Joint evidence and an alignment-blind baseline

Addresses G-CommonWitness, G-LabelledFibre and G-ImageIntersection.

Let A and B be nonempty finite sets, S a nonempty subset of A times B, and T:A times B → R a task. A joint representation retains S. The marginal summary retains only

$$p(S)=(\pi_A S,\pi_B S).$$

An alignment-blind enclosure rule E is a function of p(S) alone, required to contain T(S) for every admissible nonempty S. In this theorem the admissible family includes every nonempty subset of the common product. The rule is not allowed an additional hidden copy of the joint relation.

**Theorem 1.** The smallest such guaranteed task enclosure at the summary (A0,B0) is

$$E_{\min}(A_0,B_0)=T(A_0\times B_0).$$

For any S with those marginals,

$$T(S)\subseteq E_{\min}(p(S)).$$

**Proof.** S lies in the Cartesian product of its two projections, which proves the inclusion and sufficiency. The full rectangle A0 times B0 has the same marginal summary and is itself admissible. Any rule that is sound for every source with that summary must therefore contain its entire task image. This proves minimality. □

The conclusion is a lower bound on this precise comparator class. It makes no claim against a decoder that also receives the native joint law or a full joint likelihood.

**Quantified family.** For integer n at least 1, put

$$A_n=\{0,\ldots,n-1\},\qquad B_n=\{0,\ldots,n\},$$

$$S_n=\{(i,i),(i,i+1):0\le i<n\},\qquad T(a,b)=b-a.$$

The joint task image is {0,1}, of diameter 1. The marginal product image contains every integer from -(n-1) to n, of diameter 2n-1. Thus the ratio of guaranteed enclosure diameters is exactly 2n-1 and is unbounded.

For unrestricted real midpoint decoding under absolute error, the corresponding worst-case radii are 1/2 and (2n-1)/2. No probability law is needed. This example does not charge the storage or computation required to retain the joint relation; a cost comparison must account for those resources separately.

## 2. A fully specified streaming Gaussian sketch

Addresses G-Streaming. This is a native Gaussian model used by GURF, not a requirement to make probability primitive in BM.

Let J be a finite branch set. In branch j, the unknown parameter is theta in R to the power p_j. Record i has a known observation y_i, matrix A_ij and symmetric positive-definite covariance Sigma_ij. The covariance and matrix do not depend on theta. The conditional model is

$$y_i=A_{ij}\theta+\epsilon_i.$$

For a set S of distinct records, assume that their noises are conditionally independent given j and theta. Independent blocks may themselves have internal correlations already represented by Sigma_ij.

Define

$$M_{S,j}=\sum_{i\in S}A_{ij}^{\mathsf T}\Sigma_{ij}^{-1}A_{ij},\qquad
q_{S,j}=\sum_{i\in S}A_{ij}^{\mathsf T}\Sigma_{ij}^{-1}y_i,$$

$$\zeta_{S,j}=\sum_{i\in S}
\left[y_i^{\mathsf T}\Sigma_{ij}^{-1}y_i+\log\det\Sigma_{ij}\right],
\qquad c_S=\sum_{i\in S}d_i\log(2\pi),$$

where d_i is the observation dimension, common across branches for that record.

The log determinant is deliberately included in zeta. An equivalent convention may keep zeta purely quadratic and retain a branch-specific normalizer separately. A single common c_S cannot absorb branch-dependent determinants unless those determinants are already retained elsewhere.

**Theorem 2.** These quantities determine the complete likelihood for every j and theta:

$$-2\log L_S(j,\theta)=
\theta^{\mathsf T}M_{S,j}\theta-2q_{S,j}^{\mathsf T}\theta+
\zeta_{S,j}+c_S.$$

For disjoint conditionally independent record sets S and T, all four displayed quantities add. If a separate deterministic observation partition Pi_S is retained on a common state carrier, its parallel update is Pi_S meet Pi_T. The resulting sketch product is associative and commutative. Its partition coordinate is idempotent; its likelihood coordinates accumulate by ordinary addition.

**Proof.** Expand each residual quadratic

$$(y_i-A_{ij}\theta)^{\mathsf T}
\Sigma_{ij}^{-1}(y_i-A_{ij}\theta).$$

The quadratic, linear and constant coefficients are respectively M, -2q and the quadratic part of zeta. The Gaussian density contributes log det Sigma and d_i log(2 pi). Conditional independence makes joint log likelihood the sum. Addition is associative and commutative, as is intersection of the equivalence relations generated by the deterministic observation maps. No step identifies a hard observation partition with a Gaussian likelihood. □

**Singular parameters.** M is positive semidefinite and q belongs to its range. Indeed, if v is in ker M, the sum of the nonnegative terms

$$v^{\mathsf T}Mv=\sum_i
\|\Sigma_{ij}^{-1/2}A_{ij}v\|^2$$

vanishes, so every A_ij v is zero and v transpose q is zero. Finite-dimensional orthogonal complement therefore gives q in range M.

For an unconstrained branch parameter, every maximum-likelihood parameter is consequently

$$\theta=M^+q+v,\qquad v\in\ker M,$$

and the minimum negative twice log likelihood is

$$\zeta+c-q^{\mathsf T}M^+q.$$

A unique minimizer requires M positive definite. Hard parameter constraints can change this solution and must be imposed separately.

**Why all fields matter.** A single scalar record with A=1 and y=1 or y=-1 has the same M=1 and quadratic constant 1, but its q and maximizing parameter change sign. M does not determine the center. With A=(1,0) transpose and y=(0,a) transpose under identity covariance, M=1 and q=0 are independent of a, while the likelihood constant changes by a squared. Thus retaining M and q alone does not preserve general likelihood scores.

**Dependence counterexample.** Two scalar observations with unit variances and covariance 1/2 have joint covariance

$$\Sigma=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.$$

For A=(1,1) transpose, y=(1,1) transpose and theta=0, the true residual quadratic is 4/3. Treating the observations as independent gives 2. Disjoint record names alone do not justify independent likelihood multiplication.

**Normalization counterexample.** At y=0 and A=0, scalar noise variances 1 and 4 have identical zero quadratic statistics but likelihoods differing by a factor of 2. Either the branch normalizer or its equivalent contribution to zeta is necessary for branch comparison.

**Deletion boundary.** Numeric coordinates can be subtracted only when the removed record contributions are retained and subtraction corresponds to the original compatible model. A partition meet is generally not cancellative: meeting either the universal or the discrete partition with the discrete partition produces the discrete partition. Knowing the final meet and the removed discrete partition cannot identify which original partition was present.

## 3. Revelation, retention and reader limitations

Addresses G-RRR.

Let X be a nonempty lawful state set, T:X→Y a task, H:X→Z_H a retained history, and C=p composed with H the present carrier. Let the loss ell:Y times Y→[0,infinity) be fixed.

For an observation O, define its unrestricted deterministic minimax risk by

$$R^*(O)=\inf_D\sup_{x\in X}\ell(T(x),D(O(x))),$$

with D defined on the realized observation image. Let R be a nonempty permitted class of readers of C and put

$$R_{\mathcal R}(C)=\inf_{D\in\mathcal R}
\sup_{x\in X}\ell(T(x),D(C(x))).$$

Assume these three infima are finite. No optimizer needs to be attained for the following identity.

**Theorem 3.**

$$R_{\mathcal R}(C)
=R^*(H)+[R^*(C)-R^*(H)]
+[R_{\mathcal R}(C)-R^*(C)],$$

and all three terms on the right are nonnegative.

**Proof.** Every reader D of C is also a reader of H by composing D with p. The unrestricted H reader class can therefore reproduce every C risk, giving R^*(H) at most R^*(C). Restricting the C reader class cannot improve its infimum, so R^*(C) is at most R_R(C). The identity now follows by cancellation of the finite terms. □

The equality by itself is elementary. The factorization C=pH, reader inclusion, common loss and finite-risk assumptions establish the useful nonnegative interpretation.

**A realized finite example.** Let X={0,1,2,3}, T(x)=x, H(x)=floor(x/2), C constant, and use absolute error with real outputs. Then

$$R^*(H)=1/2,\qquad R^*(C)=3/2.$$

If the only permitted present reader returns zero, its risk is 3. The three terms are exactly 1/2, 1 and 3/2. Their sum is 3.

**Why the history condition matters.** On X={-1,1}, let H be constant and C=T be the identity task. The unrestricted risks are 1 and 0. The putative retention difference is -1. C is not a function of H; it has acquired an independent distinction. Such a system violates the theorem's retention contract rather than disproving the theorem.

**Quantitative task uncertainty.** Suppose Y is a metric space, the loss is its distance, and a second task T' satisfies

$$\sup_x d(T(x),T'(x))\le\delta.$$

For any fixed reader, its two worst-case risks differ by at most delta, by the triangle inequality in both directions. Taking infima preserves that estimate. Hence each of the three optimal risks changes by at most delta. The first decomposition term changes by at most delta and each difference term by at most 2 delta. The total restricted-reader risk still changes by at most delta; summing independent worst-case bounds for the three pieces can lose this cancellation.

A change in the observation map, reader class or loss is a different perturbation. The preceding estimate does not certify it.

## 4. Model morphisms, frame changes and conditioning

Addresses G-ModelMorph and G-Frames.

### 4.1 Exact fibres and lifting

Let F:X→Y and F':X'→Y' be observations on lawful state carriers. Let f:X→X' and u:Y→Y' satisfy

$$F'f=uF.$$

Then, for every y in Y,

$$f(F^{-1}(y))\subseteq (F')^{-1}(u(y)).$$

**Proof.** For x with F(x)=y, compatibility gives F'(f(x))=u(y). □

Equality is equivalent to the following lifting property: every target state z with F'(z)=u(y) has a preimage x under f satisfying F(x)=y. This condition is both necessary and sufficient directly from equality of the two sets.

For realized y, a convenient sufficient contract is surjectivity of f together with injectivity of u on F(X). Given z, choose x with f(x)=z. Compatibility and u(F(x))=u(y) then force F(x)=y.

Neither compatibility alone nor surjectivity of f alone supplies equality. For the latter failure, take X=X'={0,1}, f the identity, F the identity, F' constant and u constant. The target fibre has two states while each source fibre has one.

### 4.2 Exact differential criterion

Suppose now

$$F_\beta\circ G=U\circ F_\alpha,$$

where G is a differentiable local frame change with invertible derivative. At a point write

$$A=DG,\quad B=DF_\alpha,\quad C=DU,\quad E=DF_\beta.$$

The chain rule gives EA=CB.

**Theorem 4.**

$$\ker E=A\ker(CB).$$

Consequently

$$\ker E=A\ker B
\quad\Longleftrightarrow\quad
\ker C\cap\operatorname{ran}B=\{0\}.$$

**Proof.** Every target tangent has the unique form Au. It lies in ker E exactly when CBu=0. This proves the first formula. Since ker B is contained in ker(CB), equality holds exactly when no nonzero response vector in range B is killed by C. □

Full output invertibility is sufficient but stronger than necessary. Injectivity on the tangent response image is the exact requirement. A non-injective readout can create new invisible directions even if the coordinate frame is unchanged: take A the identity, B the identity on R squared and C the projection onto its first coordinate.

**Conditioning bound.** In finite-dimensional Euclidean metrics, suppose

$$\|Cw\|\ge m_C\|w\|\quad(w\in\operatorname{ran}B),\qquad m_C>0.$$

Let sigma be the least nonzero singular value of nonzero B. Then

$$\|Ev\|\ge
\frac{m_C\sigma}{\|A\|}
\operatorname{dist}(v,\ker E).$$

To prove it, substitute E=CBA inverse, use the lower response bound, then use

$$\|BA^{-1}v\|\ge\sigma\,
\operatorname{dist}(A^{-1}v,\ker B),$$

$$\operatorname{dist}(v,A\ker B)
\le\|A\|\operatorname{dist}(A^{-1}v,\ker B).$$

Thus kernel transport and stable recovery are separate assertions with explicit constants. In infinite dimensions, mere injectivity does not imply such a positive m_C: the diagonal map with entries 1/n on square-summable sequences is injective but not bounded below.

These statements concern specified model/frame/readout maps. They do not identify a coordinate change with physical time evolution or a new force law.

## 5. Retained transcripts, rank defect and lawful descent

Addresses G-JetDepth, G-LocalDef and G-RealizabilityGate.

Let the lawful source be a smooth manifold or fixed smooth stratum. Fix a C1 task T and C1 responses y_0,y_1,... on that same source. Set

$$J_m=(y_0,\ldots,y_m),\qquad
K_m(x)=\ker D J_m(x),$$

$$\Delta_m(x)=\operatorname{rank}
\left(DT(x)|_{K_m(x)}\right).$$

**Theorem 5.** K_(m+1)(x) is contained in K_m(x), and Delta_(m+1)(x) is at most Delta_m(x).

**Proof.** Differentiating the coordinate projection J_m=pi_m J_(m+1) shows that every tangent killed by the longer transcript is killed by the shorter one. The image under DT of the smaller kernel is contained in the image of the larger kernel, so its dimension cannot increase. □

The differential continuation depth is the least m with Delta_m=0 at the point under consideration, with infinity if no such m exists. It is a differential depth for a fixed task and retained transcript. It is not automatically a global exact-recovery depth or a finite-jet completeness theorem.

**Regular local descent.** Let C:V→R^p and T:V→R^q be Cr, with r at least 1. Assume C has constant rank near x and

$$\ker DC(z)\subseteq\ker DT(z)$$

throughout that neighborhood. On a smaller neighborhood of x, T has a Cr factorization through C, with a Cr decoder defined on an ambient neighborhood of the represented point.

**Proof.** Constant-rank coordinates write C(s,t)=(s,0). Shrink to a product chart with connected t plaques. The kernel condition says every t derivative of T is zero there. Integrating along coordinate segments shows T(s,t)=h(s). The function h is Cr by restriction to a fixed t slice. Extend it in target coordinates by ignoring the unused coordinates and reverse the charts. This gives the required ambient decoder. □

For a global surjective submersion C:M→N with connected fibres, the same kernel condition implies a global Cr factorization: it makes T constant on each connected fibre, and local smooth sections of C show that the induced decoder is Cr. The connected-fibre and regularity conditions are substantive.

**Counterexample to an unrestricted rank claim.** On the real line let C(t)=t squared and T(t)=t cubed. Delta_T(C;t)=0 at every point: away from zero C has trivial differential kernel, and at zero DT=0. Nevertheless C(t)=C(-t) while T(t) differs from T(-t) for nonzero t. No decoder exists on any two-sided neighborhood of zero. C fails the constant-rank hypothesis there.

Even constant rank and local descent do not remove global branch ambiguity: C(t)=(cos t,sin t), T(t)=t on the real line has trivial differential kernel everywhere, yet values separated by 2 pi share a carrier and have different tasks.

**Overwriting counterexample.** For state (a,b) and task a, retained history (a,b) is adequate. An overwritten carrier b loses the task direction. Monotonicity applies to the accumulated transcript, not every instantaneous register bearing a later time label.

## 6. Algebraic defect balance and its native realization

Addresses G-AlgebraBalance, G-PairIdeal and G-Nullstellensatz.

### 6.1 Explicit comparison maps

Work in one fixed commutative ring R. Let I be a task-difference ideal and let K be the chosen writer radical ideal. Define the already used defect module

$$D_K=(I+K)/K.$$

For writer refinement let K be contained in Khat. The natural quotient map defines a surjection D_K→D_Khat. Its kernel is

$$G=\frac{(I+K)\cap\widehat K}{K}.$$

Indeed a representative a+K maps to zero exactly when a lies in Khat. Since K is contained in both numerator terms, the displayed quotient is defined. This proves the exact sequence

$$0\longrightarrow G\longrightarrow D_K
\longrightarrow D_{\widehat K}\longrightarrow0.$$

For a subsequent coarsening with Kc contained in Khat, the same construction gives

$$0\longrightarrow E\longrightarrow D_{K_c}
\longrightarrow D_{\widehat K}\longrightarrow0,$$

$$E=\frac{(I+K_c)\cap\widehat K}{K_c}.$$

Both arrows are maps in the same module category; the symbols do not by themselves define maps between unrelated rings.

**Theorem 6.** If the displayed modules have finite length, then

$$\ell(D_{K_c})=\ell(D_K)-\ell(G)+\ell(E).$$

**Proof.** The first exact sequence gives length D_K equal to length G plus length D_Khat. The second gives length D_Kc equal to length E plus length D_Khat. Eliminate the common finite term. This uses the standard additivity of module length in an exact sequence [P1]. □

The identical class balance holds in an appropriate Grothendieck group of the module category used [P2]. A numerical difference infinity minus infinity is not authorized by that notation. Polynomial defect modules often have infinite length; a finite-dimensional count needs an additional native realization or a proved finiteness condition.

### 6.2 A complete finite-state realization

Let X be finite and P=X times X. Take R to be the product ring Q to the power P, the ring of all rational-valued functions on ordered state pairs. Encode the finite writer/task values by separating rational vectors.

At a pair (x,x'), a writer-difference generator is nonzero exactly when that writer distinguishes the pair. An ideal generated by these differences therefore contains every function supported on those distinguished pairs: multiply a nonzero generator at one coordinate by its reciprocal times the coordinate indicator. It contains no function nonzero on a writer-equal pair. Thus

$$J_W=\{f:f=0\text{ on }\operatorname{Eq}(W)\}.$$

This ideal is already radical, because the product ring is a product of fields. Consequently D_(J_W) has one one-dimensional coordinate precisely for each harmful ordered pair

$$\mathcal D_T(W)=
\operatorname{Eq}(W)\setminus\operatorname{Eq}(T).$$

Its rational vector-space dimension and its R-module length are both

$$\ell(D_{J_W})=|\mathcal D_T(W)|.$$

Adding writer V removes exactly the harmful pairs that V separates. Coarsening the enlarged writer through a deterministic map adds exactly the newly harmful pairs. The module balance becomes the exact finite identity

$$|\mathcal D_{\rm final}|=
|\mathcal D_{\rm previous}|-
|\mathcal D_{\rm removed}|+
|\mathcal D_{\rm added}|.$$

This gives an actual native model of the existing balance law. It does not assume a universally conserved scalar physical substance. Ordered pairs are used consistently; switching to unordered pairs changes every count by the same factor for these symmetric, diagonal-free defects.

### 6.3 Field and structured-descent restrictions

Over an algebraically closed field in a finite-type affine setting, the usual Nullstellensatz connects common zero sets and radical ideal containment [P3]. Over real points, ordinary radicals need not provide the same criterion.

For example, on the real line take W(t)=t cubed and O(t)=t. W is injective, so its real kernel pair is the diagonal and the task is set-theoretically recoverable. But in R[t,s],

$$J_W=(t^3-s^3),\qquad J_O=(t-s),$$

and t-s does not lie in the ordinary radical of J_W. If a positive power of t-s belonged to (t cubed-s cubed), evaluation at s=1 and a nontrivial complex cube root of unity would force a nonzero number to vanish. This contradiction proves the failure. A real zero-set criterion requires the appropriate real-radical theorem.

Even on the real line, the recovered decoder here is cube root. It is continuous but is neither a polynomial nor C1 at zero. Thus set-level adequacy, a radical certificate in its proper native field, and structured smooth/polynomial factorization remain different contracts.

## 7. When the defect discrepancy is a metric

Addresses G-Curvature, G-Functor, G-ApproxFunctor and G-RouteError.

Let L be a lattice and v:L→R a finite-valued monotone function. Retain the existing definition

$$\delta_v(A,B)=v(A)+v(B)-2v(A\wedge B).$$

Finite values are required so the differences are defined.

### 7.1 Necessary and sufficient condition

**Theorem 7.** Delta_v is a pseudometric exactly when v is supermodular:

$$v(A)+v(B)\le v(A\vee B)+v(A\wedge B)
\quad\text{for all }A,B.$$

When this condition holds, delta_v is a metric exactly when v is strictly increasing on every strict order comparison.

**Proof.** Monotonicity gives nonnegativity, symmetry is immediate, and the diagonal is zero. The triangle inequality for A,C,B is equivalent to

$$v(A\wedge C)+v(B\wedge C)
\le v(C)+v(A\wedge B). \tag{1}$$

If the triangle inequality holds, choose C=A join B. Then (1) is exactly supermodularity, proving necessity.

Conversely, supermodularity applied to A meet C and B meet C gives

$$v(A\wedge C)+v(B\wedge C)
\le v((A\wedge C)\vee(B\wedge C))
 +v(A\wedge B\wedge C).$$

The join on the right is below C and the triple meet is below A meet B. Monotonicity proves (1). This argument needs no distributive-lattice assumption.

If A is strictly below B, their discrepancy is v(B)-v(A). A metric must make this positive. Conversely, for any distinct A and B, their meet is strictly below at least one of them. Strict monotonicity then makes at least one of the two nonnegative differences in delta_v positive. □

A modular lattice valuation satisfies the required equality, so cardinality, positive weighted cardinality and finite-dimensional subspace dimension give familiar valid instances.

**Strictly monotone counterexample.** On subsets of {1,2}, set

$$v(S)=|S|+\mathbf1_{S\ne\varnothing}.$$

This function is strictly monotone. For A={1}, B={2}, C={1,2},

$$\delta_v(A,B)=4,\qquad
\delta_v(A,C)=\delta_v(C,B)=1.$$

The triangle inequality fails. Monotonicity, symmetry and positive separation alone do not license metric error propagation.

### 7.2 Exact transport and meet slack

Let Phi:L→L' be monotone, with finite monotone potentials v and v'. Write M=A meet B and

$$\mu_\Phi(A,B)=
v'(\Phi A\wedge\Phi B)-v'(\Phi M)\ge0.$$

If Phi preserves the potential on the relevant objects, then

$$\delta_{v'}(\Phi A,\Phi B)
=\delta_v(A,B)-2\mu_\Phi(A,B). \tag{2}$$

This follows by adding and subtracting twice v'(Phi M). Strict meet preservation makes mu zero and gives an isometry of discrepancies. If both discrepancies are metrics, a monotone potential-preserving transport is nonexpansive, while it need not be injective.

For a post-writer object H below both A and B, use the existing diamond terms

$$r=v(A)-v(M),\quad n=v(B)-v(M),\quad c=v(M)-v(H),$$

$$g=v(A)-v(H),\qquad e=v(B)-v(H).$$

The transformed terms satisfy

$$r'=r-\mu,\quad n'=n-\mu,\quad c'=c+\mu,
\qquad g'=g,\quad e'=e.$$

Thus a transport can change provenance classification without changing total writer gain or erasure cost. For two composable potential-preserving transports, adding and subtracting the intermediate meet potential gives

$$\mu_{\Psi\Phi}(A,B)=
\mu_\Psi(\Phi A,\Phi B)+\mu_\Phi(A,B),$$

provided preservation also holds on the intermediate meet objects.

### 7.3 Quantitative approximate transport

Now suppose

$$|v'(\Phi D)-v(D)|\le\varepsilon_v$$

on A, B, M and H, and 0 at most mu at most epsilon_meet. Define e_D=v'(Phi D)-v(D). Direct subtraction gives

$$r'-r=e_A-e_M-\mu,\quad
n'-n=e_B-e_M-\mu,\quad
c'-c=e_M-e_H+\mu.$$

Therefore

$$|r'-r|,|n'-n|,|c'-c|
\le2\varepsilon_v+\varepsilon_\wedge,$$

$$|g'-g|,|e'-e|\le2\varepsilon_v,$$

and the discrepancy has the bound

$$|\delta_{v'}(\Phi A,\Phi B)-\delta_v(A,B)|
\le4\varepsilon_v+2\varepsilon_\wedge. \tag{3}$$

For a path of N stages with the same pointwise potential budget, its total gain-plus-erasure action changes by at most 4N epsilon_v. A smaller bound needs additional cancellation or stage-dependent estimates. These are bounds between specified finite-valued defects; rank, nullity or topology jumps do not acquire a continuity modulus from this theorem alone.

### 7.4 Valid route-error propagation

Suppose a finite sequence of path replacements changes one local square at a time. At replacement j, its two local outputs have discrepancy at most epsilon_j in a genuine compatible metric, and the remaining suffix is L_j-Lipschitz on all compared states. The two final outputs for that replacement differ by at most L_j epsilon_j. Applying the triangle inequality across the finite replacement chain gives

$$d(T_pD,T_qD)\le\sum_j L_j\varepsilon_j.$$

This proves the existing route bound under a complete metric contract. If delta_v is used for d, Theorem 7 supplies the missing metric test. Infinite replacement chains additionally require appropriate convergence/completeness and summability hypotheses; those are not consequences of the finite statement.

## 8. Arc order and recovery regularity

Addresses G-ArcOrder and G-JetSpectrum.

Let W be a writer and O a task with an exact decoder O=D composed with W near a point x0. Suppose D is uniformly alpha-Hölder on the relevant writer image, with alpha positive:

$$\|D(z)-D(z')\|\le C\|z-z'\|^\alpha.$$

Consider an admissible source arc gamma(s) approaching x0. Suppose its writer and task variations have positive finite orders p and q:

$$\|W(\gamma(s))-W(x_0)\|\asymp |s|^p,\qquad
\|O(\gamma(s))-O(x_0)\|\asymp |s|^q.$$

**Theorem 8.** Every such arc forces alpha at most q/p. For a declared arc family, put Omega equal to the supremum of p/q over arcs with these well-defined orders. Then

$$\alpha\le1/\Omega.$$

If that supremum is unbounded, no positive uniform Hölder exponent is possible on this contract.

**Proof.** Exact factorization and the Hölder bound imply

$$c|s|^q\le C'|s|^{p\alpha}$$

for small nonzero s. If q were less than p alpha, division and passage to zero would contradict c positive. Apply the resulting inequality to every admissible arc and take the infimum of q/p, equivalently the reciprocal of the positive supremum of p/q. □

Adding a retained writer V gives order min(p,p_V) in the combined finite-dimensional product norm, so the obstruction ratio cannot increase. Smooth carrier postprocessing, normalized at the basepoint, is locally Lipschitz and cannot lower the writer's order; it can increase the obstruction or destroy exact factorization. A local diffeomorphic carrier reparameterization preserves the order because its map and inverse have local Lipschitz bounds.

Arcs with a constant task, a writer constant along a task-varying arc, or infinite/flat vanishing require explicit separate treatment. In particular, a writer constant on a task-varying arc already rules out exact factorization. The displayed formula is not interpreted as an undefined zero-over-zero or infinity-over-infinity ratio.

**Sharp realization.** For 1 at most q at most p on X=[0,1], take W(t)=t to the power p and O(t)=t to the power q. The decoder is D(z)=z to the power q/p. For exponent r=q/p in (0,1], subadditivity of the concave power gives

$$|u^r-v^r|\le|u-v|^r\quad(0\le u,v\le1).$$

Thus the maximum uniform Hölder exponent is exactly q/p: the theorem supplies the upper bound and this decoder attains it.

The arc inequality alone is not sufficient for recovery. On the two-sided real line, W(t)=t squared and O(t)=t meet the order bound alpha at most 1/2, but opposite nonzero t values have equal writer values and different tasks. No exact decoder exists. Restricting the source to [0,1] removes that branch collision and square-root recovery attains exponent 1/2.

## 9. Verification, provenance and remaining work

The companion Python script uses rational arithmetic and finite enumeration to check the stated finite witnesses and specializations: joint-enclosure widths, Gaussian block identities, risk decompositions, compatible fibre maps, tangent-kernel transport, retained-transcript ranks, harmful-pair balances, lattice metric conditions, transport budgets and arc-power examples. The general proofs are the written arguments above. Enumeration checks finitely many models and does not formally certify these proofs.

All eight finite-check groups passed. Selected exact run counts are below; overlapping transport counts are not added into a single headline total.

| Check | Finite cases checked |
|---|---:|
| Nonempty joint relations | 574 |
| Gaussian parameter/block cases | 175 |
| History/carrier pairs and task perturbations | 60 pairs; 4,860 perturbations |
| Compatible model squares | 1,600 |
| Frame/response/readout triples | 34,992 |
| Retained-transcript cases | 4,096 |
| Finite-pair refinement/coarsening cases | 8,192 |
| Monotone potentials on the three-generator Boolean lattice | 719 |
| Approximate pair transports | 518,400 |
| Exact rational Hölder comparisons | 6,318 |

The complete counts and outputs are recorded in the companion JSON. No observed datum, physical constant, regulator-uniform estimate or continuum construction is invented in these checks.

The original GURF encyclopedia is a lineage/source index for this continuation, especially its sections on common witnesses, MATH-017 streaming, local response rank, the risk split, model morphisms, frame covariance, pair ideals, algebraic balance, defect transport and arc order. This note reproves explicitly declared contracts. It does not reconstruct every missing historical MATH/DD transcript.

For deployment, the remaining work is to establish the actual lawful state family, comparator, dependence, parameter normalization, connected-fibre or constant-rank conditions, ring/field convention, valid potential, comparison domains and quantitative constants. The universal Steadman conservation/constitutive laws and weak-coupling/continuum Yang–Mills gates are unchanged.

### Established mathematical sources

P1. The Stacks Project, Lemma 10.52.3, module-length additivity: https://stacks.math.columbia.edu/tag/00IV

P2. The Stacks Project, Section 10.55, Grothendieck relations for finite modules: https://stacks.math.columbia.edu/tag/00JC

P3. The Stacks Project, Theorem 10.34.1, finite-type Nullstellensatz: https://stacks.math.columbia.edu/tag/00FV

These sources supply the standard algebraic ingredients identified above. The other displayed calculations and proofs are supplied in this continuation. No historical priority or external novelty is asserted.

### Reproduction files

Run `python GURF_Existing_Rules_Exact_Checks_2026-10-18.py --output GURF_Existing_Rules_Exact_Checks_2026-10-18.json` with Python 3; no third-party package is needed. The script and JSON record identify the finite inputs, checked counts, witnesses and verification scope. The updated audit register links these eight proof families while preserving the native-application obligations.

