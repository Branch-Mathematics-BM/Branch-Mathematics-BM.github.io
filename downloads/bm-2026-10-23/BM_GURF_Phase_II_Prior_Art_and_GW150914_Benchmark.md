# BM / GURF Phase II — Prior-Art Crosswalk + First Real-Data Benchmark

**Project:** GURF Research 001  
**Date:** 2026-09-05  
**Benchmark:** GW150914, GWOSC / LIGO-Virgo public event products

## 1. Prior-art crosswalk — first pass

| BM/GURF construct | Closest established mathematics found | Current novelty judgment |
|---|---|---|
| Exact Task sufficiency / factorization | Classical factorization through fibres/quotients; abstraction theory | Component is classical |
| Task quotient / refinement order | Quotients, partitions, abstraction/refinement | Component is classical |
| Parallel distinction refinement | Product-map / partition refinement | Component is classical |
| Relational MAY/MUST | Dynamic logic / modal transition semantics | Component is classical |
| Backward receiver obligations | Weakest-precondition / predicate-transformer semantics | Strong prior-art overlap |
| Passport / Interface contracts | Assume-guarantee and interface theories | Strongest prior-art challenge |
| Stochastic Dynamic Closure | Markov lumpability / aggregation | Component is classical |
| Stochastic informativeness | Blackwell comparison / garbling / statistical sufficiency | Strong prior-art overlap |
| Privacy Passports | Differential privacy / divergence accounting | Component is classical |
| Conservative ledger | Native invariant / continuity / network balance laws | Component is classical |
| Cross-semantic theorem firewall | No single exact prior-art match established in this pass | Candidate integrated-BM contribution |
| One typed contract layer spanning deterministic, metric, relational, stochastic, privacy, and conservative obligations without flattening native semantics | No single exact match established in this pass; contract/interface theory is close | Candidate integrated-BM contribution; novelty not established |
| Receiver-relative Root / re-entry semantics across heterogeneous mathematical Branches | Interface/contract theories are close but not an exact match established here | Candidate architectural contribution; leverage still required |
| Forward realization flow + backward typed obligation flow across heterogeneous Branches | Predicate transformers and contract theory cover major pieces | Candidate integration, not yet a novelty claim |

### Judgment

The existence of prior art for BM components does not invalidate BM as a higher-order framework. The open question is whether the integrated typed architecture proves or computes something not already supplied as naturally by an existing general framework.

## 2. Real-data benchmark A — detection Task

GWOSC GWTC-1 lists three search pipelines for GW150914:

- cWB: network SNR 25.2, FAR <= 1.63e-4 / yr, p_astro = 1.0
- GstLAL: network SNR 24.4, FAR <= 1e-7 / yr, p_astro = 1.0
- PyCBC: network SNR 23.6, FAR <= 1.53e-5 / yr, p_astro = 1.0

Numerical spread:

- mean SNR = 24.4
- peak-to-peak SNR spread = 1.6
- relative SNR spread = 6.56%
- FAR max/min ratio = 1630
- FAR span = 3.212 decimal orders of magnitude

But the shared receiver-space quantity p_astro is identical:

\[
p_{astro}^{cWB}=p_{astro}^{GstLAL}=p_{astro}^{PyCBC}=1.
\]

### BM interpretation

This is a valid real-data example of receiver-relative Task equivalence:

different native Branch scores can belong to the same detection-Task fibre.

The correct coherence comparison is made in an explicitly common destination space. Pipeline-native scores must not be declared mutually incoherent merely because their numerical values differ.

### Status

**PASS — framework reproduction / organizational leverage.**

It does **not** establish a new physical fact or a new detection theorem.

## 3. Real-data benchmark B — parameter / conservation coherence

GWTC-1 preferred PE central values:

\[
m_1=35.6M_\odot,\quad
m_2=30.6M_\odot,\quad
M_f=63.1M_\odot,\quad
E_{rad}=3.1M_\odot c^2.
\]

Central-value mass-energy ledger defect:

\[
\Delta_M=m_1+m_2-M_f-E_{rad}
\]

gives numerically

\[
\Delta_Mpprox 1.3	imes10^{-15}M_\odot,
\]

i.e. zero to floating-point precision.

