# Branch Mathematics — Seed provenance, law uncertainty, and closure

**Additive technical supplement, 1 November 2026.** This is a finite mathematical continuation of Branch Mathematics (BM), not an amendment to the frozen Version 1 / Edition 1.1 foundation. It does not assert universal Seed dynamics, independent peer review, historical mathematical priority, or a physical interpretation.

## 1. Sources, completeness, and nonduplication

The 12 September frozen V1 defines the typed Branch, native Interaction, certified Leaf, realized Tree, Task/Response, Passport, and receiver-accepted Root. The Research Edition updated 19 October already supplies finite completion Seeds, receiver-dependent Rooting, realization-preserving Rebranching, and finite composition (BM18-O1–O4). These are therefore **prior BM work**, not inventions of this supplement.

The 29 October `BM_Completion_and_Network_Development_2026-10-29.md` already gives a finite network of overlapping frames, a running-intersection/join-tree gluing result, an inconsistent three-frame cycle, a weighted-annotation counterexample, a no-direct-attachment Seed activation model, and an exact scalar accumulation example. Its tests reported 250 random join-tree models, 3,009 checked global extensions, eight Boolean triangle cases, 780 rational recurrence identities, and related witnesses. Do not promote these older results as new here.

The October 29 project inventory has **336 BM entries: 70 definitions, 254 theorem-classified records, two conditional theorem records, and ten hypothesis records**. These are classifications of archive entries, not 254 independent discoveries. The review traced the proof bases of 128 previously unenumerated theorem dependencies and checked 23 recorded source hashes. It did not independently certify all proofs. The same-day complete-method comparison reported agreement on 162 small tested cases, with no unique mathematical or performance advantage established. The 29 October application inventory also records 24 application directions plus four extensions, and nine finite analyzer contracts covering seven applications; those are not first proposed here.

**New question in this supplement:** When a portable Seed enters a receiver, how much generating-law identity, current state, and future behavior must be retained for a specified task or autonomous continuation? The original law, source IDs, and available side information must be declared. No generating mechanism follows merely from using the word *Seed*.

## 2. Contract: tasks, legal models, and portable Seeds

For a finite nonempty set of source-law alternatives `L`, each law `ell` supplies a nonempty legal state set `J_ell`, a typed Seed export `sigma_ell:J_ell -> S`, and a task `T_ell:J_ell -> Y`. A lawful model may also supply an explicit native transition. A **receiver** knows the Seed code and only such law/source metadata as are authorized by its Passport. A **Root** arises only when receiver applicability and admissibility are separately passed; task sufficiency alone is not Passport acceptance.

The source law may be uncertain but the world must still be one of the *declared* lawful candidates. Treating overlapping copies of one source as independent Cartesian factors can create spurious global states and false retention requirements. Unsupported correlations must not be silently assumed either. If the joint relation is unknown, the status is *underdetermined* pending a source-law contract.

The finite operation of adding constraints is conjunctive and can only remove old realizations from the same carrier. A generative Seed that changes the carrier, supplies new variables, or activates a rule is a **different native operation**; such growth cannot be inferred from constraint accumulation alone. This keeps completion Seeds distinct from portable generative Seeds.

## 3. The finite law-tag theorem

Assume each law is individually sufficient:

`sigma_ell(x)=sigma_ell(y)` implies `T_ell(x)=T_ell(y)` for any `x,y` in `J_ell`.

Define an undirected **law-conflict graph** `G_T` on `L`. Distinct laws `ell,m` are adjacent precisely when there exist `x in J_ell, y in J_m` with equal Seed exports and unequal required task answers.

**Proposition S1 (minimum task-specific law tag).** A single decoder `D:S x C -> Y` exists using law tag `c:L -> C`, so that

`D(sigma_ell(x),c(ell))=T_ell(x)` on all legal states, **if and only if** `c` is a proper coloring of `G_T`. Consequently the minimum identifier alphabet has `chi(G_T)` symbols, requiring `ceil(log2 chi(G_T))` fixed binary bits.

*Proof.* Adjacent laws sharing a tag present identical decoder input with different demanded output, which is impossible. For a proper coloring, assign each observed pair `(s,tag)` the unique required task value among worlds producing it. Uniqueness follows from within-law sufficiency and the absence of same-colored cross-law conflicts. Assign arbitrary values on unused code pairs. This defines the decoder. Both directions give the exact minimum. QED.

