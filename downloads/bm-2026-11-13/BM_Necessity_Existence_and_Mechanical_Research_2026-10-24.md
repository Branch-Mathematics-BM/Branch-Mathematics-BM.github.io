# Branch Mathematics: necessity, constructive existence, and mechanical tests

24 October 2026. Additive research note for the frozen BM V1 / Edition 1.1 foundation. DR1–DR7 are local labels, not replacements for canonical theorem identifiers. Proofs and computations here have received internal checking only. No historical novelty, independent review, or new physical law is claimed.

## What this investigation establishes

BM has a defensible mathematical purpose: identify which distinctions and compatibility conditions a declared task requires, demonstrate when available representations cannot preserve them, and construct or reject a repair. This investigation strengthens that purpose with noisy-observation criteria, exact repair dimensions, sharp error bounds, and a mechanical example suggested by the user.

The strongest additional mechanical result is simple: **position, energy, and angular momentum together need not determine the next position.** Two Newtonian orbital states can agree on all three and differ in whether they are moving inward or outward. The missing distinction produces a rigorous prediction obstruction.

Three claims have different evidence requirements:

| Claim | Evidence supplied here | Limit |
|---|---|---|
| Some distinctions or structures are necessary | Explicit pairs of indistinguishable inputs, separating futures, error lower bounds, and an incompatible collection of constraints | Relative to a stated task, observation set, model class, and tolerance |
| Declared BM configurations have mathematical realizations | Explicit finite quotients, linear state realizations, and mechanical models satisfying their declared obligations | Constructive existence for these configurations, not a consistency proof for every proposed extension |
| BM offers value beyond independently using established theories | A common record of information, evolution, noise, interventions, and global compatibility | Comparative workflow advantage and historical originality remain unestablished |

The literature independently establishes the importance of these problems. It does not establish that BM is the only framework capable of addressing them. Existing methods should be incorporated and credited wherever they already answer the question.

## 1. Primary research that changes the assessment

The following comparison uses original papers or author manuscripts, not promotional summaries. The search is targeted, not an exhaustive priority review.

| Research | What it establishes in its own scope | Consequence for BM |
|---|---|---|
| Shalizi and Crutchfield, computational mechanics [CM] | Causal states group histories by their predictive distributions; the paper proves predictive sufficiency, minimality, and uniqueness results | BM's deterministic future equivalence has a close established predictive analogue. Stochastic equivalence needs conditional distributions and its own assumptions. |
| Chorin, Hald, and Kupferman, optimal prediction and Mori–Zwanzig [MZ] | Eliminating unresolved variables leads to projected equations with memory and an unresolved contribution | Supports BM's distinction between present output and autonomous reduced state. Memory is an established repair mechanism; it is not a missing new force. |
| Ovchinnikov and colleagues, CLUE [CLUE] | Computes minimal constrained linear lumpings for polynomial differential equations, preserving specified linear observables | A direct comparison method for BM's exact reductions. A linear observability calculation alone cannot establish novelty. |
| Ettehad and Foucart, recovery with observation errors [OR] | Constructs optimal recovery maps under bounded noise; Theorem 4 covers linear functionals and includes DR4 below as a specialization | The robust error formula should be credited to optimal recovery. BM can connect it to a declared future task and a repair decision. |
| Foucart and Liao, intersected hyperellipsoids [OR24] | Gives radius-of-information and optimal-recovery results for two quadratic constraints, including inaccurate data | Supplies a more powerful baseline for future vector-valued BM repair solvers. Extending a two-constraint conclusion to arbitrary constraints requires proof. |
| Beckers and Halpern [CA]; Beckers, Eberhardt, and Halpern [CAA] | Define exact and approximate causal abstractions with explicit intervention requirements | Agreement on passive observations does not by itself establish an intervention-preserving bridge. |
| Abramsky and Brandenburger [GL] | Relates contextuality to obstructions to global sections, with explicit measurement and probability structures | Gives a precise comparison for BM's local-versus-global realization obligations. The Boolean example here is a classical constraint example, not experimental quantum evidence. |

These comparisons support the **need to handle the obligations**. They also narrow the originality question: the contribution to investigate is a useful, precise coordination of obligations across native sectors, with certificates and repairs. It is not that prediction, memory, observability, or gluing were previously unknown.

