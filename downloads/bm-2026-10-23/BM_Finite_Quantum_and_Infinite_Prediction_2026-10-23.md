# Branch Mathematics: finite quantum recovery and infinite-state prediction

23 October 2026 · Additive development B23 · Six scoped results

This note keeps the frozen V1 definitions, the original unamplified recovery norm, and the distinction between a causal predictor and a closed current-state encoder. It adds proofs and executable certificates to the 21 October working record. It does not establish historical novelty, independent review, or completion of every BM extension.

The finite algebraic quantum problems below have exact terminating procedures in principle. A general quantifier-elimination engine is **not** implemented or executed in this release. The delivered programs verify real-rational quantum certificates and construct finite response-tree predictors. Those are different implementation claims.

## 1. Fixed quantum contract

Let \(N:M_d\to M_b\) be a completely positive trace-preserving channel, with Kraus operators \(E_i:\mathbb C^d\to\mathbb C^b\). Let \(A\subset M_d\) be a supplied unital observable algebra. Retain

\[
\delta_A(N)=\min_{R\ {\rm CPTP}}\sup_{X\in A,\ \|X\|\le1}
 \|X-N^\dagger R^\dagger(X)\|,
\]

\[
\mathcal K_N=\operatorname{span}_{\mathbb C}\{E_i^\dagger E_j\},\qquad
\kappa_A(N)=\max_{Z\in\mathcal K_N,\ \|Z\|\le1; X\in A,\ \|X\|\le1}
 \|[Z,X]\|.
\]

All norms here are operator norms, including on non-Hermitian inputs. No diamond-norm lower bound is substituted. The recovery minimum is attained by compactness of the finite-dimensional channel set.

For algebraic algorithms the input consists of exact real-algebraic real and imaginary matrix entries, finite dimensions, and an explicit algebra passport

\[
\iota:\bigoplus_{j=1}^s M_{n_j}\longrightarrow A,
\qquad
\iota((X_j))=W\left[\bigoplus_j(X_j\otimes I_{m_j})\right]W^\dagger,
\quad \sum_j n_jm_j=d,
\]

with algebraic unitary \(W\). Additional channel restrictions must be supplied by finite polynomial equalities and inequalities if they are to enter the algebraic algorithm.

The standard Choi characterization used below is classical, as is quantifier elimination over real closed fields [W18, CM12]. Their use here does not establish novelty of the underlying mathematics.

## 2. BM23-Q1 — Exact recovery using only the observable algebra

For each summand choose a Hermitian block matrix

\[
H_j=[H_{j,uv}]_{u,v=1}^{n_j}\succeq0,
\quad H_{j,uv}\in M_b,
\qquad \sum_{j,u}H_{j,uu}=I_b.
\tag{Q1.1}
\]

Define \(\phi_H(\iota(X))=\sum_{j,u,v}(X_j)_{uv}H_{j,uv}\). Then

\[
\boxed{\delta_A(N)=
\min_{H\ {
m satisfying}\ (Q1.1)}
\max_{U_j^\dagger U_j=I_{n_j}}
\left\|\iota(U)-N^\dagger\phi_H(\iota(U))\right\|.}
\tag{Q1.2}
\]

Every feasible \(H\) extends to a physical recovery. In particular, the formula does not optimize over arbitrary linear decoders.

**Proof.** The Choi criterion identifies \(H_j\succeq0\) with complete positivity of the map from the \(j\)-th matrix summand to \(M_b\). The diagonal-block constraint is precisely unitality of their sum. Restricting any recovery adjoint to \(A\) therefore produces a feasible \(H\).

Conversely, let \(P_A:M_d\to A\) be the trace-preserving conditional expectation. In the displayed block coordinates it deletes off-diagonal central blocks and replaces each multiplicity block by its normalized partial trace tensored with \(I_{m_j}\). This is a unital completely positive map fixing \(A\). Thus

\[
R_H^\dagger=\phi_H\circ P_A
\]

is unital and completely positive on all of \(M_d\); its trace adjoint is a CPTP recovery. Its restriction to \(A\) is exactly \(\phi_H\).

