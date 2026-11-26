# BM: necessity certificates and an exact comparison with existing theory

23 October 2026. Additive completion analysis of the frozen BM V1 / Edition 1.1 foundation. The labels N1–N4 below identify arguments in this note; they do not replace T01–T55 or assert historical novelty. These are explicit deductions and implementations of existing principles, not a new foundational calculus.

## 1. The question that a necessity claim must answer

T01 proves that a particular representation loses a required distinction when it merges states with different task values. T11 proves when a particular representation supports autonomous evolution. T13 concerns essentiality relative to a comparison class fixed independently of the obligation test.

Three different questions must remain separate:

1. Does this proposed representation work?
2. Does any allowed representation using the available observations work?
3. Is some named Branch indispensable among all members of the specified comparison class?

A negative answer to question 1 does not automatically answer questions 2 or 3. The following construction answers all three in a finite deterministic contract and gives an independently replayable negative witness. A comparison class containing no candidates is not evidence of substantive indispensability. A positive reference realization is also required before attributing failure specifically to removal of one information source.

## 2. Declared contract

Let X be a nonempty finite native state set, A a finite action alphabet, and f_a:D_a ⊆ X → X partial deterministic updates. Every state in X is initially possible. Let O:X→Y be a product of the exact tasks required by the receiver. Legitimate task values may include a value called “null”; it is not the unavailable tag used below.

Let V:X→Z collect the observations available to an implementation. Its code may be any deterministic function C=hV into a set Q. The implementation must have a decoder d:Q→Y and partial autonomous updates g_a such that, on the realized code image,

\[
dC=O,\qquad x\in D_a\iff C(x)\in\operatorname{dom}g_a,
\qquad C(f_a x)=g_a(Cx)\quad(x\in D_a).
\]

No extra measurement, history before initialization, stochastic side channel, or native regularity requirement is present. Requiring continuity, a distributed encoder, quantum physicality, a particular output catalogue, or a hardware architecture changes this contract. An observation that must remain recoverable belongs among the tasks O; merely being available does not mean it must be retained.

Adjoin a distinct unavailable state ⊥. Extend each f_a to X∪{⊥} by mapping unavailable inputs to ⊥ and fixing ⊥. Define the tagged observation Õ(x)=(available,O(x)) for x∈X and Õ(⊥)=unavailable. For a finite action word w, let f_w denote execution in word order, including the empty word. Put

\[
xE_*y\quad\Longleftrightarrow\quad
\widetilde O(f_wx)=\widetilde O(f_wy)\quad\text{for every }w\in A^*.
\]

This is the future task-and-availability equivalence. It is computed from the native actions and required outputs, before testing any available observation V.

## 3. N1: an exact test over every encoding of available observations

**Statement.** An implementation satisfying the contract exists if and only if

\[
\boxed{\ker V\subseteq E_*.}
\]

When it exists, the smallest number of realized code states is |X/E_*|. A minimum code is the quotient q_*:X→X/E_*, expressed as a function of V.

**Necessity.** If V(x)=V(y), then C(x)=C(y). Autonomous deterministic execution from this same code has the same availability at each step and the same decoded task whenever available. Induction over the action word gives equality of every tagged future output. Thus xE_*y. Independently, any valid code satisfies ker C⊆E_*, since equal codes have equal future behavior. Consequently it must distinguish every two different E_* classes and has at least |X/E_*| realized states.

**Sufficiency.** E_* is an equivalence, since it is an intersection of kernels. Equality for the empty word preserves O. Equality for a one-action prefix preserves availability; after a common available action a, equality for all remaining words gives f_a(x) E_* f_a(y). Therefore each partial action descends to the quotient. The hypothesis ker V⊆E_* makes q_* constant on each V-fibre, so T01 supplies h on V(X) with q_*=hV. The quotient's task decoder and partial updates are well defined. Its realized size attains the lower bound. ∎