## 2. DR1 — constructive existence with imperfect observations

Let X be a nonempty state set, with a set of partial deterministic actions f_a and required task O. Adjoin an absorbing unavailable state ⊥, tagged differently from every legitimate task value. Write x E_* y when every finite action word gives the same tagged task from x and y. This includes the empty word and the availability of each continuation.

Replace a perfect observation V(x) by a nonempty set Γ(x) of possible observed values. No distribution is assumed. An initializer h(z) must work for every z in Γ(x), and its deterministic autonomous updates must reproduce every required task and action availability. It cannot obtain further measurements after initialization under this contract.

**Theorem.** Such a set-valued-noise-robust exact implementation exists if and only if

\[
\boxed{\Gamma(x)\cap\Gamma(y)\ne\varnothing\ \Longrightarrow\ xE_*y.}
\tag{DR1}
\]

When it exists, the smallest cardinality of the realized code set is |X/E_*|.

**Proof.** If a common measurement z is possible from two states, the initializer supplies the same code h(z). Deterministic execution gives identical future tasks and availability, so the states must be E_*-equivalent. Conversely, when the condition holds, assign each realized measurement z the unique E_* class of its compatible states. Equality of all future tasks makes the class update and output maps well defined, including partial-action domains. This constructs a correct implementation. Any correct implementation must use distinct codes for different future classes, because a shared code would give identical future behavior. Choosing one possible measurement for each class gives the cardinal lower bound, attained by the quotient construction. ∎

This permits different noisy measurements of one state to initialize the same quotient class. It does not assert a continuous or computable initializer, and it does not treat fresh observations, filtering, randomized risk, or physical hardware without additional structure.

**Finite certificates.** A negative certificate consists of x, y, a common possible measurement z, and a finite action word with unequal tagged outputs. A positive certificate specifies quotient outputs, action tables, and the class assigned to each realized measurement. The supplied verifier compares the criterion with an independent enumeration of all native congruence partitions for small systems.

**BM interpretation.** This supplies nontrivial positive realizations as well as impossibility witnesses. A framework that only declares failures would be weaker; DR1 says exactly when this particular repair exists.

## 3. DR2 — positive noise changes what “complete” can mean

Assume X is connected, V:X→R^m is continuous, and Γ(x) is the closed Euclidean ball of a fixed radius η>0 around V(x).

**Corollary.** A robust exact implementation under DR1 can exist only if every state has the same required future task-and-availability profile.

**Proof.** Each x has a neighborhood in which ||V(y)−V(x)||<2η. The two measurement balls then intersect, so DR1 forces y E_* x throughout that neighborhood. Thus every E_* class is open. Its complement is a union of open classes, hence is also open. Connectedness permits only one nonempty class. ∎

This is not an objection to useful measurement. It says that worst-case exactness for a nonconstant continuous-state task cannot be promised under a positive bounded-noise model. One must state a tolerance, change the admissible state set, or change the observation assumptions. Simply adding finitely many ordinary continuous noisy channels does not remove this obstruction if the resulting observation set still contains a fixed positive-radius ball.

Discrete states with adequately separated observation sets can still satisfy DR1. The connectedness and noise-interior assumptions are substantive.

## 4. DR3 — quantify the missing information for linear evolution

Let ẋ=Ax on R^n, with required future output L exp(tA)x for every t≥0 and available noiseless observation Bx. Define

\[
\mathcal O_L=\begin{bmatrix}L\\LA\\\vdots\\LA^{n-1}\end{bmatrix}.
\]

The future-invisible differences form ker O_L. If every future output of a difference vanishes, its derivatives at zero give LA^k x=0. Conversely, Cayley–Hamilton makes every higher power a combination of the first n powers; the exponential series then gives vanishing at all times.

An exact autonomous code computed only from Bx exists if and only if

\[
\boxed{\ker B\subseteq\ker\mathcal O_L}
\quad\Longleftrightarrow\quad
\operatorname{row}\mathcal O_L\subseteq\operatorname{row}B.
\tag{DR3a}
\]

Necessity holds even if arbitrary deterministic encoders are allowed. For sufficiency, choose a matrix Q whose rows form a basis of row O_L. This row space is A-invariant; therefore QA=HQ and L=DQ for suitable matrices H,D. Then z=Qx obeys ż=Hz and has output Dz. If DR3a holds, Q=KB for some K, so initialization uses only the available observation.

