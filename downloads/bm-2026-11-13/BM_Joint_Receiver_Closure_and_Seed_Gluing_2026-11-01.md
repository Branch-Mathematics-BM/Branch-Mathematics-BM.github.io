# Branch Mathematics — Joint-receiver closure and lawful Seed gluing

**1 November 2026 · Additive Volume II finite deterministic theorem.** This is a specialization of existing partition-lattice and relation-image mathematics to BM's task-closed Seed quotient F1/F2. The older overlapping-Tree gluing work already established the need for a common witness; this note tests that need specifically when several receivers demand distinct future tasks of **one native evolving source**. It does not assert novelty or alter frozen Version 1.

## Setup

Let `X` be a finite nonempty set with total deterministic native evolution `F:X->X`. Receiver A demands a task `T_A:X->Y_A`; receiver B demands `T_B:X->Y_B`. Let `Q_A:X->Z_A` and `Q_B:X->Z_B` be their respective **minimal task-closed representations** constructed by future-behavior partition stabilization (F1/F2).

Let `~_A` and `~_B` be their equivalence relations, where two native states are related when they have identical demanded task histories for all iterations of `F`.

## Theorem J1 — joint minimal closure is the meet of receiver requirements

For joint task `T_AB(x)=(T_A(x),T_B(x))`, its minimal task-closed relation is

`~_AB = ~_A intersection ~_B`.

An explicit minimal joint Seed representation is the **realizable-pair map**

`Q_AB(x)=(Q_A(x),Q_B(x))`, with image `S=Q_AB(X)`.

If `E_A` and `E_B` are the receivers' induced closed evolutions, `S` is invariant under their product update:

`(E_A,E_B)(S) subset S`.

Thus the **restriction** of the product update to `S` is a lawful autonomous evolution of the joint minimal task representation. Its size obeys

`max(|Z_A|,|Z_B|) <= |S| <= min(|X|, |Z_A|*|Z_B|)`

(interpreting `Z_A=Q_A(X)`, `Z_B=Q_B(X)`).

**Proof.** Joint future-task equality means equality of each component's complete task trajectory, so the joint equivalence is precisely the intersection. The kernel of `(Q_A,Q_B)` is the same intersection. F2 says the corresponding quotient is minimal closed for the joint task. For any `s=(Q_A(x),Q_B(x))` in `S`, applying both reduced evolutions produces `(Q_A(Fx),Q_B(Fx))`, again in `S`. The size bounds follow from the coordinate projections from `S` onto `Z_A,Z_B`, the inclusion `S subset Z_A x Z_B`, and the surjection from `X` onto `S`. QED.

## Theorem J2 — exact condition for an unrestricted Cartesian combination

The full product `Z_A x Z_B` is realizable **if and only if** every A-equivalence class intersects every B-equivalence class in at least one native state:

`S = Z_A x Z_B  <==>  for all a in Z_A, b in Z_B: Q_A^(-1)(a) intersection Q_B^(-1)(b) is nonempty`.

**Proof.** Pair `(a,b)` lies in `S` exactly if there is `x` such that `Q_A(x)=a` and `Q_B(x)=b`, which is exactly the nonempty-fibre-intersection condition. QED.

Consequently **taking the Cartesian product of local Seed states is generally unsound** as a claim that all combinations originate from the same native source, even when each receiver individually has a correct autonomous state model. The lawful joint carrier is `S`, not the unrestricted product.

## Counterexample J3 — a nonexistent pair of accepted local states

Take three native states `X={a,b,c}` and identity evolution `F(x)=x`. Let receiver A's present task partition be `{a,b}|{c}`, and receiver B's be `{a}|{b,c}`. Because evolution is identity, these are also the minimal future-task-closed partitions.

Label their outputs by `A(a)=A(b)=0`, `A(c)=1`; and `B(a)=0`, `B(b)=B(c)=1`. Then

`S={(0,0),(0,1),(1,1)}`

has three lawful pairs, while the unrestricted local product contains four. The pair `(1,0)` is a **ghost combination**: A's class requires native state `c`, while B's class requires native state `a`, and no world satisfies both.

This is a precise BM common-native-witness obstruction, not an appeal to probabilistic correlation.

## Counterexample J4 — dynamic coupling can make two full local quotients entirely redundant

Take the four two-bit states `X={00,01,10,11}` and the evolution that swaps the bits. A asks for first bit, B asks for second bit. Each current task has two values. But under repeated swapping, each receiver's **entire future task** alternates between both bits, so each receiver's minimal closed quotient already distinguishes all **four** source states.

Consequently `|Z_A|=|Z_B|=4`, yet `S` contains only four matched states, not the sixteen formal combinations in `Z_A x Z_B`. The same four native states supply the two receivers; assuming their separately labeled quotient states are independent would invent twelve impossible pairings.

This distinction matters for BM Seed accumulation: when receiver demands interact through one native evolution, the required information is the **joint realizable image**, which may be much smaller than a naive product, but cannot be replaced by arbitrary pairings without verifying the common source.

## Verification and boundary

Companion `BM_Joint_Receiver_Closure_Verifier_2026-11-01.py` tests randomized finite deterministic source maps and pairs of task maps, constructs each minimal closure quotient and their joint quotient, and checks both the intersection identity and the common-fibre realizability condition. It checks the two explicit counterexamples and confirms product dynamics preserves `S`.

**Boundary:** one **shared** native source state set and one shared deterministic evolution. If two local Trees have different native state spaces, incomplete source overlaps, different laws or incompatible time-indexing, the existence of the shared `X` itself becomes a gluing obligation; J1 must not be invoked until a common realization witness is supplied. This is a sharper scope condition for the BM network, not a universal merging algorithm.

## Registry

| ID | Status | Claim |
|---|---|---|
| J1 | Proved finite theorem | Minimal joint task-closed quotient equals intersection of individual future-task equivalences |
| J2 | Proved iff test | Full independent product is lawful exactly when every pair of quotient fibres intersects |
| J3 | Explicit counterexample | An independent product can contain ghost states incompatible with native source existence |
| J4 | Explicit counterexample | Shared evolution can make separately full local quotients redundant in joint carrier |

**Prior art:** equivalence-relation meet, quotient factorization, relational joins, finite automata minimization, and image/fibre intersection. Historical originality and comparative numerical advantage remain unresolved.
