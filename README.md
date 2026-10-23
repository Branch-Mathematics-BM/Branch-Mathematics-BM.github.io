# Branch Mathematics / GURF Website

Static GitHub Pages site — rebuilt 22 September 2026; research and calculator update 23 October 2026.

## Upload
Copy the site files, including the `assets/` and `downloads/` folders, into the root of the `branch-mathematics-bm.github.io` repository, commit, and push. GitHub Pages deploys from `main`; no local build step is required.

## Structure
- `index.html` — home
- `branch-mathematics.html` — canonical BM
- `gurf.html` — GURF
- `steadman.html` — Steadman Hypothesis V1.1 with October research continuation
- `yang-mills.html` — finite-lattice SU(2) certificates, methods, and downloads
- `downloads/` — reports, exact matrices, rational witnesses, Python source, and review archive
- `encyclopedia.html` — searchable reference
- `theorems.html` — searchable T/W/FI registries
- `definitions.html`, `equations.html`, `structures.html`, `passports.html`, `roots.html` — formal reference
- `research.html`, `applications.html`, `status.html`, `changelog.html` — research/status
- `calculator.html` — semicolon/newline symbolic input and advanced exact BM tools
- `audit.html` — searchable 645-entry, six-label completeness audit
- `development.html` — current proof notes, implementation scope and downloads
- `downloads/bm-2026-10-23/` — 23 pinned source documents, current Research Edition and executable certificates
- `assets/bm-verified.js`, `assets/verified-worker.js` — exact scoped causal, quantum and decay tools
- `assets/bm-core.js` — exact finite-state arithmetic and refinement
- `assets/equation-worker.js` — isolated symbolic calculation worker
- `assets/vendor/` — pinned Nerdamer 2.0.0 with licenses
- `book.html` — reading path
- `assets/` — CSS/JS/shared data
- `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` — discovery/support

## Important
MathJax loads from jsDelivr. Everything else is local/static.

## Calculator verification
Run:

```bash
node tests/calculator.test.cjs
node tests/verified-tools.test.cjs
python3 tests/site.test.py
```

The verified-tools suite compares finite synthesis with an independent machine oracle in 1,458 cases, verifies 15 rational quantum optima, and checks PSD against an independent principal-minor oracle. The site check verifies 932 internal references, source fingerprints and release checksums.

The scalar causal synthesizer supports up to six native states and three predictor states. The quantum tool checks supplied real-rational label-channel certificates; general quantum quantifier elimination is proved but not implemented. The decay budget assumes an independently established uniform task-decay/effectivity contract. Open research stays visible in the audit.

Saved session format 2 includes the new tools; format-1 sessions can still be restored. The site remains static: no API keys, server execution, or build step. The worker is terminated when the selected time limit is exceeded.
