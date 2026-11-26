# Branch Mathematics completion and comparison package

29 October 2026. This package is an additive research record for Branch Mathematics. It does not alter the frozen V1 / Edition 1.1 foundation or assert that every open BM problem has been solved.

## Start here

- `BM_Completion_and_Network_Development_2026-10-29.md` gives the review, finite frame and Seed models, proofs, tests, and remaining work.
- `BM_Direct_Comparison_Findings_2026-10-29.md` explains the 162-case comparison with established methods and its limitations.
- `BM_Readiness_Register_2026-10-29.json` preserves the earlier 645-entry inventory and adds this development under `completion_supplement_2026_10_29`.
- `BM_Source_Trace_2026-10-29.json` gives source locators and internal proof-basis notes for the 128 previously unenumerated-dependency BM theorem records. The earlier 55-entry canonical proof map remains in the readiness register.
- `BM_Source_Integrity_2026-10-29.json` records the earlier 23-file manifest recheck. Five relevant source documents and the earlier readiness ledger are copied in `source_evidence/`; the other files from that manifest are not reproduced in this package.

The proof-basis notes are internal reviews of arguments and hypotheses, not an independent mathematical review or formal certification. The recorded dependency graph detects unresolved identifiers and directed cycles, not missing dependencies or invalid inferences. The finite Seed examples are mathematical models, not claims about physical particles. Existing methods can solve the same benchmark problems given the same requirements.

## Replaying the checks

From the extracted package directory, Python 3.10 or later and the standard library suffice for these checks:

```sh
python3 BM_Source_Trace_2026-10-29.py .
python3 BM_Network_Seed_Verifier_2026-10-29.py .
python3 BM_Proof_Examples_Verifier_2026-10-29.py .
python3 BM_Comparison_Replay_2026-10-29.py .
python3 BM_Build_Readiness_2026-10-29.py .
```

The commands write the corresponding JSON files in the supplied directory. The replay checks recorded outputs using separately written code; it does not rerun CLUE or prove all general claims. `SHA256SUMS.txt` records the package files before replay.

The direct comparison's input protocol was prepared before the run under filenames dated 24 October and executed on 29 October. Full re-execution needs the pinned CLUE repository and the Python dependencies and versions listed in `comparison/BM_Comparison_Results_2026-10-24.json`. The third-party CLUE repository is not bundled here; use commit `0576e9b8477bc511e3fea29a3c296c5d30b688aa` from https://github.com/clue-developers/CLUE. Fourteen source/support files were checked against their Git blob hashes for the recorded run. An initial pilot passed bare symbolic expressions through an incompatible CLUE input path and failed; the recorded comparison used CLUE's supported exact sparse-polynomial inputs. No CLUE source was modified.

The independently written standard-library replay does not establish the numerical solver's general optimality. Test counts, native contracts and numerical tolerances appear in the findings and JSON output. Runtime measurements are small-instance observations, not a scaling or general-performance claim.

## Contents

`comparison/` contains the protocol, inputs, raw output, comparator, manifest and unmodified BM source files used in the test. `source_evidence/` contains the exact copied source files needed by the trace. The standalone verifiers and their results are at the package root. `SHA256SUMS.txt` excludes itself and the outer ZIP file.