The minimum dimension among linear exact codes is rank O_L: any exact linear code must determine all rows of O_L, and Q attains the bound.

If additional arbitrary noiseless linear scalar observation channels may be installed, their minimum number is

\[
\boxed{k_{\min}=\operatorname{rank}\begin{bmatrix}B\\\mathcal O_L\end{bmatrix}
-\operatorname{rank}B.}
\tag{DR3b}
\]

Each new row can increase the available row-space dimension by at most one. Conversely, a basis for the image of row O_L modulo row B supplies exactly that many rows. This proves both bounds.

This is classical observability and linear algebra expressed as a BM repair contract. It does not solve selection from a restricted sensor catalogue, sensor placement costs, noisy recovery, or nonlinear code dimension. If B itself must remain recoverable, replace the task L by the stacked task [L;B] before forming the observability stack.

## 5. DR4 — an exact error floor, including every nonlinear decoder

Normalize the admissible state set to ||x||₂≤1. Measure z=Bx+e with ||e||₂≤η. The task is the scalar ℓᵀx. Define

\[
e_* = \inf_d\ \sup_{\|x\|\le1,\ \|e\|\le\eta}
|\ell^Tx-d(Bx+e)|,
\]

where d ranges over all deterministic decoders. Then

\[
\boxed{
e_*=\max_{\|v\|\le1,\ \|Bv\|\le\eta}|\ell^Tv|
=\min_a\bigl(\|\ell-B^Ta\|_2+\eta\|a\|_2\bigr).
}
\tag{DR4}
\]

**Proof.** For each feasible v, the states ±v with errors ∓Bv both produce measurement zero. At least one error of any common decoded value is at least |ℓᵀv|. For η>0, equip pairs (x,e) with norm max(||x||,||e||/η). On the kernel of the map (x,e)↦Bx+e, the functional (x,e)↦ℓᵀx has norm equal to the displayed maximum. Hahn–Banach extends that restricted functional with the same norm. Every such extension differs from ℓᵀx by a functional aᵀ(Bx+e); its norm is ||ℓ−Bᵀa||+η||a||. The decoder d(z)=aᵀz therefore attains the lower bound. For η=0, orthogonally project ℓ onto row B; the residual norm equals the maximum on the unit ball in ker B. ∎

DR4 is explicitly a special case of [OR], Theorem 4: take its native space to be Euclidean, its approximating subspace V={0}, its model radius ε=1, and its noise exponent p=2. The proof here makes the witness and BM interpretation explicit; it is not a priority claim.

For a fixed finite family of scalar tasks with the maximum absolute-coordinate loss, solve each coordinate problem; the optimum is the maximum of their values. This does not automatically construct a dynamically consistent trajectory or a physically admissible vector output. Those are additional receiver requirements.

**Exact arithmetic example.** Set B=[1,0], ℓ=(4/5,3/5), η=3/5. The pair v=±(3/5,4/5) gives a lower bound 24/25. The linear decoder coefficient a=7/20 gives residual norm 3/4 and noise contribution 21/100, totaling 24/25. The companion script checks the matching rational certificate.

## 6. DR5 — oscillator benchmark: sufficiency, noise, and sampling

For a harmonic oscillator with known ω>0, use the normalized state (q,p), where p=v/ω. Choose a common displacement scale so q²+p²≤1 is dimensionless. The equations are

\[
\dot q=\omega p,\qquad \dot p=-\omega q,\qquad
q(t)=q_0\cos\theta+p_0\sin\theta,\quad\theta=\omega t.
\]

### Current position alone

Measuring z=q₀+e with |e|≤η gives the exact minimum worst-case error for predicting q(t):

\[
e_q(\theta,\eta)=
\begin{cases}
1,&\eta\ge|\cos\theta|,\\
|\cos\theta|\eta+|\sin\theta|\sqrt{1-\eta^2},&0\le\eta<|\cos\theta|.
\end{cases}
\tag{DR5a}
\]

The second case necessarily has η<1. To prove the formula, apply DR4 and maximize c u+s√(1−u²) over 0≤u≤min(η,1), where c=|cos θ| and s=|sin θ|. Its unconstrained maximum occurs at u=c. At zero noise, e_q=|sin θ|. At a quarter period, even perfect present position leaves worst-case future error one.