It remains to justify testing the full complex operator unit ball using unitaries. A contraction \(X_j=V_j\operatorname{diag}(s_i)W_j^\dagger\), \(0\le s_i\le1\), is the average of the two unitaries

\[
V_j\operatorname{diag}(s_i\pm i\sqrt{1-s_i^2})W_j^\dagger.
\]

Applying this simultaneously to all summands makes any contraction in \(A\) the average of two unitaries in \(A\). Linearity of the error and convexity of the norm prove the equality of the two suprema. Finally the feasible \(H\)-set is compact: it is closed, positive semidefinite, and \(\sum_j\operatorname{tr}H_j=b\). The continuous objective therefore attains its minimum. ∎

The matrix variables have block sizes \(n_jb\), so multiplicities \(m_j\) do not create unnecessary recovery variables. They still enter the physical embedding and the native channel.

## 3. BM23-Q2 — Effective exact optima and sharp defect envelopes

For the finite algebraic input contract above:

1. \(\delta_A(N)\) is a real algebraic number. An exact optimal recovery with algebraic entries can be found by a terminating real-algebraic algorithm.
2. For fixed dimensions and Kraus bound, the attainable set of pairs \((\kappa_A(N),\delta_A(N))\) is effectively semialgebraic, including any supplied semialgebraic channel restrictions.
3. For any algebraic \(c\), one can decide whether channels with \(\kappa_A=c\) exist. If they do, their sharp lower and upper recovery-error envelopes are computable real algebraic numbers. Attainment of either endpoint is decidable. An unattained endpoint still admits algebraic channels within any prescribed positive algebraic tolerance.

These are exact computability and characterization results. They do not say that the resulting elimination is efficient or provide an evaluated closed formula for every dimension and algebra.

**Proof of the fixed-channel statement.** Write every complex entry as two real variables. For \(t\ge0\), let \(\mathsf{Feas}(N,t)\) mean that there are matrices \(H\) satisfying (Q1.1) such that, for every tuple of unitary matrices \(U_j\),

\[
t^2 I_d-M(H,U)^\dagger M(H,U)\succeq0,
\quad
M(H,U)=\iota(U)-\sum_i E_i^\dagger\phi_H(\iota(U))E_i.
\tag{Q2.1}
\]

Positive semidefiniteness is equivalent to nonnegativity of **all principal minors**, not just leading minors. Unitarity, Hermiticity and (Q2.1) are finite polynomial conditions on the real coordinates. Hence \(\mathsf{Feas}\) is an explicit first-order formula over the reals. It holds exactly when \(\delta_A(N)\le t\).

The formula

\[
0\le z\le2\ \wedge\ \mathsf{Feas}(N,z)
\ \wedge\ \forall u\,[0\le u<z\Rightarrow\neg\mathsf{Feas}(N,u)]
\tag{Q2.2}
\]

defines the singleton \(\{\delta_A(N)\}\). Real-closed-field quantifier elimination computes a quantifier-free description of it. A singleton semialgebraic over the real algebraic numbers has an algebraic coordinate. Real-algebraic sampling of the nonempty feasible set at that value produces algebraic \(H\). Formula (Q1.1), the stated expectation \(P_A\), and Choi/Kraus conversion then produce an algebraic recovery. This proves the first assertion.

**Proof of the envelope statement.** Parameterize a channel by \(k\) matrices \(E_i\) with \(\sum_iE_i^\dagger E_i=I_d\). Zero matrices permit Kraus rank less than \(k\). This parameter set is compact because \(\sum_i\|E_i\|_F^2=d\).

Membership in the error space is the polynomial existential condition

\[
Z=\sum_{i,j}\lambda_{ij}E_i^\dagger E_j.
\tag{Q2.3}
\]

An exact formula for \(\kappa_A=c\) consists of \(0\le c\le2\), the universal condition

\[
[Z,\iota(U)]^\dagger[Z,\iota(U)]\preceq c^2 I_d
\tag{Q2.4}
\]

