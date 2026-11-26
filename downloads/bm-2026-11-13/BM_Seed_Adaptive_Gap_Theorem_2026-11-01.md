# Branch Mathematics — An unbounded finite Seed measurement adaptivity gap

**1 November 2026 · Additive Volume II research note.** The theorem below is a finite decision-tree fact specialized to BM's Seed and task language. It is not a claim of mathematical priority, experimental discovery, or physical particle structure. It leaves frozen Version 1 unchanged and builds on *BM Adaptive Seed Acquisition* (1 November 2026).

## The finite experiment family

Fix any integer `k >= 1`. A source world is a binary string `w` of length `k`; all `2^k` strings are admissible. The receiver's task is to identify the **entire** string (a unique answer for each world). For every binary prefix `p` of length less than `k`, the catalogue contains one unit-cost passive probe `q_p`:

* if `w` starts with `p`, it reports the bit of `w` immediately after `p`;
* otherwise, it reports the distinguished symbol `outside`.

All probes are universally enabled and deterministic. There are `2^k-1` available probes. The receiver knows this experiment catalogue; the source string is unknown. **Every observation has a specified joint source meaning.**

An **adaptive** protocol chooses the next probe after earlier observations. A **fixed battery** chooses all probes before observing anything, runs them all, and then decodes the answer. Every executed probe costs one, so each strategy is evaluated by its guaranteed worst-case number of probes. No probabilities are used.

## Theorem G1: exact adaptive and fixed costs

For the family above:

`minimum adaptive worst-case cost = k`;

`minimum fixed-battery cost = 2^(k-1)`.

Thus the fixed/adaptive cost ratio is `2^(k-1)/k`, **unbounded as k grows**.

### Adaptive upper bound

First query `q_empty` to learn bit 1. Given the observed first `j` bits `p`, query `q_p` to learn bit `j+1`. After precisely `k` queries, the entire world is known. Therefore adaptive cost is at most `k`.

### Adaptive lower bound

The adversary maintains a complete binary prefix subtree of consistent worlds. Initially it contains all length-`k` strings. If the current surviving subtree has a fixed prefix `r` and at least one unspecified bit, consider any next query `q_p`.

* If `p=r`, the outcome chooses one of the two immediate child subtrees, both of which have one fewer unspecified bit.
* If `p` is a strict prefix of `r`, the next bit it reports is already fixed across the subtree (no progress).
* If `p` strictly extends `r`, the adversary can return `outside` and retain the entire child subtree of `r` whose next bit differs from the next bit of `p`.
* If `p` is incompatible with `r`, every world in the subtree returns `outside` (no progress).

Thus there exists a lawful outcome path on which each query removes at most one unspecified bit of a whole surviving prefix subtree. After fewer than `k` queries at least two worlds remain, and the demanded task is not identified. Therefore adaptive worst-case cost is at least `k`; combined with the upper bound, it equals `k`.

### Fixed-battery lower bound

Consider every pair of sibling leaves of the depth-`k` binary tree: worlds `p0` and `p1`, with `p` any length-`k-1` prefix. Only `q_p` gives different outputs on these two worlds. Every other probe either observes an earlier shared prefix bit or outputs `outside` for both siblings. Consequently **every** fixed battery capable of distinguishing all `2^k` worlds must contain `q_p` for each of the `2^(k-1)` distinct sibling pairs. Thus its cost is at least `2^(k-1)`.

### Fixed-battery upper bound

Take exactly all `2^(k-1)` depth-`k-1` prefix probes. For a source `w`, exactly its own last-bit prefix probe returns `0` or `1`; all the others return `outside`. Its full identity is therefore recovered. Cost is `2^(k-1)`, proving exact optimality. QED.

## Exhaustive small-case verification

The executable `BM_Adaptive_Prefix_Gap_2026-11-01.py` constructs every world and every permitted probe, then independently optimizes via the finite adaptive recurrence and a complete enumeration of fixed probe bundles for `k=1,2,3,4`.

| Depth `k` | Source worlds | Probe catalogue | Optimal adaptive cost | Optimal fixed cost |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 1 |
| 2 | 4 | 3 | 2 | 2 |
| 3 | 8 | 7 | 3 | 4 |
| 4 | 16 | 15 | 4 | 8 |

The proof, not the four tests, establishes arbitrary `k`. For illustration only, at `k=10` the exact costs within this **specified hypothetical catalogue** are 10 adaptive versus 512 fixed; at `k=20`, 20 versus 524,288. These are formal complexity numbers, not laboratory cost estimates.

## Counterexample G2: adaptivity is not universally advantageous

Add a single universally enabled unit-cost probe that reports the entire source string `w` in one observation. Now both the optimal adaptive protocol and optimal fixed battery cost exactly **1**. In that richer probe catalogue the previous ratio disappears.

This proves the precise limitation: **BM cannot guarantee a gain from adaptivity without constraints on what each admissible observation can report.** The advantage belongs to a specified observation contract, not to the naming of observations as Seeds, fibres, Branches, or Roots.

## Consequence for BM

This family makes three otherwise vague BM requirements precise:

1. **Declare the task**. Identifying an entire state is not the same as predicting one output or certifying one Passport field.
2. **Declare admissible observations and their joint source relation**. The existence of information in the underlying world does not imply its availability to the receiver at zero cost.
3. **Preserve and expose branch decisions**. Conditional selection of a later test can be substantially cheaper than a battery chosen without knowing prior observations.

This is a valid candidate for the BM Volume II operational registry, marked **proved conditional finite theorem**, cross-referenced to classical adaptive decision-tree diagnosis. No BM-exclusive superiority, continuum analogue, or new law of nature follows. The stop condition for extension is a real task and observation/permission/cost contract; without one, arbitrary new constants or physical interpretations would be speculation.

## Prior art

- Hyafil and Rivest, *Constructing Optimal Binary Decision Trees Is NP-Complete* (1976), https://people.csail.mit.edu/rivest/pubs/HR76.pdf (expected-cost decision trees, not the particular worst-case proof above).
- Cicalese, Laber and Saettler, *Diagnosis determination: decision trees optimizing simultaneously worst and expected testing cost* (2014), https://proceedings.mlr.press/v32/cicalese14.html (explicit prior art on worst-case diagnosis).