### Add one actual historical position measurement

With h≥0 and α=ωh, the two observations satisfy

\[
\begin{bmatrix}q(0)\\q(-h)\end{bmatrix}
=B_h\begin{bmatrix}q_0\\p_0\end{bmatrix},\qquad
B_h=\begin{bmatrix}1&0\\\cos\alpha&-\sin\alpha\end{bmatrix}.
\]

This history must actually be available. It cannot be inferred from current position alone. The matrix is invertible exactly when sin α≠0; its squared singular values are 1±|cos α|.

For total two-measurement error ||e||₂≤η, the exact optimum for recovering the whole normalized state in Euclidean norm is

\[
e_{\rm state}=
\begin{cases}
\min\{1,\eta/\sqrt{1-|\cos\alpha|}\},&\sin\alpha\ne0,\\
1,&\sin\alpha=0.
\end{cases}
\tag{DR5b}
\]

**Proof.** Along a unit weakest right singular vector, take v with norm min(1,η/σ_min). The states ±v can produce the same zero measurement, proving the lower bound. Inversion gives error at most η/σ_min; the zero estimate gives error at most one. Use whichever bound is smaller. If the state estimate must remain in the unit disk, project the inverse estimate onto the disk; Euclidean projection cannot increase its distance from any admissible true state. At rank deficiency a unit kernel vector proves error one, attained by the zero estimate. ∎

The estimated state then follows the genuine oscillator dynamics. Rotation preserves its error, and

\[
\sup_{t\ge0}|q_x(t)-q_{\hat x}(t)|=\|x-\hat x\|_2.
\]

Thus DR5b also solves the full-future position problem when the output must be a single lawful oscillator trajectory. This avoids relying on incompatible coordinate-by-coordinate answers.

For η=0.1, with T=2π/ω:

| Sample spacing h/T | Minimum worst-case state error |
|---:|---:|
| 0.01 | 1.000000 |
| 0.05 | 0.452015 |
| 0.10 | 0.228825 |
| 0.25 | 0.100000 |
| 0.49 | 1.000000 |
| 0.50 | 1.000000 |

An arbitrarily small nonzero gap can make the noiseless matrix invertible while leaving noisy recovery nearly useless. Quarter-period spacing is optimal under this normalization and fixed total noise norm. It is not a universal prescription for unknown frequency, damping, correlated errors, or a fixed measurement-time budget.

### The task can remove the need for a distinction

If the task requests position only at multiples of half a period, q(nT/2)=(-1)^n q₀. Position alone then has an exact autonomous sampled update q↦−q. Velocity remains necessary for the full continuous future, but is unnecessary for this sampled task. This is a direct test of BM's receiver-relative essentiality; a universal claim that “velocity must always be retained” would be false.

## 7. DR6 — the user's orbit and ice-skater example

### What is conserved, and what changes

For a skater with negligible external torque, angular momentum is L=Iω. Pulling mass inward reduces I, so ω increases. Rotational kinetic energy is

\[
K_{\rm rot}=\tfrac12 I\omega^2=\frac{L^2}{2I}.
\]

It therefore increases as I decreases at fixed L. The skater's work supplies the increase; chemical energy is converted into mechanical energy. This is the standard analysis in [PHY1]. Conservation of angular momentum does not imply conservation of rotational kinetic energy.

For a Newtonian test mass in a fixed central field μ=GM, angular momentum per unit mass is h=r v_θ, so v_θ=h/r and angular speed is h/r². These formulas concern the transverse component. Total speed also includes radial motion. The specific mechanical energy is

\[
\varepsilon=\tfrac12(\dot r^2+h^2/r^2)-\mu/r.
\tag{DR6a}
\]

As a body moves inward along one unforced Kepler orbit, gravitational potential energy decreases and kinetic energy increases while ε remains constant. Along a bound orbit of semimajor axis a, rearranging ε=−μ/(2a) gives v²=μ(2/r−1/a). Kepler's changing orbital speed is documented in [PHY2].

For example, in normalized units μ=1, an ellipse with a=1 and eccentricity 3/5 has:

| Quantity per unit orbiting mass | Apoapsis | Periapsis |
|---|---:|---:|
| Radius | 8/5 | 2/5 |
| Speed | 1/2 | 2 |
| Angular momentum h | 4/5 | 4/5 |
| Kinetic energy | 1/8 | 2 |
| Gravitational potential energy | −5/8 | −5/2 |
| Total mechanical energy | −1/2 | −1/2 |

The kinetic gain 15/8 exactly matches the potential decrease. Energy has changed form. Comparing two different circular orbits is a different operation: circular speed scales as r^(−1/2), and transferring between those orbits changes the orbital energy and angular momentum. It is not the fixed-h contraction formula.

### A rigorous necessity witness for BM

Take μ=1 and the two planar states

\[
x_-=(\mathbf r=(1,0),\mathbf v=(-1/2,1)),\qquad
x_+=(\mathbf r=(1,0),\mathbf v=(1/2,1)).
\]

Both have the same position, specific angular momentum h=1, and specific energy ε=−3/8. Let the retained representation be

\[
R(x)=(\mathbf r,\varepsilon,h).
\]

Then R(x_-)=R(x_+), but their initial radius derivatives are −1/2 and +1/2. The native vector field is smooth away from collision, so uniqueness gives two locally defined trajectories whose radii differ for all sufficiently small positive times. More precisely,

\[
r_+(t)-r_-(t)=t+o(t).
\]

Any radius predictor initialized only from R must issue the same prediction for both states. Its worst error is therefore at least |r_+(t)−r_-(t)|/2, with asymptotic ratio to t at least 1/2.

The numerical illustration gives a radius separation of about 0.0998326673 at normalized t=0.1, hence a lower-bound illustration of 0.0499163336. These decimals are numerical, not interval-certified constants. The exact initial witness and derivative argument establish the impossibility independently of integration.

**Repair.** Retain (r,φ,u,h), where u=dr/dt. On r>0 the native reduced equations are

\[
\dot r=u,\qquad \dot\phi=h/r^2,\qquad
\dot u=h^2/r^3-\mu/r^2,\qquad \dot h=0.
\tag{DR6b}
\]

They are autonomous and determine the position task. Away from turning points, energy and h recover |u| but not its sign. An instantaneous sign label alone is not a complete smooth evolution law through turning points; retaining u with DR6b gives a regular repair on r>0. This is familiar phase-space mechanics, now accompanied by an explicit certificate showing why the proposed smaller representation fails.

### Spin's gravitational effect is a separate question

Orbital angular momentum, a body's rotation about its own axis, and angular momentum's contribution to relativistic gravity are distinct. Ordinary attraction remains for a nonrotating mass. Source rotation adds frame dragging in general relativity; Gravity Probe B tested that effect [PHY3]. In the weak-field far zone the characteristic spin-precession scale is GJ/(c²r³), with direction and numerical factors depending on the observable [PHY4, equation 33, leading angular-momentum moment]. Its falloff should not be substituted for the Newtonian mass-acceleration law GM/r²; the two quoted quantities even have different units.

The ice-skater analogy therefore supports a precise conservation-law comparison. It does not demonstrate that spin creates gravity, that energy increases without a source, or that BM supplies a new gravitational field equation.

## 8. DR7 — independent failures of interventions and joint realization

### Passive equivalence can hide an intervention distinction

Consider two deterministic structural causal models with binary exogenous U:

- M₁: X=U and Y=X.
- M₂: Y=U and X=Y.

Both give (X,Y)=(U,U) in passive observations. At U=1, an intervention do(X=0) produces Y=0 in M₁ and Y=1 in M₂. Thus any predictor supplied only the passive observation (1,1), while both models remain admissible, cannot determine this intervention response. Its worst absolute error for Y is at least 1/2. A model-discriminating assumption or experiment is required. Assigning a probability without justification does not remove the worst-case ambiguity.

This is an elementary causal-identifiability example, consistent with the intervention-sensitive abstraction requirements in [CA, CAA]. It supplies no evidence that either model describes an actual physical system.

### Every local piece can be satisfiable while the whole is not

Let a,b,c be Boolean. Three native constraints are a=b, b=c, and a≠c. Every individual constraint has four assignments, and every pair has two assignments. All three together have zero. Projection onto each shared single variable permits both values, so compatibility at that limited interface also fails to detect the global contradiction.