for every \(Z\) represented by (Q2.3) with \(Z^\dagger Z\preceq I_d\) and every unitary tuple \(U\), and an attaining witness \(Z,U,v\) with \(v^\dagger v=1\) and

\[
\|[Z,\iota(U)]v\|^2=c^2.
\tag{Q2.5}
\]

The unitary reduction follows by the same two-unitary averaging argument. For each fixed channel, the actual set \(\mathcal K_N\cap\{\|Z\|\le1\}\) is compact, so a witness exists. The coefficients \(\lambda_{ij}\) need not be bounded; they are quantified coordinates, not an incorrectly asserted compact parameterization of that unit ball.

Conjoin (Q2.2), (Q2.3)–(Q2.5), channel constraints and any extra polynomial restrictions, then eliminate all variables except \((c,z)\). This computes the attainable semialgebraic set. A nonempty bounded one-dimensional section at algebraic \(c\) has algebraic endpoints, computable from its polynomial description. Direct membership tests decide attainment; sample points in the open tolerance intervals provide near-extremal algebraic channels.

Although the Kraus parameter space is compact, a level set of the **normalized span defect** need not be closed. The proof uses supremum/infimum and tests attainment separately; it does not assume compactness of a defect slice. ∎

For a concrete requested envelope, (Q2.1)–(Q2.5) are the algorithm specification. No general elimination output is supplied in this release. The earlier full-algebra formulas and the certified examples below remain the evaluated cases.

## 4. BM23-Q3 — Exact recovery of classical labels carried by quantum states

Consider the native channel

\[
N(\rho)=\sum_{i=1}^r\rho_{ii}\sigma_i,
\]

where the supplied signal matrices \(\sigma_i\in M_b\) are density operators, and take the diagonal logical algebra \(A\subset M_r\). Let

\[
p_* = \max_{F_i\succeq0,\ \sum_iF_i=I_b}\min_i\operatorname{tr}(\sigma_i F_i).
\]

Then

\[
\boxed{\delta_A(N)=2(1-p_*)},\qquad
\boxed{p_* = \min_{\lambda_i\ge0,\ \sum_i\lambda_i=1; Y=Y^\dagger,\ Y\succeq\lambda_i\sigma_i}
\operatorname{tr}Y.}
\tag{Q3.1}
\]

Both optima are attained. These are worst-case recovery statements, not a substitution of an average-case probability for BM's operator norm.

**Proof.** A recovery adjoint maps the diagonal rank-one projectors to a POVM \((F_i)\). Conversely, any POVM is realized by measuring it and preparing the corresponding logical basis state. The composed classical transition probabilities are

\[
p_{j|i}=\operatorname{tr}(\sigma_i F_j).
\]

For \(X=\operatorname{diag}(z_1,\ldots,z_r)\), \(|z_i|\le1\), the reconstructed error at input label \(i\) is \(z_i-\sum_jp_{j|i}z_j\). Its supremum modulus is the row's coefficient \(\ell_1\)-norm, namely \(2(1-p_{i|i})\). It is attained by \(z_i=1\), \(z_j=-1\) for \(j\ne i\). The maximum over rows commutes with this finite supremum, proving the first identity even for complex inputs.

The primal maximizes \(q\) subject to \(\operatorname{tr}(\sigma_iF_i)\ge q\) and the POVM constraints. Its Lagrangian is

\[
(1-\textstyle\sum_i\lambda_i)q+\operatorname{tr}Y
+\sum_i\operatorname{tr}[(\lambda_i\sigma_i-Y)F_i].
\]

Taking its supremum over free \(q\) and positive semidefinite \(F_i\) is finite precisely under the displayed dual constraints, yielding \(\operatorname{tr}Y\). Strict primal feasibility holds with \(F_i=I_b/r\), \(q=0\), and strict dual feasibility with \(\lambda_i=1/r\), \(Y=2I_b\). Finite-dimensional semidefinite duality gives equality [W11]. Compactness gives primal attainment. For the dual one may restrict to \(\operatorname{tr}Y\le1\): the choice \(Y=\sigma_1\), \(\lambda_1=1\), \(\lambda_{i>1}=0\) is always feasible with trace one. The dual constraints imply \(Y\succeq0\); bounded trace and the probability simplex then give a compact minimizing set. ∎

