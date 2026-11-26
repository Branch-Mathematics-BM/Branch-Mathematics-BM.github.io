# Branch Mathematics — Finite-horizon Seed recovery versus autonomous closure

**1 November 2026 · Additive Volume II research note.** This work follows the compact Seed recovery theorems C1–C6 and the finite adaptive Seed diagnostic program. It leaves frozen BM Version 1 unchanged. All results below are conditional classical mathematics (quotient dynamics, compactness, symbolic sequences), framed to clarify BM's separate obligations. No physical theory or uniqueness claim is introduced.

## 1. Three distinct receiver obligations

Let `X` be an admissible native source state space, `F:X -> X` a lawful one-step evolution, `T:X -> Y` the demanded task, and `Q:X -> Z` the Seed representation supplied to a receiver. Distinguish:

1. **Present recovery:** there is a decoder `d` such that `T=d composed with Q`.
2. **Finite-horizon recovery:** for chosen `H`, there are decoders `d_0,...,d_H` satisfying `T composed with F^j = d_j composed with Q` for `0<=j<=H`.
3. **Autonomous closure:** there is a reduced evolution `E:Q(X)->Q(X)` with `Q composed with F = E composed with Q`.

Autonomous closure plus present recovery implies recovery at **every finite time**: `T composed with F^j = d composed with E^j composed with Q`. The reverse implication for any one finite `H` is false.

## Theorem E1 — exact topological closure test

Assume `X` compact, `Z` Hausdorff, `Q:X->Z` continuous, and `F:X->X` continuous. Then a **unique continuous** reduced evolution `E:Q(X)->Q(X)` satisfying

`Q(F(x)) = E(Q(x))`

exists **if and only if** the source equivalence induced by `Q` is forward-stable:

`Q(x)=Q(x')  ==>  Q(F(x))=Q(F(x'))` for all `x,x' in X`.

**Proof.** Necessity follows by applying the same map `E` to equal represented states. Conversely, forward stability makes `E(Q(x)):=Q(F(x))` well defined, and surjectivity onto `Q(X)` makes it unique. A continuous map from compact `X` onto Hausdorff `Q(X)` is a quotient map. Since `E composed with Q=Q composed with F` is continuous, the quotient-map criterion makes `E` continuous. QED.

**Important.** Merely determining `T(x)` from `Q(x)` does **not** establish E1. To claim that a Seed is a self-contained evolving carrier, BM must verify the **stronger** forward-stability property, or retain more native state/history.

## Theorem E2 — finite-horizon observation extraction

Suppose `X` compact Hausdorff; `F` continuous; `T:X->Y` continuous for **finite discrete** `Y`; and an arbitrary (possibly infinite) catalogue of permitted continuous passive probes `{q_i:X->O_i}` with Hausdorff outcome spaces **separates source states** (for every `x!=x'`, some probe has different outputs).

For every finite `H>=0`, there exists a **finite fixed measurement battery** `Q_H` that determines every task value in the time window

`(T(x), T(Fx), ..., T(F^H x))`.

**Proof.** Define the horizon task `T_H:X->Y^(H+1)` by this vector. Composition and finite products preserve continuity, and the target is finite discrete. Full source-state separation implies separation of all task-distinct pairs for `T_H`. Apply compact finite-task observation extraction (C1) to obtain a finite battery with a well-defined continuous decoder for `T_H`. QED.

**Weaker sufficient assumption.** Full source separation is stronger than necessary: it suffices that the probe family separates each pair with a different `T_H` value. Separation of the **present** task `T` alone does not suffice for `H>0`.

**Limitation.** E2 is an existence result *for each given finite horizon*. It does not bound the number of required probes uniformly in `H`, prove autonomy, or provide an effective optimization algorithm.

## Counterexample E3 — every finite horizon works, but no finite experiment knows the whole future

Let `X={0,1}^N` (infinite binary strings) with the compact product topology. Write `x=(x_0,x_1,...)`; let `F(x)=(x_1,x_2,...)` (left shift), and set `T(x)=x_0`. Let allowed probes be **only** the coordinate readings `q_j(x)=x_j`, one unit cost each.

All stated maps are continuous and `{q_j}` separates the source states. For horizon `H`, the future task vector is exactly

`T_H(x)=(x_0,x_1,...,x_H)`.

Each of the `H+1` corresponding coordinate probes is **necessary**: if `q_j` with `0<=j<=H` is not read, choose two strings that agree at every other coordinate but differ at `j`. They have identical observed measurements but different required future outputs. Reading the first `H+1` coordinates suffices. Hence

`minimum fixed finite-horizon cost = H+1`.

Adaptivity **does not help** for this catalogue and task: an adaptive protocol that has not read coordinate `j` cannot infer its value from any other queried coordinates. Under the worst-case source string, all `H+1` coordinates must be read, giving the same minimum adaptive cost `H+1`.

There is **no finite measurement battery** that recovers the **entire infinite future** `(x_0,x_1,...)`. Every finite coordinate selection leaves infinitely many unmeasured bits. Even a protocol with source-dependent finite stopping time cannot recover the entire arbitrary sequence using only finitely many coordinate readings.

Thus E2 does **not** extend to an unlimited horizon merely by repeating the word "compact". The infinite future task has infinitely many possible values; the finite-target hypothesis of C1 fails.

## Counterexample E4 — finite-horizon prediction does not grant closed Seed evolution