The direction of the containment matters. A code computed from V is allowed to merge more than V does. Exactification that must *retain* V is a different problem: there the repaired code must determine V, and its kernel must be contained in ker V. Reversing these two problems can manufacture a false necessity claim.

## 4. N2: finite termination, witnesses, and branch removal

Start with the partition of X∪{⊥} determined by Õ. At each round replace each state's color by the tuple consisting of its current color and every successor color. On X this can make at most n−b strict refinements, where n=|X| and b is the number of initial task classes on X. The unavailable singleton never merges or splits.

**Proof.** Each strict refinement increases the number of classes on X by at least one. The number starts at b and cannot exceed n. Inductively, equality after k rounds means equality of all tagged task outputs for words of length at most k. Once stable, equal colors have identical output and successor colors, so induction gives equality for every word. Therefore the stable relation is E_*. Every pair separated by E_* has a distinguishing word of length at most n−b. Breadth-first search on ordered state pairs finds a shortest such word. ∎

Suppose V=(V_1,…,V_m) is a supplied list of observation sources, and the full V is sufficient under N1. Remove source i and write V_{−i}. Source i is essential relative to arbitrary deterministic encodings of the remaining sources exactly when

\[
\exists x,y:\quad V_{-i}(x)=V_{-i}(y),\quad x\not E_*y.
\]

The states and a separating word are a finite proof of this relative necessity. N1 proves both directions. This is not a theorem that a mathematical discipline, a particular notation, or the whole BM framework is uniquely necessary.

For any independently supplied finite catalogue of allowed feature subsets, checking N1 on every member gives exact feasibility, inclusion-minimal members *within that catalogue*, and minimum declared feature cost. If no catalogue is supplied, the implementation enumerates all subsets. Costs are externally supplied nonnegative rationals; they are not physical measurements. An empty catalogue has no feasible member but proves nothing about an omitted implementation. If even the full observations fail, the implementation reports insufficient observations and makes no nonvacuous branch-essentiality claim.

Minimum retained code states and number of indispensable observation sources are different quantities. For the XOR task on two independent bits, both input sources are essential, while a centralized task code has only two states.

## 5. N3: a quantified obstruction under approximation

Suppose V(x)=V(y) and a common available word w gives task outputs whose distance is D in a metric space. Any deterministic autonomous predictor initialized solely from V produces one common decoded value at that word. By the triangle inequality at least one of its two task errors is at least D/2.

Thus the same witness supplies a lower bound on the attainable worst-case error. A declared tolerance ε<D/2 is impossible. This is a necessary bound, not a sufficient construction for approximate causal prediction. If the witness is unequal action availability, it is an exact domain obstruction; assigning it a numerical error requires an additional loss convention. Stochastic success probabilities, expected losses, and history-conditioned initializations need their own contracts.

## 6. Eight worked cases

The companion JSON and Python files contain the following exact cases.

| Case | Native model and obligation | Certified conclusion |
|---|---|---|
| Delayed velocity | (x,v)∈{0,1}², f(x,v)=(v,v), task x | Both x and v are essential observation sources; minimum autonomous code has four states. |
| Discard nonpredictive observation | (a,b,c)∈{0,1}³, f(a,b,c)=(a,c,c), task a, available (a,b) | Raw (a,b) is not autonomous, but C=a is. No new observation is necessary; minimum code has two states. |
| Duplicate observations | Task x; two copies of x available | Either copy suffices, so neither is individually essential. Supplied costs select the cheaper copy. |
| Availability obstruction | Constant task on two states; action enabled at only one; observation constant | No allowed encoding works; the length-one word certifies unequal availability. |
| Joint XOR | Independent bits a,b; task a XOR b | Each observation source is essential; the centralized code has two states. |
| Empty observation success | One state, no task distinctions or actions | One constant code state suffices; empty feature subset is feasible. |
| Empty candidate catalogue | A valid full observation exists but no candidates are supplied | No feasible member of that catalogue; no universal impossibility is inferred. |
| Retained legacy changes contract | Same model as the second row, but b must also remain recoverable | Available (a,b) is now insufficient; hidden c separates future legacy outputs. |

