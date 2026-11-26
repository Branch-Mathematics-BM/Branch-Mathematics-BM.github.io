# BM direct comparison protocol

24 October 2026. Fixed before running the comparison suite. This is an internal controlled benchmark, not public preregistration, independent validation, a representative sample of scientific work, or an exhaustive originality search.

## Question

Does the present BM implementation yield more accurate feasibility decisions, smaller exact representations, lower declared repair cost, or better computational performance than existing methods on the same fully specified problems?

The native comparator receives the same states, admissibility, tasks, actions, observations, costs, and tolerances. Missing an obligation in a deliberately simplified calculation is an ablation, not a competitive baseline. Different code labels, different bases, or different equal-cost optimizers count as agreement when their mathematical meanings agree.

## Fixed suites

1. **Finite future behavior and observation selection:** the eight existing BM examples plus 48 seeded systems with 4–24 states, up to three partial deterministic actions, and up to seven supplied observation channels. Compare the existing BM analyzer with a separately implemented classical distinguishable-pair algorithm and a weighted set-cover integer program solved through SciPy/HiGHS. Compare the entire state-equivalence relation, observation sufficiency, minimum feature cost, and nonvacuous essentiality. A supplied catalogue restricts both methods. Seed 241001.
2. **Distributed interfaces and correlated contexts:** six designed examples plus 30 seeded contexts, with two or three branches, each having two or three local values. Compare the existing BM interface enumerator with a binary integer program over local equivalence relations, including transitivity, task separation, partial-action availability, and dynamic closure. Optimize the identical weighted sum of local code-alphabet sizes. Seed 241002.
3. **Exact linear differential reduction:** six designed systems, twelve dense seeded systems, and twelve constructed reducible systems in dimensions two through six (one designed chain may be larger). Compare BM's existing exact rational observability calculation with actual CLUE 1.7.3 source pinned to commit `0576e9b8477bc511e3fea29a3c296c5d30b688aa`. Compare row spaces and code dimension, not basis labels. Seed 241003. Also run CLUE's published nonlinear three-state example and check its symbolic reduction; this is a capability demonstration, not a claim that the BM reference implementation has a general nonlinear reducer.
4. **Noisy scalar oscillator prediction:** 40 combinations of eight stated phases and five noise bounds. Compare BM's previously derived analytic formula with numerical minimization of the classical optimal-recovery dual objective. Compare optimal error to tolerance 1e-8. A fast formula versus an iterative numerical solver does not establish a BM-specific speed advantage.
5. **Integration case study:** run the complete native checks and BM checks on selected information-loss, initialization, noise, and global-compatibility cases. A native method that does not purport to check an obligation is marked out of scope at that stage, not wrong. Demonstrate what the explicit coordination contributes and whether a competent native workflow can reproduce it.

## Verification and timing

- Existing BM implementation files are copied without changes and hashed.
- CLUE source files are verified against their pinned Git blob hashes. Actual imported versions are recorded.
- Integer solver selections are checked using exact native predicates; integer costs are recomputed exactly. Float solver status alone is insufficient evidence of a correct selected representation.
- Exhaustive BM results on these small instances cross-check native optimal costs. No floating solver result is promoted to a general theorem.
- Any mismatch is retained and investigated. Input data are not changed to erase a failure; implementation corrections are logged.
- Runtime comparisons use a shared requested output where possible, one warm-up, three measured repetitions, and median wall time. Small timings are descriptive and machine-specific. Native solver compilation, startup, proof production, and differing output duties must be disclosed.
- The full BM analyzer emits more than a minimum-cost result. Its elapsed time may be reported as descriptive end-to-end cost, but is not used to claim a fair speed win or loss against a minimal-output solver.
- Record protocol, inputs, code, results, environment, limitations, and checksums in the deliverable.

## Decision rule

Equal outputs mean mathematical agreement, not demonstrated added predictive power. Smaller cost counts only under an identical feasible class. A benefit observed only against an omitted-obligation ablation is evidence for explicit specification, not unique necessity of BM. Failure to beat established methods must be reported plainly. Any demonstrated advantage is restricted to the tested implementation and contract.
