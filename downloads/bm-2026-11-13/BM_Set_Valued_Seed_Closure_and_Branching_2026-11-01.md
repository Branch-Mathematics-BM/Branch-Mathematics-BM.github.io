# Branch Mathematics — Set-valued Seed closure, branching, and receiver noncomposition

**1 November 2026 · Additive Volume II finite conditional theorem and counterexamples.** This is an extension of the deterministic minimal-Seed quotient F1/F2 to a finite **set-valued** native evolution. It uses classical strong bisimulation and partition refinement. It is not a proposed universal physical law, a novelty claim, or an alteration of frozen BM Version 1.

## 1. State and lawful-response contract

Let `X` be finite and nonempty, `|X|=n`. Let `K:X->P_+(X)` assign every native state a **nonempty set of lawful successor states**. Let `T:X->Y` be the receiver's demanded task, with `m=|T(X)|`. The alternative successors are lawful possibilities, **not probabilities**.

An exact reduced representation `Q:X->Z` is **task-respecting** when `T` factors through `Q`. It is **branch-preserving closed** when there is a well-defined reduced set-valued map `Kbar:Q(X)->P_+(Q(X))` such that

`Kbar(Q(x)) = {Q(x') : x' in K(x)}`

for every native state `x`.

Hence two states may be merged only if they share the task value **and** the same set of possible reduced successor classes. This is the exact stepwise branching contract; it is stronger than merely having identical sets of eventual task trajectories.

## Theorem N1 — finite minimal exact branch-preserving Seed quotient

Start with partition `P_0` by equal current task value. Given any partition `P_r`, refine each block by its **successor-class signature**

`S_r(x) = { [x']_(P_r) : x' in K(x) }`.

Thus `x` and `y` remain in the same block of `P_(r+1)` exactly when they were in the same block of `P_r` and `S_r(x)=S_r(y)`.

**Claims:**

1. The partition sequence stabilizes by `r <= n-m` refinement steps.
2. The stable partition `P*` is task-respecting and induces a well-defined branch-preserving reduced relation `Kbar`.
3. It is **coarsest** among all task-respecting branch-preserving equivalence relations: every other lawful representation's partition refines `P*`.
4. Up to class relabeling, `P*` is the unique minimal extensional strong-bisimulation task quotient for this contract.

**Proof.** `P_(r+1)` only subdivides blocks of `P_r`, never merges them. If it differs strictly, the block count increases by at least one; it begins at `m` and cannot exceed `n`. Thus it becomes constant after at most `n-m` refinements. At stability, states in one block have the same current task and identical successor-block sets, so `Kbar` is well defined and the quotient preserves the declared branch relation.

For minimality, take any task-respecting partition `R` such that native states in one R-block have identical sets of R-successor blocks. `R` refines `P_0`. Assume inductively that `R` refines `P_r`. The equal R-successor-block sets then project to equal `P_r`-successor-block sets, so states equivalent under `R` remain together under `P_(r+1)`. By induction `R` refines every `P_r` and hence `P*`. Therefore `P*` is coarsest admissible, with the fewest blocks. QED.

This is a **finite constructive answer** to BM's question of which branch distinctions must remain in a self-contained, response-complete Seed representation. The answer is relative to the specified task `T` and lawful response relation `K`.

## Counterexample N2 — identical future output sets need not preserve branching

Take seven native states `x,y,u,v,w,b,c` with task values

`T(x)=T(y)=A`, `T(u)=T(v)=T(w)=B`, `T(b)=0`, `T(c)=1`.

Lawful successor sets:

* `K(x)={u}`; `K(y)={v,w}`.
* `K(u)={b,c}`; `K(v)={b}`; `K(w)={c}`.
* `K(b)={b}` and `K(c)={c}`.

From both `x` and `y`, the entire possible infinite output-trace set is **exactly** `{A,B,0,0,0,... ; A,B,1,1,1,...}`. Therefore any representation storing only *which complete task traces are possible* merges `x` with `y`.

Nevertheless `x` and `y` are **not** strong-bisimilar. The sole successor `u` of `x` offers both distinct next-task branches `0` and `1`, while `y` has separate successor states `v` (only `0`) and `w` (only `1`). No one of those two states can match all the branching options of `u`. The fixed-point partition algorithm splits them.

This distinction is material if future observation or control occurs **between** branching events: the available continuations at that intermediate point matter, not just the eventual set of complete histories. For a receiver interested only in trace sets with no intermediate decisions, the **weaker** trace-equivalent quotient may be legitimate; N1's stronger contract must not be imposed silently.

## Counterexample N3 — deterministic joint-receiver meet fails for set-valued laws

The deterministic joint-receiver result J1 showed that the minimal joint task quotient is the intersection of the two individual future-task equivalences. **That rule cannot simply be copied to set-valued branch-preserving closure.**

Let native states be `x,y,00,01,10,11`. The last four states self-loop. Define

`K(x)={00,11}` and `K(y)={01,10}`.

Receiver A asks for the **first bit** on the four terminal states; receiver B asks for the **second bit**. Assign both roots `x,y` a current task value `0` for both receivers.

Each receiver alone judges `x` and `y` equivalent under its minimal branch-preserving quotient: A sees next-task values `{0,1}` from either root, and B sees the same values `{0,1}`. Each has matching successor classes within its own partition.

But the joint receiver sees distinct **paired** successor sets:

* From `x`: `{(0,0),(1,1)}`.
* From `y`: `{(0,1),(1,0)}`.

So the *joint* minimal branch-preserving quotient **must distinguish** the roots. The intersection of the two individual equivalences merges them and is **not itself a lawful joint branch-preserving quotient**.

This is a precise common-witness obstruction to composing separately correct local response summaries; it is the set-valued analogue of discarding shared correlations. Retaining only independent per-receiver successor marginals erases the allowable **pairing** of branch outcomes.

## Verification and limitations

The companion executable `BM_Set_Valued_Seed_Closure_Verifier_2026-11-01.py` constructs exact finite set-valued relations and validates N1 against independently enumerated candidate partitions for small systems. It verifies the seven-state trace-versus-branch counterexample N2 and the two-receiver pairing counterexample N3. As before, randomized finite checks are regression evidence, while the stated general finite proofs establish the theorem.

**Scope boundaries:** native law `K` is a fully specified set-valued one-step relation on a **shared, fixed** finite source space; every successor step remains within that space. N1 does not automatically cover uncontrolled infinite worlds, native law changes, stochastic source laws, history-dependent interventions, transition labels or asynchronous interfaces. Those require explicit extension contracts and cannot inherit the finite theorem merely because a relation is called a Tree or Seed.

## BM status registry

| Entry | Status | Result |
|---|---|---|
| N1 | Proved finite conditional theorem | Coarsest task-respecting strong-bisimulation quotient by finite partition refinement; stability by `n-m` |
| N2 | Proved counterexample | Equality of complete output-trace sets does not entail branch-preserving closure |
| N3 | Proved counterexample | Meet of individually adequate set-valued receiver quotients need not preserve lawful joint branching |

**Prior art:** strong bisimulation, coinductive behavioral equivalence, partition-refinement algorithms, and trace-versus-branching equivalence in labeled transition systems. BM's contribution in this note is a precise application with source, task, carrier and common-witness requirements, not a claim to having invented these classical results.
