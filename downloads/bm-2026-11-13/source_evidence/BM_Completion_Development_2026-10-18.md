# BM — development of the remaining contracts

Started 18 October; integrated 19 October 2026 · Additive Research Edition development · Internal proofs and executable certificates

## 1. What this release completes

This document develops the eight open BM research families recorded in the Research Edition and the completeness register. It supplies full mathematical arguments, finite algorithms, exact certificates and explicit negative results. It does not change the frozen V1 foundation. “Theorem” below means a written proof with the stated hypotheses; it does not mean independent peer review or a historical originality claim.

The main advances are a universal greatest-interface criterion for finite correlated contexts, a compressed exact fragmentation frontier algorithm with an NP-completeness and fixed-parameter analysis, the exact three-state scalar-polynomial Jordan optimum, and the sharp universal normalized-defect upper bound for qubit recovery. Additional results address infinite-horizon prediction, conditioned nonlinear optimization, global smooth realization, effective infinite presentations, finite operational candidates and native locality examples.

| Existing obligation | Result developed here | Boundary that remains |
|---|---|---|
| Nonlinear Jordan trajectory optimum | Scalar polynomial sampled autonomy forces a first integral; exact optimum for n=3, d=1 in that class and for all continuous first integrals | Arbitrary continuous noninvariant encoders, and the other interior dimensions |
| Global smooth augmentation | Explicit finite-atlas construction; exact minima for a sphere with coordinate or constant legacy; finite-degree algebraic decision formulation | Least dimension for a general smooth source/task/legacy/target contract |
| Correlated local interfaces | Necessary and sufficient join-lifting criterion for universal greatestness; exact finite dynamic and cost enumeration | Other native categories, hidden coordination resources, and practical scaling |
| Causal approximation | Complete finite infinite-horizon verifier; a compact counterexample to an overbroad existence claim; contraction-based synthesis | Optimal causal covers without the stated stability/finite hypotheses |
| Quantum recovery | Improved general dimension-dependent estimate; sharp qubit envelope; exact qubit observable optimization and rational Pauli recovery | Sharp higher-dimensional constants and general capability geometry |
| Fragmentation | Exact compressed full frontier; NP-complete scalar decision; fixed-parameter tractability in distinct row patterns; executable witnesses | Competitive large-instance methods and external application benchmarks |
| General nonlinear repair | Existence of optimal repair within compact Lipschitz-bounded contracts; relaxation limit; finite-net error bounds; polynomial decision reduction | Unrestricted encoder classes, general repair moduli and effective convergence rates |
| Effective infinite models | A universal terminating exact algorithm is impossible on all computable presentations; exact finite/native positive cases remain available | Particular PDE/channel hypotheses and effective restricted infinite classes |

These statements resolve specified questions. They do not turn the entire BM research program into a finished theory. In particular, replacing “continuous” by “polynomial,” or “all dimensions” by “qubits,” is recorded as a restricted result rather than closure of the original broad question.

## 2. Scalar polynomial autonomy and the first interior Jordan case

### BM18-J1. Polynomial scalar factors of a unipotent map are first integrals

Let U be a real unipotent linear automorphism of R^n. Let R:R^n→R be a polynomial. Suppose a single-valued function F:R(R^n)→R(R^n), with no initially assumed regularity, satisfies

\[
R(Ux)=F(R(x))\qquad(x\in\mathbb R^n).
\]

Then R(Ux)=R(x) for every x.

**Proof.** The image I=R(R^n) is an interval. A constant R is immediate, so assume I has more than one point.

First F is continuous. For an interior y in I, choose two points whose R-values bracket y and connect them by a compact path. Every value sufficiently close to y has a preimage on that path. Given a sequence y_j→y, choose these preimages x_j. Any convergent subsequence has limit x with R(x)=y, and continuity of R∘U gives F(y_j)→R(Ux)=F(y). Compactness and uniqueness of this limit prove convergence of the full sequence. At an included endpoint of I, use a path from a preimage of that endpoint to a point with another value. This gives the same one-sided argument.

The invertibility of U makes F onto I. If F(z)=F(w), take R(x)=z and R(y)=w. Iteration yields R(U^k x)=R(U^k y) for all integers k≥1. Since U=I+N with N nilpotent, its integer powers are finite sums of binomial polynomials in k. Both sides are therefore polynomials in k. Equality at infinitely many integers implies equality at k=0, so z=w. Thus F is a continuous bijection of an interval, hence an increasing or decreasing homeomorphism.

The value c=R(0) is fixed by F. If F is increasing and z is not fixed, the two-sided orbit F^k(z) is strictly monotone in k. One of its two integer half-orbits is bounded between z and c: choose the forward or backward direction according to the positions of z and F(z). But F^k(z)=R(U^k x) for all integers k, and a nonconstant real polynomial cannot remain bounded on an integer half-line. Hence every z is fixed.

If F is decreasing, apply the increasing argument to F² and U². It gives F²=id. For each x the polynomial k↦R(U^k x) is then two-periodic on the integers. A polynomial with that property is constant. Again F=id. ∎

If U=e^{hN}, h>0 and N nilpotent, the polynomial t↦R(e^{tN}x) is h-periodic, since R(Uy)=R(y) for every y. It is therefore constant. Thus sampled scalar polynomial autonomy already gives invariance under the whole nilpotent flow. This conclusion uses global closure on all R^n, not closure only on a bounded performance set.

**The polynomial restriction is essential, even against infinitely smooth alternatives.** For the three-state chain below, write b=x_2,c=x_3 and define

\[
R(x)=
\begin{cases}
\exp(-1/c^2+b/c),&c\ne0,\\
0,&c=0.
\end{cases}
\]

This is globally C∞: on every bounded b-region, each derivative is bounded by a polynomial in 1/|c| times exp(−1/c²+B/|c|), which tends to zero as c→0. Yet R(Φ_h x)=e^{εh}R(x), so it is a smooth sampled-autonomous scalar encoder with a smooth linear update and is not a first integral. It vanishes on the whole plane c=0, so it does not improve the trajectory optimum established below. Its role is to rule out an unjustified extension of BM18-J1 from polynomials to all smooth encoders.

### BM18-J2. Exact n=3, d=1 trajectory optimum for polynomial encoders

Consider

\[
\dot x_1=\epsilon x_2,\qquad
\dot x_2=\epsilon x_3,\qquad
\dot x_3=0,\qquad \epsilon\ne0.
\]

The task is the full trajectory x_1(t), 0≤t≤T with T>0, measured in L²[0,T]. Performance is the worst case over the Euclidean unit ball of initial conditions. The encoder is a global scalar polynomial R, with exact sampled autonomy at any fixed h>0. The trajectory decoder may be arbitrary.

The optimum is