**Failure certificate.** If two states within *one* law have equal Seed export but different task answers, no identifier of the law alone can repair them: their tagged export remains identical. An additional native-state distinction or a weaker task is necessary.

**Example.** Under the copy model `b=a`, export `a` determines `b`. Under the inversion model `b=1-a`, it also determines `b`. Without the model identity, the export is ambiguous. One bit specifying the model repairs it. With a third restricted model admitting only `(a,b)=(0,0)`, copy and restricted laws can share the same tag. Three model names need just two tags, not three.

## 4. Horizon-dependent distinguishability

Suppose each law has a total deterministic update `f_ell:J_ell -> J_ell`. For horizon `h>=0`, define the task trace

`V_ell^h(x)=(T_ell(x),T_ell(f_ell x),...,T_ell(f_ell^h x))`.

When each Seed export is sufficient for this trace within each law, apply S1 with `V^h` as the task. Call the conflict graph `G_h`.

**Proposition S2.** `G_h` is a subgraph of `G_{h+1}`, so `chi(G_h)` cannot decrease as the declared future obligation grows. On a finite deterministic global carrier `W` (disjoint union of all law-labelled states), the entire future-behavior equivalence partition stabilizes by at most `|W|-1` refinement steps. Consequently the model-conflict graphs stabilize no later than that finite bound. This is standard deterministic partition refinement in a BM contract, not a new universal dynamics theorem.

*Proof.* Distinct length-`h` traces remain distinct when extended by another coordinate. For stabilization, partition `W` by current output. Each further trace coordinate refines the partition. Any strict refinement increases its class count by at least one; there can be at most `|W|-1` such increases. When one refinement adds no split, deterministic successor refinement adds none later. QED.

**Test.** For source state `a in {0,1}`, export `a` and demand `T(a)=a`. The *hold* law updates `a->a`; the *flip* law updates `a->1-a`. At horizon zero no law tag is needed. At horizon one, the same Seed value leads to different answers, so one law bit becomes necessary. It remains necessary at all longer horizons.

Note that knowing future task traces does **not** guarantee an autonomous update of the exported Seed value itself.

## 5. Stronger fixed-law autonomous closure

Continue with fixed laws and total deterministic updates. The encoded carrier is `E_ell(x)=(sigma_ell(x), c(ell))`, with the law tag unchanged by the update. Demand both a single-valued task decoder `D` and a single-valued **encoded update** `F` such that:

`D(E_ell(x))=T_ell(x)` and `F(E_ell(x))=E_ell(f_ell(x))`.

**Proposition S3.** If every law separately satisfies both task sufficiency and Seed-update closure, define a graph `G_closed` with an edge `ell--m` when some states have equal Seed values but either unequal present tasks or unequal **next Seed values**. Then the minimum tag alphabet for this stronger contract is exactly `chi(G_closed)`.

The same proper-coloring proof applies to the pair of required outputs `(current task, next Seed value)`; since the tag is fixed, a properly colored code also determines its next tag.

**Strict difference.** Two laws can generate identical *task traces at every horizon* while requiring different next Seed values. Let tasks be constantly zero and Seed value be `a`; one law resets `a` to zero and the other resets `a` to one. For task prediction, no law tag is necessary. For an autonomous transition on the retained Seed code, two tags are necessary. This is the contract distinction between predicting an observable and reproducing the chosen representation's own evolution.

## 6. Simultaneous receiving tasks

For several tasks `T_1,...,T_r` on the same legal worlds, form each task-conflict graph. Their **joint** conflict graph is the union of the individual edge sets. This follows because two laws conflict for the task vector if and only if some coordinate task conflicts.

Thus the minimum shared law-tag alphabet is `chi(G_1 union ... union G_r)`, which can be *strictly larger* than each individual minimum. In a three-law exact test, receiver 1 yields the two-edge path `0--1--2` and needs two tags; receiver 2 yields the edge `0--2` and needs two tags; jointly the graph is a triangle and needs **three** tags. Separate local acceptability is not a joint interface certificate.

## 7. When the generating law can change

