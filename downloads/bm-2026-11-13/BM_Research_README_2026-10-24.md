# BM research package — 24 October 2026

Read `BM_Necessity_Existence_and_Mechanical_Research_2026-10-24.md` first. It contains the literature comparison, assumptions, proofs, mechanical examples, verification results, and remaining research questions.

The note develops:

- Exact future-task realization from observations with bounded or set-valued uncertainty.
- A connected-state obstruction to exact recovery under positive measurement noise.
- The minimum number of additional linear observation channels.
- A classical optimal-recovery formula, with explicit attribution and matching lower/upper certificates.
- Sharp oscillator recovery bounds showing the importance of sampling phase and noise.
- An orbital counterexample: equal position, energy, and angular momentum can conceal opposite radial motion.
- Independent examples of intervention ambiguity and failed global compatibility.

`BM_Mechanical_Necessity_2026-10-24.png` shows the exact oscillator error curve and the numerical orbital illustration. The orbital decimals are not interval-certified; the note's exact derivative argument proves the obstruction.

## Reproduce

With Python 3.10+ and numpy, scipy, and matplotlib available:

```bash
python BM_Research_Verification_2026-10-24.py .
```

The command writes `BM_Research_Verification_2026-10-24.json` and regenerates the PNG. It covers 524 finite noisy-initialization instances, 60 rational linear systems, one explicit oscillator rank example, 160 scalar-recovery comparisons, 160 singular-vector comparisons, exact rational certificates, and mechanical/causal/compatibility examples. The JSON records the versions used for the delivered run. Tiny numerical differences across library versions are possible.

`BM_Research_Source_Manifest_2026-10-24.json` identifies the three unmodified BM sources in `sources/`. External research is cited by primary-source links in the note; copyrighted research PDFs are not redistributed here.

`SHA256SUMS.txt` covers every other package member. To verify after extraction on a system with the corresponding utility:

```bash
sha256sum -c SHA256SUMS.txt
```

This is an additive research package. It does not revise frozen BM identifiers, publish a website change, establish historical novelty, or claim experimental confirmation of BM's physical interpretations. Verification is internal, not independent peer review or proof-assistant checking.