A directly checkable certificate consists of a POVM with every success at least \(q\), and dual-feasible \((\lambda,Y)\). Weak duality alone proves

\[
2(1-\operatorname{tr}Y)\le\delta_A(N)\le2(1-q).
\tag{Q3.2}
\]

When \(q=\operatorname{tr}Y\), the value is exact. The delivered verifier checks real-rational certificates by exact Schur complements, including zero pivots. It does not use numerical eigenvalue thresholds.

For example, take

\[
\sigma_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\sigma_2=\frac1{25}\begin{pmatrix}9&12\\12&16\end{pmatrix},
\]

\[
F_1=\frac1{10}\begin{pmatrix}9&-3\\-3&1\end{pmatrix},\quad F_2=I-F_1,
\quad\lambda_1=\lambda_2=\tfrac12,
\quad Y=\frac1{50}\begin{pmatrix}27&6\\6&18\end{pmatrix}.
\]

Both primal successes and \(\operatorname{tr}Y\) equal \(9/10\); both dual slacks are positive semidefinite of rank one. Thus \(\delta_A=1/5\), exactly. The package also certifies four BB84 signal states (error 1), identical states (error \(2-2/r\)), orthogonal states (error 0), and symmetric classical channels with diagonal success \(3/4\) (error \(1/2\)).

## 5. BM23-Q4 — Exact common-recovery capability budgets

Fix one algebraic finite-dimensional channel and a finite algebraic catalogue \(A_1,\ldots,A_s\). Require a **single** recovery \(R\) to meet all error budgets. Define

\[
\mathcal B=\{t\in[0,2]^s:\exists R\ {\rm CPTP},\ e_{A_j}(R)\le t_j\ \forall j\}.
\]

Then \(\mathcal B\) is compact, convex, upward closed within its box, and effectively semialgebraic. For algebraic budget inputs, feasibility and Pareto membership are decidable; algebraic weighted-sum optima and algebraic recovery witnesses are computable.

**Proof.** Use one full recovery-adjoint Choi matrix \(H=[H_{uv}]_{u,v=1}^d\succeq0\), \(H_{uv}\in M_b\), \(\sum_uH_{uu}=I_b\). For each algebra add the corresponding universally quantified unitary inequalities from (Q2.1), using this same \(H\). This is a polynomial formula and is therefore effectively semialgebraic after elimination.

The channel set and budget box are compact. Each error functional is continuous, so the joint feasible set is closed and its projection compact. Error is convex in a recovery; mixing two recoveries and their budgets proves convexity. Upward closure follows directly from the inequalities. Pareto membership is the first-order condition

\[
t\in\mathcal B\quad\wedge\quad
\neg\exists u\in\mathcal B\ [u\le t\ \wedge\ \bigvee_j u_j<t_j].
\]

Algebraic sampling and compact minimization handle weighted sums. ∎

Separate algebra-specific optima do not, by themselves, furnish the required shared recovery. The common Choi variable is essential. This theorem supplies a finite catalogue formulation; it does not assert that all approximate capabilities have a greatest algebra.

## 6. BM23-I1 — Finite causal prediction from a uniform decay bound

Let a native deterministic system have a finite action alphabet of size \(s\ge1\), total action maps, an initial set \(X_0\), and a task \(\tau:X\to\mathbb R^p\), \(p\ge1\). Suppose supplied rational constants \(M\ge0\), \(0\le L<1\) certify

\[
\|\tau(f_w(x))\|_2\le ML^{|w|}
\quad(x\in X_0,\ \text{every finite action word }w).
\tag{I1.1}
\]

Assume each finite response \(\tau(f_w(x))\) can be computed to any prescribed coordinate accuracy from the native description of \(x\). Then for every rational \(\varepsilon>0\) a finite causal machine admits effective admissible initialization achieving error at most \(\varepsilon/2\), uniformly over all initial states, action sequences and times. The procedure takes a supplied finite-response evaluation oracle and may select different valid codes from different descriptions of the same state.