The complete set of three constraints is a minimal unsatisfiable core. A repair must change a declared constraint or the allowed interpretation; merely joining locally accepted results does not produce a realization. This illustrates BM's nonemptiness obligation. It is already expressible in constraint satisfaction and local-to-global mathematics; [GL] supplies a richer comparison under its own measurement assumptions.

These examples prevent a one-test definition of “complete.” Present observation, future closure, intervention fidelity, robustness, and global realization can fail for different reasons.

## 9. Verification and its limits

The companion Python file and JSON report are reproducible from this folder.

| Check | Outcome |
|---|---|
| Exact noisy-initialization criterion versus independent partition enumeration | 524 instances: 324 exhaustive two-state instances and 200 seeded instances |
| Positive / negative finite cases | 214 feasible; 310 infeasible; all 310 selected negative witnesses replayed |
| Exact rational linear repair checks | 60 seeded systems; subset search independently matched minimum added-channel counts; one explicit oscillator |
| Oscillator scalar formula versus one-dimensional optimization | 160 comparisons; maximum difference 2.23×10⁻¹⁶ |
| Two-sample oscillator formula versus singular-vector witnesses | 160 comparisons; maximum difference 4.45×10⁻¹⁶ |
| Rank and tiny-sample-spacing edge cases | Four checks; stable singular-value formula avoids falsely declaring a small nonzero gap singular |
| Rational lower/upper certificates | Scalar optimum 24/25; a two-sample state-error square 1/40 |
| Orbital example | Exact equal energy/angular momentum witness; two numerical trajectories with energy and angular-momentum drift below 3×10⁻¹² |
| Causal and global constraints | Exact binary enumeration reproduces intervention disagreement and the minimal unsatisfiable core |

The general results depend on the written proofs. Numerical checks detect implementation mistakes but do not prove theorems, estimate laboratory performance, or establish priority. No third-party solver package was benchmarked for speed or predictive superiority. No observational data were used to infer a new physical law. The arbitrary-noise theorem is set-level; the mechanical noise example uses a known oscillator and a fixed normalized uncertainty set.

## 10. What would further establish BM's added value

The next comparison should test a falsifiable workflow claim: **does explicitly transporting obligations and counterexamples across several native models prevent errors, reduce unnecessary retained information, or reduce verified repair cost?** It should not ask whether BM beats ordinary algebra at a calculation that algebra already solves.

| Research question | Concrete test and comparator | What would count against BM |
|---|---|---|
| Does BM catch cross-model failures reliably? | Preregister a set of hidden-information, partial-domain, noisy, intervention, and incompatible-interface cases; compare a BM audit with a fully specified native-method workflow | Equal or worse accuracy without an offsetting cost or clarity benefit |
| Is there a theorem-level contribution? | Translate one candidate BM result both ways into bisimulation, constrained lumping, optimal recovery, or contracts; state exactly which assumptions or conclusions differ | An equivalence showing the claimed new result is just a relabeling |
| Does the repair reduce actual cost? | Restrict to a physically justified sensor/encoder catalogue; measure acquisition cost, computation, and achieved error using identical data and budgets | Cheaper native solutions omitted from the catalogue, or no observed improvement |
| Does a physical interpretation add a prediction? | Derive a definite observable with units, parameters, uncertainty, and a prediction distinct from the relevant established model | No distinct prediction, or disagreement with calibrated evidence |
| Are the mathematics independently reliable? | Have an independent reviewer or proof assistant check a bounded core, including negative cases and bridge assumptions | Unrepaired proof gaps or failures under the stated hypotheses |

For the mechanical benchmark, the next empirical step would use a measured oscillator with a calibrated frequency range and bounded measurement errors. Damping and frequency uncertainty must enter the admissible model before making a guarantee. A test should compare identical sample budgets at several phases and score prediction envelopes against held-out measurements. The exact ideal formulas here provide reference values, not permission to assume a real apparatus meets their hypotheses.

BM's strongest presently supported position is a mathematical framework with explicit nontrivial realizations and conditional necessity results. This note advances its quantitative testability. It does not turn its proposed physical interpretations into established physics or close the originality and independent-validation requirements identified in the preceding completion audit.

## Sources and reproducibility

Primary source links were checked on 23–24 October 2026. Some arXiv PDFs display a later rendering date; bibliographic years below follow their publication records rather than that rendering date.