Continue with the infinite binary shift above. Select any **finite nonempty** set of coordinate probes `Fset` and write `Q_Fset(x)=(x_j)_(j in Fset)`. Let `m=max(Fset)`.

Choose two native worlds `x,x'` that agree on all coordinates in `Fset` but differ at coordinate `m+1`. Then `Q_Fset(x)=Q_Fset(x')`, while their shifted representations disagree in the coordinate indexed `m`, since `q_m(F(x))=x_(m+1)`.

Therefore the forward-stability criterion E1 fails for **every nonempty finite coordinate set**. Even the first `H+1` probes that perfectly predict the next `H` task outputs cannot be evolved forever by a deterministic map on that finite representation alone.

The empty probe set admits a trivial constant evolution but cannot recover the nonconstant present task. The full infinite coordinate sequence is autonomous, but not a finite Seed export.

## Corollary E5 — a sufficient condition for unlimited prediction

Suppose `Q` recovers `T` through some decoder `d`, and `Q` passes E1's forward-stability test so that a reduced evolution `E` exists. Then **every** future task value is determined by `Q(x)`:

`T(F^j x)=d(E^j(Q(x)))` for every integer `j>=0`.

**Proof.** Induct on `j` to obtain `Q(F^j x)=E^j(Q(x))`; apply `T=d composed with Q`. QED.

This gives a clean BM distinction: finite-horizon knowledge can be purchased with increasing observations, while an autonomous Seed representation must retain information sufficient for *all* its own lawful updates.

## Corollary E6 — robust approximate finite-horizon recovery

Let `X` be compact and `F` continuous. Let `T:X->(Y,d_Y)` and the permitted metric-valued probes be continuous. Assume the whole probe family separates **source states**. Define the finite-horizon metric task

`T_H(x)=(T(x),T(Fx),...,T(F^H x))`,

using the maximum metric on the finite product: `d_H((y_j),(y'_j))=max_(0<=j<=H) d_Y(y_j,y'_j)`.

For every finite `H` and precision `epsilon>0`, there exists a **finite** probe battery and a positive margin `delta` so that measurement-output vectors agreeing within `delta` imply **every** one of the next `H+1` task predictions agrees within `epsilon`.

**Proof.** `T_H` is continuous, and full source-state separation implies separation of task-distinct pairs for `T_H`. Apply compact approximate-recovery theorem C5 to `T_H` with metric `d_H`. If instrument readings have a verified error bound `eta` satisfying `2 eta<delta`, corollary C6 gives the same simultaneous prediction guarantee for every completion consistent with the readings. QED.

**Scope.** The selected battery and the margin may both depend on `H` and `epsilon`. This theorem does not give uniform prediction for unlimited time and does not imply autonomous closure.

## Proposition E7 — finite-horizon information cost cannot decrease as obligations grow

Fix a static source-observation catalogue with a nonnegative cost assigned to each measurement. Let `C_H` denote the minimum **worst-case** cost of an exact diagnostic protocol (fixed or adaptive, considered separately) required to determine all of `(T(x),...,T(F^H x))` for every possible native source. Use `+infinity` if certification is impossible.

Then

`C_0 <= C_1 <= C_2 <= ...`.

**Proof.** Every protocol that certifies the `H+1` horizon also certifies the shorter `H` horizon by discarding the last task output. Therefore the admissible successful-policy set for the longer task is contained in that for the shorter task. Minimizing the same worst-case cost over a subset cannot improve the optimum. QED.

The example E3 makes this inequality **strict at every step**, with `C_H=H+1` for both fixed and adaptive coordinate-probe protocols. The result is a task-obligation monotonicity fact, not a statement that every physical future becomes harder to predict.

## 2. Finite verification analogue

The executable companion `BM_Dynamic_Seed_Closure_Verifier_2026-11-01.py` enumerates binary strings of fixed finite lengths. It implements a finite left-shift register (append `0`), all coordinate readings, and the horizon task. For each short window it exhaustively checks the minimum fixed battery against the exact `H+1` prediction, verifies the failure of closure for every proper nonempty coordinate selection that contains its largest index below the available register end, and verifies that the complete register representation is closed. These finite checks are a regression illustration, not a proof of infinite-sequence theorems E2–E5.

## 3. Registry and research boundary

| Entry | Status | What it establishes |
|---|---|---|
| E1 | Proved, conditional | Continuous autonomous reduced evolution iff represented-state equivalence is forward-stable |
| E2 | Proved, conditional | A finite experiment exists for every requested **finite** prediction horizon under compactness, continuity and suitable observation separation |
| E3 | Proved counterexample | No uniform finite battery for an unlimited future even when every finite horizon is recoverable |
| E4 | Proved counterexample | A finite Seed can forecast a chosen horizon without being autonomously evolvable |
| E5 | Proved corollary | Forward-stable exact representation + present decoder guarantees all future task outputs |
| E6 | Proved corollary | Finite-horizon approximate recovery and bounded-error certification under compactness, continuity and source separation |
| E7 | Proved proposition | Minimum guaranteed cost is monotone as finite prediction obligations are added |

The proof boundaries are essential. A real application still needs an actual native evolution law, topology, lawful measurements, receiver task and Root/Passport semantics. Failing the closure test means *that representation* is insufficient for autonomous evolution; it is not evidence that the source lacks a lawful evolution. These principles are standard in topological dynamics and sufficient-state theory; BM's role is to track their hypotheses, witness information, and receiver obligations together.
