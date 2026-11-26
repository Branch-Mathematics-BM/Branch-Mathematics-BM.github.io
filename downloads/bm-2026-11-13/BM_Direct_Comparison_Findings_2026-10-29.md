# Direct comparison: Branch Mathematics and established methods

29 October 2026. The comparison protocol and input suite were fixed before execution. They were prepared under filenames dated 24 October and run on 29 October. This is an internal, small-model comparison, not public preregistration, external review, or a representative field trial.

## Result

**BM and the stated native methods agreed on the mathematical outcomes of all 162 test cases.** The tests did not establish a unique predictive or optimization advantage for BM on those cases. They show that the existing BM implementations reproduce results from established techniques under the same declared contracts.

The most credible current value of BM is its explicit organization of multiple requirements and the certificates emitted by its finite reference implementation. A complete workflow built from existing methods can also perform those checks. The comparison does not yet show that BM's organization is faster, less error-prone for analysts, or cheaper in a real application.

| Comparison | Same-contract cases | Outcome |
|---|---:|---|
| Finite future behavior, availability and observation selection | 56 | Same state equivalence, observation sufficiency, relative essentiality and minimum declared observation cost |
| Distributed local interfaces and correlated legal contexts | 36 | Same minimum weighted local alphabet-size cost; every selected native interface was checked against the native task, action and legacy predicates |
| Exact linear differential reduction | 30 | Same minimal dimension and exact row space as the actual CLUE 1.7.3 code; CLUE's exact consistency check passed |
| Scalar oscillator prediction with bounded noise | 40 | Same minimax error as numerical optimization of the classical optimal-recovery dual; largest difference 1.12×10⁻¹⁶ |

All cases are small finite or low-dimensional synthetic examples, including the eight previously supplied BM cases. There were 48 additional seeded finite systems, 30 additional seeded interface systems, 24 seeded linear systems, and the fixed 40 noise/phase combinations. Matching results on these cases is useful validation, not a general theorem of equivalence between complete frameworks.

## What was actually compared

### Finite behavior and observations

The existing BM necessity analyzer starts with the required task partition, refines it under partial deterministic actions, examines available observation features, and emits quotient and separation witnesses. The independently written comparison propagates distinguishable **pairs of states** and solves a binary weighted set-cover problem using SciPy/HiGHS. Both receive the same tasks, allowed actions, exact availability, observations, feature costs, and candidate catalogue.

The methods agree on all 56 tests. The native method's 3,569 distinguishable state pairs were subsequently checked by a separately implemented pair-search replay. Of the 56 examples, full available observations suffice in 36; a supplied candidate catalogue has a feasible member in 35. The difference is the deliberately empty catalogue: adequate observations exist, but no candidate is authorized by that catalogue.

This is a direct match to classical behavioral equivalence and optimization, not evidence that BM discovered state minimization. The BM tool's certificate and contract presentation are concrete outputs that can be assessed for usefulness. A native implementation can also produce witnesses; their absence from one solver call is not proof that the existing method cannot provide them.

### Distributed interfaces

The BM reference program enumerates local equivalence relations over the explicitly legal joint states. It checks the task, legacy distinctions, partial action availability and joint-code closure, then minimizes the specified weighted sum of local alphabet sizes.

The comparison constructs binary variables for local equivalences and local class representatives. Transitivity, task separation, availability and dynamic closure become integer constraints. SciPy/HiGHS solves the resulting model [C2]. The selected interfaces were checked by exact predicates and their costs were recomputed exactly. BM's finite enumeration supplies an additional small-instance check on the numerical solver's optimum.

All 36 minimum costs agree. In eight of the 36 cases the BM enumeration reports that there is **no single greatest feasible family of local equivalences**. The binary optimization was asked for a minimum-cost family, not for a greatest-family existence certificate, so this count is an additional BM output rather than a direct competitive win. The diagonal-copy case shows the distinction: either local source can retain the shared bit, but merging both sources loses it. Cost weights can choose one solution even when there is no greatest permissible family.

### CLUE and exact linear observability

CLUE is an established tool for constrained linear lumping of polynomial systems [C1]. The test used the actual source at pinned commit `0576e9b8477bc511e3fea29a3c296c5d30b688aa` (version 1.7.3 in its `setup.py`). Fourteen imported source/support files were checked against their Git blob hashes before the run. BM's exact rational observability-basis calculation and CLUE received the same linear systems and required observables. Thirty row spaces and dimensions matched, and CLUE's exact consistency check succeeded in each case.