The graph formula S3 **does not automatically extend** when a Seed moves into a Tree with a different generating law. Model a finite set of worlds `W`, current law `lambda:W->L`, Seed `sigma:W->S`, task `T:W->Y`, and total update `f:W->W`. A candidate law-tag assignment `c:L->C` defines `E_c(w)=(sigma(w),c(lambda(w)))`.

**Proposition S4 (exact switching-law closure criterion).** There exist both a decoder `D` and autonomous code transition `F` exactly when every `w,v` with `E_c(w)=E_c(v)` satisfy

`T(w)=T(v)` **and** `E_c(f(w))=E_c(f(v))`.

*Proof.* Necessity follows by applying the same `D` and `F` to equal codes. For sufficiency, define `D` and `F` on each occupied code using any representative. The conditions make both choices independent of representative. Extend arbitrarily to unused codes. QED.

For worlds with equal present Seed values, S4 imposes:

1. If their required task or next Seed values differ, their **current-law tags must differ**.
2. Otherwise, **if** their current-law tags coincide, their **successor-law tags must also coincide**.

The second condition is an equality implication involving *different pairs of law labels*, not a fixed conflict edge. Exact finite tag optimization is therefore a constraint-search problem, not automatically a single graph coloring.

**No law-only repair.** Use worlds `p,q` under law 0, `r` under law 1 and `s` under law 2. All present Seed values equal zero. Set tasks `T(p)=T(q)=T(r)=0`, `T(s)=1`. Updates are `p->r`, `q->s`, `r->r`, `s->s`. The tasks of `r,s` require their different law tags. But `p,q` are indistinguishable under any law-only tag, and their successor codes would be different. Thus **no law-tag assignment** yields both task sufficiency and autonomous closure. Replacing `sigma(q)=0` with `sigma(q)=1` adds one source-state distinction and repairs the model with a two-symbol law tag.

**Unexpected consequence.** With all tasks changed to the constant zero, one common law tag gives valid closed dynamics. If the successor laws of `r,s` are given different tags while `p,q` remain merged, the refined code is *not* autonomous. Static decoding is monotone under extra information; autonomous closure of a specifically chosen representation need not be. A more detailed Seed code at the predecessor can repair that failure. This is not an argument against retaining source data.

**Three-law strict example.** With all Seed values zero, tasks `T(A)=T(B)=0`, `T(C)=1`, and updates `A->A`, `B->C`, `C->C`, present task sufficiency needs two law tags, while autonomous code closure needs all three.

## 8. Complexity boundary: every finite graph is realizable

**Proposition S5.** Every finite simple graph `H` can be represented as a task-conflict graph of a finite law/Seed family that is individually sufficient within every law.

*Construction/proof.* Give a law to every vertex. For each graph edge `{i,j}`, create one unique Seed-output symbol `e_ij`. The legal states of laws `i` and `j` each contain one occurrence exporting that symbol, with opposed task values zero and one. No other law exports the symbol. Add a private Seed-output symbol to isolated vertices to keep each legal state set nonempty. Every within-law Seed code appears once, so it is sufficient. Across laws, a conflict occurs exactly for the original edges. QED.

Consequently exact minimum law-tag computation includes ordinary graph coloring as a special case. For an explicit finite contract, deciding whether `k` tags suffice is NP-complete for fixed `k>=3` (membership can be checked by enumerating the declared finite input pairs; hardness is by the construction). It would be unjustified to advertise a polynomial-time universal optimal tagging algorithm. This imports the classical hardness of graph coloring; it is not a new complexity-class discovery.

Useful immediate special cases: no conflicts -> one tag (zero law-id bits); a bipartite conflict graph -> at most two tags; a complete graph on `n` laws -> `n` tags. Disconnected components can reuse the same palette, so the minimum for a disjoint union is the maximum component chromatic number, not the sum.

## 9. Separate BM geometry audit: nine straight segments

The user's finite-sample curve construction distinguishes two possible tasks: (A) find the exact area of the **specified nine-segment polygon**, and (B) find the area under an **unknown curved function** that passes through the ten sample positions. These are not the same task.

For `f(x)=x^2` on `[0,1]`, using ten equally spaced points (nine segments), exact rational arithmetic gives polygonal/trapezoidal area `163/486`, while the true integral is `1/3=162/486`. The discrepancy is `1/486`. It exactly attains the classical composite trapezoidal bound `||f''||_infty/(12*9^2)` for this example.