\[
E_{\rm poly}(3,1)^2
=\frac T2\left[
1+\frac{s^2}{3}
+\sqrt{\left(1-\frac{s^2}{3}\right)^2+s^2}
\right],
\qquad s=\epsilon T.
\]

It equals the known optimum among closed linear scalar encoders.

**Proof.** BM18-J1 makes R a first integral. We first prove a stronger lower-bound fact for any continuous first integral, even a nonpolynomial one.

On the plane x_3=0 with x_2=b≠0, flow translates x_1 through all real values. Hence R(a,b,0)=g(b), independently of a. Continuity extends this independence to b=0.

For c≠0, the flow time t=−2b/(εc) sends (a,b,c) to (a,−b,c). Invariance and the limit c→0 give g(b)=g(−b). Therefore

\[
R(a,b,0)=R(-a,-b,0)
\]

for every a,b. At these indistinguishable antipodal states the task trajectories are opposite:

\[
(\mathcal O_2(a,b))(t)=a+\epsilon tb.
\]

For any common decoder value w, the triangle inequality implies

\[
\max\{\|\mathcal O_2z-w\|_2,\|-\mathcal O_2z-w\|_2\}
\ge \|\mathcal O_2z\|_2.
\]

Maximizing over unit z gives the lower bound ||O_2||. The encoder R(x)=x_3, autonomous by F=id, with decoder t↦ε²t²R(x)/2 attains it. Its residual is exactly O_2(x_1,x_2).

Finally O_2*O_2 has matrix

\[
\begin{pmatrix}
T&\epsilon T^2/2\\
\epsilon T^2/2&\epsilon^2T^3/3
\end{pmatrix}.
\]

Its largest eigenvalue is the displayed expression. ∎

For ε=T=1, the squared error is (4+√13)/6, and the error is approximately 1.1258738292. The verification file encloses this value using rational arithmetic.

**Do not extend the argument without proof.** A global continuous sampled factor need not satisfy the polynomial step in BM18-J1. Also the antipodal restriction just proved is special to the three-state scalar case. For the four-state chain,

\[
I(x)=x_3^3-3x_2x_3x_4+3x_1x_4^2
\]

is a polynomial first integral, yet on x_4=0 it equals x_3³, which is odd. This explicitly blocks an attempted extension asserting that every scalar first integral is even on the whole preceding coordinate hyperplane. The supplied coefficient checker verifies this identity.

## 3. Correlated contexts: an exact universal criterion

### Definitions for this section

Let X_i be finite nonempty sets and K⊆∏_i X_i a nonempty legal context. Let B_i be fixed legacy equivalences. A local interface family E=(E_i) is allowed when each E_i⊆B_i, where inclusion means “identifies no more pairs than.” Its induced equivalence on legal states is

\[
x\,\Gamma_K(E)\,y
\quad\Longleftrightarrow\quad
x_i\,E_i\,y_i\ \text{for every }i.
\]

Joins of local families are coordinatewise equivalence joins. Joins of relations on K are equivalence joins on K.

A native action is a deterministic partial function f_a:D_a→K. For a task τ:K→Y, a family is feasible when:

1. Γ_K(E)⊆ker τ;
2. every D_a is Γ_K(E)-saturated;
3. x Γ_K(E) y in D_a implies f_a(x) Γ_K(E) f_a(y).

The second requirement retains availability. Omitting it would change the contract.

### BM18-C1. Universal greatestness is equivalent to join lifting

For fixed K and legacy bounds B, the following are equivalent:

**(a)** For every task and every collection of deterministic partial native actions on K, the feasible local families have a greatest member.

**(b)** For every pair of allowed families E,F,

\[
\boxed{\Gamma_K(E\vee F)=\Gamma_K(E)\vee\Gamma_K(F).}
\]

**Proof of sufficiency.** Equivalences on K that respect a fixed task and the native partial actions are closed under equivalence join. Indeed, a pair in the join has a finite chain of links from the constituent relations. The task is constant on every link. Domain membership propagates along every link, and, when enabled, applying f_a sends every link to another link in the same constituent relation. Thus the join is task-safe, availability-safe and stable.

Under (b), the coordinatewise join of two feasible local families induces exactly this stable join, so it is feasible. Finiteness gives closure under the join of all feasible local families. The discrete family is feasible, so the feasible set is nonempty. Its join is the greatest feasible family.

**Proof of necessity.** Always Γ_K(E)∨Γ_K(F)⊆Γ_K(E∨F). If equality fails, put H=Γ_K(E)∨Γ_K(F) and choose legal x,y identified by Γ_K(E∨F) but not by H. Use the task τ:K→K/H and only the identity action. Both E and F are feasible. Any family above both is above E∨F and therefore identifies x,y, violating the task. No greatest feasible family can exist. ∎

This is a structural classification, independent of a particular task. The criterion is not merely the older instruction to join all feasible families for one already-fixed task.

An equivalent finite test is connectivity: inside each cell of Γ_K(E∨F), connect two legal states when they are related by Γ_K(E) or Γ_K(F). Every such graph must be connected.

For full Cartesian K the condition holds: change one coordinate at a time along a local E_i/F_i chain, keeping the other coordinates fixed. Those intermediate states stay legal. Cartesian structure is sufficient but not necessary. The binary L-shaped context {(0,0),(0,1),(1,0)} passes the criterion. The diagonal {(0,0),(1,1)} fails: retaining only the first coordinate and retaining only the second are incomparable feasible choices for the nonconstant task.

### BM18-C2. Exact finite dynamic and cost synthesis

Enumerate the partitions E_i refining B_i, test the three feasibility conditions, and minimize any explicitly evaluable declared cost over the feasible families. This terminates because the search space is finite. The discrete family guarantees at least one feasible family for the stated deterministic model. A greatest interface is unnecessary for cost optimization: incomparable feasible families can be compared by cost.

The count of candidate families is at most ∏_i Bell(|X_i|). For each family, feasibility can be checked by all legal pairs and all native actions. This is an exact finite algorithm, with no polynomial-time claim.

The implementation's default cost is a weighted sum of local alphabet sizes. It is not a bit-count formula, a communication protocol cost or a physical implementation cost. The Python interface accepts a caller-supplied cost function; a new resource model must state its own cost and admissibility constraints.

The universal criterion and the task-specific optimizer have been checked against independent cell-based and order-based oracles on all 15 nonempty subsets of a binary two-coordinate product, all task partitions on each context, and all single deterministic partial actions: 10,771 instances. Thirteen of those contexts satisfy universal greatestness; the two diagonals do not. This finite check supports the implementation, not the universal proof by itself.

## 4. Fragmentation: exact frontier, complexity and parameterization

