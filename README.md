# Branch Mathematics / GURF Website

Static GitHub Pages site — rebuilt 22 September 2026; research update 9 October 2026.

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
- `calculator.html` — paste-first symbolic calculator and advanced BM checks
- `assets/bm-core.js` — exact finite-state arithmetic and refinement
- `assets/equation-worker.js` — isolated symbolic calculation worker
- `assets/vendor/` — pinned Nerdamer 2.0.0 with licenses
- `book.html` — reading path
- `assets/` — CSS/JS/shared data
- `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` — discovery/support

## Important
MathJax loads from jsDelivr. Everything else is local/static.

## Calculator verification
Run `node tests/calculator.test.cjs` for symbolic and exact finite-state regression checks. The site remains static: no API keys, server execution, or build step. The worker is terminated when the selected time limit is exceeded.
