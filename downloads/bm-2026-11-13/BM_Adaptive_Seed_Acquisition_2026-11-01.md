# Branch Mathematics — Acquiring Seed-law information without probability

**1 November 2026 · Additive Volume II candidate.** This supplement continues the earlier finite Seed provenance and law-tag work. It does not revise the frozen September 12 Version 1 or imply that existing decision-tree, constraint, or control mathematics originated with BM. The application of adaptive experiment selection was already listed in `BM_New_Uses_2026-10-29.md` as E02. The present addition is a precise finite receiver/Passport contract, proofs, counterexamples, and two executable verifiers.

## 1. Motivation: a tag cannot be manufactured

The earlier law-tag theorem computes the least number of law identifiers a receiver would need **if an authorized party could supply a correct tag**. It does not say how a tag is known. When different lawful sources yield the same Seed export, simply appending a guessed law identity would conceal an unresolved distinction rather than repair it.

The correct mathematical question is: Given a family of admissible source worlds and a declared catalogue of safe observations, can a receiver **guarantee** determination of its required task and Passport status? If yes, what is the minimum worst-case observation cost? The model here uses no probability; uncertainty is a set of lawful alternatives.

## 2. Passive, set-valued observations

Let `W` be a finite nonempty set of possible complete source worlds. Let `T:W->Y` be the receiver's demanded result. It may be the vector of a task value **and** Passport status; statuses may include accepted, rejected and not applicable. The current information set is a nonempty `C subset W`.

A probe `q` has strictly positive rational cost `c(q)`, an enabling set `E_q subset W`, and for every `w in E_q` a nonempty set `O_q(w)` of permitted observations. The probe is safe to issue when `C subset E_q`. If the observed value is `o`, the lawful surviving worlds are

`C[q,o]={w in C: o in O_q(w)}`.

A probe must make the information set **strictly smaller on every possible observation** to be useful in a guaranteed finite terminating strategy. If a possible result returns the identical `C`, an adversary respecting the declared set-valued rules can repeat that result indefinitely. With positive cost, a purported optimal terminating protocol can omit that probe; its worst-case cost cannot improve by keeping a branch that reveals nothing.

### Proposition D1 (finite robust adaptive measurement value)

For this static-world, passive-observation contract define

`V(C)=0` if the task `T` is constant on `C`. Otherwise,

`V(C)=min_q [ c(q)+max_{o in O_q(C)} V(C[q,o]) ]`,

where the minimum considers only probes enabled for every world in `C`, all branches are proper nonempty subsets of `C`, and a probe with an infeasible branch has value `+infinity`. When no qualifying probe yields finite cost, `V(C)=+infinity`.

**Proof.** Any guaranteed terminating strategy begins with some safe probe. If its observations include a nonprogressing outcome, the worst-case strategy can be shortened by removing that first probe and following the continuation of the nonprogressing branch immediately; no other branch costs more in a minimax optimum. Otherwise every successor information set is a strict subset, for which an optimal strategy can be obtained inductively by set size. Each possible outcome has its own continuation. The worst-case remaining cost is the maximum of these branch costs; choosing the best first probe gives the minimum. This induction also provides a finite decision procedure and a replayable optimal policy tree. QED.

The output `+infinity` is an **infeasibility certificate relative to the declared observation model**. It does not prove a physical experiment outside that model can never help.

### Strict benefit of adaptivity

Take four possible states `a,b,c,d`, each requiring a distinct answer. Three binary probes of unit cost are supplied:

1. `region`: distinguishes `{a,b}` from `{c,d}`;
2. `left-specific`: separates `a` from `b`, but has no useful split between `c,d`;
3. `right-specific`: separates `c` from `d`, but has no useful split between `a,b`.

An adaptive protocol probes `region` and then selects one specialized probe. Its **worst-case cost is 2**. Any nonadaptive selected subset sufficient for all four states needs all three probes, cost **3**. The verifier exhaustively confirms both minima. Adaptive choice is therefore a real operational benefit under this contract, though the method is classical decision-tree optimization.

### Passport affects the decision cost