Let M be a binary matrix with n≥1 columns and nonempty rows. A column order π gives each row i a number b_i(π) of maximal one-blocks. Positive integer weights w_i represent row multiplicities. Define

\[
B(\pi)=\sum_{b_i(\pi)>1}w_i,\qquad
D(\pi)=\sum_iw_i(b_i(\pi)-1),\qquad
D_k=\min_{B(\pi)\le k}D(\pi).
\]

If the constraint is infeasible, D_k=+∞. The implementation represents that value by JSON null.

### BM18-F1. Duplicate compression preserves the Pareto frontier

Identical rows can be merged by adding their weights. Identical columns can be grouped adjacently in a Pareto witness without increasing any row's block count.

**Proof for columns.** From any order, delete all but one member of an identical-column group. Deleting an entry from a binary word never increases its number of one-blocks. Reinsert the deleted copies beside the retained column. Repetition of its bit extends an existing run or a zero-run and adds no one-block. Repeat for every identical-column group. Conversely, expanding a compressed order by adjacent duplicate copies preserves every row's block count. Therefore every original order is weakly dominated by an expanded compressed order, and the exact Pareto frontier is unchanged. ∎

After row compression let r be the number of distinct row patterns. There are q≤min(n,2^r) distinct column patterns.

### BM18-F2. A smaller exact frontier dynamic program

Use states (S,j,F), where S is the subset of placed column patterns, j is the last pattern, and F is the set of rows already fragmented. Store the smallest accumulated D and a predecessor pointer.

Let ones(j) be the rows containing a one in column pattern j. Let seen(S)=∪_{j∈S}ones(j). The empty prefix has a zero sentinel. On appending a new pattern k define

\[
J=(\operatorname{ones}(k)\setminus\operatorname{ones}(j))
\cap\operatorname{seen}(S).
\]

Exactly the rows in J start an additional one-block. The update is

\[
(S,j,F,D)\longmapsto
(S\cup\{k\},k,F\cup J,D+\sum_{i\in J}w_i).
\]

**Proof of sufficiency of the state.** The next start decisions depend only on the last column. Whether a new start is the first block is determined by seen(S). Whether the row has already contributed to B is determined by F. Thus two prefixes with the same (S,j,F) have identical possible future cost increments. Retaining only the smaller D cannot discard an optimum. Induction on |S| proves exactness. At the full subset B is the weight of F. Take the minimum D for every B, remove dominated pairs and compute D_k by prefix minima. Predecessors give an actual order. ∎

There are at most 1+2^q q2^r states. A direct implementation uses time O(2^q q²2^r r) and O(2^q q2^r) records, apart from input and output storage and integer bit costs. Weight arithmetic is exact. Since q≤2^r, this is fixed-parameter tractable in r, though the bound is doubly exponential in r. It is also finite-parameter tractable in the original column count by the simpler n! enumeration. Neither statement promises practical speed for large parameters.

The implementation materializes all integer budgets 0≤k≤Σw_i for convenience. For binary-encoded very large weights, that output is pseudopolynomial in the total weight. The Pareto breakpoint list alone gives the same mathematical function with output bounded by the terminal states; users with large multiplicities should use that representation. The algorithmic state bound refers to this breakpoint representation.

### BM18-F3. The scalar decision problem is NP-complete

The unweighted decision problem “is there an order with D≤d₀?” is NP-complete even when every row has exactly two ones.

**Proof.** A permutation is a polynomial-size witness; its row-block counts are computed in polynomial time. For hardness, take an undirected graph G with one column per vertex and one two-one row per edge. An edge row has one block precisely when its endpoints are consecutive in the permutation. Hence

\[
B(\pi)=D(\pi)=|E(G)|-\#\{\text{consecutive pairs of }\pi\text{ that are graph edges}\}.
\]

There is a Hamiltonian path exactly when D≤|E(G)|−(|V(G)|−1). Thus Hamiltonian path reduces directly to the fragmentation decision problem.

If the decision format only permits nonnegative thresholds, a graph with fewer than |V|−1 edges is immediately a no-instance and can be mapped to the fixed triangle-edge matrix with threshold zero, also a no-instance.

The NP-completeness of undirected Hamiltonian path may be obtained from the classical undirected Hamiltonian-cycle problem: split a chosen vertex into two nonadjacent copies, attach each original incident edge to both copies, and attach a new leaf to each copy. A Hamiltonian path in the new graph must run between the two leaves; identifying the split copies closes a Hamiltonian cycle in the original graph. The reverse construction is immediate. Cases with fewer than three original vertices can be handled separately. Classical Hamiltonian-cycle hardness is the imported complexity ingredient [Karp1972]. ∎

Consequently computing the complete frontier is NP-hard. A uniformly polynomial exact algorithm for arbitrary input would imply P=NP. This does not preclude useful restricted classes, approximation, or better parameterized methods.

### Checked constructions

The solver was compared with independent permutation enumeration on 4,080 matrices, including repeated patterns and weighted rows. It also reproduced the established gap family for n=5,…,9:

| n | Minimum broken rows φ | Minimum extra blocks δ | Extra blocks at minimum breadth D_φ |
|---|---:|---:|---:|
| 5 | 1 | 2 | 2 |
| 6 | 2 | 3 | 4 |
| 7 | 3 | 4 | 9 |
| 8 | 4 | 5 | 12 |
| 9 | 5 | 6 | 20 |

Small reproducible timing cases and the exact input matrices are in the verification JSON. They test this implementation; they are not comparisons against established packages or external application benchmarks.

## 5. Infinite-horizon causal prediction

### BM18-A1. Complete finite verification by a greatest safe relation

Let X and Q be finite native and predictor state sets. For each action a let f_a and F_a be deterministic partial transitions. Let τ:X→Y and g:Q→Y be outputs in a metric space, and fix ε≥0. Initial native states form I⊆X.

Start with pairs (x,q) satisfying both d(τ(x),g(q))≤ε and equality of enabled-action sets. Repeatedly remove a pair if an enabled common action sends it outside the current relation. The process stabilizes at S_* after at most |X||Q| strict deletion rounds.

There exists an initialization ι:I→Q producing error at most ε, with correct availability for every action history and every horizon, if and only if every x∈I has some q with (x,q)∈S_*.

**Proof.** The stabilized relation is forward invariant, output-safe and availability-safe. Any initialization into it therefore satisfies the specification by induction on history length.

Conversely, all pairs satisfying the infinite-history specification belong to the initial safe relation. If they belong to the current relation, their successors also satisfy the infinite-history specification and belong to it. They survive each deletion round. Thus they belong to S_*. A removed pair has a finite witness: an immediate failure has the empty word, and a predecessor failure prepends its action. Deletion ranks strictly decrease along the witness, giving a length below |X||Q|. ∎

