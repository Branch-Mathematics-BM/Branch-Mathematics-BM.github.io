# Branch Mathematics — Finite stabilization and minimal autonomous task-Seed quotient

**1 November 2026 · Additive Volume II finite theorem.** This is the finite deterministic counterpart to *BM Dynamic Seed Recovery and Closure*, E1–E7. Its mathematics is classical partition refinement / finite automaton minimization, not a new independent mathematical invention. It is included because it closes an explicit BM gap between a carrier that reports the current task and a carrier that can update without its discarded source state.

## Contract and native relation

Let `X` be a **finite nonempty** native source world set with `n=|X|`, `F:X->X` a **total deterministic** evolution and `T:X->Y` any task map. Write `m=|T(X)|`, so `1<=m<=n`. For horizon `h>=0`, define the finite observable trajectory

`B_h(x)=(T(x),T(Fx),...,T(F^h x))`

and the equivalence `x ~_h x'` iff `B_h(x)=B_h(x')`.

The partitions `P_h=X/~_h` can only **refine** as `h` increases: adding an obligation cannot merge classes that were already task-distinct.

## Theorem F1 — finite stabilization with a sharp general bound

The sequence of trajectory partitions stabilizes by horizon

`h <= n - m`.

At its first stable index `h*`, equality of the finite trajectories `B_h*(x)=B_h*(x')` is equivalent to equality of **all** future task outputs:

`T(F^j x)=T(F^j x') for every j>=0`.

**Proof.** By construction `P_(h+1)` refines `P_h`. If two consecutive partitions coincide, then `~_h` is forward stable: equality through time `h+1` implies equality of the shifted histories through time `h`. Formally, since `P_h=P_(h+1)`, `x~_h x'` forces `x~_(h+1) x'`, hence `F(x)~_h F(x')`. Induction gives equality of the task at every later time, so no further refinement can occur.

If a step is **not** stable, it strictly increases the number of partition blocks by at least one. `P_0` has `m` blocks and there can be at most `n` blocks. Thus the number of strict refinement steps before stabilization is at most `n-m`, proving the bound. At stabilization the finite-horizon equivalence equals full-future task equivalence. QED.

### Sharpness witness

For any `n>=2`, let `X={0,...,n-1}`, `F(i)=min(i+1,n-1)`, and `T(i)=1` only at `i=n-1`, `0` otherwise. Then `m=2` and the backward chain of task-distinguishable states separates **one new class per step**, reaching the stable partition first at `h*=n-2=n-m`. Thus the bound is attained.

For `m=1` the task is constant everywhere, and stabilization is immediate at `h*=0`.

## Theorem F2 — canonical minimal closed Seed for the task

Let `h*` be the first stable index and define `Q*(x):=[x]_(~_h*)` (the equivalence class of `x` under equal whole-future task behavior). Then:

1. **Exact current task recovery:** `T=d composed with Q*`, with `d([x])=T(x)`.
2. **Autonomous evolution:** `F*([x])=[F(x)]` is a well-defined map on the quotient, and `Q* composed with F = F* composed with Q*`.
3. **All future tasks:** `T(F^j x)=d((F*)^j(Q*(x)))` for every `j>=0`.
4. **Minimality:** if another representation `R:X->Z` recovers `T` and has any deterministic reduced evolution `G:R(X)->R(X)` satisfying `R composed with F=G composed with R`, then

   `R(x)=R(x') ==> Q*(x)=Q*(x')`.

   Consequently `|R(X)| >= |Q*(X)|` and `Q*` factors uniquely through `R(X)`. Up to relabeling its classes, `Q*` is the **coarsest exact autonomous task-sufficient Seed representation**.

**Proof.** Items 1–3 follow from the stabilized forward-invariant equivalence and the induced maps. For item 4, if `R(x)=R(x')`, determinism of `G` gives `R(F^j x)=R(F^j x')` for all `j`, and its task decoder gives `T(F^j x)=T(F^j x')` for all `j`. By F1, `x~_h* x'`, hence `Q*(x)=Q*(x')`. Define `p(R(x)):=Q*(x)`; the implication makes `p` well defined and proves `Q*=p composed with R`. A surjection `p:R(X)->Q*(X)` yields the cardinality inequality. QED.

This is a statement about **task-relative lawful compression**, not about destroying physical information. Native states can share the same minimal Seed precisely when no allowed future iteration of `F` changes the demanded task distinction.

## Observation availability is a separate obligation

Even when `Q*` exists and is mathematically minimal, a receiver cannot assume it can measure `Q*` from an arbitrary initial export. For example, in the two-bit system `X={00,01,10,11}`, let `F` swap the bits and let `T` read the first bit. Current-task observation `q(x)=first bit` recovers `T`, but states `00` and `01` share `q` while their next task bits differ; the current export cannot determine the closed class. An additional permitted reading of the second bit would resolve it. This preserves BM's distinction between **a necessary representation** and **an authorized realizable measurement**.

## Proof checker and scope

`BM_Finite_Task_Closure_Verifier_2026-11-01.py` performs exact random finite map/partition refinement, verifies the `n-m` bound, checks the transition congruence, verifies that stable horizon distinguishes all task-future pairs, exhaustively enumerates all possible finite representations for small sizes to check coarsest-quotient minimality, and tests the sharpness chain family. The enumerations are independently useful regressions but not a substitute for F1/F2 proofs.

**Boundary:** finite `X`, deterministic total native `F`, exact declared task `T`. Nondeterministic transitions, interventions, changing law passports, source-driven observation noise and unrestricted infinite systems require separate conditions; transplanting this finite stabilization bound to those contexts is unjustified.

## Registry

| ID | Status | Result |
|---|---|---|
| F1 | Proved finite theorem | The task-history partition stabilizes by `n-m`; sharp for a deterministic chain |
| F2 | Proved finite theorem | Stable partition yields a unique minimal extensional autonomous task quotient |
| F3 | Proved counterexample | Present-task measurable does not imply minimal autonomous Seed measurable |

**Prior-art crosswalk:** partition refinement, Moore minimization of deterministic automata, Myhill–Nerode future-equivalence, quotient/congruence dynamics. BM applies their distinction between observation, continuation, and the receiver task to its Seed/Root/Passport status system. Independent historical novelty and practical superiority remain unestablished.
