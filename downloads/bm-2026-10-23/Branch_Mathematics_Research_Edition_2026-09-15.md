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

For general $n,d$, the first formula is proved **only for linear encoders**. The continuous nonlinear extension is proved above for $n=2,d=1$. The next chapter gives the stronger current-output and omitted-coordinate endpoint results from [R12]. The full trajectory optimum for smaller continuous nonlinear codes remains open.

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

for every nonzero ε. This includes √T for p=2 and 1 for p=∞. For 1≤d<n-1, this lower bound does **not** determine the complete finite-ε trajectory optimum. The exact linear answer from the closure supplement [C11] remains an upper bound for the nonlinear class. Historical novelty of this obstruction has not been established.

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
from [Beny2009, Theorem 3.1]. On task observables $P_{\mathcal A}^\dagger(X)=X$, and the completely bounded norm controls the unamplified operator norm. Thus $\delta\le2\sqrt\beta\le2r\sqrt\kappa$. The bound by two follows from contractivity of unital channel adjoints. Finally use $\kappa\le2\eta$.

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

**Beny2009.** Cedric Beny. Conditions for the approximate correction of algebras. TQC 2009, LNCS 5906, pp. 66-75. The upper estimate in Theorem 3.1 is used for the quantum recovery bound. [Author preprint](https://arxiv.org/abs/0907.4207).

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