CLUE's published nonlinear example was also run. It reduces the three-state system to the two variables \(x_1\) and \(x_2+2x_3\), with the expected reduced equations. The present BM reference code was **not** run as a general nonlinear polynomial reducer. That example is evidence of CLUE's capability, not a head-to-head nonlinear benchmark.

On the matched linear task, this comparison supports agreement, not mathematical novelty. Different basis vectors are not disagreements if their row spaces coincide.

### Noisy recovery

For the oscillator task and the declared unit-disk/bounded-noise model, the BM note uses the exact scalar optimal-recovery formula. The native comparison minimizes the established dual objective [C3]. The 40 results agree to numerical tolerance. A separate replay constructs matching feasible lower and upper bounds for every case.

The formula's derivation and its antecedent in optimal-recovery theory are credited in the previous research note. Comparing a closed expression to a numerical optimizer does not by itself establish a unique BM result or a general speed advantage.

## Three complete workflow checks

These cases demonstrate why checking more than one requirement can matter. In each case the complete native workflow reaches the same conclusion as the BM workflow.

| Declared requirement | BM and complete native workflow | Meaning of a narrower stage |
|---|---|---|
| Initialize the continuous oscillator's exact future model using present position only | Infeasible: the required two-dimensional future state cannot be determined from one position | CLUE's two-dimensional reduced model is correct, but the reduction call alone does not establish that the state is measurable from the available sensor |
| Recover an oscillator state from samples separated by 1% of a period, with total noise norm ≤0.1 and required error ≤0.2 | Infeasible in the stated unit-disk model; both methods give worst-case error 1 | The noiseless measurement matrix has full rank, which answers a different question from the noise-tolerance contract |
| Satisfy a=b, b=c and a≠c simultaneously | Infeasible | Each individual constraint, and each pair of constraints, is satisfiable |

A negative control is also important: if the only task is **present position**, one coordinate suffices. Requiring the whole continuous future would unnecessarily require a second coordinate for that smaller task. Both a BM workflow and a native workflow must use the actual contract.

## Runtime observations

With one warm-up and three measured repetitions per instance, the median of the per-case medians for the common finite partition calculation was 0.037 ms for the BM implementation and 0.069 ms for the independently written pair algorithm. For the exact linear invariant-subspace calculation it was 0.091 ms for the BM rational routine and 0.136 ms for the CLUE core, with CLUE's cache cleared for each timed call.

These figures describe this machine, these implementations and these very small cases. They do not show that BM is generally faster. The full BM analyzer emits candidate lists and witnesses, whereas the native minimum-cost solver in another comparison was asked for less output; their end-to-end times are not a matched performance comparison. Compilation, numerical solver setup, memory use and scaling were not systematically benchmarked.

## What the result means

The mathematical obligations BM emphasizes are real: the cases expose missing future information, receiver requirements, partial availability, noisy observations and incompatible global constraints. Existing techniques can handle them when the same obligations are specified.

For a stronger claim of BM-specific added value, specify a practical task and compare complete workflows with the same information, model assumptions, candidate classes and budgets. Measures could include missed invalid models, retained communication cost, analyst time, reproducibility, and certified accuracy. The comparison should retain unfavorable results and should not treat a solver's intentionally narrower question as an error.

## Reproduction and evidence

The `comparison/` directory includes the pre-run protocol, all inputs, results, the comparison script, the source manifest, and unmodified BM reference sources. The companion `BM_Comparison_Replay_2026-10-29.py` uses only Python's standard library to check the stored finite, interface, linear and scalar-bound results; it does not rerun CLUE or establish general optimality.

Full re-execution additionally requires NumPy, SciPy, SymPy, Matplotlib, natsort, requests and Beautiful Soup, together with the pinned CLUE repository. Exact package versions used appear in the results JSON. The source setup and earlier pilot error, caused by passing incompatible symbolic input types to CLUE, are recorded in the package README. The benchmark used CLUE's supported exact sparse-polynomial input; no CLUE source was modified.

- **[C1]** A. Ovchinnikov et al., *CLUE: exact maximal reduction of kinetic models by constrained lumping of differential equations* (2021), [paper](https://arxiv.org/abs/2004.11961); [source repository](https://github.com/clue-developers/CLUE).
- **[C2]** SciPy 1.17.0, [`optimize.milp` documentation](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.optimize.milp.html).
- **[C3]** M. Ettehad and S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors* (2021), [author manuscript](https://foucart.github.io/publi/OR_Uncertainty_v2.pdf), Theorem 4.