The source chirp mass reconstructed from the two central component masses is

\[
\mathcal M
=
rac{(m_1m_2)^{3/5}}{(m_1+m_2)^{1/5}}
=
28.7165M_\odot.
\]

GWOSC reports

\[
\mathcal M=28.6^{+1.7}_{-1.5}M_\odot.
\]

Central-value difference:

\[
|\Delta\mathcal M|=0.1165M_\odot,
\]

about 0.073 of the average quoted 90% half-width.

### Important provenance firewall

These parameters come from one parameter-estimation analysis and are not independent experimental Branches. Their agreement therefore checks internal/native model coherence; it must not be advertised as an independent confirmation of the conservation law.

### Status

**PASS — consistency test. No new information claim.**

## 4. Real-data benchmark C — immutable versioning

GWTC-1 preferred PE versus later GWTC-2.1 PE:

| Parameter | GWTC-1 | GWTC-2.1 |
|---|---:|---:|
| source chirp mass | 28.6 | 27.9 |
| source primary mass | 35.6 | 34.6 |
| source secondary mass | 30.6 | 30.0 |
| final source mass | 63.1 | 61.5 |
| luminosity distance (Mpc) | 440 | 470 |
| redshift | 0.09 | 0.10 |
| sky area (deg^2) | 182 | 250 |
| effective spin | -0.01 | -0.04 |
| final spin | 0.69 | 0.68 |

### BM interpretation

The physical event identity is stable while the analysis representation changes.

This supports immutable versioned Passports:

\[
(	ext{event},	ext{pipeline},	ext{catalog version},	ext{waveform family},	ext{parameter product})
\]

rather than silently replacing an older numerical Root.

### Status

**PASS — BM versioning rule has a direct real-data use case.**

Again, this is not a new astrophysical discovery.

## 5. Review of the first benchmark

### What passed

1. Task-relative sufficiency has a real use case.
2. Common-destination coherence prevents invalid comparison of heterogeneous pipeline outputs.
3. Provenance and immutable versioning are materially useful.
4. Conservative/functional checks can be attached without confusing them with independent evidence.
5. Native physics remained authoritative throughout.

### What did not happen

1. BM did not improve GW150914 detection.
2. BM did not estimate a new parameter.
3. BM did not derive a new gravitational-wave prediction.
4. BM did not outperform the LIGO/Virgo pipelines.
5. No integrated-BM novelty is proved by this benchmark.

### Verdict

\[
oxed{	ext{PASS as framework validation; NOT YET a distinctive BM leverage result.}}
\]

## 6. Decision for the next step

Move from one famous event to a **multi-event, multi-version benchmark**.

Predeclare several Tasks:

1. detection classification stability;
2. parameter-representation stability across catalog versions;
3. functional/coherence defects (chirp mass, total mass, remnant relations where fields are available);
4. uncertainty-aware Task fibres;
5. provenance sensitivity;
6. cross-pipeline common-destination coherence.

Then compare whether BM exposes a failure, redundancy, or minimal sufficient representation earlier or more cleanly than a straightforward native table comparison.

If the answer remains “no additional leverage,” record that as a failure of the proposed BM contribution and move to another domain rather than relabeling the reproduction as novelty.

## Sources

- GWOSC API: https://gwosc.org/api/
- GW150914 v3 parameter product: https://gwosc.org/api/v2/event-versions/GW150914-v3/parameters?format=api
- GW150914 v4 parameter product: https://gwosc.org/api/v2/event-versions/GW150914-v4/parameters?format=api
- LIGO GW150914 science summary: https://ligo.org/science-summaries/gw150914/
- Cousot & Cousot, Galois connection calculus for abstract interpretation: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL14.shtml
- Bauer, Hennicker & Legay, component interfaces with contracts on ports: https://www.sciencedirect.com/science/article/pii/S0167642313002438
- Dynamic logic overview: https://plato.stanford.edu/entries/logic-dynamic/
- Buchholz, lumpability in finite Markov chains: https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/exact-and-ordinary-lumpability-in-finite-markov-chains/2DC748F09D80BEEB03CCF18036E149D7
- Blackwell comparison discussion: https://doi.org/10.1016/j.econlet.2024.112146