- **[CM]** C. R. Shalizi and J. P. Crutchfield, *Computational Mechanics: Pattern and Prediction, Structure and Simplicity*, Journal of Statistical Physics (2001). [Paper](https://arxiv.org/abs/cond-mat/9907176). Sections IV–V and minimality discussion. Uses predictive distributions, not the deterministic bounded-noise semantics of DR1.
- **[MZ]** A. J. Chorin, O. H. Hald, R. Kupferman, *Optimal prediction and the Mori–Zwanzig representation of irreversible processes*, PNAS 97 (2000), 2968–2973. [Author manuscript](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf), sections 1–2. DOI:10.1073/pnas.97.7.2968.
- **[CLUE]** A. Ovchinnikov, I. C. Pérez Verona, G. Pogudin, M. Tribastone, *CLUE: Exact maximal reduction of kinetic models by constrained lumping of differential equations*, Bioinformatics (2021); preprint 2020. [Paper](https://arxiv.org/abs/2004.11961), algorithms 1–3 and supplementary invariant-subspace proofs.
- **[OR]** M. Ettehad and S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors*, SIAM/ASA Journal on Uncertainty Quantification 9(4) (2021), 1438–1456. [Author manuscript](https://foucart.github.io/publi/OR_Uncertainty_v2.pdf), sections 2 and 4, especially Theorem 4. DOI:10.1137/20M1328476.
- **[OR24]** S. Foucart and C. Liao, *Radius of information for two intersected centered hyperellipsoids and implications in Optimal Recovery from inaccurate data*, Journal of Complexity 83 (2024), 101841. [Author manuscript](https://foucart.github.io/publi/OR_L1Noise_v3.pdf), Theorem 1 and section 3. Publication metadata checked against the [author's bibliography](https://foucart.github.io/papers.html).
- **[CA]** S. Beckers and J. Y. Halpern, *Abstracting Causal Models*, AAAI (2019). [Paper](https://arxiv.org/abs/1812.03789), definitions 3.5, 3.7, 3.13, 3.15.
- **[CAA]** S. Beckers, F. Eberhardt, J. Y. Halpern, *Approximate Causal Abstractions*, UAI proceedings, PMLR 115 (2020), 606–615. [Proceedings record](https://proceedings.mlr.press/v115/beckers20a.html). This investigation inspected the proceedings abstract; it does not import an unexamined quantitative theorem from this paper.
- **[GL]** S. Abramsky and A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, New Journal of Physics 13 (2011), 113036. [Paper](https://arxiv.org/abs/1102.0264), introduction and local-to-global formulation. No general identification of BM with the paper's empirical-model semantics is assumed.
- **[PHY1]** OpenStax, *University Physics*, vol. 1, section 11.3, [Conservation of Angular Momentum](https://openstax.org/books/university-physics-volume-1/pages/11-3-conservation-of-angular-momentum).
- **[PHY2]** NASA, [Orbits and Kepler's Laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/). The exact normalized arithmetic and representation counterexample above are derived in this note.
- **[PHY3]** C. W. F. Everitt et al., *Gravity Probe B: Final Results of a Space Experiment to Test General Relativity*, Physical Review Letters 106 (2011), 221101. [Paper](https://arxiv.org/abs/1105.3456); related [mission explanation](https://einstein.stanford.edu/SPACETIME/spacetime4.html). The measurement is evidence about general relativity's frame dragging, not an experiment on BM.
- **[PHY4]** M. Zimbres and P. S. Letelier, *Multipolar corrections for Lense-Thirring precession* (2008). [Author preprint](https://arxiv.org/abs/0803.4133), equations 33–34. The l=1 term scales as angular momentum divided by r³ in G=c=1 units.

BM dependencies: canonical T01 (factorization), T10–T11 (future tasks and dynamic closure), T13 (relative essentiality), T31–T32/T47 (task separation and error), and the 23 October note *BM: necessity certificates and an exact comparison with existing theory*. The current research book already contains the classical observability rank result and earlier noisy-recovery examples; those are not counted here as newly discovered foundations. Frozen source identities and hashes are recorded in the accompanying source manifest.

Run `python BM_Research_Verification_2026-10-24.py .` to reproduce the JSON report and figure. The required packages and observed versions are recorded in that report.
