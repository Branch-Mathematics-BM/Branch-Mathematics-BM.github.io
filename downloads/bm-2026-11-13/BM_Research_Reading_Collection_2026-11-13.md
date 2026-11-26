# Branch Mathematics — research reading collection

Publication: 13 November 2026. Recovered developments through 1 November 2026.

This collection appends the dated source notes to the 23 October Research Edition. Original source text and source-local identifiers are retained. Later dated corrections govern their stated scope. It does not amend frozen V1 or certify completion, historical novelty or independent review. November executables and selected October checks were replayed; the recorded 162-case external-method benchmark was not rerun.

## Contents

1. Research Edition, 23 October 2026
2. BM: necessity certificates and an exact comparison with existing theory (BM_Necessity_and_Comparison_2026-10-23.md)
3. What remains to complete BM (BM_Completion_Requirements_2026-10-23.md)
4. BM canonical proof-dependency map (BM_Canonical_Dependency_Map_2026-10-23.md)
5. Reading correction to the historical BM/GURF benchmark (BM_Benchmark_Reading_Corrections_2026-10-23.md)
6. Branch Mathematics: necessity, constructive existence, and mechanical tests (BM_Necessity_Existence_and_Mechanical_Research_2026-10-24.md)
7. Branch Mathematics: completion review and tree-network development (BM_Completion_and_Network_Development_2026-10-29.md)
8. Direct comparison: Branch Mathematics and established methods (BM_Direct_Comparison_Findings_2026-10-29.md)
9. New application directions for Branch Mathematics (BM_New_Uses_2026-10-29.md)
10. Branch Mathematics — Seed provenance, law uncertainty, and closure (BM_Seed_Provenance_Completion_2026-11-01.md)
11. Branch Mathematics — Acquiring Seed-law information without probability (BM_Adaptive_Seed_Acquisition_2026-11-01.md)
12. Branch Mathematics — An unbounded finite Seed measurement adaptivity gap (BM_Seed_Adaptive_Gap_Theorem_2026-11-01.md)
13. Branch Mathematics — Compact Seed recovery and its exact failure modes (BM_Compact_Seed_Recovery_Theorem_2026-11-01.md)
14. Branch Mathematics — Finite-horizon Seed recovery versus autonomous closure (BM_Dynamic_Seed_Recovery_and_Closure_2026-11-01.md)
15. Branch Mathematics — Finite stabilization and minimal autonomous task-Seed quotient (BM_Finite_Task_Closed_Seed_Quotient_2026-11-01.md)
16. Branch Mathematics — Joint-receiver closure and lawful Seed gluing (BM_Joint_Receiver_Closure_and_Seed_Gluing_2026-11-01.md)
17. Branch Mathematics — Set-valued Seed closure, branching, and receiver noncomposition (BM_Set_Valued_Seed_Closure_and_Branching_2026-11-01.md)

---

> Public working Research Edition, 23 October 2026. Frozen V1 and dated additive proofs retain their stated scope. See the current public audit for the completion record.

---
title: "Branch Mathematics"
subtitle: "Foundations and Research Developments"
author: "Branch Mathematics Project"
date: "15 September 2026"
lang: en-US
documentclass: scrreprt
classoption: [oneside, openany, titlepage]
fontsize: 11pt
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
mathfont: Latin Modern Math
geometry: [letterpaper, left=0.85in, right=0.85in, top=0.82in, bottom=0.82in, includefoot, footskip=24pt]
colorlinks: true
linkcolor: black
urlcolor: black
toc: true
toc-depth: 0
numbersections: true
header-includes:
  - '\usepackage{amsmath,amssymb,mathtools}'
  - '\usepackage{booktabs,longtable,array}'
  - '\usepackage{xurl}'
  - '\usepackage{needspace}'
  - '\setlength{\emergencystretch}{3em}'
  - '\setlength{\parindent}{0pt}'
  - '\setlength{\parskip}{5pt plus 1pt minus 1pt}'
  - '\setcounter{secnumdepth}{1}'
  - '\setkomafont{disposition}{\normalfont\bfseries}'
  - '\RedeclareSectionCommand[beforeskip=0pt,afterskip=18pt,tocnumwidth=2.5em,tocpagenumberwidth=2.5em]{chapter}'
  - '\AtBeginDocument{\setcounter{tocdepth}{0}\let\oldtoc\tableofcontents\renewcommand{\tableofcontents}{\clearpage\oldtoc\clearpage}}'
---

# Reading this research edition {.unnumbered}

**21 October 2026 continuation.** The final chapter classifies Jordan long-return endpoint pairs for every chain length and supplies exact rational nonlinear certificates. The unit four-state continuous scalar error is bounded between 1.1258738292 and 1.1379367294; the narrower [1.2948,1.2949] squared interval applies only to cubic invariant encoders with the specified decoder. The unrestricted optimum remains open. This is a working integration snapshot while the preceding master-file write is unconfirmed.

**20 October 2026 continuation.** The final chapter proves the original continuous n=3,d=1 Jordan optimum and gives an explicit n=4 nonlinear improvement over every closed linear scalar code. It adds exact finite causal synthesis with unrestricted Euclidean outputs, sharp full-algebra quantum bounds in every finite dimension, and effective/native limit results. Earlier dated scope statements are superseded where identified in this chapter; six broad research extensions remain.

**19 October 2026 development update.** The final chapter adds 24 scoped theorem/construction results, three finite native definitions and executable solvers. Finite correlated greatestness and fragmentation complexity are resolved. The original continuous Jordan, general smooth minimum, broader causal, higher-dimensional quantum, unrestricted repair and restricted infinite/native questions retain the precise boundaries in that chapter. The frozen V1 foundation is unchanged.

**14 October 2026 research addenda.** The strict-projector example’s inaccurate numerical slope is corrected and its optimum rationally certified. The appended development gives quantitative penalty bounds and an explicit nonlinear repair with optimal noisy decoders. The closing addendum now supplies a general finite global projector certificate for every rational SPD input and positive tolerance, plus an exact rank-two example. Earlier blanket statements that finite global certification is open are superseded to this scope. Computational efficiency and broader unresolved research/evidence obligations remain separate. Public theorem identifiers and the frozen foundation are retained.

**15 October 2026 nonlinear repair extension.** The appended theorem now gives exact continuous repair for a coupled nonlinear class with fast-decaying omitted influence, a conditioned C1 coordinate repair in its triangular subclass, sharp uncertainty and finite-window estimates, and an all-orders resonance obstruction. The bounds state exactly which gaps and regularity are required. Arbitrary nonlinear optimum/cost questions and missing physical evidence remain unresolved.

Branch Mathematics studies what a representation must retain when a problem moves between mathematical descriptions. A current measurement, a future prediction, a lawful interaction, and a physically implementable recovery can require different distinctions. The central question of this book is precise: **which distinctions may be identified while all declared obligations remain satisfied?**

The answer is sometimes a quotient, sometimes a larger state, sometimes an approximation bound, and sometimes a proof that the requested realization does not exist. The book develops these answers with explicit domains, proofs, counterexamples, and finite computations. It is intended for readers who know basic linear algebra and functions; the later analytic and quantum chapters identify their additional prerequisites.

This edition preserves the Version 1 architecture governed by the 12 September 2026 Edition 1.1 amendment. It brings that architecture together with the subsequent Volume II development, the consolidated W01-W35 exploration, and the FI01-FI42 application audit. The public T01-T55 identifiers keep their original meanings. Later results do not silently rewrite them.

The mathematical content is offered for public technical review. A result described as proved has a written argument under its stated hypotheses; that description is not a claim of independent peer review, formal verification, or historical priority. An open research program has no meaningful certificate of being 100 percent finished. The release audit accompanying this book records the remaining proof, coverage, and novelty questions.

The distinctive case for BM is its coordination of requirements. The quotient constructions, fixed-point methods, low-rank approximation, lumpability, and quantum error-correction ingredients have substantial prior art. The book credits those ingredients and asks whether their combination produces a useful obstruction, a computable interface, or a quantitative performance comparison. It does not count a new name as a new theorem.

## The principal results {.unnumbered}

The finite interface theorem produces a uniquely coarsest family of exact Branch interfaces under independently substitutable contexts. The smooth-realization counterexample shows that an analogous coarsest object can fail to exist under a submersion requirement. The shear and Jordan-chain results quantify an order-one cost of exact autonomous closure even when unrestricted approximation becomes arbitrarily accurate. The W35 construction proves that minimizing the number of fragmented rows can force an unbounded multiplicative increase in total fragmentation. The quantum chapters separate linear factorization, physical closure, exact algebra recovery, and approximate recovery.

This edition supplies additional explicit arguments for two gaps in the development: a finite-dimension bound connecting the normalized commutator defect to physical recovery, and a qubit example with no greatest approximately recoverable task algebra. It also gives a finite reduction-order counterexample and an exact algorithm for the fragmentation tradeoff. These are scoped results and credited consequences; no priority claim accompanies them.

## How to use the book {.unnumbered}

Read the architecture and exactification chapters first. Then choose the chapters matching the native problem: finite interfaces, regular realization, dynamics, metric approximation, quantum recovery, or experiment design. GURF is presented as the response-specialized layer under BM. The appendices retain the supporting theorem proofs and research registries so that a short main-text explanation does not erase an assumption or a historical correction.

For every theorem, distinguish three questions. Is its mathematical statement true under the written assumptions? Can the representation or decoder be constructed in the intended native class? Is it useful and original compared with existing methods? A positive answer to one question does not supply the other two.

## Status language {.unnumbered}

**Proved here** means a proof is supplied in this edition. **Retained proof** means the governing source argument is reproduced with its scope preserved. **Imported** means an established theorem is used with attribution. **Synthesis** means a BM organization or consequence of those ingredients. **Open** means an unresolved question. **Historical record** means an item is retained for traceability without being newly certified. These labels concern evidence, not prestige.

The distinction between theorem and physical model is especially important. Information is used here as task-relative distinguishability, not as a material substance. Injectivity preserves complete-state distinctions; universal injectivity of physical dynamics is an additional claim. Nothing in a quotient proof creates fields, energy, particles, or a new force.

# A running problem

Consider a system with two coordinates and one observed output:

$$\dot x=v,\qquad \dot v=0,\qquad y=x.$$

At the present instant, retaining $R(x,v)=x$ answers the output task exactly. At a later time $t$, the required answer is $x+tv$. The states $(0,0)$ and $(0,1)$ therefore agree on the retained observation but disagree on the future task. A reduced update depending only on the present $x$ cannot produce both answers.

Several repairs are possible, and they solve different problems. Retaining $v$ as well produces a two-coordinate autonomous state. Restricting the admissible states to a known value of $v$ changes the source model. Adding a new measurement supplies an external distinction. Accepting a tolerance changes the task. A trajectory decoder can use an explicit clock, but the clock does not reveal an unknown initial velocity.

In BM terms the evolution and observation are native Branch data; the future-output requirement is a task; the failed factorization is an obstruction Leaf; the augmented state is a candidate realization; and a receiver accepts its export only after the relevant requirements are checked. The terminology follows the calculation.

The same pattern appears in other sectors. Equal aggregate concentrations need not determine future reaction outputs. Equal boundary traces for one task may fail a coupling requirement. A quantum matrix map may have an algebraic inverse that is not a physical channel. A collection of locally compatible data can fail to have a global realization. The point of the framework is to carry the exact requirement through those changes of setting.

The reward for doing this carefully is a concrete decision: what to measure, retain, communicate, reconstruct, or declare impossible. BM is most useful when more than one of these requirements acts on the same problem.


# The BM architecture

Branch Mathematics is a mathematical metaframework for carrying one problem through distinct mathematical Branches while preserving the native mathematics of each Branch. Version 1 does not assume that those Branches unify. Compatibility, transport, descent, gluing, realization, and joint computation are obligations to establish.

## Typed Branch record

A problem specification fixes its scope, native mathematical sectors, terminal obligations, allowable interventions, and comparison rules. A Branch is recorded as

\[
B=(\mathsf S_B,\tau_B,X_B,A_B,\mathcal L_B,\mathcal O_B,\mathcal P_B).
\]

Here \(\mathsf S_B\) is the native sector, \(\tau_B\) its type, \(X_B\) its carrier, \(A_B\) its admissible objects, \(\mathcal L_B\) its declared laws, \(\mathcal O_B\) its Operations, and \(\mathcal P_B\) its contracts in context. The record supplies no universal topology, algebra, probability law, or scalar information measure. Those come from the native sector.

An **Operation** is a specified native action. In a deterministic set sector it may be a partial map

\[
f:D_f\subseteq X\to Y.
\]

An **Interaction** combines declared Branch inputs. In the same sector it has the form

\[
G:D_G\subseteq A_1\times\cdots\times A_m\to W.
\]

Input admissibility by itself does not establish membership in \(D_G\). Likewise an output inherits topology, conservation, positivity, algebra, or physical meaning only through a specified construction or theorem. The names Branch and Interaction create none of these properties.

A **Leaf** is a derived result carrying its native statement, hypotheses, derivation or certificate, and provenance. A numerical output without a validated domain and error model remains a calculation rather than a universal theorem. A Leaf may be reused only when its hypotheses survive the new use.

## Contracts and Passports

A contract is a typed specification

\[
\mathcal C^\rho=(\Sigma^\rho,\Phi^\rho),
\]

and a Passport is an instantiated contract \(\mathcal P^\rho_{\theta,c}\) at parameters \(\theta\) and context \(c\). In a predicate sector write a Passport as \((D_{\mathcal P},A_{\mathcal P})\) with \(A_{\mathcal P}\subseteq D_{\mathcal P}\). The three logical outcomes are: not applicable; applicable and rejected; accepted. Acceptance may contain several independent obligations.

For a total export \(E:X\to Y\), Passport pullback is

\[
E^{\star}(D,A)=(E^{-1}D,E^{-1}A).
\]

For a partial export, the pullback is first restricted to the actual export domain. Exact task requirements can often be encoded as functions, but a general Passport is not automatically a deterministic observation map.

## Configuration, Tree, Response, and Root

A **Configuration** is

\[
C=(\Sigma_C,\Gamma_C,c),
\]

where \(\Sigma_C\) declares typed objects and coordination data, \(\Gamma_C\) the applicable obligations, and \(c\) the context. Its realization family is

\[
\mathfrak F(C;c)=\{\xi\in\operatorname{Int}(\Sigma_C;c):\xi\models_c\Gamma_C\}.
\]

Writing this set does not prove it is nonempty. Well-formedness and global realizability are different questions.

A realized **Tree** can be recorded as

\[
\mathcal T=(C,\xi,\Pi,\omega,\Lambda),
\]

with realization \(\xi\), certified provenance/dependency record \(\Pi\), order or history context \(\omega\), and active law assignments \(\Lambda\). The dependency structure may contain local trees inside a DAG or hypergraph. Calling a cyclic dependency a Tree does not make it recursively well founded.

A **Response** is a declared Tree-level output, possibly law-valued or set-valued. An export translates it to a receiver type. A **Root** is an export accepted under a specified receiver Passport. Root status is receiver-relative: acceptance by one receiver does not imply acceptance by another, and re-entry into a new Branch is a new use with new obligations.

Rooting, Rebranching, and Seed remain candidate research structures except where an ordinary native construction has separately been specified and proved. They are not required for the Version 1 core.

## Three closure universes

Version 1 freezes three mathematically different closure mechanisms.

Component dependency closure acts on configuration components,

\[
\operatorname{Cl}_C:2^{V_C}\to2^{V_C}.
\]

Obligation prerequisite closure acts on obligations,

\[
\operatorname{ReqCl}_C:2^{\Omega_C}\to2^{\Omega_C},
\]

with required obligations \(\mathscr Q_P=\operatorname{ReqCl}_C(\mathscr T_P)\). Each of these must be extensive, monotone, and idempotent before least-closure language is used.

The third construction acts on equivalence relations and **refines** them to preserve tasks, continuation, or Interactions. It is not either of the two preceding closure operators. The difference in carrier and order direction is substantive.

## Representation and admissibility

For functions \(R:X\to Z\) and \(T:X\to W\), exact task sufficiency means

\[
T=\bar T R
\quad\Longleftrightarrow\quad
\ker R\subseteq\ker T.
\]

This is a set-level factorization statement. It promises no continuous, computable, stable, positive, or physically implementable decoder. Structured quotients require congruence with every declared operation, including domain saturation for partial operations.

For a partial evolution \(\Phi_t:D_t\to X\), exact partial Dynamic Closure through \(R\) requires both

\[
D_t=R^{-1}(\bar D_t),\qquad R\Phi_t=\bar\Phi_tR\quad\text{on }D_t.
\]

The evolution and its domain are inputs to the theorem; the quotient theorem does not construct a PDE solution or extend a solution through a singular endpoint.

## Native-sector integrity

Every Branch keeps its native objects, domains, smoothness, measurability, units, algebra, positivity, probability kernels, or channel constraints. No deterministic theorem is silently promoted to stochastic, relational, quantum, or smooth semantics. Bridges must state what is transported and what additional hypotheses are required.

An exact deterministic representation cannot recover a distinction that it identifies by later deterministic processing alone. A repair can add retained history, a new observation, or another independently specified source. This set-theoretic statement is not a theorem of universal physical information conservation.

## Receiver-relative specification and essentiality

Sufficiency, essentiality, and minimality are always relative to a declared task or candidate class. A Branch is essential only relative to a fixed, independently specified coarsening class. Defining the candidate class by already preserving the target obligations would make the test circular. Branch count is therefore not an invariant of a mathematical object without an equivalence and irreducibility theorem.

## Defect and repair

A defect is failure of a named obligation \(\Psi\), not an unspecified scalar amount of badness. Repair is a declared admissible relation between Configurations with explicit change support and revalidation. Defect Calculus remains a specialized program; Version 1 assumes no universal scalar defect algebra.

Use BM when several representations, interfaces, admissibility requirements, response tasks, or realization classes need coordination. When the native mathematics already answers the question and BM adds no distinction, calculation, or certificate, the native result should be used directly.

## GURF under BM

Branch Mathematics owns the domain-independent representation and transformation mathematics. GURF is the response-specialized layer: tasks, observations, continuation, interventions, inverse recovery, memory, and repair. Core, SOE, ACE, IRE, UKE, HDE, and GHSE retain their Version 1 roles; GRDE remains frozen at 008.

## Frozen dependency order

The canonical direction is

**Native problem -> contract -> required distinctions -> descent -> synthesis -> realization -> cost -> receiver export.**

If a preferred coordinate system or model class is chosen first and the task is tested afterward, that is a different model-selection problem. BM starts with the contract and derives what may lawfully be merged before optimizing a realization.

# Exact deterministic representation and continuation


## Contract and legacy exactification

Let X be a set and let M be a **set** of total self-maps of X containing the identity and closed under composition. Let Q be a set-indexed task family T:X→Y_T. Let R:X→Z be an existing representation that must remain recoverable from the repaired representation.

Define

\[
E_Q=\bigcap_{T\in Q}\ker T,
\qquad
E^\#=\bigcap_{m\in M}(m\times m)^{-1}(\ker R\cap E_Q).
\]

Equivalently, x E# y precisely when every future legacy value R(mx) and every future task T(mx) agrees with its counterpart at y.

**Theorem.** E# is the unique largest equivalence contained in ker R∩E_Q that is stable under every map in M. Its quotient q:X→X/E# supports every task, the legacy representation, and all declared continuations. Every other exact autonomous representation S retaining those obligations has ker S⊆E# and therefore a unique induced map S(X)→X/E#.

**Proof.** Each term defining E# is an equivalence, so their intersection is one. The identity term enforces the current legacy and task requirements. If x E# y and n∈M, then for every m∈M the composite mn belongs to M; hence nx E# ny. Thus [x]↦[nx] is well-defined on the quotient, and every task and R is constant on quotient classes.

Conversely, let H be an equivalence contained in ker R∩E_Q and stable under M. If x H y, then mx H my for every m; therefore R(mx)=R(my) and T(mx)=T(my). Thus H⊆E#. Apply this to H=ker S. Fibre factorization gives the unique induced quotient map. $\square$

For an arbitrary input equivalence E, define

\[
\mathfrak E_Q(E)=\bigcap_{m\in M}(m\times m)^{-1}(E\cap E_Q).
\]

It is monotone and contractive. Applying it twice introduces composites mn and duplicates already-required task tests. Since M is a monoid and contains the identity, those tests are exactly the original tests, proving idempotence. This is an interior/refinement operator in the inclusion order on equivalences; calling it an extensive closure in that order would reverse the meaning.

For partial operations, use an explicit unavailable tag and preserve the actual composition domains. Arbitrary partial tasks cannot be treated as ordinary total maps without this change. For stochastic or game semantics, replace the deterministic statement by the corresponding native theorem.

## Simultaneous refinement beyond finite sets

The source T55 construction also has a set-level existence extension. Keep a set-indexed family of carriers X_i, initial equivalences B_i, action relations, and finite-arity partial Interactions, with the same independently substitutable Cartesian contexts as the finite interface chapter.

On

\[
\mathcal L=\prod_i[\Delta_{X_i},B_i]
\]

define F by the source refinement formula: intersect the current equivalence with equal successor signatures and equal tagged contextual output classes. This is a monotone, contractive map of a complete lattice. Monotonicity follows because equality of successor classes under a finer equivalence implies equality after passing to coarser classes, and likewise for tagged Interaction outputs.

**Theorem.** A unique coarsest exact equivalence family exists in this set-level class. It is the greatest fixed point of F below B.

**Proof.** Start at B, iterate F at successor ordinals, and intersect all earlier equivalences at limit ordinals. Every strict step removes a pair from a set of available pairs, so this descending construction must stabilize at some ordinal. Its fixed point satisfies the source descent obligations. Every other admissible family H remains contained in each stage: the successor step is the source monotonicity argument, and the limit step is intersection. Thus the terminal family contains every admissible H and is uniquely coarsest. $\square$

This is an application of classical complete-lattice fixed-point reasoning, not a new fixed-point theorem. [Tarski, *A lattice-theoretical fixpoint theorem and its applications*, Theorem 1](https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-p.pdf).

The result gives neither finite termination nor a computable procedure on arbitrary infinite presentations. In particular, it does not assert that countably many rounds suffice for arbitrary infinitely branching relations, or that the resulting equivalence has a continuous or smooth realization.

## Finite stochastic extension and explicit-table complexity

For finite Markov actions, replace a relational successor signature by the vector

\[
\left(\sum_{y\in B}K(x,y)\right)_{B\in X_i/E_i}.
\]

Equal signatures are exactly equality of the aggregated laws. Intersect their kernels with the same tagged Interaction-context constraints and initial tasks. The termination and coarsestness proof carries over: equal finer-block sums remain equal after summing them over coarser blocks.

For explicitly listed finite carriers, rational transition tables, and complete finite Interaction tables, this gives a polynomial-time procedure in the explicit input size. Each strict round increases a class count; there are at most Σ_i(|X_i|-|X_i/B_i|) strict rounds. Each round computes finite block sums and signatures by scanning the supplied tables, then groups equal signatures. Rational comparison is exact with polynomial bit complexity for these sums.

This addresses the explicit-table sector of the historical log's stochastic-refinement question. It is not a complexity result for succinctly represented exponentially large state spaces, restricted correlated contexts, or interactive strategies.

# Finite interface synthesis

## Mathematical objective

The task is to find the coarsest branch-local exact interfaces that preserve a declared receiver task, local evolution, and each declared Interaction. Static task quotients alone can fail after one step. Independently stable local quotients can fail at an Interaction. The result below enforces both requirements simultaneously and records why each extra distinction is necessary.

The deterministic theorem completes T55-C7 from the canonical log. The relational form is a derived extension, labelled T55-C7R here. Its mathematical ingredients are stable partitions, congruences, and finite fixed points. The construction and proof are part of BM development; external historical novelty is not asserted.

This chapter proves T55-C1 trace lifting, T55-C2 stable task quotient (the one-Branch, no-Interaction case), T55-C3 radius bounds, T55-C4 error propagation, T55-C5 the sufficient composition rule, T55-C6 minimal receiver repair, T55-C7 deterministic simultaneous refinement, and T55-C7R its finite relational extension. These remain a connected theorem family rather than inflated independent IDs.

## Exact finite model

Let $X_1,\ldots,X_n$ be nonempty finite sets. Branch $i$ has an initial equivalence $B_i$ encoding every distinction already required by its tasks and Passport. A family $E_i\subseteq B_i$ is a refinement; a larger equivalence relation merges more states and therefore gives a coarser interface. There are finitely many declared action relations $L_{i,a}\subseteq X_i\times X_i$. A partial deterministic action is represented by its graph, and absence of a successor remains distinguishable from a nonempty successor set.

Each Interaction is a partial function

$$G_b:D_b\subseteq X_{i_1}\times\cdots\times X_{i_m}\to X_{r(b)}.$$

All Cartesian contexts are required in this theorem. Input slots are independently replaceable; if an application imposes shared-variable aliasing, correlated admissibility, or a restricted reachable context family, that family needs its own substitution-closure argument. The theorem's minimality is relative to these declared product-form obligations.

Add an output tag $\bot$ and totalize $G_b$ to $\widehat G_b$. Extend receiver equivalence $E_{r(b)}$ by the singleton class $\{\bot\}$. This distinguishes undefined output from every defined output.

For relation $L$ define the successor signature

$$S_{L,E_i}(x)=\{[y]_{E_i}:xLy\}.$$

For input slot $p$ of Interaction $b$, define contextual equivalence

$$\begin{gathered}
u\ C_{b,p}(E_{r(b)})\ v\quad\Longleftrightarrow\\
\widehat G_b(c_1,\ldots,u,\ldots,c_m)
\ E_{r(b)}^{\bot}\
\widehat G_b(c_1,\ldots,v,\ldots,c_m)\\
\text{for every other input tuple }c.
\end{gathered}$$

Both are kernels of specified signature maps, hence equivalence relations. No collision-overlap relation is substituted for equality here.

## T55-C7R Finite simultaneous refinement theorem

Starting at $\mathbf E^0=\mathbf B$, define

$$E_i^{k+1}=E_i^k\cap\bigcap_a\ker S_{L_{i,a},E_i^k}
\cap\bigcap_{b,p:i_p=i}C_{b,p}(E_{r(b)}^k).$$

Then the iteration terminates at a family $\mathbf E^*$. It has all of the following properties.

1. Every task and initial Passport distinction represented by $B_i$ factors through $X_i/E_i^*$.
2. Each local relation has an exact reduced successor relation; dead ends are preserved.
3. Every Interaction descends to a partial map on the product of reduced interfaces, preserving both definedness and output class.
4. Every other equivalence family $\mathbf H\subseteq\mathbf B$ satisfying these same requirements obeys $H_i\subseteq E_i^*$. Thus $\mathbf E^*$ is uniquely coarsest in the declared class.
5. There are at most $\sum_i(|X_i|-|X_i/B_i|)$ rounds that make a strict refinement.

### Proof of termination and equivalence

Each signature kernel and contextual relation is an equivalence. Their intersection with $E_i^k$ is an equivalence contained in $E_i^k$. Every strict round increases the total number of equivalence classes by at least one. That number starts at $\sum_i|X_i/B_i|$ and is at most $\sum_i|X_i|$. The chain therefore terminates with the stated bound. This is a bound on strict rounds, not on runtime or the size of context tables.

### Proof of exactness at the fixed point

Task preservation follows from $E_i^*\subseteq B_i$. At the fixed point, $xE_i^*x'$ implies equality of successor-class sets for each action. Define the reduced successor set of $[x]$ to be $S_{L,E_i^*}(x)$; this is independent of the representative. Empty sets are retained exactly.

For an Interaction take input tuples $(u_1,\ldots,u_m)$ and $(v_1,\ldots,v_m)$ with $u_pE_{i_p}^*v_p$ for every slot. Replace the slots one at a time. Contextual equivalence shows equality of tagged output classes at each replacement. Transitivity gives equality from the original to the final tuple. Since $\bot$ is a separate class, one tuple is in $D_b$ iff the other is; when defined, their receiver classes agree. This defines the reduced partial Interaction with the required domain.

### Proof of coarsestness

Let $\mathbf H$ satisfy the requirements and refine $\mathbf B$. We prove $H_i\subseteq E_i^k$ for every $k$ by induction. It holds at zero. Suppose it holds at $k$. If $xH_ix'$, exact $H_i$-closure gives equality of their sets of successor $H_i$-classes. Mapping each $H_i$-class to its containing $E_i^k$-class gives equality of successor $E_i^k$-classes. For an Interaction, changing one $H_i$-equivalent slot with the other slots identical gives equal tagged receiver $H$-classes. Those are contained in equal receiver $E^k$-classes. Thus the pair lies in every intersection defining $E_i^{k+1}$. Induction proves $\mathbf H\subseteq\mathbf E^*$.

The terminal family itself is admissible, so it is the greatest admissible family of equivalence relations below $\mathbf B$, hence the coarsest exact interfaces. Uniqueness follows from mutual inclusion of any two such greatest families. This finishes the proof. $\square$

## Deterministic specialization and finite composition

For total deterministic $f_{i,a}$, $S_{L,E}(x)=\{[f_{i,a}(x)]_E\}$, so the action term is $(f_{i,a}\times f_{i,a})^{-1}E$. This recovers T55-C7 exactly. Partial maps additionally distinguish the empty signature from singleton signatures, enforcing availability.

For one relation $L$ satisfying exact closure, every finite reduced path starting at $[x]$ lifts to a path starting at that specific $x$. For the first edge, equality of successor-class sets supplies a successor in the desired class. Repeat this argument from the selected successor for each edge. Induction gives

$$q(L^m[x])=\bar L^{\,m}[q(x)]\qquad(m\ge0).$$

The same proof applies to a declared finite word of action labels. It does not infer a game strategy from reachable sets, erase action scheduling, or automatically supply an infinite path or analytic limit. For product-independent local relations followed by an Interaction that descends, match each coordinate's successor class and then apply Interaction descent; this proves the sufficient compositional certificate T55-C5. A correlated joint transition requires its own joint closure audit.

## Receiver-relative minimal repair T55-C6

Suppose an existing interface $R_i$ must be retained and only a receiver task $T$ of an Interaction output matters. Totalize the Interaction and task so that applicability is a separate output. Define

$$u\equiv_i v\ \Longleftrightarrow\ R_i(u)=R_i(v)\ \text{and}\
\widehat T\widehat G(u,c)=\widehat T\widehat G(v,c)\quad\forall c.$$

This is an intersection of kernels and hence an equivalence. Coordinate-by-coordinate substitution proves that the task-level Interaction factors through the product quotients. Conversely any branch-local refinement retaining $R_i$ and supporting that task factorization must identify only pairs with equal values in every fixed context. Its equivalence is therefore contained in $\equiv_i$. This proves coarsestness. Enlarging the task or context family adds intersections and can only refine the quotient. If contexts are restricted, the substitution argument must remain inside the declared context family; arbitrary restrictions do not supply this automatically. $\square$

## Witnesses and an operational example

A certified implementation records each round and a reason for every split: distinct successor signatures, a defined/undefined mismatch, or an Interaction context with distinct receiver signatures. These witnesses can be replayed from the finite tables. They are certificates of this supplied finite model; they are not physical measurements or claims of optimal hardware cost.

Consider a source Branch $A=\{0,1\}$ with identity local evolution and initially constant observation, an input Branch $B=\{0,1\}$ with identity evolution, and a receiver Branch $C=\{0,1\}$ whose task is its identity. Let $G(a,b)=a\mathbin{\mathrm{xor}}b$. Local dynamics permit the constant interfaces on $A$ and $B$. The context $b=0$ distinguishes the two $A$ states at the receiver, and $a=0$ distinguishes the $B$ states. Refinement therefore makes both source interfaces injective. If the receiver task is instead constant and domain acceptance imposes no distinction, no such split is needed.

For delayed observation, let $X=\{0,1,2,3\}$, $f=(1,2,3,0)$, and task values $(0,0,1,1)$. The initial blocks are $\{0,1\},\{2,3\}$. States 0 and 1 have successor task blocks 0 and 1, respectively; likewise states 2 and 3. The first refinement is discrete. Present task sufficiency was exact, yet one-step closure required all four states.

## Approximate relational closure T55-C3 and C4

Let $Z$ be metric and $Q(x)$ nonempty compact subsets. For a nonempty fibre $R^{-1}(z)$ put $\mathscr Q_z=\{Q(x):R(x)=z\}$, with Hausdorff diameter $\Delta(z)$. Define the infimum radius over nonempty compact centers $C\subseteq Z$ by $\rho(z)=\inf_C\sup_{A\in\mathscr Q_z}d_H(A,C)$. The triangle inequality gives $\Delta(z)\le2\sup_A d_H(A,C)$ for every center; choosing a member of the family as center gives $\rho(z)\le\Delta(z)$. Therefore

$$\tfrac12\Delta(z)\le\rho(z)\le\Delta(z).$$

Infimum zero implies diameter zero by the first bound, so all sets are equal and exact closure holds. Exact closure gives radius zero. A minimizing center need not exist without additional hypotheses. Empty successors require a separate convention and are excluded from this statement.

For finite-horizon propagation, suppose every current set and its image is nonempty compact, unions used below remain compact, and $\bar Q$ satisfies $d_H(\bar Q(z),\bar Q(z'))\le Ld(z,z')$. Assume $d_H(Q(x),\bar Q(Rx))\le\varepsilon$ uniformly. The union operator $\bar Q_\cup(A)=\bigcup_{z\in A}\bar Q(z)$ is $L$-Lipschitz: match a point's source $z$ with a nearby $z'$ and use the set-valued Lipschitz estimate, then take suprema and limits. The pointwise one-step mismatch gives the same bound $\varepsilon$ for unions over any common concrete set. Consequently the error between the concrete reachable image and reduced reachable set satisfies $e_{k+1}\le\varepsilon+Le_k$. Induction from $e_0=0$ yields

$$e_m\le\varepsilon\sum_{j=0}^{m-1}L^j.$$

No exact quotient is formed from the relation $d\le\varepsilon$, and no infinite-time estimate follows unless the constants make one available. $\square$

## Limits of the synthesis theorem

The theorem establishes interface compatibility and exact finite behavior under supplied operations. Additional global constraints can still make the Configuration unrealizable. It does not prove a continuous or smooth quotient, a stochastic reduction, minimal coordinate dimension, minimal bit cost, or the availability of distinctions absent from an exported carrier. A refinement algorithm can identify what information is required even when the system cannot supply it.

# Repair memory and reduction order

## Optimal error inside a fibre

Let $R:X\to Z$ be a representation and let $T:X\to Y$ take values in a metric space. For each realized $z$, set $F_z=R^{-1}(z)$. With arbitrary decoders taking values in $Y$, define

$$e^*(R,T)=\inf_D\sup_x d(Tx,D(Rx)).$$

Let $\Delta=\sup_z\operatorname{diam}T(F_z)$. Then $e^*\ge\Delta/2$. Indeed two states in one fibre have a common decoded value; the triangle inequality bounds their task separation by twice the worst error. If a representative can be selected from each nonempty fibre, $e^*\le\Delta$. For a bounded real-valued task the midpoint between the fibre infimum and supremum attains $\Delta/2$.

The exact formula is the supremum of the fibre radii when independent choices of centers are allowed, with infima interpreted carefully. It does not imply a continuous, measurable, computable, or physically admissible selector. The radius, diameter, and stability between different fibres are separate quantities.

For example, three vertices of an equilateral triangle of side one have diameter one and Euclidean enclosing radius $1/\sqrt3$. Half-diameter is a lower bound, not the exact radius in this target geometry.

## Minimal auxiliary memory

Let $X$ be nonempty and finite. Let $R$ be a legacy representation that must remain part of the autonomous state. Let $E^\#$ be the exact future equivalence preserving all future legacy values and tasks. If an auxiliary symbol can be initialized from the native state, then

$$|\mathcal A|_{\min}=\max_{z\in R(X)}\#\{E^\#\text{ classes contained in }R^{-1}(z)\}.$$

**Proof.** Distinct required classes inside one visible fibre must receive different auxiliary symbols. Conversely label those classes separately inside each fibre, reusing symbols in different visible fibres. The combined representation $(R,A)$ has kernel exactly $E^\#$, so its updates and tasks descend. This proves both the lower bound and its attainment.

Initialization is substantive. An auxiliary variable computed only from $R(x)$ cannot distinguish any pair that $R$ already identifies. Memory inferred from later observations is another architecture, with an observation alphabet and an explicit update rule.

For $X=\{0,1\}^2$, $f(a,b)=(b,b)$ and $R(a,b)=a$, a constant external task does not remove the need to retain $b$ if the autonomous state must continue to reproduce the legacy coordinate. Two auxiliary symbols are necessary and sufficient.

## Admissibility and compression

Let $A\subseteq X$ be the lawful state set. If only $R(x)$ is retained, the existential test that some lawful state has that code accepts $R(A)$. Pulling it back gives

$$A\subseteq R^{-1}(R(A)).$$

Equality holds exactly when $A$ is a union of $R$-fibres. The excess consists of unlawful states sharing a code with a lawful state. Thus an existentially admissible code is not a certificate that every state behind it is lawful.

For $X=\{0,1\}^2$, $A=\{(a,b):a=b\}$ and $R(a,b)=a$, every code has a lawful completion, but half the native states are unlawful. A universal admissibility test instead accepts only those codes whose entire fibre lies in $A$. These two tests express different quantifiers.

## Two exactification procedures need not commute

For a family of total operations $U$, write $I_U(E)$ for the largest $U$-stable equivalence contained in $E$. Stability includes all finite words in $U$. This is the predictive interior of $E$ in the inclusion order: it is monotone, contractive, and idempotent.

**Proposition.** Two such interiors need not commute, even on four states.

Take $X=\{0,1,2,3\}$, initial blocks $\{0,1\},\{2,3\}$, and the following action tables.

| State | $f$ | $g$ | Initial task |
|---:|---:|---:|---:|
| 0 | 2 | 0 | 0 |
| 1 | 3 | 1 | 0 |
| 2 | 2 | 0 | 1 |
| 3 | 3 | 2 | 1 |

The initial partition is already stable under $f$. Refinement under $g$ gives $\{0,1\},\{2\},\{3\}$. That partition is not stable under $f$, because $f(0)=2$ and $f(1)=3$. Consequently

$$I_g(I_f(E))=\{\{0,1\},\{2\},\{3\}\},\qquad
I_f(I_g(E))=\Delta_X.$$

Here the first equality uses partition notation for its corresponding equivalence. The mixed continuation $g\circ f$ distinguishes states 0 and 1. Auditing only the separately chosen order can miss a distinction required by an allowed mixed future.

**Repair theorem.** On a finite carrier, alternate the two interiors until no further split occurs. The terminal relation is $I_{U\cup V}(E)$.

**Proof.** Each step refines the previous relation. Every equivalence stable under both families and contained in $E$ remains below every iterate by monotonicity. The finite chain stabilizes. At a fixed point of the composition, contractiveness forces equality at both intermediate steps, so the terminal relation is fixed by each interior. It is therefore stable under every mixed word and contains every other such admissible relation. There are at most $|X|-|X/E|$ strict splits of the partition chain.

If the interiors commute, their composition is already idempotent and is fixed by each; one composed pass gives the joint interior. Commutation is a sufficient certificate that must be proved, not an automatic property of reduction.

## Propagating approximate defects

If an exact update is $L_k$-Lipschitz and its approximation has defect at most $\delta_k$ on every compared state, then

$$e_n\le e_0\prod_{j=1}^n L_j+
\sum_{k=1}^n\delta_k\prod_{j=k+1}^nL_j.$$

This follows by inserting the exact update of the approximate previous state and applying the triangle inequality at each step. A small one-step error alone supplies no uniform long-time bound when amplification grows. Rescaling an encoder can also make a code residual small while making its decoder proportionally ill-conditioned. All quantitative closure claims must specify the norm, relevant states, horizon, and decoder sensitivity.


# Continuous and smooth realization


## Positive continuous result

Suppose X is compact Hausdorff, all tasks have Hausdorff targets and are continuous, every m∈M is continuous, and R is continuous with Hausdorff target. Then E# in the exactification chapter is closed in X×X. The quotient Q=X/E# is compact Hausdorff, and the descended legacy map, tasks, and continuations are continuous.

**Proof.** Each kernel is the inverse image of a closed diagonal. Arbitrary intersections remain closed. For any closed A⊆X its saturation E#[A] is closed, being the projection of a compact closed subset of X×X. Distinct equivalence classes are disjoint compact sets, so choose disjoint open neighborhoods U,V containing them. The saturated open sets $X\setminus E^\#[X\setminus U]$ and $X\setminus E^\#[X\setminus V]$ still contain the respective classes and lie inside U,V. Their images separate the two quotient points, proving the quotient Hausdorff. The quotient is compact by continuity of q. A map out of Q is continuous exactly when its composite with q is continuous; apply this to every descended map. $\square$

A continuous representation with **kernel exactly E#** into ℝᵏ exists iff Q embeds in ℝᵏ. Indeed the induced map from compact Q into the Hausdorff target is a continuous bijection onto its image and hence an embedding. Conversely an embedding composed with q gives that representation. A finer representation can exist even when this exact quotient does not embed in the requested dimension.

For finitely many compact Hausdorff carriers, closed initial equivalences B_i, and total continuous finite-arity operations, the contextual construction has the same positive conclusion. A one-hole context is any finite composition of the operations with one variable input and all other inputs fixed as native constants; include the identity context. Put

\[
E_i=\bigcap_{C:X_i\to X_j}(C\times C)^{-1}B_j.
\]

Each E_i is closed. Inserting an operation into any context and replacing its input slots one at a time proves output E-equivalence whenever its inputs are E-equivalent. Conversely any congruence refining B preserves all these contexts and is therefore contained in E. This proves coarsestness directly. Finite products of the quotient maps are quotient maps here, since they are continuous surjections from compact spaces onto Hausdorff spaces. This supplies the continuity of descended Interactions. Arbitrary partial domains and relational/stochastic continuity require their own additional assumptions.

## Correct local smooth augmentation theorem

Let M be a smooth manifold and R:M→ℝᵖ a smooth legacy map. Let H# be the family of smooth scalar functions comprising the components of all declared future legacy values and tasks, including the present components of R. Write

\[
\mathscr W_\#(x)=\operatorname{span}\{dh_x:h\in H_\#\}.
\]

Suppose A:M→ℝᵏ is C¹, S=(R,A), and every required h has a **C¹ local factorization** $h=\bar h\circ S$ near the point x under discussion. Here $\bar h$ is C¹ on an open neighborhood of S(x) in ℝᵖ⁺ᵏ, and the factorization holds on a neighborhood of x mapped into that domain. Then

\[
\boxed{k\ge\dim\mathscr W_\#(x)-\operatorname{rank}dR_x.}
\]

**Proof.** The chain rule gives dh_x in the row space of dS_x for every h. Thus dim W#(x)≤rank dS_x≤rank dR_x+k. $\square$

If rank dR=r₀ and dim W#=r are constant in a neighborhood, this number r-r₀ is locally attainable with smooth A for the observable factorizations. Choose r₀ independent components of R at the point and extend their differentials to a basis of W# using r-r₀ functions from H#. They remain independent on a smaller neighborhood. Use the added functions as A. Constant-rank coordinates give connected local plaques on which every required h has zero vertical derivative, hence is constant. Each h consequently factors smoothly through the resulting rank-r local representation; its decoder extends to an ambient open neighborhood by ignoring the transverse coordinates in the constant-rank normal form. If the family is closed under the declared continuations, the same reasoning gives local descent of the represented continuations wherever the relevant local charts and domains apply. It does not establish one global chart or all-time global realization. The classical normal form used here is stated in [Loustau, *Smooth Manifolds*, Lecture 6](https://brice.loustau.eu/teaching/TUDarmstadt/Manifolds2020/Lecture6.pdf).

The decoder hypothesis matters. With identity dynamics, R(t)=t³ and task T(t)=t, exact set-level recovery uses the continuous decoder cube root, but at zero rank dR=0 while dT≠0. Thus one cannot infer this differential inequality from mere set-level factorization through an arbitrary singular smooth R.

## Global vertical-bundle restriction

Let ρ:Q→Z be a smooth submersion and V=ker dρ. Suppose a:Q→ℝᵏ is required to make (ρ,a) an immersion. Then da restricted to V is injective and defines a vector-bundle embedding

\[
V\hookrightarrow Q\times\mathbb R^k.
\]

Therefore k is at least the minimum trivial-bundle rank admitting such an embedding. This is a necessary bound, not a general attainment theorem. Mere smooth injectivity of (ρ,a) does not imply derivative injectivity, as t↦t³ shows.

The Möbius line bundle illustrates a separate global obstruction that already holds for continuous encoders. Present it as (θ,t)∼(θ+2π,-t), with ρ recording θ modulo 2π. If a scalar a is injective on each line fibre, the continuous nonzero difference a(θ,1)-a(θ,-1) must keep its sign along θ, yet the identification reverses that sign after 2π. Contradiction. Two components suffice:

\[
a(\theta,t)=\big(t\cos(\theta/2),t\sin(\theta/2)\big).
\]

This formula respects the identification and is injective with injective derivative along every fibre. Local dimension and global augmentation cost are different quantities.

## A coarsest smooth submersion need not exist

Use X=ℝ³ with coordinates (x,y,z), identity evolution, and receiver task

\[
T(x,y,z)=x^2+y^2.
\]

Allow surjective smooth submersions to finite-dimensional smooth manifolds, with task recovery. Two admissible encoders are

\[
R_1(x,y,z)=(x,y),
\]

\[
R_2(x,y,z)=(x\cos z-y\sin z,\;x\sin z+y\cos z).
\]

Both have rank two everywhere and connected fibres. Both recover T as the squared Euclidean norm and close exactly under identity dynamics.

**Theorem.** There is no admissible smooth submersion coarser than both R₁ and R₂. Consequently this admissible class has no coarsest exact reduction.

**Proof.** Suppose S:X→Q is coarser than both, so ker R_i⊆ker S. The R₁ condition makes S independent of z; write S(x,y,z)=s(x,y). Since

\[
R_2(x,y,z)=R_2(\operatorname{Rot}_z(x,y),0),
\]

the R₂ condition gives s(w)=s(Rot_z w) for every w∈ℝ² and real z. In particular s(w)=s(-w). In a smooth chart around s(0), differentiation at zero gives ds₀=-ds₀, hence ds₀=0. Independence of z gives dS=0 at every point of the z-axis.

A submersion with zero derivative must have zero-dimensional target. Since X is connected and S is surjective, that target would consist of one point, which cannot recover the nonconstant task T. Contradiction. $\square$

The set-level task quotient exists. The smooth scalar map T itself also exists and suffices, but has a critical point on the axis and is excluded by the submersion contract. Thus the result does not say that arbitrary smooth encoders fail to exist. It says that imposing regular smooth realization can destroy the existence of a coarsest admissible interface even though several valid interfaces exist.

This supplies a concrete negative answer to the unrestricted existence aspiration in open problem 6 in [LOG12] for the submersion class. BM must allow a family of admissible realizations, a changed realization contract, or a proved nonexistence outcome.

# The price of exact dynamic closure

## One problem, several mathematical requirements

Fix normalized real state coordinates. A ball in these coordinates represents a declared deterministic bound, not a probability distribution. Any application with different physical units must first specify its state and response metrics.

Let $X=\mathbb R^n$, let $\Phi_t:X\to X$ be a specified global evolution, and let

$$
\mathcal O_T:X\longrightarrow\mathcal H,
\qquad \mathcal H=L^2((0,T);\mathbb R^p),
$$

map an initial state to its requested output trajectory. The performance set is

$$
K=\{z\in\mathbb R^n:\|z\|_2\le1\}.
$$

A representation is an encoder $R:X\to\mathbb R^d$. A receiver uses a decoder $D:\mathbb R^d\to\mathcal H$. Its error is

$$
\mathcal E_T(R,D)
=\sup_{z\in K}\|\mathcal O_Tz-D(Rz)\|_{\mathcal H}.
$$

The decoder may return an entire trajectory and may use the declared model parameters and observation clock. It receives no hidden initial coordinates. It need not be continuous for any lower bound below; the explicit optimal decoders are continuous.

The **free** admissible class consists of continuous $R$ and arbitrary $D$. This measures coordinate compression of a response family. It does not require the encoded coordinates to evolve autonomously.

The **closed** class additionally requires, for some fixed $h>0$, a single-valued map $F:R(X)\to R(X)$ such that

$$
R\Phi_h=F R\qquad\text{on all of }X.
\tag{1}
$$

A semiconjugacy for the whole flow is sufficient but stronger than needed. No regularity of $F$ is needed for the two-state obstruction. Because (1) holds globally, it can be iterated. This global quantifier is essential.

Define $E^{\mathrm{free}}_d$ and $E^{\mathrm{closed}}_d$ as the infima of $\mathcal E_T$ over their respective classes. The closed class is nonempty: a constant encoder is always possible. A useful response approximation may nevertheless require more coordinates.

## What the comparison does and does not demand

The closed problem asks for an autonomous *coordinate* and a trajectory decoder. It permits more decoders than the stricter model-reduction convention $\widehat y(t)=g(\overline\Phi_t(Rz))$ with a fixed instantaneous readout $g$. Consequently, our lower bound also applies to that stricter convention. The stated sharp upper bound uses an explicitly time-dependent trajectory decoder, whose clock is part of the receiver context.

Likewise, the encoder is allowed access to the initial full state. This makes the dimension benchmark optimistic. A sensor that initially measures only $x$ cannot automatically compute an encoder involving $v$. The source supplement [C11] separately treats noisy-trajectory recovery; the distinction between ideal initialization and measured initialization remains essential.

## BM interpretation without changing the mathematics

| Native ingredient | Role in this BM problem |
|:--|:--|
| Linear dynamics and its exact flow | Evolution Branch |
| Initial-state ball and $L^2$ output norm | Admissibility and comparison data |
| Continuous map to $\mathbb R^d$ | Representation Branch |
| Factorization (1) | Exact Dynamic Closure obligation |
| Whole observed trajectory | GURF receiver task |
| Infimum error in a specified class | Derived Leaf |
| Proof plus hypotheses accepted for reuse | Receiver-relative Root |

The Branch names supply no additional axiom. The result comes from requiring these native conditions simultaneously.

## BM DC PRICE 01 continuous scalar obstruction

## Statement

Fix $T>0$, $h>0$, and $\varepsilon\ne0$. On $\mathbb R^2$ take

$$
\Phi_t(x,v)=(x+\varepsilon tv,v),
\qquad (\mathcal O_T(x,v))(t)=x+\varepsilon tv.
$$

For every continuous $R:\mathbb R^2\to\mathbb R$ satisfying (1):

1. $R(x,0)$ is constant for all $x\in\mathbb R$.
2. Every trajectory decoder satisfies $\mathcal E_T(R,D)\ge\sqrt T$.
3. Equality is attainable, so $E^{\mathrm{closed}}_1=\sqrt T$.

At $\varepsilon=0$, instead, $E^{\mathrm{closed}}_1=0$.

## Proof of the fixed-line collapse

Write

$$
r(x)=R(x,0),\qquad J=r(\mathbb R).
$$

The points $(x,0)$ are fixed by $\Phi_h$. Equation (1) therefore gives

$$
F(r(x))=r(x).
$$

Every point in $J$ is fixed by $F$. Continuity of $r$ and connectedness of $\mathbb R$ imply that $J$ is an interval.

Suppose $r$ is nonconstant. Then $J$ has nonempty interior. Choose $a$ such that $r(a)$ is an interior point of $J$. By continuity of $R$, for all sufficiently small $v$,

$$
R(a,v)\in J.
\tag{2}
$$

Fix any $b\in\mathbb R$ and, for positive integers $k$, set

$$
v_k=\frac{b-a}{k\varepsilon h}.
$$

Then $v_k\to0$ and

$$
\Phi_h^k(a,v_k)=(b,v_k).
$$

For sufficiently large $k$, (2) makes $R(a,v_k)$ a fixed point of $F$. Iterating (1) yields

$$
R(b,v_k)=F^k(R(a,v_k))=R(a,v_k).
$$

Take $k\to\infty$. Continuity gives $r(b)=r(a)$. Since $b$ was arbitrary, $r$ is constant, contradicting the supposition. Thus $R$ must collapse the entire fixed line. $\square$

This argument uses neither a linear encoder nor differentiability nor a continuous reduced map. The fact that the code space is the real line is essential: a nonconstant continuous image of the fixed line contains an interval of fixed codes.

## Proof of the sharp response error

The two initial states $(1,0)$ and $(-1,0)$ lie in $K$ and share a code. Their output trajectories are the constant functions $+1$ and $-1$. Write $q$ for the decoder's common output. The triangle inequality gives

$$
2\sqrt T=\|1-(-1)\|_{L^2}
\le \|1-q\|_{L^2}+\|-1-q\|_{L^2}.
$$

At least one of the two errors is at least $\sqrt T$.

For attainability, take

$$
R(x,v)=v,\qquad F(v)=v,\qquad D(v)(t)=\varepsilon tv.
$$

The coordinate closes exactly for all times. The response error is the constant function $x$, so

$$
\mathcal E_T(R,D)=\sup_{x^2+v^2\le1}|x|\sqrt T=\sqrt T.
$$

For $\varepsilon=0$, choose $R(x,v)=x$, $F(x)=x$, and $D(x)(t)=x$ to obtain zero error. This proves every assertion. $\square$

## Why the result matters

The failure concerns a constraint on the *retained coordinate*. For nonzero coupling, continuity and exact global autonomous evolution force it to identify stationary states that the receiver distinguishes by an order-one amount. A decoder cannot repair that identification using only the code. The result is stronger than finding one bad linear projection: it excludes every continuous scalar encoder in the declared class.

The native flow is invertible, with inverse $\Phi_{-t}$. No distinction has been physically annihilated by the underlying dynamics. The loss occurs in the allowed representation.

## The unrestricted optimum and its exact price

## A classical dimension bound, with proof

Let $O:\mathbb R^n\to\mathcal H$ be linear, where $\mathcal H$ is a real Hilbert space. Let its singular values, including zeros, be

$$
\sigma_1\ge\cdots\ge\sigma_n\ge0.
$$

For $0\le d<n$, continuous encoders into $\mathbb R^d$ and arbitrary decoders satisfy

$$
\inf_{R,D}\sup_{\|z\|\le1}\|Oz-D(Rz)\|
=\sigma_{d+1}.
\tag{3}
$$

**Upper bound.** Encode the first $d$ coordinates in a right singular-vector basis and decode with their corresponding response vectors. The residual operator has norm $\sigma_{d+1}$.

**Lower bound.** Restrict $R$ to the unit sphere in the span of the first $d+1$ right singular vectors. This is a sphere $S^d$. The classical Borsuk-Ulam theorem supplies antipodal points $z,-z$ with the same code. Their output distance is $2\|Oz\|\ge2\sigma_{d+1}$. The common decoded output must incur error at least $\sigma_{d+1}$ on one point. For $d=0$, this is simply the two-point triangle inequality. $\square$

The topological input is a classical theorem, not a new BM axiom. Equation (3) is a Hilbert-ellipsoid width fact. It proves that allowing continuous nonlinear encoders does not improve this particular worst-case benchmark. It makes no such claim for arbitrary nonlinear response families or data restricted to a smaller manifold.

## Evaluation for the shear

For $z=(x,v)$, direct integration gives

$$
\|\mathcal O_Tz\|_{L^2}^2
=z^\top Wz,\qquad
W=\begin{pmatrix}
T&\varepsilon T^2/2\\
\varepsilon T^2/2&\varepsilon^2T^3/3
\end{pmatrix}.
$$

Put $s=\varepsilon T$. The two eigenvalues are

$$
\lambda_\pm=\frac T2
\left[1+\frac{s^2}{3}
\ \pm\sqrt{\left(1-\frac{s^2}{3}\right)^2+s^2}\right].
\tag{4}
$$

Thus $E^{\mathrm{free}}_1=\sqrt{\lambda_-}$. For small $s$, use the determinant identity

$$
\lambda_+\lambda_-=\frac{T^2s^2}{12},
\qquad \lambda_+/T\to1,
$$

to obtain

$$
E^{\mathrm{free}}_1
\sim\frac{\sqrt T\,|s|}{\sqrt{12}}.
$$

For numerical evaluation, $\lambda_-=T^2s^2/(12\lambda_+)$ avoids subtracting nearly equal quantities in (4).

## Absolute and relative closure price

For $\varepsilon\ne0$, define

$$
\Gamma_1=E^{\mathrm{closed}}_1-E^{\mathrm{free}}_1,
\qquad
\Pi_1=\frac{E^{\mathrm{closed}}_1}{E^{\mathrm{free}}_1}.
$$

These are errors, not squared errors. Their limits are

$$
\Gamma_1\longrightarrow\sqrt T,
\qquad
\Pi_1\sim\frac{\sqrt{12}}{|\varepsilon T|}.
\tag{5}
$$

For $T=1$:

| Coupling $|\varepsilon|$ | Free scalar error | Closed scalar error | Relative price |
|--:|--:|--:|--:|
| 1 | 0.256400964 | 1 | 3.900141 |
| 0.1 | 0.028831467 | 1 | 34.684326 |
| 0.01 | 0.002886715 | 1 | 346.414492 |
| 0.001 | 0.000288675 | 1 | 3464.102048 |

The exact formulas prove the result; these decimal values illustrate it.

![Two costs of representation constraints. Left shows the shear formulas; right shows the W35 construction.](figures/closure_and_fragmentation.png){width=95%}

# A hierarchy for longer interaction chains

## Exact response family

For $n\ge2$, consider the declared linear chain

$$
\dot x_i=\varepsilon x_{i+1}\ (i<n),\qquad
\dot x_n=0,\qquad y=x_1.
\tag{6}
$$

Its response map is

$$
(O_{n,T}z)(t)
=\sum_{k=0}^{n-1}\frac{(\varepsilon t)^k}{k!}z_{k+1}.
\tag{7}
$$

Let $\sigma_j^{(n)}$ be its singular values in the Euclidean state and $L^2$ response norms. For every $\varepsilon\ne0$, (7) is injective: a polynomial vanishing on an interval has all coefficients zero. Hence exact continuous trajectory encoding requires $n$ real coordinates, by (3).

This is a coordinate-dimension statement. It does not equate one real coordinate with one bit, and it requires continuity of the encoder.

## Classification of exact closed linear encoders

Assume $\varepsilon\ne0$. Let $N$ have ones just above its diagonal, so the state generator is $\varepsilon N$. A rank-$d$ linear encoder $R$ closes under the continuous flow precisely when

$$
RN=BR
$$

for some matrix $B$. This is invariance of the row space of $R$ under right multiplication by $N$.

For $1\le d<n$, the only invariant $d$-dimensional row space is

$$
\operatorname{span}\{e_{n-d+1}^{\top},\ldots,e_n^{\top}\}.
\tag{8}
$$

**Proof.** In a nonzero invariant row space $V$, take the smallest coordinate index $j$ that is nonzero in any member, and a vector $w$ whose $j$th entry is nonzero. The vectors $w,wN,\ldots,wN^{n-j}$ have distinct first nonzero positions and form a triangular basis for the entire coordinate suffix from $j$ through $n$. Invariance puts this suffix in $V$. The definition of $j$ puts $V$ inside the same suffix. Therefore they are equal. Its dimension fixes $j=n-d+1$. $\square$

The same conclusion follows if a linear encoder is required to close only under one fixed step $h>0$. Invariance under $e^{\varepsilon hN}$ implies invariance under the finite polynomial

$$
N=\frac{1}{\varepsilon h}\log(e^{\varepsilon hN}),
$$

where the nilpotent logarithm is a finite sum in $e^{\varepsilon hN}-I$.

## Sharp linear closure price

By (8), a closed linear encoder retains an invertible reparameterization of the last $d$ initial coordinates. Its kernel consists of the first $n-d$ coordinates. Thus, allowing arbitrary trajectory decoders,

$$
E^{\mathrm{closed,lin}}_d
=\sigma_1^{(n-d)},\qquad
E^{\mathrm{free}}_d=\sigma_{d+1}^{(n)}.
\tag{9}
$$

For the first equality, an antipodal pair in the encoder kernel gives the lower bound $\|O_{n,T}|_{\ker R}\|$. A decoder that reconstructs the retained coordinates' contribution in (7) attains it. The omitted polynomial is exactly the $(n-d)$-state response family. The second equality is (3).

For general $n,d$, the first formula is proved **only for linear encoders**. The continuous nonlinear extension is proved above for $n=2,d=1$. The next chapter gives the stronger current-output and omitted-coordinate endpoint results from [R12]. The 20 October continuation resolves n=3,d=1 for all continuous codes and shows that n=4,d=1 admits strict nonlinear improvement over the linear optimum. The other exact interior optima remain open.

## Sharp small-coupling constants

For each fixed $n$ and $0\le k<n$,

$$
\sigma_{k+1}^{(n)}
\sim \sqrt T\,a_k|s|^k,
\qquad
a_k=\frac{1}{k!\sqrt{2k+1}\binom{2k}{k}},
\qquad s=\varepsilon T\to0.
\tag{10}
$$

Consequently, for $1\le d<n$,

$$
\frac{E^{\mathrm{closed,lin}}_d}{E^{\mathrm{free}}_d}
\sim\frac{d!\sqrt{2d+1}\binom{2d}{d}}{|\varepsilon T|^d}.
\tag{11}
$$

The price can therefore diverge at every depth $d$, even though the native equations remain globally linear and exactly solvable.

## Proof of the spectral constants

Let $P_j$ be the usual Legendre polynomial and use the orthonormal response basis

$$
\phi_j(t)=\sqrt{\frac{2j+1}{T}}P_j(2t/T-1).
$$

Orthogonality and Rodrigues' formula give, for integers $k\ge j$,

$$
\int_0^1 u^kP_j(2u-1)\,du
=\frac{(k!)^2}{(k-j)!(k+j+1)!},
\tag{12}
$$

and zero for $k<j$. To verify (12), use

$$
P_j(2u-1)=\frac1{j!}\frac{d^j}{du^j}[u^j(u-1)^j].
$$

Integrating by parts $j$ times removes all boundary terms. The remaining beta integral is $\int_0^1u^k(1-u)^jdu=k!j!/(k+j+1)!$, which gives (12).

Therefore the matrix of (7) in this orthonormal basis is upper triangular:

$$
H_{jk}=\sqrt T\,s^k
\frac{\sqrt{2j+1}\,k!}{(k-j)!(k+j+1)!}
\quad(0\le j\le k<n).
\tag{13}
$$

Its diagonal is $\sqrt T\,a_ks^k$. We now justify why those diagonal coefficients are also the leading singular-value coefficients, rather than assuming so for a general triangular matrix.

In the $r$th exterior power of $H$, the entries are its $r\times r$ minors. The smallest possible power of $s$ comes from columns $0,\ldots,r-1$, with exponent $r(r-1)/2$. Upper triangularity makes the sole nonzero minor at that order the first $r$ rows as well. Its leading coefficient is

$$
T^{r/2}\prod_{k=0}^{r-1}a_k.
$$

After division by $|s|^{r(r-1)/2}$, the exterior-power matrix converges, up to a harmless sign, to a matrix with one nonzero entry. Its operator norm therefore converges to that coefficient. The operator norm of an exterior power is the product of the largest $r$ singular values. Divide the product asymptotic for $r$ by the one for $r-1$ to obtain (10). Equation (11) follows from (9). $\square$



# Continuous Jordan obstruction


Consider the n-state chain, with n≥2,

\[
\dot x_i=\varepsilon x_{i+1}\;(i<n),\quad
\dot x_n=0,\quad y=x_1,
\qquad \varepsilon\ne0.
\]

Let Φ=e^{εhN}, h>0, where N has ones on the superdiagonal, and let O=e₁ᵀ denote the current output. The performance set is the Euclidean unit ball. Require a globally continuous encoder R:ℝⁿ→ℝᵈ and a single-valued update F satisfying RΦ=FR on all of ℝⁿ. Decoder regularity is unrestricted.

## General continuation-width lemma

For a finite S⊂{0,1,2,…} containing zero and a linear subspace V of dimension d+1, let

\[
\|x\|_S=\max_{k\in S}\|\Phi^k x\|_2,
\quad
\beta(V,S)=\inf_{x\in V\setminus\{0\}}
\frac{\max_{k\in S}|O\Phi^kx|}{\|x\|_S}.
\]

Every such code has worst-case current-output error at least β(V,S).

**Proof.** The unit sphere of this norm on V is antipodally homeomorphic to Sᵈ. The Borsuk-Ulam theorem supplies x and -x on it with R(x)=R(-x). Closure propagates this equality to Φᵏx and -Φᵏx for every k∈S. Both states lie in the performance ball. Their outputs are opposite, so a common decoded value has error at least |OΦᵏx| at one of them. Maximize over k, then use the infimum defining β. $\square$

This uses the same classical topological input as the closure supplement [C11]. Continuity of R and exact global iteration are essential. A finite performance ball is not being asserted to be invariant.

## Explicit Jordan interpolation bound

Choose S_M={0,M,2M,…,(n-1)M}, where M is a positive integer, and put a=εMh. Let $\ell_j(s)$ be the Lagrange polynomials at the nodes 0,…,n-1. Define finite constants

\[
D_r=\max_{0\le i<n}\sum_{j=0}^{n-1}|\ell_j^{(r)}(i)|,
\qquad
b_M^2=\sum_{r=1}^{n-1}\frac{D_r^2}{|a|^{2r}}.
\]

Then, for every nonzero subspace V,

\[
\boxed{\beta(V,S_M)\ge(1+b_M^2)^{-1/2}\longrightarrow1.}
\]

**Proof.** Write P(s)=x_1(Mhs), a polynomial of degree at most n-1, and A=max_j|P(j)|. Interpolation gives

\[
|P^{(r)}(i)|\le D_rA.
\]

The chain identity is P^{(r)}(i)=a^r x_{r+1}(iMh). Thus every sampled state's tail has norm at most A b_M, and its first coordinate has magnitude at most A. Consequently

\[
\max_i\|\Phi^{iM}x\|_2\le A\sqrt{1+b_M^2}.
\]

For nonzero x, A>0 because n distinct zeros would make P identically zero and all state coordinates zero. Dividing proves the bound. $\square$

For |a|≥1, one may replace b_M² by C_n/a² with C_n=Σ_rD_r². For n=3, the nodal constants are D_1=D_2=4. The proof deliberately treats the maximum-output node and maximum-state-norm node separately; they need not coincide.

## Consequences and the remaining exact optimum

For every 0≤d<n,

\[
\boxed{E_{\mathrm{current},d}^{\mathrm{closed,cont}}=1.}
\]

The lower bound follows by taking M→∞. A constant code and zero current-output decoder give the upper bound.

For the whole trajectory on [0,T], with 0<T<∞ and 1≤p≤∞,

\[
\boxed{E_{p,T,d}^{\mathrm{closed,cont}}\ge\|1\|_{L^p(0,T)}.}
\]

To prove this, use the antipodal pair from the norm sphere above and a sampled state z whose first-coordinate magnitude equals A. Its tail norm is at most A b_M. If K_{p,T} is the finite operator norm taking the tail initial coordinates to their output polynomial in Lᵖ, the triangle inequality gives

\[
\|O_Tz\|_p\ge A(\|1\|_p-K_{p,T}b_M)
\ge\frac{\|1\|_p-K_{p,T}b_M}{\sqrt{1+b_M^2}}
\]

for sufficiently large M, when the numerator is nonnegative. A common decoder for z and -z incurs at least this error. Let M→∞.

When d=n-1, retaining (x₂,…,x_n) closes exactly and reconstructs every trajectory contribution except the constant x₁. Therefore

\[
\boxed{E_{p,T,n-1}^{\mathrm{closed,cont}}=\|1\|_p}
\]

for every nonzero ε. This includes √T for p=2 and 1 for p=∞. For 1≤d<n-1, this lower bound does **not** determine the complete finite-ε trajectory optimum. The exact linear answer from the closure supplement [C11] remains an upper bound for the nonlinear class. Historical novelty of this obstruction has not been established. The 20 October continuation proves the exact continuous n=3,d=1 value in BM20-J3 and gives a nonlinear four-state improvement in BM20-J4.

# Conditioned linear repair


This section proves a precise finite-dimensional version of the linear repair question in [LOG12]. It concerns a linear representation with a linear autonomous update and an unrestricted trajectory decoder, as in C.

Let A be a real n×n matrix, O:ℝⁿ→H a linear map into a real Hilbert space, and W=O*O, with eigenvalues λ₁≥…≥λ_n≥0. Measure worst-case response error on ||x||₂≤1. Let U be a chosen leading d-dimensional spectral subspace, 0<d<n. In U⊕U⊥ write B=Aᵀ as

\[
B=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix}.
\]

For Z:U→U⊥ define the Sylvester operator L(Z)=B₂₂Z-ZB₁₁. Suppose it is invertible and, for some s>0,

\[
\|L^{-1}\|_{F\to F}\le1/s,\quad
\Delta=\|B_{21}\|_F,\quad b=\|B_{12}\|_2,
\quad 4b\Delta/s^2<1.
\]

Put r=2Δ/s, including r=0 when Δ=0. In that case U is already invariant and Z=0 supplies the theorem.

**Theorem.** There is a B-invariant graph subspace U_Z={(u,Zu):u∈U}, with ||Z||_F≤r. A rank-d encoder with rowspace U_Z supplies the following bounds on the optimum response approximation errors:

\[
\boxed{
E_\mathrm{free}^2=\lambda_{d+1}
\le E_\mathrm{closed}^2
\le\lambda_{d+1}
+(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
}
\]

E_closed denotes the optimum in the exact closed linear class; the constructed graph supplies its upper bound.

**Proof of invariant repair.** Graph invariance is equivalent to

\[
B_{21}+B_{22}Z=ZB_{11}+ZB_{12}Z,
\]

or Z=L^-1(-B₂₁+ZB₁₂Z). On the closed Frobenius ball ||Z||_F≤r this map has norm at most Δ/s+br²/s≤r. Its Lipschitz constant is at most 2br/s=4bΔ/s²<1, using

ZB₁₂Z-YB₁₂Y=(Z-Y)B₁₂Z+YB₁₂(Z-Y).

The contraction theorem supplies a unique fixed point in this ball. B-invariance of U_Z is equivalent to an exactly closing rank-d row representation for A. This works for a discrete linear update A, or for generator A and its whole flow.

**Proof of response bound.** In the chosen decomposition W is block diagonal. The orthogonal complement of U_Z consists of (-Zᵀv,v). Its W-Rayleigh quotient is at most

\[
\frac{\lambda_1\|Z^\top v\|^2+
\lambda_{d+1}\|v\|^2}{\|Z^\top v\|^2+\|v\|^2}
\le\lambda_{d+1}+
(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
\]

Encoding orthogonal coordinates in U_Z and decoding their O-contribution leaves exactly this complementary operator norm as the squared error. The free rank-d optimum is λ_{d+1}, so it is also a lower bound on the constrained optimum. $\square$

Thus the **squared-error surcharge** is O(Δ²/s²). If E_free>0, the ordinary surcharge is at most the displayed squared surcharge divided by 2E_free. If E_free=0, the available ordinary-error estimate is O(Δ/s).

This is a conditioned invariant-subspace result using classical Sylvester, Riccati, and contraction methods. It does not prove a corresponding general nonlinear repair theorem, does not certify a minimum perturbation, and does not establish historical novelty. Linear observable-preserving reduction already has established methods, including [Ovchinnikov et al., *CLUE*](https://arxiv.org/abs/2004.11961).

# Resonance and regularity

For $\dot x=-ax+\varepsilon v^m$, $\dot v=-bv$, with integer $m\ge1$, the nonresonant coordinate

$$q=x+\frac{\varepsilon}{mb-a}v^m\qquad(a\ne mb)$$

satisfies $\dot q=-aq$. At resonance $a=mb$ with $b\ne0$, instead take

$$q=x+\frac{\varepsilon}{b}v^m\log|v|,$$

extending $v^m\log|v|$ by zero at $v=0$. Differentiation away from zero gives $\dot q=-aq$; the flow identity extends to zero by continuity. For nonzero $\varepsilon$ this coordinate is $C^{m-1}$ but not $C^m$ at zero. For $m=1$ it is not locally Lipschitz there. This is an explicit price in regularity, not a universal impossibility of nonlinear closure. The resonance formula is undefined at $b=0$ and must not be used in that case.

The coordinate need not recover the whole native state or every original output. Those tasks require their own error or factorization analysis. Likewise invariance under a sampled linear map need not imply invariance under its generator: a rotation sampled after a complete period is the identity. The nilpotent Jordan-chain case is special because its generator is a finite polynomial in the sampled map minus the identity.


# The heat cascade in the correct norm


Use positive modes indexed by n≥1 and the Hilbert state space $\ell^2$×$\ell^2$:

\[
\dot u_n=-n^2u_n+\varepsilon v_n,
\qquad
\dot v_n=-n^2v_n.
\]

These are specified positive heat modes; a zero mode is excluded. Its presence would require a separate analysis. The mild flow is

\[
v_n(t)=e^{-n^2t}v_n(0),\quad
u_n(t)=e^{-n^2t}\big(u_n(0)+\varepsilon t v_n(0)\big).
\]

For δ>0 define the common-δ smooth encoding

\[
(Q_\delta(u,v))_n
=u_n+\frac{\varepsilon}{2n^2}v_n\log(v_n^2+\delta^2),
\]

and reduced semigroup (S_tq)_n=e^{-n²t}q_n.

## The rejected instantaneous estimate stays rejected

Where the generator is defined, the residual is

\[
r_n=\varepsilon v_n\frac{\delta^2}{v_n^2+\delta^2}.
\]

Per mode |r_n|≤|ε|δ/2. For N modes the resulting estimate is |ε|δ√N/2, not a bound uniform in N.

More strongly,

\[
\boxed{\sup_{\|v\|_2\le1}\|r(v)\|_2=|\varepsilon|\quad(\delta>0).}
\]

The upper bound follows from |r_n|≤|εv_n|. For the lower bound, put v_n=N^-1/2 on N coordinates and zero elsewhere. The residual norm is |ε|δ²/(N^-1+δ²), which tends to |ε| as N→∞. These are finite-support vectors, so they also lie in the generator domain. Uniformly small generator defect is impossible for this common-δ family on the unit ball.

## Uniform evolved-coordinate estimate

**Theorem.** For every δ>0,

\[
\boxed{
\sup_{t\ge0}\sup_{(u,v)\in\ell^2\times\ell^2}
\|Q_\delta(\Phi_t(u,v))-S_tQ_\delta(u,v)\|_2
\le\frac{|\varepsilon|\delta\pi^2}{2\sqrt{90}}.
}
\]

The same bound holds for every finite truncation, with no factor depending on N.

**Proof.** For each mode, variation of constants gives the mismatch

\[
d_n(t)=\int_0^t e^{-n^2(t-s)}r_n(v(s))\,ds.
\]

The per-mode residual bound yields

\[
|d_n(t)|\le\frac{|\varepsilon|\delta}{2n^2}(1-e^{-n^2t}).
\]

Squaring, summing, and using Σ_{n≥1}n^-4=π⁴/90 proves the claim. The summable majorant also justifies the passage from finite truncations to $\ell^2$. The coordinate formulas establish the identity for mild trajectories without assuming a derivative at t=0 for arbitrary $\ell^2$ data. $\square$

For fixed δ, Q_δ is a C∞ map $\ell^2$×$\ell^2$→$\ell^2$. Set f_δ(s)=s log(s²+δ²). Since f_δ(0)=0 and f_δ′ is bounded on bounded scalar intervals, the coordinate map sends bounded $\ell^2$ sets to $\ell^2$. Its kth derivative for k≥1 is coordinatewise multiplication of f_δ^(k)(v_n) with the k perturbation coordinates. Bounded scalar derivatives and ||h||∞≤||h||₂ bound the resulting $\ell^2$ norm by a constant times the product of the perturbations' $\ell^2$ norms. Scalar Taylor remainders give the Fréchet derivative and its local continuity at each order. Multiplication by 1/n² is bounded. Constants may depend on δ and the bounded set.

Define v log|v|=0 at v=0 and

\[
(Q_0(u,v))_n=u_n+\frac{\varepsilon}{n^2}v_n\log|v_n|.
\]

The elementary inequality log(1+t²)≤2t for t≥0 gives

\[
\sup_{(u,v)\in\ell^2\times\ell^2}
\|Q_\delta(u,v)-Q_0(u,v)\|_2
\le\frac{|\varepsilon|\delta\pi^2}{\sqrt{90}}
\]

uniformly on the whole state space. Hence Q₀ is a well-defined continuous map as the uniform limit of Q_δ. Direct substitution gives Q₀Φ_t=S_tQ₀. For ε≠0, it is not locally Lipschitz at the origin, already on its first v-coordinate.

This supplies a continuous exact representation and smooth approximations with uniform evolved-coordinate error. It does not make the smooth approximations exact, and it does not recover the full u,v state from the reduced code. A receiver asking for u adds the representation/reconstruction error. The constant above is a proved upper bound, not a claimed sharp optimum.

The argument extends to positive decay rates λ_n when Σλ_n^-2<∞, replacing π²/√90 by $(\sum_n\lambda_n^{-2})^{1/2}$. It is a result for this specified diagonal cascade, not all nonlinear PDEs.

# Uniform quantitative contracts

## Robust width and update amplification

Let the encoder be continuous as in the Jordan chapter, and let η be its worst-case current-output decoding error on the performance set. For initially merged native states, a one-step code residual ||RΦz-F(Rz)|| at most δ and an L_F-Lipschitz reduced update yield a uniform bound on their code separation after k steps:

\[
\alpha_k\le2\delta G_k(L_F),\qquad
G_k(L_F)=\sum_{j=0}^{k-1}L_F^j.
\]

Write Σ_{V,S}={x∈V:||x||_S=1}, with the orbit norm from the Jordan chapter. Here α_k is the supremum of ||RΦᵏx-RΦᵏ(-x)|| over initially merged antipodal pairs on that sphere, so α₀=0. The displayed estimate requires the residual bound on every intermediate state used in the comparison, not just at the sampled endpoints. If the decoder has modulus ω_D on the codes used, the continuation-width proof gives

\[
\eta\ge\inf_{x\in\Sigma_{V,S}}
\max_{k\in S}\left(
|O\Phi^kx|-\tfrac12\omega_D(\alpha_k)
\right).
\]

Consider a family indexed by δ→0. Suppose sampling sets S_M have max S_M≤cM and a uniformly available orbit-width bound β(V,S_M)≥1-C/M². Suppose also ω_D(t)≤L_Dt^γ, with a fixed 0<γ≤1. The constants c, C, and L_D, the domains needed for the comparison, and the availability of these estimates must be uniform in both M and δ. With nonexpansive reduced updates L_F≤1, α_k≤2cMδ at the sampled times. Consequently η≥1-C/M²-(L_D/2)(2cMδ)^γ. Minimizing C/M²+C′(Mδ)^γ over positive integers M gives

\[
(1-\eta)_+=O\big(\delta^{2\gamma/(2+\gamma)}\big).
\]

The positive-part notation prevents interpreting the statement as an upper bound on η. If L_F is bounded by a fixed constant strictly below one, uniformly in δ, bounded G_k instead gives (1-η)_+=O(δ^γ). For a fixed L_F>1 and the same uniform hypotheses, this argument gives an O((log(1/δ))^-2) bound by choosing M proportional to log(1/δ), with a sufficiently small proportionality constant. These are rates furnished by this argument, not sharpness claims. The power rate in [LOG12] section 13 requires a nonexpansive or comparable polynomial-growth hypothesis and control of decoder sensitivity; it does not follow for arbitrary L_F or δ-dependent decoder constants.

**Why uniform decoder control is necessary.** On the unit disk in ℝ² take the shear Φ(x,v)=(x+v,v), output O(x,v)=x, and, for δ>0,

\[
R_\delta(x,v)=\delta x,\qquad
F(q)=q,\qquad D_\delta(q)=q/\delta.
\]

The current-output error is η=0, while the one-step code residual is |δv|≤δ and L_F=1. For S_M={0,M}, the width satisfies β(V,S_M)≥(1+4/M²)^-1/2≥1-2/M², with V=ℝ². Indeed |v|≤2 max(|x|,|x+Mv|)/M. Intermediate shear states are convex combinations of the endpoint states, so normalized orbit-sphere pairs remain in the disk at every intermediate time. Thus the domain condition holds too. Nevertheless (1-η)_+=1 for every δ. The missing uniform hypothesis is exactly L_D: here L_D=1/δ. Code rescaling alone cannot imply the stated robust-error rate.

## Finite distinguishability depth

For a total deterministic map on N states, let E₀ be the current task equivalence with p blocks, and E_{h+1}=E_h∩(Φ×Φ)^-1E_h. Then

\[
\boxed{E_{N-p}=E_\infty.}
\]

If a round is not strict, it is already a fixed point and no later split occurs. Every strict round adds at least one block, and there are at most N-p such additions. Thus any pair ever distinguished by the task is distinguished by time N-p. This strengthens the true but loose N²-1 bound in [LOG12] section 22. The bound is attained for p=2 by the chain Φ(i)=max(i-1,0), with a task distinguishing state 0 from all others: states N-1 and N-2 first separate at time N-2.

# Representation constrained by receiver requirements

## A quantitative BM problem

The representation Branch selects a reconstruction $M$ of rank at most $d$. The task Branch specifies positive-definite $S\in\mathbb R^{n\times n}$; the repair or receiver Branch specifies positive-definite $K$. These can arise from a deterministic weighted family of task vectors, $S=\sum_j w_jx_jx_j^\top$ with nonnegative declared weights, and a positive quadratic receiver cost. No probability distribution is required for this interpretation. Positive definiteness, rather than a name for either matrix, is the hypothesis used below.

The objective is

$$J(M)=\operatorname{tr}\bigl[K(I-M)S(I-M)^\top\bigr]
=\|K^{1/2}(I-M)S^{1/2}\|_F^2.$$

A stricter receiver may require a Euclidean orthogonal projector $P=P^\top=P^2$ of rank $d$. The admissible set changes, so the optimum may change. Denote the unrestricted and projector optima by $J_{d,\mathrm{lin}}^*$ and $J_{d,\mathrm{proj}}^*$. Write

$$H=S^{1/2}KS^{1/2},\qquad \theta_1\ge\cdots\ge\theta_n>0.$$

## LEV 013 Weighted reconstruction theorem

For $0\le d\le n$,

$$J_{d,\mathrm{lin}}^*=\sum_{j>d}\theta_j.$$

For $0<d<n$, all minimizers have the form

$$M=S^{1/2}\Pi S^{-1/2},$$

where $\Pi$ is an orthogonal rank-$d$ projector onto a maximizing spectral subspace of $H$: it contains every eigenspace strictly above $\theta_d$, contains no eigenspace strictly below $\theta_d$, and selects the remaining needed dimension within the eigenspace at $\theta_d$. If $\theta_d>\theta_{d+1}$, this projector, and hence $M$, is unique.

### Complete proof

Set $A=K^{1/2}S^{1/2}$ and $N=K^{1/2}MS^{1/2}$. The invertible changes of variable preserve rank and transform the problem into minimizing $\|A-N\|_F^2$. Let $\Pi$ project onto the row space of $N$, of dimension $k\le d$. Since $N=N\Pi$, the row-space components are Frobenius orthogonal, giving

$$\|A-N\|_F^2=\|A(I-\Pi)\|_F^2+\|A\Pi-N\|_F^2
\ge\operatorname{tr}H-\operatorname{tr}(\Pi H).$$

In an eigenbasis $v_j$ of $H$, put $p_j=v_j^\top\Pi v_j$. Orthogonal projection gives $0\le p_j\le1$ and $\sum_jp_j=k$. Moving weight from a smaller eigenvalue to a larger one cannot decrease $\sum_j\theta_jp_j$, hence $\operatorname{tr}(\Pi H)\le\sum_{j\le k}\theta_j\le\sum_{j\le d}\theta_j$. The bound is attained by taking $N=A\Pi$ with a maximizing rank-$d$ spectral projector.

Because all $\theta_j>0$, an optimizer cannot have $k<d$ (except the trivial $d=0$ case). Equality requires both $N=A\Pi$ and maximal spectral trace. To characterize equality, let $\lambda=\theta_d$ and let $a$ count eigenvalues strictly above $\lambda$. The deficit equals

$$\sum_{j\le d}\theta_j-\sum_j\theta_jp_j
=\sum_{\theta_j>\lambda}(\theta_j-\lambda)(1-p_j)
+\sum_{\theta_j<\lambda}(\lambda-\theta_j)p_j.$$

Thus $p_j=1$ above the cutoff and $p_j=0$ below. For an orthogonal projector, $p_j=1$ implies $\Pi v_j=v_j$, and $p_j=0$ implies $\Pi v_j=0$, by the norm identities for projections. Its remaining range lies within the cutoff eigenspace. Reversing the change of variable gives $M=K^{-1/2}A\Pi S^{-1/2}=S^{1/2}\Pi S^{-1/2}$. This proves the value and all equality cases. $\square$

This is a weighted form of the classical low-rank approximation theorem. Its BM role is to identify the optimum within a precise representation Passport, rather than to rename that classical theorem.

## LEV 014C Exact zero-price criterion

For $0<d<n$, the projector optimum attains the unrestricted optimum if and only if there is a maximizing spectral projector $\Pi$ of $H$ such that

$$[S,\Pi]=0.$$

If there is a spectral gap $\theta_d>\theta_{d+1}$, it is enough and necessary to test this commutator for the unique leading spectral projector. If the commutator is nonzero, the projector admissibility price

$$\Gamma_d=J_{d,\mathrm{proj}}^*-J_{d,\mathrm{lin}}^*$$

is strictly positive. For $d=0,n$, both classes have the same trivial optimum.

### Proof

Every rank-$d$ orthogonal projector belongs to the unrestricted class, so $\Gamma_d\ge0$. An unrestricted optimizer $M=S^{1/2}\Pi S^{-1/2}$ is idempotent. It is symmetric exactly when

$$S^{1/2}\Pi S^{-1/2}=S^{-1/2}\Pi S^{1/2},$$

which, after multiplication on both sides by $S^{1/2}$, is exactly $S\Pi=\Pi S$. If this holds, $M=\Pi$ and is an admissible orthogonal optimizer. Conversely, if a projector achieves the unrestricted value, the preceding equality characterization represents it by such a $\Pi$, and symmetry forces the commutator to vanish.

The projector feasible set is closed and bounded in finite-dimensional matrix space and is nonempty. The continuous objective attains its minimum there. If the criterion fails, no projector attains the unrestricted value. The attained minimum is therefore strictly larger. The spectral-gap clause follows from uniqueness in LEV 013. $\square$

This criterion is a derived refinement of LEV 014A and its commuting sufficient condition. It does not assert historical priority. It also shows why noncommutation of $S$ and $K$ alone is not an exact test for a positive price: they can fail to commute inside the retained or discarded blocks while the separating optimal projector still commutes with $S$.

### Exact strict-price example

Let

$$S=\begin{pmatrix}9&0\\0&1\end{pmatrix},\qquad
K=\begin{pmatrix}17/2&-15/2\\-15/2&17/2\end{pmatrix},\quad d=1.$$

The eigenvalues of $K$ are 1 and 16. The trace and determinant of $H$ are 85 and 144. Therefore its eigenvalues are $(85\pm\sqrt{6649})/2$, distinct. Its off-diagonal entry is $-45/2$, so its leading eigendirection is neither coordinate axis. Any rank-one projector commuting with the distinct diagonal matrix $S$ must project onto a coordinate axis. The criterion therefore proves $\Gamma_1>0$ without relying on a numerical optimizer.

The unrestricted value is $(85-\sqrt{6649})/2\approx1.729299736$. Writing a discarded direction as $u=(1,t)/\sqrt{1+t^2}$ gives

$$J(t)=\frac{(17/2-15t+(17/2)t^2)(9+t^2)}{(1+t^2)^2}.$$

Differentiating and clearing the nonzero denominator shows every finite stationary slope solves

$$15t^4-136t^3+360t^2-136t-135=0.$$

The vertical direction has value $17/2$. The 14 October 2026 rational verification addendum certifies exactly two real stationary slopes and the global minimum, with $t\approx1.1331774435714206$ and $J_{1,\mathrm{proj}}^*\approx4.7647047437506865$. The formerly printed slope $1.13317887$ was inaccurate at its displayed precision. The unrestricted optimum is unchanged, and the certified penalty is $\Gamma_1\approx3.0354050075430659$. Full outward rational enclosures, the Sturm sequence, and the exact certificate appear in the dated development addendum below. The earlier exact proof of strict positivity is unaffected.

## LEV 014 Grassmann stationarity

For symmetric $P$, expanding gives

$$J(P)=\operatorname{tr}(KS)-\operatorname{tr}((KS+SK)P)+\operatorname{tr}(KPSP).$$

Differentiation in a symmetric direction gives ambient gradient $G(P)=-(KS+SK)+SPK+KPS$. The tangent directions to the fixed-rank projector manifold are $[\Omega,P]$ with $\Omega^\top=-\Omega$. Cyclicity of trace gives $dJ([\Omega,P])=\operatorname{tr}([P,G]\Omega)$. Since $[P,G]$ is skew-symmetric, this vanishes for every skew-symmetric $\Omega$ iff $[P,G]=0$. This is necessary and sufficient for stationarity, not global optimality.

With $Q=I-P=UU^\top$, $U^\top U=I_{n-d}$, put $A_U=U^\top KU$ and $B_U=U^\top SU$. Cyclicity yields $J=\operatorname{tr}(A_UB_U)$. Differentiation gives $\nabla_UJ=2KUB_U+2SUA_U$ and the stationary equation

$$KUB_U+SUA_U=U(A_UB_U+B_UA_U).$$

When $S$ and $K$ commute, a common orthonormal eigenbasis makes $H$ diagonal with entries $s_jk_j$. Retaining the largest $d$ products gives a projector achieving LEV 013, so it is globally optimal. Noncommuting higher-rank stationarity still requires a global certificate.

## LEV 015 One discarded dimension

For positive-definite $K,S$, let $m=\min_{\|u\|=1}(u^\top Ku)(u^\top Su)$. Then

$$m=\frac14\left[\min_{\tau>0}\lambda_{\min}(\tau K+\tau^{-1}S)\right]^2.$$

A global minimizing $\tau$ exists in

$$\left[\sqrt{s_{\min}/k_{\max}},\sqrt{s_{\max}/k_{\min}}\right].$$

### Proof and equality conditions

For $a,b>0$, $(\tau a+\tau^{-1}b)^2/4=ab+(\tau a-\tau^{-1}b)^2/4$, whose minimum is $ab$ at $\tau=\sqrt{b/a}$. Taking the joint infimum over the unit sphere and positive $\tau$ in either order is valid: both expressions are the infimum of the same function on the same product set. For fixed $\tau$, the Rayleigh principle gives the displayed eigenvalue. Positivity allows squaring after minimization.

The product objective attains its minimum on the compact sphere. A minimizing $u$ supplies a balancing $\tau$ in the stated interval by the extremal eigenvalue bounds on $a$ and $b$. Conversely the scalar objective diverges as $\tau\to0$ or $\infty$, since it is at least $\tau k_{\min}+\tau^{-1}s_{\min}$. Thus global minimizers exist.

At an exactly globally minimizing $\tau_*$, every unit minimum eigenvector $u$ is balanced and minimizes the product. Indeed its squared scalar value divided by four equals $m$; AM-GM gives $ab\le m$, while the definition of $m$ gives $ab\ge m$. Equality forces balance. Multiplying the eigen-equation by $\sqrt{ab}$ gives $bKu+aSu=2ab\,u$. This argument also covers a multiple minimum eigenvalue. A numerical or merely local scalar minimizer does not inherit this conclusion and must be checked. $\square$

The earlier log's warning that an arbitrary minimum eigenvector can fail balance at an *exact global* scalar minimizer was overly restrictive. The equality argument above repairs it; numerical degeneracy remains a computational issue.

## LEV 016 Higher-rank matrix balancing

For SPD matrices $A,B$, let $T\succ0$, $X=T^{1/2}AT^{1/2}$, $Y=T^{-1/2}BT^{-1/2}$. Trace cyclicity gives $\operatorname{tr}(XY)=\operatorname{tr}(AB)$. The parallelogram identity yields

$$\tfrac14\|X+Y\|_F^2=\operatorname{tr}(AB)+\tfrac14\|X-Y\|_F^2.$$

Equality holds precisely when $TAT=B$. Multiplying by $A^{1/2}$ shows $(A^{1/2}TA^{1/2})^2=A^{1/2}BA^{1/2}$. The unique SPD square root therefore gives the unique balancing matrix

$$T_*=A^{-1/2}(A^{1/2}BA^{1/2})^{1/2}A^{-1/2}.$$

This proves the exact balancing identity and attainability. With $A=A_U,B=B_U$, it is an exact reformulation for each discarded subspace. It does not solve the remaining nonconvex minimization over $U$.

If only a scalar $\tau$ is allowed, direct minimization gives

$$\min_{\tau>0}\tfrac14\|\tau A+\tau^{-1}B\|_F^2
=\tfrac12\bigl(\|A\|_F\|B\|_F+\operatorname{tr}(AB)\bigr).$$

The excess over $\operatorname{tr}(AB)$ is nonnegative by Frobenius Cauchy-Schwarz and vanishes exactly when $A$ and $B$ are positive scalar multiples. A scalar analogy cannot replace the matrix balancing proof. $\square$

## LEV 014S Strengthened moment certificate

Let $p=\operatorname{vec}P$ with column-major index $\iota(i,j)=i+nj$, and lift $pp^\top$ to a symmetric matrix $X$. Impose

$$\begin{pmatrix}1&p^\top\\p&X\end{pmatrix}\succeq0,\quad
P=P^\top,\quad0\preceq P\preceq I,\quad\operatorname{tr}P=d,$$

$$\sum_kX_{\iota(i,k),\iota(k,j)}=p_{\iota(i,j)},$$

$$X_{\iota(i,j),c}=X_{\iota(j,i),c},\qquad
\sum_iX_{\iota(i,i),c}=d p_c.$$

Every exact projector supplies a feasible lift: each equation is either its Passport constraint or that constraint multiplied by a coordinate. Replacing each quadratic monomial in $J$ by the corresponding $X$ entry gives a linear objective $J_{\mathrm{lift}}$. Its minimum is a lower bound on the projector optimum. Removing the last two families of equations weakens the lower bound.

For $K=\kappa I,S=\sigma I$, summing lifted diagonal idempotency and using the symmetry-localizing equations gives $\sum_{i,k}X_{\iota(i,k),\iota(i,k)}=d$. Hence every feasible strengthened point has objective $\kappa\sigma(n-2d+d)=\kappa\sigma(n-d)$, exactly the projector value. The strengthened relaxation is therefore exact throughout this isotropic sector.

If an optimal moment matrix has rank one, its top-left entry 1 and positive semidefiniteness imply $X=pp^\top$. Idempotency then recovers $P^2=P$, making $P$ a feasible projector attaining the lower bound and hence a global optimizer. A merely approximately rank-one numeric matrix is not an exact certificate. A floating-point SDP primal value alone is also not a rigorous lower bound without dual feasibility or an error certificate. $\square$

The method is classical moment relaxation. The mathematical contribution here is the complete derivation from this representation Passport and its integration with the exact admissibility test. The closing addendum supplies global matching bounds to every positive tolerance for arbitrary finite rational SPD inputs and ranks. Efficient general solution and closed-form optimizer descriptions remain unestablished.

# Continuum profiles and boundary ports

## Approximation is measured on the receiver profile

Let $K$ be the declared bounded admissible family in a native state space, and let $\mathcal P:K\to Y$ collect the receiver's required responses. In this chapter $Y$ is a complete metric space. Define $N(\varepsilon)$ to be the minimum number of radius-$\varepsilon$ balls with centers anywhere in $Y$ that cover $\mathcal P(K)$, and set

$$w(\varepsilon)=\log_2N(\varepsilon).$$

If no finite cover exists, both quantities are infinite. This is a covering number and its logarithm. Probability is not part of the definition. Requiring centers to belong to $\mathcal P(K)$ is a different convention and can change constants.

**Compactness criterion.** $N(\varepsilon)$ is finite for every $\varepsilon>0$ exactly when $\mathcal P(K)$ is relatively compact.

**Proof.** Finite covers at every scale are total boundedness. In a complete ambient space the closure of a totally bounded set is complete and totally bounded, hence compact: every sequence has a Cauchy subsequence obtained by successively selecting one ball from finite covers at scales tending to zero. Conversely a compact closure has a finite subcover at every scale.

Compactness of a response image does not assert existence or regularity of the native evolution that defines the response. Those are antecedent hypotheses. A finite covering number also does not imply that a useful cover can be discovered efficiently.

## A spectral estimate with an explicit covering proof

Let $O:H\to Y$ be a compact linear operator between real Hilbert spaces, acting on the unit ball of $H$. Write its singular values as $\sigma_1\ge\sigma_2\ge\cdots$. Choose $n\ge1$ with $\sigma_{n+1}\le\varepsilon/2$. Then the following conservative bound holds:

$$N(\varepsilon)\le
\prod_{j=1}^{n}\left(1+\frac{2\sqrt n\,\sigma_j}{\varepsilon}\right).$$

**Proof.** The omitted singular-coordinate tail has norm at most $\varepsilon/2$. In the first $n$ coordinates the image lies in the box $\prod_j[-\sigma_j,\sigma_j]$. Divide each interval into at most $\max(1,\lceil2\sqrt n\sigma_j/\varepsilon\rceil)$ equal subintervals of length at most $\varepsilon/\sqrt n$, using their midpoints. The leading-coordinate error is at most $\varepsilon/2$. Orthogonality combines leading and tail errors to at most $\varepsilon/\sqrt2$, which is below the requested radius. The number of centers is bounded by the displayed product. Zero axes use one center.

This proof deliberately exposes the dimension factor. The shorter product estimate recorded as PDEW-02 in the development log is not imported without a matching ellipsoid-covering theorem and center convention. Sharper entropy estimates are possible; this edition uses the bound proved above.

## Positive time in the heat equation

For a positive self-adjoint operator $A$ with eigenvalues $\lambda_j\to\infty$, heat evolution is $e^{-tA}$. Its singular values at time $\tau>0$ are $e^{-\tau\lambda_j}$, so the image of the unit ball is relatively compact. At time zero the unit ball in an infinite-dimensional Hilbert space is not totally bounded: an infinite orthonormal sequence has pairwise distance $\sqrt2$, precluding finite sufficiently small covers.

At every finite positive time the heat map remains injective, since all its spectral multipliers are positive. Its inverse on its range is unbounded, since inverse multipliers grow without bound. Thus exact distinction preservation and stable recovery are different properties in this familiar model.

Assume two-sided spectral growth $c j^{2/d}\le\lambda_j\le C j^{2/d}$ for large $j$. For each fixed $\tau>0$, the covering estimates imply the order

$$w_\tau(\varepsilon)\asymp
\tau^{-d/2}\left(\log\frac1\varepsilon\right)^{1+d/2}
\quad\text{as }\varepsilon\downarrow0.$$

For the upper bound choose $n$ of order $(\tau^{-1}\log(1/\varepsilon))^{d/2}$ in the grid estimate. Its logarithm is at most a constant times $n\log(1/\varepsilon)$; the extra $n\log n$ term is lower order. For the lower bound project to the first $m$ singular coordinates with $\tau\lambda_m\le\tfrac12\log(1/\varepsilon)$. Comparing the ellipsoid's volume with $m$-ball covering volumes gives $\log N\ge\sum_{j\le m}\log(\sigma_j/\varepsilon)\ge\tfrac m2\log(1/\varepsilon)$. The two spectral bounds give the stated order. Constants and the asymptotic threshold depend on the spectral bounds and fixed $\tau$; uniform joint limits in $\tau$ and $\varepsilon$ require further work.

This is a metric-entropy calculation for a specified linear evolution. It is not a theorem about arbitrary nonlinear PDEs.

## Coupling obligations at a boundary

Let $g$ be a boundary trace, $\Lambda g$ its coupling response, and $Lg$ a receiver task, with both maps linear on the declared trace space. The exact indistinguishable difference space is

$$E_{\mathrm{port}}=\ker\Lambda\cap\ker L.$$

This is the nullspace of the combined map $(\Lambda,L)$. A trace difference that is irrelevant to $L$ can remain necessary to $\Lambda$. Task-only reduction therefore need not be a lawful replacement at a physical interface.

If $\Lambda$ is bounded below by $c>0$ on an infinite-dimensional Hilbert subspace, its image of that subspace's unit ball is not totally bounded. Images of an orthonormal sequence are at least $c\sqrt2$ apart. Full-trace coupling has infinite covering width for radii smaller than $c/\sqrt2$.

The situation changes if reachable traces are $g=Tu$ with $u$ in a bounded unit ball and $T$ compact. Then $(\Lambda,L)T$ is compact whenever $\Lambda,L$ are bounded. The lawful reachable family, not the entire abstract trace space, determines the approximation problem.

For an invertible bounded coupling equation $Sg=\sum_iB_if_i$ and output $z=Cg$, the deployment-specific contribution from source $i$ is $G_i=CS^{-1}B_i$. This formula presupposes invertibility and the relevant domains. Near-singular coupling can greatly amplify a small interface error.

In a conforming coercive variational problem with continuity constant $M$ and coercivity constant $\alpha>0$, Galerkin orthogonality gives

$$\|C(g-g_n)\|\le\|C\|\frac{M}{\alpha}
\inf_{v\in V_n}\|g-v\|.$$

Indeed coercivity bounds $\alpha\|g-g_n\|^2$ by the bilinear form on $(g-g_n,g-v)$, which is at most $M\|g-g_n\|\|g-v\|$. This is a classical approximation estimate with a receiver map attached. It explains why interface approximation and coupling conditioning must be reported together.

# Causal and distributed representations

## The future profile of a past

Fix a cut time and a common set of admissible future continuations. Two past histories are equivalent if they give the same future receiver response under every such continuation. If continuation availability depends on the past, include that availability as a tagged output.

Appending an admissible input preserves this residual equivalence: every later continuation is also a continuation of the earlier extended history. The quotient therefore supports a causal state update. This is the same future-distinction construction used in automata and realization theory, with the actual task and admissibility retained.

For a linear system with zero-state reachability $\mathcal R_t$ from past inputs and future observation $\mathcal O_{t,T}$ on a fixed horizon, the zero-future-input contribution is

$$\mathcal H_t=\mathcal O_{t,T}\mathcal R_t.$$

Its kernel identifies exactly the past differences invisible to that future profile. Future forcing must either be held common or included in the receiver context. Compactness of this Hankel map is equivalent to total boundedness of the image of its input unit ball. An assertion about every bounded past family needs the same bounded linear input-space contract.

For pure delay $y(s)=u(s-\tau)$, histories $u$ known on $[0,t]$, and future receiver interval $[t,T]$, the portion of the past still needed is

$$u\big|_{[t-\tau,T-\tau]\cap[0,t]}.$$

This is exact deadline-dependent pruning in the specified delay model. It is not a claim that arbitrary memory kernels have a finite-dimensional state.

## Capacity is necessary but may not be sufficient

Let finite messages on a cut have alphabets $Q_e$, and let $Q^*$ be the exact receiver quotient on the admissible cut histories. If the joint messages determine the quotient, then

$$\sum_e\log_2|Q_e|\ge\log_2|Q^*|.$$

**Proof.** The realized joint messages must have at least $|Q^*|$ values, while their total possible values are at most $\prod_e|Q_e|$.

For a centralized encoder of two bits, their XOR needs only one output bit. If two separate senders each sees only its own bit and sends one simultaneous deterministic message to a receiver, both sender maps must be injective to recover XOR for all four input pairs. Otherwise fixing the other input gives a collision. Two transmitted bits are required. The one-bit quotient lower bound survives, but distributed realizability is stricter.

If every subset of $m-f$ routes must carry at least $H$ bits of semantic capacity, nonnegative route capacities $c_e$ obey

$$\sum_{e=1}^m c_e\ge\frac{m}{m-f}H,\qquad 0\le f<m.$$

Sum the inequality over all $\binom m{m-f}$ survivor sets. Each route is counted $\binom{m-1}{m-f-1}$ times. Dividing gives the bound. It is necessary, not a coding or routing existence theorem.

## Perturbation and usable locality

Suppose two task-profile maps into a normed space differ uniformly by at most $\delta$. The pairwise profile distances differ by at most $2\delta$, by two applications of the triangle inequality. If their profile images have Hausdorff distance at most $\delta$ and covering centers are ambient, then for $\varepsilon>\delta$,

$$N_0(\varepsilon+\delta)\le N_\lambda(\varepsilon)
\le N_0(\varepsilon-\delta).$$

Move a center only by using the existing cover, then enlarge the radius to cover the other image; this proves each inequality. Exact equality classes can split under an arbitrarily small nonzero perturbation even while this approximate-width comparison remains useful.

If a supplied locality theorem bounds omitted influence by $Ce^{-\mu(r-vH)}$, radius

$$r\ge vH+\mu^{-1}\log(C/\varepsilon)$$

is sufficient for error at most $\varepsilon$. It is an algebraic consequence of the supplied influence bound. Local interactions alone do not prove that bound, nor do they prove a semantic area law. A full-state receiver can require volume-sized information. Separate locality theorems are required for hyperbolic PDEs, parabolic PDEs, lattice systems, and quantum channels.


# Physical quantum closure


Let E:M_n(ℂ)→M_m(ℂ) and Φ:M_n(ℂ)→M_n(ℂ) be specified CPTP maps. Physical reduced closure means a CPTP map Ψ:M_m→M_m satisfying

\[
\Psi E=E\Phi.
\]

Use the input-first Choi convention

\[
J_\Psi=\sum_{a,b=1}^m |a\rangle\langle b|\otimes\Psi(|a\rangle\langle b|).
\]

Write J_ab for its m×m blocks. There is such a Ψ **if and only if** the following finite system is feasible:

\[
\boxed{
J\succeq0,\qquad
\operatorname{Tr}_\mathrm{out}J=I_m,\qquad
\sum_{a,b=1}^m[E(E_{ij})]_{ab}J_{ab}=(E\Phi)(E_{ij})
\quad(1\le i,j\le n).
}
\]

Here E_ij are the native n×n matrix units. Complex equations can be split into real and imaginary parts.

**Proof.** A reduced channel provides these blocks, and linearity gives the displayed equations. Conversely a feasible J defines Ψ(A)=Σ_ab A_ab J_ab. Choi positivity makes Ψ completely positive; the partial trace condition makes it trace preserving. The last constraints give ΨE=EΦ on a matrix-unit basis and therefore on every input. $\square$

The channel characterization is classical. The displayed constraints are its direct application to the specified BM closure equation. [Watrous, *The Theory of Quantum Information*, §2.2.2, Corollary 2.27](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf).

This is a complete finite-dimensional feasibility criterion. A floating-point solver status alone is not an exact feasibility or infeasibility certificate. General abstract operator-system realizations, infinite-dimensional channels, and a closed-form classification for all families remain different questions.

## Explicit range-invariance counterexample

For 0<λ<1, let E be qubit dephasing, acting on Bloch coordinates as

\[
(r_x,r_y,r_z)\mapsto(\lambda r_x,\lambda r_y,r_z).
\]

Let Φ be conjugation by the Hadamard unitary, so it sends (r_x,r_y,r_z) to (r_z,-r_y,r_x). E is invertible as a linear map, so Ran E† is the entire observable space and every range-invariance condition holds. The only possible linear reduced map is Ψ=EΦE^-1, which sends

\[
(r_x,r_y,r_z)\mapsto(\lambda r_z,-r_y,r_x/\lambda).
\]

Applied to the valid ambient qubit state (I+X)/2, its output is (I+λ^-1 Z)/2, with eigenvalues (1±λ^-1)/2. One is negative. Thus no physical reduced channel exists. At λ=1/2 these eigenvalues are -1/2 and 3/2. The test state lies outside E's reachable state ellipsoid when λ<1; that does not invalidate this argument, because the contract requires a CPTP map on the full reduced matrix algebra. Linear invertibility of E fixes that map on the whole algebra. A map defined only on the reachable ellipsoid is a different contract.

## A useful sufficient condition

If E has a CPTP right inverse S, ES=id, then linear kernel stability

\[
\ker E\subseteq\ker(E\Phi)
\]

is also sufficient: set Ψ=EΦS. It is CPTP by composition. Since E(SE-I)=0, stability gives EΦ(SE-I)=0, hence ΨE=EΦ. This condition covers a specified split channel, not arbitrary compressions.

In finite dimensions the physical closure defect

\[
\delta_Q=\min_{\Psi\;\mathrm{CPTP}}\|E\Phi-\Psi E\|_\diamond
\]

is attained: the channel set is compact and the objective is continuous. Therefore δ_Q=0 exactly when the feasibility system holds. The norm convention here has no extra factor of 1/2.

# Exact and approximate quantum capability

## An algebra is a task specification

Throughout this chapter all Hilbert spaces are finite-dimensional. Incorporate the fixed encoding into a channel $N:M_d\to M_b$ with Kraus operators $A_i$ and $\sum_iA_i^\dagger A_i=I_d$. A task algebra $\mathcal A\subseteq M_d$ is a unital complex star subalgebra. Recovery means a CPTP map $R:M_b\to M_d$ with

$$N^\dagger R^\dagger(X)=X\quad(X\in\mathcal A).$$

The established operator-algebra error-correction criterion is $[X,A_i^\dagger A_j]=0$ for every $X\in\mathcal A$ and every $i,j$. It follows that the greatest exactly recoverable algebra is

$$\mathcal A_{\max}(N)=C^*(A_i^\dagger A_j:i,j)'$$

inside the logical matrix algebra. This is imported OAQEC, not a new BM recovery theorem [BenyKempfKribs2007]. BM uses the algebra as a receiver Passport and retains the physical-channel requirement.

Intersecting $\mathcal A_{\max}$ with a requested algebra gives its strongest exactly recoverable subalgebra. It does not authorize changing the receiver's request. If a more damaged channel is a postprocessing $N_2=D\circ N_1$, every recovery after $N_2$ can be composed with $D$ to recover after $N_1$. Therefore $\mathcal A_{\max}(N_2)\subseteq\mathcal A_{\max}(N_1)$. Failure-set inclusion alone is insufficient unless this channel relation is justified.

## Disjoint access and failure sets

Two disjoint physical regions cannot each exactly recover the same noncommutative task algebra for every logical input. To see this, apply the two recovery channels on the disjoint regions, obtaining a joint channel $M$. Its adjoint obeys $M^\dagger(X\otimes I)=X$ and $M^\dagger(I\otimes Y)=Y$ for task operators. For task unitaries, these equalities place the corresponding operators in the multiplicative domain of the unital completely positive map. Since the two tensor factors commute, their images commute. Unitaries span a finite-dimensional star algebra, so all elements of the task algebra commute. The multiplicative-domain fact is a standard consequence of the Schwarz equality for completely positive maps [Watrous2018].

Consequently authorized sets for one noncommutative task must pairwise intersect. For a symmetric threshold structure in which every $k$ of $m$ regions is authorized, this requires $2k>m$. This is a necessary access condition; it does not construct a code.

If authorization is monotone under adding surviving regions, let $\mathcal M$ be the family of minimal authorized sets. An erasure set destroys all authorized access exactly when it intersects every member of $\mathcal M$. The minimum number of erasures causing that failure is the transversal number $\tau(\mathcal M)$. This is finite-set combinatorics applied to the actual authorization family. Trivial tasks and absent authorized sets require the usual empty-family conventions.

## Three different approximate defects

Let $\mathcal K=\operatorname{span}\{A_i^\dagger A_j\}$ and define

$$\kappa_{\mathcal A}(N)=
\sup_{\substack{Z\in\mathcal K,\ \|Z\|\le1\\X\in\mathcal A,\ \|X\|\le1}}
\|[Z,X]\|,$$

$$\eta_{\mathcal A}(N)=\sup_{Z\in\mathcal K,\ \|Z\|\le1}
\operatorname{dist}(Z,\mathcal A'),$$

$$\delta_{\mathcal A}(N)=\min_{R\ \mathrm{CPTP}}
\sup_{X\in\mathcal A,\ \|X\|\le1}
\|X-N^\dagger R^\dagger(X)\|.$$

All norms inside the suprema are operator norms. The recovery minimum is attained because the finite-dimensional channel set is compact. The first two defects concern the normalized error operator system. The third concerns a physical decoder.

**Commutator comparison.** $\eta\le\kappa\le2\eta$.

**Proof.** Average conjugation over the compact unitary group of $\mathcal A$. This produces a norm-one conditional expectation $P_{\mathcal A'}$ onto its commutant. For $\|Z\|\le1$, the norm of $Z-P_{\mathcal A'}Z$ is at most $\kappa$, by averaging $Z-UZU^\dagger$. Conversely any $Y\in\mathcal A'$ gives $\|[Z,X]\|=\|[Z-Y,X]\|\le2\|Z-Y\|$ for $\|X\|\le1$. Take infima and suprema.

These normalized algebraic defects need not vary continuously with noise strength when $\mathcal K$ changes dimension. They are not interchangeable with a channel-distance error.

## A finite Kraus rank recovery bound

The Volume II question admits the following explicit finite-dimensional answer. Let $r$ be the number of Kraus operators in a chosen representation, after incorporating the encoding. Then

$$\boxed{\delta_{\mathcal A}(N)\le
\min\{2,\,2r\sqrt{\kappa_{\mathcal A}(N)}\}
\le\min\{2,\,2r\sqrt{2\eta_{\mathcal A}(N)}\}.}$$

This bound is conservative and need not be sharp. It makes the environment-size dependence explicit.

**Proof of the norm conversion.** Choose the complementary channel with

$$\widehat N^\dagger(B)=\sum_{i,j=1}^r B_{ij}A_i^\dagger A_j.$$

Let $P=P_{\mathcal A'}$. Haar averaging gives
$\|(I-P)(A_i^\dagger A_j)\|\le\kappa\|A_i^\dagger A_j\|\le\kappa$.
At every matrix amplification, each block of a matrix of norm at most one has norm at most one. The triangle inequality for the $r^2$ blocks therefore gives

$$\beta:=\|\widehat N-\widehat N P\|_\diamond\le r^2\kappa.$$

We now use the established approximate OAQEC upper bound
$\min_R\|RN-P_{\mathcal A}\|_\diamond\le2\sqrt\beta$
from [Beny2009, Theorem 1 in the cited arXiv version]. On task observables $P_{\mathcal A}^\dagger(X)=X$, and the completely bounded norm controls the unamplified operator norm. Thus $\delta\le2\sqrt\beta\le2r\sqrt\kappa$. The bound by two follows from contractivity of unital channel adjoints. Finally use $\kappa\le2\eta$.

This is a proved norm conversion and a consequence of an imported recovery theorem. It resolves a specified finite Kraus rank version of the earlier question. It supplies neither a sharp universal dimension-free function of the original $\kappa$ nor an infinite-dimensional theorem. Changing to the stronger complementary-channel defect $\beta$ gives the imported dimension-independent estimate directly; changing the defect must be stated.

## There need not be a greatest approximate algebra

Let $N$ be complete dephasing in the qubit $Z$ basis:

$$N(\rho)=\tfrac12(\rho+Z\rho Z).$$

It exactly preserves $\mathcal A_Z=C^*(Z)$. For $0<\theta<\pi/2$ put
$A_\theta=\cos\theta\,Z+\sin\theta\,X$ and
$\mathcal A_\theta=C^*(A_\theta)$. Then

$$\delta_{\mathcal A_\theta}(N)=\sin\theta,\qquad
\delta_{M_2}(N)=1.$$

**Proof.** Every element of $\mathcal A_\theta$ has the form $aI+bA_\theta$; a unit-norm such element has $|b|\le1$. Identity recovery loses only $b\sin\theta X$, proving the upper bound $\sin\theta$. Every dephased adjoint output is diagonal. The norm distance of $A_\theta$ from any diagonal matrix is at least $\sin\theta$, because each off-diagonal matrix entry has magnitude $\sin\theta$ and is bounded by operator norm. This proves equality. For the full algebra the same argument at $X$ gives a lower bound one. Identity recovery has defect $\|I-N^\dagger\|\le1$, since $I-N^\dagger=(I-\operatorname{Ad}_Z)/2$, proving equality.

The algebras $\mathcal A_Z$ and $\mathcal A_\theta$ generate $M_2$: solve for $X$ from $A_\theta$ and $Z$, then use their product for $Y$. For any $0<\varepsilon<1$, choose $0<\sin\theta\le\varepsilon$. Both small algebras are $\varepsilon$-recoverable, but no $\varepsilon$-recoverable algebra can contain both, because it would contain $M_2$. Thus the approximate capability family has no greatest element. This is a fully explicit finite counterexample, not an inference from the mere existence of incomparable decoders.

## Perturbation reserve and repair cost

For channels with the same input and output types,

$$|\delta_{\mathcal A}(N)-\delta_{\mathcal A}(M)|\le\|N-M\|_\diamond.$$

Fix any recovery, apply the triangle inequality and adjoint contractivity, then minimize in both directions. A recovery margin therefore gives a channel-perturbation reserve. Subalgebra restriction can only decrease the defect. For an intervention $u$ at declared cost $c(u)$, an approximate repair problem is

$$J_{\mathcal A}(\varepsilon)=\inf\{c(u):\delta_{\mathcal A}(N_u)\le\varepsilon\}.$$

Existence of a feasible intervention, attainment, and computation of this infimum require their own hypotheses. The formula does not supply the intervention.


# Experiments and exact distinction gain

## Quotient width without a probability law

Let $X$ be a nonempty finite state set. Every deterministic experiment $u$ has a response $R_u:X\to Y_u$. For a family $S$, let $Q_S$ be the partition by equality of every response in $S$, and define

$$w(S)=\log_2|Q_S|,\qquad G(v\mid S)=w(S\cup\{v\})-w(S).$$

This logarithmic count is a Hartley-type support size, not Shannon entropy. No distribution is assigned to the states. It measures the number of exact response classes for the declared experiment family.

W01-W04 follow directly from partition refinement. Adding experiments cannot decrease width. The map sending a joint response class to its two separate response classes is injective, giving

$$\max\{w(A),w(B)\}\le w(A\cup B)\le w(A)+w(B).$$

An experiment adds zero width exactly when its response factors through the existing quotient. Finally, if $s_v(C)$ is the number of distinct $v$ responses in class $C\in Q_S$, then

$$|Q_{S\cup\{v\}}|=\sum_{C\in Q_S}s_v(C),\qquad
G(v\mid S)=\log_2\left(\frac1{|Q_S|}\sum_Cs_v(C)\right).$$

These are exact finite identities. The arithmetic average in the final formula is a consequence of counting classes; it is not an assumed physical probability distribution.

## The incidence cycle criterion

Suppose $A\subseteq B$. Inside each $A$ class, form a simple bipartite graph. Its left vertices are the $B$ subclasses; its right vertices are the subclasses formed by experiment $v$; an edge means that their intersection is nonempty. Let

$$p=|Q_A|,\quad K=|Q_B|,\quad S=|Q_{A\cup\{v\}}|,\quad
T=|Q_{B\cup\{v\}}|.$$

Across the local graphs let $\kappa$ be the total number of connected components and $\mu$ the total cycle rank. There are $K+S$ vertices and $T$ edges. The graph identity for cycle rank gives

$$T=K+S-\kappa+\mu.$$

Strict increasing marginal distinction, $G(v\mid B)>G(v\mid A)$, is equivalent to $pT>KS$. Substitution and rearrangement give W08:

$$\boxed{p\mu>(K-p)(S-p)+p(\kappa-p).}$$

Every local graph is nonempty, so $K,S,\kappa\ge p$. A forest therefore cannot produce strict complementarity. A cycle supplies a possible surplus; it must still exceed the refinement terms on the right. Presence of a cycle alone is not sufficient.

## Why five states are necessary and sufficient

If $p=1$, then $T\le KS$ by the elementary product bound, so strict complementarity is impossible. If $p\ge2$, the cycle criterion requires at least one cycle. A simple bipartite cycle has at least four edges and needs at least four states witnessing its nonempty intersections. Every other $A$ class requires another state. Thus at least $p+3\ge5$ states are necessary.

Five suffice. Use the following response table, where the second column refines the first.

| State | $A$ response | $B$ response | $v$ response |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 |
| 3 | 0 | 1 | 0 |
| 4 | 0 | 1 | 1 |
| 5 | 1 | 2 | 0 |

The four counts are $(p,S,K,T)=(2,3,3,5)$, so $5/3>3/2$. The local graph on the first four states is a four-cycle; the fifth state supplies another $A$ class. This proves W05 and W06. Duplicating an existing state's response pattern produces examples on every larger state set, proving W07.

The threshold depends on this exact quotient-width objective. It should not be transferred to entropy, noisy channels, adaptive costs, or pair coverage without a new argument. Historical priority for the five-state formulation and W08 is not established by this proof.

## Pair coverage has different optimization geometry

Let $D_T$ be the finite set of state pairs that the task requires to be separated. Let $D_u$ be the pairs separated by experiment $u$. Define

$$C_T(S)=\left|D_T\cap\bigcup_{u\in S}D_u\right|.$$

The marginal gain of $v$ counts the required pairs in $D_v$ not already covered by $S$. Enlarging $S$ can only remove such uncovered pairs. Therefore $C_T$ is monotone and submodular, proving W15. Exact quotient width need not be submodular, even though complete pair separation and a sufficient exact quotient may represent the same terminal requirement. Choosing the optimization objective changes the intermediate search problem.

## Exact dimension can jump while approximation survives

For independent decays $\dot x_i=-k_ix_i$, let $S=\sum_ix_i$. If the initial-state family includes all nonnegative coordinate vectors, $S$ has an exact autonomous future for all admissible states only when the rates are equal. Necessity follows by comparing initial states $e_i,e_j$, whose initial sums agree and whose futures are $e^{-k_it}$ and $e^{-k_jt}$. Equal rates make the sum solve $\dot S=-kS$, proving sufficiency.

If $k_i=k+\delta_i$, $k\ge0$, $|\delta_i|\le\eta$, and $x_i(0)\ge0$ with $\sum_i x_i(0)\le M$, then for $0\le t\le H$,

$$|S(t)-S(0)e^{-kt}|\le M(e^{\eta H}-1).$$

The proof bounds each $|e^{-\delta_it}-1|$ by $e^{\eta H}-1$ and sums the nonnegative initial weights. Without the sign condition one must bound $\sum_i|x_i(0)|$ instead. A bound on the signed sum alone is insufficient. This makes the missing admissible-state conditions in W11 explicit.

For a general linear system $\dot x=A(\theta)x$, $y=C(\theta)x$, the exact linear output-carrier dimension is the observability rank of the stack $(C,CA,\ldots,CA^{n-1})$. Cayley-Hamilton makes its kernel invariant and identifies all future-invisible differences. Any exact linear carrier must retain those distinctions, and the quotient attains the rank. This is classical observability in BM scope, not a new rank theorem.

A simple continuous example is $F_\theta(x,y)=(x,\theta y)$ on the closed unit disk. At $\theta=0$ one real coordinate is necessary and sufficient for exact recovery. At $\theta\ne0$ the map is injective, so an exact encoder must be injective. No continuous encoder of the disk into the line is injective: its restriction to the boundary circle has an equal-valued antipodal pair by Borsuk-Ulam. Two coordinates suffice. Yet the old encoder $R(x,y)=x$ and decoder $D(x)=(x,0)$ have error at most $|\theta|$. This proves a precise W12 dimension jump with uniformly vanishing approximation error.

## Adaptive and robust thresholds

For deterministic unit-cost tests, compare the worst-case depth of an adaptive decision tree with the number of tests in a fixed separating set. Four hypotheses permit a strict adaptive advantage. First ask whether the state belongs to $\{a,b\}$ or $\{c,d\}$, then ask a test isolating $a$ in the first branch or a test isolating $c$ in the second. This adaptive strategy uses two tests. All three available tests are needed in a fixed set: omitting any one leaves a pair unseparated. With at most three hypotheses, a separating family contains a fixed separating subset of at most two tests; adaptive depth one would itself be one separating fixed test. Thus four is minimal under this contract, giving W18.

For robust pairwise ambiguity, define an edge when two states' feasible observation sets are disjoint. A group allowed to share a message cannot contain an edge; the minimum pairwise grouping count is the chromatic number. Under independent product observations, distinguishability graphs unite. On three vertices take $A$ to reveal edge 12, let $B$ also reveal edge 23, and let $v$ reveal edge 13. Adding $v$ leaves $\chi(A)=2$ unchanged but increases $\chi(B)$ from two to three. With at most two vertices this is impossible. This gives W17 for the explicitly pairwise grouping objective. Every finite graph can be realized by feasible sets using a shared token for each nonedge and a private token for each vertex.

These thresholds, three for robust pairwise complementarity, four for adaptive worst-case test count, and five for exact quotient-width complementarity, concern different optimization contracts. Their comparison is useful only when those contracts remain visible.


# Robust ambiguity and fragmented realizations

## A nerve replaces an invalid quotient

Let each state $x$ have a nonempty feasible observation set $\Omega(x)$. Pairwise overlap is reflexive and symmetric but can fail transitivity: $\{a\}$, $\{a,b\}$, and $\{b\}$ overlap consecutively, while the first and last are disjoint. It therefore cannot generally serve as exact equivalence.

The complete finite joint-ambiguity object is the nerve

$$\mathcal N=\{F\subseteq X:\bigcap_{x\in F}\Omega(x)\ne\varnothing\}.$$

The empty face is included by convention. Minimal nonfaces form an obstruction hypergraph. A set of states can share one feasible observation exactly when it contains no minimal nonface. Consequently partitioning states into jointly confusable cells is equivalent to weakly coloring this hypergraph, where no obstruction edge may be monochromatic. This is a grouping problem, not automatically a decoder that identifies the true state.

Pairwise tests lose information about higher intersections. The three sets $\{a,b\}$, $\{b,c\}$, and $\{a,c\}$ intersect pairwise but have empty joint intersection. Their pairwise graph alone cannot identify the triple obstruction.

For independently combined product observations, $\Omega_{A\cup B}(x)=\Omega_A(x)\times\Omega_B(x)$, so $\mathcal N_{A\cup B}=\mathcal N_A\cap\mathcal N_B$. Independence of this set-product model is a hypothesis; arbitrary correlated feasible observations need their own joint set.

For pure complete $h$-uniform obstruction hypergraphs on $n$ vertices, each color class can contain at most $h-1$ vertices. The minimum number of colors is therefore $\lceil n/(h-1)\rceil$, attained by grouping vertices in blocks of that size. Thus $k(h-1)+1$ is the first number forcing $k+1$ colors. This is the elementary coloring content of W19.

## Task identification can change geometry

For a task map $\tau:X\to T$, define the task complex as the simplicial image $\tau(\mathcal N)$. A coherent representative section is a map $s:T\to X$ with $\tau s=I_T$ and $s(F)\in\mathcal N$ for every task face $F$.

Such a section exists exactly when choices of representative lifts on all maximal task faces can be made to agree on every overlap. Necessity is restriction of a global section. Sufficiency is well-defined assembly of the compatible local choices. With a coherent section, the task complex is precisely the induced source complex on the selected representatives; therefore any source convex realization restricts to one for the task complex. Unique-continuation or holonomy language requires additional bijective transport data and is not supplied merely by the existence of local lifts.

Without a section, complexity can increase. For any finite complex $L$, take one disjoint full simplex for each maximal face and give each occurrence of a vertex its own source copy. Realize the source simplices by groups of coincident intervals placed in disjoint regions of a line. Identify the copies with their task vertex. The task image is exactly $L$. Thus even one-dimensional source geometry can produce arbitrarily complicated task geometry.

Only two source representatives per task can already suffice for unbounded convex-realization dimension. For $m\ge3$ and task vertices $1,\ldots,m$, define

$$U_i=[1,i-1]\cup[i+1,m],$$

omitting intervals whose left endpoint exceeds their right endpoint. Every proper subfamily intersects: if index $j$ is absent, the point $j$ lies in every remaining $U_i$. The full intersection is empty. The nerve is the boundary of an $(m-1)$-simplex. Take the one or two interval components as separate source representatives and identify them with their task vertex. The source is an interval nerve and every task fibre has size at most two. Helly's theorem forces task convex-realization dimension at least $m-1$; the facets of an $(m-1)$-simplex attain it. Multiplicity one is only a relabeling and cannot produce this increase. This proves the scoped W22 threshold.

## Fragmentation breadth and depth

For a finite complex with no ghost vertices, represent each task vertex $v$ by a nonempty finite union of intervals $U_v$ whose nerve is exactly the complex. Let $c_v$ be its component count. Define

$$\phi_1=\min\#\{v:c_v>1\},\qquad
\delta_1=\min\sum_v(c_v-1).$$

The first quantity counts fragmented states; the second counts extra components. These are distinct optimization problems.

If the maximal faces are ordered as $F_{\pi(1)},\ldots,F_{\pi(n)}$, let $b_\pi(v)$ be the number of consecutive blocks of faces containing $v$. Then

$$\phi_1=\min_\pi\#\{v:b_\pi(v)>1\},\qquad
\delta_1=\min_\pi\sum_v(b_\pi(v)-1).$$

**Proof of the ordering characterization.** Given an interval-union realization, choose a witness point for every maximal face. Two distinct maximal faces cannot share a witness, since then their union would also be a face. Order these witness points. The witnesses belonging to any component of $U_v$ occur consecutively among the selected points that component contains, so $b_\pi(v)\le c_v$. This proves lower bounds by ordering.

Conversely place the maximal-face witnesses at consecutive integers. For each row take one closed interval spanning each consecutive block of its witness indices. At an integer the active vertex set is the corresponding face. Between consecutive integers it is contained in the intersection of the neighboring faces. No extra face is created, and each maximal face is witnessed. Each row has exactly its block count of components. This proves attainment in the interval model and both identities.

Thus $\phi_1$ is exactly minimum row deletion to restore the consecutive-ones property: remove the fragmented rows of an order, or insert any deleted rows back into an order for the others. The depth objective is consecutive block minimization minus the number of nonempty rows. These are established ordering problems, not new fields invented by BM [HaddadiLayouni2008]. For an arbitrary labeled binary matrix the same objectives can be studied directly; identifying them with a complex requires using its maximal-face incidence matrix.

## A topological lower bound

Fix a coefficient field. A complex is $d$-Leray when every induced subcomplex has zero reduced homology in every dimension at least $d$.

**W23.** The nerve of a finite family of subsets of a linearly ordered space, at most $s$ of which fail order convexity, is $(s+1)$-Leray.

**Proof.** For $s=0$ the nerve is an interval nerve and is 1-Leray. This remains true on an arbitrary ordered space: choose finitely many intersection witnesses, restrict to that finite order, and realize the resulting consecutive subsets by intervals. Their nerve is unchanged. Interval nerves are clique complexes of chordal graphs and have no positive-dimensional reduced homology on any induced subcomplex.

For $s>0$, choose one nonconvex set $U$. Deleting its vertex leaves at most $s-1$ nonconvex sets. Its link is the nerve of the other sets intersected with $U$, considered in the induced order on $U$. Every formerly order-convex set remains order convex there, so the link also has at most $s-1$ exceptions. By induction both deletion and link are $s$-Leray. The decomposition into deletion and the cone on the link, with their intersection the link, gives the reduced homology exact sequence. In dimensions $i\ge s+1$, the deletion's $i$-homology and the link's $(i-1)$-homology vanish, hence so does the whole complex's $i$-homology. Apply this argument to every induced subcomplex. This proves the claim.

The deletion-link method is standard topology; the scope here is the ordered-set fragmentation formulation. The interval-union construction above has $s=m-2$ fragmented members and simplex-boundary Leray number $m-1=s+1$, proving sharpness. In particular

$$\phi_1(L)\ge L_\mathrm{Leray}(L)-1.$$

This is a lower bound on breadth. It is not a bound on the number of components of an individual fragmented state. General representability and Leray theory have substantial prior art [KalaiMeshulam2007; KimLew2023].

## All breadth and depth pairs

Every order obeys $B\le D$, where $B$ counts rows with more than one block and $D$ sums excess blocks. Hence $\phi_1\le\delta_1$, and $\phi_1=0$ exactly when $\delta_1=0$.

For every integer $m\ge1$ there is an example with $(\phi_1,\delta_1)=(1,m)$. Use $2m+1$ columns, one row of odd columns, and $m+1$ distinct copies of each adjacent path row $\{i,i+1\}$. Natural order breaks only the odd row into $m+1$ blocks, giving breadth one and depth $m$. Any order breaking a path adjacency breaks all its $m+1$ copies, so its depth exceeds $m$. Preserving every path adjacency forces natural or reversed order, where the odd row is fragmented. This proves the exact values.

For systems on disjoint row and column sets, concatenate their column orders to attain the sums of both optima. Conversely deleting the other system's columns cannot increase any row's block count; restriction proves matching lower bounds. Thus both optima add under disjoint union. Combining $(1,d-k+1)$ with $k-1$ copies of $(1,1)$ realizes every integer pair $1\le k\le d$. These and $(0,0)$ are precisely the universally possible pairs, proving W29 and W30.

Equality $\delta_1=\phi_1$ holds exactly when some breadth-optimal order gives every fragmented row exactly two blocks. Each fragmented row costs at least one excess block; equality forces and is forced by this condition. This proves W31.


# The unbounded cost of minimum fragmentation breadth

## The exact Pareto problem

For a binary matrix with no empty rows and a column order $\pi$, write

$$B(\pi)=\#\{v:b_\pi(v)>1\},\qquad
D(\pi)=\sum_v(b_\pi(v)-1).$$

Define $\phi=\min B$, $\delta=\min D$, and

$$D_k=\min_{\pi:B(\pi)\le k}D(\pi),$$

with value $+\infty$ if no order is feasible. The finite part of $D_k$ is a nonincreasing integer staircase. If $k_\delta$ is the least breadth among globally depth-optimal orders, then $D_k=\delta$ exactly for $k\ge k_\delta$, and $\phi\le k_\delta\le\delta$.

For disjoint systems,

$$D_k(M\sqcup N)=\min_{i+j\le k}\bigl(D_i(M)+D_j(N)\bigr).$$

Restriction of any order supplies the lower bound; concatenating feasible orders supplies the upper bound. This is the min-plus composition law W32. It depends on the specified independence of rows and columns.

## W35 and its complete construction

Suppose $n\ge5$. Use columns $1,\ldots,n$, the $n-1$ path rows $P_i=\{i,i+1\}$, and $k=n-4$ distinct rows with the same odd-column support $O=\{1,3,5,\ldots\}$. Identical supports are distinct labeled rows and each contributes to the declared cost.

For an order $\pi$, let $a$ count broken path adjacencies and let $r$ be the odd-row block count. Direct counting gives

$$B=a+k\mathbf1_{r>1},\qquad D=a+k(r-1).$$

**Breadth optimum.** Natural or reversed path order has $a=0$, $r=\lceil n/2\rceil$, and $B=k$. If $r=1$, all odd columns are consecutive. A path edge joins odd to even and can survive only at one of the two boundaries of this odd block. At most two path edges survive, so $a\ge n-3>k$. If $r>1$, then $B=a+k\ge k$. Thus $\phi=n-4$.

Attaining $B=k$ forces $a=0$. An order preserving all edges of a path is its natural order or reversal: its $n-1$ consecutive column pairs must be exactly those path edges. Hence

$$D_\phi=(n-4)(\lceil n/2\rceil-1).$$

**Global depth optimum.** Place all odd columns in one block, with column 2 immediately before column 1 and an even neighbor of the final odd column immediately after the block. Put all other even columns outside it. For $n\ge5$ the two boundary even columns can be chosen distinct. Exactly two path edges survive, so $r=1$, $a=n-3$, and $D=n-3$.

Conversely, if $r=1$, the same boundary argument gives $D\ge n-3$. If $r>1$ and $a\ge1$, then $D\ge1+k=n-3$. If $r>1$ and $a=0$, natural order gives $D=(n-4)(\lceil n/2\rceil-1)\ge n-3$. Therefore $\delta=n-3$.

For $\delta>0$ the multiplicative price of insisting on minimum breadth is consequently

$$\boxed{\frac{D_\phi}{\delta}
=\frac{(n-4)(\lceil n/2\rceil-1)}{n-3}.}$$

It tends to infinity and is asymptotic to $n/2$. The former universal $3/2$ conjecture is false.

## The finite-column ceiling

A binary row in $n$ columns has at most $\lceil n/2\rceil$ blocks. A breadth-optimal order fragments exactly $\phi$ rows, each contributing at most $\lceil n/2\rceil-1$ excess blocks. Since $\delta\ge\phi$,

$$\frac{D_\phi}{\delta}\le\lceil n/2\rceil-1\qquad(\delta>0).$$

The construction attains the fraction $(n-4)/(n-3)$ of this ceiling. Its relative efficiency tends to one. Thus the result gives both unboundedness and the sharp asymptotic scale in the number of columns. If $\delta=0$, then $D_\phi=0$ and the ratio is undefined, not an infinite obstruction.

| Columns | Minimum breadth | Minimum depth | Depth at minimum breadth | Ratio |
|---:|---:|---:|---:|---:|
| 5 | 1 | 2 | 2 | 1 |
| 6 | 2 | 3 | 4 | $4/3$ |
| 7 | 3 | 4 | 9 | $9/4$ |
| 8 | 4 | 5 | 12 | $12/5$ |
| 9 | 5 | 6 | 20 | $10/3$ |

![The W35 construction compares minimum breadth with minimum depth on the same eight-column matrix. Rows with identical support remain distinct tasks.](figures/fragmentation_orders.png){width=95%}

The $n=6$ instance has efficient endpoints $(B,D)=(2,4)$ and $(3,3)$. Disjointly combining $m$ copies produces an additive price $D_\phi-\delta=m$, proving W34. These results concern the breadth-constrained objective. A 1.5 approximation for ordinary total block minimization says nothing by itself about this ratio. The underlying consecutive-ones and block-minimization problems are established prior art; the historical priority of this particular bicriteria construction remains unconfirmed.

## An exact finite algorithm

Exhaustive enumeration of column permutations computes the full Pareto curve and provides a witness order for every efficient point. The accompanying implementation uses reversal symmetry and verifies the construction for $n=5,\ldots,9$.

A second exact algorithm uses partial orders. Its state is a subset of placed columns, the last placed column, and the vector of row block counts. Appending column $j$ adds one to row $v$ precisely when its new entry is one and its previous last entry was zero, with a zero sentinel before the first column. Future increments depend only on the last column and the appended suffix.

At equal placed subset and last column, discard a block-count vector if another retained vector is coordinatewise no larger. Any common suffix adds the same increments to both, so the dominating vector remains no worse in both final breadth and final depth. Store a witness prefix for each retained vector. At full subsets, evaluate $(B,D)$ and discard dominated outcomes. Induction on prefix length proves that every achievable Pareto optimum has a retained witness.

The algorithm is finite and exact; the number of retained vectors can still be exponential. No polynomial-time claim is made. It is useful for auditable small instances and for checking purported general constructions. The delivered code compares its full frontier with independent permutation enumeration on the six-column instance.

The practical lesson is specific: a cost that counts how many tasks are split can select a very different interface from a cost that counts all extra pieces. A deployment must specify both costs, or explicitly justify ignoring one.


# GURF response mathematics

## Core response contract

GURF means General Unified Response Framework. A response problem declares a state carrier $X$, native response law or relation, retained observation $R$, task family $\mathscr Q$, applicability and acceptance predicates, context, interventions, and requested evolution. A deterministic response is a function; a nondeterministic response is a relation; a stochastic response is a kernel. These declarations determine which theorem applies.

For observations $r_\alpha$ and observed values $\ell_\alpha$, the completion fibre is

$$\mathfrak C_A(\ell)=\bigcap_{\alpha\in A}r_\alpha^{-1}(\ell_\alpha).$$

An empty fibre means the observation is unrealizable in the declared model. A nonempty fibre gives exact recovery of a task precisely when its task image is a singleton. A unique fitted optimizer does not establish this condition: regularization can select one point from an ambiguous fibre without making it identifiable.

For $T:X\to(W,d)$ and nonempty fibre $F_z$, the task diameter is $\operatorname{diam}T(F_z)$. The best unrestricted decoder is governed by the fibre's enclosing radius. For bounded real tasks, a midpoint of infimum and supremum attains half the diameter. Stability against perturbations of the observation requires a separate estimate between different fibres.

### Three independent defects

For a relation $\mathcal E\subseteq X\times X$, put $Q(x)=R(\mathcal E[x])$. Task collision after evolution concerns distinct source tasks whose possible observations overlap:

$$\operatorname{Col}_{\mathcal E,R,T}=\{(x,x'):T(x)\ne T(x'),\ Q(x)\cap Q(x')\ne\varnothing\}.$$

Closure failure concerns identical current observations with different reduced successor sets:

$$\operatorname{ClDef}_{\mathcal E,R}=\{(x,x'):R(x)=R(x'),\ Q(x)\ne Q(x')\}.$$

Interaction failure concerns input tuples with identical interfaces but different task-relevant outputs or applicability. These answer different questions. The collision relation need not be transitive: the sets $\{a\},\{a,b\},\{b\}$ overlap successively while the first and last are disjoint. Thresholding a metric by $d\le\varepsilon$ also need not define an equivalence.

## SOE Structured Operations Extension

SOE tracks operation type, domain, order, provenance, and handoff. For partial maps $f:D_f\to Y$ and $g:D_g\to Z$, composition has domain $D_f\cap f^{-1}D_g$. Order matters: $f(x)=x+1$, $g(x)=2x$ give $gf(x)=2x+2$ and $fg(x)=2x+1$. An order defect is meaningful only when both expressions are defined and compared in the same space.

An adaptive operation must include the state that determines its choice. REBIND is a declared change of binding or context followed by an audit; it has no universal algebra without specifying the native operation. Feedback wiring must say whether it denotes a fixed point, delayed recursion, relation, or another construction. For $x_{n+1}=ax_n+b$, $|a|<1$ gives the fixed point $b/(1-a)$ and exact error $a^n(x_0-b/(1-a))$. For $a=1,b=1$ there is no fixed point. Existence, uniqueness, stability, and selection are separate claims.

## ACE Admissibility and Constraints Extension

ACE intersects declared constraints and distinguishes static feasibility from trajectory invariance. If $A=\bigcap_j A_j$, nonempty individual $A_j$ do not imply nonempty $A$. A scalar violation function, feasibility margin, penalty, or convexity hypothesis must be supplied explicitly; none follows from naming a constraint soft or hard.

For a closed set $A$ in Euclidean space and a locally Lipschitz vector field on an open neighborhood, the appropriate tangent-cone invariance theorem can establish forward invariance on the solution's interval of existence. In the regular scalar case $A=\{g\le0\}$ with $g\in C^1$ and $\nabla g\ne0$ at every boundary point, the tangent condition is $\nabla g(x)\cdot f(x)\le0$ on the boundary. It must hold throughout the relevant boundary, with the native existence and invariance hypotheses.

The regularity assumption is essential: $g(x)=x^3$, $A=(-\infty,0]$, $f(x)=1$ satisfies $g'(0)f(0)=0$, yet the trajectory starting at zero leaves $A$ immediately. For relations, weak viability means some successor stays in $A$; strong invariance means every successor stays in $A$. Requiring nonblocking adds a separate nonempty-successor condition.

## IRE Inverse Recovery Extension

IRE uses feasible inverse families, task identifiability, and reconstruction stability. For linear $H:V\to Y$ and linear task $L:V\to W$,

$$L\text{ factors through }H\quad\Longleftrightarrow\quad\ker H\subseteq\ker L.$$

Indeed $Hx=Hx'$ iff $x-x'\in\ker H$; apply T01. On Euclidean spaces, the minimum-norm inverse on $\operatorname{ran}H$ has norm $1/\sigma_{\min}^+(H)$ when $H\ne0$. This follows by expanding in singular vectors. The nullspace determines exact ambiguity, while small positive singular values determine instability. Neither a small residual nor a unique regularized minimizer eliminates nullspace ambiguity.

Example: $H(x_1,x_2)=x_1$. The task $L=x_1$ is identifiable and the task $L=x_2$ is not. A regularizer selecting $x_2=0$ changes the selected completion; it does not prove that the true unobserved coordinate is zero.

## UKE Unified Kernel Extension

UKE retains the distinction between a linear nullspace, integral kernel, Green function, resolvent, reproducing kernel, spectral kernel, and memory kernel. These are established and different constructions. An integral response $y(t)=\int K(t,s)x(s)\,ds$ requires an integration domain, function spaces, and boundedness or convergence assumptions. A resolvent $(\lambda I-A)^{-1}$ exists only on the resolvent set; a Green function also needs the operator, boundary or initial conditions, and solution class.

A concrete memory kernel permits an exact state augmentation. Let $\beta>0$, let $x$ be continuous, and define

$$m(t)=e^{-\beta t}m_0+\int_0^t e^{-\beta(t-s)}x(s)\,ds.$$

Differentiating the integral yields $\dot m=-\beta m+x$, $m(0)=m_0$. Conversely multiplying this ODE by $e^{\beta t}$ and integrating gives the formula. Thus a response depending on this exponential memory can use the augmented state $(x,m)$. Arbitrary memory kernels need not admit a finite-dimensional exact augmentation.

## GRDE Diagrammatic Response Extension

GRDE remains frozen at GURF-GRDE-008. Existing diagrams describe declared response structure and provenance. This edition introduces no new GRDE axioms or approved structural iconography. A diagram records maps and obligations; it does not prove they exist, commute, or have limits. Any accompanying visual model must specify its native coordinate calculation; an animation cannot establish a Root or candidate Seed construction.

## HDE Halo Domain Extension

HDE represents response-relevant state beyond a chosen primary domain. The extension can be spatial, hidden-state, environmental, or historical. Write the extended state as $(x,h)$, local observation $R(x,h)=x$, and evolution $F(x,h)=(f(x,h),g(x,h))$. A local autonomous evolution exists exactly when $f(x,h)$ is independent of $h$ on each admissible local fibre, together with domain saturation if partial. This is T11, not a new physical force.

For a history space $\mathcal H$, current-state map $\pi$, and declared future-response object $\mathcal F$, memory failure is

$$\operatorname{MemDef}=\{(h,h'): \pi(h)=\pi(h'),\ \mathcal F(h)\ne\mathcal F(h')\}.$$

The finite synthesis theorem computes a coarsest exact history partition when a finite history-state model and transitions are supplied. It does not discover a finite Markov state for every continuum history process. For the exponential example, two histories with the same $x(t)$ but different $m(t)$ can have different future response, so retaining $m$ repairs that particular defect.

## GHSE Glue Hold State Extension

GHSE handles joining, holding, and release under native rules. A held record is sufficient for release only if histories it identifies give the same declared release task and availability. For example, let a joined spring have state $(q,v,k)$ and hold observation $h(q,v,k)=q$. A release task asking energy $E=(v^2+kq^2)/2$ is generally not determined by $q$. The stored velocity and stiffness, or a sufficient combination, must be supplied if the release task needs them. No additional energy is inferred from the act of naming a joined state.

A hysteresis model requires a mode variable and switching thresholds. With thresholds $a<b$, a binary mode can remain unchanged for inputs in $(a,b)$; omitting it makes the same current input compatible with distinct future outputs. HDE and GHSE share the same exact refinement theorem when their state and release semantics meet its hypotheses.

## Composition and sector boundaries

Every cross-extension use must state the shared carrier, the interface, which witnesses are reused, and the native composition law. For a relation, $\Diamond_R(U)$ means some successor lies in $U$, while $\Box_R(U)$ means every successor lies there. A dead end satisfies ordinary $\Box_R(U)$ vacuously. The nonblocking predicate $\operatorname{Dom}(R)\cap\Box_R(U)$ has different composition behavior.

For an imported finite Markov kernel, closure means equality of aggregated transition probabilities, not merely equality of supports or means. A coupling must be given if joint behavior matters. Privacy guarantees use their declared divergences and adjacency relation and are not exact quotient equivalences. Quantum physical recovery must meet complete positivity and trace preservation; algebraic inversion of a known output matrix is a different task.

# Physical interpretation and its limits

## Information as lawful distinction

The operational meaning of information in this book is the distinctions required by a declared family of tasks and continuations. For exact deterministic tasks it is expressed by a kernel intersection. For metric tasks it can be expressed by a profile distance or covering number. For quantum tasks it can be expressed by an observable system, an algebra, and a physical recovery requirement. These objects are related by explicitly typed constructions, not by identifying them with one universal substance.

If complete evolution $\Phi_t$ is injective, distinct complete states remain distinct at that time. Conversely, if $\Phi_t$ maps two different states to one state, a task distinguishing the original pair cannot be recovered from that state alone. This is exactly the factorization obstruction. Bijective evolution permits set-level recovery using its inverse; stability of that inverse is an additional issue.

Injectivity is a property to establish for a supplied dynamical model. Merely calling a system closed does not prove it. A conservation assumption may be entered into a Branch Passport, but its consequences must remain conditional until the underlying dynamics is justified. The heat example demonstrates finite-time injectivity with unbounded inverse and a many-to-one infinite-time limit. It prevents confusing distinction preservation, stable access, and limiting behavior.

## Fields energy and particles need native structure

A field model first supplies a base space, a value space or bundle, admissible sections, and equations or an action. A task may ask for local field values, relational quantities, or global holonomy. BM can test whether an observation preserves those tasks; it cannot infer the base space or field equation from an equivalence relation alone.

Energy requires additional structure. In a Hamiltonian model, the symplectic structure and Hamiltonian determine time evolution. The oscillator Hamiltonian $H=(p^2+\omega^2q^2)/2$ gives a familiar example. Multiplying it by a positive constant rescales its generated time rate while preserving many of the same state-distinction relations. Thus distinguishability alone does not determine an energy scale or physical time unit.

Particles likewise require a specified quantum or classical excitation theory. An excitation that persists under a receiver's perturbation tests is a possible BM task object; persistence alone does not identify an elementary particle or derive its mass, spin, or statistics. Standard quantum field theory attaches particle interpretations to additional spectral, symmetry, and asymptotic hypotheses [TongQFT]. The project phrase "persistent recoverable excitation sector" should therefore be treated as a proposed organizing description, not a universal particle-definition theorem.

## A rigorous energy-only obstruction for fluid motion

Use the periodic torus with normalized volume, viscosity $\nu>0$, no forcing, and smooth incompressible shear solutions

$$u_k(x,y,z,t)=A e^{-\nu k^2t}\sin(ky)\,e_x,
\qquad k=1,2,\ldots.$$

The divergence is zero. Since the velocity points in the $x$ direction and is independent of $x$, $(u_k\cdot\nabla)u_k=0$. The Laplacian is $-k^2u_k$, so the displayed field solves the Navier-Stokes equation with constant pressure. Its kinetic energy is

$$E_k(t)=\tfrac12\|u_k(t)\|_2^2
=\frac{A^2}{4}e^{-2\nu k^2t}.$$

All these solutions have the same initial energy, but their initial energy derivatives are $-2\nu k^2E_k(0)$. Their energies at any fixed positive time also differ. Hence no autonomous deterministic energy-only update can reproduce all these flows. The obstruction is already present among explicit globally smooth solutions. It establishes missing information in a particular representation, not singularity formation or failure of every energy-based analysis.

The smooth periodic energy identity T34 remains valid on the existing smooth interval. It controls an integral quantity and does not by itself control every derivative or pointwise value needed for continuation. Higher strain, gradient, spectral, and phase observables can refine a task profile, but a finite list is not automatically dynamically closed.

As of the date of this edition, OpenAI's 8 September 2026 announcement reports a forced finite-time singularity construction addressing versions C and D of the Millennium formulation and links a writeup and Lean formalization [OpenAI2026]. The current Clay page labels the problem active [ClayNS]. Those external reports are not a BM proof and their linked proof artifacts were not independently verified for this edition. The book's fluid theorems are stated directly and do not depend on an unreviewed promotion of that announcement to a broader result.

## Gauge and spectral obligations

The finite Wilson-loop identity T35 proves gauge invariance of a specified trace. It does not supply a continuum quantum Yang-Mills construction or a positive mass gap. Clay's current Yang-Mills page still identifies that problem as unsolved [ClayYM].

In finite-dimensional spectral work, enlarging a trial space improves individual Rayleigh-Ritz upper bounds. Differences between two such approximate eigenvalues need not vary monotonically and are not automatically lower bounds on the true gap. A positive variational number alone cannot close the Yang-Mills program.

A useful conditional finite-block statement is the Schur complement. For a self-adjoint block matrix

$$H=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad D-zI\succ0,$$

one has $H-zI\succ0$ exactly when

$$A-zI-B(D-zI)^{-1}B^*\succ0.$$

Complete the square in the quadratic form: replace the second vector $y$ by $y+(D-zI)^{-1}B^*x$. The remaining term is the displayed Schur complement. This shows explicitly why a large diagonal block alone cannot certify positivity when coherent off-diagonal return is uncontrolled. Infinite-dimensional operator domains, gauge constraints, thermodynamic limits, and a continuum construction require separate analysis.

## The fundamental-interaction carrier architecture

For supplied laws on $X_\mathrm{raw}$, let $A$ be the admissible set. Let $\sim_G$ be a lawful redundancy equivalence preserving $A$, and require the receiver tasks to be invariant under it. Then the deterministic exact sequence is

$$A\hookrightarrow X_\mathrm{raw},\qquad
A\longrightarrow A/{\sim_G}\longrightarrow(A/{\sim_G})/{\sim_T}.$$

The inclusion arrow is intentional. Enforcing admissibility selects a subset; it does not generally define a canonical function from every raw state to a lawful state. The later arrows are quotient maps. Any exact task carrier factors to the final task quotient by T01. This is the precise content retained from FI42.

The FI audit identifies useful obstructions: local curvature need not determine holonomy; a finite correlator hierarchy need not determine higher correlations; Ricci data need not determine Weyl data; finite effective-theory moments need not determine a general ultraviolet completion; and geometry alone need not determine a quantum-state-dependent mean source. Each uses supplied native assumptions. None of FI01-FI42 is presented as a historically new fundamental interaction or particle prediction.

## Distinction Dynamics as a continuing program

The term predictive interior is realized rigorously here by $I_U(E)$, the greatest continuation-stable equivalence inside $E$. Typed route defects can be studied only after the route domains and comparison outputs are fixed. Protection and access questions have concrete realizations in the authorization hypergraphs and channel-recovery defects above.

The broader Distinction Dynamics development, including the separately numbered DD sequence, remains a research program. A public theorem requires its actual native statement and proof. An interpretation that information creates a field, energy scale, or particle must provide the additional construction and a testable model consequence. This book does not infer such claims from terminology or from the existence of a task quotient.


# What is established and what remains open

## The defensible contribution

BM provides a typed way to organize reductions, interactions, continuation, realization, and receiver acceptance. Its strongest arguments in this edition have observable mathematical consequences: a coarsest finite exact interface, a failure of a coarsest smooth submersion, a sharp scalar closure price, a uniform evolved-coordinate repair for a specified heat cascade, a physical quantum closure criterion, an explicit approximate-algebra obstruction, and the unbounded W35 fragmentation tradeoff.

These are sufficient subjects for a serious research exposition. They do not establish that every component is historically new or that BM outperforms mature native methods on applications. A framework's value must be assessed with actual problems, retained hypotheses, reproducible implementations, and comparisons.

The finite exactification algorithm should be compared against stable partition refinement, bisimulation, and constrained lumping. The representation optimization should be compared against low-rank approximation and invariant-subspace methods. The port and causal chapters should be compared against model reduction and realization theory. The quantum chapters should be compared against OAQEC and approximate recovery. The fragmentation problem should be compared against consecutive-ones and block-minimization algorithms. Those comparisons preserve the native mathematics instead of using a vocabulary change as evidence of novelty.

## A scoped completion table

The following table and questions record the earlier release. The 18–19 October development in the final chapter supplies updated dispositions, including resolved finite correlated-context and fragmentation contracts.

| Question | Result in this edition | Remaining boundary |
|---|---|---|
| Exact deterministic future interface | Greatest stable equivalence with a full proof | Native regularity and computation on infinite presentations |
| Finite interacting interfaces | Coarsest family under Cartesian substitution | Correlated contexts and restricted deployment architectures |
| Regular realization | Compact Hausdorff result and local smooth rank bound | General sharp global smooth classification |
| Exact closure price | Sharp shear and Jordan current-output results | Smaller-code nonlinear Jordan trajectory optimum |
| Conditioned repair | Linear invariant-graph theorem; coupled continuous and triangular C1 nonlinear repair with explicit bounds in the 15 October addendum | Arbitrary dynamics outside the hypotheses and globally optimal encoder/repair cost |
| Finite weighted projector optimization | General rational epsilon-optimal projector and matching global bounds in the closing addendum | Potentially enormous enumeration; efficient algorithms and general closed forms not established |
| Infinite-dimensional smoothing | Specified positive heat cascade and profile bounds | General nonlinear PDE closure theory |
| Physical quantum closure | Finite Choi feasibility | Infinite-dimensional channels and uniform construction cost |
| Approximate quantum recovery | Finite Kraus rank bound and explicit no-greatest example | Sharp bounds for the original normalized defect and general capability geometry |
| Fragmentation tradeoff | Unbounded ratio with asymptotically sharp construction | Efficient full-frontier computation and application benchmarks |
| Fundamental physics | Scoped examples and source audit | No new physical law established by this book |

## Open problems stated as actual tasks

**Nonlinear Jordan trajectory optimum.** Fix a nonzero coupling, a finite horizon, the unit-ball performance set, global continuous encoders into $\mathbb R^d$, and exact sampled autonomy. For $1\le d<n-1$, determine the full trajectory-error optimum. The constant-mode lower bound and the linear upper bound do not settle this range.

**Global regular realization.** Given a specific smooth source, future observation family, target class, and legacy map, determine the least augmentation dimension or prove nonexistence. Local differential rank does not remove bundle or singular-quotient obstructions.

**Restricted contexts.** Replace independent Cartesian substitution by a fixed correlated reachable context set. Characterize which closure properties of that set preserve a greatest admissible family, and when different interfaces become incomparable.

**Approximate causal composition.** Determine when a sequence of near-optimal profile covers can be equipped with common causal update maps at controlled additional cost. Independent minimum covers need not compose.

**Quantum recovery constants.** For a fixed algebra and a controlled Kraus or environment class, improve the conservative $2r\sqrt\kappa$ estimate, determine sharp examples, and separate discontinuities in the normalized operator system from continuity in physical recovery error.

**Fragmentation complexity.** Determine the complexity of computing the full function $k\mapsto D_k$, and useful parameterizations by column count, row patterns, or allowed breadth. The exact algorithm here establishes computability for finite tables, not efficient general solvability.

**External novelty.** Complete a theorem-by-theorem search for the exact W06, W08, W23, W35, and closure-price statements, including equivalent formulations outside BM terminology. Absence of a match in the targeted searches recorded here is not a priority certificate.

## Validation that would change the release assessment

An independently checked proof or formalization would strengthen the reliability of a selected theorem. A reproducible benchmark against an established method could establish practical value. A completed reduction to prior art would refine the novelty classification without invalidating a useful exposition. A counterexample would force a versioned correction rather than silent editing of the frozen foundation.

For a physical application, the next step is a specified observable, intervention, parameter range, and falsifiable comparison with data or an accepted native model. The present book establishes mathematical representation results. It supplies no experimental evidence for a new fundamental ontology.

# Prior art and attribution

The exact task quotient is an elementary factorization construction. Adding all continuations gives a behavioral equivalence with close counterparts in automata, observability, and bisimulation. The complete-lattice argument is an application of Tarski's fixed-point theory [Tarski1955]. Finite interface refinement belongs to the partition-refinement tradition [PaigeTarjan1987; RanzatoTapparo2007], and constrained observable reduction already has implementations such as CLUE [Ovchinnikov2021].

The weighted reconstruction result uses the classical low-rank approximation theorem [EckartYoung1936]. The continuous width lower bounds use Borsuk-Ulam [Borsuk1933]. The conditioned repair uses Sylvester equations, Riccati graph equations, and the contraction principle. Presenting them in a BM Passport does not transfer authorship of those methods to BM.

The quantum exact-algebra criterion is OAQEC [BenyKempfKribs2007]. The recovery upper bound used here is from approximate algebra correction [Beny2009]. Choi feasibility is a direct channel characterization [Watrous2018]. The new explicit calculations in this edition are consequences in that established setting.

Nerves, Helly theory, Leray numbers, and convex representability have established geometric and topological foundations [KalaiMeshulam2007; KimLew2023]. Consecutive block minimization and its approximation literature predate this project [HaddadiLayouni2008]. The W35 ratio compares two objectives and should be assessed against bicriteria variants, not claimed as the invention of either endpoint problem.

The targeted reference checks establish important overlaps. They do not amount to a complete literature review across all BM branches. The source registries therefore keep mathematical validity and historical novelty as separate fields.


\appendix

# Canonical supporting proofs T01 to T55

Stable IDs retain their identity. A corollary, counterexample, or governing restriction is labelled as such rather than counted as an independent deep theorem. All proofs are mathematical arguments within the hypotheses below; no machine-checked or historical-novelty claim is made. The principal combined developments appear in the preceding chapters.

## T01 Exact fibre factorization {#T01}

**Classical theorem.** For functions $R:X\to Z$ and $T:X\to W$, there exists a unique $D:R(X)\to W$ with $DR=T$ iff $R(x)=R(x')$ implies $T(x)=T(x')$.

**Proof.** Factorization implies the implication by substitution. Conversely, for each realized $z$, the values $T(x)$ with $R(x)=z$ form one singleton; define $D(z)$ to be its unique element. This is independent of any representative, gives $DR=T$, and forces uniqueness on $R(X)$. Empty unrealized fibres are outside that domain. No regularity of $D$ follows. $\square$

## T02 Passport sufficiency {#T02}

**GURF corollary.** In the deterministic observation sector, let $B_P:X\to Q_P$ collect the specified Passport observations. A task $T$ factors through $B_P$ iff $\ker B_P\subseteq\ker T$.

**Proof.** Substitute $B_P$ for $R$ in T01. This treats the observation part of a Passport, not every possible native contract as a function. $\square$

## T03 Completion fibre sufficiency {#T03}

**GURF corollary.** For a set-indexed family $r_\alpha$ whose product is defined, let $R(x)=(r_\alpha(x))_\alpha$. A task is recoverable exactly when it is constant on every nonempty $\bigcap_\alpha r_\alpha^{-1}(\ell_\alpha)$.

**Proof.** The displayed intersection is precisely $R^{-1}(\ell)$, so T01 applies. For a proposed observation, check nonemptiness separately before reporting a recovered value. $\square$

## T04 Canonical exact task quotient {#T04}

**Classical quotient theorem in BM scope.** For a task family $\mathscr Q$, put $E_{\mathscr Q}=\bigcap_{T\in\mathscr Q}\ker T$. This is the coarsest equivalence whose quotient preserves every task. Any sufficient representation $R$ induces a unique map $h:R(X)\to X/E_{\mathscr Q}$ with $hR=q_{\mathscr Q}$.

**Proof.** Intersections of equivalences are equivalences. Each task is constant on its classes, so T01 gives task factorization. Sufficiency of $R$ implies $\ker R\subseteq E_{\mathscr Q}$; T01 applied to $q_{\mathscr Q}$ gives $h$. Every task-sufficient equivalence is contained in $E_{\mathscr Q}$, proving coarsestness. Structured admissibility is additional. $\square$

## T05 Finite exact carrier bound {#T05}

**Classical counting corollary.** If $X$ is finite and $T=DR$, then $|R(X)|\ge|T(X)|$. Equality within the sufficient class holds iff $R$ and $T$ have the same fibres, equivalently $R=bT$ for a bijection on realized images.

**Proof.** $D:R(X)\to T(X)$ is surjective. Equal finite cardinalities make it bijective; set $b=D^{-1}$. Conversely a bijective relabelling preserves the fibres and cardinality. Merely equal-sized images do not imply sufficiency: $R(a,b)=a$, $T(a,b)=b$ on $\{0,1\}^2$ is a counterexample. $\square$

## T06 Parallel observation refinement {#T06}

**Classical identity.** $\ker(R,S)=\ker R\cap\ker S$ for two functions on the same source.

**Proof.** Ordered pairs are equal iff both coordinates are equal. Thus adding $S$ cannot enlarge an observation fibre. Correlated measurements still require their declared joint domain. $\square$

## T07 Deterministic serial information loss {#T07}

**Classical identity.** For composable total functions $R,S$, $\ker R\subseteq\ker(SR)$. A task that separates an $R$-merged pair cannot be recovered from $SR$ alone.

**Proof.** $R(x)=R(x')$ implies $S(Rx)=S(Rx')$. Apply the necessity direction of T01 to any separating task. An independent side channel changes the observation and is outside this assertion. $\square$

## T08 Structured quotient criterion {#T08}

**Classical congruence theorem.** Let $E$ be an equivalence on $X$ with specified finite-arity partial operations $g:D_g\subseteq X^m\to X$. An exact quotient operation preserving definedness exists for each $g$ iff coordinatewise $E$-equivalent tuples have identical domain membership and, when defined, $E$-equivalent outputs.

**Proof.** Any quotient operation makes both properties necessary because equivalent tuples have the same quotient input. Conversely use the domain membership to define a saturated quotient domain, and define the output to be $[g(x)]$. The second property makes it representative-independent. These constructions work for every declared operation; native continuity or smoothness needs further hypotheses. $\square$

## T09 Typed composite domain {#T09}

**Classical partial-map theorem.** For $f:D_f\subseteq X\to Y$ and $g:D_g\subseteq Y\to Z$, the domain of $gf$ is $D_f\cap f^{-1}(D_g)$, with the preimage evaluated where $f$ exists.

**Proof.** Evaluation requires first $x\in D_f$, then $f(x)\in D_g$; these requirements are also sufficient. For three maps both parenthesizations require exactly the same successive membership tests and give the same value, proving associativity where defined. $\square$

## T10 Future task factorization for a declared evolution {#T10}

**GURF corollary.** For an already-defined total evolution $\Phi_t$, the future task $T\Phi_t$ is recoverable from $R$ iff it is constant on $R$-fibres. For a partial $\Phi_t:D_t\to X$, recovery of both availability and value additionally requires $D_t$ saturated under $R$.

**Proof.** Apply T01 to $T\Phi_t$ in the total case. In the partial case apply it to the total tagged function taking value $(\mathrm{available},T\Phi_t(x))$ on $D_t$ and a distinct unavailable tag elsewhere. Equal tagged values are exactly saturation plus equality on defined pairs. No existence or extension of $\Phi_t$ has been proved. $\square$

## T11 Exact Dynamic Closure {#T11}

**BM and GURF structural specialization.** For total $f:X\to X$, a unique $\bar f:R(X)\to R(X)$ with $Rf=\bar fR$ exists iff $\ker R\subseteq\ker(Rf)$. When it exists, $Rf^m=\bar f^mR$ for every finite $m$. For partial $f$, require domain saturation as well.

**Proof.** Apply T01 to task $Rf$. The finite-iterate identity holds at zero, and $Rf^{m+1}=\bar f Rf^m=\bar f^{m+1}R$ completes induction. Partial closure follows from T10 with task $R$; compose only where successive maps exist. For the canonical task quotient this is exactly congruence of the task equivalence under $f$. $\square$

## T12 Static sufficiency does not imply closure {#T12}

**Counterexample.** On $X=\mathbb R^2$, let $R(x,y)=x$, task $T=x$, and $f(x,y)=(x+y,y)$. $R$ exactly answers the present task but is not dynamically closed.

**Proof.** $T=R$. Yet $(0,0)$ and $(0,1)$ have equal observation and successor observations 0 and 1. T11 fails. $\square$

## T13 Branch essentiality monotonicity {#T13}

**BM proposition.** Fix a candidate class of Branch-removing coarsenings independently of the obligation test. If a Branch is essential for $\mathscr Q$, it remains essential for any $\mathscr Q'\supseteq\mathscr Q$ with the same candidate class.

**Proof.** Every candidate fails some obligation in $\mathscr Q$; that same obligation belongs to $\mathscr Q'$. Quantifying over the unchanged class proves the claim. If the candidate class changes, this argument no longer establishes monotonicity. $\square$

## T14 Refinement and composition {#T14}

**Structural corollary.** Define $R\preceq S$ when $R=hS$ on the source. This relation is reflexive and transitive. If $R$ preserves the source task family and $S$ preserves the induced tasks on $R(X)$, then $SR$ preserves the source tasks.

**Proof.** The identity gives reflexivity and composition of factoring maps gives transitivity. For a source task $T=DR$ and induced task $D=ES$, substitution gives $T=ESR$. Distinguish this composition statement from the notation for comparing two representations on one source. $\square$

## T15 Branch count need not be invariant {#T15}

**Counterexample.** Without a rule forbidding regrouping, a product state $X\times Y$ can be carried by one product Branch or by two Branches with a declared pairing Interaction.

**Proof.** The map $(x,y)\mapsto(x,y)$ is a bijection between the resulting total states and preserves every native product task carried by the pairing. The counts are one and two. Thus raw count is not determined by those total-state semantics. No claim is made for a separately defined irreducible decomposition. $\square$

## T16 Finite tree gluing {#T16}

**Classical gluing theorem.** On a finite tree let node $i$ carry nonempty $A_i$. For every edge $ij$, maps $r_{ij}:A_i\to S_{ij}$ and $r_{ji}:A_j\to S_{ij}$ have equal images. Then a compatible tuple exists, and any chosen value at any one node extends to such a tuple.

**Proof.** Root the tree at the chosen node. Given a parent's value, image equality supplies a child value matching that edge. Choose it and continue away from the root. Finiteness terminates the construction; each edge is checked once and no child has two parents imposing additional conditions. This proves extension and existence. Cycles or cross-obligations require another theorem. $\square$

## T17 Local realizability does not imply global realizability {#T17}

**Counterexample.** The three Boolean constraints $a=b$, $b=c$, $a\ne c$ are each satisfiable, and every pair is satisfiable, but their conjunction is not.

**Proof.** The first two imply $a=c$, contradicting the third. Pairs are witnessed respectively by $(0,0,0)$, $(0,0,1)$, and $(1,0,0)$. This concerns simultaneous feasibility, not transitivity of equality. $\square$

## T18 Finite deterministic DAG evaluation {#T18}

**Classical theorem.** A finite directed acyclic dependency graph with fixed source values and deterministic partial node operations has a unique evaluation if every operation is defined and accepted on its actual predecessor values.

**Proof.** A finite DAG has a topological ordering: repeatedly remove a node with no predecessor; if none existed, following predecessors would eventually form a cycle. Evaluate in this order. Each input was fixed earlier, so each output exists by hypothesis and is unique. Induction proves the entire evaluation. Other topological orders give the same values by the same dependency induction. No infinite-limit conclusion follows. $\square$

## T19 Quantifier scope matters {#T19}

**Counterexample.** $\forall x\in\{0,1\}\ \exists y\in\{0,1\}:y=x$ is true; $\exists y\ \forall x:y=x$ is false.

**Proof.** Choose $y=x$ separately in the first formula. A shared $y$ in the second would equal both 0 and 1. A Passport must specify which witness can be reused. $\square$

## T20 Separate feasibility does not imply joint feasibility {#T20}

**Counterexample.** Nonempty sets $A=\{0\}$ and $B=\{1\}$ have empty intersection.

**Proof.** A joint witness would have to be both 0 and 1. Independent witnesses exist, but that answers a different quantified task. $\square$

## T21 Root receiver relativity {#T21}

**BM proposition.** A fixed typed export $e$ can be accepted by one receiver and rejected by another.

**Proof.** Let both applicability domains be $\mathbb R$, with acceptance sets $A_1=[0,\infty)$ and $A_2=[1,\infty)$. The export $e=1/2$ belongs to $A_1$ and not $A_2$. Hence Root status must include its receiver and contract. $\square$

## T22 Root acceptance is not automatically transitive {#T22}

**Counterexample.** Acceptance at an intermediate receiver does not imply acceptance after translation to a later one.

**Proof.** Take $e=1$, first acceptance set $[0,\infty)$, translation $\tau(y)=-y$, and second acceptance set $[0,\infty)$. The first acceptance holds and $\tau(e)=-1$ is rejected. T43 states the additional transport condition that suffices. $\square$

## T23 Existence does not provide a canonical selection {#T23}

**Symmetry obstruction.** A nonempty realization family alone does not determine a selection invariant under all its symmetries.

**Proof.** Take a two-element family with no additional data. The transposition is a symmetry. Any selected element is moved by it, so no invariant choice exists. Adding an order, cost, or other selection rule changes the data and may permit selection. $\square$

## T24 Path coherence transitivity {#T24}

**Structural proposition.** If three defined paths have outputs in one comparison space with a transitive relation $\sim$, and $p(x)\sim q(x)$ and $q(x)\sim r(x)$ for every $x$ in their declared common domain, then $p(x)\sim r(x)$ there.

**Proof.** Apply transitivity pointwise. The assertion neither enlarges the common domain nor proves independent higher-order obligations. $\square$

## T25 Cyclic separator consistency can fail globally {#T25}

**Classical counterexample family.** For $n\ge3$ Boolean variables on a cycle, impose equality on consecutive edges $1$ through $n-1$ and inequality on the closing edge. Every edge relation has full projection on either endpoint and therefore agrees with neighbors on separators. The global join is empty.

**Proof.** Every Boolean endpoint value has an extension on each individual equality or inequality edge, proving separator consistency. The equality path forces $x_1=x_n$ while the closing edge forbids it. This is the cyclic boundary of T44 and is distinct from T24. $\square$

## T26 Finite serial Passport defect localization {#T26}

**BM specialization.** Let $f_k:X_{k-1}\to X_k$ be total for $1\le k\le n$, with predicates $P_k$, and $F_k=f_k\cdots f_1$, $F_0=I$. Set $D_k=\{u:P_{k-1}(u),\ \neg P_k(f_ku)\}$. Then

$$\{x:P_0(x),\ \neg P_n(F_nx)\}\subseteq\bigcup_{k=1}^nF_{k-1}^{-1}(D_k).$$

**Proof.** A Boolean sequence starting true and ending false has a first true-to-false step. That step puts $F_{k-1}x$ in $D_k$. If failure is absorbing at every stage for every input, membership on the right also implies initial truth and final failure, giving equality. For partial operations restrict to defined chains or introduce an explicit failure tag. A failure appearing only at an infinite limit is outside this finite theorem. $\square$

## T27 Exact repair refinement {#T27}

**Corollary of T06.** Adding a lawful side observation $Q$ changes a representation $R$ to $(R,Q)$ with kernel $\ker R\cap\ker Q$.

**Proof.** T06 gives the identity and its inclusion in $\ker R$. No source for $Q$ is constructed by this identity; its availability is an independent requirement. $\square$

## T28 Repair closure and revalidation {#T28}

**BM certification theorem.** Let $\operatorname{Cl}$ be a closure operator on a component set, and $A=\operatorname{Cl}(S)$. Then $A$ is the least closed set containing $S$. A certificate depending only on coordinates outside $A$ survives any change confined to $A$. On a full product $X=\prod_{v\in V}X_v$ with finite $V$, a predicate $\varphi$ is invariant under every change in $A$ iff its essential coordinate support is disjoint from $A$.

**Proof.** Extensivity and idempotence make $A$ a closed superset. If $S\subseteq B=\operatorname{Cl}(B)$, monotonicity gives $A\subseteq B$. A certificate of unchanged coordinates has unchanged arguments. For the final assertion, an essential coordinate in $A$ gives two states differing only there that change $\varphi$, contradicting invariance. Conversely, if no coordinate in $A$ is essential, replace the finitely many changed coordinates one at a time; the predicate stays unchanged at each replacement. $\square$

The finite-product qualification is essential. On $\{0,1\}^{\mathbb N}$, the predicate "infinitely many coordinates are 1" has no individually essential coordinate but changes between the all-zero and all-one sequences. Constrained products also require an admissible-path argument; coordinate replacements may leave the source domain.

## T29 Finite Markov closure {#T29}

**Classical strong lumpability theorem.** For a finite stochastic matrix $K$ and surjection $R:X\to Z$, a reduced Markov matrix preserving the one-step observed law for every initial distribution exists iff for $R(x)=R(x')$ and each $z$,

$$\sum_{R(y)=z}K(x,y)=\sum_{R(y)=z}K(x',y).$$

**Proof.** Necessity follows by choosing point-mass initial distributions at $x,x'$. Conversely define the reduced row by these sums; nonnegativity and row sum one are inherited. Summing against an arbitrary initial distribution proves the observed-law identity. Support equality alone does not establish equality of these sums. $\square$

## T30 Markov test-function composition {#T30}

**Classical identity.** For composable Markov kernels $K,L$ and bounded measurable $\phi$, $(KL)^\dagger\phi=K^\dagger(L^\dagger\phi)$, where $K^\dagger\psi(x)=\int\psi(y)K(x,dy)$.

**Proof.** Substitute $(KL)(x,A)=\int L(y,A)K(x,dy)$ into the left integral. Equality of iterated integrals holds first for indicator functions by the definition, then for simple functions by linearity, nonnegative measurable functions by monotone convergence, and bounded signed functions by positive/negative decomposition. These are kernel hypotheses, not ordinary deterministic composition. $\square$

## T31 Exact task diameter criterion {#T31}

**Metric corollary.** For metric-valued $T$, exact sufficiency of $R$ is equivalent to every nonempty task fibre image having diameter zero.

**Proof.** A metric has $d(u,v)=0$ iff $u=v$, so zero diameter is exactly fibre constancy in T01. A pseudometric gives equality only after passing to its zero-distance quotient. $\square$

## T32 Two-sided reconstruction bound {#T32}

**Quantitative theorem.** Let $\Delta=\sup_{z\in R(X)}\operatorname{diam}T(R^{-1}z)$. Every decoder has worst-case error at least $\Delta/2$. If a fibre section exists, a representative decoder has error at most $\Delta$. For bounded real-valued tasks the midpoint decoder attains $\Delta/2$.

**Proof.** For two points in a fibre, triangle inequality bounds their task distance by the sum of their errors against the shared decoded value, hence by twice the worst-case error. Take suprema. A representative task value lies in the fibre image and is within its diameter of every other member. In a bounded real fibre, the midpoint of its infimum and supremum has maximal error half its range, whether endpoints are attained or merely approached. The lower bound proves optimality. No continuous or admissible decoder class is assumed. $\square$

## T33 Lipschitz serial error propagation {#T33}

**Classical quantitative theorem.** Suppose at step $k$ the approximate update differs from the exact update by at most $\delta_k$ on the relevant states, and the exact update is $L_k$-Lipschitz there. If the prior error is $e_{k-1}$, then $e_k\le\delta_k+L_ke_{k-1}$.

**Proof.** Insert the exact update of the approximate prior state between the two compared outputs. Triangle inequality bounds the first difference by $\delta_k$ and Lipschitz continuity bounds the second by $L_ke_{k-1}$. Repeated substitution gives $e_n\le e_0\prod_{j=1}^nL_j+\sum_{k=1}^n\delta_k\prod_{j=k+1}^nL_j$. Every compared point must be in the domain of the relevant estimate. $\square$

## T34 Periodic incompressible energy identity {#T34}

**Classical applied identity.** On a periodic torus, for a smooth divergence-free solution of $\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f$ with $\nu>0$,

$$\tfrac12\frac d{dt}\|u\|_2^2=-\nu\|\nabla u\|_2^2+\langle u,f\rangle.$$

**Proof.** Take the spatial inner product with $u$. The transport term integrates to $\int\nabla\cdot(u|u|^2/2)=0$; the pressure term integrates to $-\int p\nabla\cdot u=0$; integration by parts gives $\langle u,\Delta u\rangle=-\|\nabla u\|_2^2$. Periodicity removes boundary terms. This identity holds on the smooth solution's existing interval; it does not prove global regularity or closure of an energy-only representation. $\square$

## T35 Wilson-loop gauge invariance {#T35}

**Classical applied identity.** For matrices $U_{ij}$ on the oriented edges of a closed loop and invertible gauge matrices $g_i$, let $U'_{ij}=g_iU_{ij}g_j^{-1}$. The trace of the ordered loop product is unchanged.

**Proof.** Multiplying around the loop cancels adjacent $g_j^{-1}g_j$, leaving $g_0(U_{01}\cdots U_{m0})g_0^{-1}$. Trace cyclicity removes the remaining conjugation. This finite-dimensional algebra supplies neither a continuum quantum field construction nor a mass-gap proof. $\square$

## T36 Sector non-portability {#T36}

**Governing restriction with counterexample.** A set-level factorization does not imply a factorization in a more restrictive native category.

**Proof of the obstruction.** Let $X=\mathbb R$ have the discrete topology, let $Z=\mathbb R$ have its usual topology, and let $R$ be the identity on underlying sets. The map $T:X\to\{0,1\}$ indicating nonnegative reals is continuous from discrete $X$. Its unique set-level factor through $R$ is discontinuous at zero in usual $Z$. Thus a continuous decoder cannot be inferred from T01. The general restriction is a rule of valid theorem application, not a new universal theorem. $\square$

## T37 Realization monotonicity {#T37}

**Classical semantic proposition.** With signature and context fixed, $\Gamma\subseteq\Gamma'$ implies $\mathfrak F(\Sigma,\Gamma';c)\subseteq\mathfrak F(\Sigma,\Gamma;c)$.

**Proof.** An interpretation satisfying every obligation of $\Gamma'$ satisfies every member of its subset $\Gamma$. No existence follows from this inclusion. $\square$

## T38 Independent Configuration product {#T38}

**Structural theorem.** If interpretation spaces split as a product, obligations act separately on the two factors, and there are no cross-obligations, then the combined realization family is the product of the two realization families.

**Proof.** A pair satisfies the combined obligations iff its first coordinate satisfies the first set and its second satisfies the second set. This characterizes exactly the Cartesian product. An undeclared shared constraint invalidates the premise. $\square$

## T39 Single-cycle holonomy {#T39}

**Classical group theorem.** For group labels $g_i$ on an oriented $n$-cycle, potentials with $g_i=h_i^{-1}h_{i+1}$, $h_{n+1}=h_1$, exist iff $g_1\cdots g_n=e$.

**Proof.** Necessity is telescoping in the specified order. Conversely choose $h_1=e$ and recursively $h_{i+1}=h_i g_i$. The product condition closes the final edge. No commutativity is required. $\square$

## T40 Fundamental-cycle criterion {#T40}

**Classical graph theorem.** In a finite connected graph with reverse-edge labels the inverses of forward labels, global potentials as in T39 exist iff the holonomy around every fundamental cycle of one spanning tree is trivial. There are $|E|-|V|+1$ such edges to check, counting undirected edges once.

**Proof.** Necessity follows by telescoping along any loop. For sufficiency fix a root and define each potential by the ordered product on its unique spanning-tree path. Tree edges then satisfy the equation. The cycle condition on each non-tree edge says precisely that its given label equals the potential-derived one. All edges now satisfy the equation. A spanning tree has $|V|-1$ edges, giving the count. $\square$

## T41 One-step approximate lumpability {#T41}

**Stochastic quantitative theorem.** In the finite setting of T29, suppose aggregated rows in each observation block have total-variation diameter at most $\varepsilon$. Choose one representative row per block to form $\bar K$. Then $d_\mathrm{TV}(R_\#(\mu K),(R_\#\mu)\bar K)\le\varepsilon$ for every initial law $\mu$.

**Proof.** Write the difference as the $\mu(x)$-weighted sum of the differences between each aggregated row and its block representative. Half the $\ell^1$ norm of a sum is at most the sum of half-norms, so the distance is at most $\sum_x\mu(x)\varepsilon=\varepsilon$. $\square$

## T42 Multi-step approximate lumpability {#T42}

**Derived corollary.** Under T41 the $m$-step discrepancy is at most $\min(1,m\varepsilon)$.

**Proof.** A stochastic matrix contracts total variation: for a signed row vector $v$, $\sum_z|\sum_yv_yK_{yz}|\le\sum_y|v_y|\sum_zK_{yz}=\|v\|_1$. Insert one reduced step applied to the actual aggregated law. T41 bounds the fresh error by $\varepsilon$ and contraction carries the previous error unchanged or smaller. Starting at zero gives $m\varepsilon$ by induction; distance between laws is also at most one. $\square$

## T43 Certified Root transfer {#T43}

**BM proposition.** If $e\in A_B$ and a defined translator $\tau$ satisfies $\tau(A_B)\subseteq A_C$, then $\tau(e)\in A_C$.

**Proof.** Membership and the image inclusion imply the conclusion directly. The inclusion must encode all required receiver conditions; one passed task is insufficient if acceptance includes others. $\square$

## T44 Join-tree hypergraph gluing {#T44}

**Classical local-to-global theorem.** A finite family of scopes $V_i$ has a join tree with the running-intersection property. Each carries a nonempty relation $A_i\subseteq\prod_{v\in V_i}X_v$. Adjacent relations have equal projections on $V_i\cap V_j$. Then the global natural join is nonempty and its projection to every $V_i$ is exactly $A_i$.

**Proof.** Choose any tuple at a chosen root. Move outward along the tree, extending each selected parent tuple to a child tuple with the same separator values using projection equality. A child variable already assigned elsewhere must occur on the entire connecting path by running intersection, hence in its parent separator; its value is therefore consistent. Thus the local tuples assemble into one global assignment. Any chosen root tuple extends, proving surjectivity of the global projection to that relation. Rooting at any node proves the claim for every $A_i$; the reverse projection inclusion follows from the definition of join. $\square$

## T45 Scope erasure obstruction {#T45}

**Elementary BM formulation.** An encoding retaining only a carrier arrow $R$ while erasing its task scope cannot determine whether that arrow is sufficient for the original scope.

**Proof.** Use the same constant $R:\{0,1\}\to\{*\}$ twice. It is sufficient for a constant task and insufficient for the identity task. The encoding produces the same object for opposite sufficiency outcomes. This does not obstruct enriched formalisms that retain the scope. $\square$

## T46 Receiver information order {#T46}

**Classical refinement lattice in BM scope.** If $\mathscr Q_1\subseteq\mathscr Q_2$, then $q_{\mathscr Q_1}$ factors through $q_{\mathscr Q_2}$. The least common refinement preserving both task families is the quotient by $E_{\mathscr Q_1}\cap E_{\mathscr Q_2}=E_{\mathscr Q_1\cup\mathscr Q_2}$.

**Proof.** Adding kernels to an intersection only decreases the equivalence relation. Containment gives the induced quotient map by T01. Any equivalence preserving both task families lies in both kernels and hence their intersection; that intersection itself preserves both. This proves the universal least-refinement property. $\square$

## T47 Receiver sufficiency modulus {#T47}

**Quantitative specialization.** For nonempty metric task family $T_i:X\to W_i$, use the product output with sup distance (possibly extended) and define

$$\omega(R)=\sup_{R(x)=R(x')}\sup_i d_i(T_i(x),T_i(x')).$$

 Unrestricted joint-task decoders satisfy $\omega/2\le e^*\le\omega$ when fibre representatives exist. Moreover $\omega=0$ iff every task factors through $R$.

**Proof.** Apply T32 to the product task, whose fibre diameter is exactly $\omega$. The triangle argument and representative construction work also for extended sup distance. Zero distance means equality in every coordinate, so T01 applies to each task. A receiver imposing constraints on decoded tuples can increase the optimum and needs a separate feasible-center analysis. $\square$

## T48 Quantitative Root transfer {#T48}

**Corollary.** Suppose ideal incoming value $y$ and supplied value $\hat y$ satisfy $d(y,\hat y)\le\varepsilon$, the translator $\tau$ is $L$-Lipschitz on both, and desired output $z$ obeys $d(z,\tau(y))\le\delta$. Then $d(z,\tau(\hat y))\le\delta+L\varepsilon$.

**Proof.** Insert $\tau(y)$ and apply triangle inequality and the Lipschitz bound. This estimates error; receiver acceptance also needs the bound to meet its tolerance and the output to meet other obligations. $\square$

## T49 Relational cycle criterion {#T49}

**Classical relational theorem.** For a finite cyclic chain $R_i\subseteq X_i\times X_{i+1}$ with $X_{n+1}=X_1$, a simultaneous cyclic realization exists iff $(R_n\circ\cdots\circ R_1)\cap\Delta_{X_1}\ne\varnothing$.

**Proof.** A cyclic realization provides intermediate witnesses for a diagonal pair in the composite. Conversely the definition of finite relational composition supplies the intermediate states for such a diagonal pair. Additional constraints beyond these relations must still be checked. $\square$

## T50 Satisfaction-preserving Configuration maps {#T50}

**Classical categorical construction.** Fix size conventions and typed interpretation transformations as morphisms, each sending satisfying interpretations of its source Configuration to satisfying interpretations of its target. Identity transformations and composable transformations form a category.

**Proof.** Identity preserves satisfaction. If $F$ and $G$ preserve it, a satisfying source is sent by $F$ to a satisfying intermediate and by $G$ to a satisfying target. Composition and identities inherit associativity and unit laws from the specified transformation composition. This meta-level construction does not collapse native sector mathematics into one category of bare sets. $\square$

## T51 Configuration refinement preorder {#T51}

**Classical proposition.** At fixed signature and context define $C_2\preceq C_1$ iff $\mathfrak F(C_2)\subseteq\mathfrak F(C_1)$. This is a preorder and becomes a partial order after identifying Configurations with the same realization family.

**Proof.** Reflexivity and transitivity are those of inclusion. Mutual inclusion is equality of realization families, which is exactly the chosen quotient equivalence; antisymmetry follows on equivalence classes. $\square$

## T52 Acceptance does not determine an adjunction {#T52}

**Categorical counterexample.** Object-level Root/Passport acceptance data alone cannot imply an adjunction.

**Proof.** A single accepting Root and Passport can be represented by two terminal categories, where unique functors are adjoint. The same object data can instead have a one-object Root category with two endomorphisms and a terminal Passport category. Functors exist in both directions, but the corresponding hom sets have sizes two and one, so the natural bijection required for either adjunction is impossible. Additional morphism structure is indispensable. $\square$

## T53 Mixed deterministic and stochastic continuation {#T53}

**Finite integrated theorem.** On finite $X\times Y$, let the next $x$ be $f(x)$ and the next $y$ have conditional law $K_{x,y}$. Retain $(r(x),s(y))$. If $rf=\bar f r$ and the probabilities assigned by $K_{x,y}$ to each $s$-block depend only on $(r(x),s(y))$, the joint kernel is strongly lumpable through that representation.

**Proof.** The probability of a reduced next pair $(a,b)$ is the indicator $\mathbf1_{r(f(x))=a}$ times $\sum_{s(y')=b}K_{x,y}(y')$. The first factor depends only on $r(x)$ by deterministic closure, and the second depends only on the retained pair by assumption. The product is therefore constant on every joint observation fibre. T29 gives a reduced Markov chain for every initial law. Dependence of $K$ on both native coordinates has not been discarded. $\square$

## T54 Relational exact task factorization {#T54}

**Relational specialization.** For $\mathcal E\subseteq X\times Y$, $R:Y\to Z$, and source task $T:X\to W$, put $\mathcal O(x)=R(\mathcal E[x])$. A decoder on $\bigcup_x\mathcal O(x)$ satisfying $D(Ry)=T(x)$ for every $x\mathcal E y$ exists iff $\mathcal O(x)\cap\mathcal O(x')\ne\varnothing$ implies $T(x)=T(x')$.

**Proof.** A shared observed value would have to decode to both tasks, proving necessity. Conversely all source tasks attached to a realized observed value agree by the implication; use that unique value to define the decoder. Equivalently apply T01 to the incidence pairs $(x,z)$ with $z\in\mathcal O(x)$. States without successors give no observed value and need a separate availability task if relevant. $\square$

## T55 Exact relational Dynamic Closure {#T55}

**Relational specialization.** For $\mathcal E\subseteq X\times X$ and $R:X\to Z$, a reduced relation on $R(X)$ satisfying $\bar{\mathcal E}[R(x)]=R(\mathcal E[x])$ exists iff $R(x)=R(x')$ implies equality of those successor-image sets.

**Proof.** Necessity follows because the reduced relation assigns one successor set to each reduced state. For sufficiency assign the common successor-image set to that state; fibre equality makes it well-defined. The empty set is a legitimate successor set and preserves dead ends. This is factorization of a power-set-valued map. It does not determine a stochastic law. $\square$

# Consolidated W registry

W01-W35 are the consolidated exploratory identifiers. W16-W96 used in the earlier scratchpad are retired scratch numbering and must not be counted as additional canonical theorems. The statements in the main text govern the scoped uses in this edition. No historical novelty is certified.

\begingroup
\small

| ID | Topic | Disposition in this edition |
|---|---|---|
| W01 | Contextual-Width Monotonicity | Scoped proof or derivation supplied in the main text |
| W02 | Contextual-Width Union Bounds | Scoped proof or derivation supplied in the main text |
| W03 | Experiment Redundancy / Factorization | Scoped proof or derivation supplied in the main text |
| W04 | Marginal Distinction Gain Formula | Scoped proof or derivation supplied in the main text |
| W05 | Four-State Submodularity | Scoped proof or derivation supplied in the main text |
| W06 | Five-Hypothesis Complementarity Threshold | Scoped proof or derivation supplied in the main text |
| W07 | Persistent Non-Submodularity for \(n\ge5\) | Scoped proof or derivation supplied in the main text |
| W08 | Incidence-Cycle Characterization of Exact Complementarity | Scoped proof or derivation supplied in the main text |
| W09 | Exact Aggregate Closure for Independent Decays | Scoped proof or derivation supplied in the main text |
| W10 | Critical Exact-Carrier Collapse | Scoped proof or derivation supplied in the main text |
| W11 | Approximate Carrier Survival | Proved with nonnegative data or an absolute-sum bound |
| W12 | Exact/Approximate Carrier Separation | Scoped proof or derivation supplied in the main text |
| W13 | Finite-Horizon Causal Carrier | Conditional locality application; see note below |
| W14 | Dynamic-Quasistatic Locality Non-Inheritance | Conditional locality application; see note below |
| W15 | Active Distinction Design | Scoped proof or derivation supplied in the main text |
| W16 | Robust Ambiguity Representation | Scoped proof or derivation supplied in the main text |
| W17 | Robust Pairwise Complementarity Threshold | Scoped proof or derivation supplied in the main text |
| W18 | Adaptive Distinction Threshold | Scoped proof or derivation supplied in the main text |
| W19 | Higher-Order Critical Count | Scoped proof or derivation supplied in the main text |
| W20 | Task-Projection Representative Gluing | Representative gluing proved; holonomy needs extra transport hypotheses |
| W21 | Task-Coarsening Geometric Nonmonotonicity / Explosion | Scoped proof or derivation supplied in the main text |
| W22 | Fiber-Multiplicity Threshold | Scoped proof or derivation supplied in the main text |
| W23 | Fragmented-State Leray Theorem | Scoped proof or derivation supplied in the main text |
| W24 | Exact Fragmentation-Ordering Characterization | Scoped proof or derivation supplied in the main text |
| W25 | Fragmentation-Support Lower Bound | Scoped proof or derivation supplied in the main text |
| W26 | Fragmentation Support Under Disjoint Union | Scoped proof or derivation supplied in the main text |
| W27 | Minimum Fragmentation Ordering | Prior-art identification retained |
| W28 | One-Fragment Repair Criterion | Scoped proof or derivation supplied in the main text |
| W29 | Fragmentation Breadth-Depth Separation | Scoped proof or derivation supplied in the main text |
| W30 | Complete Breadth-Depth Feasibility Law | Scoped proof or derivation supplied in the main text |
| W31 | Breadth-Depth Alignment Criterion | Scoped proof or derivation supplied in the main text |
| W32 | Fragmentation Pareto Geometry | Scoped proof or derivation supplied in the main text |
| W33 | Pareto Endpoint Laws | Scoped proof or derivation supplied in the main text |
| W34 | Additive Breadth-Optimality Price | Scoped proof or derivation supplied in the main text |
| W35 | Multiplicative breadth optimality gap | Scoped proof or derivation supplied in the main text |

\endgroup

For W13, finite-speed uniqueness and a domain-of-dependence theorem make the backward causal region sufficient for the receiver history; this is not a universal minimality result. For W14, dynamic locality does not transfer automatically to a quasistatic elliptic model. In one dimension the wave equation has the d'Alembert causal interval, while the Dirichlet Green function of $-u''=f$ on $(0,1)$ is $G(x,y)=\min(x,y)(1-\max(x,y))$, positive for every interior pair. A remote positive forcing perturbation changes an interior elliptic response immediately in that static model. These are native model examples, not a claim that every elliptic reduction is a valid approximation on every time scale.


# Fundamental interaction audit register

This register preserves FI01-FI42 as applications and research records. P means prior-art physics, C means BM corollary or synthesis, and R means retain with a scope correction. These are the source audit classifications, not 42 newly proved physics theorems. Full native theories and proof artifacts are not reproduced by listing them.

| ID | Topic | Source classification |
|---|---|---|
| FI01 | Differential-Identity Source Passport | P/C |
| FI02 | Higgs Mass-Kernel Theorem | P |
| FI03 | Critical Vector-Carrier Transition | P/C |
| FI04 | Local-EOM Incompleteness | P/C |
| FI05 | Flavor Quotient | P |
| FI06 | Local-to-Global Gauge Completeness | P/C |
| FI07 | Quantum Anomaly / Passport Non-Inheritance | P/C |
| FI08 | RG Root and Dimensional Transmutation | P/C |
| FI09 | Receiver-Relative EFT Depth | C/R |
| FI10 | BRST Cohomological Carrier | P/C |
| FI11 | Unitarity Gram Carrier | P/C |
| FI12 | Wilson-Loop / String-Tension Root | P/C |
| FI13 | Källén-Lehmann Spectral Carrier | P/C |
| FI14 | LSZ Asymptotic-Particle Carrier | P/C |
| FI15 | Schwinger-Dyson Completion Fibre | C/P |
| FI16 | Callan-Symanzik RG Transport | P/C |
| FI17 | OPE Receiver-Depth | C/R |
| FI18 | Einstein Constraint/Admissibility Fibre | P/C |
| FI19 | Tidal-Response Carrier | P/C |
| FI20 | Ricci/Weyl Non-Inheritance | P/C |
| FI21 | Gravitational-Wave Gauge Quotient | P |
| FI22 | Raychaudhuri Closure Criterion | C/P |
| FI23 | FLRW Symmetry-Induced Carrier Collapse | P/C |
| FI24 | Event-Horizon Nonlocality | P/C |
| FI25 | Black-Hole First-Law Carrier | P/C |
| FI26 | Bogoliubov Carrier Hierarchy | P/C |
| FI27 | Semiclassical Backreaction Closure | P/C/R |
| FI28 | Dirac On-Shell Carrier | P |
| FI29 | Neutrino Oscillation Quotient | P/C |
| FI30 | Standard-Model Hypercharge Passport | P |
| FI31 | Weinberg/Seesaw Low-Energy Carrier | P/C |
| FI32 | Jarlskog CP Root | P/C |
| FI33 | Strong-\(\theta\) Anomaly-Compensated Root | P/C |
| FI34 | Goldstone/Higgs Carrier Accounting | P/R |
| FI35 | Vacuum-Manifold Topological Carrier | P/R |
| FI36 | 't Hooft Anomaly as RG Root | P/R |
| FI37 | Dispersive Moment Carrier | P/C |
| FI38 | Positivity Passport | P |
| FI39 | Analytic/Crossing Completion Fibre | P/C/R |
| FI40 | Partial-Wave Unitarity Carrier | P/C |
| FI41 | CPT / Spin-Statistics Passport | P/R |
| FI42 | Fundamental-Interaction Carrier Theorem | C/P-overlap |

The governing scope corrections are as follows. FI27 uses geometry and a two-point function for a mean-source calculation for free quasifree matter under Hadamard and renormalization conditions; it is not complete semiclassical validity data. FI34 describes a reorganization of physical degrees of freedom, not a proved transfer of a material information substance. FI35 uses homotopy classification in a specified order-parameter and finite-energy boundary setting. FI36 requires lawful identification or transport of the relevant symmetry along the flow. FI39 asserts generic underdetermination by finite moment data, not nonuniqueness under every possible auxiliary prior. FI30 has a one-dimensional normalization family before a sign convention. FI29's parameter count does not establish global experimental identifiability. FI17 requires a controlled OPE remainder.

FI42 additionally needs invariant tasks on the redundancy quotient. The admissibility step is a subset selection, not an automatic repair map from arbitrary raw states. These conditions are explicit in the main text. No FI item is authorized here as an external historical novelty claim.


# Volume II and historical coverage

The Volume II log is a development registry. The table records how its families are handled here; a family label is not a substitute for its theorem hypotheses.

\begingroup
\small

| Family | Scope in the source record | Release disposition |
|---|---|---|
| PDEW-01 to 05 | Compact profiles, spectral covering, smoothing | Compactness proved; conservative spectral bound and fixed-time heat asymptotics supplied; nonlinear cases conditional |
| PORT-01 to 06 | Boundary tasks, compact transfer, conditioned coupling | Linear kernel and compact-transfer arguments supplied; conforming coercive error estimate stated with its hypotheses |
| TPORT-01 to 07 | Hankel profiles, causal quotients, delay pruning | Fixed linear history and delay contracts supplied; general PDE propagation needs native theorems |
| DCUT and STW | Distributed cuts and spacetime width | Counting, redundancy and residual quotient arguments supplied; general locality-constrained optimization open |
| COUP, LOC and CLUST | Perturbation, locality and cluster interfaces | Perturbation bounds retained with ambient covers; area laws and cluster guarantees remain conditional |
| QLOC | Quantum contextual carriers and light cones | Expectation factorization is distinct from one physical decoder; locality conclusions require supplied circuit or Lieb-Robinson hypotheses |
| QDIST | Task error correction and quantum cuts | Physical-channel recovery and imported OAQEC criterion; capacity alone not sufficient |
| QBCAST | No-broadcasting and access geometry | Disjoint-access obstruction and transversal statement supplied |
| QDEG | Greatest exact surviving algebra | Imported commutant characterization; monotonicity requires postprocessing relation |
| QAPP-01 to 07 | Algebraic and physical approximate recovery | Comparison, stability and finite Kraus-rank bound supplied; explicit no-greatest-algebra counterexample added |
| NLR, TOP, CIRC, GAUGE, BUNDLE | Nonlinear, topological and bundle realization | Core local rank and global obstruction results retained; broader families not promoted wholesale |
| QSYS, QALG, STOCH, FIN, SFIN | Native quantum and finite exactification | Specified finite sectors included; abstract labels do not certify infinite-dimensional versions |
| SRP, PAR, DUAL, PST | Structured repair, duality and perturbation | Declared optimization and linear results retained; general optimization remains open |
| DIST, DYN, CDL, SENS | Distinction, latency and sensor design | Exact task geometry and experiment examples supplied; other logged formulations remain historical |
| E2E, AE2E, RES, ALLOC | Scheduling and resource allocation | Historical development families; no universal algorithm or general optimal scheduling theorem certified |
| FLOC, PROV, COMP, HIS, WIDTH, AWIDTH | Failure, provenance, composition and semantic width | Finite proof and profile specializations retained; global and approximate extensions need their written contracts |

\endgroup

The LEV 001-012 labels are historical specializations leading to the consolidated weighted representation problem. LEV 013, LEV 014C, LEV 015, LEV 016 and the strengthened LEV 014S certificate are reproduced with proofs. The closing addendum supplies a terminating global epsilon-certificate for arbitrary finite rational SPD inputs; general efficiency and closed-form optimization are not established. The RES 001-005 and cross-formalism reduction audits preserve task, applicability, dependency and witness distinctions; they do not establish novelty over enriched institutions, contracts, abstract interpretation, decision theory or coalgebra.

The earlier 200-equation physics index and the NS and Yang-Mills application Leaves are historical records, not 200 new BM theorems or completed Millennium proofs. SSH remains retired. Seed, Rooting and Rebranching retain candidate status except for a separately specified native construction. GRDE remains frozen at 008.

The DD sequence through DD-361 is reported by partial conversation retrieval, but its complete statements and final strict-review transcript were not recovered for this edition. No per-DD proof certification or reconstruction is claimed. The predictive interior used in this book is defined and proved explicitly; it is not presented as a replacement transcript of the missing sequence. Full DD source reconciliation is required before labeling any volume a complete archive of all BM work.


# Verification and reproducibility

## What the computations establish

The release includes written proofs and a separate computational package. The computations check finite instances, exact algebraic witnesses, and numerical identities. They are useful for finding mistakes and reproducing examples. They do not replace an argument over all state sizes, all real parameters, or an infinite-dimensional limit. No proof assistant was used to certify this book.

The two verification programs from the Edition 1.1 package were rerun without changing their mathematical implementations. The new programs check the additional finite constructions and compute fragmentation frontiers. The recorded results are as follows.

| Check | Coverage | Result |
|---|---|---|
| Single-action exactification | 4,096 four-state models; comparison with all 15 partitions | Coarsestness and refinement checks pass |
| Partial interaction refinement | 648 models using 81 partial binary interactions | Definedness and coarsestness checks pass |
| Multiple-action exactification | 18,225 three-state models | Interior laws, greatestness, and iteration agree |
| Relational refinement | 2,560 models using 512 relations, including empty successor sets | Stable refinement checks pass |
| Stochastic refinement | 1,080 models; probabilities in $\{0,1/2,1\}$ | Exact block-sum checks pass |
| Quantum closure | Rational negative eigenvalues $-1/2,3/2$; positive Choi witness; 16 two-qubit matrix-unit constraints | Exact witnesses pass |
| Heat cascade | 96 independent modal quadratures | Maximum normalized disagreement below $2.7\times10^{-15}$ |
| Invariant-graph repair | Zero and nonzero defects, including zero free error | Constructed error satisfies the stated bound |
| Partition complementarity | All 19,583 nested-partition and added-test comparisons for one to five states | No violation through four states; 90 at five |
| Incidence cycle identity | All 18,616 five-state comparisons | Integer identity holds |
| W35 construction | All column orders through nine columns, modulo reversal | Predicted breadth, depth, and constrained depth agree |
| Fragmentation dynamic program | Six-column construction | Exact frontier agrees with independent enumeration |
| New finite examples | Reduction-order counterexample and qubit approximate-algebra defect | Exact witness calculations agree |

The reversal reduction in the W35 check is justified because reversing a complete column order preserves every row's number of one-blocks. The actual numbers of orders evaluated for $n=5,6,7,8,9$ are respectively 60, 360, 2,520, 20,160, and 181,440. Enumeration establishes these finite cases; the proof in the main text establishes the unbounded family.

The heat quadrature checks only the finitely many listed modes and parameter choices. The summable estimate in the heat chapter supplies the infinite-mode argument. Likewise an invariant-graph residual near floating-point precision is numerical evidence for the exhibited examples, while the contraction argument supplies the theorem.

## Running the package

Use Python 3 with NumPy and SciPy for the full set of retained checks. Matplotlib is needed only to regenerate the figures. From the extracted package directory run:

```bash
python code/bm_verification.py \
  --output data/v1_verification_rerun.json
python code/bm_second_verification.py \
  --output data/v1_second_verification_rerun.json
python code/bm_checks.py --max-columns 9 \
  --output data/verification_results.json
python code/fragmentation_dp.py \
  --output data/dp_verification.json
python code/make_figures.py
```

The README records the document-rendering command. The standalone Markdown contains the complete book text; its two figure files are included. The source inventory records recovered source filenames and SHA-256 hashes. A hash establishes byte identity, not mathematical validity. The result registry preserves T01-T55, W01-W35, and FI01-FI42, with separate dispositions for the later development families.

## Source and coverage discipline

The Edition 1.1 amendment governs conflicts with Edition 1.0. The consolidated W log governs the retired scratch numbering. The FI audit's scope corrections govern its application summaries. The main chapters reproduce or supply the arguments on which this edition relies. The historical family register explicitly identifies material that is recorded without a new full proof audit.

The complete DD sequence through DD-361 and its final strict-review transcript were not recovered. The available conversation summary supplies continuity about the research direction, but it is not a source from which missing formal statements can be certified. The book therefore gives its own explicit predictive-interior construction and marks the DD archive gap. It does not invent 361 theorems from a summary.

Public review should cite the edition date, chapter or stable result identifier, and the precise hypothesis being challenged. A correction should distinguish a wrong statement, a missing assumption, a proof gap, a numerical error, and a prior-art overlap. These are different reasons for revising a result's status.


# Notation and prerequisites

Symbols are local to a chapter when their native meanings differ. In particular, $R$ can mean a representation or a quantum recovery channel; $D$ can mean a decoder or total fragmentation; and $\delta$ can mean an approximation defect or the optimum fragmentation depth. Their domains and definitions determine the meaning.

| Symbol or term | Meaning in its stated setting |
|---|---|
| $X$, $Y$, $Z$ | Native state, task, and representation carriers |
| $R:X\to Z$ | A representation or retained code |
| $T:X\to Y$ | A declared task map |
| $D:Z\to Y$ | A decoder answering a task from a code |
| $\ker R$ | Equivalence relation of equal representation values |
| $X/E$ | Set of equivalence classes for $E$ |
| $\Delta_X$ | Equality relation on $X$ |
| $E\subseteq F$ | $E$ distinguishes at least as much as $F$ |
| $I_U(E)$ | Greatest $U$-stable equivalence contained in $E$ |
| $\Phi_t$ | Native time evolution |
| $\overline\Phi_t$ | Proposed reduced time evolution |
| $R\Phi_t=\overline\Phi_tR$ | Exact autonomous closure |
| $K$ | Declared performance set, or a matrix as locally defined |
| $\operatorname{diam}$ | Supremum of pairwise distances |
| $N_\varepsilon$ | Covering number at radius $\varepsilon$ in the stated metric |
| $d_n$ | Linear approximation width where explicitly defined |
| $\sigma_j$ | Singular values, in nonincreasing order |
| $\|\cdot\|_F$ | Frobenius norm |
| $\|\cdot\|$ | Operator or native norm, specified in the chapter |
| $P_U$ | Orthogonal projection onto a stated subspace |
| $M_d$ | Complex $d$ by $d$ matrices |
| CPTP | Completely positive and trace preserving |
| $N^\dagger$ | Heisenberg adjoint of a quantum channel |
| $\widehat N$ | A complementary channel |
| $\mathcal A'$ | Commutant of an operator algebra $\mathcal A$ |
| $P_{\mathcal A}$ | Trace-preserving conditional expectation onto $\mathcal A$ |
| $\|\cdot\|_\diamond$ | Diamond norm of a linear map between matrix spaces |
| $\kappa$, $\eta$, $\delta_{\mathcal A}$ | Normalized commutator, commutant-distance, and physical-recovery defects |
| $w(J)$ | Number of equivalence classes induced by a finite task family |
| $b_i(\pi)$ | Number of one-blocks of row $i$ in column order $\pi$ |
| $B(\pi)$ | Number of fragmented rows |
| $D(\pi)$ | Total excess blocks $\sum_i(b_i(\pi)-1)$ |
| $\phi$, $\delta$ | Minimum breadth and minimum depth over all orders |
| $D_\phi$ | Least depth among orders of minimum breadth |
| $\tau(\mathcal M)$ | Minimum size of a set meeting every member of $\mathcal M$ |
| Leaf | A typed mathematical assertion with its conditions and dependencies |
| Passport | The requirements for an export to be accepted by a receiver |
| Root | An export accepted under a specified receiver Passport |
| GURF | BM's response-specialized layer, with roles defined in its chapter |

The finite chapters need sets, functions, equivalence relations, graphs, and elementary linear algebra. The smooth chapters additionally use topology, differentials, the constant-rank theorem, and Borsuk-Ulam. The heat and continuum chapters use Hilbert spaces, compact operators, singular values, and semigroup estimates. The quantum chapters use tensor products, positive operators, completely positive maps, and operator algebras. The nerve chapter uses simplicial complexes and reduced homology. Imported results are identified where used; a reader should not mistake the presence of a technical term in the architecture for a proof of its native theorem.


# References {.unnumbered}

## Mathematical and physical sources {.unnumbered}

**Beny2009.** Cedric Beny. Conditions for the approximate correction of algebras. TQC 2009, LNCS 5906, pp. 66-75. The upper estimate in Theorem 1 of the cited arXiv version is used for the quantum recovery bound. [Author preprint](https://arxiv.org/abs/0907.4207).

**BenyKempfKribs2007.** Cedric Beny, Achim Kempf, and David W. Kribs. Generalization of Quantum Error Correction via the Heisenberg Picture. Physical Review Letters 98, 100502. [Author preprint](https://arxiv.org/abs/quant-ph/0608071).

**Borsuk1933.** Karol Borsuk. Drei Satze uber die n-dimensionale euklidische Sphare. Fundamenta Mathematicae 20, pp. 177-190. The Borsuk-Ulam theorem is an imported topological input, not proved in this book. [Original article DOI](https://doi.org/10.4064/fm-20-1-177-190).

**EckartYoung1936.** Carl Eckart and Gale Young. The approximation of one matrix by another of lower rank. Psychometrika 1, pp. 211-218. [Original article](https://link.springer.com/article/10.1007/BF02288367).

**HaddadiLayouni2008.** Salim Haddadi and Zoubir Layouni. Consecutive block minimization is 1.5-approximable. Information Processing Letters 108, pp. 132-135. The objective in that paper is ordinary total block minimization. [Article DOI](https://doi.org/10.1016/j.ipl.2008.04.009).

**KalaiMeshulam2007.** Gil Kalai and Roy Meshulam. Leray Numbers of Projections and a Topological Helly Type Theorem. [Author manuscript](https://math.huji.ac.il/~kalai/leray_num.pdf). A prior-art anchor for Leray numbers and simplicial projection methods; no assertion is made that its hypotheses coincide with every task projection here.

**KimLew2023.** Minki Kim and Alan Lew. Leray Numbers of Tolerance Complexes. Combinatorica. [Author preprint](https://arxiv.org/abs/2109.03030). Used as a boundary reference for the established representability and Leray literature, not as a proof of W23.

**Ovchinnikov2021.** Alexey Ovchinnikov and coauthors. CLUE Exact maximal reduction of kinetic models by constrained lumping of differential equations. [Author preprint](https://arxiv.org/abs/2004.11961). The named method predates this BM edition.

**PaigeTarjan1987.** Robert Paige and Robert E. Tarjan. Three Partition Refinement Algorithms. SIAM Journal on Computing 16, pp. 973-989. [Article DOI](https://doi.org/10.1137/0216062).

**RanzatoTapparo2007.** Francesco Ranzato and Francesco Tapparo. Generalizing the Paige-Tarjan Algorithm by Abstract Interpretation. [Author preprint](https://arxiv.org/abs/cs/0612120).

**Tarski1955.** Alfred Tarski. A lattice-theoretical fixpoint theorem and its applications. Pacific Journal of Mathematics 5, pp. 285-309. [Original paper](https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-p.pdf).

**TongQFT.** David Tong. Quantum Field Theory lecture notes. Background for the additional native structures needed for particle interpretations. [Author course page](https://www.damtp.cam.ac.uk/user/tong/qft.html).

**Watrous2018.** John Watrous. The Theory of Quantum Information. Cambridge University Press. The channel characterization is in the discussion of Choi representations. [Author manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf).

**OpenAI2026.** OpenAI. On the Navier-Stokes Millennium Prize Problem. 8 September 2026, updated 10 September. This is cited as an external announcement; this edition does not certify its proof artifacts. [Announcement](https://openai.com/index/navier-stokes-solution/).

**ClayNS.** Clay Mathematics Institute. Navier-Stokes Equation. Status page consulted 15 September 2026. [Problem page](https://www.claymath.org/millennium/navier-stokes-equation/).

**ClayYM.** Clay Mathematics Institute. Yang-Mills and the Mass Gap. Status page consulted 15 September 2026. [Problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/).

## Governing BM sources {.unnumbered}

**E10.** Branch Mathematics and GURF Mathematical Edition, 10 September 2026. Governs native definitions, GURF roles, T01-T55, the connected finite interface theorem family, and the consolidated LEV results. The local mathematical source used is BM-GURF-Mathematical-Edition-2026-09-10.md.

**C11.** Branch Mathematics The Price of Exact Dynamic Closure, 11 September 2026, Research Supplement 1.0. Governs BM-DC-PRICE-01 and its approximation calculations. The Markdown and original calculation script were recovered from its research package.

**R12.** Branch Mathematics Source Review Corrected Core and Scoped Mathematical Completion, 12 September 2026, Edition 1.1 verification amendment. This supersedes Edition 1.0 where they differ. The governing local file is BM-Review-and-Scoped-Completion-2026-09-12 (1).md.

**V1.** Branch Mathematics Canonical Version 1 Foundation, expanded source and archive README, 12 September 2026. The book presents the governing sources; it does not silently supersede them.

**LOG12.** BM GURF Full Chat Review Verification Log, 12 September 2026. Historical development and open-problem record, subject to the R12 amendments.

**V2LOG.** BM Volume II Development Log, 12 September 2026. Source for PDE, port, distributed, locality, and quantum capability families. The three numbered copies recovered have the same stated size; the selected copy is the one ending in (2).md. This book does not infer identity merely from file size.

**W14.** BM Post Volume II Exploratory Theorem Log, 14 September 2026, Edition 1.0. Governs the consolidation to W01-W35 and retirement of later scratch numbering.

**FI14.** BM Fundamental Interactions Sweep Audit Log, 14 September 2026, Edition 1.0. Governs FI01-FI42, the eight scope corrections, and its rejection of external historical novelty claims.

Earlier RES, LEV, institution, contract, abstract-interpretation, Blackwell, coalgebra, and provenance audits remain historical development sources. Their names and source hashes are preserved in the release package inventory. The public research edition does not turn every historical entry into a newly proved theorem.



# BM development and verification addendum — 14 October 2026

This addendum develops review issues 12, 18, 21, 22, and 35. It supplies new scoped calculations and corrects one numerical illustration in the Research Edition. It does not assign new canonical T, W, LEV, or DD identifiers. The frozen Version 1 foundation remains governed by Edition 1.1. General nonlinear repair and the nonlinear Jordan interior optimum remain open beyond the results below. The subsequent closing addendum resolves finite rational global projector certification to every positive tolerance; it does not claim an efficient general optimizer.

## 1. A demonstrated numerical correction and a complete example certificate

In the Research Edition's “Exact strict-price example,” the printed slope `1.13317887` is inaccurate at its displayed precision. The cost `4.764704744` is consistent with rounding the correct optimum; the exact positivity proof was unaffected.

For the specified matrices

\[
S=\begin{pmatrix}9&0\\0&1\end{pmatrix},\qquad
K=\begin{pmatrix}17/2&-15/2\\-15/2&17/2\end{pmatrix},\quad d=1,
\]

the discarded-direction objective is

\[
J(t)=\frac{(17/2-15t+(17/2)t^2)(9+t^2)}{(1+t^2)^2}.
\]

Exact polynomial differentiation gives

\[
J'(t)=\frac{p(t)}{(1+t^2)^3},\qquad
p(t)=15t^4-136t^3+360t^2-136t-135.
\]

The script below constructs the Sturm sequence using rational polynomial division. Its last nonzero polynomial is constant, so there are no multiple roots. The Cauchy bound puts all roots in |t|≤25; Sturm variation counting finds exactly two real roots there. The isolated positive root has a lower cost than the isolated negative root and the vertical direction, whose cost is 17/2. Every global minimum on the compact projective circle is one of these directions. This certifies the global optimum for this instance.

All following decimal intervals are outward bounds computed by **integer division of rational endpoints**, not rounded floating-point approximations.

| Quantity | Certified enclosure |
|---|---|
| Positive stationary slope | [1.133177443571420609339, 1.133177443571420609340] |
| Negative stationary slope | [−0.427387768349278916181, −0.427387768349278916180] |
| Projector global optimum | [4.764704743750686474003, 4.764704743750686474004] |
| Other stationary value | [108.085833626667231647117, 108.085833626667231647118] |
| Unrestricted optimum | [1.729299736207620541055, 1.729299736207620541056] |
| Projector penalty | [3.035405007543065932948, 3.035405007543065932949] |

The unrestricted value is (85−sqrt(6649))/2. Integer square-root bounds for sqrt(6649), rational root isolation, and interval evaluation of J certify all the enclosures. The complete Sturm polynomials and isolating rational intervals are retained in the output below.

**Correction scope:** replace the erroneous slope and upgrade this particular optimization example from numerical illustration to a reproducible rational certificate. This does not certify an arbitrary floating-point solver or the general noncommuting higher-rank optimum.

Sturm counting is classical. An authoritative account is Narkawicz and Muñoz, [NASA/TM–2014-218548](https://ntrs.nasa.gov/api/citations/20150001256/downloads/20150001256.pdf). Their formally verified PVS procedure is not the procedure executed here; this implementation has not been formally verified.

## 2. Quantitative bounds on the projector admissibility penalty

### 2.1 Declared finite-dimensional problem

Keep the Research Edition's SPD matrices S,K and loss

\[
J(M)=\|K^{1/2}(I-M)S^{1/2}\|_F^2.
\]

Fix 0<d<n. Let H=S^(1/2)KS^(1/2), with eigenvalues theta_1≥...≥theta_n>0. Suppose the cutoff gap g=theta_d−theta_(d+1)>0. Let Pi be the unique leading rank-d spectral projector, and

\[
M_*=S^{1/2}\Pi S^{-1/2},\quad
a_*^2=\|M_*-M_*^T\|_F^2,\quad
\Gamma_d=J_{d,\mathrm{proj}}^*-\sum_{j>d}\theta_j.
\]

Let k_min,k_max and s_min,s_max be the extremal eigenvalues of K and S. Let P_ran and P_row be the Euclidean orthogonal projectors onto the range and row space of M_*, respectively. Then

\[
\boxed{
\frac{k_{\min}s_{\min}}{4(1+2\theta_1/g)}a_*^2
\ \le\ \Gamma_d
\ \le\ \min_{P\in\{P_{\mathrm{ran}},P_{\mathrm{row}}\}}
\|K^{1/2}(P-M_*)S^{1/2}\|_F^2
\ \le\ \frac{k_{\max}s_{\max}}2a_*^2.
}
\]

For both explicitly constructed projectors, the middle quantity is **exactly** J(P)−J(M_*). Thus they give feasible upper certificates with no global optimizer assumed. The lower bound quantifies strict positivity when a_*>0. These are bounds, not a claim of sharp constants or an exact higher-rank solution.

### 2.2 Complete lower-bound proof

Set A=K^(1/2)S^(1/2), N=K^(1/2)P S^(1/2), and N_*=A Pi. Since P has rank d, let Q be the orthogonal projector onto N's row space. Orthogonal row-space decomposition gives

\[
J(P)-J(M_*)=\|N-AQ\|_F^2+
\operatorname{tr}(H\Pi)-\operatorname{tr}(HQ).
\]

Write r=||N−AQ||_F and z=||Q−Pi||_F. In an H-eigenbasis, the total missing diagonal weight in the leading d directions equals the weight entering discarded directions. Each exchanged unit costs at least g. Consequently

\[
\operatorname{tr}(H\Pi)-\operatorname{tr}(HQ)\ge(g/2)z^2.
\]

Indeed ||Q−Pi||_F^2=2(d−tr(Q Pi)), and the spectral trace deficit is at least g(d−tr(Q Pi)). Therefore

\[
\|N-N_*\|_F\le r+\sqrt{\theta_1}z,
\]

and weighted Cauchy–Schwarz gives

\[
\|N-N_*\|_F^2
\le(1+2\theta_1/g)\{r^2+(g/2)z^2\}
\le(1+2\theta_1/g)\{J(P)-J(M_*)\}.
\]

The two SPD multipliers give ||N−N_*||_F^2≥k_min s_min||P−M_*||_F^2. Symmetric and skew-symmetric matrices are Frobenius-orthogonal, so every symmetric P satisfies ||P−M_*||_F^2≥a_*^2/4. Combining and minimizing over orthogonal P proves the lower bound.

### 2.3 Complete upper-bound proof

The residual A−N_*=A(I−Pi) has columns orthogonal to the range of N_*: Pi H(I−Pi)=0. For P_ran, N=K^(1/2)P_ran S^(1/2) has that same column range. The cross term vanishes, giving

\[
J(P_{\mathrm{ran}})-J(M_*)=
\|K^{1/2}(P_{\mathrm{ran}}-M_*)S^{1/2}\|_F^2.
\]

For P_row, the row space of P_row S^(1/2) is Pi's range, since the row space of M_* is the range of S^(−1/2)Pi. Thus the analogous cross term vanishes by row orthogonality, proving the second identity.

An idempotent M_* has block form [[I,C],[0,0]] in an orthonormal basis adapted to its range. Hence ||P_ran−M_*||_F^2=||C||_F^2=a_*^2/2. Apply the same argument to M_*^T and use transpose invariance of Frobenius norm to obtain ||P_row−M_*||_F^2=a_*^2/2. Multiplication by K^(1/2) and S^(1/2) gives the final upper bound.

The candidate identities and upper bound remain valid for any maximizing Pi when the cutoff is tied. The lower bound requires g>0 and must not be used at a tie.

### 2.4 Relation to the existing zero-price test and a useful example bound

Direct multiplication gives

\[
M_*-M_*^T=S^{-1/2}[S,\Pi]S^{-1/2}.
\]

Thus a_*=0 is precisely the existing gapped zero-price criterion. The result adds a size estimate; noncommutation of S and K alone still is not the relevant test.

For the example in section 1, a_*^2=7200/6649, k_min=s_min=1, g=sqrt(6649), and theta_1=(85+g)/2. Since g>81, the theorem gives the entirely rational certificate

\[
\Gamma_1\ge\frac{145800}{1642303}>0.08877.
\]

The row-space projector has discarded slope (sqrt(6649)+68)/135 and is a useful direct upper candidate. Its certified cost and penalty are included in the output. The exact global penalty from section 1 is much larger than this conservative analytic lower bound; the lower bound must not be described as sharp.

### 2.5 How input uncertainty enters a penalty certificate

Suppose ||Delta S||≤delta_S<s_min and ||Delta K||≤delta_K<k_min. This ensures the intended matrices remain SPD. Let r=n−d, and define

\[
\eta_H=s_{\max}\delta_K+
(k_{\max}+\delta_K)\delta_S
\frac{\sqrt{s_{\max}}+\sqrt{s_{\max}+\delta_S}}
{\sqrt{s_{\min}}+\sqrt{s_{\min}-\delta_S}}.
\]

Then ||H'−H||≤eta_H. To justify the square-root perturbation used here, D=S^(1/2)−S'^(1/2) solves S^(1/2)D+D S'^(1/2)=S−S'. Its integral solution is bounded by delta_S/(sqrt(s_min)+sqrt(s_min−delta_S)). Expand H'−H and apply operator norms to obtain eta_H.

Eigenvalue variational bounds imply that the unrestricted tail value changes by at most r eta_H. Entry 86's projector optimum bound changes by at most r{delta_K s_max+(k_max+delta_K)delta_S}. Therefore the penalty changes by at most

\[
B_\Gamma=r\{\eta_H+\delta_Ks_{\max}
+(k_{\max}+\delta_K)\delta_S\}.
\]

A certified nominal lower bound L and feasible nominal upper bound U yield [max(0,L−B_Gamma),U+B_Gamma] for the intended penalty. A strictly positive L−B_Gamma certifies positivity despite input uncertainty. The receiver metric and admissible class must stay fixed, as required in entry 85. These are deterministic norm bounds, not statistical confidence intervals without a measurement model.

## 3. An explicit conditioned nonlinear repair

### 3.1 System, encoder, and exact flow

Consider the declared native system on R²

\[
\dot x=\alpha x+\beta y^2,\qquad
\dot y=\gamma y,
\]

with known real parameters. The initial performance set is x²+y²≤1, and the receiver asks for x or its trajectory on [0,T]. Let Delta=2gamma−alpha≠0 and k=beta/Delta. The smooth encoder

\[
u=x-ky^2
\]

is a global submersion and closes exactly: u_dot=alpha u. For every h, its reduced update is u↦exp(alpha h)u. The exact response is

\[
x(t)=e^{\alpha t}u_0+k e^{2\gamma t}y_0^2.
\]

Subtracting k times d(y²)/dt verifies the differential identity; substitution gives the flow formula globally. The unit ball need not be invariant: performance here refers to initial states, and the global flow formula handles their whole finite trajectory.

If |Delta|≥s>0, q=|k|≤|beta|/s. On the unit ball the coordinate correction has magnitude at most q, gradient norm at most 2q, and Hessian norm 2q. This gives a concrete regular repair with explicit conditioning; it is not a general existence theorem for arbitrary nonlinear systems or a proof that this encoder is optimal among all encoders.

### 3.2 Exact trajectory error for this repaired encoder

With no code noise and arbitrary trajectory decoders into Lp(0,T), 1≤p≤infinity, the exact best worst-case error **for this encoder** is

\[
\boxed{e_{R,p}^*=\frac q2 D(q)\,\|e^{2\gamma t}\|_p},
\qquad
D(q)=\begin{cases}1,&0\le q\le1,\\2/q-1/q^2,&q>1.\end{cases}
\]

For a fixed u, put s=y². Its feasible values form a compact interval inside [0,1], defined by (u+k s)²+s≤1. The possible response trajectories are a line segment e^(alpha t)u+k e^(2gamma t)s. The segment's midpoint decoder attains half its diameter in every stated norm; triangle inequality gives the matching lower bound.

It remains to find the maximum feasible s-span d. Two states in one fibre obey |x'−x|=q d and |x'−x|≤sqrt(1−s)+sqrt(1−s−d)≤1+sqrt(1−d). For q≤1, span one is attained by (x,y)=(−k,0) and (0,1). For q>1, qd≤1+sqrt(1−d) gives d≤2/q−1/q². Equality is attained at (−sign(k),0) and (sign(k)(1−1/q),sqrt(d)). Thus D(q) is exact.

For q≤1, an especially useful globally optimal decoder is

\[
D(u)(t)=e^{\alpha t}u+(k/2)e^{2\gamma t}.
\]

Its gain from the scalar code to Lp is ||exp(alpha t)||_p. Its error is at most (q/2)||exp(2gamma t)||_p, and the above fibre attains the lower bound. It therefore gives the exact global error without requiring a pointwise midpoint selector.

## 4. Exact noise and decoder-gain tradeoff for the nonlinear coordinate

### 4.1 Complete scalar minimax formula

Let the decoder receive z=u+e, |e|≤nu, and let the current task be x. A single real decoder must work for every state in the initial unit ball and every permitted code error. Impose a Lipschitz cap L≥0. Reflection of x handles k<0, so only q=|k| matters.

For nu≥1 the exact error is one: the possible codes of native tasks ±1 overlap, and the zero decoder attains one. For q=0 and 0≤nu<1 it is max{nu,1−L(1−nu)}.

For q>0 and 0≤nu<1, define

\[
D_\nu=\begin{cases}
q+2\nu,&q\le1\ \text{and }2\nu\le1-q,\\
\dfrac{2q-1+\sqrt{(2q-1)^2+8q\nu}}{2q},&\text{otherwise},
\end{cases}
\]

\[
L_0=(1+2q)^{-1},\qquad
L_* =\begin{cases}1,&D_\nu\le1,\\
(1-2q+2qD_\nu)^{-1},&D_\nu>1.
\end{cases}
\]

Then the **attained** optimum is

\[
\boxed{
e_{L,\nu}^*(q)=\begin{cases}
1-L(1-\nu),&0\le L\le L_0,\\
\dfrac{(1+L(2q-1))^2}{8Lq}+L\nu,&L_0<L<L_*,\\
D_\nu/2,&L\ge L_*.
\end{cases}}
\]

Thus D_nu/2 is the unrestricted robust error floor, and L_* is the **minimum** finite gain that attains it. In particular, without noise the gain threshold is one for q≤1 and 1/(2q−1) for q>1. A growing correction k does not merely change the code's residual: it changes the attainable task error and the noise geometry.

### 4.2 Complete reduction to a one-dimensional maximum

Take two task values separated by d=|x'−x|, 0≤d≤2. The largest possible favorable difference s'−s is

\[
f(d)=\begin{cases}1,&d\le1,\\2d-d^2,&1<d\le2.\end{cases}
\]

For d≤1 use x'=0,x=−d; for d>1 use x'=d−1,x=−1. In both cases s=0, and s' can range from zero to f(d). Conversely the unit-ball constraints force s'−s≤f(d). Therefore the least possible noiseless code separation at task separation d is

\[
g_q(d)=\max\{0,d-q f(d)\},
\]

and every value used in this expression is attainable by lawful states. Adding code intervals of radius nu changes the minimum set distance to (g_q(d)−2nu)_+.

Entry 59's scalar envelope theorem now gives

\[
e_{L,\nu}^*(q)=\frac12\max_{0\le d\le2}
\{d-L(g_q(d)-2\nu)_+\}.
\]

D_nu is the largest d with g_q(d)≤2nu. Beyond D_nu the function g_q is increasing and convex. Its quadratic part is qd²+(1−2q)d; its linear part, if present, is d−q. The maximum is at d=2 when L≤L_0, at d=(1+L(2q−1))/(2Lq) in the intermediate regime, and at d=D_nu once L≥L_*. Substituting yields the three formulas above. The envelope theorem proves attainment, and the following affine construction gives an explicit independent upper certificate.

**Explicit optimal decoder for every cap.** For nu<1 and q>0, choose A=min(L,L_*), let a=1−A, and define

\[
M_A=\begin{cases}a,&A\le L_0,\\
Aq+\dfrac{a^2}{4Aq},&A>L_0,\end{cases}
\qquad B_A=(M_A-a)/2.
\]

Then

\[
\boxed{D_{L,\nu}(z)=Az+\operatorname{sign}(k)B_A}
\]

is globally L-Lipschitz and attains e_(L,nu)^*(q). For q=0 take A=min(L,1), B_A=0; for nu≥1 take D=0.

To verify this directly for k=q>0, the native residual before the bias is x−A(x−qs)=a x+Aq s. Its minimum on the ball is −a. Its maximum is max_(0≤s≤1){a sqrt(1−s)+Aq s}=M_A. The maximum is at s=0 in the first case, and at sqrt(1−s)=a/(2Aq) in the second. Subtracting B_A centers this interval, and independent code noise adds at most A nu at both ends. Hence the exact worst-case affine error is (M_A+a)/2+A nu. Substitution gives the claimed first or middle expression, or the plateau after A is capped at L_*. Reflection gives k<0. The pairwise lower bound already computed proves global optimality among **all** L-Lipschitz decoders, not only affine ones. Clipping the current-task decoder to [−1,1] preserves its gain and cannot increase error, so the same optimum is attainable if that interval is the accepted output range.

For a noiseless, realized code u with k≠0, its native fibre endpoints can be computed from

\[
k^2s^2+(2ku+1)s+u^2-1\le0,\qquad0\le s\le1.
\]

The correct root discriminant is 1+4ku+4k². These roots describe the exact code u. For a noisy measurement z, use the noise-aware completion constraints x²+s≤1, 0≤s≤1, and |z−(x−ks)|≤nu instead. A z outside the exact image R(K) can still be lawful. Reject only an empty completion set for the actual observation contract.

### 4.3 A sharp noisy trajectory result in the well-conditioned regime

If q+2nu≤1, the affine trajectory decoder from section 3, applied to the noisy code z, has the exact unrestricted minimax error

\[
\boxed{
e_{R,\nu,p}^*=\|\nu e^{\alpha t}+(q/2)e^{2\gamma t}\|_p.
}
\]

For the upper bound, its error is k(s−1/2)e^(2gamma t)−e exp(alpha t), bounded pointwise by the displayed positive function. For the lower bound, let sign(k)=sigma (choose either sign at k=0), and compare initial states (−sigma(q+2nu),0) and (0,1). They are lawful, their code intervals overlap, and their trajectories differ by sigma{2nu exp(alpha t)+q exp(2gamma t)}. Every common decoded trajectory has error at least half that norm. The affine decoder matches it.

For p=2, define I(a)=(exp(aT)−1)/a, with I(0)=T. Then

\[
(e_{R,\nu,2}^*)^2
=\nu^2 I(2\alpha)+(q^2/4)I(4\gamma)
+q\nu I(\alpha+2\gamma).
\]

This exact formula controls the declared **code** noise. If instead the native input measurement has Euclidean error at most rho, then the polynomial encoder gives the conservative conversion

\[
|\Delta u|\le\rho\sqrt{1+4q^2}+q\rho^2
\]

for a true initial state in the unit ball, before adding instrument or transmission noise. Expand Delta u=Delta x−k(2y Delta y+(Delta y)²) and use Cauchy–Schwarz. Unknown native measurement error must not be silently treated as exact initialization.

## 5. A decoder correction: pointwise optimality can destroy sensitivity

At k=1/2 with no noise, the fibrewise midpoint decoder for the **current** task, on realized codes −1≤u≤1, is

\[
D_{\mathrm{mid}}(u)=u/2-1/2+\tfrac12\sqrt{2u+2}.
\]

It is pointwise optimal within each fibre, yet it is not Lipschitz at u=−1. Set eta=1/(2j²). Its secant slope from −1 to −1+eta is exactly j+1/2, tending to infinity.

The corrected choice for a finite-sensitivity receiver is

\[
D_{\mathrm{stable}}(u)=u+1/4.
\]

This decoder has gain one and worst-case error exactly 1/4, the same **global** minimax error as the pointwise midpoint decoder. Since x=u+s/2 and 0≤s≤1, its error is |s/2−1/4|≤1/4. The full fibre at u=−1/2 forces every decoder to incur at least 1/4, and section 4 proves gain one is minimal for attaining that error.

The repair deliberately spends some unused local accuracy to control sensitivity without increasing the global error. This is a correction to the decoder choice for this new construction, not a counterexample to the existing scalar envelope theorem or to the Research Edition's already-stated separation of radius and regularity.

## 6. What happens at exact nonlinear resonance

Let alpha=2gamma, gamma≠0, and beta≠0. The nonresonant coefficient beta/(2gamma−alpha) is undefined and cannot be substituted into any preceding smooth-repair bound.

### 6.1 A fixed-step C2 obstruction without a regularity assumption on the update

Suppose a C2 scalar encoder R near the origin has R_x(0,0)≠0 and closes under one nonzero sampled step h>0 with a single-valued reduced update. Restrict r(x)=R(x,0), which is locally invertible, and put U=r^−1 R. Then U(x,0)=x. Axis closure forces the reduced update in this coordinate to be multiplication by exp(alpha h), so

\[
U(e^{\alpha h}(x+\beta h y^2),e^{\gamma h}y)
=e^{\alpha h}U(x,y)
\]

locally. This conclusion does not assume the original reduced update is differentiable; the axis determines it on a neighborhood of realized codes.

At x=0, write U(0,y)=A y+(B/2)y²+o(y²), with U_x(0,0)=1. Comparing linear terms gives A exp(gamma h)=A exp(2gamma h), hence A=0. Comparing quadratic terms then gives beta h exp(alpha h)=0, because exp(2gamma h)=exp(alpha h). This contradicts beta≠0. Thus no such C2 x-regular scalar repair exists even for this sampled contract.

The x-regular condition matters: retaining y alone is a smooth closed coordinate, but it does not satisfy R_x≠0. This obstruction is not a universal prohibition on one-coordinate nonlinear closure.

### 6.2 A C1 repair and its finite-horizon bound

The explicit coordinate

\[
U=x-(\beta/\gamma)y^2\log|y|,
\]

extended by U=x at y=0, is globally C1 and closes exactly as U_dot=alpha U. Its second y-derivative is unbounded at zero, so it is not C2. This is the quadratic specialization of the Research Edition's resonance example, with the growth-rate convention stated here.

On |y|≤1,

\[
|U-x|\le |\beta/\gamma|/(2e),\qquad
|\partial_y(U-x)|\le|\beta/\gamma|.
\]

The first bound maximizes −y²log|y| at |y|=exp(−1/2); the second maximizes |y(2log|y|+1)|, whose largest value is one. The finite-horizon decoder D(U_0)(t)=exp(2gamma t)U_0 has error bounded by

\[
|\beta|\left(T+\frac1{2e|\gamma|}\right)
\|e^{2\gamma t}\|_p.
\]

Indeed the omitted trajectory is exp(2gamma t){(beta/gamma)y_0²log|y_0|+beta t y_0²}; apply the two initial-state bounds and triangle inequality. This is an upper bound, not a claimed sharp resonant minimax value.

**Scope correction:** exact resonance changes the admissible regularity class. A C1 solution cannot be reported as a C2 conditioned repair, and the formula at gamma=0 remains inapplicable. General nonlinear repair and optimal encoder selection remain open.

## 7. Verification and integration status

The exact rational example certificate passed. Supplementary checks passed for 225 finite SPD instances, 150 finite noisy-decoder LP problems, 174 flow tests, exact rational secant ratios for the unstable midpoint, and three sharp noisy-trajectory witness pairs. The largest LP/formula difference was 1.11e−16. Random matrix and flow checks are numerical consistency evidence; the general statements above rely on their written proofs.

The earlier 108 review references remain a mixed register of broad gaps and worked subfindings, not 108 independent theorem failures. This continuation adds proofs and a demonstrated source correction rather than another counted batch of issues.

The original source's finite-precision slope is corrected. Issues 12 and 22 now have additional scoped progress; issues 18 and 21 have a solved nonlinear code/noise/gain family. The general nonlinear Jordan interior problem is still open. No result here constructs a physical Yang–Mills continuum theory, resolves Navier–Stokes, or validates the experimental Steadman constitutive model.

The methods include classical low-rank approximation, spectral-gap estimates, exact rational root isolation, scalar Lipschitz envelopes, and normal-form coordinates. No historical novelty, independent proof review, or formal certification of this implementation is claimed.


## Reproducible verification record

Script SHA-256: `62d9ad91300253c294ef2c42323ef7f479d556c05929bc4d905096fe22ec01da`.

Output SHA-256: `4fda666978078792820cc5616328d7990be983c357bb33d198b2749dcc4d697a`.

The rational certificate uses Python standard-library integer and Fraction arithmetic, including outward decimal conversion. The supplementary numerical checks use NumPy and SciPy.

```python
#!/usr/bin/env python3
"""Exact rational example certificate and supplementary development checks.

Sturm counts, interval arithmetic, and midpoint-instability ratios are exact.
LP and random matrix/flow computations are numerical consistency checks.
"""
from fractions import Fraction as F
from math import isqrt, exp, log, sqrt
import json
import numpy as np
from scipy.optimize import linprog

out={}; rng=np.random.default_rng(141026)

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def deriv(p): return trim([i*p[i] for i in range(1,len(p))] or [F(0)])
def peval(p,x):
    s=F(0)
    for a in reversed(p): s=s*x+a
    return s
def padd(p,q):
    return trim([(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0))
                 for i in range(max(len(p),len(q)))])
def pscale(p,c): return trim([c*x for x in p])
def pmul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return trim(r)
def pdiv(p,q):
    r=trim(p); q=trim(q); quotient=[F(0)]*max(1,len(r)-len(q)+1)
    while not(len(r)==1 and r[0]==0) and len(r)>=len(q):
        k=len(r)-len(q); a=r[-1]/q[-1]; quotient[k]+=a
        for j,b in enumerate(q): r[j+k]-=a*b
        r=trim(r)
    return trim(quotient),r
def sturm(p):
    seq=[trim(p),deriv(p)]
    while True:
        _,r=pdiv(seq[-2],seq[-1])
        if r==[F(0)]: break
        seq.append(pscale(r,F(-1)))
    return seq
def variation(seq,x):
    signs=[int(v>0)-int(v<0) for v in (peval(p,x) for p in seq)]
    signs=[s for s in signs if s]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def count(seq,a,b): return variation(seq,a)-variation(seq,b)
def refine_root(seq,a,b,width=F(1,10**36)):
    assert count(seq,a,b)==1
    while b-a>width:
        mid=(a+b)/2
        assert peval(seq[0],mid)!=0
        if count(seq,a,mid)==1: b=mid
        else: a=mid
    return (a,b)
def imul(a,b):
    vs=[x*y for x in a for y in b]; return (min(vs),max(vs))
def iadd(a,b): return (a[0]+b[0],a[1]+b[1])
def idiv(a,b):
    assert b[0]>0 or b[1]<0
    return imul(a,(1/b[1],1/b[0]))
def ipoly(p,x):
    r=(F(0),F(0))
    for a in reversed(p): r=iadd(imul(r,x),(a,a))
    return r
def decimal_endpoint(x,rounding,places=21):
    scale=10**places; num=x.numerator*scale; den=x.denominator
    value=num//den if rounding=='floor' else -((-num)//den)
    a=abs(value)
    return ('-' if value<0 else '')+str(a//scale)+'.'+str(a%scale).zfill(places)
def decimal_interval(interval,places=21):
    return [decimal_endpoint(interval[0],'floor',places),
            decimal_endpoint(interval[1],'ceiling',places)]

# The stationary quartic is derived exactly from the objective, then every
# real root is counted independently of floating-point root estimates.
N=pmul([F(17,2),F(-15),F(17,2)],[F(9),F(0),F(1)])
den=[F(1),F(0),F(2),F(0),F(1)]
p=padd(pmul(deriv(N),[F(1),F(0),F(1)]),pscale(pmul([F(0),F(1)],N),F(-4)))
assert p==[F(-135),F(-136),F(360),F(-136),F(15)]
seq=sturm(p); assert len(seq[-1])==1 and seq[-1][0]!=0
bound=F(25)
assert all(abs(a/p[-1])<=24 for a in p[:-1])
assert count(seq,-bound,bound)==2
pos=refine_root(seq,F('1.13317744357142'),F('1.13317744357143'))
neg=refine_root(seq,F('-.42738776834928'),F('-.42738776834927'))
assert count(seq,*pos)==1 and count(seq,*neg)==1
assert pos[1]<F('1.133178865')  # outside rounding interval of the old slope
def cost_interval(t): return idiv(ipoly(N,t),ipoly(den,t))
jpos=cost_interval(pos); jneg=cost_interval(neg)
assert jpos[1]<F(17,2)<jneg[0]
scale=10**45; z=isqrt(6649*scale*scale)
gamma=(F(z,scale),F(z+1,scale))
assert gamma[0]**2<6649<gamma[1]**2
jlin=((85-gamma[1])/2,(85-gamma[0])/2)
price=(jpos[0]-jlin[1],jpos[1]-jlin[0])
rational_row_slope=((gamma[0]+68)/135,(gamma[1]+68)/135)
rowcost=cost_interval(rational_row_slope)
rowprice=(rowcost[0]-jlin[1],rowcost[1]-jlin[0])
assert jpos[1]<rowcost[0]
rational_lower=F(145800,1642303)
assert price[0]>rational_lower>F('0.08877')
out['strict_projector_example']={
    'arithmetic':'exact Fraction Sturm counts and rational interval evaluation',
    'real_root_count':2,
    'positive_stationary_slope':decimal_interval(pos),
    'negative_stationary_slope':decimal_interval(neg),
    'projector_optimum':decimal_interval(jpos),
    'other_stationary_value':decimal_interval(jneg),
    'vertical_value':'17/2',
    'unrestricted_optimum':decimal_interval(jlin),
    'projector_price':decimal_interval(price),
    'explicit_row_projector_cost':decimal_interval(rowcost),
    'explicit_row_projector_price':decimal_interval(rowprice),
    'analytic_rational_lower':str(rational_lower),
    'stationary_quartic_low_to_high':[str(v) for v in p],
    'sturm_polynomials_low_to_high':[[str(v) for v in q] for q in seq],
    'isolating_rational_intervals':{'positive':[str(v) for v in pos],'negative':[str(v) for v in neg]}}

# General gapped bounds, exact range-projector identity, and independent
# rank-d approximation decomposition are checked numerically.
def sqrtspd(A):
    v,U=np.linalg.eigh(A); return (U*np.sqrt(v))@U.T
matrix_cases=0; max_identity_gap=0.; max_rank_gap=0.
for n in range(2,7):
    for d in range(1,n):
        for _ in range(15):
            A=rng.normal(size=(n,n)); S=A@A.T+.5*np.eye(n)
            A=rng.normal(size=(n,n)); K=A@A.T+.5*np.eye(n)
            sh=sqrtspd(S); kh=sqrtspd(K); H=sh@K@sh
            theta,V=np.linalg.eigh(H); ix=np.argsort(theta)[::-1]
            theta=theta[ix]; V=V[:,ix]; leading=V[:,:d]; Pi=leading@leading.T
            gap=theta[d-1]-theta[d]; assert gap>0
            M=sh@Pi@np.linalg.inv(sh)
            W,_=np.linalg.qr(sh@leading); P=W@W.T
            jlin=sum(theta[d:])
            obj=lambda Z:np.linalg.norm(kh@(np.eye(n)-Z)@sh,'fro')**2
            Wrow,_=np.linalg.qr(np.linalg.solve(sh,leading)); Prow=Wrow@Wrow.T
            candidates=[P,Prow]
            candidate_errors=[]
            for Pc in candidates:
                identity=np.linalg.norm(kh@(Pc-M)@sh,'fro')**2
                max_identity_gap=max(max_identity_gap,abs(obj(Pc)-jlin-identity))
                assert abs(obj(Pc)-jlin-identity)<1e-8
                candidate_errors.append(identity)
            skew=np.linalg.norm(M-M.T,'fro')**2
            kmin=np.linalg.eigvalsh(K)[0]; smin=np.linalg.eigvalsh(S)[0]
            lower=kmin*smin*skew/(4*(1+2*theta[0]/gap))
            upper=np.linalg.norm(K,2)*np.linalg.norm(S,2)*skew/2
            for Pc,identity in zip(candidates,candidate_errors):
                assert lower<=identity+1e-9 and identity<=upper+1e-8
                assert abs(np.linalg.norm(Pc-M,'fro')**2-skew/2)<1e-9
            Z,_=np.linalg.qr(rng.normal(size=(n,d))); Pr=Z@Z.T
            assert obj(Pr)-jlin>=lower-1e-8
            nativeA=kh@sh
            N=rng.normal(size=(n,d))@rng.normal(size=(d,n))
            _,_,rv=np.linalg.svd(N,full_matrices=False); PiN=rv[:d].T@rv[:d]
            r2=np.linalg.norm(N-nativeA@PiN,'fro')**2
            deficit=np.trace(H@(Pi-PiN))
            excess=np.linalg.norm(nativeA-N,'fro')**2-jlin
            max_rank_gap=max(max_rank_gap,abs(excess-r2-deficit))
            assert abs(excess-r2-deficit)<1e-8
            assert deficit>=gap/2*np.linalg.norm(Pi-PiN,'fro')**2-1e-9
            assert np.linalg.norm(N-nativeA@Pi,'fro')**2<= (1+2*theta[0]/gap)*excess+1e-8
            ds=.01*np.diag([(-1)**i*(i+1)/n for i in range(n)])
            dk=.007*np.diag([(-1)**(i+1)*(n-i)/n for i in range(n)])
            Sp=S+ds; Kp=K+dk; shp=sqrtspd(Sp); Hp=shp@Kp@shp
            se=np.linalg.norm(ds,2); ke=np.linalg.norm(dk,2)
            sm=np.linalg.norm(S,2); km=np.linalg.norm(K,2)
            eta=sm*ke+(km+ke)*se*(sqrt(sm)+sqrt(sm+se))/(sqrt(smin)+sqrt(smin-se))
            assert np.linalg.norm(Hp-H,2)<=eta+1e-10
            newtheta=np.linalg.eigvalsh(Hp)[::-1]
            assert abs(sum(newtheta[d:])-jlin)<=(n-d)*eta+1e-9
            fixed_bound=(n-d)*(ke*sm+(km+ke)*se)
            assert abs(np.trace(Kp@(np.eye(n)-P)@Sp@(np.eye(n)-P))-obj(P))<=fixed_bound+1e-8
            matrix_cases+=1
out['general_projector_bounds']={'numeric_matrix_instances':matrix_cases,
    'maximum_candidate_identity_gap':max_identity_gap,'maximum_rank_decomposition_gap':max_rank_gap,
    'matrix_uncertainty_bound_checks':matrix_cases}

# Scalar robust error curve for the quadratic normal-form encoder.
def nonlinear_curve(q,nu,L):
    if nu>=1: return 1.,2.,0.
    if q==0: return max(nu,1-L*(1-nu)),(2. if L<=1 else 2*nu),1.
    if q<=1 and 2*nu<=1-q: D=q+2*nu
    else: D=(2*q-1+sqrt((2*q-1)**2+8*q*nu))/(2*q)
    Lstar=1. if D<=1 else 1/(1-2*q+2*q*D)
    L0=1/(1+2*q)
    if L<=L0: val=1-L*(1-nu)
    elif L<Lstar: val=(1+L*(2*q-1))**2/(8*L*q)+L*nu
    else: val=D/2
    if L<=L0: d=2.
    elif L<Lstar: d=(1+L*(2*q-1))/(2*L*q)
    else: d=D
    return val,d,Lstar

lp_cases=0; max_lp_gap=0.
for q in [0.,.1,.5,1.,2.,5.]:
    for nu in [0.,.05,.3,.9,1.1]:
        for L in [0.,.1,.5,1.,3.]:
            exact,d,_=nonlinear_curve(q,nu,L)
            if nu>=1:
                again=0.; bias=0.
            else:
                _,_,gain_star=nonlinear_curve(q,nu,L)
                again=min(L,gain_star)
                if q==0 or again<=1/(1+2*q):
                    bias=0.
                else:
                    mval=again*q+(1-again)**2/(4*again*q)
                    bias=(mval-(1-again))/2
            natives=[(-1.,0.),(1.,0.),(0.,1.),(0.,0.)]
            for _ in range(6):
                x=rng.uniform(-1,1); s=rng.uniform(0,max(0,1-x*x)); natives.append((x,s))
            xh=0. if d<=1 else d-1
            xl=xh-d; cap=1-xh*xh
            natives.extend([(xl,0.),(xh,min(cap,d/q) if q>0 else 0.)])
            sign=1 if lp_cases%2==0 else -1
            natives=[(sign*x,s) for x,s in natives]
            k=sign*q; targets=[x for x,s in natives]
            for x,s in natives:
                for enoise in [-nu,nu]:
                    predicted=again*(x-k*s+enoise)+sign*bias
                    assert abs(predicted-x)<=exact+1e-10
            centers=[x-k*s for x,s in natives]
            intervals=[(c-nu,c+nu) for c in centers]
            zs=sorted(set(z for i in intervals for z in i)); size=len(zs)+1
            aub=[]; bub=[]
            for t,(lo,hi) in zip(targets,intervals):
                for j,z in enumerate(zs):
                    if not lo-1e-13<=z<=hi+1e-13: continue
                    row=[0.]*size; row[j]=1; row[-1]=-1; aub.append(row); bub.append(t)
                    row=[0.]*size; row[j]=-1; row[-1]=-1; aub.append(row); bub.append(-t)
            for j in range(len(zs)-1):
                row=[0.]*size; row[j]=1; row[j+1]=-1
                aub.append(row); bub.append(L*(zs[j+1]-zs[j]))
                aub.append([-v for v in row]); bub.append(L*(zs[j+1]-zs[j]))
            sol=linprog([0.]*(size-1)+[1.],A_ub=aub,b_ub=bub,
                bounds=[(None,None)]*(size-1)+[(0,None)],method='highs')
            assert sol.success
            diff=abs(sol.fun-exact); max_lp_gap=max(max_lp_gap,diff)
            assert diff<1e-8,(q,nu,L,exact,sol.fun,d)
            lp_cases+=1
out['nonlinear_noisy_decoder']={'finite_lp_problems':lp_cases,'maximum_numeric_gap':max_lp_gap,
    'explicit_affine_decoders':'checked at the witness and sampled states with both noise endpoints',
    'scope':'finite problems include extremal witness pairs; the continuum result relies on the proof'}

# Exact instability of a fibrewise midpoint; a gain-one affine decoder is
# globally minimax at q=1/2 and needs no such singularity.
ratios=[]
for j in [2,4,8,16,32,64,128,256]:
    eta=F(1,2*j*j)
    change=eta/2+F(1,2*j)
    ratio=change/eta
    assert ratio==F(1,2)+j
    ratios.append(str(ratio))
for xi in range(-12,13):
    x=F(xi,12)
    for si in range(145):
        s=F(si,144)
        if x*x+s>1: continue
        u=x-s/2; affine=u+F(1,4)
        assert abs(x-affine)<=F(1,4)
out['stable_decoder_correction']={'exact_secant_ratios':ratios,'gain_one_bound':'exact rational grid'}

# Nonresonant and resonant semiconjugacy; numerical consistency supplements
# the algebraic flow proofs. Include states outside the performance ball.
flow_cases=0; max_flow_gap=0.
for _ in range(150):
    gamma=float(rng.uniform(-1,1))
    gap=float(rng.choice([-1,1])*rng.uniform(.2,2)); alpha=2*gamma-gap
    beta=float(rng.uniform(-1,1)); k=beta/gap
    x,y=rng.uniform(-2,2,2); t=float(rng.uniform(0,1))
    xt=exp(alpha*t)*x+k*(exp(2*gamma*t)-exp(alpha*t))*y*y
    yt=exp(gamma*t)*y
    a=xt-k*yt*yt; b=exp(alpha*t)*(x-k*y*y)
    rel=abs(a-b)/(1+abs(a)+abs(b)); max_flow_gap=max(max_flow_gap,rel)
    assert rel<1e-12; flow_cases+=1
for gamma in [-.7,-.2,.2,.7]:
    for beta in [-.5,.3]:
        for x,y in [(.2,0.),(-1.,.3),(.5,-.8)]:
            t=.4; alpha=2*gamma
            xt=exp(alpha*t)*(x+beta*t*y*y); yt=exp(gamma*t)*y
            def u(x,y): return x if y==0 else x-beta/gamma*y*y*log(abs(y))
            a=u(xt,yt); b=exp(alpha*t)*u(x,y)
            rel=abs(a-b)/(1+abs(a)+abs(b)); max_flow_gap=max(max_flow_gap,rel)
            assert rel<1e-12; flow_cases+=1
out['nonlinear_exact_flow']={'numeric_flow_tests':flow_cases,'maximum_relative_gap':max_flow_gap}

# Noisy trajectory minimax: explicit common-code antipodal-in-loss witnesses
# attain the pointwise bound under q+2nu<=1. Compute the L2 value by integration.
def integ_exp(a,T): return T if abs(a)<1e-14 else np.expm1(a*T)/a
trajectory_cases=[]
for k,nu,gamma,gap in [(F(1,5),F(1,10),-.4,.8),
                        (F(-1,2),F(1,20),.3,.5),
                        (F(4,5),F(1,20),.2,-.6)]:
    q=abs(k); assert q+2*nu<=1
    alpha=2*gamma-gap; T=.7
    sgn=1 if k>0 else -1
    xA=-sgn*(q+2*nu); sA=F(0); xB=F(0); sB=F(1)
    uA=xA-k*sA; uB=xB-k*sB
    assert abs(uA-uB)==2*nu and xA*xA+sA<=1 and xB*xB+sB<=1
    mid=(uA+uB)/2
    times=np.linspace(0,T,1001)
    pa=np.exp(alpha*times)*float(uA)
    pb=np.exp(alpha*times)*float(uB)+float(k)*np.exp(2*gamma*times)
    decoder=np.exp(alpha*times)*float(mid)+float(k)/2*np.exp(2*gamma*times)
    bound=float(q)/2*np.exp(2*gamma*times)+float(nu)*np.exp(alpha*times)
    assert np.allclose(np.abs(pa-decoder),bound) and np.allclose(np.abs(pb-decoder),bound)
    norm2=float(q)**2/4*integ_exp(4*gamma,T)+float(nu)**2*integ_exp(2*alpha,T)
    norm2+=float(q*nu)*integ_exp(alpha+2*gamma,T)
    trajectory_cases.append({'k':str(k),'nu':str(nu),'exact_formula_l2_value_numeric':sqrt(norm2)})
out['sharp_noisy_trajectory']={'cases':trajectory_cases,'witness_points':'rational and lawful'}
out['scope']={'exact':'Sturm/interval certificate and stated rational checks.',
              'numerical':'LP, flow, and random matrix checks are consistency checks.',
              'proof':'General mathematical results rely on written derivations, not sampling.',
              'excluded':'No independent review, formal proof verification, or physical-model validation.'}
print(json.dumps(out,indent=2))
```

```json
{
  "strict_projector_example": {
    "arithmetic": "exact Fraction Sturm counts and rational interval evaluation",
    "real_root_count": 2,
    "positive_stationary_slope": [
      "1.133177443571420609339",
      "1.133177443571420609340"
    ],
    "negative_stationary_slope": [
      "-0.427387768349278916181",
      "-0.427387768349278916180"
    ],
    "projector_optimum": [
      "4.764704743750686474003",
      "4.764704743750686474004"
    ],
    "other_stationary_value": [
      "108.085833626667231647117",
      "108.085833626667231647118"
    ],
    "vertical_value": "17/2",
    "unrestricted_optimum": [
      "1.729299736207620541055",
      "1.729299736207620541056"
    ],
    "projector_price": [
      "3.035405007543065932948",
      "3.035405007543065932949"
    ],
    "explicit_row_projector_cost": [
      "4.771660901141995519134",
      "4.771660901141995519135"
    ],
    "explicit_row_projector_price": [
      "3.042361164934374978078",
      "3.042361164934374978079"
    ],
    "analytic_rational_lower": "145800/1642303",
    "stationary_quartic_low_to_high": [
      "-135",
      "-136",
      "360",
      "-136",
      "15"
    ],
    "sturm_polynomials_low_to_high": [
      [
        "-135",
        "-136",
        "360",
        "-136",
        "15"
      ],
      [
        "-136",
        "720",
        "-408",
        "60"
      ],
      [
        "3181/15",
        "-306",
        "256/5"
      ],
      [
        "-562275/8192",
        "-721735/4096"
      ],
      [
        "-7482609664/22070535"
      ]
    ],
    "isolating_rational_intervals": {
      "positive": [
        "107025583573311707974773351205212307/94447329657392904273920000000000000",
        "2140511671466234159495467024104246141/1888946593147858085478400000000000000"
      ],
      "negative": [
        "-807312668976436379911247441917813939/1888946593147858085478400000000000000",
        "-403656334488218189955623720958906969/944473296573929042739200000000000000"
      ]
    }
  },
  "general_projector_bounds": {
    "numeric_matrix_instances": 225,
    "maximum_candidate_identity_gap": 2.8133051444001467e-13,
    "maximum_rank_decomposition_gap": 9.663381206337363e-13,
    "matrix_uncertainty_bound_checks": 225
  },
  "nonlinear_noisy_decoder": {
    "finite_lp_problems": 150,
    "maximum_numeric_gap": 1.1102230246251565e-16,
    "explicit_affine_decoders": "checked at the witness and sampled states with both noise endpoints",
    "scope": "finite problems include extremal witness pairs; the continuum result relies on the proof"
  },
  "stable_decoder_correction": {
    "exact_secant_ratios": [
      "5/2",
      "9/2",
      "17/2",
      "33/2",
      "65/2",
      "129/2",
      "257/2",
      "513/2"
    ],
    "gain_one_bound": "exact rational grid"
  },
  "nonlinear_exact_flow": {
    "numeric_flow_tests": 174,
    "maximum_relative_gap": 3.0311205651279327e-16
  },
  "sharp_noisy_trajectory": {
    "cases": [
      {
        "k": "1/5",
        "nu": "1/10",
        "exact_formula_l2_value_numeric": 0.11740223730303903
      },
      {
        "k": "-1/2",
        "nu": "1/20",
        "exact_formula_l2_value_numeric": 0.30499495842990704
      },
      {
        "k": "4/5",
        "nu": "1/20",
        "exact_formula_l2_value_numeric": 0.448897975763236
      }
    ],
    "witness_points": "rational and lawful"
  },
  "scope": {
    "exact": "Sturm/interval certificate and stated rational checks.",
    "numerical": "LP, flow, and random matrix checks are consistency checks.",
    "proof": "General mathematical results rely on written derivations, not sampling.",
    "excluded": "No independent review, formal proof verification, or physical-model validation."
  }
}
```


---

# BM closure addendum — finite global projector certificates and review dispositions

Date: 14 October 2026. This is a dated Research Edition extension. It does not alter the frozen Foundation or assign canonical theorem identifiers.

## 1. What the previous review did and did not establish

The review register mixed three different outcomes: a corrected mathematical claim, a completed calculation under specified hypotheses, and a broader research or application obligation. These must not be treated as interchangeable defects. In particular, entries 59–108 are fifty worked audit questions, not fifty unresolved errors. Each already contains a formula, proof, counterexample, or verification procedure. A procedure that requires application inputs does not establish that those inputs have been supplied or checked.

The eleven historical corrections listed in the register have dispositions; the inaccurate stationary slope found on 14 October is also corrected and globally certified. The conservative replacement for the unsupported PDE covering estimate closes that published bound's certification problem; it does not prove the shorter estimate false. No uncorrected counterexample to the properly scoped amended T01–T55 core was established by this review. This is an evidence statement about this review, rather than a certificate that no error can exist.

The original blanket statement that general finite higher-rank projector optimization is "open" is too broad once a constructive global approximation certificate is supplied. The following result closes that finite certification question for arbitrary rational positive-definite input matrices, at every requested positive tolerance. Closed forms, polynomial efficiency, and independently verified implementations are separate claims.

## 2. General finite global projector certificate

Let S and K be rational symmetric positive-definite n by n matrices. Fix an integer 0 < d < n, put r=n-d, and define

\[
\mathcal P_d=\{P:P=P^\top=P^2,\ \operatorname{tr}P=d\},\qquad
J(P)=\operatorname{tr}[K(I-P)S(I-P)].
\]

Let sbar and kbar be rational upper bounds for the operator norms of S and K. The maximum absolute row sum is one such bound for a symmetric matrix. Let

\[
B=\left\lceil\sqrt{2rnd}\right\rceil,\qquad
q\ge\max\left\{nd,\left\lceil\frac{B\,\mathrm{kbar}\,\mathrm{sbar}}{\varepsilon}\right\rceil\right\},
\]

where epsilon is any positive rational tolerance. Enumerate every n by d matrix V whose entries belong to {i/q:-q <= i <= q}. Discard matrices without full column rank, and compute exactly

\[
P_V=V(V^\top V)^{-1}V^\top.
\]

Let Pbest minimize the rational value J(P_V) over this finite enumeration, and put U=J(Pbest). Then

\[
\boxed{\quad
\max\{0,U-B\,\mathrm{kbar}\,\mathrm{sbar}/q\}
\ \le J_{d,\mathrm{proj}}^*\le U,
\qquad U-J_{d,\mathrm{proj}}^*\le\varepsilon.
\quad}
\]

All computed candidates and bounds are rational. No spectral gap, unique minimizer, numerical stationary point, or rank-one moment assumption is needed. The enumeration contains at most (2q+1)^(nd) matrices. This is a terminating global certificate, with a quantified and potentially enormous cost; it is not an efficient general algorithm.

For d=0 the only projector is zero and the value is tr(KS); for d=n the only projector is I and the value is zero. These endpoint cases require no enumeration.

### Proof: existence, coverage, and objective error

The projector constraints define a closed bounded subset of a finite-dimensional Euclidean space: every such P has Frobenius norm sqrt(d). The set is nonempty, so the continuous polynomial J attains its minimum.

Take any P in this set and choose an n by d orthonormal frame W with P=WW^T. Every entry of W is in [-1,1]. Round its entries to the nearest grid values to obtain V. Then

\[
\|V-W\|_F\le\frac{\sqrt{nd}}{2q}<1.
\]

For every unit a in R^d, ||Va|| >= ||Wa||-||(V-W)a|| > 0. Thus V has full column rank and is among the retained candidates. Write P_V for its orthogonal range projector. Equal-rank projectors satisfy

\[
\|P-P_V\|_F^2
=2d-2\operatorname{tr}(PP_V)
=2\|(I-P_V)W\|_F^2
\le2\|W-V\|_F^2
\le\frac{nd}{2q^2}.
\]

The inequality uses (I-P_V)V=0 and the operator norm of I-P_V being at most one. Consequently the enumerated projectors cover the entire admissible set within radius sqrt(nd/2)/q, including singular coordinate charts and tied optimal subspaces.

For Q=I-P, let A_P=K^(1/2) Q S^(1/2). Its Frobenius norm is at most sqrt(r kbar sbar). Also

\[
\|A_P-A_{P'}\|_F
\le\sqrt{\mathrm{kbar}\,\mathrm{sbar}}\,\|P-P'\|_F.
\]

The difference-of-squares inequality therefore gives

\[
|J(P)-J(P')|
\le2\sqrt r\,\mathrm{kbar}\,\mathrm{sbar}\,\|P-P'\|_F.
\]

Apply this to an attained global optimizer and its rounded frame. That grid candidate has cost at most the optimum plus kbar sbar sqrt(2rnd)/q. The minimum grid cost can only be smaller. Its feasibility provides the upper bound; nonnegativity provides the optional lower bound by zero. The definition of B and q completes the proof.

An individual rational feasible projector certifies only an upper bound. The lower certificate also requires verification of the grid minimum and the coverage/error argument. Checking only the winning candidate or only sampled grid points is insufficient. The supplied implementation exhausts the stated demo grid; for other inputs it must run the corresponding complete enumeration, or use another rigorously justified lower certificate.

### A sharper optional Lipschitz constant

When S and K are near scalar matrices, the preceding bound needlessly charges for the constant part of the objective. Choose rational sigma and kappa, and put

\[
\Delta S=S-\sigma I,\quad \Delta K=K-\kappa I,\quad
A=\kappa\Delta S+\sigma\Delta K.
\]

Since Q is a rank-r projector,

\[
J(P)=\kappa\sigma r+\operatorname{tr}(AQ)
+\operatorname{tr}(\Delta K Q\Delta S Q).
\]

The linear term has Lipschitz constant ||A||_F. Expand the last term's difference as

\[
\operatorname{tr}[\Delta K(Q-Q')\Delta S Q]
+\operatorname{tr}[\Delta K Q'\Delta S(Q-Q')].
\]

Frobenius Cauchy–Schwarz bounds each by sqrt(r)||Delta K||op||Delta S||op||Q-Q'||F. Hence a valid alternative is

\[
L_c=\|A\|_F+2\sqrt r\,\|\Delta K\|_{\rm op}\|\Delta S\|_{\rm op}.
\]

Use certified rational upper bounds for these norms and square roots. The covering error becomes L_c sqrt(nd/2)/q. The smaller of the original error coefficient and this certified coefficient may be used to select q. The implementation's square-root upper bounds use integer arithmetic and explicitly check their squared values, rather than trusting decimal rounding.

### Exact enumerated demonstration

For

\[
S=\operatorname{diag}(11/10,9/10),\qquad
K=\begin{pmatrix}1&1/10\\1/10&1\end{pmatrix},\quad d=1,
\]

the matrices do not commute. With sigma=kappa=1, L_c=11/50 and the covering factor sqrt(nd/2)=1. At tolerance 1/250, q=55 suffices. All 12,321 integer-grid matrices were visited; 12,320 have full rank. The exact winner is

\[
P_{\rm best}=\frac1{1970}
\begin{pmatrix}1681&697\\697&289\end{pmatrix}.
\]

The globally certified interval is

\[
\frac{20849618}{24255625}
\ \le J_{1,\mathrm{proj}}^*
\ \le\frac{41893281}{48511250},
\]

whose exact width is 1/250. Outward decimal display is [0.859578675049601896467, 0.863578675049601896468]. This interval comes from exhaustive rational enumeration and a covering proof, rather than a local solver's status.

### Certified input uncertainty

Suppose the intended matrices S' and K' are positive semidefinite and satisfy ||S'-S||op <= deltaS and ||K'-K||op <= deltaK. For every rank-d P, expansion of K'QS'Q-KQSQ gives

\[
|J'(P)-J(P)|\le
\eta=r\{\delta K\,\mathrm{sbar}+(\mathrm{kbar}+\delta K)\delta S\}.
\]

For example, |tr(Delta K Q S Q)| <= deltaK sbar r; the other term is bounded in the same way using ||K'||op <= kbar+deltaK. Taking minima gives the same bound for the optimum values. Thus a nominal interval [L,U] implies the intended interval [max(0,L-eta),U+eta]. The nominal Pbest remains a feasible projector, with intended cost at most U+eta and intended suboptimality at most epsilon+2eta. Smaller solver tolerances alone cannot remove fixed physical input uncertainty.

## 3. An exact noncommuting example with two retained and two discarded dimensions

Set

\[
S_0=\operatorname{diag}(9,1),\qquad
K_0=\begin{pmatrix}17/2&-15/2\\-15/2&17/2\end{pmatrix},
\qquad S=\operatorname{diag}(S_0,S_0),\quad K=\operatorname{diag}(K_0,K_0),\quad d=2.
\]

Let m be the minimum of (v^T K_0 v)(v^T S_0 v) over unit v in R^2. The previous rational Sturm certificate establishes m as the two-dimensional projector value and isolates its minimizing slope t in

[1.133177443571420609339, 1.133177443571420609340].

Every unit w=(w1,w2) in R^4 has (w^T K w)(w^T S w) >= m. Indeed, put a_i=||wi||^2 and normalize each nonzero wi. Their unit quadratic forms k_i,s_i satisfy k_i s_i >= m, so Cauchy–Schwarz gives

\[
\left(\sum_i a_i k_i\right)\left(\sum_i a_i s_i\right)
\ge\left(\sum_i a_i\sqrt{k_i s_i}\right)^2\ge m,
\qquad \sum_i a_i=1.
\]

Now choose an orthonormal basis u1,u2 for any rank-two discarded subspace and rotate that basis to diagonalize its compressed S. Its projector cost is

\[
\operatorname{tr}[(U^T K U)(U^T S U)]
=\sum_{j=1}^2(u_j^T K u_j)(u_j^T S u_j)\ge2m.
\]

Choose u1=(v,0), u2=(0,v), where v=(1,t)/sqrt(1+t^2) is a minimizing vector. The cross-block forms vanish, so equality holds. This proves global optimality across every rank-two subspace, including those that mix the blocks. The retained projector is I-diag(vv^T,vv^T).

The previously certified two-dimensional Sturm intervals give the following outward bounds:

| Quantity | Certified interval |
|---|---|
| Projector optimum | [9.529409487501372948007, 9.529409487501372948008] |
| Unrestricted rank-two optimum | [3.458599472415241082110, 3.458599472415241082111] |
| Positive projector admissibility penalty | [6.070810015086131865896, 6.070810015086131865897] |

The unrestricted value follows because the two eigenvalues of S0^(1/2) K0 S0^(1/2) each occur twice; the smaller is (85-sqrt(6649))/2. This is a structured exact higher-rank example. The arbitrary-input result is the finite net theorem, which does not require this block structure.

## 4. Closure standard and verification record

For review item 22, the request for finite global matching bounds is resolved to every prescribed positive tolerance for rational SPD inputs. The actual optimizer exists. The output provides a feasible epsilon-optimal rational projector and a rigorous optimum interval; it does not necessarily produce an exactly optimal rational projector. Computational efficiency and a general closed-form optimizer remain unestablished. Arbitrary noncomputable real inputs are not finite algorithm inputs.

For item 35, the present reported projector results have the required exact certificate. The verification contract for future solver outputs is explicit; it must be applied to each actual output. This does not certify uninspected quantum solver runs.

The standalone implementation uses Python's fractions.Fraction and integer square-root arithmetic. It exhaustively verifies the noncommuting demo and performs 30 additional exact rational coverage/Lipschitz/uncertainty checks, covering every rank 1 <= d < n for dimensions 2 through 6, twice each. It also reconstructs the Sturm root count and interval calculation used by the higher-rank example. These checks support the implementation and examples. The general guarantee rests on the written proof above. Independent review, formal proof checking, historical priority, and physical-model validation are not claimed.

The corrected review dispositions identify completed repairs separately from missing source material, unproved broader results, missing physical definitions/data, and unverified implementation behavior. Those latter obligations cannot be marked complete by changing a status label.

## Reproducible closing verification package

Run the following standalone Python 3 script. It requires only the standard library. SHA-256 of the UTF-8 script: `695fc2b18a09eb18bb75de34816dc51326491bf9f554019f3c330793d3c30476`. SHA-256 of the captured UTF-8 JSON output: `6f6da0c3345cebd3a03e27bc7c9c310d570607b5735a571e5098f5ce4ca6131b`.

```python
#!/usr/bin/env python3
"""Rational finite projector certificates; no floating-point optimization.

The general guarantees follow from the accompanying net-coverage proof.
The enumerated demo, rational matrix checks, and Sturm certificate are exact.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt, ceil
from random import Random
import json


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in bt] for row in a]


def add(a, b, scale=F(1)):
    return [[x+scale*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def times(a, t):
    return [[t*x for x in row] for row in a]


def trace(a):
    return sum((row[i] for i, row in enumerate(a)), F(0))


def frob2(a):
    return sum((x*x for row in a for x in row), F(0))


def row_bound(a):
    return max(sum(abs(x) for x in row) for row in a)


def inverse(a):
    n = len(a)
    z = [list(row)+ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if z[i][j]), None)
        if pivot is None:
            return None
        z[j], z[pivot] = z[pivot], z[j]
        divisor = z[j][j]
        z[j] = [x/divisor for x in z[j]]
        for i in range(n):
            if i != j:
                c = z[i][j]
                z[i] = [x-c*y for x, y in zip(z[i], z[j])]
    return [row[n:] for row in z]


def is_spd(a):
    if a != transpose(a):
        return False
    z = [list(row) for row in a]
    for j in range(len(z)):
        if z[j][j] <= 0:
            return False
        pivot = z[j][j]
        for i in range(j+1, len(z)):
            for k in range(j+1, len(z)):
                z[i][k] -= z[i][j]*z[j][k]/pivot
    return True


def projector(v):
    vt = transpose(v)
    ginv = inverse(mul(vt, v))
    return None if ginv is None else mul(mul(v, ginv), vt)


def cost(s, k, p):
    q = add(eye(len(s)), p, F(-1))
    return trace(mul(mul(mul(k, q), s), q))


def sqrt_upper(x, places=12):
    scale = 10**places
    value = x*scale*scale
    z = isqrt(value.numerator//value.denominator)
    if F(z*z) < value:
        z += 1
    result = F(z, scale)
    assert result*result >= x
    return result


def ceil_sqrt(x):
    z = isqrt(x)
    return z if z*z == x else z+1


def net_error_coefficient(s, k, d, centers=None):
    n = len(s)
    r = n-d
    coefficient = F(ceil_sqrt(2*r*n*d))*row_bound(s)*row_bound(k)
    if centers is not None:
        sigma, kappa = centers
        ds = add(s, times(eye(n), sigma), F(-1))
        dk = add(k, times(eye(n), kappa), F(-1))
        linear = add(times(ds, kappa), times(dk, sigma))
        lip = sqrt_upper(frob2(linear))
        lip += 2*sqrt_upper(F(r))*row_bound(ds)*row_bound(dk)
        coefficient = min(coefficient, lip*sqrt_upper(F(n*d, 2)))
    return coefficient


def global_grid_certificate(s, k, d, epsilon, centers=None):
    n = len(s)
    assert is_spd(s) and is_spd(k) and 0 < d < n and epsilon > 0
    coefficient = net_error_coefficient(s, k, d, centers)
    q = max(n*d, ceil(coefficient/epsilon))
    best = None
    winner = None
    accepted = 0
    total = (2*q+1)**(n*d)
    # Scaling by 1/q leaves this projector unchanged. The corresponding
    # integer-grid matrix represents the rounded rational frame V.
    for entries in product(range(-q, q+1), repeat=n*d):
        v = [[F(x) for x in entries[i*d:(i+1)*d]] for i in range(n)]
        p = projector(v)
        if p is None:
            continue
        accepted += 1
        value = cost(s, k, p)
        if best is None or value < best:
            best = value
            winner = p
    assert winner == transpose(winner)
    assert mul(winner, winner) == winner and trace(winner) == d
    error = coefficient/q
    assert error <= epsilon
    return {'q': q, 'grid_matrices': total, 'full_rank_matrices': accepted,
            'lower': max(F(0), best-error), 'upper': best,
            'error': error, 'projector': winner, 'coefficient': coefficient}


def decimal(x, upper=False, places=21):
    scale = 10**places
    a = x.numerator*scale
    z = -((-a)//x.denominator) if upper else a//x.denominator
    sign = '-' if z < 0 else ''
    z = abs(z)
    return sign+str(z//scale)+'.'+str(z % scale).zfill(places)


def interval_text(lo, hi):
    return [decimal(lo), decimal(hi, True)]


def rational_matrix(a):
    return [[str(x) for x in row] for row in a]


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def peval(p, x):
    result = F(0)
    for a in reversed(p):
        result = result*x+a
    return result


def sturm(p):
    seq = [p, [i*p[i] for i in range(1, len(p))]]
    while True:
        rem = list(seq[-2])
        divisor = seq[-1]
        while rem != [F(0)] and len(rem) >= len(divisor):
            j = len(rem)-len(divisor)
            c = rem[-1]/divisor[-1]
            for i, a in enumerate(divisor):
                rem[j+i] -= c*a
            rem = trim(rem)
        if rem == [F(0)]:
            return seq
        seq.append([-x for x in rem])


def variations(seq, x):
    vals = [peval(p, x) for p in seq]
    signs = [1 if v > 0 else -1 for v in vals if v]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def root_count(seq, a, b):
    return variations(seq, a)-variations(seq, b)


def refine(seq, a, b):
    assert root_count(seq, a, b) == 1
    while b-a > F(1, 10**36):
        mid = (a+b)/2
        assert peval(seq[0], mid)
        if root_count(seq, a, mid):
            b = mid
        else:
            a = mid
    return a, b


def imul(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def ipoly(p, x):
    value = (F(0), F(0))
    for a in reversed(p):
        lo, hi = imul(value, x)
        value = lo+a, hi+a
    return value


def strict_cost_interval(t):
    numerator = ipoly([F(153, 2), F(-135), F(85), F(-15), F(17, 2)], t)
    denominator = ipoly([F(1), F(0), F(2), F(0), F(1)], t)
    assert denominator[0] > 0
    return imul(numerator, (1/denominator[1], 1/denominator[0]))


def main():
    out = {}
    s = [[F(11, 10), F(0)], [F(0), F(9, 10)]]
    k = [[F(1), F(1, 10)], [F(1, 10), F(1)]]
    assert mul(s, k) != mul(k, s)
    cert = global_grid_certificate(s, k, 1, F(1, 250), (F(1), F(1)))
    out['exhaustive_noncommuting_demo'] = {
        'S': rational_matrix(s), 'K': rational_matrix(k), 'd': 1,
        'requested_tolerance': '1/250',
        'q': cert['q'], 'grid_matrices': cert['grid_matrices'],
        'full_rank_matrices': cert['full_rank_matrices'],
        'exact_bounds': [str(cert['lower']), str(cert['upper'])],
        'outward_decimal_bounds': interval_text(cert['lower'], cert['upper']),
        'certified_width': str(cert['error']),
        'rational_feasible_projector': rational_matrix(cert['projector']),
    }

    rng = Random(141026)
    tested = 0
    for n in range(2, 7):
        for d in range(1, n):
            for repeat in range(2):
                ident = eye(n)
                w = [F(rng.randint(-3, 3)) for _ in range(n)]
                if not any(w):
                    w[0] = F(1)
                ww = sum(x*x for x in w)
                h = add(ident, [[2*x*y/ww for y in w] for x in w], F(-1))
                assert mul(transpose(h), h) == ident
                u = [row[:d] for row in h]
                q = n*d+repeat+1
                v = [[F((2*(q*x).numerator+(q*x).denominator)//
                         (2*(q*x).denominator), q) for x in row] for row in u]
                p = projector(v)
                assert p is not None
                original = mul(u, transpose(u))
                dist2 = frob2(add(p, original, F(-1)))
                residual2 = frob2(mul(add(ident, p, F(-1)), u))
                assert dist2 == 2*residual2 <= F(n*d, 2*q*q)
                a = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
                b = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
                s = add(mul(a, transpose(a)), ident)
                k = add(mul(b, transpose(b)), ident)
                assert is_spd(s) and is_spd(k)
                difference = abs(cost(s, k, p)-cost(s, k, original))
                assert difference*difference <= (
                    4*(n-d)*(row_bound(s)*row_bound(k))**2*dist2)
                sigma, kappa = s[0][0], k[0][0]
                ds = add(s, times(ident, sigma), F(-1))
                dk = add(k, times(ident, kappa), F(-1))
                linear = add(times(ds, kappa), times(dk, sigma))
                lip = sqrt_upper(frob2(linear))
                lip += 2*sqrt_upper(F(n-d))*row_bound(ds)*row_bound(dk)
                assert difference*difference <= lip*lip*dist2
                ps = times(ident, F(1, 100))
                pk = times(ident, F(1, 200))
                eta = (n-d)*(row_bound(pk)*row_bound(s)+
                      (row_bound(k)+row_bound(pk))*row_bound(ps))
                assert abs(cost(add(s, ps), add(k, pk), p)-cost(s, k, p)) <= eta
                tested += 1
    out['rational_coverage_and_bound_checks'] = {
        'cases': tested, 'dimensions': [2, 3, 4, 5, 6],
        'ranks': 'Every 1 <= d < n in each dimension; two cases each',
        'checks': ['Exact projector covering identity and radius',
                   'Original and centered objective Lipschitz bounds',
                   'Fixed-projector matrix uncertainty bound'],
        'arithmetic': 'fractions.Fraction throughout',
    }

    p = [F(-135), F(-136), F(360), F(-136), F(15)]
    seq = sturm(p)
    assert root_count(seq, F(-25), F(25)) == 2
    assert all(abs(x/p[-1]) <= 24 for x in p[:-1])
    positive = refine(seq, F('1.13317744357142'), F('1.13317744357143'))
    negative = refine(seq, F('-.42738776834928'), F('-.42738776834927'))
    j = strict_cost_interval(positive)
    other = strict_cost_interval(negative)
    assert j[1] < F(17, 2) < other[0]
    z = isqrt(6649*10**90)
    square_root = (F(z, 10**45), F(z+1, 10**45))
    assert square_root[0]**2 < 6649 < square_root[1]**2
    # Two identical independent 2D blocks: n=4, retained and discarded ranks 2.
    # The accompanying compression-diagonalization proof gives J*=2*j.
    free = (F(85)-square_root[1], F(85)-square_root[0])
    higher = (2*j[0], 2*j[1])
    penalty = (higher[0]-free[1], higher[1]-free[0])
    out['higher_rank_structured_global_certificate'] = {
        'n': 4, 'retained_rank': 2, 'discarded_rank': 2,
        'S': 'diag(9,1,9,1)',
        'K': 'diag(K0,K0), K0=[[17/2,-15/2],[-15/2,17/2]]',
        'projector_global_value': interval_text(*higher),
        'unrestricted_global_value': interval_text(*free),
        'positive_projector_penalty': interval_text(*penalty),
        'optimizer': 'I-diag(u*u^T,u*u^T), u=(1,t)/sqrt(1+t^2)',
        't': interval_text(*positive),
        'certificate': 'All stationary directions plus tensor-block lower bound',
        'scope': 'Structured higher-rank example; the net theorem handles arbitrary finite rational inputs',
    }
    out['scope'] = {
        'general_result': 'Written proof of finite epsilon-optimal global certificates for arbitrary rational SPD inputs',
        'implemented': 'Exhaustive rational net; optional centered Lipschitz bound',
        'not_claimed': 'Polynomial efficiency, independent review, formal verification, or physical-model validation',
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
```

Actual successful output:

```json
{
  "exhaustive_noncommuting_demo": {
    "S": [
      [
        "11/10",
        "0"
      ],
      [
        "0",
        "9/10"
      ]
    ],
    "K": [
      [
        "1",
        "1/10"
      ],
      [
        "1/10",
        "1"
      ]
    ],
    "d": 1,
    "requested_tolerance": "1/250",
    "q": 55,
    "grid_matrices": 12321,
    "full_rank_matrices": 12320,
    "exact_bounds": [
      "20849618/24255625",
      "41893281/48511250"
    ],
    "outward_decimal_bounds": [
      "0.859578675049601896467",
      "0.863578675049601896468"
    ],
    "certified_width": "1/250",
    "rational_feasible_projector": [
      [
        "1681/1970",
        "697/1970"
      ],
      [
        "697/1970",
        "289/1970"
      ]
    ]
  },
  "rational_coverage_and_bound_checks": {
    "cases": 30,
    "dimensions": [
      2,
      3,
      4,
      5,
      6
    ],
    "ranks": "Every 1 <= d < n in each dimension; two cases each",
    "checks": [
      "Exact projector covering identity and radius",
      "Original and centered objective Lipschitz bounds",
      "Fixed-projector matrix uncertainty bound"
    ],
    "arithmetic": "fractions.Fraction throughout"
  },
  "higher_rank_structured_global_certificate": {
    "n": 4,
    "retained_rank": 2,
    "discarded_rank": 2,
    "S": "diag(9,1,9,1)",
    "K": "diag(K0,K0), K0=[[17/2,-15/2],[-15/2,17/2]]",
    "projector_global_value": [
      "9.529409487501372948007",
      "9.529409487501372948008"
    ],
    "unrestricted_global_value": [
      "3.458599472415241082110",
      "3.458599472415241082111"
    ],
    "positive_projector_penalty": [
      "6.070810015086131865896",
      "6.070810015086131865897"
    ],
    "optimizer": "I-diag(u*u^T,u*u^T), u=(1,t)/sqrt(1+t^2)",
    "t": [
      "1.133177443571420609339",
      "1.133177443571420609340"
    ],
    "certificate": "All stationary directions plus tensor-block lower bound",
    "scope": "Structured higher-rank example; the net theorem handles arbitrary finite rational inputs"
  },
  "scope": {
    "general_result": "Written proof of finite epsilon-optimal global certificates for arbitrary rational SPD inputs",
    "implemented": "Exhaustive rational net; optional centered Lipschitz bound",
    "not_claimed": "Polynomial efficiency, independent review, formal verification, or physical-model validation"
  }
}
```


---

# BM nonlinear repair addendum — exact reduction, conditioning, and model uncertainty

Date: 15 October 2026. This is an extension of the Research Edition, addressing review references 12, 19, and 21. It preserves the frozen Foundation and existing canonical identifiers.

The construction corrects a present-time code by following the full system forward and pulling the retained state backward with a chosen reduced model. When the omitted influence fades faster than this backward operation amplifies error, the corrected code converges. It then evolves exactly under the reduced model. The proof quantifies approximation, regularity, sensitivity, uncertainty, and finite evaluation. It extends the earlier quadratic example to a class of nonlinear systems, including feedback in both directions in its continuous version.

This is a sufficient theorem in a specified native class. It does not determine the globally optimal encoder or repair cost for arbitrary nonlinear dynamics. The construction is an asymptotic-phase construction; no historical novelty or independent verification is asserted.

## 1. Declared system and uniform hypotheses

Use Euclidean norms throughout. Let x be in R^d and y in the closed ball of radius rho>0 in R^m. Consider

\[
\dot x=f(x)+b(x,y),\qquad \dot y=g(x,y).
\tag{N1}
\]

Assume the vector fields are C1 on an open neighborhood of this domain. For every relevant x and y, assume

\[
g(x,0)=0,\qquad
\langle y,g(x,y)\rangle\le-\beta\|y\|^2,
\qquad \|b(x,y)\|\le B_0\|y\|^q,
\tag{N2}
\]

where beta>0, B0>=0, and q>=1 is an integer. In particular b(x,0)=0. Suppose f is defined on all of R^d and

\[
-aI\preceq\operatorname{sym}Df(x)\preceq\ell I,
\qquad a\ge0,\quad\ell\ge-a.
\tag{N3}
\]

Let Psi_t be the reference flow generated by x_dot=f(x), and Phi_t the native flow (N1). The reference exists for all positive and negative times: (N3), applied to f and -f, bounds radial growth by a linear Gronwall estimate with the finite constant ||f(0)||. Its variational equation gives

\[
\operatorname{Lip}\Psi_t\le e^{\ell t},\qquad
\operatorname{Lip}\Psi_{-t}\le e^{at},\qquad t\ge0.
\tag{N4}
\]

The native flow exists for every t>=0 on the stated domain. Indeed (N2) gives ||y_t||<=e^(-beta t)||y_0|| and preserves the ball. The x equation has the same radial growth bound as f with the additional uniformly bounded forcing B0 rho^q. Neither component can escape to infinity in finite time, and the fields extend to a neighborhood of the closed y-ball. Local existence therefore continues forward.

The decisive value gap is

\[
\delta=q\beta-a>0.
\tag{N5}
\]

These are uniform native hypotheses, not quantities inferred from a successful sample fit. In particular, a perturbation that fails to vanish to the stated order at y=0 may violate this contract even when its unweighted amplitude is small.

## 2. Exact continuous repair for the coupled system

Write x_t=pi_x Phi_t(x,y). Define the finite and limiting encoders

\[
R_T(x,y)=\Psi_{-T}(x_T),\qquad
R(x,y)=\lim_{T\to\infty}R_T(x,y).
\tag{N6}
\]

**Theorem.** Under (N1)–(N5), this limit exists uniformly on the whole stated domain, is continuous, and satisfies

\[
R(x,0)=x,\qquad
\boxed{R\Phi_t=\Psi_t R\quad(t\ge0)}.
\tag{N7}
\]

Its correction and truncation obey

\[
\boxed{\quad
\|R(x,y)-x\|\le\frac{B_0}{\delta}\|y\|^q,\qquad
\|R-R_T\|(x,y)\le\frac{B_0}{\delta}\|y\|^q e^{-\delta T}.
\quad}
\tag{N8}
\]

This includes x-dependent forcing and x-dependent driver dynamics; no independence between the retained and omitted components is assumed in this continuous theorem.

### Complete proof

The reference flow transports its vector field: D Psi_-t(z) f(z)=f(Psi_-t(z)). Thus differentiating Psi_-t(x_t) cancels the reference part of the native derivative and gives

\[
\frac{d}{dt}R_t(x,y)
=D\Psi_{-t}(x_t)b(x_t,y_t).
\]

Its norm is at most B0 ||y||^q exp[-(q beta-a)t]. Integrating from T to S proves the uniform Cauchy estimate; integrating from zero or from T to infinity proves (N8). Each R_T is continuous, so the uniform limit is continuous. At y=0 native evolution is reference evolution, giving R_T(x,0)=x and hence the normalization.

For s>=0, the native semigroup and reference group identities give

\[
R_T(\Phi_s z)=\Psi_{-T}(x_{T+s})
=\Psi_s R_{T+s}(z).
\]

Take T to infinity and use continuity of Psi_s to obtain (N7). This proves one common exact update for every time, hence for every chosen sampling step, rather than separate independently fitted updates.

The repair is unique within its uniform normalization class. If another map U satisfies the same semiconjugacy and ||U(x,y)-x||<=C||y||^q with a finite uniform C, pull both codes backward along the reference flow:

\[
\|U(z)-R(z)\|
\le e^{at}\|U(\Phi_tz)-R(\Phi_tz)\|
\le(C+B_0/\delta)\|y\|^q e^{-\delta t}\longrightarrow0.
\]

Uniqueness in this class is not a claim of optimality across other reduced dynamics, code dimensions, or receiver tasks.

### Forecast and code-noise bounds

For the retained-state task x_t, use decoder D_t(z)=Psi_t(z). Apply (N8) at the actual current state and use (N7):

\[
\boxed{\quad
\|x_t-\Psi_tR(x_0,y_0)\|
\le\frac{B_0}{\delta}\|y_0\|^q e^{-q\beta t}.
\quad}
\tag{N9}
\]

The error decays at the omitted forcing rate. This sharper statement follows by applying the value bound after evolution; propagating only the initial correction with a forward Lipschitz constant would lose it.

If the observed code has error at most nu, the pointwise forecast error is at most

\[
\frac{B_0}{\delta}\|y_0\|^q e^{-q\beta t}+\nu e^{\ell t}.
\tag{N10}
\]

For 1<=p<=infinity, its Lp trajectory error is bounded by the Lp norm of this scalar envelope. When ell<=0 it supplies a uniform infinite-time upper bound B0 rho^q/delta+nu. No minimax equality is claimed for these general nonlinear systems.

## 3. A quantitative C1 repair theorem

Additional assumptions now restrict (N1) to the triangular class

\[
\dot x=f(x)+b(y),\qquad \dot y=g(y).
\tag{N11}
\]

Let f be C2 with ||D2 f||<=M uniformly, and let g be C1 with sym Dg(y)<=-beta I throughout the y-ball. Suppose

\[
\|Db(y)\|\le B_1\|y\|^{q-1},\qquad
\omega=q\beta-2a-\ell>0.
\tag{N12}
\]

The derivative norms are operator norms; D2 f uses the induced bilinear norm. Define

\[
c=\frac{B_1\rho^{q-1}}{q\beta+\ell},\qquad
\eta_x=\frac{MB_0\rho^q}{\omega(\omega+a)},\qquad
\eta_y=c\eta_x+\frac{B_1\rho^{q-1}}{\delta}.
\tag{N13}
\]

The denominators are positive: ell>=-a and omega>0 imply q beta+ell>0 and delta>0.

**Theorem.** The same limiting R is C1 on R^d times the open y-ball, with uniform bounds

\[
\boxed{\|D_xR-I\|\le\eta_x,\qquad \|D_yR\|\le\eta_y.}
\tag{N14}
\]

If eta_x<1, each map x -> R(x,y) is a global C1 diffeomorphism of R^d. Its inverse has Lipschitz constant at most 1/(1-eta_x). Consequently (x,y)->(R(x,y),y) is a C1 coordinate change on the product domain, R is a submersion, and

\[
\operatorname{Lip}R\le\sqrt{(1+\eta_x)^2+\eta_y^2}.
\tag{N15}
\]

This conditions the repair itself as well as its decoder. The C1 assertion is for the triangular subclass; it is not automatically transferred to the fully coupled continuous theorem.

### Complete derivative and invertibility proof

Driver contraction gives ||D_y phi_t||<=e^(-beta t). Variations of the x equation, using the upper one-sided bound ell, give

\[
\|D_{x_0}x_t\|\le e^{\ell t},\qquad
\|D_{y_0}x_t\|\le c e^{\ell t}.
\tag{N16}
\]

For the latter, integrate the forcing derivative B1 rho^(q-1)e^(-q beta t) against the evolution bound e^(ell(t-s)). The resulting factor is at most B1 rho^(q-1)/(q beta+ell).

The second variation of the backward reference flow satisfies

\[
\|D^2\Psi_{-t}\|
\le M e^{at}\frac{e^{at}-1}{a}\quad(a>0),
\]

with continuous limit Mt when a=0. This follows by integrating the quadratic forcing D2(-f)[D Psi_-s,D Psi_-s] in the second-variation equation, using (N4).

Differentiate the convergent integral for R-x. In the x direction, only the evaluation point of D Psi_-t(x_t) varies. The derivative integrand is bounded, for a>0, by

\[
\frac{MB_0\rho^q}{a}
\{e^{-\omega t}-e^{-(\omega+a)t}\}.
\]

Its integral equals MB0 rho^q/[omega(omega+a)]. For a=0, integrate MB0 rho^q t e^(-omega t) to obtain the same formula. In the y direction, evaluation-point variation costs at most c times this integral. The additional derivative of b(phi_t(y)) has integral at most B1 rho^(q-1)/delta. These bounds prove uniform convergence of the derivative integrals; together with uniform convergence of R_T they justify C1 differentiation and (N14).

For fixed y write R(x,y)=x+h_y(x). The bound on D_xR-I makes h_y globally eta_x-Lipschitz. For any target z, x=z-h_y(x) is a contraction on the complete space R^d when eta_x<1. It has a unique solution. The derivative I+D h_y is invertible with inverse norm at most 1/(1-eta_x); the inverse function theorem gives C1 dependence on z and y. This proves the global triangular coordinate change. The operator bound on the two derivative blocks gives (N15).

**Affine reference improvement.** If f is affine, M=0 and the second-variation term vanishes. The stronger omega condition is then unnecessary: delta>0 alone gives C1 repair, D_xR=I, and ||D_yR||<=B1 rho^(q-1)/delta. The earlier quadratic repair is recovered on its convergent side. Failure of delta>0 does not prove repair impossible; a different construction may still work.

## 4. Model uncertainty, including new feedback

Let R1 be the C1 repair for a triangular baseline (N11), with eta_x and eta_y as above. Define

\[
G_y=\frac{B_1}{\delta}
+\frac{B_1\eta_x}{q\beta+\ell}.
\]

Repeating the derivative proof with ||y|| in place of rho gives the pointwise estimate ||D_yR1(x,y)||<=G_y||y||^(q-1); in particular eta_y=G_y rho^(q-1). For the affine improvement use eta_x=0 in this formula, without any omega denominator.

Now change the native system to

\[
\dot x=f(x)+b(y)+\Delta b(x,y),\qquad
\dot y=g(y)+\Delta g(x,y),
\]

where the perturbations are C1 and uniformly satisfy

\[
\|\Delta b(x,y)\|\le\epsilon_b\|y\|^q,\qquad
\|\Delta g(x,y)\|\le\epsilon_g\|y\|,
\quad\beta'=\beta-\epsilon_g>0,
\quad\delta'=q\beta'-a>0.
\tag{N17}
\]

This permits feedback in both directions. The continuous theorem constructs R2 for the changed system. Its change from the baseline code obeys

\[
\boxed{\quad
\|R_2(x,y)-R_1(x,y)\|
\le\frac{(1+\eta_x)\epsilon_b+G_y\epsilon_g}{\delta'}\|y\|^q.
\quad}
\tag{N18}
\]

To prove this, let z_t follow the changed system and put w_t=R1(z_t). Differentiating baseline semiconjugacy at zero time gives D R1 v1=f(R1). Therefore

\[
\dot w_t=f(w_t)+D_xR_1\Delta b+D_yR_1\Delta g.
\]

The added forcing has norm at most [(1+eta_x)epsilon_b+G_y epsilon_g]||y||^q e^(-q beta' t). Pull w_t backward by Psi_-t and integrate, as in section 2, to obtain (N18). This pullback limit is R2: the difference w_t-x_t is at most B0||y_t||^q/delta, whose backward magnification tends to zero since delta'>0.

The estimate is sharp in an affine subclass. Take scalar f(x)=-a x, g(y)=-beta y, b(y)=kappa y^q with kappa>0. Increase forcing by epsilon_b y^q and reduce decay by epsilon_g y. Then

\[
R_1=x+\frac{\kappa y^q}{q\beta-a},\qquad
R_2=x+\frac{(\kappa+\epsilon_b)y^q}{q(\beta-\epsilon_g)-a}.
\]

Here eta_x=0, G_y=q kappa/(q beta-a), and the absolute coefficient difference equals the right-hand coefficient in (N18). Thus the uncertainty constant is not merely a qualitative continuity assertion. No C1 or inverse bound for the newly coupled R2 is asserted without additional derivative hypotheses.

## 5. Finite evaluation, closure residual, and precision window

The exact code is a limit; a finite evaluated code has a quantified residual. From the identity used in section 2,

\[
\boxed{\quad
\|R_T\Phi_h(z)-\Psi_hR_T(z)\|
\le e^{\ell h}\frac{B_0}{\delta}\|y\|^q
e^{-\delta T}(1-e^{-\delta h}).
\quad}
\tag{N19}
\]

Indeed R_T Phi_h=Psi_h R_(T+h); integrate the encoder derivative only from T to T+h and apply the forward Lipschitz bound. Equality is attained in the scalar affine power-forcing model with positive coupling, so this finite-window residual bound is sharp in that subclass.

If an evaluated code differs from R_T by at most epsilon_eval at both required native inputs, its sampled closure residual has the additional budget (1+e^(ell h))epsilon_eval. Error in the reduced update itself needs its own budget.

Suppose the endpoint x_T is computed within epsilon_x and the backward-flow evaluation at that computed endpoint has error at most epsilon_back. Then

\[
\|\widehat R_T-R\|
\le C e^{-\delta T}+e^{aT}\epsilon_x+\epsilon_{\rm back},
\qquad C=B_0\|y\|^q/\delta.
\tag{N20}
\]

This separates analytic truncation from numerical flow error. Taking T ever larger reduces one and can amplify the other. Under a declared fixed epsilon_x>0 and a>0, the minimizing nonnegative window for this envelope is

\[
T_* =\max\left\{0,\frac1{q\beta}
\log\frac{B_0\|y\|^q}{a\epsilon_x}\right\}.
\tag{N21}
\]

For y=0 or B0=0 choose T*=0. When a=0 the envelope decreases toward epsilon_x+epsilon_back as T tends to infinity. If the flow error budget depends on T, that dependence must instead be included before optimizing. The formula is an optimization of the stated evaluation envelope, not an optimal physical sensor or repair-cost theorem.

An executable numerical certificate requires certified epsilon_x and epsilon_back. The floating-point ODE checks below do not supply rigorous interval enclosures for them.

## 6. A non-polynomial example with exact rational constants

Take d=m=1, rho=1, and

\[
f(x)=-x+\tfrac14\sin x,\qquad
g(y)=-2y-y^3,\qquad
b(y)=\tfrac15(1-\cos y).
\]

The global inequalities |sin y|<=|y| and 1-cos y<=y^2/2 give q=2, B0=1/10, B1=1/5. Also

\[
a=5/4,\quad\ell=-3/4,\quad M=1/4,\quad\beta=2,
\quad\delta=11/4,\quad\omega=9/4.
\]

The theorem gives

\[
\|R-x\|\le\frac2{55}y^2,\qquad
|D_xR-1|\le\frac1{315},\qquad
|D_yR|\le\frac{16424}{225225},
\]

\[
\operatorname{Lip}(x\text{-inverse at fixed }y)\le315/314,
\qquad\operatorname{Lip}R\le1.005822
\]

where the last decimal is a conservatively rounded display of the exact square-root expression (N15). Its upper-bound direction is certified by the rational inequality (1005822/10^6)^2 >= (316/315)^2+(16424/225225)^2. Forecast error for the exact code is at most (2/55)y_0^2 e^(-4t), and code noise nu adds at most nu e^(-3t/4). These estimates hold over the full stated domain; they are derived from analytic inequalities, not fitted to the tests.

A genuinely coupled continuous example replaces forcing by sin(x)(1-cos y)/5 and driver dynamics by -(2+sin^2(x)/2)y-y^3. The same q, beta, B0 and value/forecast bounds apply. The triangular C1 derivative constants are not assigned to this changed system.

For a smaller certified feedback perturbation, add sin(x)y^2/100 to the original x equation and cos(x)y/10 to its y equation. This has epsilon_b=1/100, epsilon_g=1/10 and remaining value gap delta'=51/20; (N18) gives its explicit code-change bound.

With assumed endpoint error 10^-10 and backward evaluation error 10^-12, the envelope for the original example at |y|=1 has T* approximately 5.12503 and minimum approximately 8.80943 times 10^-8. Those are numerical displays conditional on those error budgets, not certified error guarantees for the test solver.

## 7. Resonance: an obstruction for every forcing order

For integer q>=1, beta>0 and kappa nonzero, consider the scalar retained coordinate in

\[
\dot x=-q\beta x+\kappa y^q,\qquad \dot y=-\beta y.
\tag{N22}
\]

**Obstruction.** There is no local C^q scalar encoder R with R_x(0,0) nonzero that closes under even one fixed step h>0 with any single-valued update F. No regularity of F is assumed.

**Proof.** Write r(x)=R(x,0). Its derivative at zero is nonzero, so its local inverse exists and is C^q. Normalize U=r^-1 R, so U(x,0)=x. On the axis, closure forces the normalized update to be multiplication by exp(-q beta h), and hence locally

\[
U(\Phi_h(x,y))=e^{-q\beta h}U(x,y).
\]

Put lambda=exp(-beta h), so 0<lambda<1. The native step is

\[
\Phi_h(x,y)=(\lambda^q(x+\kappa h y^q),\lambda y).
\]

For q>=2, Taylor expansion at (0,0), U_x(0,0)=1, and x=0 give

\[
\kappa h\lambda^q y^q
+\sum_{j=1}^q c_j\lambda^j y^j+o(|y|^q)
=\lambda^q\sum_{j=1}^q c_j y^j+o(|y|^q).
\]

Mixed terms involving x have degree at least q+1 after substitution; pure x^2 terms have degree at least 2q. For every j<q, lambda^j differs from lambda^q, forcing c_j=0. At degree q the c_q terms cancel and force kappa h lambda^q=0, a contradiction. For q=1, the first-order Taylor expansion directly gives the same contradiction, including its x-derivative term. This proves the obstruction for all q.

The lower-regularity repair

\[
U=x+\frac\kappa\beta y^q\log|y|,
\]

extended by U=x at y=0, still closes exactly. It is C^(q-1) but not C^q at zero: the q-th derivative of y^q log|y| contains q! log|y| and diverges, while all derivatives of lower order extend continuously. For q=1 it is continuous and not locally Lipschitz. This strengthens the earlier example from a nonsmooth chosen formula to a nonexistence result for every C^q scalar encoder preserving the x direction. It does not rule out retaining y alone or using a larger code, and it assumes beta>0.

## 8. Current closure and verification scope

The conditioned nonlinear repair question now has a general continuous theorem for the declared coupled class, a quantitative C1 theorem for the triangular subclass, a sharp model-uncertainty estimate, a sharp finite-window closure estimate, and an all-orders resonant regularity obstruction. The nonlinear reference dynamics need not be linear or polynomial. Arbitrary nonlinear systems outside these hypotheses, globally optimal encoder choice and repair cost, and the nonlinear Jordan interior trajectory optimum remain unresolved.

The reproducible checks comprise 72 exact rational affine encoder identities, 72 exact equalities in the uncertainty bound, 216 exact dyadic resonant identities across orders 1–12, 128 non-polynomial ODE initial-state tests, and 32 additional feedback-perturbation tests. The ODE computations use floating-point DOP853 and are consistency checks with an explicitly stated numerical allowance; their small residuals are not formal or interval-certified proof. The written arguments establish the general results under the hypotheses. None of this supplies missing physical constitutive laws, calibrated native parameters, continuum estimates, or independent review.

## Reproducible 15 October verification record

The following standalone Python 3 script requires NumPy and SciPy. SHA-256 of the UTF-8 script: `ab6628d0c1a0e52b1120adc2ccc8d3e3efe9c0053328a4647874a68d11f6cc05`. SHA-256 of its captured UTF-8 JSON output: `28f9f86f00cf2e0c66181dfb97c45173e5cdb087203bcd8658e776bc2e71272b`. Exact and floating-point parts are labelled in the output.

```python
#!/usr/bin/env python3
"""Exact rational identities and numerical checks of the nonlinear phase repair.

The accompanying written theorem carries the general guarantees. ODE solver
outputs are consistency checks, not interval-certified flow computations.
"""
from fractions import Fraction as F
from math import sin, cos, exp, log, sqrt
from random import Random
import json
import numpy as np
from scipy.integrate import solve_ivp


def integrate(rhs, initial, time, times=None):
    if time == 0:
        return np.asarray(initial, dtype=float)
    answer = solve_ivp(rhs, (0, time), initial, method='DOP853',
                       rtol=3e-13, atol=2e-14, t_eval=times)
    assert answer.success, answer.message
    return answer.y if times is not None else answer.y[:, -1]


def reference(x, t, derivative=False):
    direction = 1 if t >= 0 else -1
    def rhs(s, z):
        values = [direction*(-z[0]+sin(z[0])/4)]
        if derivative:
            values.append(direction*(-1+cos(z[0])/4)*z[1])
        return values
    return integrate(rhs, [x, 1] if derivative else [x], abs(t))


def native(x, y, t, coupled=False, derivative=False, times=None):
    assert not (coupled and derivative)
    def rhs(s, z):
        u, v = z[:2]
        force = (1-cos(v))/5
        decay = 2
        if coupled == 'perturbed':
            force += sin(u)*v*v/100
            decay -= cos(u)/10
        elif coupled:
            force *= sin(u)
            decay += sin(u)**2/2
        values = [-u+sin(u)/4+force, -decay*v-v**3]
        if derivative:
            a, b, c = z[2:]
            values += [(-1+cos(u)/4)*a,
                       (-1+cos(u)/4)*b+sin(v)*c/5,
                       (-2-3*v*v)*c]
        return values
    return integrate(rhs, [x, y, 1, 0, 1] if derivative else [x, y], t, times)


def phase(x, y, horizon, coupled=False, derivative=False):
    end = native(x, y, horizon, coupled, derivative)
    back = reference(end[0], -horizon, derivative)
    if derivative:
        return back[0], back[1]*end[2], back[1]*end[3]
    return back[0]


def main():
    a, ell, beta, q = F(5, 4), F(-3, 4), F(2), 2
    curvature, b0, b1, radius = F(1, 4), F(1, 10), F(1, 5), F(1)
    gap = q*beta-a
    bunch = q*beta-2*a-ell
    eta_x = curvature*b0*radius**q/(bunch*(bunch+a))
    c = b1*radius**(q-1)/(q*beta+ell)
    eta_y = c*eta_x+b1*radius**(q-1)/gap
    assert gap == F(11, 4) and bunch == F(9, 4)
    assert eta_x == F(1, 315) < 1
    assert c == F(4, 65)
    assert b0/gap == F(2, 55)
    constants = {
        'inverse_growth_a': str(a), 'forward_growth_ell': str(ell),
        'driver_decay_beta': str(beta), 'forcing_order_q': q,
        'curvature_M': str(curvature), 'B0': str(b0), 'B1': str(b1),
        'value_gap': str(gap), 'C1_gap': str(bunch),
        'repair_value_coefficient': str(b0/gap),
        'Dx_repair_bound': str(eta_x), 'Dy_repair_bound': str(eta_y),
        'fixed_y_inverse_Lipschitz_bound': str(1/(1-eta_x)),
        'encoder_Lipschitz_bound_display': sqrt(float((1+eta_x)**2+eta_y**2)),
        'status': 'Exact rational constants; final Lipschitz decimal is a display only',
    }
    out = {'nonpolynomial_example_constants': constants}

    # Check the affine specialization directly in the differential identity,
    # with exact rational arithmetic and many orders/parameters.
    affine = 0
    rng = Random(151026)
    for order in range(1, 9):
        for j in range(9):
            decay = F(j+2, 3)
            slow = F(order)*decay/F(2+j % 3)
            kappa = F((-1)**j*(j+1), 7)
            x, y = F(rng.randint(-9, 9), 5), F(rng.randint(-7, 7), 8)
            delta = order*decay-slow
            assert delta > 0
            r = x+kappa*y**order/delta
            lhs = -slow*x+kappa*y**order
            lhs += kappa*order*y**(order-1)/delta*(-decay*y)
            assert lhs == -slow*r
            affine += 1
    out['exact_affine_specializations'] = {
        'cases': affine, 'orders': list(range(1, 9)),
        'arithmetic': 'fractions.Fraction',
        'identity': 'DR.vector_field = -a*R',
    }

    # The uncertainty estimate is sharp for this affine subclass: increase
    # forcing and reduce driver decay, both in the adverse direction.
    perturbation_identities = 0
    for order in range(1, 9):
        for j in range(9):
            decay = F(j+2, 3)
            slow = order*decay/F(2+j % 3)
            kappa = F(j+1, 7)
            delta = order*decay-slow
            eps_g, eps_b = delta/(4*order), F(j+1, 100)
            new_delta = order*(decay-eps_g)-slow
            true_change = (kappa+eps_b)/new_delta-kappa/delta
            certified_change = (eps_b+order*kappa*eps_g/delta)/new_delta
            assert true_change == certified_change > 0
            perturbation_identities += 1
    out['sharp_rational_uncertainty_checks'] = {
        'cases': perturbation_identities,
        'result': 'Exact equality in the general encoder-perturbation bound',
        'arithmetic': 'fractions.Fraction',
    }

    # At sampled resonance: (x,y) -> (lambda^q*(x+y^q), lambda*y).
    # Lower jet coefficients are forced to zero; the q-th forcing term is
    # nonzero while its decoder coefficient cancels. Check the rational map
    # and its logarithmic repair exactly on dyadic y.
    resonant_cases = 0
    lam = F(1, 2)
    for order in range(1, 13):
        eigenvalue = lam**order
        assert all(lam**j != eigenvalue for j in range(1, order))
        assert eigenvalue != 0
        for j in range(9):
            for sign in (-1, 1):
                y = sign*lam**j
                x = F(j-order, 7)
                # b=log(2), kappa=h=1: log|y|/b=-j exactly.
                r = x-j*y**order
                new_x = eigenvalue*(x+y**order)
                new_y = lam*y
                new_r = new_x-(j+1)*new_y**order
                assert new_r == eigenvalue*r
                resonant_cases += 1
    out['resonance_exact_checks'] = {
        'orders_checked': list(range(1, 13)),
        'dyadic_logarithmic_repair_cases': resonant_cases,
        'arithmetic': 'fractions.Fraction; the dyadic logarithm cancels exactly',
        'general_obstruction': 'The written Taylor-jet proof applies to every integer q>=1',
    }

    # Non-polynomial examples. The second has feedback in both directions;
    # only the continuous theorem is asserted for that example.
    starts = [(x, y) for x in (-20, -3, -1, 0, 1, 3, 20)
              for y in (-1, -.6, -.2, 0, .2, .6, 1)]
    starts += [(rng.uniform(-12, 12), rng.uniform(-1, 1)) for _ in range(15)]
    horizon, h, nu = 5., .37, .001
    roundoff_allowance = 2e-9  # Not a certified solver error budget.
    times = np.array([0., .25, .5, 1., 2., 4.])
    numerical = []
    for coupled in (False, True):
        max_dx, max_dy = 0., 0.
        max_repair_ratio, max_forecast_excess, max_closure_excess = 0., 0., 0.
        for x, y in starts:
            if coupled:
                r = phase(x, y, horizon, coupled)
            else:
                r, dx, dy = phase(x, y, horizon, coupled, True)
                max_dx = max(max_dx, abs(dx-1))
                max_dy = max(max_dy, abs(dy))
                assert abs(dx-1) <= float(eta_x)+roundoff_allowance
                assert abs(dy) <= float(eta_y)+roundoff_allowance
            value_bound = float(b0/gap)*y*y
            if value_bound:
                max_repair_ratio = max(max_repair_ratio, abs(r-x)/value_bound)
            assert abs(r-x) <= value_bound+roundoff_allowance
            finite_tail = value_bound*exp(-float(gap)*horizon)
            native_h = native(x, y, h, coupled)
            encoded_next = phase(*native_h, horizon, coupled)
            reduced_next = reference(r, h)[0]
            defect_bound = exp(float(ell)*h)*finite_tail*(1-exp(-float(gap)*h))
            excess = abs(encoded_next-reduced_next)-defect_bound
            max_closure_excess = max(max_closure_excess, excess)
            assert excess <= roundoff_allowance
            actual = native(x, y, times[-1], coupled, times=times)[0]
            for noise in (-nu, 0., nu):
                predicted = integrate(lambda t, z: [-z[0]+sin(z[0])/4],
                                      [r+noise], times[-1], times=times)[0]
                bounds = value_bound*np.exp(-float(q*beta)*times)
                bounds += (abs(noise)+finite_tail)*np.exp(float(ell)*times)
                excess = float(np.max(np.abs(actual-predicted)-bounds))
                max_forecast_excess = max(max_forecast_excess, excess)
                assert excess <= roundoff_allowance
        numerical.append({
            'model': 'fully coupled continuous repair' if coupled else 'triangular C1 repair',
            'initial_states': len(starts), 'phase_horizon': horizon,
            'forecast_times': times.tolist(), 'code_noise_values': [-nu, 0., nu],
            'max_observed_value_bound_ratio': max_repair_ratio,
            'max_observed_DxR_minus_I': None if coupled else max_dx,
            'max_observed_DyR': None if coupled else max_dy,
            'max_forecast_bound_excess': max_forecast_excess,
            'max_finite_closure_bound_excess': max_closure_excess,
            'solver': 'SciPy DOP853, rtol=3e-13, atol=2e-14',
            'status': 'Numerical consistency only; solver errors are not rigorously enclosed',
        })
    out['nonpolynomial_ODE_checks'] = numerical

    eps_b, eps_g = F(1, 100), F(1, 10)
    perturbed_gap = q*(beta-eps_g)-a
    uncertainty_coefficient = ((1+eta_x)*eps_b+eta_y*eps_g)/perturbed_gap
    maximum_perturbation_excess = 0.
    for x, y in starts[::2]:
        base_r = phase(x, y, horizon)
        changed_r = phase(x, y, horizon, 'perturbed')
        base_tail = float(b0/gap)*y*y*exp(-float(gap)*horizon)
        changed_tail = float((b0+eps_b)/perturbed_gap)*y*y
        changed_tail *= exp(-float(perturbed_gap)*horizon)
        bound = float(uncertainty_coefficient)*y*y+base_tail+changed_tail
        excess = abs(base_r-changed_r)-bound
        maximum_perturbation_excess = max(maximum_perturbation_excess, excess)
        assert excess <= roundoff_allowance
    out['nonlinear_feedback_uncertainty'] = {
        'initial_states': len(starts[::2]), 'epsilon_b': str(eps_b),
        'epsilon_g': str(eps_g), 'remaining_value_gap': str(perturbed_gap),
        'exact_uncertainty_coefficient': str(uncertainty_coefficient),
        'max_observed_bound_excess': maximum_perturbation_excess,
        'status': 'Numerical consistency; the general bound has a written proof',
    }

    # Check the analytic evaluation-window optimizer independently against a
    # dense set of alternative horizons, under a fixed error-envelope model.
    flow_error, back_error = 1e-10, 1e-12
    c0 = float(b0/gap)
    optimum = max(0., log(float(b0)/(float(a)*flow_error))/float(q*beta))
    def envelope(t):
        return c0*exp(-float(gap)*t)+flow_error*exp(float(a)*t)+back_error
    best = envelope(optimum)
    assert all(envelope(t) >= best-1e-20 for t in np.linspace(0, 12, 2401))
    derivative = -float(gap)*c0*exp(-float(gap)*optimum)
    derivative += float(a)*flow_error*exp(float(a)*optimum)
    assert abs(derivative) < 1e-20
    out['finite_precision_window'] = {
        'assumed_forward_state_error': flow_error,
        'assumed_backflow_evaluation_error': back_error,
        'best_horizon_display': optimum, 'minimum_envelope_display': best,
        'comparison_horizons': 2401,
        'scope': 'Optimization of a declared error envelope; the ODE solver is not certified to meet these error assumptions',
    }
    out['scope'] = {
        'general_guarantees': 'Written proofs under stated decay, curvature, and regularity assumptions',
        'exact_computation': 'Rational constants, affine identities, and sampled resonant dyadic identities',
        'numerical_computation': 'Non-polynomial ODE examples and evaluation-window display',
        'not_claimed': 'Independent review, formal verification, optimal encoder cost, or physical-model validation',
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
```

Actual successful output:

```json
{
  "nonpolynomial_example_constants": {
    "inverse_growth_a": "5/4",
    "forward_growth_ell": "-3/4",
    "driver_decay_beta": "2",
    "forcing_order_q": 2,
    "curvature_M": "1/4",
    "B0": "1/10",
    "B1": "1/5",
    "value_gap": "11/4",
    "C1_gap": "9/4",
    "repair_value_coefficient": "2/55",
    "Dx_repair_bound": "1/315",
    "Dy_repair_bound": "16424/225225",
    "fixed_y_inverse_Lipschitz_bound": "315/314",
    "encoder_Lipschitz_bound_display": 1.005821552188504,
    "status": "Exact rational constants; final Lipschitz decimal is a display only"
  },
  "exact_affine_specializations": {
    "cases": 72,
    "orders": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8
    ],
    "arithmetic": "fractions.Fraction",
    "identity": "DR.vector_field = -a*R"
  },
  "sharp_rational_uncertainty_checks": {
    "cases": 72,
    "result": "Exact equality in the general encoder-perturbation bound",
    "arithmetic": "fractions.Fraction"
  },
  "resonance_exact_checks": {
    "orders_checked": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12
    ],
    "dyadic_logarithmic_repair_cases": 216,
    "arithmetic": "fractions.Fraction; the dyadic logarithm cancels exactly",
    "general_obstruction": "The written Taylor-jet proof applies to every integer q>=1"
  },
  "nonpolynomial_ODE_checks": [
    {
      "model": "triangular C1 repair",
      "initial_states": 64,
      "phase_horizon": 5.0,
      "forecast_times": [
        0.0,
        0.25,
        0.5,
        1.0,
        2.0,
        4.0
      ],
      "code_noise_values": [
        -0.001,
        0.0,
        0.001
      ],
      "max_observed_value_bound_ratio": 0.9506246789954264,
      "max_observed_DxR_minus_I": 0.0010478146770038776,
      "max_observed_DyR": 0.04093499956830908,
      "max_forecast_bound_excess": 1.956879103204301e-12,
      "max_finite_closure_bound_excess": 1.2860823517257813e-12,
      "solver": "SciPy DOP853, rtol=3e-13, atol=2e-14",
      "status": "Numerical consistency only; solver errors are not rigorously enclosed"
    },
    {
      "model": "fully coupled continuous repair",
      "initial_states": 64,
      "phase_horizon": 5.0,
      "forecast_times": [
        0.0,
        0.25,
        0.5,
        1.0,
        2.0,
        4.0
      ],
      "code_noise_values": [
        -0.001,
        0.0,
        0.001
      ],
      "max_observed_value_bound_ratio": 0.5883236795807982,
      "max_observed_DxR_minus_I": null,
      "max_observed_DyR": null,
      "max_forecast_bound_excess": 2.042588320705363e-12,
      "max_finite_closure_bound_excess": 8.757439218243235e-13,
      "solver": "SciPy DOP853, rtol=3e-13, atol=2e-14",
      "status": "Numerical consistency only; solver errors are not rigorously enclosed"
    }
  ],
  "nonlinear_feedback_uncertainty": {
    "initial_states": 32,
    "epsilon_b": "1/100",
    "epsilon_g": "1/10",
    "remaining_value_gap": "51/20",
    "exact_uncertainty_coefficient": "3716/546975",
    "max_observed_bound_excess": 0.0,
    "status": "Numerical consistency; the general bound has a written proof"
  },
  "finite_precision_window": {
    "assumed_forward_state_error": 1e-10,
    "assumed_backflow_evaluation_error": 1e-12,
    "best_horizon_display": 5.12503057140805,
    "minimum_envelope_display": 8.809430798129595e-08,
    "comparison_horizons": 2401,
    "scope": "Optimization of a declared error envelope; the ODE solver is not certified to meet these error assumptions"
  },
  "scope": {
    "general_guarantees": "Written proofs under stated decay, curvature, and regularity assumptions",
    "exact_computation": "Rational constants, affine identities, and sampled resonant dyadic identities",
    "numerical_computation": "Non-polynomial ODE examples and evaluation-window display",
    "not_claimed": "Independent review, formal verification, optimal encoder cost, or physical-model validation"
  }
}
```


# 18–19 October development of the remaining BM contracts

Started 18 October; integrated 19 October 2026 · Additive Research Edition development · Internal proofs and executable certificates

## 1. What this release completes

This document develops the eight open BM research families recorded in the Research Edition and the completeness register. It supplies full mathematical arguments, finite algorithms, exact certificates and explicit negative results. It does not change the frozen V1 foundation. “Theorem” below means a written proof with the stated hypotheses; it does not mean independent peer review or a historical originality claim.

The main advances are a universal greatest-interface criterion for finite correlated contexts, a compressed exact fragmentation frontier algorithm with an NP-completeness and fixed-parameter analysis, the exact three-state scalar-polynomial Jordan optimum, and the sharp universal normalized-defect upper bound for qubit recovery. Additional results address infinite-horizon prediction, conditioned nonlinear optimization, global smooth realization, effective infinite presentations, finite operational candidates and native locality examples.

| Existing obligation | Result developed here | Boundary that remains |
|---|---|---|
| Nonlinear Jordan trajectory optimum | Scalar polynomial sampled autonomy forces a first integral; exact optimum for n=3, d=1 in that class and for all continuous first integrals | Arbitrary continuous noninvariant encoders, and the other interior dimensions |
| Global smooth augmentation | Explicit finite-atlas construction; exact minima for a sphere with coordinate or constant legacy; finite-degree algebraic decision formulation | Least dimension for a general smooth source/task/legacy/target contract |
| Correlated local interfaces | Necessary and sufficient join-lifting criterion for universal greatestness; exact finite dynamic and cost enumeration | Other native categories, hidden coordination resources, and practical scaling |
| Causal approximation | Complete finite infinite-horizon verifier; a compact counterexample to an overbroad existence claim; contraction-based synthesis | Optimal causal covers without the stated stability/finite hypotheses |
| Quantum recovery | Improved general dimension-dependent estimate; sharp qubit envelope; exact qubit observable optimization and rational Pauli recovery | Sharp higher-dimensional constants and general capability geometry |
| Fragmentation | Exact compressed full frontier; NP-complete scalar decision; fixed-parameter tractability in distinct row patterns; executable witnesses | Competitive large-instance methods and external application benchmarks |
| General nonlinear repair | Existence of optimal repair within compact Lipschitz-bounded contracts; relaxation limit; finite-net error bounds; polynomial decision reduction | Unrestricted encoder classes, general repair moduli and effective convergence rates |
| Effective infinite models | A universal terminating exact algorithm is impossible on all computable presentations; exact finite/native positive cases remain available | Particular PDE/channel hypotheses and effective restricted infinite classes |

These statements resolve specified questions. They do not turn the entire BM research program into a finished theory. In particular, replacing “continuous” by “polynomial,” or “all dimensions” by “qubits,” is recorded as a restricted result rather than closure of the original broad question.

## 2. Scalar polynomial autonomy and the first interior Jordan case

### BM18-J1. Polynomial scalar factors of a unipotent map are first integrals

Let U be a real unipotent linear automorphism of R^n. Let R:R^n→R be a polynomial. Suppose a single-valued function F:R(R^n)→R(R^n), with no initially assumed regularity, satisfies

\[
R(Ux)=F(R(x))\qquad(x\in\mathbb R^n).
\]

Then R(Ux)=R(x) for every x.

**Proof.** The image I=R(R^n) is an interval. A constant R is immediate, so assume I has more than one point.

First F is continuous. For an interior y in I, choose two points whose R-values bracket y and connect them by a compact path. Every value sufficiently close to y has a preimage on that path. Given a sequence y_j→y, choose these preimages x_j. Any convergent subsequence has limit x with R(x)=y, and continuity of R∘U gives F(y_j)→R(Ux)=F(y). Compactness and uniqueness of this limit prove convergence of the full sequence. At an included endpoint of I, use a path from a preimage of that endpoint to a point with another value. This gives the same one-sided argument.

The invertibility of U makes F onto I. If F(z)=F(w), take R(x)=z and R(y)=w. Iteration yields R(U^k x)=R(U^k y) for all integers k≥1. Since U=I+N with N nilpotent, its integer powers are finite sums of binomial polynomials in k. Both sides are therefore polynomials in k. Equality at infinitely many integers implies equality at k=0, so z=w. Thus F is a continuous bijection of an interval, hence an increasing or decreasing homeomorphism.

The value c=R(0) is fixed by F. If F is increasing and z is not fixed, the two-sided orbit F^k(z) is strictly monotone in k. One of its two integer half-orbits is bounded between z and c: choose the forward or backward direction according to the positions of z and F(z). But F^k(z)=R(U^k x) for all integers k, and a nonconstant real polynomial cannot remain bounded on an integer half-line. Hence every z is fixed.

If F is decreasing, apply the increasing argument to F² and U². It gives F²=id. For each x the polynomial k↦R(U^k x) is then two-periodic on the integers. A polynomial with that property is constant. Again F=id. ∎

If U=e^{hN}, h>0 and N nilpotent, the polynomial t↦R(e^{tN}x) is h-periodic, since R(Uy)=R(y) for every y. It is therefore constant. Thus sampled scalar polynomial autonomy already gives invariance under the whole nilpotent flow. This conclusion uses global closure on all R^n, not closure only on a bounded performance set.

**The polynomial restriction is essential, even against infinitely smooth alternatives.** For the three-state chain below, write b=x_2,c=x_3 and define

\[
R(x)=
\begin{cases}
\exp(-1/c^2+b/c),&c\ne0,\\
0,&c=0.
\end{cases}
\]

This is globally C∞: on every bounded b-region, each derivative is bounded by a polynomial in 1/|c| times exp(−1/c²+B/|c|), which tends to zero as c→0. Yet R(Φ_h x)=e^{εh}R(x), so it is a smooth sampled-autonomous scalar encoder with a smooth linear update and is not a first integral. It vanishes on the whole plane c=0, so it does not improve the trajectory optimum established below. Its role is to rule out an unjustified extension of BM18-J1 from polynomials to all smooth encoders.

### BM18-J2. Exact n=3, d=1 trajectory optimum for polynomial encoders

Consider

\[
\dot x_1=\epsilon x_2,\qquad
\dot x_2=\epsilon x_3,\qquad
\dot x_3=0,\qquad \epsilon\ne0.
\]

The task is the full trajectory x_1(t), 0≤t≤T with T>0, measured in L²[0,T]. Performance is the worst case over the Euclidean unit ball of initial conditions. The encoder is a global scalar polynomial R, with exact sampled autonomy at any fixed h>0. The trajectory decoder may be arbitrary.

The optimum is

\[
E_{\rm poly}(3,1)^2
=\frac T2\left[
1+\frac{s^2}{3}
+\sqrt{\left(1-\frac{s^2}{3}\right)^2+s^2}
\right],
\qquad s=\epsilon T.
\]

It equals the known optimum among closed linear scalar encoders.

**Proof.** BM18-J1 makes R a first integral. We first prove a stronger lower-bound fact for any continuous first integral, even a nonpolynomial one.

On the plane x_3=0 with x_2=b≠0, flow translates x_1 through all real values. Hence R(a,b,0)=g(b), independently of a. Continuity extends this independence to b=0.

For c≠0, the flow time t=−2b/(εc) sends (a,b,c) to (a,−b,c). Invariance and the limit c→0 give g(b)=g(−b). Therefore

\[
R(a,b,0)=R(-a,-b,0)
\]

for every a,b. At these indistinguishable antipodal states the task trajectories are opposite:

\[
(\mathcal O_2(a,b))(t)=a+\epsilon tb.
\]

For any common decoder value w, the triangle inequality implies

\[
\max\{\|\mathcal O_2z-w\|_2,\|-\mathcal O_2z-w\|_2\}
\ge \|\mathcal O_2z\|_2.
\]

Maximizing over unit z gives the lower bound ||O_2||. The encoder R(x)=x_3, autonomous by F=id, with decoder t↦ε²t²R(x)/2 attains it. Its residual is exactly O_2(x_1,x_2).

Finally O_2*O_2 has matrix

\[
\begin{pmatrix}
T&\epsilon T^2/2\\
\epsilon T^2/2&\epsilon^2T^3/3
\end{pmatrix}.
\]

Its largest eigenvalue is the displayed expression. ∎

For ε=T=1, the squared error is (4+√13)/6, and the error is approximately 1.1258738292. The verification file encloses this value using rational arithmetic.

**Do not extend the argument without proof.** A global continuous sampled factor need not satisfy the polynomial step in BM18-J1. Also the antipodal restriction just proved is special to the three-state scalar case. For the four-state chain,

\[
I(x)=x_3^3-3x_2x_3x_4+3x_1x_4^2
\]

is a polynomial first integral, yet on x_4=0 it equals x_3³, which is odd. This explicitly blocks an attempted extension asserting that every scalar first integral is even on the whole preceding coordinate hyperplane. The supplied coefficient checker verifies this identity.

## 3. Correlated contexts: an exact universal criterion

### Definitions for this section

Let X_i be finite nonempty sets and K⊆∏_i X_i a nonempty legal context. Let B_i be fixed legacy equivalences. A local interface family E=(E_i) is allowed when each E_i⊆B_i, where inclusion means “identifies no more pairs than.” Its induced equivalence on legal states is

\[
x\,\Gamma_K(E)\,y
\quad\Longleftrightarrow\quad
x_i\,E_i\,y_i\ \text{for every }i.
\]

Joins of local families are coordinatewise equivalence joins. Joins of relations on K are equivalence joins on K.

A native action is a deterministic partial function f_a:D_a→K. For a task τ:K→Y, a family is feasible when:

1. Γ_K(E)⊆ker τ;
2. every D_a is Γ_K(E)-saturated;
3. x Γ_K(E) y in D_a implies f_a(x) Γ_K(E) f_a(y).

The second requirement retains availability. Omitting it would change the contract.

### BM18-C1. Universal greatestness is equivalent to join lifting

For fixed K and legacy bounds B, the following are equivalent:

**(a)** For every task and every collection of deterministic partial native actions on K, the feasible local families have a greatest member.

**(b)** For every pair of allowed families E,F,

\[
\boxed{\Gamma_K(E\vee F)=\Gamma_K(E)\vee\Gamma_K(F).}
\]

**Proof of sufficiency.** Equivalences on K that respect a fixed task and the native partial actions are closed under equivalence join. Indeed, a pair in the join has a finite chain of links from the constituent relations. The task is constant on every link. Domain membership propagates along every link, and, when enabled, applying f_a sends every link to another link in the same constituent relation. Thus the join is task-safe, availability-safe and stable.

Under (b), the coordinatewise join of two feasible local families induces exactly this stable join, so it is feasible. Finiteness gives closure under the join of all feasible local families. The discrete family is feasible, so the feasible set is nonempty. Its join is the greatest feasible family.

**Proof of necessity.** Always Γ_K(E)∨Γ_K(F)⊆Γ_K(E∨F). If equality fails, put H=Γ_K(E)∨Γ_K(F) and choose legal x,y identified by Γ_K(E∨F) but not by H. Use the task τ:K→K/H and only the identity action. Both E and F are feasible. Any family above both is above E∨F and therefore identifies x,y, violating the task. No greatest feasible family can exist. ∎

This is a structural classification, independent of a particular task. The criterion is not merely the older instruction to join all feasible families for one already-fixed task.

An equivalent finite test is connectivity: inside each cell of Γ_K(E∨F), connect two legal states when they are related by Γ_K(E) or Γ_K(F). Every such graph must be connected.

For full Cartesian K the condition holds: change one coordinate at a time along a local E_i/F_i chain, keeping the other coordinates fixed. Those intermediate states stay legal. Cartesian structure is sufficient but not necessary. The binary L-shaped context {(0,0),(0,1),(1,0)} passes the criterion. The diagonal {(0,0),(1,1)} fails: retaining only the first coordinate and retaining only the second are incomparable feasible choices for the nonconstant task.

### BM18-C2. Exact finite dynamic and cost synthesis

Enumerate the partitions E_i refining B_i, test the three feasibility conditions, and minimize any explicitly evaluable declared cost over the feasible families. This terminates because the search space is finite. The discrete family guarantees at least one feasible family for the stated deterministic model. A greatest interface is unnecessary for cost optimization: incomparable feasible families can be compared by cost.

The count of candidate families is at most ∏_i Bell(|X_i|). For each family, feasibility can be checked by all legal pairs and all native actions. This is an exact finite algorithm, with no polynomial-time claim.

The implementation's default cost is a weighted sum of local alphabet sizes. It is not a bit-count formula, a communication protocol cost or a physical implementation cost. The Python interface accepts a caller-supplied cost function; a new resource model must state its own cost and admissibility constraints.

The universal criterion and the task-specific optimizer have been checked against independent cell-based and order-based oracles on all 15 nonempty subsets of a binary two-coordinate product, all task partitions on each context, and all single deterministic partial actions: 10,771 instances. Thirteen of those contexts satisfy universal greatestness; the two diagonals do not. This finite check supports the implementation, not the universal proof by itself.

## 4. Fragmentation: exact frontier, complexity and parameterization

Let M be a binary matrix with n≥1 columns and nonempty rows. A column order π gives each row i a number b_i(π) of maximal one-blocks. Positive integer weights w_i represent row multiplicities. Define

\[
B(\pi)=\sum_{b_i(\pi)>1}w_i,\qquad
D(\pi)=\sum_iw_i(b_i(\pi)-1),\qquad
D_k=\min_{B(\pi)\le k}D(\pi).
\]

If the constraint is infeasible, D_k=+∞. The implementation represents that value by JSON null.

### BM18-F1. Duplicate compression preserves the Pareto frontier

Identical rows can be merged by adding their weights. Identical columns can be grouped adjacently in a Pareto witness without increasing any row's block count.

**Proof for columns.** From any order, delete all but one member of an identical-column group. Deleting an entry from a binary word never increases its number of one-blocks. Reinsert the deleted copies beside the retained column. Repetition of its bit extends an existing run or a zero-run and adds no one-block. Repeat for every identical-column group. Conversely, expanding a compressed order by adjacent duplicate copies preserves every row's block count. Therefore every original order is weakly dominated by an expanded compressed order, and the exact Pareto frontier is unchanged. ∎

After row compression let r be the number of distinct row patterns. There are q≤min(n,2^r) distinct column patterns.

### BM18-F2. A smaller exact frontier dynamic program

Use states (S,j,F), where S is the subset of placed column patterns, j is the last pattern, and F is the set of rows already fragmented. Store the smallest accumulated D and a predecessor pointer.

Let ones(j) be the rows containing a one in column pattern j. Let seen(S)=∪_{j∈S}ones(j). The empty prefix has a zero sentinel. On appending a new pattern k define

\[
J=(\operatorname{ones}(k)\setminus\operatorname{ones}(j))
\cap\operatorname{seen}(S).
\]

Exactly the rows in J start an additional one-block. The update is

\[
(S,j,F,D)\longmapsto
(S\cup\{k\},k,F\cup J,D+\sum_{i\in J}w_i).
\]

**Proof of sufficiency of the state.** The next start decisions depend only on the last column. Whether a new start is the first block is determined by seen(S). Whether the row has already contributed to B is determined by F. Thus two prefixes with the same (S,j,F) have identical possible future cost increments. Retaining only the smaller D cannot discard an optimum. Induction on |S| proves exactness. At the full subset B is the weight of F. Take the minimum D for every B, remove dominated pairs and compute D_k by prefix minima. Predecessors give an actual order. ∎

There are at most 1+2^q q2^r states. A direct implementation uses time O(2^q q²2^r r) and O(2^q q2^r) records, apart from input and output storage and integer bit costs. Weight arithmetic is exact. Since q≤2^r, this is fixed-parameter tractable in r, though the bound is doubly exponential in r. It is also finite-parameter tractable in the original column count by the simpler n! enumeration. Neither statement promises practical speed for large parameters.

The implementation materializes all integer budgets 0≤k≤Σw_i for convenience. For binary-encoded very large weights, that output is pseudopolynomial in the total weight. The Pareto breakpoint list alone gives the same mathematical function with output bounded by the terminal states; users with large multiplicities should use that representation. The algorithmic state bound refers to this breakpoint representation.

### BM18-F3. The scalar decision problem is NP-complete

The unweighted decision problem “is there an order with D≤d₀?” is NP-complete even when every row has exactly two ones.

**Proof.** A permutation is a polynomial-size witness; its row-block counts are computed in polynomial time. For hardness, take an undirected graph G with one column per vertex and one two-one row per edge. An edge row has one block precisely when its endpoints are consecutive in the permutation. Hence

\[
B(\pi)=D(\pi)=|E(G)|-\#\{\text{consecutive pairs of }\pi\text{ that are graph edges}\}.
\]

There is a Hamiltonian path exactly when D≤|E(G)|−(|V(G)|−1). Thus Hamiltonian path reduces directly to the fragmentation decision problem.

If the decision format only permits nonnegative thresholds, a graph with fewer than |V|−1 edges is immediately a no-instance and can be mapped to the fixed triangle-edge matrix with threshold zero, also a no-instance.

The NP-completeness of undirected Hamiltonian path may be obtained from the classical undirected Hamiltonian-cycle problem: split a chosen vertex into two nonadjacent copies, attach each original incident edge to both copies, and attach a new leaf to each copy. A Hamiltonian path in the new graph must run between the two leaves; identifying the split copies closes a Hamiltonian cycle in the original graph. The reverse construction is immediate. Cases with fewer than three original vertices can be handled separately. Classical Hamiltonian-cycle hardness is the imported complexity ingredient [Karp1972]. ∎

Consequently computing the complete frontier is NP-hard. A uniformly polynomial exact algorithm for arbitrary input would imply P=NP. This does not preclude useful restricted classes, approximation, or better parameterized methods.

### Checked constructions

The solver was compared with independent permutation enumeration on 4,080 matrices, including repeated patterns and weighted rows. It also reproduced the established gap family for n=5,…,9:

| n | Minimum broken rows φ | Minimum extra blocks δ | Extra blocks at minimum breadth D_φ |
|---|---:|---:|---:|
| 5 | 1 | 2 | 2 |
| 6 | 2 | 3 | 4 |
| 7 | 3 | 4 | 9 |
| 8 | 4 | 5 | 12 |
| 9 | 5 | 6 | 20 |

Small reproducible timing cases and the exact input matrices are in the verification JSON. They test this implementation; they are not comparisons against established packages or external application benchmarks.

## 5. Infinite-horizon causal prediction

### BM18-A1. Complete finite verification by a greatest safe relation

Let X and Q be finite native and predictor state sets. For each action a let f_a and F_a be deterministic partial transitions. Let τ:X→Y and g:Q→Y be outputs in a metric space, and fix ε≥0. Initial native states form I⊆X.

Start with pairs (x,q) satisfying both d(τ(x),g(q))≤ε and equality of enabled-action sets. Repeatedly remove a pair if an enabled common action sends it outside the current relation. The process stabilizes at S_* after at most |X||Q| strict deletion rounds.

There exists an initialization ι:I→Q producing error at most ε, with correct availability for every action history and every horizon, if and only if every x∈I has some q with (x,q)∈S_*.

**Proof.** The stabilized relation is forward invariant, output-safe and availability-safe. Any initialization into it therefore satisfies the specification by induction on history length.

Conversely, all pairs satisfying the infinite-history specification belong to the initial safe relation. If they belong to the current relation, their successors also satisfy the infinite-history specification and belong to it. They survive each deletion round. Thus they belong to S_*. A removed pair has a finite witness: an immediate failure has the empty word, and a predecessor failure prepends its action. Deletion ranks strictly decrease along the witness, giving a length below |X||Q|. ∎

This verifier does not secretly reobserve the native state during prediction. Initialization chooses q once; subsequent evolution uses only q and the action.

For a fixed state budget, finite allowed output catalogue and finite transition architecture, enumerate all candidate predictors and run this verifier. This completely decides that finite synthesis contract and minimizes any finite declared cost. It does not cover an unrestricted continuum of possible outputs or arbitrary infinite state architectures.

### BM18-A2. Compact future profiles need not admit a finite autonomous approximation

Let X=S¹⊂R², f(x) an irrational rotation, and τ(x)=x. The infinite-horizon profile metric is

\[
\rho_\infty(x,y)=\sup_{t\ge0}\|f^t(x)-f^t(y)\|=\|x-y\|.
\]

Thus the profile space is compact and totally bounded. Nevertheless no finite autonomous deterministic predictor can achieve uniform-in-time error ε<1, even for a single fixed initial state, when its outputs are allowed anywhere in R².

**Proof.** Every orbit of a finite autonomous predictor is eventually periodic. On one eventual residue class modulo its period p the predicted output is a fixed vector v. The native states along that subsequence are dense on S¹ because p times an irrational rotation angle is irrational. Their supremum distance to v is 1+||v||≥1. A constant-zero predictor attains error 1.

For completeness, density follows because the closure of the cyclic subgroup generated by an irrational rotation is an infinite closed subgroup of the circle. A proper closed subgroup has a smallest positive angular spacing and is finite; hence the closure is the whole circle. Positive tails and p-step subsequences have the same closure. ∎

This refutes an infinite-horizon inference from total boundedness alone. A finite cover of full response profiles is not automatically a finite causal machine.

### BM18-A3. A uniform construction for contracting dynamics

Let X be a compact metric space and let all total native actions f_a have a common Lipschitz constant L<1. Suppose τ is C-Lipschitz. Choose a finite η-net {c_j}⊆X and a quantizer q with d(x,c_{q(x)})≤η. Define

\[
F_a(j)=q(f_a(c_j)),\quad g(j)=\tau(c_j),\quad \iota(x)=q(x).
\]

For any action sequence, if e_t is the native-to-representative state error, then e_0≤η and e_{t+1}≤Le_t+η. Therefore

\[
\sup_{t\ge0}d(\tau(x_t),g(q_t))
\le \frac{C\eta}{1-L}.
\]

This is an actual finite autonomous implementation. Partial action boundaries, additional physical implementation restrictions and a minimum-cardinality claim require separate arguments.

## 6. Nonlinear repair under explicit compactness conditions

### BM18-N1. Existence of an optimal conditioned nonlinear repair

Let X,Z,Y be nonempty compact metric spaces. Let f:X→X and τ:X→Y be continuous. Let r:X→W and h:Z→W be continuous maps into a metric space W. Fix finite Lipschitz bounds L_R,L_F,L_D. Optimize over

\[
R:X\to Z,\quad F:Z\to Z,\quad D:Z\to Y
\]

with those respective bounds, subject to h∘R=r and R∘f=F∘R. Use worst-case task error

\[
E(R,D)=\sup_{x\in X}d_Y(\tau(x),D(R(x))).
\]

If the feasible set is nonempty, E attains its minimum.

**Proof.** Each bounded-Lipschitz map family is equicontinuous and has compact target. Arzelà–Ascoli makes it compact in the uniform topology; the Lipschitz inequality is preserved under uniform limits. The product of the three map families is compact.

Uniform convergence preserves the constraints. For example, D_j∘R_j→D∘R uniformly because

\[
\sup_xd_Y(D_j(R_jx),D(Rx))
\le \|D_j-D\|_\infty+L_D\|R_j-R\|_\infty.
\]

The analogous bound applies to F_j∘R_j; h is uniformly continuous on compact Z. Thus the feasible set is closed. E is continuous under this convergence, so its minimum is attained. The same compactness argument works for finitely many native actions and their corresponding reduced updates. ∎

This theorem supplies global optimal existence within the stated class. It does not show that the class is nonempty or that its optimizer can be computed from arbitrary black-box continuous maps.

### BM18-N2. Relaxation convergence and finite-net certificates

Within the same fixed compact map class, relax both constraint residuals to at most δ. These feasible sets are nested compact sets. If exact feasibility holds, their minimum errors E_δ increase to E_0 as δ↓0.

**Proof.** E_δ≤E_0 and monotonicity gives a limit. For δ_j↓0 choose minimizing triples. A convergent subsequence exists by compactness, its limit satisfies the exact constraints, and continuity of E gives a limiting value at least E_0. Thus equality holds. If every positive-δ problem is feasible, compactness and the same argument imply exact feasibility. There is no asserted computable rate. ∎

When f,τ,h,r are Lipschitz, an η-net N⊆X gives explicit upper certificates:

\[
\begin{aligned}
E(R,D)&\le \max_{x\in N}d_Y(\tau x,DRx)
 +(L_\tau+L_DL_R)\eta,\\
c&:=\sup_Xd_Z(Rf,FR)
\le\max_{x\in N}d_Z(Rfx,FRx)+L_R(L_f+L_F)\eta,\\
\ell&:=\sup_Xd_W(hR,r)
\le\max_{x\in N}d_W(hRx,rx)+(L_hL_R+L_r)\eta.
\end{aligned}
\]

Each follows by comparing an arbitrary x to a net point and applying the triangle inequality to the two component maps. These are rigorous upper bounds when the net radius and Lipschitz bounds are themselves certified.

With reduced initialization z_0=R(x_0), the closure defect c accumulates as

\[
d_Z(R(x_t),F^t(z_0))\le c\sum_{j=0}^{t-1}L_F^j.
\]

The task error is therefore at most

\[
E(R,D)+L_Dc\sum_{j=0}^{t-1}L_F^j.
\]

If L_F<1 this is bounded uniformly by E+L_Dc/(1−L_F). Otherwise a fixed one-step defect alone does not supply a time-uniform guarantee.

### Why the conditioning cannot simply be dropped

On S¹ let f be rotation by irrational α, let F=id, and choose integers q_j with ||q_jα|| modulo 1 tending to zero. The maps R_j(z)=z^{q_j} are surjective and have closure residual

\[
\sup_z|R_j(fz)-R_j(z)|=|e^{2\pi iq_j\alpha}-1|\longrightarrow0.
\]

Every continuous exact first integral of f is constant, because its value is constant on each dense orbit. Yet every R_j is at uniform distance 2 from every constant map into S¹. Their Lipschitz constants are unbounded. This is an explicit failure of an unrestricted “small residual implies nearby exact repair” claim. A general repair modulus needs additional hypotheses.

### BM18-N3. Fixed-degree semialgebraic synthesis is decidable

Suppose all source/target sets are explicitly semialgebraic over the real algebraic numbers, all supplied native and task maps are polynomial over that field, and the dimensions and degree bounds of unknown R,F,D are fixed. Express their coefficients as unknown real variables.

Range containment, exact closure, legacy retention and a threshold e on squared Euclidean task error are first-order polynomial conditions, for example

\[
\begin{gathered}
\forall x\in X:\ R(x)\in Z,\quad h(R(x))=r(x),\quad
R(f(x))=F(R(x)),\\
\forall x\in X:\ \|\tau(x)-D(R(x))\|^2\le e^2.
\end{gathered}
\]

Quantify separately over z∈Z for the ranges of F,D. Euclidean Lipschitz caps are polynomial inequalities on pairs of points. Existence of coefficients is therefore a sentence in the first-order theory of real closed fields. Quantifier elimination decides it and, in a nonempty definable coefficient set over real algebraic parameters, permits an algebraic sample witness. Testing dimensions up to a prescribed finite bound determines the least feasible dimension in that degree-bounded class.

This is a reduction to an established decision procedure, not a new quantifier-elimination algorithm and not an implementation of one in the supplied Python package. It does not decide arbitrary smooth synthesis or an unbounded search over all degrees. A formalized algebraic foundation for real-closed-field quantifier elimination is described by Mahboubi and Cohen [MC2012].

## 7. Global smooth augmentation: a construction and sharp families

### BM18-G1. A finite-atlas augmentation with a smooth decoder

Let M be a compact smooth n-manifold without boundary, with a supplied finite atlas (U_i,φ_i), i=1,…,k. Choose a smooth partition of unity ψ_i subordinate to this cover, with support compactly contained in U_i. Let r:M→R^ℓ be a supplied smooth legacy map.

Define, extending by zero outside each chart,

\[
g(x)=\big(\psi_i(x),\ \psi_i(x)\phi_i(x)\big)_{i=1}^k
\in\mathbb R^{k(n+1)}.
\]

Then g, and therefore E=(r,g), is a smooth embedding. Every supplied smooth task τ:M→R^p has a smooth decoder on E(M), and on an ambient neighborhood of E(M).

**Proof.** Smoothness across the chart boundaries follows from the compact supports. If g(x)=g(y), choose i with ψ_i(x)>0. The matching scalar block gives ψ_i(y)=ψ_i(x)>0, and the matching vector block then gives φ_i(y)=φ_i(x). Thus y=x.

If dg_x(v)=0, the same positive ψ_i gives dψ_i(v)=0 and

\[
d(\psi_i\phi_i)(v)=\psi_i(x)d\phi_i(v)=0.
\]

The chart differential is invertible, so v=0. Thus g is an injective immersion. Compactness of M and the Hausdorff target make it a homeomorphism onto its image, hence an embedding. Adding r preserves these properties.

On the image define D=τ∘E^{-1}; it is smooth. More explicitly, in any ambient neighborhood where the i-th scalar block a_i is positive and the ratio b_i/a_i lies in φ_i(U_i), use the local decoder τ∘φ_i^{-1}(b_i/a_i). These neighborhoods cover E(M); an ambient smooth partition of unity glues the local formulas, which all agree with τ on E(M). The Euclidean task target permits this weighted gluing. A smooth cutoff equal to one near compact E(M) can extend the decoder to the whole ambient Euclidean space if required. ∎

All smooth native transitions descend on the image by E∘f∘E^{-1}. The theorem does not assert that an arbitrary prescribed ambient target architecture admits an extension that preserves additional constraints away from E(M).

This is an explicit upper bound of k(n+1) augmentation coordinates for a supplied atlas. It is not asserted to be the least dimension or the best general embedding bound. Its purpose is to make one global repair construction concrete.

### BM18-G2. Exact augmentation dimensions on spheres

Let M=S^n⊂R^{n+1}, n≥1, and require full-state recovery.

* With legacy r(x)=x_0, the minimum number of continuous augmentation coordinates is n. Retaining x_1,…,x_n attains it.
* With constant legacy, the minimum is n+1. Retaining all coordinates attains it.

**Proof.** In the first case the fiber r^{-1}(0) is S^{n−1}. An augmentation into R^m with m≤n−1 identifies an antipodal pair by Borsuk–Ulam (including the elementary S⁰ case). Their legacy values also agree, so full-state decoding is impossible. Thus m≥n, and the coordinate construction attains equality.

With constant legacy, apply Borsuk–Ulam directly to S^n for m≤n. The full coordinate embedding attains n+1. These lower bounds hold even with an arbitrary decoder, so they also hold under a smooth-decoder requirement. ∎

Local rank alone does not yield these global minima. The topological obstruction and the actual retained legacy both matter. General source/task/legacy/target classification remains a separate obligation.

## 8. Quantum recovery: improved constants and exact qubit results

### Fixed normalization and imported ingredient

Let N be a finite-dimensional CPTP channel with d-dimensional logical input and a Kraus representation with r operators E_i. Let

\[
\mathcal K=\operatorname{span}\{E_i^\dagger E_j\}
\]

and let A⊆M_d be a unital *-subalgebra. Use exactly the Research Edition's normalized commutator defect and unamplified recovery error:

\[
\kappa_A=
\sup_{\substack{Z\in\mathcal K,\ \|Z\|\le1\\X\in A,\ \|X\|\le1}}
\|[Z,X]\|,
\qquad
\delta_A=
\inf_{\mathcal R\ {\rm CPTP}}
\sup_{\substack{X\in A\\\|X\|\le1}}
\|X-N^\dagger\mathcal R^\dagger(X)\|.
\]

The norm is the operator norm. The recovery runs from the channel output back to the logical input. The complementary-channel quantity below is a different object; do not also name it δ.

Let P_{A'} be the trace-preserving conditional expectation onto the commutant. Set

\[
\beta=\|\widehat N-\widehat N P_{A'}\|_\diamond.
\]

The imported approximate-algebra recovery theorem gives a CPTP recovery with diamond reconstruction error at most 2√β relative to P_A. Restricting its adjoint error to A gives δ_A≤2√β. This is the upper bound in **Theorem 1** of the cited arXiv version of Bény [Beny2009]; the earlier Research Edition's “Theorem 3.1” locator should be read as corrected here. The lower bound in that paper concerns its diamond-error definition and is not silently transferred to BM's unamplified δ_A.

### BM18-Q1. Improved general bound

\[
\boxed{\delta_A\le
\min\{2,\ 2\sqrt{\min(d,r^2)\,\kappa_A}\}.}
\]

**Proof.** Put L=(I−P_{A'})\widehat N^\dagger. Since the adjoint complementary channel is unital completely positive, ||\widehat N^\dagger(B)||≤||B||. Its range is K. Averaging conjugation by unitaries in A gives P_{A'}, so

\[
\|Z-P_{A'}Z\|
\le \sup_{U\in\mathcal U(A)}\|[Z,U]\|
\le\kappa_A\|Z\|\quad(Z\in\mathcal K).
\]

Thus ||L||_{∞→∞}≤κ_A. Its trace-dual Δ=\widehat N−\widehat N P_{A'} has ||Δ||_{1→1}≤κ_A.

For unit vectors u,v in C^d⊗H, write Schmidt decompositions with coefficients s_i,t_j. The trace norm of (Δ⊗id)(uv†) is at most

\[
\kappa_A\Big(\sum_i s_i\Big)\Big(\sum_j t_j\Big)
\le d\kappa_A.
\]

Here each input rank-one factor has trace norm one, each ancillary rank-one factor has trace norm one, and each Schmidt rank is at most d. Extending by a singular-value decomposition proves β≤dκ_A for arbitrary ancilla dimension.

For the alternative environment bound, write an amplified B in r×r blocks B_{ij}. Since ||L(|i⟩⟨j|)||≤κ_A and every block norm is at most ||B||, the triangle inequality gives ||(L⊗id)(B)||≤r²κ_A||B||. Hence β≤r²κ_A as well. Combine both bounds with the imported δ_A≤2√β. Finally δ_A≤2 follows because both the identity and N†R† are contractions on the operator unit ball. ∎

This estimate is conservative in higher dimensions. In particular, it need not become informative when only the physical channel is weakly noisy.

### BM18-Q2. What the normalized operator-system defect can and cannot measure

For the full logical algebra A=M_d, κ_A is either zero or two.

**Proof.** If K=CI, all commutators vanish. Otherwise the unital self-adjoint space K contains a nonscalar Hermitian H. Subtract the midpoint of its largest and smallest eigenvalues times I and normalize the resulting operator. This produces Z∈K with ||Z||=1 and extreme eigenvalues ±1. A norm-one operator taking an extreme eigenvector to the opposite one has commutator norm two with Z. The general upper bound is two, so κ_A=2. ∎

Thus a channel whose nontrivial error operators become arbitrarily small can retain κ_A=2. Normalizing every member of their span removes the channel's amplitude scale. A channel-weighted quantity such as β is needed to track that continuity directly.

### BM18-Q3. Sharp universal qubit upper envelope

For logical input dimension d=2, any CPTP channel, and any unital *-subalgebra A⊆M_2,

\[
\boxed{\delta_A\le\kappa_A/2.}
\]

This is the sharp universal upper bound as a function of κ_A over this class: every value κ∈[0,2] has an example with δ=κ/2. For every fixed κ>0 the infimum of δ among examples with that κ is zero. Thus κ does not specify the actual recovery error.

**Proof.** Every unital *-subalgebra of M_2 is CI, the full matrix algebra, or a two-dimensional algebra generated by A_u=u·σ for a real unit vector u.

The completely depolarizing recovery gives δ_A≤1 for every such algebra. For the full matrix algebra this uses the norm-one traceless projection

\[
P_0(X)=X-\tfrac12\operatorname{tr}(X)I
=\tfrac12(X-\sigma_y X^{\mathsf T}\sigma_y).
\]

The second expression proves ||P_0||≤1 since transpose and unitary conjugation preserve operator norm; a Pauli matrix attains one.

Write the Hermitian part of K as RI⊕{v·σ:v∈V}, where V is a real subspace of R³.

For A=CI both errors vanish. For A=M_2, BM18-Q2 gives κ=0 or 2. At κ=0 the exact commutant recovery theorem gives δ=0; at κ=2 the depolarizing recovery gives δ≤1.

Now let A=C*(A_u). If dim V≥2, V contains a unit vector v perpendicular to u. The commutator of v·σ and u·σ has norm two, so κ=2 and δ≤1 suffices.

If V={0}, exact recovery gives δ=0. In the remaining case V=Rv for a unit vector v. Then K=span{I,v·σ} and

\[
\kappa_A=2\sqrt{1-(u\cdot v)^2}.
\]

To verify the supremum, write Z=aI+b(v·σ), X=cI+e(u·σ). The constraints ||Z||,||X||≤1 imply |b|,|e|≤1, and the commutator norm is 2|be|√(1−(u·v)²). Choosing b=e=1 attains the bound.

The exact commutant theorem supplies a CPTP recovery preserving the algebra C*(v·σ). Follow it by dephasing along v. On A_u the recovered observable is (u·v)v·σ. The error norm is √(1−(u·v)²)=κ_A/2. On any element cI+eA_u of the algebra, |e|≤||cI+eA_u||, so this same bound controls its whole unit ball.

For sharpness use complete dephasing along v. Its complementary error space is span{I,v·σ}; every recovered observable remains in that span. The component of u perpendicular to v has norm √(1−(u·v)²), giving the matching lower bound. Choose u·v to realize any κ in [0,2].

Finally replace complete dephasing by partial dephasing with transverse Bloch multiplier λ∈[0,1). Its operator system is the same span for every λ<1, so κ stays fixed. Identity recovery already has error at most (1−λ)√(1−(u·v)²), which tends to zero as λ↑1. This proves the lower-envelope assertion without claiming δ=0 at any nonzero κ. ∎

This settles a sharp normalized-defect question for qubits, including arbitrary output dimension. It does not supply the sharp higher-dimensional envelope.

### BM18-Q4. Exact recovery of one qubit observable algebra

For a qubit-to-qubit channel with Bloch action x↦Ax+t and a task algebra generated by A_u=u·σ, ||u||=1,

\[
\boxed{
\delta_{A_u}=
\min_{|b_0|+\|v\|\le1}
\left(|b_0+t\cdot v|+\|u-A^{\mathsf T}v\|\right).
}
\]

**Proof.** A unital positive adjoint recovery sends A_u to a Hermitian contraction B=b_0I+v·σ, precisely satisfying |b_0|+||v||≤1. Conversely every such B is realized by measuring the effects (I±B)/2 and preparing the ± eigenstates of A_u, which is CPTP.

The channel adjoint sends B to (b_0+t·v)I+(A^T v)·σ. The difference from A_u has norm |b_0+t·v|+||u−A^T v||. As above, the error on A_u controls exactly the unit ball of its two-dimensional algebra. Minimization gives the formula. ∎

This is a convex second-order cone optimization, with a directly realizable recovery. For a unital channel, b_0=0 is optimal, and δ is the Euclidean distance from u to the ellipsoid A^T{v:||v||≤1}.

For dephasing A=diag(λ,λ,1), 0<λ<1, the nontrivial case can be computed from a single multiplier μ>0. Writing a_i for the diagonal entries,

\[
\sum_i\frac{a_i^2u_i^2}{(a_i^2+\mu)^2}=1,\qquad
v_i=\frac{a_i u_i}{a_i^2+\mu},\qquad
\delta^2=\sum_i\frac{\mu^2u_i^2}{(a_i^2+\mu)^2}.
\]

The left side is strictly decreasing in μ on the nontrivial support, so the root is unique when u lies outside the ellipsoid. These equations follow from minimizing ||u−Av||² subject to ||v||≤1 and the convex Lagrange multiplier conditions. If u already lies in the ellipsoid the distance is zero. The λ=0 case uses the corresponding segment directly.

The supplied exact rational bracketing example λ=1/2, u=(3/5,0,4/5) has error approximately 0.2622622320. The rational inequalities, not the decimal display, are the numerical certificate.

### BM18-Q5. Exact full-algebra recovery for Pauli channels

Let N be a qubit Pauli channel with probabilities p_0,p_x,p_y,p_z. Its Bloch multipliers are

\[
\lambda=(p_0+p_x-p_y-p_z,\ p_0-p_x+p_y-p_z,\ p_0-p_x-p_y+p_z).
\]

The optimal unamplified full-algebra error is the linear-program value

\[
\min_{q\ge0,\ \sum q=1}\ \max_{i=x,y,z}(1-\alpha_i(q)\lambda_i),
\]

where α(q) is obtained from q by the same Pauli-multiplier formula.

**Proof.** Twirl any recovery over Pauli conjugations. The noise channel commutes with those conjugations, the target identity is covariant, and the operator-norm objective is convex and unchanged by conjugation. The twirled recovery is a Pauli channel with no greater error.

The resulting error map vanishes on I and multiplies σ_i by a_i=1−α_iλ_i≥0. Its induced operator norm is max_i a_i. For the upper bound, first apply the norm-one traceless projection P_0. On traceless matrices, every coordinate sign flip in the Pauli basis is an operator-norm isometry: orthogonal actions with determinant one come from unitary conjugation, and determinant-minus-one actions also use transpose. Any real diagonal multiplier with entries in [−1,1] is a convex combination of these sign flips. Scaling gives the upper bound max_i|a_i|; a Pauli matrix for a maximizing coordinate gives equality.

Minimizing that maximum over the probability simplex is exactly the displayed LP. ∎

For rational noise probabilities, the implementation enumerates rational vertices of a four-variable LP and returns both a feasible recovery and nonnegative dual multipliers with the same objective. Those matching rational values certify optimality. It is not relying on a floating solver's status string.

For an isotropic depolarizing multiplier λ∈[0,1], the answer is δ=1−λ: α_i≤1 supplies the lower bound, and identity recovery attains it. For λ<1 its full-algebra normalized κ equals two, while δ tends to zero as λ tends to one.

## 9. Effective infinite presentations: a universal impossibility result

### BM18-I1. Exact future equivalence is not decidable on all computable carriers

There is no algorithm that always terminates and decides exact future equivalence for every countable, effectively presented deterministic system, even with one total computable update and one binary task.

**Proof.** Use the countable carrier of configurations of a universal Turing machine, together with an extra absorbing state ⊥. The update performs one machine step; halting configurations and ⊥ are absorbing. Let the task be one on halting configurations and zero elsewhere.

For the effectively given initial configuration c_e encoding a machine and input, c_e and ⊥ have equal task outputs at every future time exactly when that machine never halts. A terminating exact equivalence decider would therefore decide halting by negating its answer. Such a decider is impossible.

The underlying diagonal contradiction is brief: if H(p,x) decided whether program p halts on x, construct D(x) to loop when H(x,x) says “halts,” and to halt otherwise. Applying D to its own program description contradicts either answer of H. ∎

The same obstruction applies to a universal terminating quotient constructor that returns codes with decidable equality and whose code equality exactly captures future equivalence. It does not prohibit a non-effective semantic quotient.

Finite-horizon equivalence remains decidable by direct iteration. Inequivalence is semidecidable by searching for a finite distinguishing time (or, with finitely many actions, a distinguishing word). Full equivalence is not generally decidable. This is a precise limit on a universal algorithm, not a statement that a particular heat equation, quantum channel or physically specified PDE has no useful effective theory.

## 10. Finite operational realizations of Seed, Rooting and Rebranching

These are explicit finite native conventions. They finish an executable interpretation of the candidate vocabulary; they do not assert a unique universal interpretation or alter the V1 core.

### BM18-O1. Finite Seed

A finite Seed consists of a finite typed variable list with domains D_i, a partial assignment, and a supplied set or decidable predicate of allowed complete assignments. Its realizations are exactly the completions respecting all three. Enumeration terminates. An empty result is a valid infeasibility answer; there is no theorem that a Seed must grow into a realization.

The solver preserves every realization rather than arbitrarily declaring one canonical. A requested choice needs a declared order, cost or selection rule.

### BM18-O2. Finite Rooting

Given a realization s, a declared typed export e, and receiver predicates for applicability and admissibility, compute v=e(s). Return:

* not applicable if the applicability predicate fails;
* rejected if applicable but inadmissible;
* accepted if both predicates pass.

A Root is the receiver-relative accepted export with its provenance. Merely computing an export does not make it accepted. The code's simple result is a status record; a production use must attach the actual source/receiver identifiers and evidence required by its passport.

### BM18-O3. Finite Rebranching

Given source and target realization sets, a proposed transport H, and declared tasks τ_S,τ_T, a task-preserving rebranching satisfies

\[
H(\operatorname{Real}(S))\subseteq\operatorname{Real}(T),
\qquad \tau_T\circ H=\tau_S.
\]

Both conditions are decidable by finite enumeration. If accepted exports must also be preserved, add the corresponding export square and receiver-passport implication. Task preservation alone does not imply passport preservation.

### BM18-O4. Composition and passport transport

If H:S→T and J:T→U satisfy the displayed realization and task conditions, J∘H does too, by substitution. If, additionally, both mappings preserve the applicable/accepted passport predicates through their declared export squares, their composite preserves those predicates. This proves finite operational consistency. It does not establish physical causation or canonical selection.

The reference tests cover successful and empty Seeds, all three Rooting outcomes, and accepted and rejected rebranching witnesses.

## 11. Native witnesses for the locality clauses

### BM18-L1. Sharp one-dimensional wave restriction radius

For the classical one-dimensional wave equation u_tt=c²u_xx on R, c>0, with smooth initial displacement f and velocity g, d'Alembert's formula gives

\[
u(0,t)=\frac{f(-ct)+f(ct)}2+
\frac1{2c}\int_{-ct}^{ct}g(y)\,dy.
\]

The output over 0≤t≤T depends only on the initial data restricted to [−cT,cT]. Among centered restriction carriers [−r,r], this radius is sharp: for any 0≤r<cT choose f=0 and a nonzero nonnegative smooth g supported inside (r,cT). These data agree with zero on [−r,r], but u(0,T)>0. The formula follows by differentiating and checking the initial data, or by decomposing the solution into left- and right-moving waves.

This supplies an actual native realization of the finite-propagation conditional clause. It does not prove that every optimal encoder must literally store the whole interval, nor does it assert finite propagation for other PDEs.

### BM18-L2. A quasistatic problem has a different carrier

For −u''=f on (0,1), u(0)=u(1)=0, the Green function is

\[
G(x,y)=\min(x,y)(1-\max(x,y)),\qquad
u(x)=\int_0^1G(x,y)f(y)\,dy.
\]

It is positive for interior x,y. A positive forcing bump supported away from a neighborhood of x_0 still changes u(x_0), although the local forcing data at x_0 are unchanged. For example, x_0=1/4 and the integrable forcing f=1 on [1/2,3/4], zero elsewhere, give u(x_0)=3/128 exactly.

This is a direct counterexample to inheriting a finite spatial restriction rule merely by using similar field notation. No convergence of a dynamical model to this elliptic model has been asserted. Such a limit, if desired, needs its own topology, boundary conditions, scaling and proof.

## 12. What is executable and what was checked

The accompanying reference package uses Python 3.10 or later and the standard library. Keep the solver, examples and verification script together.

    python BM_Finite_Solvers_2026-10-18.py BM_Solver_Examples_2026-10-18.json
    python BM_Solver_Verification_2026-10-18.py

| Component | Delivered computation | Verification evidence |
|---|---|---|
| Fragmentation | Full Pareto breakpoints, every budget value, actual column-order witnesses | 4,080 independent permutation comparisons; five gap-family instances |
| Correlated interfaces | Universal criterion with negative witness; exact dynamic feasibility and cost optimizer | 10,771 independent finite task/action comparisons over all 15 binary contexts |
| Infinite-horizon finite prediction | Greatest safe relation, initialization decision, finite failure words; minimum-state finite-catalogue synthesis | 1,376 independent reachability comparisons; all failure words replayed; three bounded synthesis cases |
| Pauli recovery | Rational optimum, recovery probabilities, primal/dual certificate | 153 rational noise instances with exact certificate checks |
| Jordan examples | Exact flow identities and a rational enclosure of the sharp n=3 polynomial value | Coefficient equality for two invariants; exact Gram polynomial root bracket |
| Qubit observable example | Rational secular-root and error-squared enclosures | Monotone root bracket, with decimal display explicitly approximate |
| Finite operational conventions | Seed completion, Rooting statuses and rebranching checker | Seven specified examples |
| Native quasistatic example | Exact Green-function integral | Rational result 3/128 |

The check suite passed. The JSON records exact rational quantities, deterministic seed, source hashes, input matrices and timing observations. Timings are specific to this run and are not a performance guarantee.

The supplied package does not implement general quantifier elimination, unrestricted nonlinear functional optimization, general CPTP optimization, a PDE solver or a proof assistant. Those statements are mathematical reductions or proofs in this document. The Python checks are supporting evidence for the finite implementations.

## 13. Remaining obligations, stated without inflated completion claims

1. **Jordan:** prove an equally sharp bound or give a counterexample for arbitrary globally continuous sampled-autonomous encoders in the original interior regime. Polynomial invariance does not settle it.
2. **Global smooth minimum:** for a given general source, task, legacy and target architecture, establish the least augmentation dimension, including singular fibers and topology. The atlas construction is an upper bound, not the classification.
3. **Causal optimum:** characterize finite approximate causal implementations beyond the contraction and finite-state contracts, including controlled optimal cost. The rotation obstruction prevents an unrestricted existence theorem.
4. **Higher-dimensional quantum sharpness:** determine the optimal normalized-defect envelope or suitably channel-weighted alternatives above logical dimension two, and the stated capability geometry.
5. **Unrestricted nonlinear repair:** identify assumptions giving effective repair moduli and optimizer computation outside the compact Lipschitz and finite-degree algebraic classes. Vanishing residuals alone do not suffice.
6. **Restricted infinite/native theories:** prove regularity, effective presentation and quantitative closure for each intended infinite-dimensional application. The universal algorithm has been ruled out; these application-specific problems have not.
7. **Validation and positioning:** obtain independent checking or formalization of selected proofs, external benchmarks and theorem-by-theorem prior-art comparisons. Internal checks do not satisfy these external gates.

The finite correlated-context question and the mathematical fragmentation complexity/parameterization question now have exact answers under their explicit contracts. Their implementations are complete reference implementations for those contracts. Practical scaling and application evaluation remain separately tracked. Seed, Rooting and Rebranching have finite operational definitions; universal claims about them remain candidates.

The appropriate release claim is therefore: **BM has an internally established core, additional proved and executable extensions, explicit impossibility boundaries, and a shorter, precisely stated research remainder. It is not a fully closed research program or a verified universal physical theory.**

## References and provenance

* **BM-R3.** Branch Mathematics Research Edition, Library version 3, inspected 18 October 2026. Governing source for the existing contracts and theorem families. The version-3 source snapshot remains unchanged; this development is appended in version 4.
* **BM-I6.** BM Outstanding Issues, 14 October 2026, version 6. Earlier broad completion wording is interpreted through the current completeness register and this scoped continuation.
* **Beny2009.** Cédric Bény, “Conditions for the approximate correction of algebras,” arXiv:0907.4207. Exact commutant criterion and Theorem 1's approximate upper bound are imported mathematical ingredients, not BM discoveries. https://arxiv.org/pdf/0907.4207
* **Karp1972.** Richard M. Karp, “Reducibility Among Combinatorial Problems,” in Complexity of Computer Computations. The classical Hamiltonian-cycle hardness is the imported ingredient in BM18-F3; the two-one-row construction and split-vertex reduction are written out here. https://www2.seas.gwu.edu/~simhaweb/champalg/tsp/papers/KarpOriginal.pdf
* **MC2012.** Assia Mahboubi and Cyril Cohen, “Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination,” Logical Methods in Computer Science 8(1), 2012. https://arxiv.org/abs/1201.3731
* **Turing1937.** A. M. Turing, “On Computable Numbers, with an Application to the Entscheidungsproblem,” Proceedings of the London Mathematical Society s2-42, 230–265. The halting obstruction is classical; the BM future-equivalence reduction is explicit above. https://doi.org/10.1112/plms/s2-42.1.230
* Classical ingredients also include Borsuk–Ulam, partitions of unity, compact injective-immersion embedding, Arzelà–Ascoli, finite safety fixed points, LP duality and the elementary wave/Green formulas. They are not presented as newly discovered mathematics. The contribution claimed here is the written contract-specific development; no exhaustive novelty search has been completed.


# 20 October continuation: continuous closure and completion work

20 October 2026. Research Edition continuation. The frozen V1 foundation is unchanged.

This note continues the unresolved contracts recorded on 19 October. It does not use a change of definitions to declare the research program complete. Proofs below are mathematical arguments, not independent peer review or proof-assistant certification. Historical novelty has not been established.

## 1. Removing the polynomial restriction in the three-state Jordan problem

### BM20-J1. A continuous scalar factor has an ordered, invertible refinement

Let U be a homeomorphism of R^n. Let R:R^n→R be continuous, and suppose a single-valued F on I=R(R^n) satisfies R U=F R. There are an interval J⊆R, continuous maps q:R^n→J and p:J→I, and a monotone homeomorphism g:J→J such that

\[
R=pq,\qquad qU=gq.
\]

The refinement retains the entire past of R in the sense that

\[
q(x)=q(y)\quad\Longleftrightarrow\quad
R(U^{-k}x)=R(U^{-k}y)\ \text{for every integer }k\ge0.
\]

This is an existence result for a continuous scalar coordinate. It does not give a finite-precision algorithm for constructing that coordinate, and it does not assert that F itself is injective or monotone.

**Proof.** A constant R is immediate. Otherwise I is a nondegenerate interval. First F is continuous: for any y∈I, join preimages of values bracketing y by a compact path in R^n. Nearby values have preimages on this path; compactness, continuity of R U, and the single-valued factor identity show that F(y_j)→F(y) whenever y_j→y. At an included endpoint, use a path from a preimage of that endpoint to a preimage of an interior value. Invertibility of U makes F onto I.

Form the history map

\[
H(x)=(R(x),R(U^{-1}x),R(U^{-2}x),\ldots)
\]

with its product topology, metrized by

\[
d(z,w)=\sum_{k\ge0}2^{-k-1}\min\{1,|z_k-w_k|\}.
\]

The map H is continuous. For each closed Euclidean ball B_m of integer radius m≥1, let K_m=H(B_m). These are nested compact connected metric spaces. Each is locally connected: a ball is a continuous image of [0,1], and so is K_m; the Hahn–Mazurkiewicz characterization applies.

If K_m is nondegenerate, it is also arc-like. Indeed, projection to coordinate N has an interval image. Two histories with equal Nth coordinate have equal coordinates 0,…,N, because z_k=F^{N-k}(z_N). Its fibers therefore have diameter at most 2^{-N-1}. For all sufficiently large N the image interval is nondegenerate, and rescaling it gives arbitrarily small-fiber continuous surjections onto [0,1]. A locally connected, arc-like metric continuum is an arc. These two classical continuum-theory facts are the only imported topological ingredients; see [Nadler1999, §1] and [Bankston2019, §6; reference 26, Chapter XII].

Consequently each K_m is an arc or a point. Orient the nested nondegenerate arcs consistently. Parameterize the first one by a real compact interval and extend the parameterization over any additional end pieces of each larger arc. The extensions agree on previous arcs. Their union gives a bijection θ:H(R^n)→J onto a real interval, whose restriction to each K_m is a homeomorphism. (One can give each newly added nonempty end piece length one.) Set q=θH and p=π_0θ^{-1}.

Both maps are continuous. For q, every point of R^n has a neighborhood in some B_m, where the composition is continuous. For p, any point of J and a sufficiently small one-sided or two-sided interval neighborhood lie in one of the parameter intervals θ(K_m). Thus continuity follows from the corresponding arc parameterization.

On histories the shift

\[
G(z_0,z_1,\ldots)=(F(z_0),z_0,z_1,\ldots)
\]

is a homeomorphism of H(R^n), with inverse deleting the first coordinate, and H U=G H. Each G(K_m) is an arc contained in some K_M, since U(B_m) is compact. It preserves or reverses the order on that arc. Consistency on nested arcs shows that g=θGθ^{-1} is globally increasing or decreasing. It is onto J, so it is a homeomorphism of the interval. The factor identities and equality-of-histories characterization follow directly. ∎

### BM20-J2. Mutual long returns cannot separate scalar closed codes

Under BM20-J1, suppose x_j→x and U^{2m_j}x_j→y, while y_j→y and U^{2n_j}y_j→x, where m_j,n_j are nonnegative integers. Then R(x)=R(y); in fact q(x)=q(y).

**Proof.** The map f=g² is increasing. If q(x)<q(y), choose z strictly between them. If f(z)≥z, the upper interval {v:v≥z} is forward invariant; the sequence starting near q(y) cannot have endpoints converging below z. If f(z)≤z, the lower interval {v:v≤z} is forward invariant; the sequence starting near q(x) cannot end above z. One of these two cases always holds, giving a contradiction. Reverse the roles if q(y)<q(x). ∎

Using even iterates is essential here because g can reverse order. The proof allows F to be noninjective; that is exactly the case not covered by a direct interval-homeomorphism argument.

### BM20-J3. Exact continuous n=3, d=1 Jordan trajectory optimum

Let

\[
\dot x_1=\varepsilon x_2,\quad
\dot x_2=\varepsilon x_3,\quad
\dot x_3=0,\quad \varepsilon\ne0.
\]

Require a globally continuous scalar encoder R with exact sampled autonomy RΦ_h=F R on all R³, for one h>0. Measure worst-case error over the initial Euclidean unit ball, and allow any decoder of the complete output trajectory x_1(t), 0≤t≤T.

Every such R satisfies

\[
\boxed{R(a,b,0)=R(a',-b,0)\quad\text{for all real }a,a',b.}
\]

**Proof of the boundary identity.** Put τ_m=2mεh and

\[
c_m=\frac{2(a'-a-\tau_m b)}{\tau_m^2},\qquad
x_m=(a,b,c_m).
\]

Then x_m→(a,b,0), while the exact flow identity gives

\[
\Phi_h^{2m}x_m
=\left(a',-b+\frac{2(a'-a)}{\tau_m},c_m\right)
\longrightarrow(a',-b,0).
\]

Repeating the same construction with the endpoints exchanged supplies the reverse return. BM20-J2 proves the claim. Negative ε causes no problem: τ_m tends to negative infinity, while the number of forward sampled updates remains 2m. ∎

In particular the two unit-ball states (a,b,0) and (−a,−b,0) always have the same code. Their trajectories are opposite, so the triangle inequality for any common decoded trajectory gives error at least ||a+εtb||. Maximizing over a²+b²≤1 and using R(x)=x_3 with decoder ε²t²R/2 for the upper bound proves, for every 1≤p≤∞,

\[
\boxed{E^{\mathrm{closed,cont}}_{p,T}(3,1)
=\sup_{a^2+b^2\le1}\|a+\varepsilon tb\|_{L^p(0,T)}.}
\]

For p=2, set s=εT. The exact value is

\[
\boxed{E^2=\frac T2\left[1+\frac{s^2}{3}
+\sqrt{\left(1-\frac{s^2}{3}\right)^2+s^2}\right].}
\]

For p=∞ it is √(1+s²), since sup over unit (a,b) and sup over t commute and ||(1,εt)|| is largest at t=T. The p=2 value at ε=T=1 is √((4+√13)/6), approximately 1.1258738292.

This removes the polynomial and first-integral restrictions from BM18-J2. It resolves the first interior case of the original continuous contract. It does not classify all n,d.

## 2. A nonlinear code that strictly improves on every closed linear code

### BM20-J4. The closed linear trajectory formula is not universal

Consider the four-state chain with ε=T=1. Write x=(a,b,c,d), and let

\[
I(x)=c^3-3bcd+3ad^2,\qquad R_\eta(x)=d+\eta I(x).
\]

The polynomial I is a first integral: differentiating with a'=b, b'=c, c'=d, d'=0 gives 3c²d−3(c²d+bd²)+3bd²=0. Hence R_η is a globally continuous, exactly autonomous scalar code, with F=id. Use the trajectory decoder D(z)(t)=t³z/6.

For every sufficiently small η>0 this code has strictly smaller worst-case L²[0,1] error on the unit ball than every closed linear scalar code. An explicit certified choice is η=1/300000.

**Proof with an explicit margin.** Define A(a,b,c)=a+tb+t²c/2 and v(t)=t³/6. The residual is Ax_{1:3}−ηI(x)v. Put

\[
M=A^*A=\begin{pmatrix}1&1/2&1/6\\1/2&1/3&1/8\\1/6&1/8&1/20\end{pmatrix},
\quad k=A^*v=(1/24,1/30,1/72),\quad\|v\|^2=1/252.
\]

Let λ be the largest eigenvalue of M, and w its positive unit eigenvector, extended by zero in the fourth coordinate. The matrix has strictly positive entries, so λ is simple and w is strictly positive. The best closed linear scalar squared error is λ.

For the following elementary rational estimates, write w=(w_1,w_2,w_3,0). Componentwise row comparison gives w_1≥w_2≥w_3. The vector (1,1/2,0) gives λ≥19/15, while tr M=83/60. Thus the gap to the next eigenvalue of diag(M,0) is at least 2(19/15)−83/60=23/20>1. The eigenvector equations give

\[
\frac{w_2}{w_1}\le\frac{60}{97},\qquad
\frac{w_3}{w_1}\le\frac{1/6+(60/97)/8}{19/15-1/20}<\frac{21}{100}.
\]

The sum of the squares of these ratio bounds, plus one, is less than 36/25. Therefore w_1>5/6, and w_3≥w_1/(6λ)>25/249>1/10. Consequently

\[
B(w):=I(w)\,k\cdot w_{1:3}=w_3^3 k\cdot w_{1:3}>1/28800=:b_0.
\]

On the unit ball, |I|≤7, ||∇I||≤√135<12, and ||k||<1/16. Hence B(x)=I(x)k·x_{1:3} has Lipschitz constant less than 2, and C(x)=I(x)²/252<1/5. Both B and the squared residual are even, so replace x by −x if necessary to arrange α=x·w≥0. With z=x−αw and r=||x−w||, the gap estimate gives

\[
\lambda-\|Ax_{1:3}\|^2
\ge 1-\alpha^2\ge r^2/2.
\]

The first inequality follows more explicitly from λ(1−||x||²)+(λ−λ_2)||z||²≥(1−||x||²)+||z||²=1−α². The second follows from ||x||≤1 and 0≤α≤1.

Therefore

\[
\begin{aligned}
\|Ax_{1:3}-\eta I(x)v\|^2
&\le\lambda-r^2/2-2\eta(b_0-2r)+\eta^2/5\\
&\le\lambda-2b_0\eta+9\eta^2.
\end{aligned}
\]

The last line maximizes −r²/2+4ηr, whose maximum is 8η². At η=1/300000,

\[
2b_0\eta-9\eta^2>10^{-10}.
\]

Thus the new squared worst-case error is at most λ−10^{-10}, strictly below the optimum λ of the entire closed linear scalar class. Every step is an exact inequality; a floating-point optimization is not being used as a certificate. ∎

The margin is deliberately conservative. This result refutes an unrestricted extension of the linear optimum formula. It does not compute the exact nonlinear n=4,d=1 optimum.

## 3. Exact finite causal synthesis without an output catalogue

### BM20-C1. Invariant-cover criterion for finite causal prediction

Let X be any state set, with a finite alphabet of deterministic partial actions f_a, task τ:X→Y into a metric space, and a nonempty initial set I⊆X. A deterministic predictor has finitely many states q, a fixed output y_q at each state, deterministic partial updates g_a, and an initialization map I→Q. The predictor receives the action sequence, with no further observation of the native state. Require matching action availability and error at most ε at every time on every legal history.

Such a predictor with at most m states exists if and only if there are at most m nonempty sets C_q⊆X, outputs y_q, and successor choices g_a(q) satisfying:

1. I⊆∪_q C_q.
2. Every x∈C_q has the same enabled-action set as q.
3. For each enabled action, f_a(C_q)⊆C_{g_a(q)}.
4. d(τ(x),y_q)≤ε for every x∈C_q.

If an exact legacy label must also be retained, require it to be constant on each C_q. These sets may overlap: the same native state can accompany different predictor states after different histories.

**Proof.** A cover gives an initialization by selecting a containing cell. Induction on history length preserves membership, matching availability, and the output bound. Conversely, from a successful predictor take C_q to be the set of native states actually paired with q over all initializations and finite legal histories. Remove empty cells. Availability, successor containment and the output bound hold by construction. ∎

For a predictor that must be a function of the current native state alone and close exactly, the criterion is the same with the C_q forming a partition of the reachable carrier. This extra restriction is substantive; overlapping covers and partitions can have different optima.

The criterion is a specialization of established simulation-relation methodology, not a claim to have invented approximate simulation; compare [Tabuada2008]. For an infinite X it is an exact semantic criterion, not a general finite algorithm.

### BM20-C2. Exact rational minimum-ball certificates

For a nonempty finite set P⊆Q^p, a smallest Euclidean enclosing ball has rational center c and rational squared radius ρ². There is an affinely independent support {z_0,…,z_k}⊆P, k≤p, and nonnegative rational weights w_i summing to one such that

\[
c=\sum_i w_i z_i,\qquad \|z_i-c\|^2=\rho^2,
\qquad \|z-c\|^2\le\rho^2\ (z\in P).
\]

These equalities and inequalities certify optimality exactly.

**Proof.** The maximum distance is continuous and coercive, so a minimizing center exists. That center lies in the convex hull of the points attaining the maximum: otherwise strict separation gives a direction that decreases all active distances, and a sufficiently small step also preserves the slack of the other finitely many points. Reduce a convex combination to an affinely independent one by removing an affine dependence while keeping weights nonnegative.

Put u_i=z_i−z_0 and c=z_0+Σ_{i=1}^k α_i u_i. Equal squared distances give the nonsingular rational Gram system

\[
\sum_j (u_i\cdot u_j)\alpha_j=\|u_i\|^2/2.
\]

Its solution and c are rational, with w_0=1−Σα_i and w_i=α_i. Conversely, for any proposed center v the displayed support certificate gives

\[
\sum_i w_i\|z_i-v\|^2=\rho^2+\|c-v\|^2\ge\rho^2.
\]

Some support point is therefore at least distance ρ from v. Together with containment, this proves optimality. Enumerating supports of size at most p+1 finds such a certificate. ∎

This is standard minimum-enclosing-ball geometry, with the proof included to make the exact implementation auditable; see also [Welzl1991]. Squared radii are rational; the radii themselves need not be.

### BM20-C3. Globally optimal finite synthesis, all real outputs and all horizons

For a finite deterministic partial-action system with rational Euclidean task coordinates, the following algorithm computes the exact optimum for every predictor-state budget up to a supplied m:

1. Restrict to the native states reachable from I.
2. Enumerate every nonempty subset with uniform action availability and, if specified, uniform legacy label. Compute its minimum-ball certificate by BM20-C2.
3. Enumerate families of at most m distinct such subsets. Check initial coverage and successor containment from BM20-C1.
4. Minimize the largest squared cell radius. Return a realizing transition table, initialization, outputs, and the cell certificates.

Use disjoint full covers in step 3 for the exactly closed current-state encoder variant.

**Proof.** Each accepted cover supplies a valid infinite-horizon predictor. Conversely, the reachable-pair cells of any predictor are among the enumerated subsets. Replacing its outputs with their minimum-ball centers cannot increase the error. Duplicate cells can be removed: retain one copy, and choose any successor cell containing each required image. Thus distinct-subset families suffice. Enumeration attains the global optimum, including optimization over all real output vectors, by BM20-C2. The singleton native-state model gives zero error with at most |Reach(I)| states. ∎

If n states are reachable, there are at most 2^n−1 candidate cells and at most Σ_{j≤m} binom(2^n−1,j) distinct families. This is an exact exponential reference algorithm, not an efficient general implementation. It closes the finite deterministic, Euclidean-output contract; it does not establish finite realizability for every infinite carrier or satisfy unspecified physical and continuity constraints.

**Concrete distinction between history and current-state encoding.** Take states 0,1,2,3, one update (3,1,1,2), and scalar task values (2,2,3,0). With two predictor states, the overlapping cells {0,1,2} and {1,3}, outputs 5/2 and 1, and alternating updates have worst-case error 1. The exact optimum among closed current-state encoders using at most two states is 3/2. The supplied exact solver checks both optima. The shared state 1 can legitimately occur in either predictor cell as the predictor alternates; its task value 2 stays within both error bounds.

These optima also have short direct lower bounds. If ε<1, no cell containing state 3 can contain any of states 0,1,2. Two cells would therefore have to separate {3} from {0,1,2}, but the latter's update image contains both 3 and 1, which cannot fit in either cell. Thus history-based error is at least 1. For a closed two-state quotient, the image of native state 1 is fixed. In a two-state map every state that eventually reaches that fixed state does so in at most one step. Consequently native states 1,2,3 must share its code. Their task values range from 0 to 3, giving error at least 3/2, attained by the constant output 3/2.

## 4. Sharp finite-dimensional recovery results beyond qubits

Use the original unamplified operator-norm recovery error δ_A and normalized error-space defect κ_A from BM18-Q1. No diamond-norm lower bound is substituted for δ_A.

### BM20-Q1. Sharp universal error ceiling for every finite observable algebra

Write a unital finite-dimensional observable algebra, up to unitary equivalence, as

\[
A=\bigoplus_{j=1}^s (M_{n_j}\otimes I_{m_j}),
\qquad r=\sum_j n_j.
\]

Then every channel admits a recovery with

\[
\boxed{\delta_A\le 2(1-1/r).}
\]

The ceiling is attained by a completely erasing channel. For r=1 it is zero. Multiplicity factors m_j do not count as additional independent observables.

**Proof.** On M_r let P(X)=X−tr(X)I/r. For r≥2 its induced operator norm is 2(1−1/r), including non-Hermitian inputs. To see this, dualize a matrix coefficient:

\[
\|P\|=\sup_{\|u\|=\|v\|=1}
\|vu^*-(u^*v)I/r\|_1.
\]

After removing a scalar phase, let c=|u^*v|∈[0,1]. In the span of u and v, the two singular values of the rank-one-minus-scalar matrix have sum one: the sum of their squares is 1−2c²/r+2c²/r², and twice the absolute determinant is 2c²(r−1)/r². The other r−2 singular values are c/r. The trace norm is therefore 1+(r−2)c/r≤2−2/r. The coincident-vector and orthogonal-vector cases follow by the same formula or by continuity. The Hermitian contraction I−2|u⟩⟨u| attains the upper bound.

Represent the abstract direct sum ⊕M_{n_j} faithfully on C^r; this preserves its operator norm. A constant recovery output can implement its normalized trace functional tr_r/r, for example with physical state ⊕_j I_{n_jm_j}/(r m_j). Its error is the restriction of P, proving the ceiling.

For an erasing channel every recovery is a constant state σ. Choose r mutually orthogonal minimal projections of the abstract algebra that sum to I. At least one, e, has tr(σe)≤1/r. On X=I−2e the reconstruction error has norm at least 2(1−tr(σe))≥2−2/r. The ceiling is therefore exact. ∎

Together with BM18-Q1 this improves the stated general bound to

\[
\delta_A\le\min\{2(1-1/r),\ 2\sqrt{\min(d,k^2)\kappa_A}\},
\]

where d is the logical dimension and k is the number of Kraus operators in the chosen representation. The symbol r in this section is the abstract algebra rank, not Kraus rank.

### BM20-Q2. Complete normalized-defect envelope for the full matrix algebra

For A=M_d, d≥2, the possible pairs are exactly

\[
(\kappa,\delta)=(0,0),\qquad
\kappa=2,\quad 0<\delta\le 2(1-1/d).
\]

**Proof.** BM18-Q2 gives κ∈{0,2}. Exact recovery is equivalent to κ=0, and the recovery minimum is attained because finite-dimensional CPTP maps form a compact set and the objective is continuous. Thus κ=2 implies δ>0. BM20-Q1 supplies the upper endpoint.

Every positive value up to that endpoint is realized by a depolarizing channel

\[
N_\lambda(\rho)=\lambda\rho+(1-\lambda)I\operatorname{tr}(\rho)/d,
\qquad0\le\lambda<1,
\]

for which

\[
\delta=(1-\lambda)\,2(1-1/d),\qquad\kappa=2.
\]

To prove optimality, twirl a candidate recovery under all unitary conjugations. Convexity and unitary invariance of the objective, and covariance of N_λ, show that twirling cannot increase the error. The resulting channel is depolarizing with multiplier α∈[−1/(d²−1),1]; this follows either from the invariant scalar/traceless decomposition or directly from its Choi matrix, whose eigenvalues are (1+(d²−1)α)/d and (1−α)/d. The error is (1−λα)||P||, minimized at α=1. For λ<1 a Weyl Kraus representation has all its coefficients nonzero and error space M_d, giving κ=2. ∎

This settles the full-algebra normalized-defect question in every finite dimension. Intermediate-defect envelopes for arbitrary proper algebras are still a separate problem.

### BM20-Q3. Exact primal and dual recovery for any binary observable algebra

Let A=C*(S), where S=S* and S²=I, with both eigenspaces nonzero. The logical and channel-output dimensions may be arbitrary finite values. Then

\[
\boxed{\delta_A=\min_{B=B^*,\ -I\preceq B\preceq I}
\|S-N^\dagger(B)\|}
\]

and equivalently

\[
\boxed{\delta_A=\max_{H=H^*,\ \|H\|_1\le1}
\left(\operatorname{tr}(SH)-\|N(H)\|_1\right).}
\]

**Proof.** A recovery adjoint sends S to a Hermitian contraction B. Conversely any B is realized by measuring (I±B)/2 and preparing a fixed state in the corresponding ± eigenspace of S. For X=cI+eS, |e|≤||X||, and the recovery error is e(S−N†B). Thus the first formula is exact on the entire complex operator unit ball of A.

The operator norm on Hermitian matrices is dual to the trace norm on Hermitian matrices. The minimum over B and maximum over H can be interchanged by the finite-dimensional compact convex minimax theorem. Maximizing tr(N(H)B) over Hermitian contractions B gives ||N(H)||_1, proving the dual formula. Both extrema are attained. ∎

The primal is a semidefinite program with constraints −I≼B≼I and −tI≼S−N†B≼tI. A feasible B gives an upper bound, and any dual-feasible H gives the displayed lower bound. Matching values certify optimality. This is a theorem and explicit optimization formulation; the new Python implementation concerns causal covers, not a general SDP engine. Standard channel/Choi and norm conventions are documented in [Watrous2018].

## 5. Effective repair under an explicit algebraic contract

### BM20-N1. A computable repair modulus on compact semialgebraic parameter sets

Let Θ be a nonempty compact semialgebraic coefficient set over the real algebraic numbers. Let g:Θ→[0,∞) be continuous and semialgebraic, with nonempty exact feasible set Z={θ:g(θ)=0}. For every positive rational η there is an algorithm returning a positive rational δ such that

\[
g(\theta)\le\delta\quad\Longrightarrow\quad
\operatorname{dist}(\theta,Z)<\eta.
\]

For algebraic input θ meeting this residual bound, a feasible algebraic θ* with ||θ−θ*||<η can also be produced.

**Proof.** For k=0,1,2,… use real quantifier elimination to decide

\[
\exists\theta\in\Theta:\quad g(\theta)\le2^{-k}
\quad\text{and}\quad
\forall\phi\in Z,\ \|\theta-\phi\|^2\ge\eta^2.
\]

Stop at the first false sentence and return δ=2^{-k}. The compact set {θ:dist(θ,Z)≥η}, if nonempty, has strictly positive minimum g. Thus the procedure terminates. If it is empty, it terminates immediately. The negated sentence supplies the claimed distance bound. For algebraic θ, sample the nonempty semialgebraic set {φ∈Z:||θ−φ||²<η²}; it has an algebraic sample point. ∎

In bounded-degree polynomial BM repair, Θ must explicitly bound coefficients, or otherwise be proved compact after removing redundant parameters. The residual g can include closure, legacy and range violations, provided it is continuous and semialgebraic on that fixed contract. Maxima of continuous semialgebraic residuals over compact semialgebraic carriers can be represented by first-order formulas, so the hypothesis is checkable in that setting. The conclusion concerns coefficient distance; a bound on the monomial evaluation vector converts it to a uniform function-distance bound.

This supplies an effective modulus absent from BM18-N2's bare compactness argument. It uses the same classical real-algebraic decision ingredient as BM18-N3. No quantifier-elimination engine is implemented in the accompanying Python file, and no polynomial-time complexity or unrestricted smooth repair modulus is claimed.

## 6. An impossibility boundary for general smooth minimum-dimension algorithms

### BM20-G1. Exact minimum augmentation is not uniformly decidable for computable smooth data

There is no algorithm that always terminates and determines the least continuous exact representation dimension for every computably specified smooth task, even with source [0,1], identity dynamics, constant legacy, and a task of the form τ(x)=a x with 0≤a≤1.

Here a computable specification supplies a program that approximates a to any requested rational error; it is more general than a finite algebraic-number input.

**Proof.** Given a program e and input, define a_e=2^{-t} if it first halts at step t≥1, and a_e=0 if it never halts. This is uniformly computable: simulate N steps; return the exact value if halting was observed and otherwise return zero, whose error is at most 2^{-N}.

If a_e=0, the zero-dimensional constant code represents the task exactly. If a_e>0, a constant code cannot represent the nonconstant task, while the one-dimensional code R(x)=x with identity update and decoder a_e x does. Therefore the minimum dimension is zero precisely in the nonhalting case. A terminating minimum-dimension algorithm would decide halting, which is impossible by the diagonal argument in BM18-I1. ∎

All tasks in the construction are smooth, uniformly bounded and uniformly Lipschitz. Those qualitative bounds do not remove the exact-zero decision problem. This is not a claim that a specified algebraic or geometrically restricted instance is undecidable; BM18-N3 and BM20-N1 deliberately use stricter effective inputs.

## 7. A constructive infinite-dimensional native class

### BM20-I1. Finite causal prediction of diagonal contractions with a compact task

Let X be the unit ball of the real Hilbert space ℓ². There are finitely many total actions

\[
(f_a x)_i=\lambda_{a,i}x_i,\qquad |\lambda_{a,i}|\le L<1.
\]

Let τ(x)=(b_i x_i)_i, with |b_i|≤C. Assume the diagonal coefficient sequences are effectively given rationals, L,C are supplied rational bounds, and a computable rational tail bound β_N≥sup_{i>N}|b_i| tends to zero. Then for every rational ε>0 a finite deterministic predictor with uniform ℓ² task error at most ε on every infinite action history can be constructed.

**Construction and proof.** The case C=0 needs one zero-output state. Otherwise choose N≥1 with β_N≤ε/2. Put a grid of spacing 1/K in each of the first N coordinates of [−1,1]^N, giving at most (2K+1)^N predictor states. Initialize by a grid approximation and update by coordinatewise multiplication with the selected λ_{a,i}, followed by nearest-grid rounding. Output the first N coordinates b_i q_i and zeros thereafter.

Choose K large enough that η=√N/K≤ε(1−L)/(2C); using √N≤N gives an entirely rational sufficient choice. Initialization can be implemented from approximations to the first N native coordinates with coordinate error at most 1/(4K), followed by clipping and rounding. Its Euclidean error is less than η, including rounding ties. Each subsequent rational grid update introduces at most η/2 and hence at most η error. Thus

\[
e_t\le L^t\eta+\eta\sum_{j=0}^{t-1}L^j\le\frac{\eta}{1-L}.
\]

The omitted task tail has norm at most β_N L^t≤β_N. Orthogonality of the retained and omitted coordinates gives

\[
\|\tau(x_t)-\widehat y_t\|_2
\le\sqrt{\beta_N^2+\left(\frac{C\eta}{1-L}\right)^2}
\le\varepsilon/\sqrt2<\varepsilon.
\]

Every grid and transition table is finite and computable from the stated data. ∎

This closes an effective infinite-dimensional native contract. It is a finite causal predictor with memory, not an assertion that the instantaneous rounding map commutes exactly with native dynamics. Arbitrary nonlinear PDEs, discontinuous availability boundaries, and infinite-dimensional quantum channels are outside this theorem.

## 8. Executed verification

The supplied verification program passed using exact rational arithmetic:

| Check | Executed scope |
| --- | --- |
| Minimum enclosing balls | 205 support certificates, including repeated points, affine degeneracy and dimensions 1–4 |
| Causal synthesis | 577 native/task cases; 2,166 history/closed-mode and memory-budget comparisons with an independent transition-table/initialization oracle |
| Independent causal oracle | 88,210 candidate transition/initialization combinations examined; scalar output centers computed independently as interval midpoints |
| Jordan bridge | 100 exact endpoint identity checks, with both signs of coupling |
| Nonlinear four-state witness | Exact zero Lie derivative and rational inequalities certifying squared-error improvement at least 71/540000000000, hence greater than 10^−10 |
| Quantum ceiling identity | 399 rational two-singular-value identities and ceiling inequalities for dimensions 2–20 |
| Infinite diagonal example | L=1/2, b_i=1/i, N=3, K=24 gives at most 117,649 grid states and squared-error bound 1/12, below (1/2)² |
| Input boundaries | Eight malformed or out-of-contract inputs rejected |

The mathematical arguments establish the general results. Finite checks corroborate identities and implementations; they do not prove the continuum-topology input, undecidability, or every infinite-dimensional instance. Independent review remains open.

## 9. Completion status after this continuation

| Original obligation | What is now completed | What remains in the original broader scope |
| --- | --- | --- |
| Continuous Jordan trajectory optimum | Exact n=3,d=1 value for every continuous scalar sampled factor; all L^p trajectory norms; explicit n=4 counterexample to universal linear optimality | Exact higher/intermediate n,d optima, including n=4,d=1 |
| Correlated finite architectures | BM18-C1–C2 already supplied the criterion and finite synthesis | External application benchmarks and new native categories |
| Fragmentation | BM18-F1–F3 already supplied exact frontier computation and complexity results | Competitive implementations and external benchmarks |
| Causal approximation | Exact arbitrary-output finite synthesis with partial availability, optional exact legacy, all infinite histories, and both memory/current-state variants | General infinite-carrier optimum and additional specified physical/regularity constraints |
| Quantum recovery | Sharp full-algebra normalized-defect envelope in every finite dimension; sharp algebra-dependent universal ceiling; exact binary-algebra primal/dual | Sharp intermediate-defect envelopes for general proper algebras and broader capability geometry |
| Nonlinear repair | Effective modulus and algebraic repair selection for compact semialgebraic coefficient contracts | Uniform guarantees beyond those contracts; unrestricted residual repair is already false |
| Global minimum realization | Exact universal smooth-input algorithm is ruled out even for a linear task with a computable coefficient | Geometry and least augmentation of individual specified native classes |
| Infinite presentations | Universal exact algorithm is ruled out; finite prediction now constructed for a diagonal contraction/compact-task class | Other specified PDE and infinite-dimensional channel classes |

The six broad extension rows remain open at their original breadth. The new proofs remove particular gaps and refute two tempting universal shortcuts; they do not erase the remaining questions. External physical validation, competitive usefulness, independent mathematical review and historical novelty are separate requirements. None is marked completed by this note.

## References

- [Nadler1999] S. B. Nadler, Jr., *Arc-like and circle-like almost continuous images of Peano continua*, Topology Proceedings 24 (1999), 249–259. Definitions of arc-like continua and the path/Peano characterization are in §1. https://topology.nipissingu.ca/tp/reprints/v24/tp24118.pdf
- [Bankston2019] P. Bankston, *On continuous images of ultra-arcs*, Topology and its Applications 261 (2019); author manuscript, §6, p. 9. It records the classical metric theorem that a locally connected chainable continuum is an arc and points to S. B. Nadler, *Continuum Theory: An Introduction* (1992), Chapter XII. https://www.mscsnet.mu.edu/~paul/Paper/ta_ultarcs113018.pdf
- [Tabuada2008] P. Tabuada, *An approximate simulation approach to symbolic control*, IEEE Transactions on Automatic Control 53(6) (2008), 1406–1418; author draft. https://www.seas.ucla.edu/~tabuada/Papers/ApproxSymbolicControl.pdf
- [Welzl1991] E. Welzl, *Smallest enclosing disks (balls and ellipsoids)*, LNCS 555 (1991), 359–370. https://doi.org/10.1007/BFb0038202
- [Watrous2018] J. Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), author draft. General conventions for operator norms, CPTP maps, Choi matrices, and convex optimization. https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf


# 21 October continuation: Jordan returns and certified nonlinear bounds

21 October 2026 · Continuation of the 20 October development

This development completes the long-return calculation for Jordan chains of every length and supplies exact upper and lower certificates for a concrete four-state nonlinear construction. It does **not** assert that the remaining continuous four-state minimax problem is solved. The distinction between a global bound and a bound for one encoder/decoder family is maintained throughout.

The proofs are internally checked mathematical arguments. The finite numerical certificates are verified with exact rational arithmetic. Independent proof review and historical novelty assessment remain separate obligations.

The earlier frozen BM foundation is unchanged. The two imported BM results are BM20-J1–J2 (ordered refinement and mutual-return obstruction) and, for the optional extension from invariant polynomials to all sampled-autonomous polynomials, BM18-J1. Their full proofs are included in the accompanying package.

## Contract and notation

For a positive integer n, let N be the Jordan nilpotent matrix with ones immediately above the diagonal. Thus

\[
 (e^{\tau N}x)_{k+1}
 =\sum_{j=k}^{n-1}\frac{\tau^{j-k}}{(j-k)!}x_{j+1},
 \qquad 0\le k<n.
\]

The dynamics are \(\dot x=\varepsilon Nx\), with \(\varepsilon\ne0\). Exact scalar closure means that a **globally continuous** map \(R:\mathbb R^n\to\mathbb R\) satisfies

\[
 R(e^{\varepsilon hN}x)=F(R(x))\quad(x\in\mathbb R^n)
\]

for a fixed \(h>0\) and a single-valued F on the image of R. F is not initially assumed invertible. The performance set is the Euclidean unit ball of initial states; closure is required on all of \(\mathbb R^n\). The performance set is not asserted to be invariant.

Let \(V_k=\{x:x_{k+1}=\cdots=x_n=0\}\), with \(V_0=\{0\}\). The output trajectory operator on its first k coordinates is

\[
 (\mathcal O_{k,T}z)(t)=\sum_{j=0}^{k-1}
 \frac{(\varepsilon t)^j}{j!}z_{j+1},\qquad 0\le t\le T.
\]

A decoder may return any trajectory in the chosen \(L^p[0,T]\) space unless an explicit restricted decoder is named.

## 1. All long-return endpoint pairs

### BM21-J1. Complete long-return relation for every Jordan chain

Fix any sequence \(\tau_j\) with \(|\tau_j|\to\infty\). A pair (x,y) can occur as

\[
 z_j\longrightarrow x,\qquad e^{\tau_jN}z_j\longrightarrow y
\]

if and only if it has the following form:

| Chain length | Exactly the possible endpoint pairs |
|---|---|
| \(n=2m\) | \(x,y\in V_m\), with their first m coordinates arbitrary and independent. |
| \(n=2m+1\) | \(x=(a,c,0_m)\), \(y=(b,(-1)^m c,0_m)\), where \(a,b\in\mathbb R^m\) and \(c\in\mathbb R\). |

Here \(0_m\) denotes m trailing zeros. The statement holds for either time direction and for every prescribed diverging sequence, including \(\tau_j=2j\varepsilon h\). For n=1 it says x=y, as it should for the identity dynamics.

**Proof.** Associate to a state z the polynomial

\[
 p(s)=\sum_{k=0}^{n-1}z_{k+1}s^k/k!.
\]

Its derivatives at 0 are the state z; its derivatives at \(\tau\) are the state \(e^{\tau N}z\).

First let n=2m. The derivatives of orders 0 through m−1 at 0 and at \(\tau\ne0\) uniquely determine a polynomial of degree at most 2m−1. Indeed, the difference of two such polynomials is divisible by \(s^m(s-\tau)^m\), which has degree 2m. This proves uniqueness; the square linear interpolation system then also has a solution.

Let \(h_{0k},h_{1k}\), \(0\le k<m\), be the corresponding Hermite basis on the fixed interval with endpoints 0 and 1: the kth specified derivative at the named endpoint is one and all other specified derivatives are zero. If the endpoint derivative data are \(u_k,v_k\), the interpolant obeys

\[
 H_\tau(\tau s)=\sum_{k=0}^{m-1}\tau^k
 \bigl(u_k h_{0k}(s)+v_k h_{1k}(s)\bigr).
\]

For bounded data, every endpoint derivative of order r≥m is therefore

\[
 O(|\tau|^{m-1-r})\longrightarrow0.
\]

This proves necessity: any converging states and their converging endpoints have bounded lower derivative data and hence vanishing upper halves. Conversely, choose fixed lower data equal to the desired x and y coordinates and use this interpolant at each \(\tau_j\). Its full derivative vectors converge to the specified endpoints. This proves the even case.

Now let n=2m+1 with m≥1. Construct the same degree-\((2m-1)\) interpolant H for the lower m derivatives at each endpoint. The additional degree of freedom is a multiple of

\[
 q(s)=s^m(s-1)^m,
 \qquad q^{(m)}(0)=(-1)^m m!,\quad q^{(m)}(1)=m!.
\]

If the initial mth derivative is \(u_m\), the unique degree-at-most-2m polynomial is

\[
 p_\tau(t)=H_\tau(t)+
 \frac{u_m-H_\tau^{(m)}(0)}{(-1)^m m!}
 \tau^m q(t/\tau).
\]

Its mth derivative at the other endpoint is

\[
 p_\tau^{(m)}(\tau)
 =H_\tau^{(m)}(\tau)+(-1)^m
 \bigl(u_m-H_\tau^{(m)}(0)\bigr).
\]

Both H derivatives are \(O(1/|\tau|)\). The endpoint mth derivatives consequently tend to c and \((-1)^m c\). All derivatives above order m tend to zero: those of H do, and those of the added term have size \(O(|\tau|^{m-r})\) for r>m. This proves necessity for bounded converging endpoint data, and sufficiency by choosing fixed lower data and \(u_m=c\). The case n=1 follows directly. ∎

This theorem classifies endpoint limits of the **native linear flow**. It does not assert that these pairs exhaust the fibers of every scalar factor.

## 2. What every continuous scalar code must forget

### BM21-J2. Forced scalar identifications and trajectory lower bounds

Under the stated global continuous closure contract:

* For n=2m, R is constant on \(V_m\).
* For n=2m+1, there is a continuous scalar function \(\phi\) such that
  \(R(a,c,0_m)=\phi(c)\). If m is odd, \(\phi(c)=\phi(-c)\).

Consequently define

\[
 k(n)=\left\lfloor\frac n2\right\rfloor
 +\begin{cases}1,&n\equiv3\pmod4,\\0,&\text{otherwise}.\end{cases}
\]

For every \(z\in V_{k(n)}\), \(R(z)=R(-z)\). For any trajectory decoder, any T>0 and any \(1\le p\le\infty\),

\[
 \boxed{E^{\mathrm{closed,cont}}_{p,T}(n,1)
 \ \ge\ \|\mathcal O_{k(n),T}\|_{\ell_2\to L^p}.}
\]

For k=0 the right side is zero. This is a lower bound, not a general equality assertion.

**Proof.** BM20-J1 supplies a continuous refinement q of R and an interval homeomorphism g with \(qU=gq\), where \(U=e^{\varepsilon hN}\); it permits F itself to be noninjective. Its mutual-return consequence BM20-J2 is elementary once that refinement exists: \(g^2\) is increasing. If two limiting q-values lie on opposite sides of a point u, then either \(g^2(u)\ge u\), making the upper half-interval forward invariant, or \(g^2(u)\le u\), making the lower half-interval forward invariant. Thus even forward iterates cannot approach each endpoint from the other.

The relation in BM21-J1 is symmetric. Apply its construction to \(\tau_j=2j\varepsilon h\), first with the endpoints in one order and then reversed. The mutual-return result identifies their q-values and hence their R-values. In the odd case with sign −1, applying the relation twice also proves independence of the first m coordinates at fixed c. This gives the claimed restrictions.

The indicated \(V_{k(n)}\) consists of forced antipodal pairs. Their true trajectories are opposites. If a decoder returns the same w for such a pair, the triangle inequality gives

\[
 \max\{\|\mathcal O_{k,T}z-w\|_p,
          \|-\mathcal O_{k,T}z-w\|_p\}
 \ge\|\mathcal O_{k,T}z\|_p.
\]

Take the supremum over unit z and then the infimum over codes and decoders. ∎

For p=2 the bound is the square root of the largest eigenvalue of the k×k matrix

\[
 G_{ij}=\frac{\varepsilon^{i+j}T^{i+j+1}}{i!j!(i+j+1)},
 \qquad 0\le i,j<k.
\]

For p=∞ the bound is

\[
 \left(\sum_{j=0}^{k-1}\frac{(\varepsilon T)^{2j}}{(j!)^2}\right)^{1/2}.
\]

The latter follows by commuting the two suprema and observing that the squared coefficient-vector norm increases with t≥0. The first chain lengths have \(k(n)=0,1,2,2,2,3,4,4\) for n=1,…,8. The parity distinction is part of the result; a stronger antipodal claim on every odd chain's full middle prefix has not been proved here.

For block-diagonal collections of Jordan chains the endpoint relation is the product of the block relations, using the same iterate counts. The same proof gives a scalar-code lower bound on the direct sum of their forced antipodal subspaces for any linear trajectory task. Different nonzero block couplings change the interpolation times but not the endpoint classification.

In particular, for n=4 and \(\varepsilon=T=1\),

\[
 \boxed{E^2\ge(4+\sqrt{13})/6
 \approx1.267591879244.}
\]

## 3. A substantially stronger certified four-state construction

### BM21-J3. A rational cubic encoder with squared error at most 1.2949

Write the four-state unit chain as

\[
 \dot a=b,\quad\dot b=c,\quad\dot c=d,\quad\dot d=0.
\]

Set

\[
 Q=c^2-2bd,\qquad I=c^3-3bcd+3ad^2,
\]

and choose the scalar encoder

\[
 \boxed{R(x)=\frac{1969d+8757I-7014dQ+159d^3}{10000}.}
\]

Decode it as the entire trajectory

\[
 \boxed{D(z)(t)=(1+t/2)z,\qquad 0\le t\le1.}
\]

Then R is a global polynomial first integral, so its exactly closed update is F=id for every sampling interval. For every initial state of Euclidean norm at most one,

\[
 \boxed{\int_0^1
 \left|a+bt+\frac{ct^2}{2}+\frac{dt^3}{6}-(1+t/2)R(x)\right|^2dt
 \le\frac{12949}{10000}=1.2949.}
\]

**Proof by an exact rational certificate.** Direct differentiation gives \(DQ=DI=Dd=0\), where \(D=b\partial_a+c\partial_b+d\partial_c\). Hence DR=0.

To certify the bound on the whole ball, introduce a fifth real variable e, and write

\[
 \rho=a^2+b^2+c^2+d^2+e^2,
 \quad R_h=\frac{1969d\rho+8757I-7014dQ+159d^3}{10000}.
\]

Let \(x=(a,b,c,d)^T\), let

\[
 G_{ij}=\frac{1}{i!j!(i+j+1)}\quad(0\le i,j\le3),
 \qquad k=(5/4,2/3,11/48,7/120)^T.
\]

Integration gives \(\|Ox\|_2^2=x^TGx\), \(\langle Ox,1+t/2\rangle=k^Tx\), and \(\|1+t/2\|_2^2=19/12\). The homogeneous degree-six polynomial

\[
 P=\frac{12949}{10000}\rho^3-\rho^2 x^TGx
       +2\rho R_h k^Tx-\frac{19}{12}R_h^2
\]

has the exact identity

\[
 P=m(a,b,c,d,e)^T H\,m(a,b,c,d,e),
\]

where m is the vector of all 35 degree-three monomials in five variables, in the order specified in the certificate. The supplied 35×35 rational matrix H has common denominator **630000000000**. The companion verifier checks all 210 degree-six coefficients exactly, computes an exact LDLᵀ factorization with 35 strictly positive pivots, and independently reconstructs H from that factorization. Thus H is positive definite and P≥0 everywhere.

For a state in the unit ball choose \(e=\sqrt{1-\|x\|^2}\). Then \(\rho=1\), \(R_h=R\), and P is precisely the asserted error bound minus the squared error. This proves the claim. No sampled numerical maximum or floating-point eigenvalue is used to accept the certificate. ∎

The exact matrix is in `BM_Jordan_Rational_Certificate_2026-10-21.json`. The standalone verifier uses only the Python standard library.

**Strict comparison with every closed linear scalar code.** A nonzero linear scalar factor must retain d alone: closure makes its kernel invariant, so its defining row is a left eigenvector of the unipotent Jordan update, hence a multiple of the last-coordinate row. At d=0, indistinguishable antipodal states give the squared lower bound \(\lambda_{\max}(G_{0:3,0:3})\), attained by decoding d as \(t^3d/6\). Thus the best such linear code has squared error approximately 1.301498187997. A rational Rayleigh vector (87,47,16) already gives

\[
 \lambda_{\max}\ge\frac{195887}{150510}
 >\frac{12949}{10000}.
\]

The new construction therefore improves squared worst-case error by at least

\[
 \frac{991601}{150510000}\approx0.006588273204
\]

over the optimum of that entire linear class. The previously established linear formula is retained in its linear scope; it is not substituted for the unrestricted nonlinear optimum.

Together, BM21-J2–J3 now certify the global continuous four-state interval

\[
 \boxed{\sqrt{\frac{4+\sqrt{13}}6}
 \ \le E^{\mathrm{closed,cont}}_{2,1}(4,1)
 \ \le\frac{\sqrt{12949}}{100}.}
\]

Numerically this is **1.1258738292 ≤ E ≤ 1.1379367294**. The endpoints are bounds; the exact value inside this interval has not been established.

## 4. How much remains possible within this cubic family?

### BM21-J4. A certified 0.0001 bracket for cubic invariant codes with the fixed decoder

Keep the decoder \(D(z)(t)=(1+t/2)z\), but allow **every invariant scalar polynomial of total degree at most three**, with arbitrary real coefficients. Let \(E_{\le3,v}\) be the resulting best worst-case error on the same unit ball. Then

\[
 \boxed{1.2948\le E_{\le3,v}^2\le1.2949.}
\]

BM18-J1 also makes this the bracket for every globally sampled-autonomous scalar polynomial of that degree with this decoder: such a polynomial is necessarily a first integral. This conclusion does not extend the fixed decoder restriction to arbitrary decoders.

**Proof.** The task is odd in x, and the ball is symmetric. Given an invariant polynomial R, its odd part \(R_o(x)=(R(x)-R(-x))/2\) is also invariant and has no larger worst-case error. Its residual at x is the average of the residual of R at x and the negative residual of R at −x, so this follows from convexity of the norm.

The odd invariant polynomials of degree at most three are exactly

\[
 R_o=\alpha d+\beta I+\gamma dQ+\delta d^3.
\]

For completeness, the degree-one kernel of D is spanned by d. Comparing coefficients of a general homogeneous cubic in \(DP=0\) eliminates the monomials involving \(a^3,a^2b,a^2c,a^2d,ab^2,abc,abd,ac^2,acd,b^3,b^2c,b^2d,bc^2,cd^2\); the remaining coefficients satisfy

\[
 [ad^2]=3[c^3],\quad[bcd]=-3[c^3],\quad[bd^2]=-2[c^2d].
\]

Thus the cubic kernel has the three independent basis elements I, dQ and d³. Degree components do not mix under D.

On d=0, the encoder is simply \(\beta c^3\). Take the two exact rational unit-sphere states and positive rational weights in `BM_Jordan_Cubic_Family_Lower_Certificate_2026-10-21.json`. For orientation, their first three coordinates and weights are approximately

| State | a | b | c | Weight |
|---|---:|---:|---:|---:|
| 1 | 0.8737739 | 0.4711565 | 0.1205436 | 0.99773646 |
| 2 | 0.3520258 | 0.1775054 | −0.9190047 | 0.00226354 |

Both have d=0. The printed decimals are explanatory only; the certificate contains the exact rational coordinates, whose squared norms are exactly one, and exact weights summing to one.

With \(v=1+t/2\), form the weighted squared error

\[
 \sum_i w_i\|Ox_i-\beta c_i^3 v\|_2^2
 =A\beta^2-2B\beta+C,
\]

where

\[
 A=\frac{19}{12}\sum_iw_i c_i^6>0,\quad
 B=\sum_iw_i c_i^3 k^Tx_i,\quad
 C=\sum_iw_i x_i^TGx_i.
\]

Its minimum is the exact rational number \(C-B^2/A\). The verifier checks

\[
 C-B^2/A>\frac{3237}{2500}=1.2948.
\]

The numerical value is approximately 1.29480030513. A worst-case error is at least this weighted average for every β. For a polynomial with an even part, symmetrization justifies the reduction above; equivalently use each certificate state and its antipode with half its weight. This proves the lower bound for the whole stated family. BM21-J3 proves the upper bound. ∎

This is a bracket, not an exact symbolic optimum. It establishes that changing coefficients within this cubic family and keeping this decoder can improve the certified squared-error ceiling by **less than 0.0001**. A larger improvement requires changing the family, the decoder, or both. It does not obstruct a better general continuous scalar code.

## 5. Executed verification and remaining boundary

The certificate verifier accepted the exact polynomial identity, all 35 positive LDL pivots and their reconstruction, the invariant identities, the rational comparison with the linear optimum, and the two-state lower certificate. Its acceptance path uses rational arithmetic only. It also rejects deliberately changed matrix and weight certificates.

`BM_Jordan_Return_Bridge_2026-10-21.py` supplies the exact rational Hermite construction. Its included checks cover n=1 through n=12, both time signs and several endpoint choices, and verify the complete Jordan flow identity, exactly prescribed endpoint derivatives, and the integer-power decay of the undesignated derivatives. These finite checks support the implementation; the all-n statement is proved above, not inferred from examples.

The updated working audit adds four scoped theorem records without reclassifying the broad open Jordan row as solved. The other frameworks' classifications, physical gates, independent-review gate and frozen foundation remain unchanged.

The remaining Jordan research obligation is precise: determine the unrestricted continuous n=4 scalar optimum inside the displayed interval, and the other unsolved interior encoder dimensions. The results here do not supply those missing proofs. They do supply a complete native long-return calculation, general continuous lower bounds, an explicit strictly better nonlinear code, and exact certificates identifying how close that code is to the best one in its stated cubic family.

## Included dependencies

* `BM_Continuous_Closure_and_Completion_2026-10-20.md`, BM20-J1–J2: ordered refinement of a continuous scalar factor and the mutual even-return obstruction; full proofs and primary topology references.
* `BM_Completion_Development_2026-10-18.md`, BM18-J1: sampled scalar polynomial factors of unipotent maps are first integrals.

These dependencies are included as dated source snapshots in the combined package. New claims are attributed to the proofs and certificates above; no external paper is cited as proving them.


---

# Branch Mathematics: finite quantum recovery and infinite-state prediction

23 October 2026 · Additive development B23 · Six scoped results

This note keeps the frozen V1 definitions, the original unamplified recovery norm, and the distinction between a causal predictor and a closed current-state encoder. It adds proofs and executable certificates to the 21 October working record. It does not establish historical novelty, independent review, or completion of every BM extension.

The finite algebraic quantum problems below have exact terminating procedures in principle. A general quantifier-elimination engine is **not** implemented or executed in this release. The delivered programs verify real-rational quantum certificates and construct finite response-tree predictors. Those are different implementation claims.

## 1. Fixed quantum contract

Let \(N:M_d\to M_b\) be a completely positive trace-preserving channel, with Kraus operators \(E_i:\mathbb C^d\to\mathbb C^b\). Let \(A\subset M_d\) be a supplied unital observable algebra. Retain

\[
\delta_A(N)=\min_{R\ {\rm CPTP}}\sup_{X\in A,\ \|X\|\le1}
 \|X-N^\dagger R^\dagger(X)\|,
\]

\[
\mathcal K_N=\operatorname{span}_{\mathbb C}\{E_i^\dagger E_j\},\qquad
\kappa_A(N)=\max_{Z\in\mathcal K_N,\ \|Z\|\le1; X\in A,\ \|X\|\le1}
 \|[Z,X]\|.
\]

All norms here are operator norms, including on non-Hermitian inputs. No diamond-norm lower bound is substituted. The recovery minimum is attained by compactness of the finite-dimensional channel set.

For algebraic algorithms the input consists of exact real-algebraic real and imaginary matrix entries, finite dimensions, and an explicit algebra passport

\[
\iota:\bigoplus_{j=1}^s M_{n_j}\longrightarrow A,
\qquad
\iota((X_j))=W\left[\bigoplus_j(X_j\otimes I_{m_j})\right]W^\dagger,
\quad \sum_j n_jm_j=d,
\]

with algebraic unitary \(W\). Additional channel restrictions must be supplied by finite polynomial equalities and inequalities if they are to enter the algebraic algorithm.

The standard Choi characterization used below is classical, as is quantifier elimination over real closed fields [W18, CM12]. Their use here does not establish novelty of the underlying mathematics.

## 2. BM23-Q1 — Exact recovery using only the observable algebra

For each summand choose a Hermitian block matrix

\[
H_j=[H_{j,uv}]_{u,v=1}^{n_j}\succeq0,
\quad H_{j,uv}\in M_b,
\qquad \sum_{j,u}H_{j,uu}=I_b.
\tag{Q1.1}
\]

Define \(\phi_H(\iota(X))=\sum_{j,u,v}(X_j)_{uv}H_{j,uv}\). Then

\[
\boxed{\delta_A(N)=
\min_{H\ {
m satisfying}\ (Q1.1)}
\max_{U_j^\dagger U_j=I_{n_j}}
\left\|\iota(U)-N^\dagger\phi_H(\iota(U))\right\|.}
\tag{Q1.2}
\]

Every feasible \(H\) extends to a physical recovery. In particular, the formula does not optimize over arbitrary linear decoders.

**Proof.** The Choi criterion identifies \(H_j\succeq0\) with complete positivity of the map from the \(j\)-th matrix summand to \(M_b\). The diagonal-block constraint is precisely unitality of their sum. Restricting any recovery adjoint to \(A\) therefore produces a feasible \(H\).

Conversely, let \(P_A:M_d\to A\) be the trace-preserving conditional expectation. In the displayed block coordinates it deletes off-diagonal central blocks and replaces each multiplicity block by its normalized partial trace tensored with \(I_{m_j}\). This is a unital completely positive map fixing \(A\). Thus

\[
R_H^\dagger=\phi_H\circ P_A
\]

is unital and completely positive on all of \(M_d\); its trace adjoint is a CPTP recovery. Its restriction to \(A\) is exactly \(\phi_H\).

It remains to justify testing the full complex operator unit ball using unitaries. A contraction \(X_j=V_j\operatorname{diag}(s_i)W_j^\dagger\), \(0\le s_i\le1\), is the average of the two unitaries

\[
V_j\operatorname{diag}(s_i\pm i\sqrt{1-s_i^2})W_j^\dagger.
\]

Applying this simultaneously to all summands makes any contraction in \(A\) the average of two unitaries in \(A\). Linearity of the error and convexity of the norm prove the equality of the two suprema. Finally the feasible \(H\)-set is compact: it is closed, positive semidefinite, and \(\sum_j\operatorname{tr}H_j=b\). The continuous objective therefore attains its minimum. ∎

The matrix variables have block sizes \(n_jb\), so multiplicities \(m_j\) do not create unnecessary recovery variables. They still enter the physical embedding and the native channel.

## 3. BM23-Q2 — Effective exact optima and sharp defect envelopes

For the finite algebraic input contract above:

1. \(\delta_A(N)\) is a real algebraic number. An exact optimal recovery with algebraic entries can be found by a terminating real-algebraic algorithm.
2. For fixed dimensions and Kraus bound, the attainable set of pairs \((\kappa_A(N),\delta_A(N))\) is effectively semialgebraic, including any supplied semialgebraic channel restrictions.
3. For any algebraic \(c\), one can decide whether channels with \(\kappa_A=c\) exist. If they do, their sharp lower and upper recovery-error envelopes are computable real algebraic numbers. Attainment of either endpoint is decidable. An unattained endpoint still admits algebraic channels within any prescribed positive algebraic tolerance.

These are exact computability and characterization results. They do not say that the resulting elimination is efficient or provide an evaluated closed formula for every dimension and algebra.

**Proof of the fixed-channel statement.** Write every complex entry as two real variables. For \(t\ge0\), let \(\mathsf{Feas}(N,t)\) mean that there are matrices \(H\) satisfying (Q1.1) such that, for every tuple of unitary matrices \(U_j\),

\[
t^2 I_d-M(H,U)^\dagger M(H,U)\succeq0,
\quad
M(H,U)=\iota(U)-\sum_i E_i^\dagger\phi_H(\iota(U))E_i.
\tag{Q2.1}
\]

Positive semidefiniteness is equivalent to nonnegativity of **all principal minors**, not just leading minors. Unitarity, Hermiticity and (Q2.1) are finite polynomial conditions on the real coordinates. Hence \(\mathsf{Feas}\) is an explicit first-order formula over the reals. It holds exactly when \(\delta_A(N)\le t\).

The formula

\[
0\le z\le2\ \wedge\ \mathsf{Feas}(N,z)
\ \wedge\ \forall u\,[0\le u<z\Rightarrow\neg\mathsf{Feas}(N,u)]
\tag{Q2.2}
\]

defines the singleton \(\{\delta_A(N)\}\). Real-closed-field quantifier elimination computes a quantifier-free description of it. A singleton semialgebraic over the real algebraic numbers has an algebraic coordinate. Real-algebraic sampling of the nonempty feasible set at that value produces algebraic \(H\). Formula (Q1.1), the stated expectation \(P_A\), and Choi/Kraus conversion then produce an algebraic recovery. This proves the first assertion.

**Proof of the envelope statement.** Parameterize a channel by \(k\) matrices \(E_i\) with \(\sum_iE_i^\dagger E_i=I_d\). Zero matrices permit Kraus rank less than \(k\). This parameter set is compact because \(\sum_i\|E_i\|_F^2=d\).

Membership in the error space is the polynomial existential condition

\[
Z=\sum_{i,j}\lambda_{ij}E_i^\dagger E_j.
\tag{Q2.3}
\]

An exact formula for \(\kappa_A=c\) consists of \(0\le c\le2\), the universal condition

\[
[Z,\iota(U)]^\dagger[Z,\iota(U)]\preceq c^2 I_d
\tag{Q2.4}
\]

for every \(Z\) represented by (Q2.3) with \(Z^\dagger Z\preceq I_d\) and every unitary tuple \(U\), and an attaining witness \(Z,U,v\) with \(v^\dagger v=1\) and

\[
\|[Z,\iota(U)]v\|^2=c^2.
\tag{Q2.5}
\]

The unitary reduction follows by the same two-unitary averaging argument. For each fixed channel, the actual set \(\mathcal K_N\cap\{\|Z\|\le1\}\) is compact, so a witness exists. The coefficients \(\lambda_{ij}\) need not be bounded; they are quantified coordinates, not an incorrectly asserted compact parameterization of that unit ball.

Conjoin (Q2.2), (Q2.3)–(Q2.5), channel constraints and any extra polynomial restrictions, then eliminate all variables except \((c,z)\). This computes the attainable semialgebraic set. A nonempty bounded one-dimensional section at algebraic \(c\) has algebraic endpoints, computable from its polynomial description. Direct membership tests decide attainment; sample points in the open tolerance intervals provide near-extremal algebraic channels.

Although the Kraus parameter space is compact, a level set of the **normalized span defect** need not be closed. The proof uses supremum/infimum and tests attainment separately; it does not assume compactness of a defect slice. ∎

For a concrete requested envelope, (Q2.1)–(Q2.5) are the algorithm specification. No general elimination output is supplied in this release. The earlier full-algebra formulas and the certified examples below remain the evaluated cases.

## 4. BM23-Q3 — Exact recovery of classical labels carried by quantum states

Consider the native channel

\[
N(\rho)=\sum_{i=1}^r\rho_{ii}\sigma_i,
\]

where the supplied signal matrices \(\sigma_i\in M_b\) are density operators, and take the diagonal logical algebra \(A\subset M_r\). Let

\[
p_* = \max_{F_i\succeq0,\ \sum_iF_i=I_b}\min_i\operatorname{tr}(\sigma_i F_i).
\]

Then

\[
\boxed{\delta_A(N)=2(1-p_*)},\qquad
\boxed{p_* = \min_{\lambda_i\ge0,\ \sum_i\lambda_i=1; Y=Y^\dagger,\ Y\succeq\lambda_i\sigma_i}
\operatorname{tr}Y.}
\tag{Q3.1}
\]

Both optima are attained. These are worst-case recovery statements, not a substitution of an average-case probability for BM's operator norm.

**Proof.** A recovery adjoint maps the diagonal rank-one projectors to a POVM \((F_i)\). Conversely, any POVM is realized by measuring it and preparing the corresponding logical basis state. The composed classical transition probabilities are

\[
p_{j|i}=\operatorname{tr}(\sigma_i F_j).
\]

For \(X=\operatorname{diag}(z_1,\ldots,z_r)\), \(|z_i|\le1\), the reconstructed error at input label \(i\) is \(z_i-\sum_jp_{j|i}z_j\). Its supremum modulus is the row's coefficient \(\ell_1\)-norm, namely \(2(1-p_{i|i})\). It is attained by \(z_i=1\), \(z_j=-1\) for \(j\ne i\). The maximum over rows commutes with this finite supremum, proving the first identity even for complex inputs.

The primal maximizes \(q\) subject to \(\operatorname{tr}(\sigma_iF_i)\ge q\) and the POVM constraints. Its Lagrangian is

\[
(1-\textstyle\sum_i\lambda_i)q+\operatorname{tr}Y
+\sum_i\operatorname{tr}[(\lambda_i\sigma_i-Y)F_i].
\]

Taking its supremum over free \(q\) and positive semidefinite \(F_i\) is finite precisely under the displayed dual constraints, yielding \(\operatorname{tr}Y\). Strict primal feasibility holds with \(F_i=I_b/r\), \(q=0\), and strict dual feasibility with \(\lambda_i=1/r\), \(Y=2I_b\). Finite-dimensional semidefinite duality gives equality [W11]. Compactness gives primal attainment. For the dual one may restrict to \(\operatorname{tr}Y\le1\): the choice \(Y=\sigma_1\), \(\lambda_1=1\), \(\lambda_{i>1}=0\) is always feasible with trace one. The dual constraints imply \(Y\succeq0\); bounded trace and the probability simplex then give a compact minimizing set. ∎

A directly checkable certificate consists of a POVM with every success at least \(q\), and dual-feasible \((\lambda,Y)\). Weak duality alone proves

\[
2(1-\operatorname{tr}Y)\le\delta_A(N)\le2(1-q).
\tag{Q3.2}
\]

When \(q=\operatorname{tr}Y\), the value is exact. The delivered verifier checks real-rational certificates by exact Schur complements, including zero pivots. It does not use numerical eigenvalue thresholds.

For example, take

\[
\sigma_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\sigma_2=\frac1{25}\begin{pmatrix}9&12\\12&16\end{pmatrix},
\]

\[
F_1=\frac1{10}\begin{pmatrix}9&-3\\-3&1\end{pmatrix},\quad F_2=I-F_1,
\quad\lambda_1=\lambda_2=\tfrac12,
\quad Y=\frac1{50}\begin{pmatrix}27&6\\6&18\end{pmatrix}.
\]

Both primal successes and \(\operatorname{tr}Y\) equal \(9/10\); both dual slacks are positive semidefinite of rank one. Thus \(\delta_A=1/5\), exactly. The package also certifies four BB84 signal states (error 1), identical states (error \(2-2/r\)), orthogonal states (error 0), and symmetric classical channels with diagonal success \(3/4\) (error \(1/2\)).

## 5. BM23-Q4 — Exact common-recovery capability budgets

Fix one algebraic finite-dimensional channel and a finite algebraic catalogue \(A_1,\ldots,A_s\). Require a **single** recovery \(R\) to meet all error budgets. Define

\[
\mathcal B=\{t\in[0,2]^s:\exists R\ {\rm CPTP},\ e_{A_j}(R)\le t_j\ \forall j\}.
\]

Then \(\mathcal B\) is compact, convex, upward closed within its box, and effectively semialgebraic. For algebraic budget inputs, feasibility and Pareto membership are decidable; algebraic weighted-sum optima and algebraic recovery witnesses are computable.

**Proof.** Use one full recovery-adjoint Choi matrix \(H=[H_{uv}]_{u,v=1}^d\succeq0\), \(H_{uv}\in M_b\), \(\sum_uH_{uu}=I_b\). For each algebra add the corresponding universally quantified unitary inequalities from (Q2.1), using this same \(H\). This is a polynomial formula and is therefore effectively semialgebraic after elimination.

The channel set and budget box are compact. Each error functional is continuous, so the joint feasible set is closed and its projection compact. Error is convex in a recovery; mixing two recoveries and their budgets proves convexity. Upward closure follows directly from the inequalities. Pareto membership is the first-order condition

\[
t\in\mathcal B\quad\wedge\quad
\neg\exists u\in\mathcal B\ [u\le t\ \wedge\ \bigvee_j u_j<t_j].
\]

Algebraic sampling and compact minimization handle weighted sums. ∎

Separate algebra-specific optima do not, by themselves, furnish the required shared recovery. The common Choi variable is essential. This theorem supplies a finite catalogue formulation; it does not assert that all approximate capabilities have a greatest algebra.

## 6. BM23-I1 — Finite causal prediction from a uniform decay bound

Let a native deterministic system have a finite action alphabet of size \(s\ge1\), total action maps, an initial set \(X_0\), and a task \(\tau:X\to\mathbb R^p\), \(p\ge1\). Suppose supplied rational constants \(M\ge0\), \(0\le L<1\) certify

\[
\|\tau(f_w(x))\|_2\le ML^{|w|}
\quad(x\in X_0,\ \text{every finite action word }w).
\tag{I1.1}
\]

Assume each finite response \(\tau(f_w(x))\) can be computed to any prescribed coordinate accuracy from the native description of \(x\). Then for every rational \(\varepsilon>0\) a finite causal machine admits effective admissible initialization achieving error at most \(\varepsilon/2\), uniformly over all initial states, action sequences and times. The procedure takes a supplied finite-response evaluation oracle and may select different valid codes from different descriptions of the same state.

No compactness of \(X_0\), common eigenbasis, or commutation of the actions is required. At the set level one may select one admissible code for each state; the effective procedure does not promise a canonical extensional or continuous finite-valued quantizer.

**Construction and proof.** Choose the least \(K\ge0\) with \(ML^K\le\varepsilon/2\), with \(L^0=1\). Let

\[
h=\varepsilon/(2p),\qquad
J=\lceil M/h\rceil+1,\qquad Q=(2J+1)^p.
\]

For every word of length below \(K\), compute its task to coordinate error at most \(\varepsilon/(4p)=h/2\), then round each coordinate to the nearest multiple of \(h\). The total coordinate error is at most \(h\). Each integer grid label lies between \(-J\) and \(J\).

The initial machine state is the resulting labelled full \(s\)-ary response tree of depth \(K\). Its output is the root label times \(h\). An action selects the corresponding child tree. At depth zero it enters a zero-output absorbing state. These updates are well-defined on the finite universal codebook of all such labelled trees, independent of the particular initialized native state.

At times \(t<K\), the stored subtree root is exactly the quantized initial response for the action prefix actually taken. Its error is at most \(\sqrt p\,h=\varepsilon/(2\sqrt p)\le\varepsilon/2\). At \(t\ge K\), (I1.1) bounds the native task's distance from the absorbing output by \(ML^t\le\varepsilon/2\).

Writing \(N_r=1+s+\cdots+s^{r-1}\), a universal state bound is

\[
\boxed{1+\sum_{r=1}^K Q^{N_r}.}
\tag{I1.2}
\]

The sum is zero when \(K=0\). This is an existence and effective construction bound, not a minimum-state claim. ∎

The finite code carries remaining forecast depth. Every admissible initial code satisfies the bound, so uniqueness of initialization is unnecessary. A continuous finite-valued initializer on a connected native carrier would be constant; no such initializer is asserted here. It need not equal a fixed instantaneous encoding of the current native state. Thus this is a causal-history construction, not a new exact-quotient theorem. Its assumptions do not include persistent forcing or arbitrary partial-action boundaries.

### A noncommuting infinite-dimensional witness

On the unit ball of \(\ell_2(\mathbb N_0)\), let \(S\) be the unilateral right shift,

\[
f_0(x)=\tfrac12Sx,\qquad f_1(x)=\tfrac12S^*x,
\qquad\tau(x)=(x_0,x_1).
\]

Both action norms are \(1/2\), and the task norm is at most the state norm. Hence (I1.1) holds with \(M=1,L=1/2\). The actions do not commute: \(S^*S=I\), whereas \(SS^*=I-P_0\). Their initial unit ball is not norm compact. This example therefore lies beyond a shared diagonal contraction model.

For \(\varepsilon=1/8\), the construction uses \(K=4\), \(h=1/32\), \(J=33\), and \(Q=4489\). Its universal codebook bound is

\[
1+4489+4489^3+4489^7+4489^{15}.
\]

Only a depth-four tree is built for each initialized input. The package replays every binary action word through length nine for 24 rational initial states, both with exact profile values and deliberately perturbed values within the allowed oracle accuracy. All 49,104 checks pass; the largest observed squared error is \(1/256\). The analytic operator-norm argument, not this finite replay, proves the bound for the entire infinite-dimensional unit ball and all times.

## 7. BM23-I2 — No universal additive approximation algorithm

There is no algorithm that, for every computable infinite-carrier deterministic system with bounded rational task values, always returns the optimal infinite-horizon one-state prediction error to additive accuracy \(1/5\). There is also no algorithm that always returns a one-state predictor whose error is within \(1/5\) of the optimum. This already holds for one fixed native update \(f(n)=n+1\) on \(\mathbb N_0\), one initial state \(n=0\), and scalar task values in \(\{0,1\}\).

**Proof.** Given a program \(e\), define \(\tau_e(0)=0\). For \(n\ge1\), simulate \(e\) for \(n-1\) transitions and put \(\tau_e(n)=1\) if it has halted, and zero otherwise. This is a uniformly computable rational-valued task: each individual evaluation requires only a finite simulation.

A one-state predictor outputs a constant \(c\). If \(e\) never halts, the trajectory is constantly zero and the optimal error is zero. If \(e\) halts, the trajectory contains both zero and one, so

\[
\inf_c\sup_{n\ge0}|\tau_e(n)-c|
=\inf_c\max\{|c|,|1-c|\}=\tfrac12.
\]

An additive-\(1/5\) value approximation must lie in \([-1/5,1/5]\) in the first case and \([3/10,7/10]\) in the second. Comparing it to \(1/4\) decides halting, which is impossible. A returned near-optimal constant must lie in \([-1/5,1/5]\) in the first case and \([3/10,7/10]\) in the second, so it gives the same contradiction. For a computable-real output, the separated intervals allow a finite-precision comparison.

Likewise, deciding feasibility of one-state error \(1/4\) would decide nonhalting. ∎

This rules out an unrestricted algorithmic completion demand. It does not prevent solving a specified native instance, a finite carrier, or the effective decay class in BM23-I1. In the reduction the missing uniform tail information is substantive, not an implementation inconvenience.

## 8. Verification, disposition and residual obligations

The exact certificate program validates 15 quantum optima. Its critical PSD routine agrees with an independent all-principal-minors oracle on 854 symmetric rational matrices. Nine deliberately corrupted quantum inputs are rejected. The response-tree implementation passes 49,104 trajectory checks and eight invalid-parameter/action rejection checks. These checks validate the supplied implementations; the general theorems are established by the arguments above.

| Existing obligation | Disposition after this note | Still not claimed |
|---|---|---|
| Finite quantum optimum for a specified algebraic channel/algebra | Exact attained algebraic optimum and terminating algorithm specification | A general QE implementation or efficient solver |
| Sharp proper-algebra defect envelopes in a fixed finite algebraic class | Effective semialgebraic characterization; endpoint and attainment procedures | Evaluated closed-form envelopes for every class |
| Finite catalogue under a common quantum recovery | Exact semialgebraic compact convex budget set | A greatest approximate observable algebra in every setting |
| General infinite-carrier predictor optimization | A universal additive approximation algorithm is impossible | An algorithm for all computable native inputs |
| Infinite-dimensional causal prediction under uniform task decay | Explicit finite construction with a state bound | Minimum state count, persistent forcing, or exact current-state closure |
| Unrestricted continuous four-state Jordan optimum | Unchanged: squared error lies in the prior certified interval | An exact unrestricted optimum |
| All global regular realization and nonlinear repair classes | Unchanged outside established contracts | A universal classification or universally valid repair |

These results narrow the research boundary. They do not justify marking the six broad extension rows as wholly solved. The V1 framework's completion gate was already internally met; that is a separate and narrower claim than exhausting the research programme.

## References

- **[W18]** John Watrous, *The Theory of Quantum Information*, Chapter 2, especially Theorem 2.22 and channel characterizations. [Author-hosted chapter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf). Used for the standard Choi criterion and native channel conventions.
- **[W11]** John Watrous, *Theory of Quantum Information*, Lecture 8, optimal-measurement semidefinite programs. [Author-hosted notes](https://cs.uwaterloo.ca/~watrous/TQI-notes/TQI-notes.08.pdf). Used for standard measurement optimization/duality; the minimax recovery reduction is written above.
- **[CM12]** Cyril Cohen and Assia Mahboubi, “Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination,” *Logical Methods in Computer Science* 8(1:02), 2012. [Journal article](https://lmcs.episciences.org/844). Used for effective real-closed-field quantifier elimination; no claim is made that the new BM formulas have been formally verified by that work.
- **[BM18]** *BM Completion Development*, 18 October 2026, especially Q1–Q5 and A1–A3. Included in the prior development package.
- **[BM20]** *BM Continuous Closure and Completion*, 20 October 2026, especially C1–C3, Q1–Q3 and I1.
- **[BM21]** *BM Jordan Returns and Certified Bounds*, 21 October 2026. Its exact rational Jordan certificates remain unchanged.


---

Source: BM_Necessity_and_Comparison_2026-10-23.md

# BM: necessity certificates and an exact comparison with existing theory

23 October 2026. Additive completion analysis of the frozen BM V1 / Edition 1.1 foundation. The labels N1–N4 below identify arguments in this note; they do not replace T01–T55 or assert historical novelty. These are explicit deductions and implementations of existing principles, not a new foundational calculus.

## 1. The question that a necessity claim must answer

T01 proves that a particular representation loses a required distinction when it merges states with different task values. T11 proves when a particular representation supports autonomous evolution. T13 concerns essentiality relative to a comparison class fixed independently of the obligation test.

Three different questions must remain separate:

1. Does this proposed representation work?
2. Does any allowed representation using the available observations work?
3. Is some named Branch indispensable among all members of the specified comparison class?

A negative answer to question 1 does not automatically answer questions 2 or 3. The following construction answers all three in a finite deterministic contract and gives an independently replayable negative witness. A comparison class containing no candidates is not evidence of substantive indispensability. A positive reference realization is also required before attributing failure specifically to removal of one information source.

## 2. Declared contract

Let X be a nonempty finite native state set, A a finite action alphabet, and f_a:D_a ⊆ X → X partial deterministic updates. Every state in X is initially possible. Let O:X→Y be a product of the exact tasks required by the receiver. Legitimate task values may include a value called “null”; it is not the unavailable tag used below.

Let V:X→Z collect the observations available to an implementation. Its code may be any deterministic function C=hV into a set Q. The implementation must have a decoder d:Q→Y and partial autonomous updates g_a such that, on the realized code image,

\[
dC=O,\qquad x\in D_a\iff C(x)\in\operatorname{dom}g_a,
\qquad C(f_a x)=g_a(Cx)\quad(x\in D_a).
\]

No extra measurement, history before initialization, stochastic side channel, or native regularity requirement is present. Requiring continuity, a distributed encoder, quantum physicality, a particular output catalogue, or a hardware architecture changes this contract. An observation that must remain recoverable belongs among the tasks O; merely being available does not mean it must be retained.

Adjoin a distinct unavailable state ⊥. Extend each f_a to X∪{⊥} by mapping unavailable inputs to ⊥ and fixing ⊥. Define the tagged observation Õ(x)=(available,O(x)) for x∈X and Õ(⊥)=unavailable. For a finite action word w, let f_w denote execution in word order, including the empty word. Put

\[
xE_*y\quad\Longleftrightarrow\quad
\widetilde O(f_wx)=\widetilde O(f_wy)\quad\text{for every }w\in A^*.
\]

This is the future task-and-availability equivalence. It is computed from the native actions and required outputs, before testing any available observation V.

## 3. N1: an exact test over every encoding of available observations

**Statement.** An implementation satisfying the contract exists if and only if

\[
\boxed{\ker V\subseteq E_*.}
\]

When it exists, the smallest number of realized code states is |X/E_*|. A minimum code is the quotient q_*:X→X/E_*, expressed as a function of V.

**Necessity.** If V(x)=V(y), then C(x)=C(y). Autonomous deterministic execution from this same code has the same availability at each step and the same decoded task whenever available. Induction over the action word gives equality of every tagged future output. Thus xE_*y. Independently, any valid code satisfies ker C⊆E_*, since equal codes have equal future behavior. Consequently it must distinguish every two different E_* classes and has at least |X/E_*| realized states.

**Sufficiency.** E_* is an equivalence, since it is an intersection of kernels. Equality for the empty word preserves O. Equality for a one-action prefix preserves availability; after a common available action a, equality for all remaining words gives f_a(x) E_* f_a(y). Therefore each partial action descends to the quotient. The hypothesis ker V⊆E_* makes q_* constant on each V-fibre, so T01 supplies h on V(X) with q_*=hV. The quotient's task decoder and partial updates are well defined. Its realized size attains the lower bound. ∎

The direction of the containment matters. A code computed from V is allowed to merge more than V does. Exactification that must *retain* V is a different problem: there the repaired code must determine V, and its kernel must be contained in ker V. Reversing these two problems can manufacture a false necessity claim.

## 4. N2: finite termination, witnesses, and branch removal

Start with the partition of X∪{⊥} determined by Õ. At each round replace each state's color by the tuple consisting of its current color and every successor color. On X this can make at most n−b strict refinements, where n=|X| and b is the number of initial task classes on X. The unavailable singleton never merges or splits.

**Proof.** Each strict refinement increases the number of classes on X by at least one. The number starts at b and cannot exceed n. Inductively, equality after k rounds means equality of all tagged task outputs for words of length at most k. Once stable, equal colors have identical output and successor colors, so induction gives equality for every word. Therefore the stable relation is E_*. Every pair separated by E_* has a distinguishing word of length at most n−b. Breadth-first search on ordered state pairs finds a shortest such word. ∎

Suppose V=(V_1,…,V_m) is a supplied list of observation sources, and the full V is sufficient under N1. Remove source i and write V_{−i}. Source i is essential relative to arbitrary deterministic encodings of the remaining sources exactly when

\[
\exists x,y:\quad V_{-i}(x)=V_{-i}(y),\quad x\not E_*y.
\]

The states and a separating word are a finite proof of this relative necessity. N1 proves both directions. This is not a theorem that a mathematical discipline, a particular notation, or the whole BM framework is uniquely necessary.

For any independently supplied finite catalogue of allowed feature subsets, checking N1 on every member gives exact feasibility, inclusion-minimal members *within that catalogue*, and minimum declared feature cost. If no catalogue is supplied, the implementation enumerates all subsets. Costs are externally supplied nonnegative rationals; they are not physical measurements. An empty catalogue has no feasible member but proves nothing about an omitted implementation. If even the full observations fail, the implementation reports insufficient observations and makes no nonvacuous branch-essentiality claim.

Minimum retained code states and number of indispensable observation sources are different quantities. For the XOR task on two independent bits, both input sources are essential, while a centralized task code has only two states.

## 5. N3: a quantified obstruction under approximation

Suppose V(x)=V(y) and a common available word w gives task outputs whose distance is D in a metric space. Any deterministic autonomous predictor initialized solely from V produces one common decoded value at that word. By the triangle inequality at least one of its two task errors is at least D/2.

Thus the same witness supplies a lower bound on the attainable worst-case error. A declared tolerance ε<D/2 is impossible. This is a necessary bound, not a sufficient construction for approximate causal prediction. If the witness is unequal action availability, it is an exact domain obstruction; assigning it a numerical error requires an additional loss convention. Stochastic success probabilities, expected losses, and history-conditioned initializations need their own contracts.

## 6. Eight worked cases

The companion JSON and Python files contain the following exact cases.

| Case | Native model and obligation | Certified conclusion |
|---|---|---|
| Delayed velocity | (x,v)∈{0,1}², f(x,v)=(v,v), task x | Both x and v are essential observation sources; minimum autonomous code has four states. |
| Discard nonpredictive observation | (a,b,c)∈{0,1}³, f(a,b,c)=(a,c,c), task a, available (a,b) | Raw (a,b) is not autonomous, but C=a is. No new observation is necessary; minimum code has two states. |
| Duplicate observations | Task x; two copies of x available | Either copy suffices, so neither is individually essential. Supplied costs select the cheaper copy. |
| Availability obstruction | Constant task on two states; action enabled at only one; observation constant | No allowed encoding works; the length-one word certifies unequal availability. |
| Joint XOR | Independent bits a,b; task a XOR b | Each observation source is essential; the centralized code has two states. |
| Empty observation success | One state, no task distinctions or actions | One constant code state suffices; empty feature subset is feasible. |
| Empty candidate catalogue | A valid full observation exists but no candidates are supplied | No feasible member of that catalogue; no universal impossibility is inferred. |
| Retained legacy changes contract | Same model as the second row, but b must also remain recoverable | Available (a,b) is now insufficient; hidden c separates future legacy outputs. |

The second row is a decisive control example. Two states (0,0,0) and (0,0,1) have the same available observation (0,0), but its successors are (0,0) and (0,1). T11 rejects the raw observation as autonomous. Yet the requested task a stays unchanged, so C=a solves the task exactly. The first failure cannot justify demanding a new Branch unless retaining b is part of the obligation.

## 7. N4: T55-C7R as observed labelled bisimulation

This is an explicit comparison deduction, not a claim that the entire BM framework is equivalent to one other framework.

Take precisely the finite T55-C7R contract: nonempty sorts X_i, initial equivalences B_i, local labelled relations L_{i,a}, and finitely many partial deterministic interactions G_b with independently replaceable input slots and all Cartesian contexts. Form a labelled transition system with carrier

\[
S=\coprod_i X_i\;\amalg\;\{\bot_r:\ r\text{ is an interaction receiver sort}\}.
\]

Observe each native state's sort and initial B_i class. Observe each ⊥_r by its own distinct unavailable tag. All labels below are distinct and act only on their declared source sort; other sorts and unavailable states have no successors for that label.

* For each local relation L_{i,a}, add its labelled edges unchanged.
* For every interaction b, input slot p, and fixed tuple c of all other inputs, add a label (b,p,c). From u∈X_{i_p}, its unique successor is G_b(c[u]) in the receiver sort when defined, and ⊥_{r(b)} otherwise.

For an equivalence H refining the observations, labelled bisimulation means equality of successor H-class sets for every label. The local labels impose exactly the T55-C7R local relation conditions. A context label has one tagged successor, so its condition is exactly contextual equivalence in that slot. The unavailable singleton enforces saturation of the interaction domain.

Conversely these local and contextual conditions imply bisimulation on the expanded system. For a full interaction, replace equivalent input slots one at a time. All intermediate tuples remain permitted Cartesian contexts, and transitivity preserves the receiver class and domain membership. This recovers full interaction descent. Hence restrictions of observed bisimulation equivalences are exactly the admissible equivalence families of T55-C7R. The greatest such bisimulation restricts to the theorem's uniquely coarsest family. ∎

If n_i=|X_i|, this expansion uses Σ_i n_i plus at most one unavailable state per receiver sort. Interaction b of arity m_b contributes

\[
\sum_{p=1}^{m_b}\prod_{q\ne p}n_{i_q}
\]

context labels and m_b ∏_q n_{i_q} context edges. Local relation edges are additional. This can be a large expansion when interactions are supplied succinctly. An efficient direct BM implementation would need a separate complexity comparison; the reduction alone proves no speed advantage.

This reduction does not transport to arbitrary correlated admissibility by fiat. The coordinate-replacement proof can leave a restricted legal context set. The BM18 correlated-interface criteria address that different problem. It also does not collapse relational bisimulation into trace equality, probabilities into successor supports, or a native quantum channel into an arbitrary relation.

## 8. What the external comparison establishes

The bibliography below was checked on 23 October 2026. This was a targeted foundational comparison, not an exhaustive novelty search.

| BM item | Existing mathematical source | Result of this comparison |
|---|---|---|
| T01, T04, T06, T07 | Quotient factorization and elementary kernel identities; BM sources already mark them classical | Retain their proofs and necessity role; make no novelty claim for these ingredients. |
| Contextual exactification and deterministic future quotient | Rutten's treatment of systems, homomorphisms and bisimulation | Same standard system-equivalence structure in the deterministic contract. N1 states the additional available-observation feasibility test explicitly. |
| T55-C7R under full product contexts | Relational partition refinement and labelled bisimulation | N4 supplies an exact reduction, rather than merely a vocabulary resemblance. |
| Passport/contract refinement, conjunction and composition | Benveniste et al., *Contracts for system design*, especially Chapter 4 | A prior mathematical meta-theory already exists. The entire heterogeneous BM architecture has not been proved equivalent or inequivalent here. |
| Refinement and fixed-point reasoning | Cousot and Cousot's abstract interpretation | Existing abstraction/fixed-point theory is a required comparison baseline. No claim that exact BM quotients exhaust that framework. |
| Quantum algebra recovery | Bény, *Conditions for the approximate correction of algebras* | Imported recovery theory must be attributed. Its amplified norms must not be silently substituted for BM's stated unamplified defect/error quantities. |
| BM21 Jordan certificates; BM23 exact special-family envelopes | No theorem-specific priority conclusion established in this search | Compare identical encoder classes, horizons, norms and native constraints before claiming novelty. Absence of a search match is not evidence of priority. |

The legitimate positioning question is which BM statements, implementations or coordination guarantees add something under an exact shared contract. Proving that no other mathematical framework could express them is neither established nor required for a useful, rigorous theory.

## 9. Verification and limits

Run from the directory containing the files:

```sh
python3 BM_Necessity_Verification_2026-10-23.py
```

The run passed 2,824 native-instance certificates: 2,636 exhaustively generated small systems, 180 seeded multi-action systems and eight worked examples. It made 6,735 comparisons against a separate oracle that enumerates every possible code partition and checks encoder dependence, output equality, partial availability and autonomous closure directly. It replayed 6,256 quotient-separation witnesses and checked 2,744 shorter words; eight malformed inputs and fourteen corrupted certificates were rejected.

The positive checker verifies exact quotient descent. A separating word for each pair of quotient representatives certifies that different classes cannot be merged; closure makes this argument apply to their whole classes. This proves the finite certificate's minimality without rerunning the refinement algorithm. The checker does not use a proof-assistant kernel. All code and written proofs here were developed within this project; a differently implemented oracle is not an independent human review.

The reference implementation deliberately accepts at most 64 native states, eight actions and twelve observation sources. These are implementation limits, not mathematical limits. It enumerates feature subsets and makes no polynomial-time claim in the number of features. Refinement-round counts are execution diagnostics; the replay checker verifies the mathematical quotient and bounds but does not independently reproduce the exact number of rounds taken.

## References

1. BM, *Branch Mathematics Research Edition*, pinned public 23 October 2026 release: T01, T04, T08, T10–T13, T55 and the exactification construction. The source hash is in the accompanying completion register.
2. BM, *Mathematical Edition*, 10 September 2026, finite simultaneous-refinement chapter T55-C7R. Frozen hypotheses govern N4.
3. J. J. M. Rutten, “Universal coalgebra: a theory of systems,” *Theoretical Computer Science* 249 (2000), 3–80. [CWI record](https://ir.cwi.nl/pub/48); [paper](https://pages.jh.edu/rrynasi1/NewFoundations4Math/Literature/Coalgebras/Rutten2000UniversalCoalgebra-ATheoryOfSystems.pdf). Sections 2, 5 and 7 describe the relevant structures. N4 is the explicit translation written in this note.
4. R. Paige and R. E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6) (1987), 973–989. [Publisher record](https://epubs.siam.org/doi/abs/10.1137/0216062). The abstract identifies the relational coarsest-partition problem; no runtime bound was imported from an unread proof.
5. A. Benveniste et al., *Contracts for system design*, *Foundations and Trends in Electronic Design Automation* 12(2–3) (2018), 124–400. [Institutional record](https://research-explorer.ista.ac.at/record/5677); [author manuscript](https://www.cpsschool.eu/wp-content/uploads/2018/09/main_contracts.pdf). The manuscript has provisional publisher pagination; Chapter 4 is the comparison location.
6. P. Cousot and R. Cousot, “Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints,” POPL (1977), 238–252. [Author's publication page](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml).
7. C. Bény, “Conditions for the approximate correction of algebras,” arXiv:0907.4207 (2009). [Paper](https://arxiv.org/pdf/0907.4207), Sections 1.2–3.


---

Source: BM_Completion_Requirements_2026-10-23.md

# What remains to complete BM

**23 October 2026 — scope, closure conditions, completed corrections and remaining work**

BM's task-distinction, dynamic-closure and relative-essentiality arguments are already part of its foundation. They establish mathematical necessities under stated contracts. The remaining work is to make the accepted claims fully traceable, assess their relationship to existing mathematics, obtain independent validation, finish any implementations actually promised, and resolve the specifically retained research problems.

This audit maps every one of the **336 BM entries** in the current **645-entry** BM/GURF/Steadman inventory. It checks the fingerprints of all **23 source documents**, reads and maps the proof basis of **T01–T55**, and adds a tested finite necessity analyzer. It does not re-prove all the long analytic and quantum results, recover missing historical transcripts, or establish the completeness of an unbounded research program.

## 1. Completion must refer to a fixed claim

The word “complete” currently covers several different milestones. They have different tests.

| Milestone | Acceptance condition | Current assessment |
|---|---|---|
| Defined V1 framework | Every required object, rule, domain, native structure and acceptance relation is specified; principal scoped claims have arguments and explicit boundaries | Recorded as internally established in the frozen V1 / Edition 1.1 sources. No contradiction was found in the 55 short canonical arguments inspected here. |
| Fully traceable proof release | Every retained claim resolves to its exact statement, assumptions, proof, dependencies and applicable errata | Partly complete. This audit maps T01–T55; other dependency lists still need review. |
| Independently checked release | Named proofs/certificates are checked by an independent reviewer or an appropriate formal checker, with objections resolved and scope recorded | Not established. Internal tests, including this audit, do not satisfy this milestone. |
| Finished reference implementation | Every advertised supported contract has an executable path, honest limits, positive/negative certificates and adequate differential checks | Several finite contracts are implemented. General algebraic quantum elimination is a proved procedure, not delivered general software. |
| Demonstrated contribution over alternatives | Exact theorem comparisons and controlled benchmarks establish a specific mathematical or practical difference | Some foundational correspondence is now explicit. Broader novelty and practical superiority remain unestablished. |
| Complete historical archive | Every retained historical identifier has its original source or an explicit supersession/retirement record | Still incomplete in the governing sources. This turn's targeted searches did not recover the missing material. |
| Completed declared research extensions | Each selected remaining native problem has a proof, counterexample or precisely justified impossibility disposition | Six broad extension families remain. Some universal algorithmic demands have already been disproved. |

A complete framework can define and analyze unsolved instances. That does not solve those instances. Conversely, leaving an optional research extension open does not erase a proved necessity theorem. These distinctions preserve existing progress while preventing a broader completion claim than the evidence supports.

For a release, fix its finite set of mandatory obligations **before** evaluating it. Each one must end in one of four honest dispositions: proved under its stated assumptions; explicitly conditional on a separately checkable native premise; corrected/replaced after a counterexample; or excluded from that release with its open status preserved. Calling an unsolved mandatory theorem “optional” after the fact is not a proof of completion.

## 2. BM's established purpose should lead the presentation

The foundation's central claim is precise:

> Given a native system and a declared task, continuation and realization contract, determine which distinctions cannot be removed, whether the operations descend, whether the interfaces work jointly, and what the requested realization costs.

The main supporting chain is already present:

| Requirement | Existing mathematical content | Necessary restriction |
|---|---|---|
| Present task | T01, T04: a decoder exists exactly when the task is constant on representation fibres | Set-level existence gives no automatic continuous, measurable or physical decoder. |
| Future behavior | T10–T12 and contextual exactification | Partial availability, allowed action words, initial-state scope and retained legacy information are part of the contract. |
| Branch removal | T13 and the fixed comparison-class definition | The class must be independently specified; one failed encoding is insufficient to reject every possible encoding. |
| Joint interfaces | T08, T55-C7R and the later correlated-interface results | Full product contexts and restricted/correlated contexts have different theorems. |
| Joint realization | T16–T20, T25, T44 and configuration semantics | Local feasibility and pairwise agreement do not generally give one global witness. |
| Quantitative loss | T32, T33, T41–T42, T47–T48 and later closure-price results | Metric, norm, horizon, decoder class and admissibility constraints must stay fixed. |
| Native realization | Smooth, stochastic, quantum and infinite-dimensional results | Each native category has its own existence and admissibility obligations. |

This demonstrates a mathematical purpose. It does not establish that no other framework can state the same results. BM's public contribution statement should specify exactly which synthesis, calculation, bound, counterexample or executable certificate it supplies.

## 3. What this audit completed

### 3.1 Corrected source accounting and made proof evidence explicit

The base gate A0 still described **22** sources, while its manifest contained **23**. The readiness edition corrects the count and checks every source hash. All 645 prior IDs and classifications are preserved.

The base BM ledger had **183 theorem-classified entries with an empty dependency field**, including all 55 canonical supporting results. Empty fields do not show that a proof is missing: many short arguments are self-contained. The new map records the proof basis of all **55**. Fifteen of these entries use prior numbered results in their argument; the other forty are self-contained at that level. Nontrivial imported mathematics is still stated where used.

**128 other theorem-classified entries** still have no enumerated dependency list in this supplement. The remaining existing lists also require a completeness review; successful identifier resolution is not proof of completeness. The recorded dependency edges are acyclic, but this is not a complete formal proof graph for the entire corpus.

### 3.2 Turned relative necessity into a certificate-generating finite test

For finite partial deterministic systems, define E_* by agreement of every required future task and action-availability outcome. If V is the available observation, then

\[
\boxed{\text{Some exact autonomous task code computed from }V\text{ exists}
\iff \ker V\subseteq E_*.}
\]

This tests **every deterministic encoding of V**, not just the encoding first proposed. A successful test constructs a minimum-state quotient. A failure supplies two states with the same available observation and a finite action word separating their required behavior. The full proof, feature-removal test, conditional approximation lower bound and code are included.

The analyzer also handles duplicate observations, joint XOR, unavailable actions, empty candidate catalogues, and the difference between available information and mandatory retained legacy information. It makes no “indispensable feature” claim when the full observations cannot satisfy the task in the first place.

**Verification:** 2,824 instance certificates, 6,735 comparisons against independently implemented exhaustive code-partition search, 6,256 replayed separation witnesses, 2,744 shorter-word checks, eight invalid-input rejections and fourteen corrupted-certificate rejections passed. These are internal software checks, not external proof review.

### 3.3 Made one foundational prior-art comparison exact

Under its original finite full-product assumptions, T55-C7R translates to observed labelled bisimulation on a disjoint union of typed states, with one label for each fixed interaction context. The note proves both directions and quantifies the size of the expanded system. Thus this theorem's relationship to classical partition refinement is explicit.

Primary sources also establish that mathematical contract meta-theories and abstraction/fixed-point frameworks predate BM. This identifies concrete comparison targets. It neither proves that all of BM is redundant nor establishes that its entire architecture is historically new.

### 3.4 Corrected the old benchmark's presentation and inference

A separately labelled reading edition corrects four problems in the historical GW150914 benchmark:

* The mass-equivalent residual must be m₁+m₂−M_f−E_rad/c². Subtracting the declared energy directly from masses is dimensionally wrong.
* The supplied rounded decimal inputs give an exact arithmetic zero. A residual near 10⁻¹⁵ from binary floating-point arithmetic is not experimental accuracy.
* Ratios of displayed FAR upper limits are not ratios of actual false-alarm rates.
* Matching reported p_astro values of 1.0 does not establish equality of the unrounded probabilities or exact certainty. It establishes equality for the task of returning that reported field.

Three nonprinting control characters and damaged LaTeX commands were repaired in that reading copy. The original byte-pinned source remains available as historical evidence. Its observational inputs were **not** newly fetched or independently verified here. The example continues to demonstrate an organizational use of task scope and provenance; it does not demonstrate a new physical prediction or superiority over the native pipelines.

An additional typesetting erratum is recorded for BM23-Q1.2: the broken “H satisfying (Q1.1)” subscript should read

\[
\delta_A(N)=\min_{H\text{ satisfying (Q1.1)}}
\max_{U_j^\dagger U_j=I_{n_j}}
\left\|\iota(U)-N^\dagger\phi_H(\iota(U))\right\|.
\]

The surrounding definition and proof already supply this meaning. This repairs display text, not the recovery theorem.

## 4. Every BM entry has a completion disposition

| Inventory disposition | Entries | What remains |
|---|---:|---|
| Explicit definitions | 70 | Instantiate their native data in applications; a definition alone does not prove nonempty realization. |
| Recorded scoped theorems/corollaries/counterexamples | 254 | Retain hypotheses; finish traceable dependency and evidence review. These are registry entries, not 254 independent discoveries. |
| Conditional locality results W13 and W14 | 2 | Check each actual PDE/model's finite-speed, uniqueness, boundary and limiting assumptions. The supplied one-dimensional examples do not discharge every future application. |
| Broad active extension families | 6 | Close the selected native research contracts described below. |
| Optional broad candidates: Seed, Rooting, Rebranching | 3 | Their finite operational versions are supplied separately. Broader universal/canonical meanings require additional specification and proof only if retained as claims. |
| Retired SSH proposal | 1 | Keep retired. It is not an unfinished core theorem. |
| **Total BM entries** | **336** | Every entry is mapped in the readiness JSON. |

There are eight historical B-OPEN-prefixed rows, but only six remain Hypothesis: two finite families have already been resolved while retaining their stable IDs. Counting the prefix alone gives the wrong number of active research families.

This inventory has no BM rows labelled Missing equation. That is a property of its classifications, not a theorem that all desired BM equations or future applications are complete. GURF and Steadman have separate obligations; their unresolved physical or historical work must not be concealed by a BM core status.

## 5. The remaining release work, with acceptance tests

| Work item | Required work | What objectively closes it |
|---|---|---|
| R1. Full proof traceability | Resolve all 128 unenumerated theorem dependency records, review existing lists, identify aliases, imports and source amendments | Every retained result has a precise source statement, assumptions, proof location, direct dependencies or an explicit self-contained proof basis; all cross-references resolve. No alias is counted as a separate proof. |
| R2. Independent mathematical validation | Submit a fixed set of proofs and certificates to independent checking; resolve substantive objections | An attributable review or formal-checker record identifies exactly what was checked, what assumptions were accepted and how each objection was closed. Nothing was sent to reviewers in this turn. |
| R3. Proof-scope reconciliation | Audit all long results for changes of domain, norm, quantifier order, locality, compactness, attainment, regularity and legacy retention | Every cross-sector use cites the bridge hypotheses actually discharged; conjectural applications remain explicitly conditional. |
| R4. Theorem-specific originality | Compare the principal candidate contributions under equivalent formulations, not only BM terminology | A statement-level matrix records exact matches, reductions, differing assumptions/conclusions and unresolved searches. Historical priority is claimed only where evidence supports it. |
| R5. Implementation coverage | Match advertised calculator/solver capabilities to theorems and input contracts; implement general routines only where promised | Each supported mode has a typed schema, error/availability conventions, source linkage, independently computed finite examples and honest rejection of unsupported inputs. “Proved computable” and “implemented” remain different fields. |
| R6. Reproducible release | Assemble the authoritative statements, source hashes, versions, tests, certificates and errata under one stable release manifest | A fresh environment can reproduce the advertised finite outputs from exact supplied inputs; checker versions and expected outputs are pinned. Numerical tests are not represented as general proofs. |
| R7. Demonstrated practical value | Run predeclared comparisons against direct native methods using the same information, constraints, resources and task | A benchmark establishes a concrete benefit or records no benefit. Possible measures include certified state/communication cost, missed-invalid-model rate, runtime, or reproducible analyst decisions. No improvement percentage is presently justified. |
| R8. Historical source recovery, if claiming all-history completion | Recover missing retained DD/lineage statements and the exact frozen GRDE-008 source; reconcile supersessions | Each retained historical ID has original evidence or an explicit exclusion/retirement. New replacement proofs must not be relabelled as recovered history. |

R1–R3 support a stronger checked mathematical release. R4 supports novelty claims; R7 supports comparative usefulness claims. R8 is necessary for a complete-history claim, not for every scoped V1 theorem. R5's scope is determined by what the software actually promises.

This audit attempted targeted source searches and one simpler retry for the DD/GRDE material; both returned no matches. That is a retrieval limitation, not proof that the source files do not exist. No historical statement was reconstructed from memory.

## 6. The six active research families

### E1. Unrestricted nonlinear Jordan interior optima

The continuous n=3 scalar case is already solved. Long-return endpoints are classified for every chain length. For the four-state, scalar, unit-coupling/unit-horizon L² trajectory contract, the currently certified **squared-error** interval is

\[
\frac{4+\sqrt{13}}6\le e_*^2\le1.2949.
\]

The lower endpoint is approximately 1.267591879244, so the remaining interval width is approximately 0.027308120756 in squared-error units. The separate interval [1.2948,1.2949] applies only to the specified cubic invariant encoder family with its fixed decoder. It cannot be used as the general lower bound.

**Close the four-state question:** give an admissible globally continuous scalar code R and a decoder achieving a value, and prove the matching lower bound for every permitted code/decoder, or prove a limiting infimum and its attainment/nonattainment correctly. Exact sampled autonomy is global on R⁴, while performance is measured on the unit ball; replacing global closure by closure only on that ball changes the question. The arbitrary single-valued reduced update F and fixed h>0 retain the published contract. Other interior n,d cases need their own identified claims.

**Next decisive work:** characterize the surviving continuous quotient after the forced return identifications, then optimize decoder radii on its fibres. Another polynomial example or sampled optimization alone cannot close the unrestricted lower-bound problem.

### E2. Global regular realization and least augmentation

Existing constructions and special-family minima are already proved. A universal terminating exact minimum-dimension algorithm for arbitrary computable smooth inputs has been ruled out.

**Required problem data:** source space, admissible native states, tasks, legacy map, target category, regularity class, decoder/update requirements and allowed augmentations.

**Closure:** produce a realization with an explicit dimension upper bound and a matching obstruction below it, or prove nonexistence in the specified class. Local rank bounds alone do not settle global topology, singular fibres, Hausdorffness or smooth quotient existence. Algebraic input contracts must not inherit undecidability conclusions intended for arbitrary computable-real inputs, or vice versa.

### E3. Constrained and infinite-horizon causal realization

The specified finite deterministic all-output minimax contract is solved. History-carrying predictors and closed current-state encoders have different feasible sets. Effective uniform-decay classes also have finite predictor constructions.

**Required problem data:** native state/actions, initial states, task metric, horizon, available initialization information, allowed history, code/output/update class, partial availability, tolerance and cost.

**Closure:** a necessary-and-sufficient feasibility characterization plus an optimizer or certified bounds within that native class; otherwise a proved obstruction. Additional distributed, smooth, stochastic or physical constraints are new premises, not consequences of the finite set theorem. Universal additive approximation for all bounded computable infinite presentations is already impossible; it must not remain on a list of achievable coding tasks.

### E4. Quantum recovery formulas and implementation

Finite algebraic recovery/capability formulations and terminating real-algebraic procedures are proved. Real-rational label-channel certificates are implemented. General elimination has not been implemented or run. Several qubit, full-algebra and other specific contracts have already been resolved.

**Required problem data:** dimensions, exact Kraus entries, supplied observable-algebra embedding, the original unamplified operator norms, any fixed-rank/channel constraints, and whether one common recovery must serve multiple tasks.

**Closure for a selected unsolved class:** evaluate its optimal error or envelope with a matching bound and a lawful CPTP witness; state whether extrema are attained. For a general-software claim, supply an actual implementation and replayable algebraic certificates. A finite Choi formulation does not itself make a numerical solver exact, and a floating-point SDP estimate does not certify its dual slacks.

### E5. Nonlinear optimal repair outside the solved classes

Coupled/triangular constructions and compact algebraic repair have scoped results. Small residual alone does not imply small repair under arbitrary nonlinear dynamics.

**Required problem data:** domain, native flow, norm and time horizon, encoder/decoder regularity, allowed repairs, compactness/coercivity or other existence conditions, and effective input descriptions.

**Closure:** prove existence or nonexistence of an admissible repair, give an effective residual-to-repair modulus with its parameter dependence, and certify optimality or declared approximation error for the chosen cost. Separate attainment from an unattained infimum. Resonance and loss of regularity need explicit treatment rather than a silent change from C² to C¹.

### E6. Additional infinite-dimensional native theories

Uniformly decaying effective tasks already admit a finite response-tree construction, including a noncommuting Hilbert-space example. This does not cover every forced, non-decaying, nonlinear PDE or infinite quantum-channel problem.

**Required problem data:** carrier and topology, solution domain and existence/uniqueness, boundary conditions, forcing, task regularity, effective finite observations, an independently proved tail/decay estimate, and computable constants.

**Closure:** prove native well-posedness and a finite truncation/prediction bound at the requested tolerance, with a lawful initialization and update construction. If inverse recovery is requested, separately characterize nonuniqueness and conditioning. Finite modal checks cannot replace a uniform tail estimate or justify interchanging limits. The uniform-decay theorem requires its supplied decay bound; fitting a few trajectories cannot certify that premise.

## 7. Demands that should not be treated as pending achievable work

| Demand | Correct disposition |
|---|---|
| Recover a task distinction destroyed by the only available deterministic observation | Impossible under T01; change the observation, scope or tolerance explicitly. |
| Infer one uniquely indispensable Branch from a single failed reduction | Invalid inference; quantify over the independently declared alternatives. N1–N2 now implement that test in a finite contract. |
| Assign an absolute Branch count without equivalence/irreducibility rules | Unsupported; T15 gives a regrouping counterexample. |
| Compute exact future equivalence on every computable infinite presentation | Ruled out by the existing reduction. Select a restricted effective class. |
| Universally approximate infinite-horizon predictor optimum to the stated fixed additive tolerance | Ruled out by BM23-I2. A bounded output task alone is insufficient. |
| Obtain a universal exact smooth minimum-dimension algorithm | Ruled out in the specified computable-input class. |
| Deduce general physical laws or information conservation from set-theoretic injectivity | Requires separate physical hypotheses and evidence. |
| Prove BM is the only framework that can supply necessary structure | No such conclusion follows from the necessity proofs, and it is not a prerequisite for mathematical validity. |

Negative results close the corresponding universal questions negatively. They do not supply positive implementations and do not settle every restricted native case.

## 8. Verification sequence and completion claims

The next proof-audit order should be: finish source/dependency mapping; check the principal general results independently; resolve scope changes and counterexamples; then make result-specific novelty and benchmark claims. The six research families should proceed as explicit native contracts with lower and upper certificates, not as indefinite requests to solve all mathematics.

For the current release, the defensible statement is:

> BM has an internally established, contract-scoped foundation that proves when distinctions and additional structure are necessary. It has several solved extensions and executable finite certificates. Its full proof traceability, independent validation, broader originality assessment, historical archive and six identified research families are not all complete.

No completion percentage is given: a count of definitions, aliases, theorems, optional proposals and broad research programs has no justified common denominator. Nor is there evidence for a calendar estimate for the unresolved proofs.

## 9. Package contents and reproducibility

* `BM_Completion_Requirements_2026-10-23.md`: this full completion specification.
* `BM_Necessity_and_Comparison_2026-10-23.md`: proofs N1–N4, worked cases, exact foundational comparison and primary references.
* `BM_Canonical_Dependency_Map_2026-10-23.md`: all T01–T55 direct proof bases.
* `BM_Completeness_Readiness_2026-10-23.json`: all 645 original entries plus the 336-entry BM readiness supplement, source hashes and audit amendments.
* `BM_Necessity_Analyzer_2026-10-23.py`: finite exact analyzer and certificate replay checker.
* `BM_Necessity_Verification_2026-10-23.py`: separate exhaustive-partition oracle and adversarial checks.
* `BM_Necessity_Examples_2026-10-23.json`, `BM_Necessity_Certificates_2026-10-23.json`, `BM_Necessity_Verification_2026-10-23.json`: eight examples, their outputs and test results.
* `BM_Benchmark_Reading_Corrections_2026-10-23.md`: explicitly labelled correction of the historical benchmark.
* `BM_Readiness_Verification_2026-10-23.json`: coverage and dependency metrics.
* The ZIP also contains the 23 original source snapshots, the baseline inventory, build script and checksum manifest, so the audit can be inspected without recovering this conversation.

The earlier website/calculator regression run remains separate evidence: 23,988 assertions and 932 internal-link checks were recorded for that deployment. Those tests were not counted again as new work here. This package's new necessity tests do not change their scope.

Primary references for the external comparison are linked in the companion proof note: Rutten (2000), Paige–Tarjan (1987), Benveniste et al. (2018), Cousot–Cousot (1977), and Bény (2009). The N4 correspondence is proved in this package; the broader historical-priority question remains open.


---

Source: BM_Canonical_Dependency_Map_2026-10-23.md

# BM canonical proof-dependency map

23 October 2026. Internal source-level review of T01–T55. A blank prior-theorem list below means that the written argument is self-contained at this level, not that it uses no ordinary mathematics. External review and formal verification are separate.

| ID | Result | Direct numbered proof dependencies | Proof basis / restriction |
|---|---|---|---|
| T01 | Exact fibre factorization | None required by this short argument | Well-defined factorization on realized fibres; no representative choice or regularity assumption. |
| T02 | Passport sufficiency | T01 | Substitution of the Passport observation map into fibre factorization. |
| T03 | Completion fibre sufficiency | T01 | Product observation fibres are intersections; nonempty realized fibres only. |
| T04 | Canonical exact task quotient | T01 | Intersection of equivalences and fibre factorization; set-level quotient. |
| T05 | Finite exact carrier bound | None required by this short argument | Surjection between finite realized images; equal cardinality gives a bijection. |
| T06 | Parallel observation refinement | None required by this short argument | Coordinatewise equality of ordered pairs. |
| T07 | Deterministic serial information loss | T01 | Function substitution and the necessity half of fibre factorization. |
| T08 | Structured quotient criterion | None required by this short argument | Domain saturation and representative-independent finite-arity output classes. |
| T09 | Typed composite domain | None required by this short argument | Successive definedness tests; associativity on the actual composite domain. |
| T10 | Future task factorization for a declared evolution | T01 | Tagged task factorization; evolution and existence interval are supplied. |
| T11 | Exact Dynamic Closure | T01, T10 | Factorization of Rf, finite induction, and tagged partial availability. |
| T12 | Static sufficiency does not imply closure | T11 | Explicit two-state witness embedded in R². |
| T13 | Branch essentiality monotonicity | None required by this short argument | Universal quantification over one fixed independently specified candidate class. |
| T14 | Refinement and composition | None required by this short argument | Composition and identities of supplied factoring maps; composition types stated separately. |
| T15 | Branch count need not be invariant | None required by this short argument | Bijection between product state descriptions with different raw Branch counts. |
| T16 | Finite tree gluing | None required by this short argument | Finite rooted-tree extension using equal edge images. |
| T17 | Local realizability does not imply global realizability | None required by this short argument | Three explicit Boolean constraints with pairwise witnesses and joint contradiction. |
| T18 | Finite deterministic DAG evaluation | None required by this short argument | Finite DAG topological ordering and deterministic evaluation induction. |
| T19 | Quantifier scope matters | None required by this short argument | Two-element quantifier-order counterexample. |
| T20 | Separate feasibility does not imply joint feasibility | None required by this short argument | Two disjoint nonempty singleton realization sets. |
| T21 | Root receiver relativity | None required by this short argument | Two explicitly different receiver acceptance sets. |
| T22 | Root acceptance is not automatically transitive | None required by this short argument | Explicit translating sign change; T43 is context, not a proof dependency. |
| T23 | Existence does not provide a canonical selection | None required by this short argument | Two-element symmetry has no fixed point; invariant choice obstruction. |
| T24 | Path coherence transitivity | None required by this short argument | Pointwise transitivity on one declared common comparison domain. |
| T25 | Cyclic separator consistency can fail globally | None required by this short argument | Boolean equality path and inconsistent closing edge; T44 is context only. |
| T26 | Finite serial Passport defect localization | None required by this short argument | First true-to-false transition in a finite Boolean sequence; equality needs absorbing failure. |
| T27 | Exact repair refinement | T06 | Product observation kernel identity from T06. |
| T28 | Repair closure and revalidation | None required by this short argument | Closure-operator axioms; coordinate replacement on a finite full product only. |
| T29 | Finite Markov closure | None required by this short argument | Point-mass necessity; block sums define a nonnegative normalized reduced kernel. |
| T30 | Markov test-function composition | None required by this short argument | Kernel integration: indicators, simple functions, monotone convergence and signed decomposition. |
| T31 | Exact task diameter criterion | T01 | Metric zero-distance equality plus fibre factorization. |
| T32 | Two-sided reconstruction bound | None required by this short argument | Triangle inequality, optional fibre section, and bounded-real midrange. |
| T33 | Lipschitz serial error propagation | None required by this short argument | Triangle inequality and stated Lipschitz bounds at every compared point. |
| T34 | Periodic incompressible energy identity | None required by this short argument | Smooth periodic integration by parts and divergence-free identities. |
| T35 | Wilson-loop gauge invariance | None required by this short argument | Ordered matrix cancellation and cyclicity of trace. |
| T36 | Sector non-portability | None required by this short argument | Explicit discrete-to-usual-topology example; no automatic continuous decoder. |
| T37 | Realization monotonicity | None required by this short argument | Satisfaction of a larger obligation set implies satisfaction of a subset. |
| T38 | Independent Configuration product | None required by this short argument | Independent factor obligations and a genuinely product interpretation space. |
| T39 | Single-cycle holonomy | None required by this short argument | Ordered group telescoping and recursive potential construction. |
| T40 | Fundamental-cycle criterion | None required by this short argument | Spanning-tree potential construction and fundamental-cycle equations; T39 gives notation. |
| T41 | One-step approximate lumpability | None required by this short argument | Finite aggregated probability rows and convexity of half the l1 norm; T29 gives setting. |
| T42 | Multi-step approximate lumpability | T41 | T41 plus stochastic total-variation contraction and induction. |
| T43 | Certified Root transfer | None required by this short argument | Membership in a declared acceptance-set image inclusion. |
| T44 | Join-tree hypergraph gluing | None required by this short argument | Finite join-tree tuple extension using running intersection. |
| T45 | Scope erasure obstruction | None required by this short argument | Same constant representation with two different task scopes. |
| T46 | Receiver information order | T01 | Task-kernel intersections and the induced factorization from T01. |
| T47 | Receiver sufficiency modulus | T01, T32 | T32 applied to the product task with extended sup distance; T01 for zero error. |
| T48 | Quantitative Root transfer | None required by this short argument | Triangle inequality and translator Lipschitz bound. |
| T49 | Relational cycle criterion | None required by this short argument | Definition of finite relational composition with a diagonal endpoint witness. |
| T50 | Satisfaction-preserving Configuration maps | None required by this short argument | Identities and composition of supplied satisfaction-preserving morphisms. |
| T51 | Configuration refinement preorder | None required by this short argument | Set inclusion and quotient by equality of realization families. |
| T52 | Acceptance does not determine an adjunction | None required by this short argument | One-object category hom-set cardinality counterexample to an inferred adjunction. |
| T53 | Mixed deterministic and stochastic continuation | T29 | Explicit joint block-probability formula followed by T29. |
| T54 | Relational exact task factorization | T01 | Incidence-pair fibre factorization; empty successor fibres need separate availability. |
| T55 | Exact relational Dynamic Closure | T01 | Factorization of a power-set-valued successor-image map; empty set preserved. |

Source: pinned `Branch_Mathematics_Research_Edition_2026-09-15.md`, identifier R. Section positions and SHA-256 hashes appear in the readiness JSON. The section text was inspected, but this is not a proof-assistant transcript. No contradiction was identified in these short arguments; no assertion about all remaining general proofs follows.


---

Source: BM_Benchmark_Reading_Corrections_2026-10-23.md

# Reading correction to the historical BM/GURF benchmark

23 October 2026. This reading copy corrects escaped mathematical text, restores the mass-equivalent factor E_rad/c², identifies rounded reporting labels, and distinguishes FAR upper limits from measured rate ratios. The underlying September input snapshot is retained; its GWOSC records were not re-fetched or independently revalidated in this correction. The original byte-pinned source BEN remains historical evidence. The newer exact comparison is in BM_Necessity_and_Comparison_2026-10-23.md.

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
- ratio of the largest to smallest displayed FAR upper limits = 1630
- span of those displayed FAR upper limits = 3.212 decimal orders of magnitude

The source reports the same displayed p_astro field for all three pipelines. This identifies the reported labels, not unrounded underlying probabilities:

\[
p_{\mathrm{astro,reported}}^{cWB}=p_{\mathrm{astro,reported}}^{GstLAL}=p_{\mathrm{astro,reported}}^{PyCBC}=1.0.
\]

### BM interpretation

This is a valid real-data example of receiver-relative Task equivalence:

different native Branch scores can belong to the same fibre of the task “return the displayed p_astro label.” This alone does not prove equality of latent probabilities, exact posterior certainty, or equivalence for every detection task. Ratios of FAR upper limits do not determine ratios of actual false-alarm rates.

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
\Delta_M=m_1+m_2-M_f-\frac{E_{rad}}{c^2}
\]

gives, using the stated decimal inputs exactly,

\[
\Delta_M=(35.6+30.6-63.1-3.1)M_\odot=0,
\]

a zero residual of the supplied rounded central values. The previously reported residual near 10⁻¹⁵ is floating-point roundoff, not measurement accuracy or a bound on physical energy nonconservation.

The source chirp mass reconstructed from the two central component masses is

\[
\mathcal M
=
\frac{(m_1m_2)^{3/5}}{(m_1+m_2)^{1/5}}
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

about 0.073 of the average quoted 90% half-width. This is a descriptive normalization, not a significance level or an uncertainty propagation result; nonlinear parameter summaries and correlated posteriors need their own analysis.

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
(\text{event},\text{pipeline},\text{catalog version},\text{waveform family},\text{parameter product})
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
\boxed{\text{PASS as framework validation; NOT YET a distinctive BM leverage result.}}
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


---

Source: BM_Necessity_Existence_and_Mechanical_Research_2026-10-24.md

# Branch Mathematics: necessity, constructive existence, and mechanical tests

24 October 2026. Additive research note for the frozen BM V1 / Edition 1.1 foundation. DR1–DR7 are local labels, not replacements for canonical theorem identifiers. Proofs and computations here have received internal checking only. No historical novelty, independent review, or new physical law is claimed.

## What this investigation establishes

BM has a defensible mathematical purpose: identify which distinctions and compatibility conditions a declared task requires, demonstrate when available representations cannot preserve them, and construct or reject a repair. This investigation strengthens that purpose with noisy-observation criteria, exact repair dimensions, sharp error bounds, and a mechanical example suggested by the user.

The strongest additional mechanical result is simple: **position, energy, and angular momentum together need not determine the next position.** Two Newtonian orbital states can agree on all three and differ in whether they are moving inward or outward. The missing distinction produces a rigorous prediction obstruction.

Three claims have different evidence requirements:

| Claim | Evidence supplied here | Limit |
|---|---|---|
| Some distinctions or structures are necessary | Explicit pairs of indistinguishable inputs, separating futures, error lower bounds, and an incompatible collection of constraints | Relative to a stated task, observation set, model class, and tolerance |
| Declared BM configurations have mathematical realizations | Explicit finite quotients, linear state realizations, and mechanical models satisfying their declared obligations | Constructive existence for these configurations, not a consistency proof for every proposed extension |
| BM offers value beyond independently using established theories | A common record of information, evolution, noise, interventions, and global compatibility | Comparative workflow advantage and historical originality remain unestablished |

The literature independently establishes the importance of these problems. It does not establish that BM is the only framework capable of addressing them. Existing methods should be incorporated and credited wherever they already answer the question.

## 1. Primary research that changes the assessment

The following comparison uses original papers or author manuscripts, not promotional summaries. The search is targeted, not an exhaustive priority review.

| Research | What it establishes in its own scope | Consequence for BM |
|---|---|---|
| Shalizi and Crutchfield, computational mechanics [CM] | Causal states group histories by their predictive distributions; the paper proves predictive sufficiency, minimality, and uniqueness results | BM's deterministic future equivalence has a close established predictive analogue. Stochastic equivalence needs conditional distributions and its own assumptions. |
| Chorin, Hald, and Kupferman, optimal prediction and Mori–Zwanzig [MZ] | Eliminating unresolved variables leads to projected equations with memory and an unresolved contribution | Supports BM's distinction between present output and autonomous reduced state. Memory is an established repair mechanism; it is not a missing new force. |
| Ovchinnikov and colleagues, CLUE [CLUE] | Computes minimal constrained linear lumpings for polynomial differential equations, preserving specified linear observables | A direct comparison method for BM's exact reductions. A linear observability calculation alone cannot establish novelty. |
| Ettehad and Foucart, recovery with observation errors [OR] | Constructs optimal recovery maps under bounded noise; Theorem 4 covers linear functionals and includes DR4 below as a specialization | The robust error formula should be credited to optimal recovery. BM can connect it to a declared future task and a repair decision. |
| Foucart and Liao, intersected hyperellipsoids [OR24] | Gives radius-of-information and optimal-recovery results for two quadratic constraints, including inaccurate data | Supplies a more powerful baseline for future vector-valued BM repair solvers. Extending a two-constraint conclusion to arbitrary constraints requires proof. |
| Beckers and Halpern [CA]; Beckers, Eberhardt, and Halpern [CAA] | Define exact and approximate causal abstractions with explicit intervention requirements | Agreement on passive observations does not by itself establish an intervention-preserving bridge. |
| Abramsky and Brandenburger [GL] | Relates contextuality to obstructions to global sections, with explicit measurement and probability structures | Gives a precise comparison for BM's local-versus-global realization obligations. The Boolean example here is a classical constraint example, not experimental quantum evidence. |

These comparisons support the **need to handle the obligations**. They also narrow the originality question: the contribution to investigate is a useful, precise coordination of obligations across native sectors, with certificates and repairs. It is not that prediction, memory, observability, or gluing were previously unknown.

## 2. DR1 — constructive existence with imperfect observations

Let X be a nonempty state set, with a set of partial deterministic actions f_a and required task O. Adjoin an absorbing unavailable state ⊥, tagged differently from every legitimate task value. Write x E_* y when every finite action word gives the same tagged task from x and y. This includes the empty word and the availability of each continuation.

Replace a perfect observation V(x) by a nonempty set Γ(x) of possible observed values. No distribution is assumed. An initializer h(z) must work for every z in Γ(x), and its deterministic autonomous updates must reproduce every required task and action availability. It cannot obtain further measurements after initialization under this contract.

**Theorem.** Such a set-valued-noise-robust exact implementation exists if and only if

\[
\boxed{\Gamma(x)\cap\Gamma(y)\ne\varnothing\ \Longrightarrow\ xE_*y.}
\tag{DR1}
\]

When it exists, the smallest cardinality of the realized code set is |X/E_*|.

**Proof.** If a common measurement z is possible from two states, the initializer supplies the same code h(z). Deterministic execution gives identical future tasks and availability, so the states must be E_*-equivalent. Conversely, when the condition holds, assign each realized measurement z the unique E_* class of its compatible states. Equality of all future tasks makes the class update and output maps well defined, including partial-action domains. This constructs a correct implementation. Any correct implementation must use distinct codes for different future classes, because a shared code would give identical future behavior. Choosing one possible measurement for each class gives the cardinal lower bound, attained by the quotient construction. ∎

This permits different noisy measurements of one state to initialize the same quotient class. It does not assert a continuous or computable initializer, and it does not treat fresh observations, filtering, randomized risk, or physical hardware without additional structure.

**Finite certificates.** A negative certificate consists of x, y, a common possible measurement z, and a finite action word with unequal tagged outputs. A positive certificate specifies quotient outputs, action tables, and the class assigned to each realized measurement. The supplied verifier compares the criterion with an independent enumeration of all native congruence partitions for small systems.

**BM interpretation.** This supplies nontrivial positive realizations as well as impossibility witnesses. A framework that only declares failures would be weaker; DR1 says exactly when this particular repair exists.

## 3. DR2 — positive noise changes what “complete” can mean

Assume X is connected, V:X→R^m is continuous, and Γ(x) is the closed Euclidean ball of a fixed radius η>0 around V(x).

**Corollary.** A robust exact implementation under DR1 can exist only if every state has the same required future task-and-availability profile.

**Proof.** Each x has a neighborhood in which ||V(y)−V(x)||<2η. The two measurement balls then intersect, so DR1 forces y E_* x throughout that neighborhood. Thus every E_* class is open. Its complement is a union of open classes, hence is also open. Connectedness permits only one nonempty class. ∎

This is not an objection to useful measurement. It says that worst-case exactness for a nonconstant continuous-state task cannot be promised under a positive bounded-noise model. One must state a tolerance, change the admissible state set, or change the observation assumptions. Simply adding finitely many ordinary continuous noisy channels does not remove this obstruction if the resulting observation set still contains a fixed positive-radius ball.

Discrete states with adequately separated observation sets can still satisfy DR1. The connectedness and noise-interior assumptions are substantive.

## 4. DR3 — quantify the missing information for linear evolution

Let ẋ=Ax on R^n, with required future output L exp(tA)x for every t≥0 and available noiseless observation Bx. Define

\[
\mathcal O_L=\begin{bmatrix}L\\LA\\\vdots\\LA^{n-1}\end{bmatrix}.
\]

The future-invisible differences form ker O_L. If every future output of a difference vanishes, its derivatives at zero give LA^k x=0. Conversely, Cayley–Hamilton makes every higher power a combination of the first n powers; the exponential series then gives vanishing at all times.

An exact autonomous code computed only from Bx exists if and only if

\[
\boxed{\ker B\subseteq\ker\mathcal O_L}
\quad\Longleftrightarrow\quad
\operatorname{row}\mathcal O_L\subseteq\operatorname{row}B.
\tag{DR3a}
\]

Necessity holds even if arbitrary deterministic encoders are allowed. For sufficiency, choose a matrix Q whose rows form a basis of row O_L. This row space is A-invariant; therefore QA=HQ and L=DQ for suitable matrices H,D. Then z=Qx obeys ż=Hz and has output Dz. If DR3a holds, Q=KB for some K, so initialization uses only the available observation.

The minimum dimension among linear exact codes is rank O_L: any exact linear code must determine all rows of O_L, and Q attains the bound.

If additional arbitrary noiseless linear scalar observation channels may be installed, their minimum number is

\[
\boxed{k_{\min}=\operatorname{rank}\begin{bmatrix}B\\\mathcal O_L\end{bmatrix}
-\operatorname{rank}B.}
\tag{DR3b}
\]

Each new row can increase the available row-space dimension by at most one. Conversely, a basis for the image of row O_L modulo row B supplies exactly that many rows. This proves both bounds.

This is classical observability and linear algebra expressed as a BM repair contract. It does not solve selection from a restricted sensor catalogue, sensor placement costs, noisy recovery, or nonlinear code dimension. If B itself must remain recoverable, replace the task L by the stacked task [L;B] before forming the observability stack.

## 5. DR4 — an exact error floor, including every nonlinear decoder

Normalize the admissible state set to ||x||₂≤1. Measure z=Bx+e with ||e||₂≤η. The task is the scalar ℓᵀx. Define

\[
e_* = \inf_d\ \sup_{\|x\|\le1,\ \|e\|\le\eta}
|\ell^Tx-d(Bx+e)|,
\]

where d ranges over all deterministic decoders. Then

\[
\boxed{
e_*=\max_{\|v\|\le1,\ \|Bv\|\le\eta}|\ell^Tv|
=\min_a\bigl(\|\ell-B^Ta\|_2+\eta\|a\|_2\bigr).
}
\tag{DR4}
\]

**Proof.** For each feasible v, the states ±v with errors ∓Bv both produce measurement zero. At least one error of any common decoded value is at least |ℓᵀv|. For η>0, equip pairs (x,e) with norm max(||x||,||e||/η). On the kernel of the map (x,e)↦Bx+e, the functional (x,e)↦ℓᵀx has norm equal to the displayed maximum. Hahn–Banach extends that restricted functional with the same norm. Every such extension differs from ℓᵀx by a functional aᵀ(Bx+e); its norm is ||ℓ−Bᵀa||+η||a||. The decoder d(z)=aᵀz therefore attains the lower bound. For η=0, orthogonally project ℓ onto row B; the residual norm equals the maximum on the unit ball in ker B. ∎

DR4 is explicitly a special case of [OR], Theorem 4: take its native space to be Euclidean, its approximating subspace V={0}, its model radius ε=1, and its noise exponent p=2. The proof here makes the witness and BM interpretation explicit; it is not a priority claim.

For a fixed finite family of scalar tasks with the maximum absolute-coordinate loss, solve each coordinate problem; the optimum is the maximum of their values. This does not automatically construct a dynamically consistent trajectory or a physically admissible vector output. Those are additional receiver requirements.

**Exact arithmetic example.** Set B=[1,0], ℓ=(4/5,3/5), η=3/5. The pair v=±(3/5,4/5) gives a lower bound 24/25. The linear decoder coefficient a=7/20 gives residual norm 3/4 and noise contribution 21/100, totaling 24/25. The companion script checks the matching rational certificate.

## 6. DR5 — oscillator benchmark: sufficiency, noise, and sampling

For a harmonic oscillator with known ω>0, use the normalized state (q,p), where p=v/ω. Choose a common displacement scale so q²+p²≤1 is dimensionless. The equations are

\[
\dot q=\omega p,\qquad \dot p=-\omega q,\qquad
q(t)=q_0\cos\theta+p_0\sin\theta,\quad\theta=\omega t.
\]

### Current position alone

Measuring z=q₀+e with |e|≤η gives the exact minimum worst-case error for predicting q(t):

\[
e_q(\theta,\eta)=
\begin{cases}
1,&\eta\ge|\cos\theta|,\\
|\cos\theta|\eta+|\sin\theta|\sqrt{1-\eta^2},&0\le\eta<|\cos\theta|.
\end{cases}
\tag{DR5a}
\]

The second case necessarily has η<1. To prove the formula, apply DR4 and maximize c u+s√(1−u²) over 0≤u≤min(η,1), where c=|cos θ| and s=|sin θ|. Its unconstrained maximum occurs at u=c. At zero noise, e_q=|sin θ|. At a quarter period, even perfect present position leaves worst-case future error one.

### Add one actual historical position measurement

With h≥0 and α=ωh, the two observations satisfy

\[
\begin{bmatrix}q(0)\\q(-h)\end{bmatrix}
=B_h\begin{bmatrix}q_0\\p_0\end{bmatrix},\qquad
B_h=\begin{bmatrix}1&0\\\cos\alpha&-\sin\alpha\end{bmatrix}.
\]

This history must actually be available. It cannot be inferred from current position alone. The matrix is invertible exactly when sin α≠0; its squared singular values are 1±|cos α|.

For total two-measurement error ||e||₂≤η, the exact optimum for recovering the whole normalized state in Euclidean norm is

\[
e_{\rm state}=
\begin{cases}
\min\{1,\eta/\sqrt{1-|\cos\alpha|}\},&\sin\alpha\ne0,\\
1,&\sin\alpha=0.
\end{cases}
\tag{DR5b}
\]

**Proof.** Along a unit weakest right singular vector, take v with norm min(1,η/σ_min). The states ±v can produce the same zero measurement, proving the lower bound. Inversion gives error at most η/σ_min; the zero estimate gives error at most one. Use whichever bound is smaller. If the state estimate must remain in the unit disk, project the inverse estimate onto the disk; Euclidean projection cannot increase its distance from any admissible true state. At rank deficiency a unit kernel vector proves error one, attained by the zero estimate. ∎

The estimated state then follows the genuine oscillator dynamics. Rotation preserves its error, and

\[
\sup_{t\ge0}|q_x(t)-q_{\hat x}(t)|=\|x-\hat x\|_2.
\]

Thus DR5b also solves the full-future position problem when the output must be a single lawful oscillator trajectory. This avoids relying on incompatible coordinate-by-coordinate answers.

For η=0.1, with T=2π/ω:

| Sample spacing h/T | Minimum worst-case state error |
|---:|---:|
| 0.01 | 1.000000 |
| 0.05 | 0.452015 |
| 0.10 | 0.228825 |
| 0.25 | 0.100000 |
| 0.49 | 1.000000 |
| 0.50 | 1.000000 |

An arbitrarily small nonzero gap can make the noiseless matrix invertible while leaving noisy recovery nearly useless. Quarter-period spacing is optimal under this normalization and fixed total noise norm. It is not a universal prescription for unknown frequency, damping, correlated errors, or a fixed measurement-time budget.

### The task can remove the need for a distinction

If the task requests position only at multiples of half a period, q(nT/2)=(-1)^n q₀. Position alone then has an exact autonomous sampled update q↦−q. Velocity remains necessary for the full continuous future, but is unnecessary for this sampled task. This is a direct test of BM's receiver-relative essentiality; a universal claim that “velocity must always be retained” would be false.

## 7. DR6 — the user's orbit and ice-skater example

### What is conserved, and what changes

For a skater with negligible external torque, angular momentum is L=Iω. Pulling mass inward reduces I, so ω increases. Rotational kinetic energy is

\[
K_{\rm rot}=\tfrac12 I\omega^2=\frac{L^2}{2I}.
\]

It therefore increases as I decreases at fixed L. The skater's work supplies the increase; chemical energy is converted into mechanical energy. This is the standard analysis in [PHY1]. Conservation of angular momentum does not imply conservation of rotational kinetic energy.

For a Newtonian test mass in a fixed central field μ=GM, angular momentum per unit mass is h=r v_θ, so v_θ=h/r and angular speed is h/r². These formulas concern the transverse component. Total speed also includes radial motion. The specific mechanical energy is

\[
\varepsilon=\tfrac12(\dot r^2+h^2/r^2)-\mu/r.
\tag{DR6a}
\]

As a body moves inward along one unforced Kepler orbit, gravitational potential energy decreases and kinetic energy increases while ε remains constant. Along a bound orbit of semimajor axis a, rearranging ε=−μ/(2a) gives v²=μ(2/r−1/a). Kepler's changing orbital speed is documented in [PHY2].

For example, in normalized units μ=1, an ellipse with a=1 and eccentricity 3/5 has:

| Quantity per unit orbiting mass | Apoapsis | Periapsis |
|---|---:|---:|
| Radius | 8/5 | 2/5 |
| Speed | 1/2 | 2 |
| Angular momentum h | 4/5 | 4/5 |
| Kinetic energy | 1/8 | 2 |
| Gravitational potential energy | −5/8 | −5/2 |
| Total mechanical energy | −1/2 | −1/2 |

The kinetic gain 15/8 exactly matches the potential decrease. Energy has changed form. Comparing two different circular orbits is a different operation: circular speed scales as r^(−1/2), and transferring between those orbits changes the orbital energy and angular momentum. It is not the fixed-h contraction formula.

### A rigorous necessity witness for BM

Take μ=1 and the two planar states

\[
x_-=(\mathbf r=(1,0),\mathbf v=(-1/2,1)),\qquad
x_+=(\mathbf r=(1,0),\mathbf v=(1/2,1)).
\]

Both have the same position, specific angular momentum h=1, and specific energy ε=−3/8. Let the retained representation be

\[
R(x)=(\mathbf r,\varepsilon,h).
\]

Then R(x_-)=R(x_+), but their initial radius derivatives are −1/2 and +1/2. The native vector field is smooth away from collision, so uniqueness gives two locally defined trajectories whose radii differ for all sufficiently small positive times. More precisely,

\[
r_+(t)-r_-(t)=t+o(t).
\]

Any radius predictor initialized only from R must issue the same prediction for both states. Its worst error is therefore at least |r_+(t)−r_-(t)|/2, with asymptotic ratio to t at least 1/2.

The numerical illustration gives a radius separation of about 0.0998326673 at normalized t=0.1, hence a lower-bound illustration of 0.0499163336. These decimals are numerical, not interval-certified constants. The exact initial witness and derivative argument establish the impossibility independently of integration.

**Repair.** Retain (r,φ,u,h), where u=dr/dt. On r>0 the native reduced equations are

\[
\dot r=u,\qquad \dot\phi=h/r^2,\qquad
\dot u=h^2/r^3-\mu/r^2,\qquad \dot h=0.
\tag{DR6b}
\]

They are autonomous and determine the position task. Away from turning points, energy and h recover |u| but not its sign. An instantaneous sign label alone is not a complete smooth evolution law through turning points; retaining u with DR6b gives a regular repair on r>0. This is familiar phase-space mechanics, now accompanied by an explicit certificate showing why the proposed smaller representation fails.

### Spin's gravitational effect is a separate question

Orbital angular momentum, a body's rotation about its own axis, and angular momentum's contribution to relativistic gravity are distinct. Ordinary attraction remains for a nonrotating mass. Source rotation adds frame dragging in general relativity; Gravity Probe B tested that effect [PHY3]. In the weak-field far zone the characteristic spin-precession scale is GJ/(c²r³), with direction and numerical factors depending on the observable [PHY4, equation 33, leading angular-momentum moment]. Its falloff should not be substituted for the Newtonian mass-acceleration law GM/r²; the two quoted quantities even have different units.

The ice-skater analogy therefore supports a precise conservation-law comparison. It does not demonstrate that spin creates gravity, that energy increases without a source, or that BM supplies a new gravitational field equation.

## 8. DR7 — independent failures of interventions and joint realization

### Passive equivalence can hide an intervention distinction

Consider two deterministic structural causal models with binary exogenous U:

- M₁: X=U and Y=X.
- M₂: Y=U and X=Y.

Both give (X,Y)=(U,U) in passive observations. At U=1, an intervention do(X=0) produces Y=0 in M₁ and Y=1 in M₂. Thus any predictor supplied only the passive observation (1,1), while both models remain admissible, cannot determine this intervention response. Its worst absolute error for Y is at least 1/2. A model-discriminating assumption or experiment is required. Assigning a probability without justification does not remove the worst-case ambiguity.

This is an elementary causal-identifiability example, consistent with the intervention-sensitive abstraction requirements in [CA, CAA]. It supplies no evidence that either model describes an actual physical system.

### Every local piece can be satisfiable while the whole is not

Let a,b,c be Boolean. Three native constraints are a=b, b=c, and a≠c. Every individual constraint has four assignments, and every pair has two assignments. All three together have zero. Projection onto each shared single variable permits both values, so compatibility at that limited interface also fails to detect the global contradiction.

The complete set of three constraints is a minimal unsatisfiable core. A repair must change a declared constraint or the allowed interpretation; merely joining locally accepted results does not produce a realization. This illustrates BM's nonemptiness obligation. It is already expressible in constraint satisfaction and local-to-global mathematics; [GL] supplies a richer comparison under its own measurement assumptions.

These examples prevent a one-test definition of “complete.” Present observation, future closure, intervention fidelity, robustness, and global realization can fail for different reasons.

## 9. Verification and its limits

The companion Python file and JSON report are reproducible from this folder.

| Check | Outcome |
|---|---|
| Exact noisy-initialization criterion versus independent partition enumeration | 524 instances: 324 exhaustive two-state instances and 200 seeded instances |
| Positive / negative finite cases | 214 feasible; 310 infeasible; all 310 selected negative witnesses replayed |
| Exact rational linear repair checks | 60 seeded systems; subset search independently matched minimum added-channel counts; one explicit oscillator |
| Oscillator scalar formula versus one-dimensional optimization | 160 comparisons; maximum difference 2.23×10⁻¹⁶ |
| Two-sample oscillator formula versus singular-vector witnesses | 160 comparisons; maximum difference 4.45×10⁻¹⁶ |
| Rank and tiny-sample-spacing edge cases | Four checks; stable singular-value formula avoids falsely declaring a small nonzero gap singular |
| Rational lower/upper certificates | Scalar optimum 24/25; a two-sample state-error square 1/40 |
| Orbital example | Exact equal energy/angular momentum witness; two numerical trajectories with energy and angular-momentum drift below 3×10⁻¹² |
| Causal and global constraints | Exact binary enumeration reproduces intervention disagreement and the minimal unsatisfiable core |

The general results depend on the written proofs. Numerical checks detect implementation mistakes but do not prove theorems, estimate laboratory performance, or establish priority. No third-party solver package was benchmarked for speed or predictive superiority. No observational data were used to infer a new physical law. The arbitrary-noise theorem is set-level; the mechanical noise example uses a known oscillator and a fixed normalized uncertainty set.

## 10. What would further establish BM's added value

The next comparison should test a falsifiable workflow claim: **does explicitly transporting obligations and counterexamples across several native models prevent errors, reduce unnecessary retained information, or reduce verified repair cost?** It should not ask whether BM beats ordinary algebra at a calculation that algebra already solves.

| Research question | Concrete test and comparator | What would count against BM |
|---|---|---|
| Does BM catch cross-model failures reliably? | Preregister a set of hidden-information, partial-domain, noisy, intervention, and incompatible-interface cases; compare a BM audit with a fully specified native-method workflow | Equal or worse accuracy without an offsetting cost or clarity benefit |
| Is there a theorem-level contribution? | Translate one candidate BM result both ways into bisimulation, constrained lumping, optimal recovery, or contracts; state exactly which assumptions or conclusions differ | An equivalence showing the claimed new result is just a relabeling |
| Does the repair reduce actual cost? | Restrict to a physically justified sensor/encoder catalogue; measure acquisition cost, computation, and achieved error using identical data and budgets | Cheaper native solutions omitted from the catalogue, or no observed improvement |
| Does a physical interpretation add a prediction? | Derive a definite observable with units, parameters, uncertainty, and a prediction distinct from the relevant established model | No distinct prediction, or disagreement with calibrated evidence |
| Are the mathematics independently reliable? | Have an independent reviewer or proof assistant check a bounded core, including negative cases and bridge assumptions | Unrepaired proof gaps or failures under the stated hypotheses |

For the mechanical benchmark, the next empirical step would use a measured oscillator with a calibrated frequency range and bounded measurement errors. Damping and frequency uncertainty must enter the admissible model before making a guarantee. A test should compare identical sample budgets at several phases and score prediction envelopes against held-out measurements. The exact ideal formulas here provide reference values, not permission to assume a real apparatus meets their hypotheses.

BM's strongest presently supported position is a mathematical framework with explicit nontrivial realizations and conditional necessity results. This note advances its quantitative testability. It does not turn its proposed physical interpretations into established physics or close the originality and independent-validation requirements identified in the preceding completion audit.

## Sources and reproducibility

Primary source links were checked on 23–24 October 2026. Some arXiv PDFs display a later rendering date; bibliographic years below follow their publication records rather than that rendering date.

- **[CM]** C. R. Shalizi and J. P. Crutchfield, *Computational Mechanics: Pattern and Prediction, Structure and Simplicity*, Journal of Statistical Physics (2001). [Paper](https://arxiv.org/abs/cond-mat/9907176). Sections IV–V and minimality discussion. Uses predictive distributions, not the deterministic bounded-noise semantics of DR1.
- **[MZ]** A. J. Chorin, O. H. Hald, R. Kupferman, *Optimal prediction and the Mori–Zwanzig representation of irreversible processes*, PNAS 97 (2000), 2968–2973. [Author manuscript](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf), sections 1–2. DOI:10.1073/pnas.97.7.2968.
- **[CLUE]** A. Ovchinnikov, I. C. Pérez Verona, G. Pogudin, M. Tribastone, *CLUE: Exact maximal reduction of kinetic models by constrained lumping of differential equations*, Bioinformatics (2021); preprint 2020. [Paper](https://arxiv.org/abs/2004.11961), algorithms 1–3 and supplementary invariant-subspace proofs.
- **[OR]** M. Ettehad and S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors*, SIAM/ASA Journal on Uncertainty Quantification 9(4) (2021), 1438–1456. [Author manuscript](https://foucart.github.io/publi/OR_Uncertainty_v2.pdf), sections 2 and 4, especially Theorem 4. DOI:10.1137/20M1328476.
- **[OR24]** S. Foucart and C. Liao, *Radius of information for two intersected centered hyperellipsoids and implications in Optimal Recovery from inaccurate data*, Journal of Complexity 83 (2024), 101841. [Author manuscript](https://foucart.github.io/publi/OR_L1Noise_v3.pdf), Theorem 1 and section 3. Publication metadata checked against the [author's bibliography](https://foucart.github.io/papers.html).
- **[CA]** S. Beckers and J. Y. Halpern, *Abstracting Causal Models*, AAAI (2019). [Paper](https://arxiv.org/abs/1812.03789), definitions 3.5, 3.7, 3.13, 3.15.
- **[CAA]** S. Beckers, F. Eberhardt, J. Y. Halpern, *Approximate Causal Abstractions*, UAI proceedings, PMLR 115 (2020), 606–615. [Proceedings record](https://proceedings.mlr.press/v115/beckers20a.html). This investigation inspected the proceedings abstract; it does not import an unexamined quantitative theorem from this paper.
- **[GL]** S. Abramsky and A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*, New Journal of Physics 13 (2011), 113036. [Paper](https://arxiv.org/abs/1102.0264), introduction and local-to-global formulation. No general identification of BM with the paper's empirical-model semantics is assumed.
- **[PHY1]** OpenStax, *University Physics*, vol. 1, section 11.3, [Conservation of Angular Momentum](https://openstax.org/books/university-physics-volume-1/pages/11-3-conservation-of-angular-momentum).
- **[PHY2]** NASA, [Orbits and Kepler's Laws](https://science.nasa.gov/solar-system/orbits-and-keplers-laws/). The exact normalized arithmetic and representation counterexample above are derived in this note.
- **[PHY3]** C. W. F. Everitt et al., *Gravity Probe B: Final Results of a Space Experiment to Test General Relativity*, Physical Review Letters 106 (2011), 221101. [Paper](https://arxiv.org/abs/1105.3456); related [mission explanation](https://einstein.stanford.edu/SPACETIME/spacetime4.html). The measurement is evidence about general relativity's frame dragging, not an experiment on BM.
- **[PHY4]** M. Zimbres and P. S. Letelier, *Multipolar corrections for Lense-Thirring precession* (2008). [Author preprint](https://arxiv.org/abs/0803.4133), equations 33–34. The l=1 term scales as angular momentum divided by r³ in G=c=1 units.

BM dependencies: canonical T01 (factorization), T10–T11 (future tasks and dynamic closure), T13 (relative essentiality), T31–T32/T47 (task separation and error), and the 23 October note *BM: necessity certificates and an exact comparison with existing theory*. The current research book already contains the classical observability rank result and earlier noisy-recovery examples; those are not counted here as newly discovered foundations. Frozen source identities and hashes are recorded in the accompanying source manifest.

Run `python BM_Research_Verification_2026-10-24.py .` to reproduce the JSON report and figure. The required packages and observed versions are recorded in that report.


---

Source: BM_Completion_and_Network_Development_2026-10-29.md

# Branch Mathematics: completion review and tree-network development

29 October 2026. This is an additive development for BM's frozen V1 / Edition 1.1 foundation. It uses the 23 October public research inventory and preserves its classifications and stable identifiers. It does not claim that open research questions have been solved or that this work received independent mathematical review.

## 1. Result and scope

The established BM core provides definitions and conditional results for representing tasks, retaining necessary distinctions, descending operations, reconciling interfaces, and checking realization. The current work makes three concrete additions:

1. It locates and internally reviews the stated proof basis of all 128 BM theorem rows previously lacking an enumerated dependency list. The source trace records their proof ideas, declared scope and direct named BM dependencies. This is a structured internal review, not a formal proof verification or independent review.
2. It completes a direct, bounded comparison: BM's existing reference programs and established methods agreed on the outcomes of 162 specified test cases. The comparison is described separately in `BM_Direct_Comparison_Findings_2026-10-29.md`.
3. It supplies a finite mathematical contract for overlapping frames, tree-shaped composition, seed contributions and activation, including positive results, counterexamples, and executable checks. These are explicit models of the ideas, not empirical claims about particles or the universe.

The 23 source hashes from the earlier release were checked again. The preceding inventory contains 336 BM entries: 70 definitions, 254 theorem-classified records, two conditional theorem records, and ten hypothesis records. The 254 records include corollaries, aliases and counterexamples; they are not a count of independent discoveries.

The 10 hypothesis records consist of six active broad research families, three optional broad Seed/Rooting/Rebranching candidates, and one retired proposal. The finite operational versions are separate from claims about a universal Seed, Root, or rebranching mechanism. The original 645-entry BM/GURF/Steadman inventory is preserved as source evidence; this development focuses on BM.

## 2. Review and evidence status

| Item | Completed here | Still needed |
|---|---|---|
| Source integrity | 23 source hashes match their recorded values | Historical sources absent from that manifest are not recovered by a hash check |
| Original T01–T55 | The earlier internal dependency map is retained | Independent proof checking and review of use in later results |
| Previously unenumerated BM proof dependencies | All 128 have source-section locators, hashes and an internal proof-basis review | Independent proof checking remains; the completeness and substance of previously populated dependency lists also need review |
| Inventory dependency structure | All 336 BM records have statements and source references; all 119 previously listed dependency links resolve, and the combined listed graph has no directed cycle | A resolved link is not proof that it is necessary, sufficient or complete; this check does not certify the proofs |
| Finite reference software | Direct comparison and witness replay on declared finite models | More implementation coverage, external review, and appropriate scaling tests |
| Overlapping trees and Seeds | A finite model, existence conditions, explicit failure cases, and tests below | Other native sectors, physical interpretation, and any general operational claims need their own specifications and proofs |
| Originality and practical benefit | Specific overlaps with existing state minimization, constrained lumping, integer optimization and optimal recovery are identified | A controlled application showing a distinct practical or theorem-level advantage; historical priority remains a separate research question |

The reviewed records include finite representation and closure results, October examples, weighted reconstruction, projector certificates, Jordan and nonlinear repair, and quantum information. Their individual locations, direct named dependencies, proof ideas and limits are in `BM_Source_Trace_2026-10-29.json`. Some results invoke established outside theorems; the trace identifies those imports. Two records point first to the historical open-question section and separately identify the later resolution, rather than presenting the earlier statement as its proof.

The user recently developed related overlapping-tree and seed ideas in another conversation. The available context records the distinctions between a completion Seed and a generative rule, local and global consistency, and loss of history under thresholding. Exact earlier numerical settings and transcripts were not recovered in the inspected files. The examples below are therefore newly specified examples, not reconstructions of those earlier experiments.

## 3. A finite model of overlapping tree frames

Let V be a finite set of typed variables. Each variable v has a nonempty finite domain D_v. A **frame** i declares a scope B_i⊆V and an allowed relation

\[
R_i\subseteq\prod_{v\in B_i}D_v.
\]

Two frames overlap when they mention a common variable. A **network realization** is one assignment to every variable that satisfies every declared frame relation:

\[
\mathcal F=\left\{x\in\prod_{v\in V}D_v:
                 x|_{B_i}\in R_i\text{ for every frame }i\right\}.
\tag{N1}
\]

A declared obligation on several frames is itself another relation or predicate on the appropriate variables. Merely naming frames does not supply a coupling rule. A finite **tree of frames** is a connected acyclic graph whose nodes are frames. Several trees may share variables or frames; their union is a network and may have loops. A Tree in the existing BM record also carries realization, provenance, history and law assignments, so a graph alone is not the whole BM Tree object.

For a specific finite network, enumeration of the product domains decides whether \(\mathcal F\) is empty. This is an exact finite construction; it does not imply an efficient algorithm for large networks, or a general algorithm for arbitrary infinite presentations. The reference verifier prunes a partial assignment only after all variables of a violated frame have been assigned.

### 3.1 When local frame data do extend to a common realization

Suppose the frame graph is a finite tree and satisfies the **running-intersection condition**: for every variable v, the set of frames containing v is connected in that tree. Require each R_i to be nonempty. For every edge i—j, require equality of the projections of R_i and R_j onto their shared variables:

\[
\pi_{B_i\cap B_j}R_i=\pi_{B_i\cap B_j}R_j.
\tag{N2}
\]

**Theorem.** Every allowed tuple in any frame extends to a global realization in \(\mathcal F\). In particular, \(\mathcal F\ne\varnothing\), and its projection onto each frame is exactly that frame's declared relation.

**Proof.** Choose any frame as root and choose any tuple in its relation. Visit neighboring frames outward. For a child j with parent i, its overlap with everything already assigned is exactly contained in \(B_i\cap B_j\): otherwise a variable occurring in j and an earlier frame would, by running intersection, also occur along the path through i. The parent's overlap values occur in the projection of R_i and hence, by (N2), in the projection of R_j. Choose a tuple of R_j with those overlap values and extend the assignment. Finite induction assigns all frames consistently. Any variable in no frame can be given a value from its nonempty domain. Starting with any chosen tuple proves the projection statement. ∎

This is the finite join-tree/gluing principle already present in the BM core, not a claim of a new gluing theorem. Its relationship to established acyclic database theory is documented by Beeri, Fagin, Maier and Yannakakis (1983); a 2026 primary research paper restates the broader local-to-global result [R1, R2]. The exact edge condition above is a sufficient condition for the stated model. It is not necessary for a global realization: some local tuples may simply be unused.

### 3.2 Why overlaps can produce a loop that changes the answer

Let a,b,c be Boolean and give three frames the relations

\[
a=b,\qquad b=c,\qquad a\ne c.
\tag{N3}
\]

Each relation is nonempty. Every pair of the three relations is jointly satisfiable. Every shared single-variable projection is \(\{0,1\}\). But all three together are impossible, because the first two imply a=c. Thus local pair checks do not establish one global realization when the frame scopes form this cyclic arrangement.

The third relation cannot be silently discarded to make a tree. If it is dropped, the resulting path has the two solutions (0,0,0) and (1,1,1); neither satisfies the original full network. A spanning tree can organize evaluation, but all omitted cross-links still need to be checked.

The verifier enumerates all eight combinations of equality/inequality on a Boolean triangle. Four are globally satisfiable and four are not. In each unsatisfiable case, deleting any one constraint restores satisfiability, giving 12 checked deletion witnesses.

### 3.3 Correction: overlap equality depends on the kind of data

N2 concerns ordinary **sets of tuples**. It cannot be promoted automatically to every weighted or annotated sector.

Consider the additive monoid \(K=\{0\}\cup\{2,3,4,\ldots\}\). It is closed under addition and has zero, but it does not contain 1. Let one frame contain a variable with three values and declared weights (2,2,2), and another contain a disjoint variable with two values and declared weights (3,3). Their shared scope is empty, and both project to the same total weight 6.

A common K-valued joint relation would be a 3-by-2 matrix with those row and column sums. Each row sums to 2, so it must be either (2,0) or (0,2). Every column sum would therefore be even, contradicting the required column sum 3. **Equal weighted overlap sums do not supply a common weighted witness in this sector.**

For ordinary nonnegative integer weights, the matrix with a 1 in every cell gives the required margins. For ordinary Boolean relations, the full 3-by-2 support gives a common set-valued relation. The obstruction is thus a property of the chosen native annotation algebra and its admissible witnesses; it is not an inconsistency of the set-level theorem.

This is a small explicit instance of the need for an additional native consistency property in annotated-relation theory [R2]. Equality of weighted overlaps here is called *inner consistency*: for the chosen K it does not imply even a pairwise weighted joint witness. It must not be confused with the stronger condition that a pairwise witness already exists.

## 4. Completion Seeds and generative Seeds

BM18-O1 already provides a finite **completion Seed**: domains, a partial assignment, and allowed complete assignments. Its completion set may be empty. It is a valid way to describe candidates and constraints.

The more recent generative idea needs additional data. In this finite development, a **generative Seed record** contains a source identifier, a typed contribution or state, its admissibility conditions, and a declared rule saying when and how it contributes to a candidate output. Provenance records which input records were used. An output becomes an accepted Root only after a specified receiver's applicability and acceptance conditions hold.

These are related constructions, not an implicit redefinition of BM18-O1. The steps are:

1. **Complete:** determine which inputs are compatible with all constraints.
2. **Generate:** apply a separately declared operation or update rule to compatible inputs.
3. **Validate:** check the resulting network, its obligations and provenance.
4. **Export:** apply a receiver-specific Passport. A receiver can accept, reject, or find the export inapplicable.

Accumulating candidates can alter a declared input to a generation rule, but accumulation by itself does not prove a new object, a lawful Tree, or a physical particle exists. If no rule or acceptance contract has been supplied, the appropriate result is “not yet specified.”

## 5. A no-attachment activation example

The following is a finite toy model designed to test the user's idea that Seeds need not attach directly to one another in order to contribute to a local network. It introduces no seed-to-seed edges. Each seed supplies nonnegative contributions to four sites A,B,C,D. A site activates when its total is at least 2. The site network uses the fixed square edges AB, BC, CD and DA, restricted to active sites.

| Configuration | Seed 1 contributions A–D | Seed 2 | Seed 3 | Site totals | Activated network |
|---|---|---|---|---|---|
| Path | (2,1,0,0) | (0,1,1,0) | (1,1,1,0) | (3,3,2,0) | A—B—C: 3 vertices, 2 edges, no cycle |
| Cycle | (1,1,1,0) | (1,0,0,1) | (0,1,1,1) | (2,2,2,2) | A—B—C—D—A: 4 vertices, 4 edges, one independent cycle |

Both configurations have three Seeds. Their individual total contributions are 3, 2 and 3 in the same order, and the total over all sites is 8. Under the supplied threshold and site-edge rule, the different distribution produces a different network. The cycle rank is \(|E|-|V|+c\), where c is the number of connected components.

This demonstrates logical possibility in a specified model. The threshold, contribution functions and edge rule were chosen for the example; no measurement or prior physical law determines them here. A connected cyclic output is a network, not a graph-theoretic tree. A tree could be selected inside it, but dropping the closing edge would lose one relation unless that edge remains recorded separately.

## 6. When accumulation reaches a threshold

Let \(S_t\ge0\) be a scalar retained quantity, let \(0\le\rho\le1\), and let \(u_t\ge0\) be an explicitly supplied input. The rule

\[
S_{t+1}=\rho S_t+u_t
\]

has the exact solution

\[
S_t=\rho^tS_0+\sum_{j=0}^{t-1}\rho^{t-1-j}u_j.
\tag{N4}
\]

Proof is by induction. This is an example of a specified accumulation law, not a universal BM axiom.

For constant u and \(0\le\rho<1\), the limiting level is \(S_\infty=u/(1-\rho)\). If \(0<\rho<1\) and \(S_0<S_\infty\), the sequence increases toward that level. A threshold above the limit is never reached. A threshold equal to the limit is not reached in finite time under these strict assumptions. For \(S_0<\theta<S_\infty\), the first crossing is the smallest integer t satisfying

\[
\rho^t\le\frac{S_\infty-\theta}{S_\infty-S_0}.
\]

If \(\rho=1\), \(S_t=S_0+tu\); if \(u>0\), any finite threshold is eventually reached. If \(\rho=0\), the next level is u and subsequent levels remain u. Other initial levels and varying inputs require their own comparisons; the monotonic crossing conclusion is not universal.

### Thresholding loses distinctions that can matter later

Let the visible output be \(b(S)=1\) when \(S\ge1\), otherwise 0. Take \(S=3/5\) and \(S'=9/10\), so both outputs are zero. With the same update \(\rho=1/2,u=3/5\), the next levels are 9/10 and 21/20, with outputs 0 and 1. Thus the current Boolean output alone cannot evolve autonomously for both states. The underlying levels or another sufficient history must be retained for this future task.

This proves a failure of that representation under the declared update. It does not assert that the discarded distinction physically disappears from every system.

## 7. Verification

`BM_Network_Seed_Verifier_2026-10-29.py` is a standard-library finite reference checker. Its checks include:

| Test | Result |
|---|---:|
| Finite join-tree models compared with a separate full-product oracle | 250 |
| Local tuples checked to have a global extension in those models | 3,009 |
| Boolean triangle parity cases | 8: four satisfiable, four unsatisfiable |
| Single-constraint deletions restoring those four inconsistent cases | 12 |
| Exact rational recurrence equalities | 780 |
| Exact finite threshold-crossing checks | 20 |
| Row-valid matrices checked in the weighted counterexample | 8; none satisfy both column sums |
| Malformed finite inputs rejected | 4 |

The independently written comparison replay verifies 3,569 finite separating-pair outcomes, 36 selected interface families, 30 exact linear bases and 40 scalar primal/dual recovery bounds. A separate replay does not equal external independent review, and floating-point agreement does not prove a universal statement.

For the reviewed October examples, a second checker also examined 274 oracle-adversary witnesses, 90 small integer-capacity optimization cases, 14 field-code recovery subsets and 11 insufficient-subset examples, 12 quantizer sizes, and 512 triangle inequalities for the declared capped successor-set metric. These examples support the scoped arguments; they do not replace their proofs.

## 8. Work that remains open

The framework is mathematically meaningful, and these additions resolve the finite contracts stated here. Completion of **every** intended BM claim has not been established. The remaining work includes:

- Substantive review of the previously populated dependency lists and verification that the listed assumptions and references are complete; identifier resolution alone does not establish that.
- Independent review or formal proof checking of a specified core and of the longer analytic arguments.
- The six retained broad research families: nonlinear Jordan interior optima; global regular realization and minimal augmentation; constrained/infinite causal realization; general quantum-algebra recovery implementation; nonlinear repair beyond solved classes; and further infinite-dimensional native settings. Each needs its own fixed assumptions and a proof, counterexample or justified impossibility result.
- Native-sector bridges for continuous, stochastic, weighted, smooth, quantum and physical cases. The set-valued join theorem in section 3 cannot by itself settle them.
- A measured practical comparison on a declared real application. The 162-case comparison supplies correctness evidence and overlap with existing mathematics, not a measured field advantage.
- Exact recovery of earlier research records if a complete historical archive is claimed. The recent conversation-derived Seed ideas are recorded with their scope above, but the underlying transcripts and parameters were not available in the inspected files.

The frozen foundation is not altered. New results are conditional on the explicit models in this note. BM does not need an invented universal formula for every possible native domain in order to be a valid framework; unsupported universal claims should remain visibly open.

## References

- **[R1]** C. Beeri, R. Fagin, D. Maier, M. Yannakakis, “On the Desirability of Acyclic Database Schemes,” *Journal of the ACM* 30(3), 479–513 (1983). [IBM Research record](https://research.ibm.com/publications/on-the-desirability-of-acyclic-database-schemes).
- **[R2]** A. Atserias and P. G. Kolaitis, “Gamma Acyclicity, Annotated Relations, and Consistency Witness Functions,” ICDT (2026), [open paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol365-icdt2026/html/LIPIcs.ICDT.2026.16/LIPIcs.ICDT.2026.16.html), sections on standard relations, inner consistency and local-to-global consistency. The finite weighted counterexample above is checked directly in the accompanying code.
- Existing BM source dependencies and hashes are listed in `BM_Source_Integrity_2026-10-29.json` and `BM_Source_Trace_2026-10-29.json`. The older source ledger and the five relevant evidence files are bundled under `source_evidence/`.


---

Source: BM_Direct_Comparison_Findings_2026-10-29.md

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


---

Source: BM_New_Uses_2026-10-29.md

# New application directions for Branch Mathematics

29 October 2026

BM can be applied to more than physical states. A native object can be a program, a dataset, an experimental hypothesis, a history, a document with formal requirements, or a candidate design. Its representation can be a summary, score, file conversion, interface, report, or set of observations. Its receiver task determines which distinctions must survive.

This survey identifies **24 specific application candidates not found as worked examples in the retrieved earlier discussions**, followed by **four extensions of ideas already discussed**. Retrieval is not a complete historical archive, so these are candidates for new applications within the project, not claims that the user has never mentioned them. No historical priority or BM-exclusive capability is claimed.

Earlier work already covers model reduction, uncertainty, control, memory, privacy, secure compilation, physical Seeds, and general experiment selection. The survey focuses on concrete deployments of BM and stays within BM rather than pursuing the excluded physics projects.

## What makes an application concrete

A proposed application should supply a native state/model family X, the information retained by R, the required outputs T, admissible actions, receiver constraints and a cost or error objective. When R(x)=R(y) but T(x) differs from T(y), the pair is an exact obstruction to decoding that task from R alone. For future tasks, the retained distinction must also survive the declared actions and their availability. For combined branches, one compatible joint realization must satisfy the obligations together.

These conditions can support a useful output: a certificate of sufficiency within the model, a concrete counterexample, a minimum-cost addition in a finite catalogue, or an explicit unresolved requirement. They do not automatically extract a correct formal model from ordinary language or prove that the supplied model describes reality.

Readiness labels below mean:

- **Demonstrated:** a small exact example is included in this package. This is not a real-world performance trial.
- **Buildable:** the current finite BM methods can support a prototype after the native contract is supplied; no prototype for this entry was run here.
- **Research:** a substantial model, semantics, measurement or theory gap remains.

## The 24 application candidates

| ID | Application | What BM would produce | Readiness and material limitation |
|---|---|---|---|
| A01 | Find blind spots in AI or software benchmarks | Two candidate behaviors with identical existing test results but different required deployment outputs; an additional separating test | Demonstrated on four Boolean rules. Coverage is relative to the supplied candidate behaviors. |
| A02 | Detect loopholes in reward metrics and performance scores | Equal-score outcomes with different actual task success, identifying what the score failed to measure | Demonstrated on reported versus completed work. A complete real objective still has to be specified. |
| A03 | Check database migrations before losing future capability | A distinction preserved for current queries but required by a later update, with a failing operation sequence | Demonstrated on a three-state inventory. Real concurrency, transactions and schemas need explicit models. |
| A04 | Choose the least costly diagnostic event log | A minimum-cost subset of log fields that distinguishes every declared fault class, with witnesses for insufficient choices | Demonstrated on four fault states. Logging cost is a declared toy cost, and the task is diagnosis rather than reconstruction of every event. |
| A05 | Audit undo/redo, game saves and rollback snapshots | Whether a saved representation retains the history required by the allowed continuations | Demonstrated on a four-state undo model. Randomness and external services must be represented when they affect replay. |
| A06 | Invalidate caches when the task changes | Which previously sufficient summaries are no longer sufficient, and how much supplemental information is necessary | Demonstrated on a parity cache with a new query. Discarded distinctions cannot be reconstructed from the cache alone. |
| A07 | Propagate corrections through research and proof records | The downstream results requiring revalidation after an assumption, dataset, calibration or proof step changes | Buildable with declared dependency alternatives. A dependency edge marks possible impact; it does not prove the conclusion is false or that no independent proof survives. |
| A08 | Detect repeated evidence masquerading as additional sources | A provenance account separating three reports from three distinct source records | Demonstrated by explicit source enumeration. Distinct sources do not by themselves establish statistical independence or truth. |
| A09 | Check whether retrieved documents jointly contain enough information | A pair of compatible completions giving different answers, or a set of missing fields that would separate them | Buildable for structured facts. Search relevance and fluency do not themselves certify that the fact inventory is complete. |
| A10 | Generate precise abstentions and useful clarification questions | “The supplied facts allow answers A and B; this particular measurement/question separates them” | Buildable for a finite completion family. An incomplete family can hide other possibilities. |
| A11 | Audit synthetic data beyond matching ordinary statistics | A task whose joint structure changes despite matching marginal or pairwise distributions | Demonstrated with even/odd parity datasets. It does not establish the fidelity of a real generator. |
| A12 | Check offline synchronization of scarce resources | Whether locally valid edits, bookings or reservations admit one globally valid merged state | Buildable for bounded models. Distributed timing, message loss and retry semantics need a native distributed model. |
| A13 | Certify API compatibility for particular clients | The client-visible tasks and operation sequences preserved by a new implementation, together with breaking witnesses | Buildable for finite interfaces. This gives receiver-specific compatibility, not a guarantee for every possible client. |
| A14 | Generate focused regression tests after a change | Input or action sequences that distinguish the old and new required behavior; a selected test family covering declared differences | Buildable for bounded systems. General program equivalence is not made decidable by BM. |
| A15 | Find order-sensitive automation steps | Workflows whose reordered operations alter availability, output or validity, identifying which order information must be retained | Buildable with explicit partial actions. A mere list of operations omits the needed execution semantics. |
| A16 | Audit CAD-to-manufacturing handoffs | Required tolerances, reference surfaces, material/process attributes or assembly constraints lost by a conversion | Research. Geometry, approximation and manufacturing acceptance need exact or validated semantics; matching appearance is only one possible task. |
| A17 | Select mutually compatible replacement components | Feasible component combinations and minimum-cost repairs satisfying all declared interfaces together | Buildable for finite catalogues. The catalogues and physical interaction laws must be supplied and validated. |
| A18 | Preserve measurement meaning across labs and file imports | Whether units, calibration, coordinate frame, sampling and uncertainty remain sufficient for a stated downstream comparison | Buildable in a restricted measurement model. BM cannot infer an absent calibration law from metadata alone. |
| A19 | Decide what a simulator certificate transfers to | The obligations proved in a simulator that remain valid under the measured simulator-to-target discrepancy | Research. A valid discrepancy bound and domain coverage are essential; a successful simulation alone supplies neither. |
| A20 | Turn surprising results into structured competing explanations | Separate inconsistent assumptions, insufficient observations, an invalid bridge, numerical error and alternative model families; propose discriminating checks | Research. A failure does not identify its true cause automatically. Unexpected results remain evidence to investigate instead of being discarded for missing an expected answer. |
| A21 | Identify what aggregate performance statistics cannot answer | Explicit underlying event histories with the same published aggregate but different retention, attribution or sequence behavior | Buildable for bounded event models. This identifies ambiguity; it does not reconstruct the actual hidden event history. |
| A22 | Diagnose learning needs that a total score hides | Distinct skill profiles with the same score but different next instructional tasks, plus a separating question | Demonstrated on two binary skills. Real educational validity and learning effects need empirical study. |
| A23 | Check translation, simplification and accessible documents against required meaning | Required negations, quantities, exceptions, actor identities and ordering lost by a transformation | Research for free text; buildable for an explicitly formalized fragment. A semantic extractor can itself make mistakes. |
| A24 | Keep stories, game quests and constrained creative edits consistent | A shared realization of declared chronology, inventory, character knowledge, promises and plot constraints; a small incompatible subset when none exists | Buildable for formal story rules. Artistic quality and reader interpretation remain separate receiver judgments. |

## Four extensions of earlier ideas

These should not be advertised as newly discovered uses of BM.

| ID | Existing direction | Specific next application | Readiness |
|---|---|---|---|
| E01 | Future-response memory and compression | A conversation-summary checker that preserves declared commitments, permissions, exceptions and pending tasks | Buildable for structured conversation state; unrestricted language-model reliability requires empirical testing. |
| E02 | Experiment selection and identifiability | Choose the next experiment that separates task-relevant competing models, rather than merely collecting more of the same output | Buildable for a finite model/experiment family; causal conclusions require native causal assumptions. |
| E03 | Failure cascades, cuts and redundancy | Audit backups that secretly share a power source, supplier, clock, calibration file or communication route | Buildable on a declared dependency/failure model; failure probabilities and unmodeled common causes remain external inputs. |
| E04 | Calculator, interfaces and Passports | Check an equation pipeline for mismatched domains, units, invertibility, approximation error and missing assumptions when one result is reused | Buildable on a supported symbolic fragment. Unsupported notation or an unproved premise should remain explicit. |

## Nine worked application examples

The package runs nine finite analyzer contracts covering seven applications, plus two direct enumeration checks for synthetic data and provenance. The source analyzer is unchanged from the earlier BM necessity implementation and verifies its own certificates. These are internal model demonstrations; no external reviewer or deployed application is claimed.

### A01: A benchmark can certify the wrong distinction

Consider four possible Boolean behaviors: return input A, return input B, always return zero, and always return one. The existing tests use (A,B)=(0,0) and (1,1). The first two behaviors give the same answers on both tests, yet differ on (0,1) and (1,0).

The checker certifies that the old test record cannot determine the full required truth table. With the old record retained, one additional off-diagonal probe suffices to distinguish all four declared candidate behaviors. This is an exact result for that candidate family. It is a model for generating tests that target the missing distinction rather than merely increasing the test count.

### A02: A reported completion metric can hide non-completion

The native outcomes record both whether a task was completed and whether completion was reported. If the score records only the report, “not completed, reported” and “completed, reported” have the same score and different task outcomes. The score cannot determine completion. A verified completion observation repairs the stated task.

This locates a specification gap. It does not solve the more difficult problem of automatically formalizing everything people intend an AI system to do.

### A03: A database conversion can preserve today and break tomorrow

The native stock count is 0, 1 or 2. A conversion keeps only “in stock,” mapping 1 and 2 to the same label. For the present availability query, two code states suffice.

Now allow a reserve operation that subtracts one when stock is available. Starting with stock 1 produces stock 0, while starting with stock 2 produces stock 1. Their next availability answers differ. The finite future-behavior quotient therefore requires three code states. The current Boolean field cannot support that exact autonomous update.

This suggests testing migrations against permitted updates and later queries, not just today's query results.

### A04: A minimal diagnostic log

The four modeled conditions are healthy, sensor fault, actuator fault and both faults. One alarm flag distinguishes healthy from faulty but merges three different diagnoses. A sensor-test bit and an actuator-test bit distinguish all four states. A verbose trace also distinguishes them, but has declared cost 10, while each test bit has cost 1.

Exhaustive observation-subset analysis gives minimum cost 2, attained by the two test bits. These costs are illustrative. The practical experiment would replace them with measured logging, storage and diagnostic costs.

### A05: A save file can preserve the screen but break undo

Let a history consist of a previous display bit and a current display bit. The visible display has two values. Undo replaces the current display with its previous value. Histories with the same current display and different previous displays must remain distinct.

The exact model has four future-behavior classes. Retaining both bits supports undo; retaining the current display alone does not. This provides a direct model for checking save files, checkpoints and rollback records against the actions they promise to support.

### A06: New questions can invalidate an old cache

The source has two bits a and b. If the only task is their parity, caching a XOR b suffices and needs two code states. Add the task “what is a?” and all four native states become distinguishable by the task pair. The old cache is insufficient; retaining a alongside the parity repairs it.

The earlier BM finite-memory argument gives a general bound for this kind of static retasking. For a finite native set, a fixed old code R, and a new task vector T, define

\[
m=\max_{z\in R(X)} |\{T(x):R(x)=z\}|.
\]

If a supplemental symbol is computed from the original native state and decoded together with the old code, its alphabet needs at least m symbols. The bound is attained by labeling the different task values separately inside each old fibre and reusing labels in different fibres. Thus a fixed-length binary supplement needs at least ceil(log2(m)) bits. This is an application of existing finite sufficiency/memory reasoning, not a new information theorem. It assumes access to the original state when the supplement is created; it cannot restore an already deleted distinction from the old cache.

### A08: More reports need not mean more original sources

The source lists (A,A,A) and (A,B,C) both produce a report count of three. They contain one and three distinct origin identifiers, respectively. A count-only representation cannot recover the number of distinct origins. Keeping the provenance identifiers fixes this finite task.

Neither origin count nor source separation proves truth or statistical independence. The useful application is detecting the unsupported jump from “many reports” to “many independent confirmations.”

### A11: Perfect pairwise statistical matching can miss a joint task

Give equal weight to each row in the following datasets:

| Even-parity source | Odd-parity replacement |
|---|---|
| 000 | 001 |
| 011 | 010 |
| 101 | 100 |
| 110 | 111 |

Every single-column distribution agrees. Every two-column joint distribution also agrees: each pair of bits occurs once. All six projections onto one or two columns therefore match exactly.

Nevertheless, the parity of all three bits is always zero in the source and always one in the replacement. A synthetic-data validator restricted to the matching projections would miss a complete reversal of that task. BM can make the task-preservation requirement explicit and return the exact lost distinction. This parity construction is classical; its use here is a concrete audit specification.

### A22: Equal educational scores need not imply the same next lesson

Two binary skills produce total scores 0, 1 or 2. A student who knows only A and a student who knows only B each score 1, but the stipulated next lessons differ. The total score is insufficient for that instructional task. In the finite model, one targeted item, combined with the old score, distinguishes all four skill profiles.

The result concerns the explicitly modeled skills and teaching decision. It does not establish that real students have binary skill states or that the selected lesson improves learning.

## Where established methods already overlap

The proposed uses are not evidence of historical novelty. The prior 162-case BM comparison found agreement with the tested native methods. A useful BM application must earn its value through a better integrated contract, fewer missed requirements, better explanations, lower verified cost, or a genuinely new theorem under stated assumptions.

| Proposed use | Relevant established work | What a fair BM comparison would measure |
|---|---|---|
| Benchmark gaps and behavioral refinement | Counterexample-guided abstraction refinement [S1]; shortcut-learning analysis [S2] | Same candidate systems and task requirements: missed behaviors, number/cost of added tests, checkable witnesses |
| Agent memory and tool-workflow requirements | LLMLingua prompt compression [S3]; tool-agent-user evaluation in tau-bench [S4] | Same memory/latency budget and episodes: lost commitments, task success and consistent adherence to specified rules |
| Database updates and representation changes | Relational lenses and incremental change propagation [S5] | Same query/update contract: preservation, breaking traces and computational cost |
| Evidence provenance and correction impact | PennProvenance's workflow, regression and cross-source provenance program [S6] | Same lineage inputs: missed shared origins, affected outputs and unnecessary recomputation |
| Offline composition and coordination | CALM and application-level distributed consistency [S7] | Same failure/communication model and invariants: valid merges, required coordination and complete counterexamples |
| Selecting interventions between models | Structural causal models and identifiability [S8] | Same causal assumptions and data: identified targets and discriminating intervention cost |
| Reducing an observed failure to its important inputs | Delta debugging [S9] | Same oracle and failure predicate: number of calls and actual minimality criterion; inclusion-minimal and minimum-cost are different goals |

These references establish nearby capabilities and comparison targets. They do not establish that a proposed BM system has already improved upon them. In particular, CEGAR refines an abstraction after analyzing potentially spurious counterexamples; the finite BM examples above use explicit native states and exact failure pairs. Those contracts should be aligned before comparing algorithms.

## The strongest first implementations

My judgment is that A01, A03 and A04 are the best immediate development targets. Each has explicit inputs, an exact finite witness, a clear user-facing decision and a conventional comparator. This priority is an assessment of testability, not a market forecast.

1. **Benchmark gap checker:** enter candidate behaviors, existing tests and deployment tasks; obtain a separating example and a lowest-cost test set within the supplied catalogue.
2. **Migration behavior checker:** enter an old state model, a proposed retained schema, queries and updates; obtain a valid reduced model or a separating action sequence.
3. **Diagnostic log selector:** enter fault states, observable event fields and measured costs; obtain a sufficient selected log and a witness showing what each excluded alternative fails to distinguish.

A06 can accompany all three: when the required task changes, invalidate the old certificate and calculate the additional information needed. A07 then makes the same discipline useful inside BM's own research corpus.

The more ambitious direction is A20: use BM to organize unexpected results without presuming the expected answer is correct. The system would preserve the raw result and distinguish which assumptions, reductions and bridges are actually contradicted. It could then propose tests between alternatives. Discovering the true replacement model would remain a scientific or mathematical task.

## Reproduction

Run `python3 BM_Application_Demonstrations_2026-10-29.py` from the extracted package. Python 3.10 or later and its standard library suffice. The script checks the hash of the bundled unchanged analyzer, runs nine finite contracts and their certificate checks, and exhaustively verifies the parity and source-count examples. Full inputs, certificates and outputs are written to `BM_Application_Demonstrations_2026-10-29.json`.

No LLM, external API, empirical trial, physical experiment or independent peer review was run for these application examples. The exact statements hold in their declared finite models.

## Primary sources and research records

- **[S1]** Clarke, Grumberg, Jha, Lu and Veith, *Counterexample-guided Abstraction Refinement*, CAV 2000. [Paper](https://web.stanford.edu/class/cs357/cegar.pdf).
- **[S2]** Geirhos et al., *Shortcut Learning in Deep Neural Networks*, Nature Machine Intelligence (2020). [Author manuscript](https://arxiv.org/abs/2004.07780).
- **[S3]** Jiang et al., *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models*, EMNLP 2023. [ACL paper record](https://aclanthology.org/2023.emnlp-main.825/).
- **[S4]** Yao et al., *tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains* (2024). [Paper](https://arxiv.org/abs/2406.12045). Its original measurements concern the models and evaluation conditions in that paper, not current models.
- **[S5]** Horn, Perera and Cheney, *Incremental Relational Lenses*, ICFP 2018. [Author institutional record and open paper](https://eprints.gla.ac.uk/167403/).
- **[S6]** University of Pennsylvania Database Group, *PennProvenance*. [Research program and papers](https://db.cis.upenn.edu/pennprovenance/).
- **[S7]** Hellerstein and Alvaro, *Keeping CALM: When Distributed Consistency is Easy*. [Author manuscript](https://arxiv.org/abs/1901.01930).
- **[S8]** Pearl, *Causal Inference*, PMLR 6, 39–58 (2010). [Paper](https://proceedings.mlr.press/v6/pearl10a.html).
- **[S9]** Zeller and Hildebrandt, *Simplifying and Isolating Failure-Inducing Input*, IEEE TSE 28(2), 183–200 (2002). [Author publication record](https://www.st.cs.uni-saarland.de/papers/tse2002/); [DOI](https://doi.org/10.1109/32.988498). The author-hosted full-text retrieval timed out during this survey; this source is used only to identify the established comparison method.


---

Source: BM_Seed_Provenance_Completion_2026-11-01.md

# Branch Mathematics — Seed provenance, law uncertainty, and closure

**Additive technical supplement, 1 November 2026.** This is a finite mathematical continuation of Branch Mathematics (BM), not an amendment to the frozen Version 1 / Edition 1.1 foundation. It does not assert universal Seed dynamics, independent peer review, historical mathematical priority, or a physical interpretation.

## 1. Sources, completeness, and nonduplication

The 12 September frozen V1 defines the typed Branch, native Interaction, certified Leaf, realized Tree, Task/Response, Passport, and receiver-accepted Root. The Research Edition updated 19 October already supplies finite completion Seeds, receiver-dependent Rooting, realization-preserving Rebranching, and finite composition (BM18-O1–O4). These are therefore **prior BM work**, not inventions of this supplement.

The 29 October `BM_Completion_and_Network_Development_2026-10-29.md` already gives a finite network of overlapping frames, a running-intersection/join-tree gluing result, an inconsistent three-frame cycle, a weighted-annotation counterexample, a no-direct-attachment Seed activation model, and an exact scalar accumulation example. Its tests reported 250 random join-tree models, 3,009 checked global extensions, eight Boolean triangle cases, 780 rational recurrence identities, and related witnesses. Do not promote these older results as new here.

The October 29 project inventory has **336 BM entries: 70 definitions, 254 theorem-classified records, two conditional theorem records, and ten hypothesis records**. These are classifications of archive entries, not 254 independent discoveries. The review traced the proof bases of 128 previously unenumerated theorem dependencies and checked 23 recorded source hashes. It did not independently certify all proofs. The same-day complete-method comparison reported agreement on 162 small tested cases, with no unique mathematical or performance advantage established. The 29 October application inventory also records 24 application directions plus four extensions, and nine finite analyzer contracts covering seven applications; those are not first proposed here.

**New question in this supplement:** When a portable Seed enters a receiver, how much generating-law identity, current state, and future behavior must be retained for a specified task or autonomous continuation? The original law, source IDs, and available side information must be declared. No generating mechanism follows merely from using the word *Seed*.

## 2. Contract: tasks, legal models, and portable Seeds

For a finite nonempty set of source-law alternatives `L`, each law `ell` supplies a nonempty legal state set `J_ell`, a typed Seed export `sigma_ell:J_ell -> S`, and a task `T_ell:J_ell -> Y`. A lawful model may also supply an explicit native transition. A **receiver** knows the Seed code and only such law/source metadata as are authorized by its Passport. A **Root** arises only when receiver applicability and admissibility are separately passed; task sufficiency alone is not Passport acceptance.

The source law may be uncertain but the world must still be one of the *declared* lawful candidates. Treating overlapping copies of one source as independent Cartesian factors can create spurious global states and false retention requirements. Unsupported correlations must not be silently assumed either. If the joint relation is unknown, the status is *underdetermined* pending a source-law contract.

The finite operation of adding constraints is conjunctive and can only remove old realizations from the same carrier. A generative Seed that changes the carrier, supplies new variables, or activates a rule is a **different native operation**; such growth cannot be inferred from constraint accumulation alone. This keeps completion Seeds distinct from portable generative Seeds.

## 3. The finite law-tag theorem

Assume each law is individually sufficient:

`sigma_ell(x)=sigma_ell(y)` implies `T_ell(x)=T_ell(y)` for any `x,y` in `J_ell`.

Define an undirected **law-conflict graph** `G_T` on `L`. Distinct laws `ell,m` are adjacent precisely when there exist `x in J_ell, y in J_m` with equal Seed exports and unequal required task answers.

**Proposition S1 (minimum task-specific law tag).** A single decoder `D:S x C -> Y` exists using law tag `c:L -> C`, so that

`D(sigma_ell(x),c(ell))=T_ell(x)` on all legal states, **if and only if** `c` is a proper coloring of `G_T`. Consequently the minimum identifier alphabet has `chi(G_T)` symbols, requiring `ceil(log2 chi(G_T))` fixed binary bits.

*Proof.* Adjacent laws sharing a tag present identical decoder input with different demanded output, which is impossible. For a proper coloring, assign each observed pair `(s,tag)` the unique required task value among worlds producing it. Uniqueness follows from within-law sufficiency and the absence of same-colored cross-law conflicts. Assign arbitrary values on unused code pairs. This defines the decoder. Both directions give the exact minimum. QED.

**Failure certificate.** If two states within *one* law have equal Seed export but different task answers, no identifier of the law alone can repair them: their tagged export remains identical. An additional native-state distinction or a weaker task is necessary.

**Example.** Under the copy model `b=a`, export `a` determines `b`. Under the inversion model `b=1-a`, it also determines `b`. Without the model identity, the export is ambiguous. One bit specifying the model repairs it. With a third restricted model admitting only `(a,b)=(0,0)`, copy and restricted laws can share the same tag. Three model names need just two tags, not three.

## 4. Horizon-dependent distinguishability

Suppose each law has a total deterministic update `f_ell:J_ell -> J_ell`. For horizon `h>=0`, define the task trace

`V_ell^h(x)=(T_ell(x),T_ell(f_ell x),...,T_ell(f_ell^h x))`.

When each Seed export is sufficient for this trace within each law, apply S1 with `V^h` as the task. Call the conflict graph `G_h`.

**Proposition S2.** `G_h` is a subgraph of `G_{h+1}`, so `chi(G_h)` cannot decrease as the declared future obligation grows. On a finite deterministic global carrier `W` (disjoint union of all law-labelled states), the entire future-behavior equivalence partition stabilizes by at most `|W|-1` refinement steps. Consequently the model-conflict graphs stabilize no later than that finite bound. This is standard deterministic partition refinement in a BM contract, not a new universal dynamics theorem.

*Proof.* Distinct length-`h` traces remain distinct when extended by another coordinate. For stabilization, partition `W` by current output. Each further trace coordinate refines the partition. Any strict refinement increases its class count by at least one; there can be at most `|W|-1` such increases. When one refinement adds no split, deterministic successor refinement adds none later. QED.

**Test.** For source state `a in {0,1}`, export `a` and demand `T(a)=a`. The *hold* law updates `a->a`; the *flip* law updates `a->1-a`. At horizon zero no law tag is needed. At horizon one, the same Seed value leads to different answers, so one law bit becomes necessary. It remains necessary at all longer horizons.

Note that knowing future task traces does **not** guarantee an autonomous update of the exported Seed value itself.

## 5. Stronger fixed-law autonomous closure

Continue with fixed laws and total deterministic updates. The encoded carrier is `E_ell(x)=(sigma_ell(x), c(ell))`, with the law tag unchanged by the update. Demand both a single-valued task decoder `D` and a single-valued **encoded update** `F` such that:

`D(E_ell(x))=T_ell(x)` and `F(E_ell(x))=E_ell(f_ell(x))`.

**Proposition S3.** If every law separately satisfies both task sufficiency and Seed-update closure, define a graph `G_closed` with an edge `ell--m` when some states have equal Seed values but either unequal present tasks or unequal **next Seed values**. Then the minimum tag alphabet for this stronger contract is exactly `chi(G_closed)`.

The same proper-coloring proof applies to the pair of required outputs `(current task, next Seed value)`; since the tag is fixed, a properly colored code also determines its next tag.

**Strict difference.** Two laws can generate identical *task traces at every horizon* while requiring different next Seed values. Let tasks be constantly zero and Seed value be `a`; one law resets `a` to zero and the other resets `a` to one. For task prediction, no law tag is necessary. For an autonomous transition on the retained Seed code, two tags are necessary. This is the contract distinction between predicting an observable and reproducing the chosen representation's own evolution.

## 6. Simultaneous receiving tasks

For several tasks `T_1,...,T_r` on the same legal worlds, form each task-conflict graph. Their **joint** conflict graph is the union of the individual edge sets. This follows because two laws conflict for the task vector if and only if some coordinate task conflicts.

Thus the minimum shared law-tag alphabet is `chi(G_1 union ... union G_r)`, which can be *strictly larger* than each individual minimum. In a three-law exact test, receiver 1 yields the two-edge path `0--1--2` and needs two tags; receiver 2 yields the edge `0--2` and needs two tags; jointly the graph is a triangle and needs **three** tags. Separate local acceptability is not a joint interface certificate.

## 7. When the generating law can change

The graph formula S3 **does not automatically extend** when a Seed moves into a Tree with a different generating law. Model a finite set of worlds `W`, current law `lambda:W->L`, Seed `sigma:W->S`, task `T:W->Y`, and total update `f:W->W`. A candidate law-tag assignment `c:L->C` defines `E_c(w)=(sigma(w),c(lambda(w)))`.

**Proposition S4 (exact switching-law closure criterion).** There exist both a decoder `D` and autonomous code transition `F` exactly when every `w,v` with `E_c(w)=E_c(v)` satisfy

`T(w)=T(v)` **and** `E_c(f(w))=E_c(f(v))`.

*Proof.* Necessity follows by applying the same `D` and `F` to equal codes. For sufficiency, define `D` and `F` on each occupied code using any representative. The conditions make both choices independent of representative. Extend arbitrarily to unused codes. QED.

For worlds with equal present Seed values, S4 imposes:

1. If their required task or next Seed values differ, their **current-law tags must differ**.
2. Otherwise, **if** their current-law tags coincide, their **successor-law tags must also coincide**.

The second condition is an equality implication involving *different pairs of law labels*, not a fixed conflict edge. Exact finite tag optimization is therefore a constraint-search problem, not automatically a single graph coloring.

**No law-only repair.** Use worlds `p,q` under law 0, `r` under law 1 and `s` under law 2. All present Seed values equal zero. Set tasks `T(p)=T(q)=T(r)=0`, `T(s)=1`. Updates are `p->r`, `q->s`, `r->r`, `s->s`. The tasks of `r,s` require their different law tags. But `p,q` are indistinguishable under any law-only tag, and their successor codes would be different. Thus **no law-tag assignment** yields both task sufficiency and autonomous closure. Replacing `sigma(q)=0` with `sigma(q)=1` adds one source-state distinction and repairs the model with a two-symbol law tag.

**Unexpected consequence.** With all tasks changed to the constant zero, one common law tag gives valid closed dynamics. If the successor laws of `r,s` are given different tags while `p,q` remain merged, the refined code is *not* autonomous. Static decoding is monotone under extra information; autonomous closure of a specifically chosen representation need not be. A more detailed Seed code at the predecessor can repair that failure. This is not an argument against retaining source data.

**Three-law strict example.** With all Seed values zero, tasks `T(A)=T(B)=0`, `T(C)=1`, and updates `A->A`, `B->C`, `C->C`, present task sufficiency needs two law tags, while autonomous code closure needs all three.

## 8. Complexity boundary: every finite graph is realizable

**Proposition S5.** Every finite simple graph `H` can be represented as a task-conflict graph of a finite law/Seed family that is individually sufficient within every law.

*Construction/proof.* Give a law to every vertex. For each graph edge `{i,j}`, create one unique Seed-output symbol `e_ij`. The legal states of laws `i` and `j` each contain one occurrence exporting that symbol, with opposed task values zero and one. No other law exports the symbol. Add a private Seed-output symbol to isolated vertices to keep each legal state set nonempty. Every within-law Seed code appears once, so it is sufficient. Across laws, a conflict occurs exactly for the original edges. QED.

Consequently exact minimum law-tag computation includes ordinary graph coloring as a special case. For an explicit finite contract, deciding whether `k` tags suffice is NP-complete for fixed `k>=3` (membership can be checked by enumerating the declared finite input pairs; hardness is by the construction). It would be unjustified to advertise a polynomial-time universal optimal tagging algorithm. This imports the classical hardness of graph coloring; it is not a new complexity-class discovery.

Useful immediate special cases: no conflicts -> one tag (zero law-id bits); a bipartite conflict graph -> at most two tags; a complete graph on `n` laws -> `n` tags. Disconnected components can reuse the same palette, so the minimum for a disjoint union is the maximum component chromatic number, not the sum.

## 9. Separate BM geometry audit: nine straight segments

The user's finite-sample curve construction distinguishes two possible tasks: (A) find the exact area of the **specified nine-segment polygon**, and (B) find the area under an **unknown curved function** that passes through the ten sample positions. These are not the same task.

For `f(x)=x^2` on `[0,1]`, using ten equally spaced points (nine segments), exact rational arithmetic gives polygonal/trapezoidal area `163/486`, while the true integral is `1/3=162/486`. The discrepancy is `1/486`. It exactly attains the classical composite trapezoidal bound `||f''||_infty/(12*9^2)` for this example.

There is **no universally exact ten-point area method for all smooth curves**. For example, the nonnegative smooth polynomial `g(x)=prod_{k=0}^9 (x-k/9)^2` vanishes at every sampling point but has positive integral; the zero function has identical samples and zero integral. The two tasks produce identical finite data and different correct answers, so the BM task-sufficiency criterion forbids a decoder that always returns the exact continuous area from just those samples. Multiplying `g` by arbitrary positive constants makes the hidden area arbitrarily large. This negative result does not deny that geometry and linear algebra exactly compute **polygonal** area; it specifies the missing regularity or interpolation contract needed for a continuum claim.

## 10. Verification, status, and stopping boundary

The accompanying standard-library script `BM_Seed_Law_Tag_Verifier_2026-11-01.py` verifies the declared finite contracts. Independently structured direct decoder enumeration and the graph-coloring procedure agree on **1,400 random fixed-law horizon instances** and **350 random autonomous-update instances**. Every simple graph on one through five vertices was constructed and recovered (**1,099 graphs**). The finite trace stabilization assertion passed **350 random model tests**. The independent pair-implication test and explicit encoded transition test agreed on **4,434 random switching-law tag assignments**. All specified positive, negative and one-distinction repair examples passed, as did the exact rational nine-segment test. These counts describe test instances, not independent proofs or new mathematical discoveries.

**Status register:**

| Result | Scope and status |
|---|---|
| S1 minimum law tag | Proven for finite legal models with per-law task sufficiency; classical coloring reduction |
| S2 horizon monotonicity/stabilization | Proven for finite deterministic total actions; classical finite-state refinement |
| S3 code-autonomy tag graph | Proven for one total fixed-law update with per-law Seed closure |
| Simultaneous receivers | Proven by union of finite conflict graphs; no cross-receiver resource restriction |
| S4 changing-law condition | Proven for finite total deterministic world transition and explicit task/Seed maps |
| Changing-law model-tag optimization | Exact finite exhaustive procedure; may be infeasible, not claimed efficient |
| S5 arbitrary graph realization and hardness | Explicit reduction; graph-coloring NP-completeness is prior mathematics |
| Nine-segment area audit | Exact finite calculation and general information obstruction; classical analysis |
| General categorical, smooth, probabilistic, quantum, physical Seed mechanism | **Not established**; would require separate typed native semantics and bridges |
| Whole BM historical originality and peer-review certification | **Not established** |

BM's pre-existing six broad open families are not solved here: unrestricted nonlinear Jordan interior optima; global regular realizations/minimal augmentation; constrained or infinite causal realization; unrestricted quantum observable-algebra recovery implementation; nonlinear repair beyond solved contract classes; and further infinite-dimensional native systems. The missing full historical DD sources, independently checked proofs, external novelty review, real-application head-to-head benchmarks, and live calculator/source conformance remain evidence gates. None can be completed by a finite toy example or a new name.

**Stopping rule:** The present finite research questions admit exact answers and have been worked to explicit proofs, witnesses, and tests. Further universal claims require a specified new native category or admissibility law, external source evidence, or independent reviewer; no such input can be fabricated. Preserve frozen V1, append this note as a scoped Volume II candidate, and retain all failures and assumptions.

## Prior-art and project sources

1. *Branch Mathematics V1 Canonical Foundation* (September 2026; Edition 1.1 frozen).
2. *Branch Mathematics Research Edition*, version updated 19 October 2026, BM18-O1–O4.
3. *BM — Correction and Evidence Closure Register* (updated 18 October 2026).
4. *BM Completion and Network Development* (29 October 2026), including Beeri–Fagin–Maier–Yannakakis (1983) and Atserias–Kolaitis (2026) references on relational consistency.
5. *BM Direct Comparison Findings* (29 October 2026), 162 matched internal comparisons.
6. *BM New Uses* (29 October 2026), 24 candidates plus four follow-ups.
7. Aho, Beeri and Ullman, *The Theory of Joins in Relational Databases* (1979), ACM Transactions on Database Systems 4(3).
8. Established finite-state partition refinement, graph coloring, database dependencies, and constraint satisfaction; these are imported algorithms and proof ideas, not BM discoveries.


---

Source: BM_Adaptive_Seed_Acquisition_2026-11-01.md

# Branch Mathematics — Acquiring Seed-law information without probability

**1 November 2026 · Additive Volume II candidate.** This supplement continues the earlier finite Seed provenance and law-tag work. It does not revise the frozen September 12 Version 1 or imply that existing decision-tree, constraint, or control mathematics originated with BM. The application of adaptive experiment selection was already listed in `BM_New_Uses_2026-10-29.md` as E02. The present addition is a precise finite receiver/Passport contract, proofs, counterexamples, and two executable verifiers.

## 1. Motivation: a tag cannot be manufactured

The earlier law-tag theorem computes the least number of law identifiers a receiver would need **if an authorized party could supply a correct tag**. It does not say how a tag is known. When different lawful sources yield the same Seed export, simply appending a guessed law identity would conceal an unresolved distinction rather than repair it.

The correct mathematical question is: Given a family of admissible source worlds and a declared catalogue of safe observations, can a receiver **guarantee** determination of its required task and Passport status? If yes, what is the minimum worst-case observation cost? The model here uses no probability; uncertainty is a set of lawful alternatives.

## 2. Passive, set-valued observations

Let `W` be a finite nonempty set of possible complete source worlds. Let `T:W->Y` be the receiver's demanded result. It may be the vector of a task value **and** Passport status; statuses may include accepted, rejected and not applicable. The current information set is a nonempty `C subset W`.

A probe `q` has strictly positive rational cost `c(q)`, an enabling set `E_q subset W`, and for every `w in E_q` a nonempty set `O_q(w)` of permitted observations. The probe is safe to issue when `C subset E_q`. If the observed value is `o`, the lawful surviving worlds are

`C[q,o]={w in C: o in O_q(w)}`.

A probe must make the information set **strictly smaller on every possible observation** to be useful in a guaranteed finite terminating strategy. If a possible result returns the identical `C`, an adversary respecting the declared set-valued rules can repeat that result indefinitely. With positive cost, a purported optimal terminating protocol can omit that probe; its worst-case cost cannot improve by keeping a branch that reveals nothing.

### Proposition D1 (finite robust adaptive measurement value)

For this static-world, passive-observation contract define

`V(C)=0` if the task `T` is constant on `C`. Otherwise,

`V(C)=min_q [ c(q)+max_{o in O_q(C)} V(C[q,o]) ]`,

where the minimum considers only probes enabled for every world in `C`, all branches are proper nonempty subsets of `C`, and a probe with an infeasible branch has value `+infinity`. When no qualifying probe yields finite cost, `V(C)=+infinity`.

**Proof.** Any guaranteed terminating strategy begins with some safe probe. If its observations include a nonprogressing outcome, the worst-case strategy can be shortened by removing that first probe and following the continuation of the nonprogressing branch immediately; no other branch costs more in a minimax optimum. Otherwise every successor information set is a strict subset, for which an optimal strategy can be obtained inductively by set size. Each possible outcome has its own continuation. The worst-case remaining cost is the maximum of these branch costs; choosing the best first probe gives the minimum. This induction also provides a finite decision procedure and a replayable optimal policy tree. QED.

The output `+infinity` is an **infeasibility certificate relative to the declared observation model**. It does not prove a physical experiment outside that model can never help.

### Strict benefit of adaptivity

Take four possible states `a,b,c,d`, each requiring a distinct answer. Three binary probes of unit cost are supplied:

1. `region`: distinguishes `{a,b}` from `{c,d}`;
2. `left-specific`: separates `a` from `b`, but has no useful split between `c,d`;
3. `right-specific`: separates `c` from `d`, but has no useful split between `a,b`.

An adaptive protocol probes `region` and then selects one specialized probe. Its **worst-case cost is 2**. Any nonadaptive selected subset sufficient for all four states needs all three probes, cost **3**. The verifier exhaustively confirms both minima. Adaptive choice is therefore a real operational benefit under this contract, though the method is classical decision-tree optimization.

### Passport affects the decision cost

Two source laws may demand the same task answer but different Root acceptance statuses. If the task alone is requested, cost zero may suffice. If the receiver must certify `(task,Passport status)`, it may need an extra law-identifying probe. The test implements such a case with minimum costs **0 versus 1**. An output's content does not imply that its Root is accepted.

### Partial availability and adversarial noise

An inexpensive probe available in only one candidate world is not uniformly safe when the receiver cannot tell which world is actual. In a two-world test, the safe universally enabled probe costs 4; the unavailable cheaper probe is correctly excluded.

If a noisy sensor can return one common ambiguous outcome under two task-distinct states, repeated readings may never distinguish them under an adversarial set-valued contract. The test returns infeasible with that sensor alone, and a finite cost of 3 after adding a guaranteed distinguishing fallback. No probabilities or favorable repetition assumptions are smuggled into the conclusion.

## 3. Correlated probes and a persistent hidden witness

**Counterexample to marginal-only reasoning.** Let the source's complete state be `(t,h)` with task bit `t` and a persistent hidden calibration bit `h`. Two deterministic probes are

`q_1(t,h)=h`,

`q_2(t,h)=t XOR h`.

Each probe separately produces both 0 and 1 for both task values; **each marginal probe alone is uninformative**. But the joint pair satisfies `t=q_1 XOR q_2`, so two probes recover the task exactly. The exact finite adaptive solver returns cost **2**.

If the receiver deletes `h` from the model and retains only separate unrestricted outcome sets `{0,1}` for each task state, then every individual observation remains ambiguous and the robust solver correctly refuses certification. It has lost the **shared native witness** that forces the two results to be correlated.

This does not prove that the world has hidden calibration. It proves that a declared lawful joint relation can change the answer to a recovery question. A pair of marginal observation sets is not in general a substitute for the correlated joint source model. This is the same BM principle behind the earlier even/odd three-variable counterexample, now turned into an actionable receiver-observation contract.

## 4. Controlled observations that change the world

The passive recurrence D1 is not valid unchanged when a measurement alters the world, its available actions, or the source law. Define a finite controlled system with a total task map `T:W->Y` and an action catalogue `A`. Each action `a` has positive cost, an enabling subset, and for each enabled world `w` a nonempty finite **joint** relation of observable-successor pairs `K_a(w) subset O_a x W`.

To preserve the task *originally asked*, require that every permitted transition `w -> w'` satisfies `T(w')=T(w)`. If an intervention changes that original answer, either (i) reject it for this contract, or (ii) augment the state with the original target before evaluating its usefulness. Redefining the target after an intervention without saying so is an invalid task switch.

For current information `C`, the action is safely callable only if every possible world enables it. Its possible updated belief after observing `o` is

`C[a,o]={w': exists w in C with (o,w') in K_a(w)}`.

Unlike the passive case, this belief need not be a subset of `C`. Therefore induction on `|C|` is no longer justified.

### Proposition D2 (finite controlled robust diagnosis)

Assume `W` finite, `A` finite, costs strictly positive, and all actions preserve the receiver's declared original task. Consider the finite state space `B` of nonempty subsets of `W`. Initialize `V_0(C)=0` for task-constant information sets and `+infinity` otherwise. Recursively define

`V_{n+1}(C)=min( V_n(C), min_{a enabled on C} [c(a)+max_o V_n(C[a,o])] )`.

Then this iteration, run through at most `|B|` policy steps, yields the exact minimum worst-case cost of a guaranteed finite terminating adaptive policy, or `+infinity` when none exists.

**Proof.** Induction on `n` shows `V_n` is the optimal worst-case cost among strategies guaranteed to terminate in at most `n` further actions. The first action incurs `c(a)` and the adversary chooses among its lawful observations, yielding the maximum continuation cost; the minimum takes the best safe action. The optional `V_n(C)` term allows termination earlier than the horizon. A guaranteed terminating strategy with positive costs cannot improve by revisiting the identical belief set along a possible execution path: at a repeat, it can use the later continuation immediately, saving positive cost while leaving the lawful future belief problem unchanged. Thus an optimal successful strategy can be chosen acyclic on the finite belief-state graph, with depth at most `|B|`. No such strategy exists if the value remains infinite. QED.

This is a standard finite worst-case information-state reachability construction, organized under BM's task, source, action-availability and Passport obligations. It is not a general theorem for arbitrary continuous, stochastic or infinite systems.

### Controlled activation example

Let a world carry a task bit and a readiness mode. Initially a read action is unavailable. A first action activates the mode while preserving the task; a second action reports the task. Both actions cost 1. The exact controlled game returns worst-case cost **2**.

An action that maps two original task-distinct states into one state and thereby changes the declared task is rejected by the verifier. A repeated noninformative action with a shared output is correctly judged unable to guarantee completion.

## 5. Implementation and checks

`BM_Adaptive_Seed_Diagnostics_2026-11-01.py` implements D1, exact finite nonadaptive bundle comparison, source-law Passport tests, partial query availability, adversarial noise, and persistent hidden-witness tests. It passed **200 randomized comparisons** against an independently structured nonmemoized policy enumeration; **151** of those random contracts were infeasible under their declared catalogues.

`BM_Active_Seed_Diagnostics_2026-11-01.py` implements D2 by finite belief-state value iteration and rejects original-task-changing actions. It passed **150 randomized comparisons** against explicit depth-bounded policy-tree enumeration; **84** sampled cases were feasible. The special two-step activation, noninformative-action and forbidden-erasure examples passed.

These are reproducible internal tests of exact finite models, **not independent theorem checking, empirical source accuracy, or evidence of BM-exclusive performance**. The prior BM archive's 162 native-method comparisons reported mathematical agreement; it remains the benchmark baseline rather than a claim of BM superiority.

## 6. New operational rule and stopping boundary

A Seed receiver should return one of four evidence statuses:

1. **Certified:** all surviving lawful worlds agree on task and Passport result.
2. **Acquirable:** a declared safe observation/control policy guarantees certification; report a minimal worst-case policy and cost.
3. **Unresolved within catalogue:** a concrete pair of surviving task-distinct worlds remains, with no permitted guaranteed policy under the supplied model.
4. **Contract missing:** the source-law alternatives, joint observation relation, task, Passport, action availability or cost are not provided; do not invent them.

The four statuses are a proposed finite BM implementation convention, not a new universal metaphysical principle. An unknown source law cannot be identified by asserting a tag. A hidden shared witness cannot be dropped without checking whether it matters. A successful current answer does not establish autonomous closure or receiver acceptance.

The finite passive and controlled problems are now solved under their stated hypotheses. Extending them requires **new information**, not another name: a declared continuous/noisy native observation contract; joint correlations across laboratories/receivers; infinite carriers with effective presentation; distributed communication constraints; empirical calibration; or proof of a field-performance advantage. Without such inputs, further universal conclusions would not be justified.

## Prior work and sources

- *Branch Mathematics V1 Canonical Foundation* (Edition 1.1, frozen 12 September 2026).
- *Branch Mathematics Research Edition*, update of 19 October 2026, BM18-O1–O4.
- *BM Completion and Network Development* (29 October 2026), finite overlapping frames and Seed models.
- *BM New Uses* (29 October 2026), especially experimental-selection application E02.
- *BM Seed Provenance, Law Uncertainty and Closure* (1 November 2026), the directly preceding supplement.
- Laurent Hyafil and Ronald L. Rivest, “Constructing Optimal Binary Decision Trees Is NP-Complete,” *Information Processing Letters* 5(1), 15–17 (1976), author-hosted PDF: https://people.csail.mit.edu/rivest/pubs/HR76.pdf. This paper studies expected decision cost; this supplement uses a different explicitly worst-case contract.
- Ferdinando Cicalese, Eduardo Laber and Aline Medeiros Saettler, “Diagnosis determination: decision trees optimizing simultaneously worst and expected testing cost,” *Proceedings of the 31st International Conference on Machine Learning* (2014), https://proceedings.mlr.press/v32/cicalese14.html. Existing literature directly covers worst-case diagnosis optimization.


---

Source: BM_Seed_Adaptive_Gap_Theorem_2026-11-01.md

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


---

Source: BM_Compact_Seed_Recovery_Theorem_2026-11-01.md

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


---

Source: BM_Dynamic_Seed_Recovery_and_Closure_2026-11-01.md

# Branch Mathematics — Finite-horizon Seed recovery versus autonomous closure

**1 November 2026 · Additive Volume II research note.** This work follows the compact Seed recovery theorems C1–C6 and the finite adaptive Seed diagnostic program. It leaves frozen BM Version 1 unchanged. All results below are conditional classical mathematics (quotient dynamics, compactness, symbolic sequences), framed to clarify BM's separate obligations. No physical theory or uniqueness claim is introduced.

## 1. Three distinct receiver obligations

Let `X` be an admissible native source state space, `F:X -> X` a lawful one-step evolution, `T:X -> Y` the demanded task, and `Q:X -> Z` the Seed representation supplied to a receiver. Distinguish:

1. **Present recovery:** there is a decoder `d` such that `T=d composed with Q`.
2. **Finite-horizon recovery:** for chosen `H`, there are decoders `d_0,...,d_H` satisfying `T composed with F^j = d_j composed with Q` for `0<=j<=H`.
3. **Autonomous closure:** there is a reduced evolution `E:Q(X)->Q(X)` with `Q composed with F = E composed with Q`.

Autonomous closure plus present recovery implies recovery at **every finite time**: `T composed with F^j = d composed with E^j composed with Q`. The reverse implication for any one finite `H` is false.

## Theorem E1 — exact topological closure test

Assume `X` compact, `Z` Hausdorff, `Q:X->Z` continuous, and `F:X->X` continuous. Then a **unique continuous** reduced evolution `E:Q(X)->Q(X)` satisfying

`Q(F(x)) = E(Q(x))`

exists **if and only if** the source equivalence induced by `Q` is forward-stable:

`Q(x)=Q(x')  ==>  Q(F(x))=Q(F(x'))` for all `x,x' in X`.

**Proof.** Necessity follows by applying the same map `E` to equal represented states. Conversely, forward stability makes `E(Q(x)):=Q(F(x))` well defined, and surjectivity onto `Q(X)` makes it unique. A continuous map from compact `X` onto Hausdorff `Q(X)` is a quotient map. Since `E composed with Q=Q composed with F` is continuous, the quotient-map criterion makes `E` continuous. QED.

**Important.** Merely determining `T(x)` from `Q(x)` does **not** establish E1. To claim that a Seed is a self-contained evolving carrier, BM must verify the **stronger** forward-stability property, or retain more native state/history.

## Theorem E2 — finite-horizon observation extraction

Suppose `X` compact Hausdorff; `F` continuous; `T:X->Y` continuous for **finite discrete** `Y`; and an arbitrary (possibly infinite) catalogue of permitted continuous passive probes `{q_i:X->O_i}` with Hausdorff outcome spaces **separates source states** (for every `x!=x'`, some probe has different outputs).

For every finite `H>=0`, there exists a **finite fixed measurement battery** `Q_H` that determines every task value in the time window

`(T(x), T(Fx), ..., T(F^H x))`.

**Proof.** Define the horizon task `T_H:X->Y^(H+1)` by this vector. Composition and finite products preserve continuity, and the target is finite discrete. Full source-state separation implies separation of all task-distinct pairs for `T_H`. Apply compact finite-task observation extraction (C1) to obtain a finite battery with a well-defined continuous decoder for `T_H`. QED.

**Weaker sufficient assumption.** Full source separation is stronger than necessary: it suffices that the probe family separates each pair with a different `T_H` value. Separation of the **present** task `T` alone does not suffice for `H>0`.

**Limitation.** E2 is an existence result *for each given finite horizon*. It does not bound the number of required probes uniformly in `H`, prove autonomy, or provide an effective optimization algorithm.

## Counterexample E3 — every finite horizon works, but no finite experiment knows the whole future

Let `X={0,1}^N` (infinite binary strings) with the compact product topology. Write `x=(x_0,x_1,...)`; let `F(x)=(x_1,x_2,...)` (left shift), and set `T(x)=x_0`. Let allowed probes be **only** the coordinate readings `q_j(x)=x_j`, one unit cost each.

All stated maps are continuous and `{q_j}` separates the source states. For horizon `H`, the future task vector is exactly

`T_H(x)=(x_0,x_1,...,x_H)`.

Each of the `H+1` corresponding coordinate probes is **necessary**: if `q_j` with `0<=j<=H` is not read, choose two strings that agree at every other coordinate but differ at `j`. They have identical observed measurements but different required future outputs. Reading the first `H+1` coordinates suffices. Hence

`minimum fixed finite-horizon cost = H+1`.

Adaptivity **does not help** for this catalogue and task: an adaptive protocol that has not read coordinate `j` cannot infer its value from any other queried coordinates. Under the worst-case source string, all `H+1` coordinates must be read, giving the same minimum adaptive cost `H+1`.

There is **no finite measurement battery** that recovers the **entire infinite future** `(x_0,x_1,...)`. Every finite coordinate selection leaves infinitely many unmeasured bits. Even a protocol with source-dependent finite stopping time cannot recover the entire arbitrary sequence using only finitely many coordinate readings.

Thus E2 does **not** extend to an unlimited horizon merely by repeating the word "compact". The infinite future task has infinitely many possible values; the finite-target hypothesis of C1 fails.

## Counterexample E4 — finite-horizon prediction does not grant closed Seed evolution

Continue with the infinite binary shift above. Select any **finite nonempty** set of coordinate probes `Fset` and write `Q_Fset(x)=(x_j)_(j in Fset)`. Let `m=max(Fset)`.

Choose two native worlds `x,x'` that agree on all coordinates in `Fset` but differ at coordinate `m+1`. Then `Q_Fset(x)=Q_Fset(x')`, while their shifted representations disagree in the coordinate indexed `m`, since `q_m(F(x))=x_(m+1)`.

Therefore the forward-stability criterion E1 fails for **every nonempty finite coordinate set**. Even the first `H+1` probes that perfectly predict the next `H` task outputs cannot be evolved forever by a deterministic map on that finite representation alone.

The empty probe set admits a trivial constant evolution but cannot recover the nonconstant present task. The full infinite coordinate sequence is autonomous, but not a finite Seed export.

## Corollary E5 — a sufficient condition for unlimited prediction

Suppose `Q` recovers `T` through some decoder `d`, and `Q` passes E1's forward-stability test so that a reduced evolution `E` exists. Then **every** future task value is determined by `Q(x)`:

`T(F^j x)=d(E^j(Q(x)))` for every integer `j>=0`.

**Proof.** Induct on `j` to obtain `Q(F^j x)=E^j(Q(x))`; apply `T=d composed with Q`. QED.

This gives a clean BM distinction: finite-horizon knowledge can be purchased with increasing observations, while an autonomous Seed representation must retain information sufficient for *all* its own lawful updates.

## Corollary E6 — robust approximate finite-horizon recovery

Let `X` be compact and `F` continuous. Let `T:X->(Y,d_Y)` and the permitted metric-valued probes be continuous. Assume the whole probe family separates **source states**. Define the finite-horizon metric task

`T_H(x)=(T(x),T(Fx),...,T(F^H x))`,

using the maximum metric on the finite product: `d_H((y_j),(y'_j))=max_(0<=j<=H) d_Y(y_j,y'_j)`.

For every finite `H` and precision `epsilon>0`, there exists a **finite** probe battery and a positive margin `delta` so that measurement-output vectors agreeing within `delta` imply **every** one of the next `H+1` task predictions agrees within `epsilon`.

**Proof.** `T_H` is continuous, and full source-state separation implies separation of task-distinct pairs for `T_H`. Apply compact approximate-recovery theorem C5 to `T_H` with metric `d_H`. If instrument readings have a verified error bound `eta` satisfying `2 eta<delta`, corollary C6 gives the same simultaneous prediction guarantee for every completion consistent with the readings. QED.

**Scope.** The selected battery and the margin may both depend on `H` and `epsilon`. This theorem does not give uniform prediction for unlimited time and does not imply autonomous closure.

## Proposition E7 — finite-horizon information cost cannot decrease as obligations grow

Fix a static source-observation catalogue with a nonnegative cost assigned to each measurement. Let `C_H` denote the minimum **worst-case** cost of an exact diagnostic protocol (fixed or adaptive, considered separately) required to determine all of `(T(x),...,T(F^H x))` for every possible native source. Use `+infinity` if certification is impossible.

Then

`C_0 <= C_1 <= C_2 <= ...`.

**Proof.** Every protocol that certifies the `H+1` horizon also certifies the shorter `H` horizon by discarding the last task output. Therefore the admissible successful-policy set for the longer task is contained in that for the shorter task. Minimizing the same worst-case cost over a subset cannot improve the optimum. QED.

The example E3 makes this inequality **strict at every step**, with `C_H=H+1` for both fixed and adaptive coordinate-probe protocols. The result is a task-obligation monotonicity fact, not a statement that every physical future becomes harder to predict.

## 2. Finite verification analogue

The executable companion `BM_Dynamic_Seed_Closure_Verifier_2026-11-01.py` enumerates binary strings of fixed finite lengths. It implements a finite left-shift register (append `0`), all coordinate readings, and the horizon task. For each short window it exhaustively checks the minimum fixed battery against the exact `H+1` prediction, verifies the failure of closure for every proper nonempty coordinate selection that contains its largest index below the available register end, and verifies that the complete register representation is closed. These finite checks are a regression illustration, not a proof of infinite-sequence theorems E2–E5.

## 3. Registry and research boundary

| Entry | Status | What it establishes |
|---|---|---|
| E1 | Proved, conditional | Continuous autonomous reduced evolution iff represented-state equivalence is forward-stable |
| E2 | Proved, conditional | A finite experiment exists for every requested **finite** prediction horizon under compactness, continuity and suitable observation separation |
| E3 | Proved counterexample | No uniform finite battery for an unlimited future even when every finite horizon is recoverable |
| E4 | Proved counterexample | A finite Seed can forecast a chosen horizon without being autonomously evolvable |
| E5 | Proved corollary | Forward-stable exact representation + present decoder guarantees all future task outputs |
| E6 | Proved corollary | Finite-horizon approximate recovery and bounded-error certification under compactness, continuity and source separation |
| E7 | Proved proposition | Minimum guaranteed cost is monotone as finite prediction obligations are added |

The proof boundaries are essential. A real application still needs an actual native evolution law, topology, lawful measurements, receiver task and Root/Passport semantics. Failing the closure test means *that representation* is insufficient for autonomous evolution; it is not evidence that the source lacks a lawful evolution. These principles are standard in topological dynamics and sufficient-state theory; BM's role is to track their hypotheses, witness information, and receiver obligations together.


---

Source: BM_Finite_Task_Closed_Seed_Quotient_2026-11-01.md

# Branch Mathematics — Finite stabilization and minimal autonomous task-Seed quotient

**1 November 2026 · Additive Volume II finite theorem.** This is the finite deterministic counterpart to *BM Dynamic Seed Recovery and Closure*, E1–E7. Its mathematics is classical partition refinement / finite automaton minimization, not a new independent mathematical invention. It is included because it closes an explicit BM gap between a carrier that reports the current task and a carrier that can update without its discarded source state.

## Contract and native relation

Let `X` be a **finite nonempty** native source world set with `n=|X|`, `F:X->X` a **total deterministic** evolution and `T:X->Y` any task map. Write `m=|T(X)|`, so `1<=m<=n`. For horizon `h>=0`, define the finite observable trajectory

`B_h(x)=(T(x),T(Fx),...,T(F^h x))`

and the equivalence `x ~_h x'` iff `B_h(x)=B_h(x')`.

The partitions `P_h=X/~_h` can only **refine** as `h` increases: adding an obligation cannot merge classes that were already task-distinct.

## Theorem F1 — finite stabilization with a sharp general bound

The sequence of trajectory partitions stabilizes by horizon

`h <= n - m`.

At its first stable index `h*`, equality of the finite trajectories `B_h*(x)=B_h*(x')` is equivalent to equality of **all** future task outputs:

`T(F^j x)=T(F^j x') for every j>=0`.

**Proof.** By construction `P_(h+1)` refines `P_h`. If two consecutive partitions coincide, then `~_h` is forward stable: equality through time `h+1` implies equality of the shifted histories through time `h`. Formally, since `P_h=P_(h+1)`, `x~_h x'` forces `x~_(h+1) x'`, hence `F(x)~_h F(x')`. Induction gives equality of the task at every later time, so no further refinement can occur.

If a step is **not** stable, it strictly increases the number of partition blocks by at least one. `P_0` has `m` blocks and there can be at most `n` blocks. Thus the number of strict refinement steps before stabilization is at most `n-m`, proving the bound. At stabilization the finite-horizon equivalence equals full-future task equivalence. QED.

### Sharpness witness

For any `n>=2`, let `X={0,...,n-1}`, `F(i)=min(i+1,n-1)`, and `T(i)=1` only at `i=n-1`, `0` otherwise. Then `m=2` and the backward chain of task-distinguishable states separates **one new class per step**, reaching the stable partition first at `h*=n-2=n-m`. Thus the bound is attained.

For `m=1` the task is constant everywhere, and stabilization is immediate at `h*=0`.

## Theorem F2 — canonical minimal closed Seed for the task

Let `h*` be the first stable index and define `Q*(x):=[x]_(~_h*)` (the equivalence class of `x` under equal whole-future task behavior). Then:

1. **Exact current task recovery:** `T=d composed with Q*`, with `d([x])=T(x)`.
2. **Autonomous evolution:** `F*([x])=[F(x)]` is a well-defined map on the quotient, and `Q* composed with F = F* composed with Q*`.
3. **All future tasks:** `T(F^j x)=d((F*)^j(Q*(x)))` for every `j>=0`.
4. **Minimality:** if another representation `R:X->Z` recovers `T` and has any deterministic reduced evolution `G:R(X)->R(X)` satisfying `R composed with F=G composed with R`, then

   `R(x)=R(x') ==> Q*(x)=Q*(x')`.

   Consequently `|R(X)| >= |Q*(X)|` and `Q*` factors uniquely through `R(X)`. Up to relabeling its classes, `Q*` is the **coarsest exact autonomous task-sufficient Seed representation**.

**Proof.** Items 1–3 follow from the stabilized forward-invariant equivalence and the induced maps. For item 4, if `R(x)=R(x')`, determinism of `G` gives `R(F^j x)=R(F^j x')` for all `j`, and its task decoder gives `T(F^j x)=T(F^j x')` for all `j`. By F1, `x~_h* x'`, hence `Q*(x)=Q*(x')`. Define `p(R(x)):=Q*(x)`; the implication makes `p` well defined and proves `Q*=p composed with R`. A surjection `p:R(X)->Q*(X)` yields the cardinality inequality. QED.

This is a statement about **task-relative lawful compression**, not about destroying physical information. Native states can share the same minimal Seed precisely when no allowed future iteration of `F` changes the demanded task distinction.

## Observation availability is a separate obligation

Even when `Q*` exists and is mathematically minimal, a receiver cannot assume it can measure `Q*` from an arbitrary initial export. For example, in the two-bit system `X={00,01,10,11}`, let `F` swap the bits and let `T` read the first bit. Current-task observation `q(x)=first bit` recovers `T`, but states `00` and `01` share `q` while their next task bits differ; the current export cannot determine the closed class. An additional permitted reading of the second bit would resolve it. This preserves BM's distinction between **a necessary representation** and **an authorized realizable measurement**.

## Proof checker and scope

`BM_Finite_Task_Closure_Verifier_2026-11-01.py` performs exact random finite map/partition refinement, verifies the `n-m` bound, checks the transition congruence, verifies that stable horizon distinguishes all task-future pairs, exhaustively enumerates all possible finite representations for small sizes to check coarsest-quotient minimality, and tests the sharpness chain family. The enumerations are independently useful regressions but not a substitute for F1/F2 proofs.

**Boundary:** finite `X`, deterministic total native `F`, exact declared task `T`. Nondeterministic transitions, interventions, changing law passports, source-driven observation noise and unrestricted infinite systems require separate conditions; transplanting this finite stabilization bound to those contexts is unjustified.

## Registry

| ID | Status | Result |
|---|---|---|
| F1 | Proved finite theorem | The task-history partition stabilizes by `n-m`; sharp for a deterministic chain |
| F2 | Proved finite theorem | Stable partition yields a unique minimal extensional autonomous task quotient |
| F3 | Proved counterexample | Present-task measurable does not imply minimal autonomous Seed measurable |

**Prior-art crosswalk:** partition refinement, Moore minimization of deterministic automata, Myhill–Nerode future-equivalence, quotient/congruence dynamics. BM applies their distinction between observation, continuation, and the receiver task to its Seed/Root/Passport status system. Independent historical novelty and practical superiority remain unestablished.


---

Source: BM_Joint_Receiver_Closure_and_Seed_Gluing_2026-11-01.md

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


---

Source: BM_Set_Valued_Seed_Closure_and_Branching_2026-11-01.md

# Branch Mathematics — Set-valued Seed closure, branching, and receiver noncomposition

**1 November 2026 · Additive Volume II finite conditional theorem and counterexamples.** This is an extension of the deterministic minimal-Seed quotient F1/F2 to a finite **set-valued** native evolution. It uses classical strong bisimulation and partition refinement. It is not a proposed universal physical law, a novelty claim, or an alteration of frozen BM Version 1.

## 1. State and lawful-response contract

Let `X` be finite and nonempty, `|X|=n`. Let `K:X->P_+(X)` assign every native state a **nonempty set of lawful successor states**. Let `T:X->Y` be the receiver's demanded task, with `m=|T(X)|`. The alternative successors are lawful possibilities, **not probabilities**.

An exact reduced representation `Q:X->Z` is **task-respecting** when `T` factors through `Q`. It is **branch-preserving closed** when there is a well-defined reduced set-valued map `Kbar:Q(X)->P_+(Q(X))` such that

`Kbar(Q(x)) = {Q(x') : x' in K(x)}`

for every native state `x`.

Hence two states may be merged only if they share the task value **and** the same set of possible reduced successor classes. This is the exact stepwise branching contract; it is stronger than merely having identical sets of eventual task trajectories.

## Theorem N1 — finite minimal exact branch-preserving Seed quotient

Start with partition `P_0` by equal current task value. Given any partition `P_r`, refine each block by its **successor-class signature**

`S_r(x) = { [x']_(P_r) : x' in K(x) }`.

Thus `x` and `y` remain in the same block of `P_(r+1)` exactly when they were in the same block of `P_r` and `S_r(x)=S_r(y)`.

**Claims:**

1. The partition sequence stabilizes by `r <= n-m` refinement steps.
2. The stable partition `P*` is task-respecting and induces a well-defined branch-preserving reduced relation `Kbar`.
3. It is **coarsest** among all task-respecting branch-preserving equivalence relations: every other lawful representation's partition refines `P*`.
4. Up to class relabeling, `P*` is the unique minimal extensional strong-bisimulation task quotient for this contract.

**Proof.** `P_(r+1)` only subdivides blocks of `P_r`, never merges them. If it differs strictly, the block count increases by at least one; it begins at `m` and cannot exceed `n`. Thus it becomes constant after at most `n-m` refinements. At stability, states in one block have the same current task and identical successor-block sets, so `Kbar` is well defined and the quotient preserves the declared branch relation.

For minimality, take any task-respecting partition `R` such that native states in one R-block have identical sets of R-successor blocks. `R` refines `P_0`. Assume inductively that `R` refines `P_r`. The equal R-successor-block sets then project to equal `P_r`-successor-block sets, so states equivalent under `R` remain together under `P_(r+1)`. By induction `R` refines every `P_r` and hence `P*`. Therefore `P*` is coarsest admissible, with the fewest blocks. QED.

This is a **finite constructive answer** to BM's question of which branch distinctions must remain in a self-contained, response-complete Seed representation. The answer is relative to the specified task `T` and lawful response relation `K`.

## Counterexample N2 — identical future output sets need not preserve branching

Take seven native states `x,y,u,v,w,b,c` with task values

`T(x)=T(y)=A`, `T(u)=T(v)=T(w)=B`, `T(b)=0`, `T(c)=1`.

Lawful successor sets:

* `K(x)={u}`; `K(y)={v,w}`.
* `K(u)={b,c}`; `K(v)={b}`; `K(w)={c}`.
* `K(b)={b}` and `K(c)={c}`.

From both `x` and `y`, the entire possible infinite output-trace set is **exactly** `{A,B,0,0,0,... ; A,B,1,1,1,...}`. Therefore any representation storing only *which complete task traces are possible* merges `x` with `y`.

Nevertheless `x` and `y` are **not** strong-bisimilar. The sole successor `u` of `x` offers both distinct next-task branches `0` and `1`, while `y` has separate successor states `v` (only `0`) and `w` (only `1`). No one of those two states can match all the branching options of `u`. The fixed-point partition algorithm splits them.

This distinction is material if future observation or control occurs **between** branching events: the available continuations at that intermediate point matter, not just the eventual set of complete histories. For a receiver interested only in trace sets with no intermediate decisions, the **weaker** trace-equivalent quotient may be legitimate; N1's stronger contract must not be imposed silently.

## Counterexample N3 — deterministic joint-receiver meet fails for set-valued laws

The deterministic joint-receiver result J1 showed that the minimal joint task quotient is the intersection of the two individual future-task equivalences. **That rule cannot simply be copied to set-valued branch-preserving closure.**

Let native states be `x,y,00,01,10,11`. The last four states self-loop. Define

`K(x)={00,11}` and `K(y)={01,10}`.

Receiver A asks for the **first bit** on the four terminal states; receiver B asks for the **second bit**. Assign both roots `x,y` a current task value `0` for both receivers.

Each receiver alone judges `x` and `y` equivalent under its minimal branch-preserving quotient: A sees next-task values `{0,1}` from either root, and B sees the same values `{0,1}`. Each has matching successor classes within its own partition.

But the joint receiver sees distinct **paired** successor sets:

* From `x`: `{(0,0),(1,1)}`.
* From `y`: `{(0,1),(1,0)}`.

So the *joint* minimal branch-preserving quotient **must distinguish** the roots. The intersection of the two individual equivalences merges them and is **not itself a lawful joint branch-preserving quotient**.

This is a precise common-witness obstruction to composing separately correct local response summaries; it is the set-valued analogue of discarding shared correlations. Retaining only independent per-receiver successor marginals erases the allowable **pairing** of branch outcomes.

## Verification and limitations

The companion executable `BM_Set_Valued_Seed_Closure_Verifier_2026-11-01.py` constructs exact finite set-valued relations and validates N1 against independently enumerated candidate partitions for small systems. It verifies the seven-state trace-versus-branch counterexample N2 and the two-receiver pairing counterexample N3. As before, randomized finite checks are regression evidence, while the stated general finite proofs establish the theorem.

**Scope boundaries:** native law `K` is a fully specified set-valued one-step relation on a **shared, fixed** finite source space; every successor step remains within that space. N1 does not automatically cover uncontrolled infinite worlds, native law changes, stochastic source laws, history-dependent interventions, transition labels or asynchronous interfaces. Those require explicit extension contracts and cannot inherit the finite theorem merely because a relation is called a Tree or Seed.

## BM status registry

| Entry | Status | Result |
|---|---|---|
| N1 | Proved finite conditional theorem | Coarsest task-respecting strong-bisimulation quotient by finite partition refinement; stability by `n-m` |
| N2 | Proved counterexample | Equality of complete output-trace sets does not entail branch-preserving closure |
| N3 | Proved counterexample | Meet of individually adequate set-valued receiver quotients need not preserve lawful joint branching |

**Prior art:** strong bisimulation, coinductive behavioral equivalence, partition-refinement algorithms, and trace-versus-branching equivalence in labeled transition systems. BM's contribution in this note is a precise application with source, task, carrier and common-witness requirements, not a claim to having invented these classical results.