This verifier does not secretly reobserve the native state during prediction. Initialization chooses q once; subsequent evolution uses only q and the action.

For a fixed state budget, finite allowed output catalogue and finite transition architecture, enumerate all candidate predictors and run this verifier. This completely decides that finite synthesis contract and minimizes any finite declared cost. It does not cover an unrestricted continuum of possible outputs or arbitrary infinite state architectures.

### BM18-A2. Compact future profiles need not admit a finite autonomous approximation

Let X=S¹⊂R², f(x) an irrational rotation, and τ(x)=x. The infinite-horizon profile metric is

\[
\rho_\infty(x,y)=\sup_{t\ge0}\|f^t(x)-f^t(y)\|=\|x-y\|.
\]

Thus the profile space is compact and totally bounded. Nevertheless no finite autonomous deterministic predictor can achieve uniform-in-time error ε<1, even for a single fixed initial state, when its outputs are allowed anywhere in R².

**Proof.** Every orbit of a finite autonomous predictor is eventually periodic. On one eventual residue class modulo its period p the predicted output is a fixed vector v. The native states along that subsequence are dense on S¹ because p times an irrational rotation angle is irrational. Their supremum distance to v is 1+||v||≥1. A constant-zero predictor attains error 1.

For completeness, density follows because the closure of the cyclic subgroup generated by an irrational rotation is an infinite closed subgroup of the circle. A proper closed subgroup has a smallest positive angular spacing and is finite; hence the closure is the whole circle. Positive tails and p-step subsequences have the same closure. ∎

This refutes an infinite-horizon inference from total boundedness alone. A finite cover of full response profiles is not automatically a finite causal machine.

### BM18-A3. A uniform construction for contracting dynamics

Let X be a compact metric space and let all total native actions f_a have a common Lipschitz constant L<1. Suppose τ is C-Lipschitz. Choose a finite η-net {c_j}⊆X and a quantizer q with d(x,c_{q(x)})≤η. Define

\[
F_a(j)=q(f_a(c_j)),\quad g(j)=\tau(c_j),\quad \iota(x)=q(x).
\]

For any action sequence, if e_t is the native-to-representative state error, then e_0≤η and e_{t+1}≤Le_t+η. Therefore

\[
\sup_{t\ge0}d(\tau(x_t),g(q_t))
\le \frac{C\eta}{1-L}.
\]

This is an actual finite autonomous implementation. Partial action boundaries, additional physical implementation restrictions and a minimum-cardinality claim require separate arguments.

## 6. Nonlinear repair under explicit compactness conditions

### BM18-N1. Existence of an optimal conditioned nonlinear repair

Let X,Z,Y be nonempty compact metric spaces. Let f:X→X and τ:X→Y be continuous. Let r:X→W and h:Z→W be continuous maps into a metric space W. Fix finite Lipschitz bounds L_R,L_F,L_D. Optimize over

\[
R:X\to Z,\quad F:Z\to Z,\quad D:Z\to Y
\]

with those respective bounds, subject to h∘R=r and R∘f=F∘R. Use worst-case task error

\[
E(R,D)=\sup_{x\in X}d_Y(\tau(x),D(R(x))).
\]

If the feasible set is nonempty, E attains its minimum.

**Proof.** Each bounded-Lipschitz map family is equicontinuous and has compact target. Arzelà–Ascoli makes it compact in the uniform topology; the Lipschitz inequality is preserved under uniform limits. The product of the three map families is compact.

Uniform convergence preserves the constraints. For example, D_j∘R_j→D∘R uniformly because

\[
\sup_xd_Y(D_j(R_jx),D(Rx))
\le \|D_j-D\|_\infty+L_D\|R_j-R\|_\infty.
\]

The analogous bound applies to F_j∘R_j; h is uniformly continuous on compact Z. Thus the feasible set is closed. E is continuous under this convergence, so its minimum is attained. The same compactness argument works for finitely many native actions and their corresponding reduced updates. ∎

This theorem supplies global optimal existence within the stated class. It does not show that the class is nonempty or that its optimizer can be computed from arbitrary black-box continuous maps.

### BM18-N2. Relaxation convergence and finite-net certificates

Within the same fixed compact map class, relax both constraint residuals to at most δ. These feasible sets are nested compact sets. If exact feasibility holds, their minimum errors E_δ increase to E_0 as δ↓0.

**Proof.** E_δ≤E_0 and monotonicity gives a limit. For δ_j↓0 choose minimizing triples. A convergent subsequence exists by compactness, its limit satisfies the exact constraints, and continuity of E gives a limiting value at least E_0. Thus equality holds. If every positive-δ problem is feasible, compactness and the same argument imply exact feasibility. There is no asserted computable rate. ∎

When f,τ,h,r are Lipschitz, an η-net N⊆X gives explicit upper certificates:

\[
\begin{aligned}
E(R,D)&\le \max_{x\in N}d_Y(\tau x,DRx)
 +(L_\tau+L_DL_R)\eta,\\
c&:=\sup_Xd_Z(Rf,FR)
\le\max_{x\in N}d_Z(Rfx,FRx)+L_R(L_f+L_F)\eta,\\
\ell&:=\sup_Xd_W(hR,r)
\le\max_{x\in N}d_W(hRx,rx)+(L_hL_R+L_r)\eta.
\end{aligned}
\]

Each follows by comparing an arbitrary x to a net point and applying the triangle inequality to the two component maps. These are rigorous upper bounds when the net radius and Lipschitz bounds are themselves certified.

With reduced initialization z_0=R(x_0), the closure defect c accumulates as

\[
d_Z(R(x_t),F^t(z_0))\le c\sum_{j=0}^{t-1}L_F^j.
\]

The task error is therefore at most

\[
E(R,D)+L_Dc\sum_{j=0}^{t-1}L_F^j.
\]

If L_F<1 this is bounded uniformly by E+L_Dc/(1−L_F). Otherwise a fixed one-step defect alone does not supply a time-uniform guarantee.

### Why the conditioning cannot simply be dropped

On S¹ let f be rotation by irrational α, let F=id, and choose integers q_j with ||q_jα|| modulo 1 tending to zero. The maps R_j(z)=z^{q_j} are surjective and have closure residual

\[
\sup_z|R_j(fz)-R_j(z)|=|e^{2\pi iq_j\alpha}-1|\longrightarrow0.
\]

Every continuous exact first integral of f is constant, because its value is constant on each dense orbit. Yet every R_j is at uniform distance 2 from every constant map into S¹. Their Lipschitz constants are unbounded. This is an explicit failure of an unrestricted “small residual implies nearby exact repair” claim. A general repair modulus needs additional hypotheses.

### BM18-N3. Fixed-degree semialgebraic synthesis is decidable