The second row is a decisive control example. Two states (0,0,0) and (0,0,1) have the same available observation (0,0), but its successors are (0,0) and (0,1). T11 rejects the raw observation as autonomous. Yet the requested task a stays unchanged, so C=a solves the task exactly. The first failure cannot justify demanding a new Branch unless retaining b is part of the obligation.

## 7. N4: T55-C7R as observed labelled bisimulation

This is an explicit comparison deduction, not a claim that the entire BM framework is equivalent to one other framework.

Take precisely the finite T55-C7R contract: nonempty sorts X_i, initial equivalences B_i, local labelled relations L_{i,a}, and finitely many partial deterministic interactions G_b with independently replaceable input slots and all Cartesian contexts. Form a labelled transition system with carrier

\[
S=\coprod_i X_i\;\amalg\;\{\bot_r:\ r\text{ is an interaction receiver sort}\}.
\]

Observe each native state's sort and initial B_i class. Observe each ⊥_r by its own distinct unavailable tag. All labels below are distinct and act only on their declared source sort; other sorts and unavailable states have no successors for that label.

* For each local relation L_{i,a}, add its labelled edges unchanged.
* For every interaction b, input slot p, and fixed tuple c of all other inputs, add a label (b,p,c). From u∈X_{i_p}, its unique successor is G_b(c[u]) in the receiver sort when defined, and ⊥_{r(b)} otherwise.

For an equivalence H refining the observations, labelled bisimulation means equality of successor H-class sets for every label. The local labels impose exactly the T55-C7R local relation conditions. A context label has one tagged successor, so its condition is exactly contextual equivalence in that slot. The unavailable singleton enforces saturation of the interaction domain.

Conversely these local and contextual conditions imply bisimulation on the expanded system. For a full interaction, replace equivalent input slots one at a time. All intermediate tuples remain permitted Cartesian contexts, and transitivity preserves the receiver class and domain membership. This recovers full interaction descent. Hence restrictions of observed bisimulation equivalences are exactly the admissible equivalence families of T55-C7R. The greatest such bisimulation restricts to the theorem's uniquely coarsest family. ∎

If n_i=|X_i|, this expansion uses Σ_i n_i plus at most one unavailable state per receiver sort. Interaction b of arity m_b contributes

\[
\sum_{p=1}^{m_b}\prod_{q\ne p}n_{i_q}
\]

context labels and m_b ∏_q n_{i_q} context edges. Local relation edges are additional. This can be a large expansion when interactions are supplied succinctly. An efficient direct BM implementation would need a separate complexity comparison; the reduction alone proves no speed advantage.

This reduction does not transport to arbitrary correlated admissibility by fiat. The coordinate-replacement proof can leave a restricted legal context set. The BM18 correlated-interface criteria address that different problem. It also does not collapse relational bisimulation into trace equality, probabilities into successor supports, or a native quantum channel into an arbitrary relation.

## 8. What the external comparison establishes

The bibliography below was checked on 23 October 2026. This was a targeted foundational comparison, not an exhaustive novelty search.

| BM item | Existing mathematical source | Result of this comparison |
|---|---|---|
| T01, T04, T06, T07 | Quotient factorization and elementary kernel identities; BM sources already mark them classical | Retain their proofs and necessity role; make no novelty claim for these ingredients. |
| Contextual exactification and deterministic future quotient | Rutten's treatment of systems, homomorphisms and bisimulation | Same standard system-equivalence structure in the deterministic contract. N1 states the additional available-observation feasibility test explicitly. |
| T55-C7R under full product contexts | Relational partition refinement and labelled bisimulation | N4 supplies an exact reduction, rather than merely a vocabulary resemblance. |
| Passport/contract refinement, conjunction and composition | Benveniste et al., *Contracts for system design*, especially Chapter 4 | A prior mathematical meta-theory already exists. The entire heterogeneous BM architecture has not been proved equivalent or inequivalent here. |
| Refinement and fixed-point reasoning | Cousot and Cousot's abstract interpretation | Existing abstraction/fixed-point theory is a required comparison baseline. No claim that exact BM quotients exhaust that framework. |
| Quantum algebra recovery | Bény, *Conditions for the approximate correction of algebras* | Imported recovery theory must be attributed. Its amplified norms must not be silently substituted for BM's stated unamplified defect/error quantities. |
| BM21 Jordan certificates; BM23 exact special-family envelopes | No theorem-specific priority conclusion established in this search | Compare identical encoder classes, horizons, norms and native constraints before claiming novelty. Absence of a search match is not evidence of priority. |