No compactness of \(X_0\), common eigenbasis, or commutation of the actions is required. At the set level one may select one admissible code for each state; the effective procedure does not promise a canonical extensional or continuous finite-valued quantizer.

**Construction and proof.** Choose the least \(K\ge0\) with \(ML^K\le\varepsilon/2\), with \(L^0=1\). Let

\[
h=\varepsilon/(2p),\qquad
J=\lceil M/h\rceil+1,\qquad Q=(2J+1)^p.
\]

For every word of length below \(K\), compute its task to coordinate error at most \(\varepsilon/(4p)=h/2\), then round each coordinate to the nearest multiple of \(h\). The total coordinate error is at most \(h\). Each integer grid label lies between \(-J\) and \(J\).

The initial machine state is the resulting labelled full \(s\)-ary response tree of depth \(K\). Its output is the root label times \(h\). An action selects the corresponding child tree. At depth zero it enters a zero-output absorbing state. These updates are well-defined on the finite universal codebook of all such labelled trees, independent of the particular initialized native state.

At times \(t<K\), the stored subtree root is exactly the quantized initial response for the action prefix actually taken. Its error is at most \(\sqrt p\,h=\varepsilon/(2\sqrt p)\le\varepsilon/2\). At \(t\ge K\), (I1.1) bounds the native task's distance from the absorbing output by \(ML^t\le\varepsilon/2\).

Writing \(N_r=1+s+\cdots+s^{r-1}\), a universal state bound is

\[
\boxed{1+\sum_{r=1}^K Q^{N_r}.}
\tag{I1.2}
\]

The sum is zero when \(K=0\). This is an existence and effective construction bound, not a minimum-state claim. ∎

The finite code carries remaining forecast depth. Every admissible initial code satisfies the bound, so uniqueness of initialization is unnecessary. A continuous finite-valued initializer on a connected native carrier would be constant; no such initializer is asserted here. It need not equal a fixed instantaneous encoding of the current native state. Thus this is a causal-history construction, not a new exact-quotient theorem. Its assumptions do not include persistent forcing or arbitrary partial-action boundaries.

### A noncommuting infinite-dimensional witness

On the unit ball of \(\ell_2(\mathbb N_0)\), let \(S\) be the unilateral right shift,

\[
f_0(x)=\tfrac12Sx,\qquad f_1(x)=\tfrac12S^*x,
\qquad\tau(x)=(x_0,x_1).
\]

Both action norms are \(1/2\), and the task norm is at most the state norm. Hence (I1.1) holds with \(M=1,L=1/2\). The actions do not commute: \(S^*S=I\), whereas \(SS^*=I-P_0\). Their initial unit ball is not norm compact. This example therefore lies beyond a shared diagonal contraction model.

For \(\varepsilon=1/8\), the construction uses \(K=4\), \(h=1/32\), \(J=33\), and \(Q=4489\). Its universal codebook bound is

\[
1+4489+4489^3+4489^7+4489^{15}.
\]

Only a depth-four tree is built for each initialized input. The package replays every binary action word through length nine for 24 rational initial states, both with exact profile values and deliberately perturbed values within the allowed oracle accuracy. All 49,104 checks pass; the largest observed squared error is \(1/256\). The analytic operator-norm argument, not this finite replay, proves the bound for the entire infinite-dimensional unit ball and all times.

## 7. BM23-I2 — No universal additive approximation algorithm

There is no algorithm that, for every computable infinite-carrier deterministic system with bounded rational task values, always returns the optimal infinite-horizon one-state prediction error to additive accuracy \(1/5\). There is also no algorithm that always returns a one-state predictor whose error is within \(1/5\) of the optimum. This already holds for one fixed native update \(f(n)=n+1\) on \(\mathbb N_0\), one initial state \(n=0\), and scalar task values in \(\{0,1\}\).

**Proof.** Given a program \(e\), define \(\tau_e(0)=0\). For \(n\ge1\), simulate \(e\) for \(n-1\) transitions and put \(\tau_e(n)=1\) if it has halted, and zero otherwise. This is a uniformly computable rational-valued task: each individual evaluation requires only a finite simulation.