Suppose all source/target sets are explicitly semialgebraic over the real algebraic numbers, all supplied native and task maps are polynomial over that field, and the dimensions and degree bounds of unknown R,F,D are fixed. Express their coefficients as unknown real variables.

Range containment, exact closure, legacy retention and a threshold e on squared Euclidean task error are first-order polynomial conditions, for example

\[
\begin{gathered}
\forall x\in X:\ R(x)\in Z,\quad h(R(x))=r(x),\quad
R(f(x))=F(R(x)),\\
\forall x\in X:\ \|\tau(x)-D(R(x))\|^2\le e^2.
\end{gathered}
\]

Quantify separately over z∈Z for the ranges of F,D. Euclidean Lipschitz caps are polynomial inequalities on pairs of points. Existence of coefficients is therefore a sentence in the first-order theory of real closed fields. Quantifier elimination decides it and, in a nonempty definable coefficient set over real algebraic parameters, permits an algebraic sample witness. Testing dimensions up to a prescribed finite bound determines the least feasible dimension in that degree-bounded class.

This is a reduction to an established decision procedure, not a new quantifier-elimination algorithm and not an implementation of one in the supplied Python package. It does not decide arbitrary smooth synthesis or an unbounded search over all degrees. A formalized algebraic foundation for real-closed-field quantifier elimination is described by Mahboubi and Cohen [MC2012].

## 7. Global smooth augmentation: a construction and sharp families

### BM18-G1. A finite-atlas augmentation with a smooth decoder

Let M be a compact smooth n-manifold without boundary, with a supplied finite atlas (U_i,φ_i), i=1,…,k. Choose a smooth partition of unity ψ_i subordinate to this cover, with support compactly contained in U_i. Let r:M→R^ℓ be a supplied smooth legacy map.

Define, extending by zero outside each chart,

\[
g(x)=\big(\psi_i(x),\ \psi_i(x)\phi_i(x)\big)_{i=1}^k
\in\mathbb R^{k(n+1)}.
\]

Then g, and therefore E=(r,g), is a smooth embedding. Every supplied smooth task τ:M→R^p has a smooth decoder on E(M), and on an ambient neighborhood of E(M).

**Proof.** Smoothness across the chart boundaries follows from the compact supports. If g(x)=g(y), choose i with ψ_i(x)>0. The matching scalar block gives ψ_i(y)=ψ_i(x)>0, and the matching vector block then gives φ_i(y)=φ_i(x). Thus y=x.

If dg_x(v)=0, the same positive ψ_i gives dψ_i(v)=0 and

\[
d(\psi_i\phi_i)(v)=\psi_i(x)d\phi_i(v)=0.
\]

The chart differential is invertible, so v=0. Thus g is an injective immersion. Compactness of M and the Hausdorff target make it a homeomorphism onto its image, hence an embedding. Adding r preserves these properties.

On the image define D=τ∘E^{-1}; it is smooth. More explicitly, in any ambient neighborhood where the i-th scalar block a_i is positive and the ratio b_i/a_i lies in φ_i(U_i), use the local decoder τ∘φ_i^{-1}(b_i/a_i). These neighborhoods cover E(M); an ambient smooth partition of unity glues the local formulas, which all agree with τ on E(M). The Euclidean task target permits this weighted gluing. A smooth cutoff equal to one near compact E(M) can extend the decoder to the whole ambient Euclidean space if required. ∎

All smooth native transitions descend on the image by E∘f∘E^{-1}. The theorem does not assert that an arbitrary prescribed ambient target architecture admits an extension that preserves additional constraints away from E(M).

This is an explicit upper bound of k(n+1) augmentation coordinates for a supplied atlas. It is not asserted to be the least dimension or the best general embedding bound. Its purpose is to make one global repair construction concrete.

### BM18-G2. Exact augmentation dimensions on spheres

Let M=S^n⊂R^{n+1}, n≥1, and require full-state recovery.

* With legacy r(x)=x_0, the minimum number of continuous augmentation coordinates is n. Retaining x_1,…,x_n attains it.
* With constant legacy, the minimum is n+1. Retaining all coordinates attains it.

**Proof.** In the first case the fiber r^{-1}(0) is S^{n−1}. An augmentation into R^m with m≤n−1 identifies an antipodal pair by Borsuk–Ulam (including the elementary S⁰ case). Their legacy values also agree, so full-state decoding is impossible. Thus m≥n, and the coordinate construction attains equality.

With constant legacy, apply Borsuk–Ulam directly to S^n for m≤n. The full coordinate embedding attains n+1. These lower bounds hold even with an arbitrary decoder, so they also hold under a smooth-decoder requirement. ∎

Local rank alone does not yield these global minima. The topological obstruction and the actual retained legacy both matter. General source/task/legacy/target classification remains a separate obligation.

## 8. Quantum recovery: improved constants and exact qubit results

### Fixed normalization and imported ingredient

Let N be a finite-dimensional CPTP channel with d-dimensional logical input and a Kraus representation with r operators E_i. Let

\[
\mathcal K=\operatorname{span}\{E_i^\dagger E_j\}
\]

and let A⊆M_d be a unital *-subalgebra. Use exactly the Research Edition's normalized commutator defect and unamplified recovery error:

\[
\kappa_A=
\sup_{\substack{Z\in\mathcal K,\ \|Z\|\le1\\X\in A,\ \|X\|\le1}}
\|[Z,X]\|,
\qquad
\delta_A=
\inf_{\mathcal R\ {\rm CPTP}}
\sup_{\substack{X\in A\\\|X\|\le1}}
\|X-N^\dagger\mathcal R^\dagger(X)\|.
\]

The norm is the operator norm. The recovery runs from the channel output back to the logical input. The complementary-channel quantity below is a different object; do not also name it δ.

