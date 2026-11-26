# Branch Mathematics — Compact Seed recovery and its exact failure modes

**1 November 2026 · Additive Volume II conditional theorem.** This note extends the finite passive Seed measurement work without altering canonical BM Version 1. It is an elementary consequence of topological compactness and the quotient-map factorization theorem, not a historically new principle attributable exclusively to BM.

## Setup

Let `X` be the space of admissible complete native source states. For each `i` in a possibly **infinite** index set `I`, a permitted deterministic passive measurement is a map `q_i:X -> O_i`. The receiver's task is `T:X -> Y`. We ask whether finitely many of these measurements suffice to determine `T(x)` **exactly** for every lawful source `x`.

`T` is determined by a selected finite measurement vector `Q=(q_i1,...,q_im)` precisely when

`Q(x)=Q(x') implies T(x)=T(x')` for all `x,x' in X`.

This is BM's exact task-relative recoverability test expressed at native source level.

## Theorem C1 — compact finite-task observation extraction

Assume:

1. `X` is compact Hausdorff (compact is the essential property for finite extraction; Hausdorff is a convenient standard setting).
2. The required task space `Y` is **finite and discrete**, and `T:X -> Y` is continuous.
3. Every measurement `q_i:X -> O_i` is continuous, with `O_i` Hausdorff.
4. The **full** measurement family separates task-distinct worlds: whenever `T(x) != T(x')`, some `i` satisfies `q_i(x) != q_i(x')`.

**Conclusion.** There exists a **finite** subset `F subset I` such that its joint measurement vector `Q_F` determines `T` on all of `X`. Furthermore the exact decoder `d:Q_F(X) -> Y` with `T=d composed with Q_F` can be chosen **continuous**.

### Proof

Consider the task-conflict set

`D={(x,x') in X x X: T(x) != T(x')}`.

Since `Y` is finite discrete and `T` continuous, `D` is closed in the compact product `X x X`, hence compact.

For every available probe `q_i` define its separation set

`U_i={(x,x') in X x X: q_i(x) != q_i(x')}`.

Because `O_i` is Hausdorff and `q_i` continuous, `U_i` is open: the diagonal in `O_i x O_i` is closed, and `U_i` is its complement pulled back along `q_i x q_i`. The separating-family assumption says `{U_i}` covers `D`. Compactness of `D` gives a **finite subcover**, say `U_i1,...,U_im`.

Therefore if two source states agree on all selected measurements, they cannot belong to `D`, so their task values agree. Define `d(Q_F(x))=T(x)`; the agreement condition proves this is well defined.

For continuity, `Q_F:X -> Q_F(X)` is a continuous surjection from a compact space onto a Hausdorff subspace of `O_i1 x ... x O_im`, and is therefore a quotient map. Since `T=d composed with Q_F` is continuous and `Q_F` is quotient, `d` is continuous. QED.

### What this does and does not guarantee

- A potentially infinite catalogue has a **finite exact witness** for any continuous, finite-valued task whenever all task-conflicts are pairwise separated.
- This proves existence of a fixed finite battery. Consequently a finite adaptive measurement plan also exists, but its optimal cost may differ.
- If each selected probe has finite positive cost, the selected battery's total cost is finite. **No numerical upper bound**, efficient search algorithm, or optimal battery follows from compactness alone.
- If `X` is connected, any continuous map into a finite discrete `Y` is constant; the theorem is then trivial. This assumption cannot be casually applied to nontrivial discontinuous threshold tasks on connected physical state spaces.
- This is for **deterministic and jointly coherent** observations. Arbitrary adversarial set-valued noise needs the separate robust contract of theorem D1 and cannot be inserted into this proof without additional assumptions.

## Three counterexamples locating the boundary

### C2 — without compactness, finite recovery can fail

Take `X=N` with the discrete, noncompact topology and `T(n)=n mod 2`. For each natural number `j` define `q_j(n)=1 if n=j, else 0`.

Every opposite-parity pair is separated by at least one probe (for example, `q_n` distinguishes `n` from every different integer). Yet any **finite** selection of probes misses infinitely many odd and even integers; they all return the same zero measurement vector. No finite battery determines parity. All task and probes are continuous. Compactness cannot simply be omitted.

### C3 — compactness without task continuity is insufficient

Take `X={0} union {1/n:n in N}` with its inherited compact topology. Set `T(0)=0` and `T(1/n)=1`. For each `j`, let `q_j(x)=1 if x=1/j, else 0`.

Each probe `q_j` is continuous, because the isolated point `{1/j}` is clopen in `X`. Every task-distinct pair `(0,1/n)` is distinguished by `q_n`. But for any finite selected list, choose `m` outside its indices: then `0` and `1/m` give the identical all-zero vector despite distinct tasks. The failure is exactly that `T` is **discontinuous at 0**. Here the task-conflict set `D` is not compact.

### C4 — compactness is insufficient for an infinite-valued exact task

Let `X={0,1}^N` be the compact product space of infinite binary sequences, set `T(x)=x` (the full sequence), and let `q_j(x)` return the `j`th bit. Every two distinct source sequences are distinguished by some continuous coordinate probe. However no finite set of coordinates determines the whole infinite sequence. The task is continuous, but its range is **infinite**, and the task-conflict set (all off-diagonal pairs) is not compact.