A one-state predictor outputs a constant \(c\). If \(e\) never halts, the trajectory is constantly zero and the optimal error is zero. If \(e\) halts, the trajectory contains both zero and one, so

\[
\inf_c\sup_{n\ge0}|\tau_e(n)-c|
=\inf_c\max\{|c|,|1-c|\}=\tfrac12.
\]

An additive-\(1/5\) value approximation must lie in \([-1/5,1/5]\) in the first case and \([3/10,7/10]\) in the second. Comparing it to \(1/4\) decides halting, which is impossible. A returned near-optimal constant must lie in \([-1/5,1/5]\) in the first case and \([3/10,7/10]\) in the second, so it gives the same contradiction. For a computable-real output, the separated intervals allow a finite-precision comparison.

Likewise, deciding feasibility of one-state error \(1/4\) would decide nonhalting. ∎

This rules out an unrestricted algorithmic completion demand. It does not prevent solving a specified native instance, a finite carrier, or the effective decay class in BM23-I1. In the reduction the missing uniform tail information is substantive, not an implementation inconvenience.

## 8. Verification, disposition and residual obligations

The exact certificate program validates 15 quantum optima. Its critical PSD routine agrees with an independent all-principal-minors oracle on 854 symmetric rational matrices. Nine deliberately corrupted quantum inputs are rejected. The response-tree implementation passes 49,104 trajectory checks and eight invalid-parameter/action rejection checks. These checks validate the supplied implementations; the general theorems are established by the arguments above.

| Existing obligation | Disposition after this note | Still not claimed |
|---|---|---|
| Finite quantum optimum for a specified algebraic channel/algebra | Exact attained algebraic optimum and terminating algorithm specification | A general QE implementation or efficient solver |
| Sharp proper-algebra defect envelopes in a fixed finite algebraic class | Effective semialgebraic characterization; endpoint and attainment procedures | Evaluated closed-form envelopes for every class |
| Finite catalogue under a common quantum recovery | Exact semialgebraic compact convex budget set | A greatest approximate observable algebra in every setting |
| General infinite-carrier predictor optimization | A universal additive approximation algorithm is impossible | An algorithm for all computable native inputs |
| Infinite-dimensional causal prediction under uniform task decay | Explicit finite construction with a state bound | Minimum state count, persistent forcing, or exact current-state closure |
| Unrestricted continuous four-state Jordan optimum | Unchanged: squared error lies in the prior certified interval | An exact unrestricted optimum |
| All global regular realization and nonlinear repair classes | Unchanged outside established contracts | A universal classification or universally valid repair |

These results narrow the research boundary. They do not justify marking the six broad extension rows as wholly solved. The V1 framework's completion gate was already internally met; that is a separate and narrower claim than exhausting the research programme.

## References

- **[W18]** John Watrous, *The Theory of Quantum Information*, Chapter 2, especially Theorem 2.22 and channel characterizations. [Author-hosted chapter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf). Used for the standard Choi criterion and native channel conventions.
- **[W11]** John Watrous, *Theory of Quantum Information*, Lecture 8, optimal-measurement semidefinite programs. [Author-hosted notes](https://cs.uwaterloo.ca/~watrous/TQI-notes/TQI-notes.08.pdf). Used for standard measurement optimization/duality; the minimax recovery reduction is written above.
- **[CM12]** Cyril Cohen and Assia Mahboubi, “Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination,” *Logical Methods in Computer Science* 8(1:02), 2012. [Journal article](https://lmcs.episciences.org/844). Used for effective real-closed-field quantifier elimination; no claim is made that the new BM formulas have been formally verified by that work.
- **[BM18]** *BM Completion Development*, 18 October 2026, especially Q1–Q5 and A1–A3. Included in the prior development package.
- **[BM20]** *BM Continuous Closure and Completion*, 20 October 2026, especially C1–C3, Q1–Q3 and I1.
- **[BM21]** *BM Jordan Returns and Certified Bounds*, 21 October 2026. Its exact rational Jordan certificates remain unchanged.