Two source laws may demand the same task answer but different Root acceptance statuses. If the task alone is requested, cost zero may suffice. If the receiver must certify `(task,Passport status)`, it may need an extra law-identifying probe. The test implements such a case with minimum costs **0 versus 1**. An output's content does not imply that its Root is accepted.

### Partial availability and adversarial noise

An inexpensive probe available in only one candidate world is not uniformly safe when the receiver cannot tell which world is actual. In a two-world test, the safe universally enabled probe costs 4; the unavailable cheaper probe is correctly excluded.

If a noisy sensor can return one common ambiguous outcome under two task-distinct states, repeated readings may never distinguish them under an adversarial set-valued contract. The test returns infeasible with that sensor alone, and a finite cost of 3 after adding a guaranteed distinguishing fallback. No probabilities or favorable repetition assumptions are smuggled into the conclusion.

## 3. Correlated probes and a persistent hidden witness

**Counterexample to marginal-only reasoning.** Let the source's complete state be `(t,h)` with task bit `t` and a persistent hidden calibration bit `h`. Two deterministic probes are

`q_1(t,h)=h`,

`q_2(t,h)=t XOR h`.

Each probe separately produces both 0 and 1 for both task values; **each marginal probe alone is uninformative**. But the joint pair satisfies `t=q_1 XOR q_2`, so two probes recover the task exactly. The exact finite adaptive solver returns cost **2**.

If the receiver deletes `h` from the model and retains only separate unrestricted outcome sets `{0,1}` for each task state, then every individual observation remains ambiguous and the robust solver correctly refuses certification. It has lost the **shared native witness** that forces the two results to be correlated.

This does not prove that the world has hidden calibration. It proves that a declared lawful joint relation can change the answer to a recovery question. A pair of marginal observation sets is not in general a substitute for the correlated joint source model. This is the same BM principle behind the earlier even/odd three-variable counterexample, now turned into an actionable receiver-observation contract.

## 4. Controlled observations that change the world

The passive recurrence D1 is not valid unchanged when a measurement alters the world, its available actions, or the source law. Define a finite controlled system with a total task map `T:W->Y` and an action catalogue `A`. Each action `a` has positive cost, an enabling subset, and for each enabled world `w` a nonempty finite **joint** relation of observable-successor pairs `K_a(w) subset O_a x W`.

To preserve the task *originally asked*, require that every permitted transition `w -> w'` satisfies `T(w')=T(w)`. If an intervention changes that original answer, either (i) reject it for this contract, or (ii) augment the state with the original target before evaluating its usefulness. Redefining the target after an intervention without saying so is an invalid task switch.

For current information `C`, the action is safely callable only if every possible world enables it. Its possible updated belief after observing `o` is

`C[a,o]={w': exists w in C with (o,w') in K_a(w)}`.

Unlike the passive case, this belief need not be a subset of `C`. Therefore induction on `|C|` is no longer justified.

### Proposition D2 (finite controlled robust diagnosis)

Assume `W` finite, `A` finite, costs strictly positive, and all actions preserve the receiver's declared original task. Consider the finite state space `B` of nonempty subsets of `W`. Initialize `V_0(C)=0` for task-constant information sets and `+infinity` otherwise. Recursively define

`V_{n+1}(C)=min( V_n(C), min_{a enabled on C} [c(a)+max_o V_n(C[a,o])] )`.

Then this iteration, run through at most `|B|` policy steps, yields the exact minimum worst-case cost of a guaranteed finite terminating adaptive policy, or `+infinity` when none exists.

**Proof.** Induction on `n` shows `V_n` is the optimal worst-case cost among strategies guaranteed to terminate in at most `n` further actions. The first action incurs `c(a)` and the adversary chooses among its lawful observations, yielding the maximum continuation cost; the minimum takes the best safe action. The optional `V_n(C)` term allows termination earlier than the horizon. A guaranteed terminating strategy with positive costs cannot improve by revisiting the identical belief set along a possible execution path: at a repeat, it can use the later continuation immediately, saving positive cost while leaving the lawful future belief problem unchanged. Thus an optimal successful strategy can be chosen acyclic on the finite belief-state graph, with depth at most `|B|`. No such strategy exists if the value remains infinite. QED.