The legitimate positioning question is which BM statements, implementations or coordination guarantees add something under an exact shared contract. Proving that no other mathematical framework could express them is neither established nor required for a useful, rigorous theory.

## 9. Verification and limits

Run from the directory containing the files:

```sh
python3 BM_Necessity_Verification_2026-10-23.py
```

The run passed 2,824 native-instance certificates: 2,636 exhaustively generated small systems, 180 seeded multi-action systems and eight worked examples. It made 6,735 comparisons against a separate oracle that enumerates every possible code partition and checks encoder dependence, output equality, partial availability and autonomous closure directly. It replayed 6,256 quotient-separation witnesses and checked 2,744 shorter words; eight malformed inputs and fourteen corrupted certificates were rejected.

The positive checker verifies exact quotient descent. A separating word for each pair of quotient representatives certifies that different classes cannot be merged; closure makes this argument apply to their whole classes. This proves the finite certificate's minimality without rerunning the refinement algorithm. The checker does not use a proof-assistant kernel. All code and written proofs here were developed within this project; a differently implemented oracle is not an independent human review.

The reference implementation deliberately accepts at most 64 native states, eight actions and twelve observation sources. These are implementation limits, not mathematical limits. It enumerates feature subsets and makes no polynomial-time claim in the number of features. Refinement-round counts are execution diagnostics; the replay checker verifies the mathematical quotient and bounds but does not independently reproduce the exact number of rounds taken.

## References

1. BM, *Branch Mathematics Research Edition*, pinned public 23 October 2026 release: T01, T04, T08, T10–T13, T55 and the exactification construction. The source hash is in the accompanying completion register.
2. BM, *Mathematical Edition*, 10 September 2026, finite simultaneous-refinement chapter T55-C7R. Frozen hypotheses govern N4.
3. J. J. M. Rutten, “Universal coalgebra: a theory of systems,” *Theoretical Computer Science* 249 (2000), 3–80. [CWI record](https://ir.cwi.nl/pub/48); [paper](https://pages.jh.edu/rrynasi1/NewFoundations4Math/Literature/Coalgebras/Rutten2000UniversalCoalgebra-ATheoryOfSystems.pdf). Sections 2, 5 and 7 describe the relevant structures. N4 is the explicit translation written in this note.
4. R. Paige and R. E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6) (1987), 973–989. [Publisher record](https://epubs.siam.org/doi/abs/10.1137/0216062). The abstract identifies the relational coarsest-partition problem; no runtime bound was imported from an unread proof.
5. A. Benveniste et al., *Contracts for system design*, *Foundations and Trends in Electronic Design Automation* 12(2–3) (2018), 124–400. [Institutional record](https://research-explorer.ista.ac.at/record/5677); [author manuscript](https://www.cpsschool.eu/wp-content/uploads/2018/09/main_contracts.pdf). The manuscript has provisional publisher pagination; Chapter 4 is the comparison location.
6. P. Cousot and R. Cousot, “Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints,” POPL (1977), 238–252. [Author's publication page](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml).
7. C. Bény, “Conditions for the approximate correction of algebras,” arXiv:0907.4207 (2009). [Paper](https://arxiv.org/pdf/0907.4207), Sections 1.2–3.
