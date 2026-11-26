# BM: continuous closure and completion work

20 October 2026. Research Edition continuation. The frozen V1 foundation is unchanged.

This note continues the unresolved contracts recorded on 19 October. It does not use a change of definitions to declare the research program complete. Proofs below are mathematical arguments, not independent peer review or proof-assistant certification. Historical novelty has not been established.

## 1. Removing the polynomial restriction in the three-state Jordan problem

### BM20-J1. A continuous scalar factor has an ordered, invertible refinement

Let U be a homeomorphism of R^n. Let R:R^n→R be continuous, and suppose a single-valued F on I=R(R^n) satisfies R U=F R. There are an interval J⊆R, continuous maps q:R^n→J and p:J→I, and a monotone homeomorphism g:J→J such that

\[
R=pq,\qquad qU=gq.
\]

The refinement retains the entire past of R in the sense that

\[
q(x)=q(y)\quad\Longleftrightarrow\quad
R(U^{-k}x)=R(U^{-k}y)\ \text{for every integer }k\ge0.
\]

This is an existence result for a continuous scalar coordinate. It does not give a finite-precision algorithm for constructing that coordinate, and it does not assert that F itself is injective or monotone.

**Proof.** A constant R is immediate. Otherwise I is a nondegenerate interval. First F is continuous: for any y∈I, join preimages of values bracketing y by a compact path in R^n. Nearby values have preimages on this path; compactness, continuity of R U, and the single-valued factor identity show that F(y_j)→F(y) whenever y_j→y. At an included endpoint, use a path from a preimage of that endpoint to a preimage of an interior value. Invertibility of U makes F onto I.

Form the history map

\[
H(x)=(R(x),R(U^{-1}x),R(U^{-2}x),\ldots)
\]

with its product topology, metrized by

\[
d(z,w)=\sum_{k\ge0}2^{-k-1}\min\{1,|z_k-w_k|\}.
\]

The map H is continuous. For each closed Euclidean ball B_m of integer radius m≥1, let K_m=H(B_m). These are nested compact connected metric spaces. Each is locally connected: a ball is a continuous image of [0,1], and so is K_m; the Hahn–Mazurkiewicz characterization applies.

If K_m is nondegenerate, it is also arc-like. Indeed, projection to coordinate N has an interval image. Two histories with equal Nth coordinate have equal coordinates 0,…,N, because z_k=F^{N-k}(z_N). Its fibers therefore have diameter at most 2^{-N-1}. For all sufficiently large N the image interval is nondegenerate, and rescaling it gives arbitrarily small-fiber continuous surjections onto [0,1]. A locally connected, arc-like metric continuum is an arc. These two classical continuum-theory facts are the only imported topological ingredients; see [Nadler1999, §1] and [Bankston2019, §6; reference 26, Chapter XII].

Consequently each K_m is an arc or a point. Orient the nested nondegenerate arcs consistently. Parameterize the first one by a real compact interval and extend the parameterization over any additional end pieces of each larger arc. The extensions agree on previous arcs. Their union gives a bijection θ:H(R^n)→J onto a real interval, whose restriction to each K_m is a homeomorphism. (One can give each newly added nonempty end piece length one.) Set q=θH and p=π_0θ^{-1}.

Both maps are continuous. For q, every point of R^n has a neighborhood in some B_m, where the composition is continuous. For p, any point of J and a sufficiently small one-sided or two-sided interval neighborhood lie in one of the parameter intervals θ(K_m). Thus continuity follows from the corresponding arc parameterization.

On histories the shift

\[
G(z_0,z_1,\ldots)=(F(z_0),z_0,z_1,\ldots)
\]

is a homeomorphism of H(R^n), with inverse deleting the first coordinate, and H U=G H. Each G(K_m) is an arc contained in some K_M, since U(B_m) is compact. It preserves or reverses the order on that arc. Consistency on nested arcs shows that g=θGθ^{-1} is globally increasing or decreasing. It is onto J, so it is a homeomorphism of the interval. The factor identities and equality-of-histories characterization follow directly. ∎

### BM20-J2. Mutual long returns cannot separate scalar closed codes