There is **no universally exact ten-point area method for all smooth curves**. For example, the nonnegative smooth polynomial `g(x)=prod_{k=0}^9 (x-k/9)^2` vanishes at every sampling point but has positive integral; the zero function has identical samples and zero integral. The two tasks produce identical finite data and different correct answers, so the BM task-sufficiency criterion forbids a decoder that always returns the exact continuous area from just those samples. Multiplying `g` by arbitrary positive constants makes the hidden area arbitrarily large. This negative result does not deny that geometry and linear algebra exactly compute **polygonal** area; it specifies the missing regularity or interpolation contract needed for a continuum claim.

## 10. Verification, status, and stopping boundary

The accompanying standard-library script `BM_Seed_Law_Tag_Verifier_2026-11-01.py` verifies the declared finite contracts. Independently structured direct decoder enumeration and the graph-coloring procedure agree on **1,400 random fixed-law horizon instances** and **350 random autonomous-update instances**. Every simple graph on one through five vertices was constructed and recovered (**1,099 graphs**). The finite trace stabilization assertion passed **350 random model tests**. The independent pair-implication test and explicit encoded transition test agreed on **4,434 random switching-law tag assignments**. All specified positive, negative and one-distinction repair examples passed, as did the exact rational nine-segment test. These counts describe test instances, not independent proofs or new mathematical discoveries.

**Status register:**

| Result | Scope and status |
|---|---|
| S1 minimum law tag | Proven for finite legal models with per-law task sufficiency; classical coloring reduction |
| S2 horizon monotonicity/stabilization | Proven for finite deterministic total actions; classical finite-state refinement |
| S3 code-autonomy tag graph | Proven for one total fixed-law update with per-law Seed closure |
| Simultaneous receivers | Proven by union of finite conflict graphs; no cross-receiver resource restriction |
| S4 changing-law condition | Proven for finite total deterministic world transition and explicit task/Seed maps |
| Changing-law model-tag optimization | Exact finite exhaustive procedure; may be infeasible, not claimed efficient |
| S5 arbitrary graph realization and hardness | Explicit reduction; graph-coloring NP-completeness is prior mathematics |
| Nine-segment area audit | Exact finite calculation and general information obstruction; classical analysis |
| General categorical, smooth, probabilistic, quantum, physical Seed mechanism | **Not established**; would require separate typed native semantics and bridges |
| Whole BM historical originality and peer-review certification | **Not established** |

BM's pre-existing six broad open families are not solved here: unrestricted nonlinear Jordan interior optima; global regular realizations/minimal augmentation; constrained or infinite causal realization; unrestricted quantum observable-algebra recovery implementation; nonlinear repair beyond solved contract classes; and further infinite-dimensional native systems. The missing full historical DD sources, independently checked proofs, external novelty review, real-application head-to-head benchmarks, and live calculator/source conformance remain evidence gates. None can be completed by a finite toy example or a new name.

**Stopping rule:** The present finite research questions admit exact answers and have been worked to explicit proofs, witnesses, and tests. Further universal claims require a specified new native category or admissibility law, external source evidence, or independent reviewer; no such input can be fabricated. Preserve frozen V1, append this note as a scoped Volume II candidate, and retain all failures and assumptions.

## Prior-art and project sources

1. *Branch Mathematics V1 Canonical Foundation* (September 2026; Edition 1.1 frozen).
2. *Branch Mathematics Research Edition*, version updated 19 October 2026, BM18-O1–O4.
3. *BM — Correction and Evidence Closure Register* (updated 18 October 2026).
4. *BM Completion and Network Development* (29 October 2026), including Beeri–Fagin–Maier–Yannakakis (1983) and Atserias–Kolaitis (2026) references on relational consistency.
5. *BM Direct Comparison Findings* (29 October 2026), 162 matched internal comparisons.
6. *BM New Uses* (29 October 2026), 24 candidates plus four follow-ups.
7. Aho, Beeri and Ullman, *The Theory of Joins in Relational Databases* (1979), ACM Transactions on Database Systems 4(3).
8. Established finite-state partition refinement, graph coloring, database dependencies, and constraint satisfaction; these are imported algorithms and proof ideas, not BM discoveries.