This is a standard finite worst-case information-state reachability construction, organized under BM's task, source, action-availability and Passport obligations. It is not a general theorem for arbitrary continuous, stochastic or infinite systems.

### Controlled activation example

Let a world carry a task bit and a readiness mode. Initially a read action is unavailable. A first action activates the mode while preserving the task; a second action reports the task. Both actions cost 1. The exact controlled game returns worst-case cost **2**.

An action that maps two original task-distinct states into one state and thereby changes the declared task is rejected by the verifier. A repeated noninformative action with a shared output is correctly judged unable to guarantee completion.

## 5. Implementation and checks

`BM_Adaptive_Seed_Diagnostics_2026-11-01.py` implements D1, exact finite nonadaptive bundle comparison, source-law Passport tests, partial query availability, adversarial noise, and persistent hidden-witness tests. It passed **200 randomized comparisons** against an independently structured nonmemoized policy enumeration; **151** of those random contracts were infeasible under their declared catalogues.

`BM_Active_Seed_Diagnostics_2026-11-01.py` implements D2 by finite belief-state value iteration and rejects original-task-changing actions. It passed **150 randomized comparisons** against explicit depth-bounded policy-tree enumeration; **84** sampled cases were feasible. The special two-step activation, noninformative-action and forbidden-erasure examples passed.

These are reproducible internal tests of exact finite models, **not independent theorem checking, empirical source accuracy, or evidence of BM-exclusive performance**. The prior BM archive's 162 native-method comparisons reported mathematical agreement; it remains the benchmark baseline rather than a claim of BM superiority.

## 6. New operational rule and stopping boundary

A Seed receiver should return one of four evidence statuses:

1. **Certified:** all surviving lawful worlds agree on task and Passport result.
2. **Acquirable:** a declared safe observation/control policy guarantees certification; report a minimal worst-case policy and cost.
3. **Unresolved within catalogue:** a concrete pair of surviving task-distinct worlds remains, with no permitted guaranteed policy under the supplied model.
4. **Contract missing:** the source-law alternatives, joint observation relation, task, Passport, action availability or cost are not provided; do not invent them.

The four statuses are a proposed finite BM implementation convention, not a new universal metaphysical principle. An unknown source law cannot be identified by asserting a tag. A hidden shared witness cannot be dropped without checking whether it matters. A successful current answer does not establish autonomous closure or receiver acceptance.

The finite passive and controlled problems are now solved under their stated hypotheses. Extending them requires **new information**, not another name: a declared continuous/noisy native observation contract; joint correlations across laboratories/receivers; infinite carriers with effective presentation; distributed communication constraints; empirical calibration; or proof of a field-performance advantage. Without such inputs, further universal conclusions would not be justified.

## Prior work and sources

- *Branch Mathematics V1 Canonical Foundation* (Edition 1.1, frozen 12 September 2026).
- *Branch Mathematics Research Edition*, update of 19 October 2026, BM18-O1–O4.
- *BM Completion and Network Development* (29 October 2026), finite overlapping frames and Seed models.
- *BM New Uses* (29 October 2026), especially experimental-selection application E02.
- *BM Seed Provenance, Law Uncertainty and Closure* (1 November 2026), the directly preceding supplement.
- Laurent Hyafil and Ronald L. Rivest, “Constructing Optimal Binary Decision Trees Is NP-Complete,” *Information Processing Letters* 5(1), 15–17 (1976), author-hosted PDF: https://people.csail.mit.edu/rivest/pubs/HR76.pdf. This paper studies expected decision cost; this supplement uses a different explicitly worst-case contract.
- Ferdinando Cicalese, Eduardo Laber and Aline Medeiros Saettler, “Diagnosis determination: decision trees optimizing simultaneously worst and expected testing cost,” *Proceedings of the 31st International Conference on Machine Learning* (2014), https://proceedings.mlr.press/v32/cicalese14.html. Existing literature directly covers worst-case diagnosis optimization.