## Theorem C5 — finite approximate recovery with a uniform measurement margin

There is a useful stronger conclusion when the task's range is not finite. Assume `X` compact, `T:X -> (Y,d_Y)` continuous into a **metric** task space, and the available continuous probes `q_i:X -> (O_i,d_i)` have **metric** observation spaces. Suppose every pair with different task values is distinguished by some available probe.

Then for **every prescribed tolerance `epsilon>0`**, there is a finite set `F` of probes and a positive number `delta` such that

`max_{i in F} d_i(q_i(x),q_i(x')) < delta  ==>  d_Y(T(x),T(x')) < epsilon`

for **every** pair of admissible source worlds `x,x'` (with the convention that the maximum over an empty selected catalogue is zero).

**Proof.** Set `D_epsilon={(x,x'):d_Y(T(x),T(x')) >= epsilon}`. Continuity of `T` makes `D_epsilon` closed in compact `X x X`, hence compact. Each pair in this set is task-distinct, so some probe separates it. As in C1, the open sets where individual probes differ cover `D_epsilon`; select a finite subcover `F`. On `D_epsilon`, the continuous function

`g(x,x')=max_{i in F} d_i(q_i(x),q_i(x'))`

is **strictly positive**. If `D_epsilon` is nonempty, compactness gives a positive minimum `delta=min_{D_epsilon} g > 0`. Thus observation distances all strictly below `delta` preclude membership in `D_epsilon`, proving the implication. If `D_epsilon` is empty, the task is already `epsilon`-constant and the claim is vacuous (choose no probes). QED.

**Example.** On the compact space of infinite binary sequences, equip the task space with the ordinary prefix metric: two sequences first differing at position `j` have distance `2^(-j)`. Measuring the first `m` coordinate bits exactly guarantees task distance at most `2^(-(m+1))`, though no finite number of coordinates identifies the full sequence exactly. For probes with discrete `0/1` observation metrics, any `delta` with `0<delta<=1` forces identical measured prefix bits. This converts the exact impossibility in C4 into **certified finite-resolution recovery**, once a task metric and tolerance are actually declared.

**Limits.** This theorem does not compute the finite probe subset or its margin from an unspecified catalogue. A positive mathematical margin is not a guarantee that instruments achieve it. In the example, the metric is part of the chosen task contract; choosing a different metric changes the claimed precision. This is standard compactness/uniform-continuity reasoning, not an independently verified physical result.

## Corollary C6 — bounded-error readings still certify a task tolerance

Use the same finite probe set `F` and uniform separation margin `delta>0` provided by C5 for a target tolerance `epsilon`. Let an actual measurement return readings `z_i` with a **guaranteed** error bound

`d_i(z_i, q_i(x)) <= eta` for every `i in F`,

where `2 eta < delta`. Form the nonempty receiver-completion set

`C_z={x' in X: d_i(z_i,q_i(x')) <= eta for every i in F}`.

Then for **every** possible original world `x` consistent with the readings and **every** `x' in C_z`, the task estimate obeys

`d_Y(T(x),T(x')) < epsilon`.

**Proof.** Any two states consistent with the same reading vector satisfy, by the triangle inequality, `d_i(q_i(x),q_i(x')) <= 2 eta < delta` for all selected probes. Apply C5 to obtain the claimed task bound. QED.

This gives a **deterministic, no-probability robust error certificate**: any candidate completion of the measured data is an `epsilon`-accurate task answer, provided the declared instrument-error guarantee is true. It does **not** validate the error bound or prove one can compute a completion efficiently. If `delta` is unknown or `eta` is not guaranteed, the certificate is unavailable. This is distinct from adversarial overlapping-outcome sensors without a numeric error envelope.

## BM interpretation and proof-status registry

The compactness theorem offers a mathematically justified **conditional bridge** from an infinite Seed source to a finite Root-readable task certificate. It clarifies that a finite probe suite is justified by the geometry/topology of the admissible native states, continuity of the requested finite task and of observations, plus actual task-separation—not by simply declaring that Seeds contain information.

Suggested registry entries:

| Entry | Status | Precise scope |
|---|---|---|
| C1 | Proved, conditional | Compact source, continuous finite-valued task, continuous Hausdorff-valued deterministic probes, task-pair separation |
| C2 | Proved counterexample | Noncompact source; finite battery not guaranteed |
| C3 | Proved counterexample | Compact source but task discontinuous |
| C4 | Proved counterexample | Compact source, continuous infinite-valued task |
| C5 | Proved, conditional | Compact source and continuous metric-valued task/probes; finite epsilon-resolution with positive margin |
| C6 | Proved corollary | Bounded measurement errors strictly within half of C5 margin |

**Boundary.** No recovery theorem can currently be asserted for an arbitrary unstructured continuum, arbitrary discontinuous receiver demand, correlated noisy observations lacking a shared model, or an unknown physical source law. The data needed to strengthen the claim are a specified native topology, task, admissible measurement maps, and a source-law Passport. Without those, the mathematically honest next step is to stop and review rather than postulate more structure.

## Classical antecedents

- The finite-subcover property of compactness (standard general topology).
- The closed-diagonal characterization of Hausdorff spaces.
- The continuous factorization property of quotient maps (standard general topology).

These are existing mathematical results; BM here provides a task-oriented contract and audit trail for their application.