Under BM20-J1, suppose x_j→x and U^{2m_j}x_j→y, while y_j→y and U^{2n_j}y_j→x, where m_j,n_j are nonnegative integers. Then R(x)=R(y); in fact q(x)=q(y).

**Proof.** The map f=g² is increasing. If q(x)<q(y), choose z strictly between them. If f(z)≥z, the upper interval {v:v≥z} is forward invariant; the sequence starting near q(y) cannot have endpoints converging below z. If f(z)≤z, the lower interval {v:v≤z} is forward invariant; the sequence starting near q(x) cannot end above z. One of these two cases always holds, giving a contradiction. Reverse the roles if q(y)<q(x). ∎

Using even iterates is essential here because g can reverse order. The proof allows F to be noninjective; that is exactly the case not covered by a direct interval-homeomorphism argument.

### BM20-J3. Exact continuous n=3, d=1 Jordan trajectory optimum

Let

\[
\dot x_1=\varepsilon x_2,\quad
\dot x_2=\varepsilon x_3,\quad
\dot x_3=0,\quad \varepsilon\ne0.
\]

Require a globally continuous scalar encoder R with exact sampled autonomy RΦ_h=F R on all R³, for one h>0. Measure worst-case error over the initial Euclidean unit ball, and allow any decoder of the complete output trajectory x_1(t), 0≤t≤T.

Every such R satisfies