Let P_{A'} be the trace-preserving conditional expectation onto the commutant. Set

\[
\beta=\|\widehat N-\widehat N P_{A'}\|_\diamond.
\]

The imported approximate-algebra recovery theorem gives a CPTP recovery with diamond reconstruction error at most 2√β relative to P_A. Restricting its adjoint error to A gives δ_A≤2√β. This is the upper bound in **Theorem 1** of the cited arXiv version of Bény [Beny2009]; the earlier Research Edition's “Theorem 3.1” locator should be read as corrected here. The lower bound in that paper concerns its diamond-error definition and is not silently transferred to BM's unamplified δ_A.

### BM18-Q1. Improved general bound

\[
\boxed{\delta_A\le
\min\{2,\ 2\sqrt{\min(d,r^2)\,\kappa_A}\}.}
\]

**Proof.** Put L=(I−P_{A'})\widehat N^\dagger. Since the adjoint complementary channel is unital completely positive, ||\widehat N^\dagger(B)||≤||B||. Its range is K. Averaging conjugation by unitaries in A gives P_{A'}, so

\[
\|Z-P_{A'}Z\|
\le \sup_{U\in\mathcal U(A)}\|[Z,U]\|
\le\kappa_A\|Z\|\quad(Z\in\mathcal K).
\]

Thus ||L||_{∞→∞}≤κ_A. Its trace-dual Δ=\widehat N−\widehat N P_{A'} has ||Δ||_{1→1}≤κ_A.

For unit vectors u,v in C^d⊗H, write Schmidt decompositions with coefficients s_i,t_j. The trace norm of (Δ⊗id)(uv†) is at most

\[
\kappa_A\Big(\sum_i s_i\Big)\Big(\sum_j t_j\Big)
\le d\kappa_A.
\]

Here each input rank-one factor has trace norm one, each ancillary rank-one factor has trace norm one, and each Schmidt rank is at most d. Extending by a singular-value decomposition proves β≤dκ_A for arbitrary ancilla dimension.

For the alternative environment bound, write an amplified B in r×r blocks B_{ij}. Since ||L(|i⟩⟨j|)||≤κ_A and every block norm is at most ||B||, the triangle inequality gives ||(L⊗id)(B)||≤r²κ_A||B||. Hence β≤r²κ_A as well. Combine both bounds with the imported δ_A≤2√β. Finally δ_A≤2 follows because both the identity and N†R† are contractions on the operator unit ball. ∎

This estimate is conservative in higher dimensions. In particular, it need not become informative when only the physical channel is weakly noisy.

### BM18-Q2. What the normalized operator-system defect can and cannot measure

For the full logical algebra A=M_d, κ_A is either zero or two.

**Proof.** If K=CI, all commutators vanish. Otherwise the unital self-adjoint space K contains a nonscalar Hermitian H. Subtract the midpoint of its largest and smallest eigenvalues times I and normalize the resulting operator. This produces Z∈K with ||Z||=1 and extreme eigenvalues ±1. A norm-one operator taking an extreme eigenvector to the opposite one has commutator norm two with Z. The general upper bound is two, so κ_A=2. ∎

Thus a channel whose nontrivial error operators become arbitrarily small can retain κ_A=2. Normalizing every member of their span removes the channel's amplitude scale. A channel-weighted quantity such as β is needed to track that continuity directly.

### BM18-Q3. Sharp universal qubit upper envelope

For logical input dimension d=2, any CPTP channel, and any unital *-subalgebra A⊆M_2,

\[
\boxed{\delta_A\le\kappa_A/2.}
\]

This is the sharp universal upper bound as a function of κ_A over this class: every value κ∈[0,2] has an example with δ=κ/2. For every fixed κ>0 the infimum of δ among examples with that κ is zero. Thus κ does not specify the actual recovery error.

**Proof.** Every unital *-subalgebra of M_2 is CI, the full matrix algebra, or a two-dimensional algebra generated by A_u=u·σ for a real unit vector u.

The completely depolarizing recovery gives δ_A≤1 for every such algebra. For the full matrix algebra this uses the norm-one traceless projection

\[
P_0(X)=X-\tfrac12\operatorname{tr}(X)I
=\tfrac12(X-\sigma_y X^{\mathsf T}\sigma_y).
\]

The second expression proves ||P_0||≤1 since transpose and unitary conjugation preserve operator norm; a Pauli matrix attains one.

Write the Hermitian part of K as RI⊕{v·σ:v∈V}, where V is a real subspace of R³.

For A=CI both errors vanish. For A=M_2, BM18-Q2 gives κ=0 or 2. At κ=0 the exact commutant recovery theorem gives δ=0; at κ=2 the depolarizing recovery gives δ≤1.

Now let A=C*(A_u). If dim V≥2, V contains a unit vector v perpendicular to u. The commutator of v·σ and u·σ has norm two, so κ=2 and δ≤1 suffices.

If V={0}, exact recovery gives δ=0. In the remaining case V=Rv for a unit vector v. Then K=span{I,v·σ} and

\[
\kappa_A=2\sqrt{1-(u\cdot v)^2}.
\]

To verify the supremum, write Z=aI+b(v·σ), X=cI+e(u·σ). The constraints ||Z||,||X||≤1 imply |b|,|e|≤1, and the commutator norm is 2|be|√(1−(u·v)²). Choosing b=e=1 attains the bound.

The exact commutant theorem supplies a CPTP recovery preserving the algebra C*(v·σ). Follow it by dephasing along v. On A_u the recovered observable is (u·v)v·σ. The error norm is √(1−(u·v)²)=κ_A/2. On any element cI+eA_u of the algebra, |e|≤||cI+eA_u||, so this same bound controls its whole unit ball.

For sharpness use complete dephasing along v. Its complementary error space is span{I,v·σ}; every recovered observable remains in that span. The component of u perpendicular to v has norm √(1−(u·v)²), giving the matching lower bound. Choose u·v to realize any κ in [0,2].

Finally replace complete dephasing by partial dephasing with transverse Bloch multiplier λ∈[0,1). Its operator system is the same span for every λ<1, so κ stays fixed. Identity recovery already has error at most (1−λ)√(1−(u·v)²), which tends to zero as λ↑1. This proves the lower-envelope assertion without claiming δ=0 at any nonzero κ. ∎

This settles a sharp normalized-defect question for qubits, including arbitrary output dimension. It does not supply the sharp higher-dimensional envelope.

### BM18-Q4. Exact recovery of one qubit observable algebra

For a qubit-to-qubit channel with Bloch action x↦Ax+t and a task algebra generated by A_u=u·σ, ||u||=1,

\[
\boxed{
\delta_{A_u}=
\min_{|b_0|+\|v\|\le1}
\left(|b_0+t\cdot v|+\|u-A^{\mathsf T}v\|\right).
}
\]

**Proof.** A unital positive adjoint recovery sends A_u to a Hermitian contraction B=b_0I+v·σ, precisely satisfying |b_0|+||v||≤1. Conversely every such B is realized by measuring the effects (I±B)/2 and preparing the ± eigenstates of A_u, which is CPTP.

The channel adjoint sends B to (b_0+t·v)I+(A^T v)·σ. The difference from A_u has norm |b_0+t·v|+||u−A^T v||. As above, the error on A_u controls exactly the unit ball of its two-dimensional algebra. Minimization gives the formula. ∎

This is a convex second-order cone optimization, with a directly realizable recovery. For a unital channel, b_0=0 is optimal, and δ is the Euclidean distance from u to the ellipsoid A^T{v:||v||≤1}.

For dephasing A=diag(λ,λ,1), 0<λ<1, the nontrivial case can be computed from a single multiplier μ>0. Writing a_i for the diagonal entries,

\[
\sum_i\frac{a_i^2u_i^2}{(a_i^2+\mu)^2}=1,\qquad
v_i=\frac{a_i u_i}{a_i^2+\mu},\qquad
\delta^2=\sum_i\frac{\mu^2u_i^2}{(a_i^2+\mu)^2}.
\]

The left side is strictly decreasing in μ on the nontrivial support, so the root is unique when u lies outside the ellipsoid. These equations follow from minimizing ||u−Av||² subject to ||v||≤1 and the convex Lagrange multiplier conditions. If u already lies in the ellipsoid the distance is zero. The λ=0 case uses the corresponding segment directly.

The supplied exact rational bracketing example λ=1/2, u=(3/5,0,4/5) has error approximately 0.2622622320. The rational inequalities, not the decimal display, are the numerical certificate.

### BM18-Q5. Exact full-algebra recovery for Pauli channels

Let N be a qubit Pauli channel with probabilities p_0,p_x,p_y,p_z. Its Bloch multipliers are

\[
\lambda=(p_0+p_x-p_y-p_z,\ p_0-p_x+p_y-p_z,\ p_0-p_x-p_y+p_z).
\]

The optimal unamplified full-algebra error is the linear-program value

\[
\min_{q\ge0,\ \sum q=1}\ \max_{i=x,y,z}(1-\alpha_i(q)\lambda_i),
\]

where α(q) is obtained from q by the same Pauli-multiplier formula.

**Proof.** Twirl any recovery over Pauli conjugations. The noise channel commutes with those conjugations, the target identity is covariant, and the operator-norm objective is convex and unchanged by conjugation. The twirled recovery is a Pauli channel with no greater error.

The resulting error map vanishes on I and multiplies σ_i by a_i=1−α_iλ_i≥0. Its induced operator norm is max_i a_i. For the upper bound, first apply the norm-one traceless projection P_0. On traceless matrices, every coordinate sign flip in the Pauli basis is an operator-norm isometry: orthogonal actions with determinant one come from unitary conjugation, and determinant-minus-one actions also use transpose. Any real diagonal multiplier with entries in [−1,1] is a convex combination of these sign flips. Scaling gives the upper bound max_i|a_i|; a Pauli matrix for a maximizing coordinate gives equality.

Minimizing that maximum over the probability simplex is exactly the displayed LP. ∎

For rational noise probabilities, the implementation enumerates rational vertices of a four-variable LP and returns both a feasible recovery and nonnegative dual multipliers with the same objective. Those matching rational values certify optimality. It is not relying on a floating solver's status string.

For an isotropic depolarizing multiplier λ∈[0,1], the answer is δ=1−λ: α_i≤1 supplies the lower bound, and identity recovery attains it. For λ<1 its full-algebra normalized κ equals two, while δ tends to zero as λ tends to one.

## 9. Effective infinite presentations: a universal impossibility result

### BM18-I1. Exact future equivalence is not decidable on all computable carriers

There is no algorithm that always terminates and decides exact future equivalence for every countable, effectively presented deterministic system, even with one total computable update and one binary task.

**Proof.** Use the countable carrier of configurations of a universal Turing machine, together with an extra absorbing state ⊥. The update performs one machine step; halting configurations and ⊥ are absorbing. Let the task be one on halting configurations and zero elsewhere.

For the effectively given initial configuration c_e encoding a machine and input, c_e and ⊥ have equal task outputs at every future time exactly when that machine never halts. A terminating exact equivalence decider would therefore decide halting by negating its answer. Such a decider is impossible.

The underlying diagonal contradiction is brief: if H(p,x) decided whether program p halts on x, construct D(x) to loop when H(x,x) says “halts,” and to halt otherwise. Applying D to its own program description contradicts either answer of H. ∎

The same obstruction applies to a universal terminating quotient constructor that returns codes with decidable equality and whose code equality exactly captures future equivalence. It does not prohibit a non-effective semantic quotient.

Finite-horizon equivalence remains decidable by direct iteration. Inequivalence is semidecidable by searching for a finite distinguishing time (or, with finitely many actions, a distinguishing word). Full equivalence is not generally decidable. This is a precise limit on a universal algorithm, not a statement that a particular heat equation, quantum channel or physically specified PDE has no useful effective theory.

## 10. Finite operational realizations of Seed, Rooting and Rebranching

These are explicit finite native conventions. They finish an executable interpretation of the candidate vocabulary; they do not assert a unique universal interpretation or alter the V1 core.

### BM18-O1. Finite Seed

A finite Seed consists of a finite typed variable list with domains D_i, a partial assignment, and a supplied set or decidable predicate of allowed complete assignments. Its realizations are exactly the completions respecting all three. Enumeration terminates. An empty result is a valid infeasibility answer; there is no theorem that a Seed must grow into a realization.

The solver preserves every realization rather than arbitrarily declaring one canonical. A requested choice needs a declared order, cost or selection rule.

### BM18-O2. Finite Rooting

Given a realization s, a declared typed export e, and receiver predicates for applicability and admissibility, compute v=e(s). Return:

* not applicable if the applicability predicate fails;
* rejected if applicable but inadmissible;
* accepted if both predicates pass.

A Root is the receiver-relative accepted export with its provenance. Merely computing an export does not make it accepted. The code's simple result is a status record; a production use must attach the actual source/receiver identifiers and evidence required by its passport.

### BM18-O3. Finite Rebranching

Given source and target realization sets, a proposed transport H, and declared tasks τ_S,τ_T, a task-preserving rebranching satisfies

\[
H(\operatorname{Real}(S))\subseteq\operatorname{Real}(T),
\qquad \tau_T\circ H=\tau_S.
\]

Both conditions are decidable by finite enumeration. If accepted exports must also be preserved, add the corresponding export square and receiver-passport implication. Task preservation alone does not imply passport preservation.

### BM18-O4. Composition and passport transport

If H:S→T and J:T→U satisfy the displayed realization and task conditions, J∘H does too, by substitution. If, additionally, both mappings preserve the applicable/accepted passport predicates through their declared export squares, their composite preserves those predicates. This proves finite operational consistency. It does not establish physical causation or canonical selection.

The reference tests cover successful and empty Seeds, all three Rooting outcomes, and accepted and rejected rebranching witnesses.

## 11. Native witnesses for the locality clauses

### BM18-L1. Sharp one-dimensional wave restriction radius

For the classical one-dimensional wave equation u_tt=c²u_xx on R, c>0, with smooth initial displacement f and velocity g, d'Alembert's formula gives

\[
u(0,t)=\frac{f(-ct)+f(ct)}2+
\frac1{2c}\int_{-ct}^{ct}g(y)\,dy.
\]

The output over 0≤t≤T depends only on the initial data restricted to [−cT,cT]. Among centered restriction carriers [−r,r], this radius is sharp: for any 0≤r<cT choose f=0 and a nonzero nonnegative smooth g supported inside (r,cT). These data agree with zero on [−r,r], but u(0,T)>0. The formula follows by differentiating and checking the initial data, or by decomposing the solution into left- and right-moving waves.

This supplies an actual native realization of the finite-propagation conditional clause. It does not prove that every optimal encoder must literally store the whole interval, nor does it assert finite propagation for other PDEs.

### BM18-L2. A quasistatic problem has a different carrier

For −u''=f on (0,1), u(0)=u(1)=0, the Green function is

\[
G(x,y)=\min(x,y)(1-\max(x,y)),\qquad
u(x)=\int_0^1G(x,y)f(y)\,dy.
\]

It is positive for interior x,y. A positive forcing bump supported away from a neighborhood of x_0 still changes u(x_0), although the local forcing data at x_0 are unchanged. For example, x_0=1/4 and the integrable forcing f=1 on [1/2,3/4], zero elsewhere, give u(x_0)=3/128 exactly.

This is a direct counterexample to inheriting a finite spatial restriction rule merely by using similar field notation. No convergence of a dynamical model to this elliptic model has been asserted. Such a limit, if desired, needs its own topology, boundary conditions, scaling and proof.

## 12. What is executable and what was checked

The accompanying reference package uses Python 3.10 or later and the standard library. Keep the solver, examples and verification script together.

    python BM_Finite_Solvers_2026-10-18.py BM_Solver_Examples_2026-10-18.json
    python BM_Solver_Verification_2026-10-18.py

| Component | Delivered computation | Verification evidence |
|---|---|---|
| Fragmentation | Full Pareto breakpoints, every budget value, actual column-order witnesses | 4,080 independent permutation comparisons; five gap-family instances |
| Correlated interfaces | Universal criterion with negative witness; exact dynamic feasibility and cost optimizer | 10,771 independent finite task/action comparisons over all 15 binary contexts |
| Infinite-horizon finite prediction | Greatest safe relation, initialization decision, finite failure words; minimum-state finite-catalogue synthesis | 1,376 independent reachability comparisons; all failure words replayed; three bounded synthesis cases |
| Pauli recovery | Rational optimum, recovery probabilities, primal/dual certificate | 153 rational noise instances with exact certificate checks |
| Jordan examples | Exact flow identities and a rational enclosure of the sharp n=3 polynomial value | Coefficient equality for two invariants; exact Gram polynomial root bracket |
| Qubit observable example | Rational secular-root and error-squared enclosures | Monotone root bracket, with decimal display explicitly approximate |
| Finite operational conventions | Seed completion, Rooting statuses and rebranching checker | Seven specified examples |
| Native quasistatic example | Exact Green-function integral | Rational result 3/128 |

The check suite passed. The JSON records exact rational quantities, deterministic seed, source hashes, input matrices and timing observations. Timings are specific to this run and are not a performance guarantee.

The supplied package does not implement general quantifier elimination, unrestricted nonlinear functional optimization, general CPTP optimization, a PDE solver or a proof assistant. Those statements are mathematical reductions or proofs in this document. The Python checks are supporting evidence for the finite implementations.

## 13. Remaining obligations, stated without inflated completion claims

1. **Jordan:** prove an equally sharp bound or give a counterexample for arbitrary globally continuous sampled-autonomous encoders in the original interior regime. Polynomial invariance does not settle it.
2. **Global smooth minimum:** for a given general source, task, legacy and target architecture, establish the least augmentation dimension, including singular fibers and topology. The atlas construction is an upper bound, not the classification.
3. **Causal optimum:** characterize finite approximate causal implementations beyond the contraction and finite-state contracts, including controlled optimal cost. The rotation obstruction prevents an unrestricted existence theorem.
4. **Higher-dimensional quantum sharpness:** determine the optimal normalized-defect envelope or suitably channel-weighted alternatives above logical dimension two, and the stated capability geometry.
5. **Unrestricted nonlinear repair:** identify assumptions giving effective repair moduli and optimizer computation outside the compact Lipschitz and finite-degree algebraic classes. Vanishing residuals alone do not suffice.
6. **Restricted infinite/native theories:** prove regularity, effective presentation and quantitative closure for each intended infinite-dimensional application. The universal algorithm has been ruled out; these application-specific problems have not.
7. **Validation and positioning:** obtain independent checking or formalization of selected proofs, external benchmarks and theorem-by-theorem prior-art comparisons. Internal checks do not satisfy these external gates.

The finite correlated-context question and the mathematical fragmentation complexity/parameterization question now have exact answers under their explicit contracts. Their implementations are complete reference implementations for those contracts. Practical scaling and application evaluation remain separately tracked. Seed, Rooting and Rebranching have finite operational definitions; universal claims about them remain candidates.

The appropriate release claim is therefore: **BM has an internally established core, additional proved and executable extensions, explicit impossibility boundaries, and a shorter, precisely stated research remainder. It is not a fully closed research program or a verified universal physical theory.**

## References and provenance

* **BM-R3.** Branch Mathematics Research Edition, Library version 3, inspected 18 October 2026. Governing source for the existing contracts and theorem families. The version-3 source snapshot remains unchanged; this development is appended in version 4.
* **BM-I6.** BM Outstanding Issues, 14 October 2026, version 6. Earlier broad completion wording is interpreted through the current completeness register and this scoped continuation.
* **Beny2009.** Cédric Bény, “Conditions for the approximate correction of algebras,” arXiv:0907.4207. Exact commutant criterion and Theorem 1's approximate upper bound are imported mathematical ingredients, not BM discoveries. https://arxiv.org/pdf/0907.4207
* **Karp1972.** Richard M. Karp, “Reducibility Among Combinatorial Problems,” in Complexity of Computer Computations. The classical Hamiltonian-cycle hardness is the imported ingredient in BM18-F3; the two-one-row construction and split-vertex reduction are written out here. https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/papers/KarpOriginal.pdf
* **MC2012.** Assia Mahboubi and Cyril Cohen, “Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination,” Logical Methods in Computer Science 8(1), 2012. https://arxiv.org/abs/1201.3731
* **Turing1937.** A. M. Turing, “On Computable Numbers, with an Application to the Entscheidungsproblem,” Proceedings of the London Mathematical Society s2-42, 230–265. The halting obstruction is classical; the BM future-equivalence reduction is explicit above. https://doi.org/10.1112/plms/s2-42.1.230
* Classical ingredients also include Borsuk–Ulam, partitions of unity, compact injective-immersion embedding, Arzelà–Ascoli, finite safety fixed points, LP duality and the elementary wave/Green formulas. They are not presented as newly discovered mathematics. The contribution claimed here is the written contract-specific development; no exhaustive novelty search has been completed.