\[
\boxed{R(a,b,0)=R(a',-b,0)\quad\text{for all real }a,a',b.}
\]

**Proof of the boundary identity.** Put τ_m=2mεh and

\[
c_m=\frac{2(a'-a-\tau_m b)}{\tau_m^2},\qquad
x_m=(a,b,c_m).
\]

Then x_m→(a,b,0), while the exact flow identity gives

\[
\Phi_h^{2m}x_m
=\left(a',-b+\frac{2(a'-a)}{\tau_m},c_m\right)
\longrightarrow(a',-b,0).
\]

Repeating the same construction with the endpoints exchanged supplies the reverse return. BM20-J2 proves the claim. Negative ε causes no problem: τ_m tends to negative infinity, while the number of forward sampled updates remains 2m. ∎

In particular the two unit-ball states (a,b,0) and (−a,−b,0) always have the same code. Their trajectories are opposite, so the triangle inequality for any common decoded trajectory gives error at least ||a+εtb||. Maximizing over a²+b²≤1 and using R(x)=x_3 with decoder ε²t²R/2 for the upper bound proves, for every 1≤p≤∞,

\[
\boxed{E^{\mathrm{closed,cont}}_{p,T}(3,1)
=\sup_{a^2+b^2\le1}\|a+\varepsilon tb\|_{L^p(0,T)}.}
\]

For p=2, set s=εT. The exact value is

\[
\boxed{E^2=\frac T2\left[1+\frac{s^2}{3}
+\sqrt{\left(1-\frac{s^2}{3}\right)^2+s^2}\right].}
\]

For p=∞ it is √(1+s²), since sup over unit (a,b) and sup over t commute and ||(1,εt)|| is largest at t=T. The p=2 value at ε=T=1 is √((4+√13)/6), approximately 1.1258738292.

This removes the polynomial and first-integral restrictions from BM18-J2. It resolves the first interior case of the original continuous contract. It does not classify all n,d.

## 2. A nonlinear code that strictly improves on every closed linear code

### BM20-J4. The closed linear trajectory formula is not universal

Consider the four-state chain with ε=T=1. Write x=(a,b,c,d), and let

\[
I(x)=c^3-3bcd+3ad^2,\qquad R_\eta(x)=d+\eta I(x).
\]

The polynomial I is a first integral: differentiating with a'=b, b'=c, c'=d, d'=0 gives 3c²d−3(c²d+bd²)+3bd²=0. Hence R_η is a globally continuous, exactly autonomous scalar code, with F=id. Use the trajectory decoder D(z)(t)=t³z/6.

For every sufficiently small η>0 this code has strictly smaller worst-case L²[0,1] error on the unit ball than every closed linear scalar code. An explicit certified choice is η=1/300000.

**Proof with an explicit margin.** Define A(a,b,c)=a+tb+t²c/2 and v(t)=t³/6. The residual is Ax_{1:3}−ηI(x)v. Put

\[
M=A^*A=\begin{pmatrix}1&1/2&1/6\\1/2&1/3&1/8\\1/6&1/8&1/20\end{pmatrix},
\quad k=A^*v=(1/24,1/30,1/72),\quad\|v\|^2=1/252.
\]

Let λ be the largest eigenvalue of M, and w its positive unit eigenvector, extended by zero in the fourth coordinate. The matrix has strictly positive entries, so λ is simple and w is strictly positive. The best closed linear scalar squared error is λ.

For the following elementary rational estimates, write w=(w_1,w_2,w_3,0). Componentwise row comparison gives w_1≥w_2≥w_3. The vector (1,1/2,0) gives λ≥19/15, while tr M=83/60. Thus the gap to the next eigenvalue of diag(M,0) is at least 2(19/15)−83/60=23/20>1. The eigenvector equations give

\[
\frac{w_2}{w_1}\le\frac{60}{97},\qquad
\frac{w_3}{w_1}\le\frac{1/6+(60/97)/8}{19/15-1/20}<\frac{21}{100}.
\]

The sum of the squares of these ratio bounds, plus one, is less than 36/25. Therefore w_1>5/6, and w_3≥w_1/(6λ)>25/249>1/10. Consequently

\[
B(w):=I(w)\,k\cdot w_{1:3}=w_3^3 k\cdot w_{1:3}>1/28800=:b_0.
\]

On the unit ball, |I|≤7, ||∇I||≤√135<12, and ||k||<1/16. Hence B(x)=I(x)k·x_{1:3} has Lipschitz constant less than 2, and C(x)=I(x)²/252<1/5. Both B and the squared residual are even, so replace x by −x if necessary to arrange α=x·w≥0. With z=x−αw and r=||x−w||, the gap estimate gives

\[
\lambda-\|Ax_{1:3}\|^2
\ge 1-\alpha^2\ge r^2/2.
\]

The first inequality follows more explicitly from λ(1−||x||²)+(λ−λ_2)||z||²≥(1−||x||²)+||z||²=1−α². The second follows from ||x||≤1 and 0≤α≤1.

Therefore

\[
\begin{aligned}
\|Ax_{1:3}-\eta I(x)v\|^2
&\le\lambda-r^2/2-2\eta(b_0-2r)+\eta^2/5\\
&\le\lambda-2b_0\eta+9\eta^2.
\end{aligned}
\]

The last line maximizes −r²/2+4ηr, whose maximum is 8η². At η=1/300000,

\[
2b_0\eta-9\eta^2>10^{-10}.
\]

Thus the new squared worst-case error is at most λ−10^{-10}, strictly below the optimum λ of the entire closed linear scalar class. Every step is an exact inequality; a floating-point optimization is not being used as a certificate. ∎

The margin is deliberately conservative. This result refutes an unrestricted extension of the linear optimum formula. It does not compute the exact nonlinear n=4,d=1 optimum.

## 3. Exact finite causal synthesis without an output catalogue

### BM20-C1. Invariant-cover criterion for finite causal prediction

Let X be any state set, with a finite alphabet of deterministic partial actions f_a, task τ:X→Y into a metric space, and a nonempty initial set I⊆X. A deterministic predictor has finitely many states q, a fixed output y_q at each state, deterministic partial updates g_a, and an initialization map I→Q. The predictor receives the action sequence, with no further observation of the native state. Require matching action availability and error at most ε at every time on every legal history.

Such a predictor with at most m states exists if and only if there are at most m nonempty sets C_q⊆X, outputs y_q, and successor choices g_a(q) satisfying:

1. I⊆∪_q C_q.
2. Every x∈C_q has the same enabled-action set as q.
3. For each enabled action, f_a(C_q)⊆C_{g_a(q)}.
4. d(τ(x),y_q)≤ε for every x∈C_q.

If an exact legacy label must also be retained, require it to be constant on each C_q. These sets may overlap: the same native state can accompany different predictor states after different histories.

**Proof.** A cover gives an initialization by selecting a containing cell. Induction on history length preserves membership, matching availability, and the output bound. Conversely, from a successful predictor take C_q to be the set of native states actually paired with q over all initializations and finite legal histories. Remove empty cells. Availability, successor containment and the output bound hold by construction. ∎

For a predictor that must be a function of the current native state alone and close exactly, the criterion is the same with the C_q forming a partition of the reachable carrier. This extra restriction is substantive; overlapping covers and partitions can have different optima.

The criterion is a specialization of established simulation-relation methodology, not a claim to have invented approximate simulation; compare [Tabuada2008]. For an infinite X it is an exact semantic criterion, not a general finite algorithm.

### BM20-C2. Exact rational minimum-ball certificates

For a nonempty finite set P⊆Q^p, a smallest Euclidean enclosing ball has rational center c and rational squared radius ρ². There is an affinely independent support {z_0,…,z_k}⊆P, k≤p, and nonnegative rational weights w_i summing to one such that

\[
c=\sum_i w_i z_i,\qquad \|z_i-c\|^2=\rho^2,
\qquad \|z-c\|^2\le\rho^2\ (z\in P).
\]

These equalities and inequalities certify optimality exactly.

**Proof.** The maximum distance is continuous and coercive, so a minimizing center exists. That center lies in the convex hull of the points attaining the maximum: otherwise strict separation gives a direction that decreases all active distances, and a sufficiently small step also preserves the slack of the other finitely many points. Reduce a convex combination to an affinely independent one by removing an affine dependence while keeping weights nonnegative.

Put u_i=z_i−z_0 and c=z_0+Σ_{i=1}^k α_i u_i. Equal squared distances give the nonsingular rational Gram system

\[
\sum_j (u_i\cdot u_j)\alpha_j=\|u_i\|^2/2.
\]

Its solution and c are rational, with w_0=1−Σα_i and w_i=α_i. Conversely, for any proposed center v the displayed support certificate gives

\[
\sum_i w_i\|z_i-v\|^2=\rho^2+\|c-v\|^2\ge\rho^2.
\]

Some support point is therefore at least distance ρ from v. Together with containment, this proves optimality. Enumerating supports of size at most p+1 finds such a certificate. ∎

This is standard minimum-enclosing-ball geometry, with the proof included to make the exact implementation auditable; see also [Welzl1991]. Squared radii are rational; the radii themselves need not be.

### BM20-C3. Globally optimal finite synthesis, all real outputs and all horizons

For a finite deterministic partial-action system with rational Euclidean task coordinates, the following algorithm computes the exact optimum for every predictor-state budget up to a supplied m:

1. Restrict to the native states reachable from I.
2. Enumerate every nonempty subset with uniform action availability and, if specified, uniform legacy label. Compute its minimum-ball certificate by BM20-C2.
3. Enumerate families of at most m distinct such subsets. Check initial coverage and successor containment from BM20-C1.
4. Minimize the largest squared cell radius. Return a realizing transition table, initialization, outputs, and the cell certificates.

Use disjoint full covers in step 3 for the exactly closed current-state encoder variant.

**Proof.** Each accepted cover supplies a valid infinite-horizon predictor. Conversely, the reachable-pair cells of any predictor are among the enumerated subsets. Replacing its outputs with their minimum-ball centers cannot increase the error. Duplicate cells can be removed: retain one copy, and choose any successor cell containing each required image. Thus distinct-subset families suffice. Enumeration attains the global optimum, including optimization over all real output vectors, by BM20-C2. The singleton native-state model gives zero error with at most |Reach(I)| states. ∎

If n states are reachable, there are at most 2^n−1 candidate cells and at most Σ_{j≤m} binom(2^n−1,j) distinct families. This is an exact exponential reference algorithm, not an efficient general implementation. It closes the finite deterministic, Euclidean-output contract; it does not establish finite realizability for every infinite carrier or satisfy unspecified physical and continuity constraints.

**Concrete distinction between history and current-state encoding.** Take states 0,1,2,3, one update (3,1,1,2), and scalar task values (2,2,3,0). With two predictor states, the overlapping cells {0,1,2} and {1,3}, outputs 5/2 and 1, and alternating updates have worst-case error 1. The exact optimum among closed current-state encoders using at most two states is 3/2. The supplied exact solver checks both optima. The shared state 1 can legitimately occur in either predictor cell as the predictor alternates; its task value 2 stays within both error bounds.

These optima also have short direct lower bounds. If ε<1, no cell containing state 3 can contain any of states 0,1,2. Two cells would therefore have to separate {3} from {0,1,2}, but the latter's update image contains both 3 and 1, which cannot fit in either cell. Thus history-based error is at least 1. For a closed two-state quotient, the image of native state 1 is fixed. In a two-state map every state that eventually reaches that fixed state does so in at most one step. Consequently native states 1,2,3 must share its code. Their task values range from 0 to 3, giving error at least 3/2, attained by the constant output 3/2.

## 4. Sharp finite-dimensional recovery results beyond qubits

Use the original unamplified operator-norm recovery error δ_A and normalized error-space defect κ_A from BM18-Q1. No diamond-norm lower bound is substituted for δ_A.

### BM20-Q1. Sharp universal error ceiling for every finite observable algebra

Write a unital finite-dimensional observable algebra, up to unitary equivalence, as

\[
A=\bigoplus_{j=1}^s (M_{n_j}\otimes I_{m_j}),
\qquad r=\sum_j n_j.
\]

Then every channel admits a recovery with

\[
\boxed{\delta_A\le 2(1-1/r).}
\]

The ceiling is attained by a completely erasing channel. For r=1 it is zero. Multiplicity factors m_j do not count as additional independent observables.

**Proof.** On M_r let P(X)=X−tr(X)I/r. For r≥2 its induced operator norm is 2(1−1/r), including non-Hermitian inputs. To see this, dualize a matrix coefficient:

\[
\|P\|=\sup_{\|u\|=\|v\|=1}
\|vu^*-(u^*v)I/r\|_1.
\]

After removing a scalar phase, let c=|u^*v|∈[0,1]. In the span of u and v, the two singular values of the rank-one-minus-scalar matrix have sum one: the sum of their squares is 1−2c²/r+2c²/r², and twice the absolute determinant is 2c²(r−1)/r². The other r−2 singular values are c/r. The trace norm is therefore 1+(r−2)c/r≤2−2/r. The coincident-vector and orthogonal-vector cases follow by the same formula or by continuity. The Hermitian contraction I−2|u⟩⟨u| attains the upper bound.

Represent the abstract direct sum ⊕M_{n_j} faithfully on C^r; this preserves its operator norm. A constant recovery output can implement its normalized trace functional tr_r/r, for example with physical state ⊕_j I_{n_jm_j}/(r m_j). Its error is the restriction of P, proving the ceiling.

For an erasing channel every recovery is a constant state σ. Choose r mutually orthogonal minimal projections of the abstract algebra that sum to I. At least one, e, has tr(σe)≤1/r. On X=I−2e the reconstruction error has norm at least 2(1−tr(σe))≥2−2/r. The ceiling is therefore exact. ∎

Together with BM18-Q1 this improves the stated general bound to

\[
\delta_A\le\min\{2(1-1/r),\ 2\sqrt{\min(d,k^2)\kappa_A}\},
\]

where d is the logical dimension and k is the number of Kraus operators in the chosen representation. The symbol r in this section is the abstract algebra rank, not Kraus rank.

### BM20-Q2. Complete normalized-defect envelope for the full matrix algebra

For A=M_d, d≥2, the possible pairs are exactly

\[
(\kappa,\delta)=(0,0),\qquad
\kappa=2,\quad 0<\delta\le 2(1-1/d).
\]

**Proof.** BM18-Q2 gives κ∈{0,2}. Exact recovery is equivalent to κ=0, and the recovery minimum is attained because finite-dimensional CPTP maps form a compact set and the objective is continuous. Thus κ=2 implies δ>0. BM20-Q1 supplies the upper endpoint.

Every positive value up to that endpoint is realized by a depolarizing channel

\[
N_\lambda(\rho)=\lambda\rho+(1-\lambda)I\operatorname{tr}(\rho)/d,
\qquad0\le\lambda<1,
\]

for which

\[
\delta=(1-\lambda)\,2(1-1/d),\qquad\kappa=2.
\]

To prove optimality, twirl a candidate recovery under all unitary conjugations. Convexity and unitary invariance of the objective, and covariance of N_λ, show that twirling cannot increase the error. The resulting channel is depolarizing with multiplier α∈[−1/(d²−1),1]; this follows either from the invariant scalar/traceless decomposition or directly from its Choi matrix, whose eigenvalues are (1+(d²−1)α)/d and (1−α)/d. The error is (1−λα)||P||, minimized at α=1. For λ<1 a Weyl Kraus representation has all its coefficients nonzero and error space M_d, giving κ=2. ∎

This settles the full-algebra normalized-defect question in every finite dimension. Intermediate-defect envelopes for arbitrary proper algebras are still a separate problem.

### BM20-Q3. Exact primal and dual recovery for any binary observable algebra

Let A=C*(S), where S=S* and S²=I, with both eigenspaces nonzero. The logical and channel-output dimensions may be arbitrary finite values. Then

\[
\boxed{\delta_A=\min_{B=B^*,\ -I\preceq B\preceq I}
\|S-N^\dagger(B)\|}
\]

and equivalently

\[
\boxed{\delta_A=\max_{H=H^*,\ \|H\|_1\le1}
\left(\operatorname{tr}(SH)-\|N(H)\|_1\right).}
\]

**Proof.** A recovery adjoint sends S to a Hermitian contraction B. Conversely any B is realized by measuring (I±B)/2 and preparing a fixed state in the corresponding ± eigenspace of S. For X=cI+eS, |e|≤||X||, and the recovery error is e(S−N†B). Thus the first formula is exact on the entire complex operator unit ball of A.

The operator norm on Hermitian matrices is dual to the trace norm on Hermitian matrices. The minimum over B and maximum over H can be interchanged by the finite-dimensional compact convex minimax theorem. Maximizing tr(N(H)B) over Hermitian contractions B gives ||N(H)||_1, proving the dual formula. Both extrema are attained. ∎

The primal is a semidefinite program with constraints −I≼B≼I and −tI≼S−N†B≼tI. A feasible B gives an upper bound, and any dual-feasible H gives the displayed lower bound. Matching values certify optimality. This is a theorem and explicit optimization formulation; the new Python implementation concerns causal covers, not a general SDP engine. Standard channel/Choi and norm conventions are documented in [Watrous2018].

## 5. Effective repair under an explicit algebraic contract

### BM20-N1. A computable repair modulus on compact semialgebraic parameter sets

Let Θ be a nonempty compact semialgebraic coefficient set over the real algebraic numbers. Let g:Θ→[0,∞) be continuous and semialgebraic, with nonempty exact feasible set Z={θ:g(θ)=0}. For every positive rational η there is an algorithm returning a positive rational δ such that

\[
g(\theta)\le\delta\quad\Longrightarrow\quad
\operatorname{dist}(\theta,Z)<\eta.
\]

For algebraic input θ meeting this residual bound, a feasible algebraic θ* with ||θ−θ*||<η can also be produced.

**Proof.** For k=0,1,2,… use real quantifier elimination to decide

\[
\exists\theta\in\Theta:\quad g(\theta)\le2^{-k}
\quad\text{and}\quad
\forall\phi\in Z,\ \|\theta-\phi\|^2\ge\eta^2.
\]

Stop at the first false sentence and return δ=2^{-k}. The compact set {θ:dist(θ,Z)≥η}, if nonempty, has strictly positive minimum g. Thus the procedure terminates. If it is empty, it terminates immediately. The negated sentence supplies the claimed distance bound. For algebraic θ, sample the nonempty semialgebraic set {φ∈Z:||θ−φ||²<η²}; it has an algebraic sample point. ∎

In bounded-degree polynomial BM repair, Θ must explicitly bound coefficients, or otherwise be proved compact after removing redundant parameters. The residual g can include closure, legacy and range violations, provided it is continuous and semialgebraic on that fixed contract. Maxima of continuous semialgebraic residuals over compact semialgebraic carriers can be represented by first-order formulas, so the hypothesis is checkable in that setting. The conclusion concerns coefficient distance; a bound on the monomial evaluation vector converts it to a uniform function-distance bound.

This supplies an effective modulus absent from BM18-N2's bare compactness argument. It uses the same classical real-algebraic decision ingredient as BM18-N3. No quantifier-elimination engine is implemented in the accompanying Python file, and no polynomial-time complexity or unrestricted smooth repair modulus is claimed.

## 6. An impossibility boundary for general smooth minimum-dimension algorithms

### BM20-G1. Exact minimum augmentation is not uniformly decidable for computable smooth data

There is no algorithm that always terminates and determines the least continuous exact representation dimension for every computably specified smooth task, even with source [0,1], identity dynamics, constant legacy, and a task of the form τ(x)=a x with 0≤a≤1.

Here a computable specification supplies a program that approximates a to any requested rational error; it is more general than a finite algebraic-number input.

**Proof.** Given a program e and input, define a_e=2^{-t} if it first halts at step t≥1, and a_e=0 if it never halts. This is uniformly computable: simulate N steps; return the exact value if halting was observed and otherwise return zero, whose error is at most 2^{-N}.

If a_e=0, the zero-dimensional constant code represents the task exactly. If a_e>0, a constant code cannot represent the nonconstant task, while the one-dimensional code R(x)=x with identity update and decoder a_e x does. Therefore the minimum dimension is zero precisely in the nonhalting case. A terminating minimum-dimension algorithm would decide halting, which is impossible by the diagonal argument in BM18-I1. ∎

All tasks in the construction are smooth, uniformly bounded and uniformly Lipschitz. Those qualitative bounds do not remove the exact-zero decision problem. This is not a claim that a specified algebraic or geometrically restricted instance is undecidable; BM18-N3 and BM20-N1 deliberately use stricter effective inputs.

## 7. A constructive infinite-dimensional native class

### BM20-I1. Finite causal prediction of diagonal contractions with a compact task

Let X be the unit ball of the real Hilbert space ℓ². There are finitely many total actions

\[
(f_a x)_i=\lambda_{a,i}x_i,\qquad |\lambda_{a,i}|\le L<1.
\]

Let τ(x)=(b_i x_i)_i, with |b_i|≤C. Assume the diagonal coefficient sequences are effectively given rationals, L,C are supplied rational bounds, and a computable rational tail bound β_N≥sup_{i>N}|b_i| tends to zero. Then for every rational ε>0 a finite deterministic predictor with uniform ℓ² task error at most ε on every infinite action history can be constructed.

**Construction and proof.** The case C=0 needs one zero-output state. Otherwise choose N≥1 with β_N≤ε/2. Put a grid of spacing 1/K in each of the first N coordinates of [−1,1]^N, giving at most (2K+1)^N predictor states. Initialize by a grid approximation and update by coordinatewise multiplication with the selected λ_{a,i}, followed by nearest-grid rounding. Output the first N coordinates b_i q_i and zeros thereafter.

Choose K large enough that η=√N/K≤ε(1−L)/(2C); using √N≤N gives an entirely rational sufficient choice. Initialization can be implemented from approximations to the first N native coordinates with coordinate error at most 1/(4K), followed by clipping and rounding. Its Euclidean error is less than η, including rounding ties. Each subsequent rational grid update introduces at most η/2 and hence at most η error. Thus

\[
e_t\le L^t\eta+\eta\sum_{j=0}^{t-1}L^j\le\frac{\eta}{1-L}.
\]

The omitted task tail has norm at most β_N L^t≤β_N. Orthogonality of the retained and omitted coordinates gives

\[
\|\tau(x_t)-\widehat y_t\|_2
\le\sqrt{\beta_N^2+\left(\frac{C\eta}{1-L}\right)^2}
\le\varepsilon/\sqrt2<\varepsilon.
\]

Every grid and transition table is finite and computable from the stated data. ∎

This closes an effective infinite-dimensional native contract. It is a finite causal predictor with memory, not an assertion that the instantaneous rounding map commutes exactly with native dynamics. Arbitrary nonlinear PDEs, discontinuous availability boundaries, and infinite-dimensional quantum channels are outside this theorem.

## 8. Executed verification

The supplied verification program passed using exact rational arithmetic:

| Check | Executed scope |
| --- | --- |
| Minimum enclosing balls | 205 support certificates, including repeated points, affine degeneracy and dimensions 1–4 |
| Causal synthesis | 577 native/task cases; 2,166 history/closed-mode and memory-budget comparisons with an independent transition-table/initialization oracle |
| Independent causal oracle | 88,210 candidate transition/initialization combinations examined; scalar output centers computed independently as interval midpoints |
| Jordan bridge | 100 exact endpoint identity checks, with both signs of coupling |
| Nonlinear four-state witness | Exact zero Lie derivative and rational inequalities certifying squared-error improvement at least 71/540000000000, hence greater than 10^−10 |
| Quantum ceiling identity | 399 rational two-singular-value identities and ceiling inequalities for dimensions 2–20 |
| Infinite diagonal example | L=1/2, b_i=1/i, N=3, K=24 gives at most 117,649 grid states and squared-error bound 1/12, below (1/2)² |
| Input boundaries | Eight malformed or out-of-contract inputs rejected |

The mathematical arguments establish the general results. Finite checks corroborate identities and implementations; they do not prove the continuum-topology input, undecidability, or every infinite-dimensional instance. Independent review remains open.

## 9. Completion status after this continuation

| Original obligation | What is now completed | What remains in the original broader scope |
| --- | --- | --- |
| Continuous Jordan trajectory optimum | Exact n=3,d=1 value for every continuous scalar sampled factor; all L^p trajectory norms; explicit n=4 counterexample to universal linear optimality | Exact higher/intermediate n,d optima, including n=4,d=1 |
| Correlated finite architectures | BM18-C1–C2 already supplied the criterion and finite synthesis | External application benchmarks and new native categories |
| Fragmentation | BM18-F1–F3 already supplied exact frontier computation and complexity results | Competitive implementations and external benchmarks |
| Causal approximation | Exact arbitrary-output finite synthesis with partial availability, optional exact legacy, all infinite histories, and both memory/current-state variants | General infinite-carrier optimum and additional specified physical/regularity constraints |
| Quantum recovery | Sharp full-algebra normalized-defect envelope in every finite dimension; sharp algebra-dependent universal ceiling; exact binary-algebra primal/dual | Sharp intermediate-defect envelopes for general proper algebras and broader capability geometry |
| Nonlinear repair | Effective modulus and algebraic repair selection for compact semialgebraic coefficient contracts | Uniform guarantees beyond those contracts; unrestricted residual repair is already false |
| Global minimum realization | Exact universal smooth-input algorithm is ruled out even for a linear task with a computable coefficient | Geometry and least augmentation of individual specified native classes |
| Infinite presentations | Universal exact algorithm is ruled out; finite prediction now constructed for a diagonal contraction/compact-task class | Other specified PDE and infinite-dimensional channel classes |

The six broad extension rows remain open at their original breadth. The new proofs remove particular gaps and refute two tempting universal shortcuts; they do not erase the remaining questions. External physical validation, competitive usefulness, independent mathematical review and historical novelty are separate requirements. None is marked completed by this note.

## References

- [Nadler1999] S. B. Nadler, Jr., *Arc-like and circle-like almost continuous images of Peano continua*, Topology Proceedings 24 (1999), 249–259. Definitions of arc-like continua and the path/Peano characterization are in §1. https://topology.nipissingu.ca/tp/reprints/v24/tp24118.pdf
- [Bankston2019] P. Bankston, *On continuous images of ultra-arcs*, Topology and its Applications 261 (2019); author manuscript, §6, p. 9. It records the classical metric theorem that a locally connected chainable continuum is an arc and points to S. B. Nadler, *Continuum Theory: An Introduction* (1992), Chapter XII. https://www.mscsnet.mu.edu/~paul/Paper/ta_ultarcs113018.pdf
- [Tabuada2008] P. Tabuada, *An approximate simulation approach to symbolic control*, IEEE Transactions on Automatic Control 53(6) (2008), 1406–1418; author draft. https://www.seas.ucla.edu/~tabuada/Papers/ApproxSymbolicControl.pdf
- [Welzl1991] E. Welzl, *Smallest enclosing disks (balls and ellipsoids)*, LNCS 555 (1991), 359–370. https://doi.org/10.1007/BFb0038202
- [Watrous2018] J. Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), author draft. General conventions for operator norms, CPTP maps, Choi matrices, and convex optimization. https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf
