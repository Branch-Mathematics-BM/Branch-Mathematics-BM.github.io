---
title: "Branch Mathematics"
subtitle: "Foundations, Exactification, Descent, Realization, and Closure Price"
author: "Canonical Version 1 Foundation"
date: "September 2026"
lang: en-US
---


# Contents {.unnumbered}

**1.** Why Branch Mathematics Is Needed  
**2.** The Version 1 Architecture  
**3.** Exact Representation and Task Sufficiency  
**4.** Contextual Equivalence and Exactification  
**5.** Dynamic Closure and Contract-Indexed Descent  
**6.** Simultaneous Branch Interface Synthesis  
**7.** Successor Fibres and Approximate Dynamic Closure  
**8.** Witness Reuse, Path Lifting, and History  
**9.** State, Memory, Locality, and Communication  
**10.** Adaptive Passports  
**11.** Temporal Quotients and Retention Cost  
**12.** Approximate Temporal Cascades  
**13.** Smooth and Nonlinear Contract-Indexed Descent  
**14.** Continuous and Smooth Realization  
**15.** Closure Price: Exact Dynamic Closure Versus Free Approximation  
**16.** Jordan Chains and Orbit Width  
**17.** Linear Compatibility and Repair  
**18.** Nonlinear Resonance and Regularity Price  
**19.** Infinite-Dimensional Example: The Heat Cascade  
**20.** Stochastic Branch Mathematics  
**21.** Quantum Branch Mathematics  
**22.** GURF: The Response-Specialized Layer  
**23.** Failure Atlas  
**24.** Canonical Status Registry  
**25.** Open Problems and Research Program  
**26.** Verification, Reproducibility, and Limits  

**Back matter:** Version History and Freeze Policy; References; Appendix A: Canonical Edition 1.1 Review Text.


# Preface {.unnumbered}

**Canonical status:** Version 1 foundation, frozen after the 12 September 2026 Edition 1.1 verification amendment.

**Scope statement.** This volume preserves the internally verified mathematical foundation of Branch Mathematics and the GURF response layer. It distinguishes proved source results, results proved in the September review, classical imported mathematics, BM-specific synthesis, counterexamples, and open research problems. It makes no claim of independent peer review, formal proof-assistant certification, or historical priority for Branch Mathematics as a whole.

> **Foundation Freeze Statement.** The definitions, theorem architecture, descent principles, realization distinctions, and status boundaries in this volume constitute the canonical Version 1 foundation of Branch Mathematics. Future developments may extend, specialize, or apply this foundation, but should not alter its core definitions or theorem dependencies unless a demonstrated contradiction or counterexample requires correction.

The governing review source is **Branch Mathematics: Source review, corrected core, and scoped mathematical completion, Edition 1.1 - verification amendment, 12 September 2026**. Edition 1.0 is historical and superseded.

Branch Mathematics began with a practical mathematical difficulty: a single serious problem often has to be carried through several kinds of mathematics at once, while each kind of mathematics has its own objects, notions of admissibility, equivalence, approximation, continuation, and physical realizability. A representation can be sufficient for a current task and still fail under time evolution. Two local interfaces can each be sufficient and still fail jointly. An algebraic quotient can exist while no smooth quotient of the desired type exists. A quantum observable can be recoverable algebraically while no physical reduced channel exists. A low-dimensional approximation can be excellent while exact autonomous closure remains expensive.

The purpose of Branch Mathematics is to make those distinctions explicit and composable. It does not replace topology, probability, operator theory, control theory, category theory, communication complexity, or any other native discipline. Instead it asks a disciplined sequence of questions: what distinctions does the declared contract require; which of those distinctions survive a proposed representation; do the native operations descend; can the resulting abstract interface be realized in the requested category; and what price is paid when exact realization is restricted or approximated?

Version 1 is now frozen because the foundation has both positive theorems and negative theorems. The theory no longer assumes that every desired coarsest realization exists. It records when smoothness, locality, physicality, topology, memory, or communication impose additional costs. It also records when a claimed implication is false.

This book is therefore a foundation volume, not a claim that the research program is finished. The goal is archival stability: a future reader should be able to reconstruct the Version 1 mathematics without access to the chat history from which much of the development emerged.

## Status legend {.unnumbered}

- **[SC] Source-certified.** Proved in the canonical 10-11 September source corpus and retained by the 1.1 audit.
- **[RP] Review-proved.** Proved in the 12 September Edition 1.1 review or re-proved in this volume.
- **[CI] Classical/imported.** Standard mathematics used in its native scope.
- **[BM-SYN] BM synthesis.** A Branch Mathematics placement or synthesis of established ingredients; no historical novelty claim is implied.
- **[FW] Firewall.** A counterexample or restriction preventing an invalid generalization.
- **[OPEN] Open.** An explicit unresolved mathematical question.

Original public theorem identifiers T01-T55 remain stable. Book theorem labels organize exposition only and do not replace the source registry.


# Why Branch Mathematics Is Needed

The need for Branch Mathematics is not that mathematics lacks theories of quotient spaces, observability, lumpability, communication, smooth realization, or channel compression. Those theories already exist and must be respected. The need is that a single problem may require several of them simultaneously, and the strongest valid interface depends on the declared task and realization class.

Consider five failures that occur in ordinary reduction work.

First, **static sufficiency need not imply dynamic closure**. A representation may determine the current output while merging states whose future outputs differ. Second, **local sufficiency need not imply joint sufficiency**. Marginal Markov behavior can agree while correlations differ; local quantum observables can be preserved while an entangling future observable is lost. Third, **set-level exactness need not imply regular realizability**. A quotient may exist abstractly while no continuous, smooth, or submersive realization of the desired form exists. Fourth, **algebraic recoverability need not imply physical realizability**. A linear reduced quantum map may exist yet fail positivity. Fifth, **approximation quality need not imply autonomous compatibility**. Independently optimal low-rank models at consecutive horizons may not chain into one lawful reduced dynamics.

Branch Mathematics treats these not as exceptions to be patched after the fact, but as different gates in a single typed pipeline.

![The frozen Version 1 mathematical spine.](figures/bm_pipeline.png){width=95%}

The central discipline is simple:

\[
\boxed{\text{Specify} \to \text{Distinguish} \to \text{Descend} \to \text{Synthesize} \to \text{Realize} \to \text{Quantify}.}
\]

A *Branch* carries native mathematics. An *Interaction* is an actual typed native operation. A *Leaf* records a derived result with hypotheses and provenance. A *Tree* is the realized dependency structure. A *Passport* is the instantiated contract that says what must be preserved and accepted. A *Root* is a receiver-accepted export. These names organize mathematics; they do not create missing existence theorems.

The decisive principle is receiver-relative necessity. Two native states may be equivalent for one task and distinct for another. A distinction may be unnecessary now but necessary after one continuation step. A distinction may be needed by a local substitute even when a centralized statistic can forget it. Branch Mathematics therefore does not assign one universal scalar amount of information to a system. It computes the equivalences and realization costs induced by declared obligations.


# The Version 1 Architecture

## Native-sector integrity

Every Branch keeps its native objects, operations, topology, order, positivity, probability law, or physical admissibility conditions. No theorem proved for deterministic functions is silently promoted to Markov kernels, quantum channels, partial relations, or smooth manifolds. Bridges must state what is transported and what additional hypotheses are required.

## Receiver-relative specification

A representation is never called sufficient in the abstract. Sufficiency is with respect to a task family, continuation family, Interaction family, or receiver contract. This prevents a central source of ambiguity: the same quotient may be exact for one receiver and invalid for another.

## Three closure notions that must not be conflated

Version 1 keeps three different closure mechanisms separate:

1. component dependency closure on configuration components;
2. prerequisite/obligation closure on obligations;
3. refinement/exactification on equivalence relations.

Their domains and order structures are different. Similar vocabulary is not a mathematical identification.

## GURF under BM

Branch Mathematics owns the domain-independent representation and transformation mathematics. GURF is the response-specialized layer: it organizes tasks, observations, continuation, interventions, inverse recovery, memory, and repair. Core, SOE, ACE, IRE, UKE, HDE, and GHSE retain their roles. GRDE remains frozen at 008. Rooting, Rebranching, and Seed remain candidate structures except where a native theorem supplies them.

## The dependency order

The frozen dependency order is:

> Native objects and laws -> receiver obligations -> required distinctions -> descent.
>
> Abstract interface -> native realization -> cost and stability -> receiver export.

The ordering matters. If one starts by choosing a preferred coordinate system or model class, then asks what tasks it preserves, the result is a model-selection exercise. BM starts from the contract and derives what may legally be merged before optimizing a realization.


# Exact Representation and Task Sufficiency

**[SC][CI] Fibre factorization.** Let \(R:X\to Z\) and \(T:X\to Y\). There exists a function \(\bar T:R(X)\to Y\) with

\[
T=\bar T\circ R
\]

if and only if

\[
\boxed{\ker R\subseteq\ker T.}
\]

The proof is elementary and foundational. If \(T=\bar T R\), equal representation values force equal task values. Conversely, if task values are constant on each fibre of \(R\), define \(\bar T(Rx)=T(x)\); fibre constancy makes the definition well defined.

Several consequences follow immediately. The decoder need only be defined on the realized image \(R(X)\). No continuity, linearity, measurability, positivity, or physical admissibility follows unless separately required. Exactness is therefore a statement about distinctions, not automatically about realization quality.

## Partial tasks and definedness

For a partial task \(T:D_T\subseteq X\to Y\), applicability can itself be behavior. Introduce a tag \(\bot\) and define

\[
\widetilde T(x)=
\begin{cases}
T(x),&x\in D_T,\\
\bot,&x\notin D_T.
\end{cases}
\]

Then ordinary fibre factorization applies to \(\widetilde T\). This prevents an invalid quotient from merging a state where the task is defined with a state where it is not.

## Families of tasks

For a family \(\mathcal Q\), define

\[
E_{\mathcal Q}=\bigcap_{T\in\mathcal Q}\ker T.
\]

This is the coarsest set-level equivalence preserving every task in the family. It is semantic: it records the declared behavior, not a choice of algorithm for computing the quotient.


# Contextual Equivalence and Exactification

The first major BM construction is exactification: starting from a contract and, if necessary, a legacy representation that must remain recoverable, derive the coarsest equivalence stable under the declared future contexts.


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

Conversely, let H be an equivalence contained in ker R∩E_Q and stable under M. If x H y, then mx H my for every m; therefore R(mx)=R(my) and T(mx)=T(my). Thus H⊆E#. Apply this to H=ker S. Fibre factorization gives the unique induced quotient map. ∎

For an arbitrary input equivalence E, define

\[
\mathfrak E_Q(E)=\bigcap_{m\in M}(m\times m)^{-1}(E\cap E_Q).
\]

It is monotone and contractive. Applying it twice introduces composites mn and duplicates already-required task tests. Since M is a monoid and contains the identity, those tests are exactly the original tests, proving idempotence. This is an interior/refinement operator in the inclusion order on equivalences; calling it an extensive closure in that order would reverse the meaning.

For partial operations, use an explicit unavailable tag and preserve the actual composition domains. Arbitrary partial tasks cannot be treated as ordinary total maps without this change. For stochastic or game semantics, replace the deterministic statement by the corresponding native theorem.


## Context families without a monoid

A monoid is required for the idempotent exactification operator above, but not for the bare semantic notion of contextual equivalence. Given any family \(\mathcal C\) of tests or contexts,

\[
xE_{\mathcal C}y\iff C(x)=C(y)\quad\forall C\in\mathcal C
\]

is an equivalence whenever the codomain equalities are ordinary equalities. The monoid assumption becomes relevant when the family is intended to be stable under repeated continuation and one wants a one-step exactification operator to already contain all composites.


# Dynamic Closure and Contract-Indexed Descent

Static task sufficiency does not imply that the representation can evolve autonomously. This is the central reason continuation enters BM as a separate gate.

For a total deterministic map \(f:X\to X\), a representation \(R:X\to Z\) admits a reduced map \(\bar f\) satisfying

\[
R f=\bar f R
\]

if and only if

\[
\boxed{\ker R\subseteq\ker(Rf).}
\]

For partial operations one must also preserve applicability: each representation fibre must lie entirely inside or entirely outside the operation domain.

## Contract-indexed descent

The stationary equation \(Rf=\bar fR\) is not the most general form. Suppose the current contract uses an equivalence \(E_v\) and the next contract uses \(E_w\). A reduced transition exists exactly when

\[
\boxed{xE_vy\Longrightarrow f(x)E_wf(y),}
\]

or equivalently

\[
\boxed{E_v\subseteq(f\times f)^{-1}(E_w).}
\]

Then the quotient map is well defined by \([x]_{E_v}\mapsto[f(x)]_{E_w}\). Ordinary Dynamic Closure is the special case \(E_v=E_w\).

![Stationary closure is a special case of contract-indexed descent.](figures/contract_indexed_descent.png){width=82%}

This reformulation becomes essential when obligations expire, contexts are revealed, or a finite-horizon task counts down. The interface is allowed to change when the contract changes, but it may change only through a lawful descent.


# Simultaneous Branch Interface Synthesis

A difficult problem rarely contains one isolated representation. Multiple Branches interact, and an interface that is locally sufficient can still fail when substituted into an Interaction. The finite T55 family addresses this by refining all Branch equivalences simultaneously.

For finite carriers \(X_i\), initial equivalences \(B_i\), local successor relations, and partial Interactions, the source construction iterates

\[
E_i^{k+1}=E_i^k\cap\bigcap_a\ker S_{L_{i,a},E_i^k}\cap\bigcap_{b,p:i_p=i}C_{b,p}(E_{r(b)}^k),
\]

with an explicit undefined tag for partial outputs. Every strict round splits at least one class, so finite termination is bounded by the total available class increases.

**[SC] T55-C7/C7R.** In its declared finite Cartesian-context setting, the terminal family is the unique coarsest exact collection of Branch-local interfaces preserving tasks, successor signatures, Interaction definedness, and Interaction output classes.

The qualification is structural, not cosmetic. Cartesian contextual substitution asks each Branch interface to remain valid while the other inputs range independently through their admissible classes. If native admissibility correlates the inputs, full Cartesian substitution can over-refine. BM therefore records the context family as part of the contract.

## Beyond finite carriers


The source T55 construction also has a set-level existence extension. Keep a set-indexed family of carriers X_i, initial equivalences B_i, action relations, and finite-arity partial Interactions, with the same independently substitutable Cartesian contexts as E chapter 3.

On

\[
\mathcal L=\prod_i[\Delta_{X_i},B_i]
\]

define F by the source refinement formula: intersect the current equivalence with equal successor signatures and equal tagged contextual output classes. This is a monotone, contractive map of a complete lattice. Monotonicity follows because equality of successor classes under a finer equivalence implies equality after passing to coarser classes, and likewise for tagged Interaction outputs.

**Theorem.** A unique coarsest exact equivalence family exists in this set-level class. It is the greatest fixed point of F below B.

**Proof.** Start at B, iterate F at successor ordinals, and intersect all earlier equivalences at limit ordinals. Every strict step removes a pair from a set of available pairs, so this descending construction must stabilize at some ordinal. Its fixed point satisfies the source descent obligations. Every other admissible family H remains contained in each stage: the successor step is the source monotonicity argument, and the limit step is intersection. Thus the terminal family contains every admissible H and is uniquely coarsest. ∎

This is an application of classical complete-lattice fixed-point reasoning, not a new fixed-point theorem. [Tarski, *A lattice-theoretical fixpoint theorem and its applications*, Theorem 1](https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-p.pdf).

The result gives neither finite termination nor a computable procedure on arbitrary infinite presentations. In particular, it does not assert that countably many rounds suffice for arbitrary infinitely branching relations, or that the resulting equivalence has a continuous or smooth realization.


The set-level theorem is an existence result. It supplies neither finite termination nor a computational procedure on an arbitrary infinite presentation. Regularity of the quotient is a later realization question.


# Successor Fibres and Approximate Dynamic Closure

A representation that is not exactly closed still has an exact set-valued one-step semantics. Let \(\Phi:X\to X\) and \(R:X\to Q\). Define the canonical successor multifunction

\[
\boxed{\mathcal S_R(q)=\{R(\Phi x):R(x)=q\}.}
\]

Exact Dynamic Closure holds if and only if every successor set is a singleton. This yields a natural ambiguity measure

\[
\alpha(R)=\sup_q\operatorname{diam}\mathcal S_R(q).
\]

For an unrestricted deterministic reduced predictor \(F:Q\to Q\), the best possible one-step error is the Chebyshev radius of the successor fibres:

\[
\boxed{\delta_1^*(R)=\sup_q\operatorname{rad}\mathcal S_R(q),}
\]

hence

\[
\frac12\alpha(R)\le\delta_1^*(R)\le\alpha(R).
\]

This equality is exact only for the declared unrestricted predictor class. Continuity, linearity, CPTP physicality, or other realization constraints can increase the optimum.

## Long-time ambiguity

Define the actual depth-\(k\) future set

\[
\mathcal S_R^{(k)}(q)=\{R\Phi^kx:R(x)=q\}
\]

and

\[
\alpha_k(R)=\sup_q\operatorname{diam}\mathcal S_R^{(k)}(q).
\]

Let the successor multifunction have Hausdorff modulus

\[
h_R(r)=\sup_{d(q,q')\le r}d_H(\mathcal S_R(q),\mathcal S_R(q')).
\]

Then

\[
\boxed{\alpha_{k+1}\le\alpha_1+h_R(\alpha_k).}
\]

If \(h_R(r)\le Lr\),

\[
\alpha_k\le\alpha_1\sum_{j=0}^{k-1}L^j,
\]

and for \(L<1\), \(\alpha_k\le\alpha_1/(1-L)\).

A set-theoretic selector \(F(q)\in\mathcal S_R(q)\) gives an autonomous **predictor**, with the same recurrence for its prediction error. It is not automatically a native-liftable reduced realization. Path lifting is a separate obligation.


# Witness Reuse, Path Lifting, and History

One-step quotient correctness can fail at the level of complete trajectories because a set-valued quotient relation can switch hidden witnesses at intermediate states.

For a reduced path \(\pi=(q_0,\ldots,q_k)\), define its completion fibre

\[
\boxed{\mathfrak C(\pi)=\bigcap_{j=0}^{k}\Phi^{-j}(R^{-1}(q_j)).}
\]

The path is genuinely realized by one native initial state if and only if \(\mathfrak C(\pi)\neq\varnothing\).

Define the current completion set

\[
B(\pi)=\Phi^k\mathfrak C(\pi).
\]

Appending a candidate next code \(q'\) gives the exact recursion

\[
\boxed{B(\pi q')=\Phi(B(\pi))\cap R^{-1}(q').}
\]

![A quotient relation can permit a path assembled from incompatible hidden witnesses.](figures/witness_switching.png){width=78%}

This distinguishes four notions:

1. one-step successor correctness;
2. endpoint correctness at a fixed depth;
3. whole-trace realizability;
4. strong representative substitutability.

The memoryless quotient relation is trace-exact exactly when historical narrowing of the completion set never removes a successor still advertised by the coarse state:

\[
\boxed{\mathcal S_R(B(\pi))=\mathcal S_R(q_k)}
\]

for every realizable prefix \(\pi\).

For finite native state spaces, completion-state dynamics gives a finite witness-preserving automaton. Raw completion sets are generally not minimal. Two histories may be merged whenever they induce the same residual future language; this is the classical Myhill-Nerode idea placed inside HDE.

For infinite paths, finite-prefix realizability alone is insufficient in arbitrary spaces. A standard compactness route works when the nested completion sets are nonempty and closed inside a compact initial fibre.


# State, Memory, Locality, and Communication

The word *memory* hides several mathematically different architectures. Version 1 keeps them separate.

## Latent memory initialized from the native state

Let \(E_*\) be the complete future-behavior equivalence required by the contract, including future legacy values if the legacy interface itself is retained. Fix \(R:X\to Q\). For each visible code \(q\), let \(n_R(q)\) be the number of \(E_*\)-classes intersecting \(R^{-1}(q)\). If an auxiliary state \(A(x)\) may inspect the native state initially, then

\[
\boxed{|\mathcal A|_{\min}=\max_q n_R(q).}
\]

The proof is exact pigeonhole reasoning inside each visible fibre: distinct required classes need distinct auxiliary labels, while labels may be reused across different visible codes.

## Autonomous memory initialized only from the coarse interface

If the auxiliary state receives no information beyond \(R(x)\), deterministic recurrence cannot reconstruct distinctions already merged by \(R\). Exact future behavior therefore still requires

\[
\ker R\subseteq E_*.
\]

A downstream recurrent network does not reverse an irreversible merger without new observations.

## Observation-derived history memory

History memory is different because later observations carry new information. The completion-state update above filters the native possibilities. The minimal exact finite history state is obtained by quotienting realizable histories by equality of residual future languages.

## Branch-locality surcharge

Let

\[
B:Z_1\times\cdots\times Z_m\to Y
\]

be complete receiver behavior. Define the Branch-\(i\) contextual equivalence by

\[
z_i\sim_i z_i'\iff B(z_i,c_{-i})=B(z_i',c_{-i})\quad\forall c_{-i}.
\]

Then \(Q_i=Z_i/\!\sim_i\) is the coarsest exact independently substitutable interface for Branch \(i\). In finite systems, if \(N_{\mathrm{joint}}=|\operatorname{im}B|\), the locality surcharge is

\[
\boxed{\Gamma_{\mathrm{loc}}=\sum_i\log_2|Q_i|-\log_2N_{\mathrm{joint}}\ge0.}
\]

For \(m\)-bit parity, the centralized behavior is one bit while every Branch must preserve its own bit, so

\[
\Gamma_{\mathrm{loc}}=m-1\text{ bits}.
\]

![Required distinctions can be carried by different architectures, but every cut must remain sufficient.](figures/carriers.png){width=88%}

## Communication as adaptive transfer

For \(B:X\times Y\to Z\), one-way deterministic communication from \(X\) to a receiver that knows \(y\) requires exactly the contextual quotient

\[
x\sim_Xx'\iff B(x,y)=B(x',y)\quad\forall y.
\]

Thus the minimum message alphabet is \(|X/\!\sim_X|\). Interactive communication can be cheaper because the receiver may first reveal which context is relevant. This does not recreate source distinctions that were already discarded before the query arrived.

At any network cut, collect every surviving carrier - local memories, shared state, transcript, and persistent interfaces - into a combined map \(C\). If no later exogenous observation introduces new distinguishing information, exact future behavior \(\mathcal B\) requires

\[
\boxed{\ker C\subseteq\ker\mathcal B.}
\]

This is fibre factorization applied to a distributed computation cut, not a physical information-conservation law.


# Adaptive Passports

A Passport can be static or adaptive. Static preparedness requires correctness for every declared context simultaneously. An adaptive Passport allows the receiver to reveal which part of the declared context envelope actually applies.

Let \(B:X\times Y\to Z\). For a set \(U\subseteq Y\) of still-possible receiver contexts define

\[
\boxed{xE_Ux'\iff B(x,y)=B(x',y)\quad\forall y\in U.}
\]

Then

\[
E_{U\cup V}=E_U\cap E_V,
\]

and if \(U'\subseteq U\),

\[
E_U\subseteq E_{U'}.
\]

So pure context revelation can only make the required source equivalence coarser. There is a canonical quotient map \(X/E_U\to X/E_{U'}\).

This yields a clean distinction between **revelation** and **contract amendment**. Revelation selects within the original task envelope. A later request not contained in that envelope is a new contract and requires revalidation.

## Preparedness versus response complexity

If the source must compress before learning which \(y\in Y\) will be requested, its retained state \(S(x)\) must satisfy

\[
\boxed{\ker S\subseteq E_Y.}
\]

In the INDEX problem, \(x\in\{0,1\}^n\) and the receiver asks for \(x_i\). Before \(i\) is known the source must retain all \(n\) bits, although after the query only one bit is relevant. Interactive communication can therefore reduce export bandwidth without reducing pre-query retention complexity.

A deterministic protocol can be viewed as adaptive rectangular refinement of \(X\times Y\). Every transcript restricts the remaining inputs to a rectangle \(A\times U\), and the protocol terminates when the declared behavior is homogeneous on that rectangle. In BM language, interaction performs runtime contextual specialization; T55 performs compiled contextual readiness.


# Temporal Quotients and Retention Cost

Finite-horizon contracts create a canonical nonstationary exact realization. Let \(\Phi:X\to X\) and \(T:X\to Y\). Define

\[
\beta_h(x)=\big(T(x),T(\Phi x),\ldots,T(\Phi^hx)\big)
\]

and

\[
\boxed{E_h=\bigcap_{j=0}^{h}\ker(T\circ\Phi^j).}
\]

Longer horizons require finer equivalences: \(E_{h+1}\subseteq E_h\). But as time passes and the remaining horizon shrinks, there is a canonical exact transition

\[
\boxed{F_h:X/E_h\to X/E_{h-1},\qquad [x]_{E_h}\mapsto[\Phi x]_{E_{h-1}}.}
\]

![The exact interface may shrink as a finite contract counts down.](figures/temporal_countdown.png){width=80%}

This countdown quotient is stagewise minimal. Any state that predicts the next \(h+1\) task values must refine \(E_h\).

For finite \(X\), let \(N_h=|X/E_h|\) and \(c_h=\log_2N_h\). The idealized integrated state-capacity burden of the exact countdown is

\[
\boxed{\mathcal R_H=\sum_{h=0}^{H}c_h.}
\]

With increments \(\Delta_0=c_0\) and \(\Delta_j=c_j-c_{j-1}\),

\[
\mathcal R_H=\sum_{j=0}^{H}(H-j+1)\Delta_j.
\]

A fixed \(H\)-horizon state carried for every stage instead costs \((H+1)c_H\), giving temporal retention surcharge

\[
\boxed{\Gamma_H^{\mathrm{time}}=(H+1)c_H-\sum_{h=0}^{H}c_h=\sum_{j=1}^{H}j\Delta_j.}
\]

This is a representation-capacity accounting identity, not thermodynamic entropy.

## Finite distinguishability depth

If a deterministic finite system has \(N\) states and the current task equivalence has \(p\) blocks, repeated future refinement stabilizes by depth

\[
\boxed{N-p.}
\]

Every strict refinement increases the block count, and there are at most \(N-p\) increases. This sharpens the cruder pair-state bound.


# Approximate Temporal Cascades

For the linear system

\[
x_{t+1}=Ax_t,\qquad y_t=Cx_t,
\]

define the horizon observability operator

\[
\mathcal O_h=\begin{bmatrix}C\\CA\\\vdots\\CA^h\end{bmatrix}
\]

and Gramian \(W_h=\mathcal O_h^*\mathcal O_h\). The independently optimal rank-\(d_h\) linear approximation has error

\[
\boxed{E_h^{\mathrm{free}}(d_h)=\sigma_{d_h+1}(\mathcal O_h).}
\]

But independently optimal stage subspaces need not chain into one lawful countdown dynamics. If \(U_h=\operatorname{row}(R_h)\), exact inter-stage descent requires

\[
\boxed{A^\top U_{h-1}\subseteq U_h.}
\]

For fixed representations, the least one-step compatibility defect is

\[
\boxed{\delta_h=\inf_{F_h}\|R_{h-1}A-F_hR_h\|=\|R_{h-1}A(I-P_h)\|,}
\]

where \(P_h\) projects onto \(U_h\).

Thus three different optimization problems exist, ordered by increasing architectural constraint:

- independent stagewise approximation;
- contract-indexed compatible countdown approximation;
- one fixed autonomous approximation.

The inequalities refer to feasible integrated dimension or a chosen resource cost. The first can be unrealizable dynamically; the last imposes the strongest architecture.

If the approximate transitions satisfy

\[
\|R_{h-1}Ax-F_hR_hx\|\le\delta_h
\]

and \(F_h\) is \(L_h\)-Lipschitz, then the reduced-state error obeys

\[
e_{t+1}\le L_{H-t}e_t+\delta_{H-t},
\]

hence

\[
\boxed{e_k\le\sum_{j=0}^{k-1}\delta_{H-j}\prod_{r=j+1}^{k-1}L_{H-r}.}
\]

Approximation error, dimension, compatibility defect, and amplification are therefore distinct coordinates of the temporal Pareto problem.


# Smooth and Nonlinear Contract-Indexed Descent

The contract-indexed condition has a coordinate-free nonlinear form. Let \(\Phi:M\to M\), \(R_h:M\to Q_h\), and \(R_{h-1}:M\to Q_{h-1}\). Define

\[
\boxed{\mathcal S_h(q)=\{R_{h-1}(\Phi x):R_h(x)=q\}.}
\]

A deterministic reduced transition \(F_h\) with

\[
R_{h-1}\Phi=F_hR_h
\]

exists exactly when every \(\mathcal S_h(q)\) is a singleton. The global compatibility diameter is

\[
\alpha_h=\sup_q\operatorname{diam}\mathcal S_h(q),
\]

and the best unrestricted reduced transition has Chebyshev-radius error

\[
\boxed{\delta_h^*=\sup_q\operatorname{rad}\mathcal S_h(q),\qquad \alpha_h/2\le\delta_h^*\le\alpha_h.}
\]

If \(R_h\) is a smooth submersion, exact descent implies the differential condition

\[
\boxed{d(R_{h-1}\Phi)(\ker dR_h)=0.}
\]

In cotangent form, if \(\mathcal H_h=\operatorname{im}dR_h^*\),

\[
\boxed{\Phi_x^*\mathcal H_{h-1}(\Phi x)\subseteq\mathcal H_h(x).}
\]

This is the nonlinear analogue of \(A^\top U_{h-1}\subseteq U_h\). With connected fibres, the differential condition is sufficient for smooth local-to-global descent because the target map is constant along each fibre. Without connected fibres it can fail: a covering map has zero vertical tangent space while distinct discrete fibre points may demand different outputs.

A quantitative local-to-global estimate also needs geometric conditioning. If

\[
\varepsilon_h=\sup_x\|d(R_{h-1}\Phi)_x|_{\ker dR_h(x)}\|
\]

and every connected fibre has intrinsic path diameter at most \(D_h\), then

\[
\boxed{\alpha_h\le\varepsilon_hD_h.}
\]

Small vertical derivative alone does not control global fibre variation when fibres can be arbitrarily long.


# Continuous and Smooth Realization

Abstract exactification does not settle whether a quotient exists in a requested regularity class. Version 1 therefore separates semantic exactness from realization.


Suppose X is compact Hausdorff, all tasks have Hausdorff targets and are continuous, every m∈M is continuous, and R is continuous with Hausdorff target. Then E# in section 3 is closed in X×X. The quotient Q=X/E# is compact Hausdorff, and the descended legacy map, tasks, and continuations are continuous.

**Proof.** Each kernel is the inverse image of a closed diagonal. Arbitrary intersections remain closed. For any closed A⊆X its saturation E#[A] is closed, being the projection of a compact closed subset of X×X. Distinct equivalence classes are disjoint compact sets, so choose disjoint open neighborhoods U,V containing them. The saturated open sets X∖E#[X∖U] and X∖E#[X∖V] still contain the respective classes and lie inside U,V. Their images separate the two quotient points, proving the quotient Hausdorff. The quotient is compact by continuity of q. A map out of Q is continuous exactly when its composite with q is continuous; apply this to every descended map. ∎

A continuous representation with **kernel exactly E#** into ℝᵏ exists iff Q embeds in ℝᵏ. Indeed the induced map from compact Q into the Hausdorff target is a continuous bijection onto its image and hence an embedding. Conversely an embedding composed with q gives that representation. A finer representation can exist even when this exact quotient does not embed in the requested dimension.

For finitely many compact Hausdorff carriers, closed initial equivalences B_i, and total continuous finite-arity operations, the contextual construction has the same positive conclusion. A one-hole context is any finite composition of the operations with one variable input and all other inputs fixed as native constants; include the identity context. Put

\[
E_i=\bigcap_{C:X_i\to X_j}(C\times C)^{-1}B_j.
\]

Each E_i is closed. Inserting an operation into any context and replacing its input slots one at a time proves output E-equivalence whenever its inputs are E-equivalent. Conversely any congruence refining B preserves all these contexts and is therefore contained in E. This proves coarsestness directly. Finite products of the quotient maps are quotient maps here, since they are continuous surjections from compact spaces onto Hausdorff spaces. This supplies the continuity of descended Interactions. Arbitrary partial domains and relational/stochastic continuity require their own additional assumptions.


## Local smooth augmentation


Let M be a smooth manifold and R:M→ℝᵖ a smooth legacy map. Let H# be the family of smooth scalar functions comprising the components of all declared future legacy values and tasks, including the present components of R. Write

\[
\mathscr W_\#(x)=\operatorname{span}\{dh_x:h\in H_\#\}.
\]

Suppose A:M→ℝᵏ is C¹, S=(R,A), and every required h has a **C¹ local factorization** h=\bar h∘S near the point x under discussion. Here \bar h is C¹ on an open neighborhood of S(x) in ℝᵖ⁺ᵏ, and the factorization holds on a neighborhood of x mapped into that domain. Then

\[
\boxed{k\ge\dim\mathscr W_\#(x)-\operatorname{rank}dR_x.}
\]

**Proof.** The chain rule gives dh_x in the row space of dS_x for every h. Thus dim W#(x)≤rank dS_x≤rank dR_x+k. ∎

If rank dR=r₀ and dim W#=r are constant in a neighborhood, this number r−r₀ is locally attainable with smooth A for the observable factorizations. Choose r₀ independent components of R at the point and extend their differentials to a basis of W# using r−r₀ functions from H#. They remain independent on a smaller neighborhood. Use the added functions as A. Constant-rank coordinates give connected local plaques on which every required h has zero vertical derivative, hence is constant. Each h consequently factors smoothly through the resulting rank-r local representation; its decoder extends to an ambient open neighborhood by ignoring the transverse coordinates in the constant-rank normal form. If the family is closed under the declared continuations, the same reasoning gives local descent of the represented continuations wherever the relevant local charts and domains apply. It does not establish one global chart or all-time global realization. The classical normal form used here is stated in [Loustau, *Smooth Manifolds*, Lecture 6](https://brice.loustau.eu/teaching/TUDarmstadt/Manifolds2020/Lecture6.pdf).

The decoder hypothesis matters. With identity dynamics, R(t)=t³ and task T(t)=t, exact set-level recovery uses the continuous decoder cube root, but at zero rank dR=0 while dT≠0. Thus one cannot infer this differential inequality from mere set-level factorization through an arbitrary singular smooth R.


## Global vertical-bundle restriction


Let ρ:Q→Z be a smooth submersion and V=ker dρ. Suppose a:Q→ℝᵏ is required to make (ρ,a) an immersion. Then da restricted to V is injective and defines a vector-bundle embedding

\[
V\hookrightarrow Q\times\mathbb R^k.
\]

Therefore k is at least the minimum trivial-bundle rank admitting such an embedding. This is a necessary bound, not a general attainment theorem. Mere smooth injectivity of (ρ,a) does not imply derivative injectivity, as t↦t³ shows.

The Möbius line bundle illustrates a separate global obstruction that already holds for continuous encoders. Present it as (θ,t)∼(θ+2π,−t), with ρ recording θ modulo 2π. If a scalar a is injective on each line fibre, the continuous nonzero difference a(θ,1)−a(θ,−1) must keep its sign along θ, yet the identification reverses that sign after 2π. Contradiction. Two components suffice:

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

the R₂ condition gives s(w)=s(Rot_z w) for every w∈ℝ² and real z. In particular s(w)=s(−w). In a smooth chart around s(0), differentiation at zero gives ds₀=−ds₀, hence ds₀=0. Independence of z gives dS=0 at every point of the z-axis.

A submersion with zero derivative must have zero-dimensional target. Since X is connected and S is surjective, that target would consist of one point, which cannot recover the nonconstant task T. Contradiction. ∎

The set-level task quotient exists. The smooth scalar map T itself also exists and suffices, but has a critical point on the axis and is excluded by the submersion contract. Thus the result does not say that arbitrary smooth encoders fail to exist. It says that imposing regular smooth realization can destroy the existence of a coarsest admissible interface even though several valid interfaces exist.

This supplies a concrete negative answer to the unrestricted existence aspiration in L open problem 6 for the submersion class. BM must allow a family of admissible realizations, a changed realization contract, or a proved nonexistence outcome.


The negative theorem is foundational. It prevents BM from treating “the coarsest regular realization” as a universally existing object. Set-level exactification may exist while the admissible smooth-submersion class has several incomparable valid realizations and no coarsest one.


# Closure Price: Exact Dynamic Closure Versus Free Approximation

The closure-price program asks a precise quantitative question: how much performance can be lost when a representation is required not only to approximate the receiver task but also to evolve autonomously in the declared realization class?

The canonical scalar example is

\[
\dot x=\varepsilon v,\qquad \dot v=0,\qquad y=x.
\]

For every nonzero \(\varepsilon\), any globally continuous scalar encoder satisfying exact fixed-step autonomous closure collapses the fixed line \(v=0\). On the Euclidean unit ball this forces worst-case trajectory error

\[
\boxed{E_1^{\mathrm{closed}}=\sqrt T.}
\]

The free continuous scalar trajectory approximation has error equal to the second singular value of the response operator. For small \(s=\varepsilon T\),

\[
E_1^{\mathrm{free}}\sim\frac{\sqrt T|s|}{\sqrt{12}},
\]

so

\[
\boxed{\frac{E_1^{\mathrm{closed}}}{E_1^{\mathrm{free}}}\sim\frac{\sqrt{12}}{|s|}.}
\]

At \(\varepsilon=0\), exact scalar closure has zero error. Thus an arbitrarily weak coupling can create an order-one exact-closure obstruction while the free approximation error tends to zero.

Closure price is always realization-class dependent. Discontinuous set-theoretic encodings can defeat Euclidean coordinate lower bounds; smoothness, continuity, linearity, locality, or physicality must therefore be part of the theorem statement.


# Jordan Chains and Orbit Width

The Jordan chain amplifies the scalar closure phenomenon into a hierarchy of continuation depths:

\[
\dot x_i=\varepsilon x_{i+1}\;(i<n),\qquad \dot x_n=0,\qquad y=x_1.
\]

The response operator is

\[
(O_{n,T}z)(t)=\sum_{k=0}^{n-1}\frac{(\varepsilon t)^k}{k!}z_{k+1}.
\]

For linear rank-\(d\) exact closed encoders, the source supplement classifies the admissible invariant rowspaces and gives the exact linear closed error. The stronger continuous nonlinear lower bound uses orbit width and Borsuk-Ulam.


Consider the n-state chain, with n≥2,

\[
\dot x_i=\varepsilon x_{i+1}\;(i<n),\quad
\dot x_n=0,\quad y=x_1,
\qquad \varepsilon\ne0.
\]

Let Φ=e^{εhN}, h>0, where N has ones on the superdiagonal, and let O=e₁ᵀ denote the current output. The performance set is the Euclidean unit ball. Require a globally continuous encoder R:ℝⁿ→ℝᵈ and a single-valued update F satisfying RΦ=FR on all of ℝⁿ. Decoder regularity is unrestricted.

### 4.1 General continuation-width lemma

For a finite S⊂{0,1,2,…} containing zero and a linear subspace V of dimension d+1, let

\[
\|x\|_S=\max_{k\in S}\|\Phi^k x\|_2,
\quad
\beta(V,S)=\inf_{x\in V\setminus\{0\}}
\frac{\max_{k\in S}|O\Phi^kx|}{\|x\|_S}.
\]

Every such code has worst-case current-output error at least β(V,S).

**Proof.** The unit sphere of this norm on V is antipodally homeomorphic to Sᵈ. The Borsuk–Ulam theorem supplies x and −x on it with R(x)=R(−x). Closure propagates this equality to Φᵏx and −Φᵏx for every k∈S. Both states lie in the performance ball. Their outputs are opposite, so a common decoded value has error at least |OΦᵏx| at one of them. Maximize over k, then use the infimum defining β. ∎

This uses the same classical topological input as C §4.1. Continuity of R and exact global iteration are essential. A finite performance ball is not being asserted to be invariant.

### 4.2 Explicit Jordan interpolation bound

Choose S_M={0,M,2M,…,(n−1)M}, where M is a positive integer, and put a=εMh. Let ℓ_j(s) be the Lagrange polynomials at the nodes 0,…,n−1. Define finite constants

\[
D_r=\max_{0\le i<n}\sum_{j=0}^{n-1}|\ell_j^{(r)}(i)|,
\qquad
b_M^2=\sum_{r=1}^{n-1}\frac{D_r^2}{|a|^{2r}}.
\]

Then, for every nonzero subspace V,

\[
\boxed{\beta(V,S_M)\ge(1+b_M^2)^{-1/2}\longrightarrow1.}
\]

**Proof.** Write P(s)=x_1(Mhs), a polynomial of degree at most n−1, and A=max_j|P(j)|. Interpolation gives

\[
|P^{(r)}(i)|\le D_rA.
\]

The chain identity is P^{(r)}(i)=a^r x_{r+1}(iMh). Thus every sampled state's tail has norm at most A b_M, and its first coordinate has magnitude at most A. Consequently

\[
\max_i\|\Phi^{iM}x\|_2\le A\sqrt{1+b_M^2}.
\]

For nonzero x, A>0 because n distinct zeros would make P identically zero and all state coordinates zero. Dividing proves the bound. ∎

For |a|≥1, one may replace b_M² by C_n/a² with C_n=Σ_rD_r². For n=3, the nodal constants are D_1=D_2=4. The proof deliberately treats the maximum-output node and maximum-state-norm node separately; they need not coincide.

### 4.3 Consequences and the remaining exact optimum

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

for sufficiently large M, when the numerator is nonnegative. A common decoder for z and −z incurs at least this error. Let M→∞.

When d=n−1, retaining (x₂,…,x_n) closes exactly and reconstructs every trajectory contribution except the constant x₁. Therefore

\[
\boxed{E_{p,T,n-1}^{\mathrm{closed,cont}}=\|1\|_p}
\]

for every nonzero ε. This includes √T for p=2 and 1 for p=∞. For 1≤d<n−1, this lower bound does **not** determine the complete finite-ε trajectory optimum. The exact linear answer from C remains an upper bound for the nonlinear class. Historical novelty of this obstruction has not been established.


## Orbit width as reconstruction conditioning

For a finite continuation set \(S\ni0\) and subspace \(V\), define

\[
\|x\|_S=\max_{k\in S}\|\Phi^kx\|,
\qquad
\beta(V,S)=\inf_{x\neq0}\frac{\max_{k\in S}\|O\Phi^kx\|}{\max_{k\in S}\|\Phi^kx\|}.
\]

When the sampled receiver map is injective on \(V\), orbit width is the reciprocal conditioning of reconstructing the native sampled orbit from receiver samples. This interpretation connects the topological lower bound to observability rather than leaving it as a purely topological curiosity.

The finite-dimensional generalized-Gramian estimate

\[
\beta(V,S)^2\ge\frac1{|S|}\min_{x\in V\setminus\{0\}}\frac{x^*W_Sx}{x^*B_Sx}
\]

yields computable lower certificates. The Gramian bound can be conservative; the exact orbit-width definition remains the controlling quantity in the theorem.


# Linear Compatibility and Repair

Exact linear whole-flow closure requires an invariant rowspace. Let \(O\) be the response operator and \(W=O^*O\). Free rank-constrained approximation selects leading response singular directions; exact autonomous closure additionally requires native invariance. These geometric objectives need not agree.

The conditioned repair theorem below quantifies when a receiver-optimal subspace can be repaired to a nearby invariant graph.


This section proves a precise finite-dimensional version of L §38. It concerns a linear representation with a linear autonomous update and an unrestricted trajectory decoder, as in C.

Let A be a real n×n matrix, O:ℝⁿ→H a linear map into a real Hilbert space, and W=O*O, with eigenvalues λ₁≥…≥λ_n≥0. Measure worst-case response error on ||x||₂≤1. Let U be a chosen leading d-dimensional spectral subspace, 0<d<n. In U⊕U⊥ write B=Aᵀ as

\[
B=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix}.
\]

For Z:U→U⊥ define the Sylvester operator L(Z)=B₂₂Z−ZB₁₁. Suppose it is invertible and, for some s>0,

\[
\|L^{-1}\|_{F\to F}\le1/s,\quad
\Delta=\|B_{21}\|_F,\quad b=\|B_{12}\|_2,
\quad 4b\Delta/s^2<1.
\]

Put r=2Δ/s, including r=0 when Δ=0. In that case U is already invariant and Z=0 supplies the theorem.

**Theorem.** There is a B-invariant graph subspace U_Z={(u,Zu):u∈U}, with ||Z||_F≤r. A rank-d encoder with rowspace U_Z supplies the following bounds on the optimum response approximation errors:

\[
\boxed{
E_{\mathrm{free}}^2=\lambda_{d+1}
\le E_{\mathrm{closed}}^2
\le\lambda_{d+1}
+(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
}
\]

E_closed denotes the optimum in the exact closed linear class; the constructed graph supplies its upper bound.

**Proof of invariant repair.** Graph invariance is equivalent to

\[
B_{21}+B_{22}Z=ZB_{11}+ZB_{12}Z,
\]

or Z=L^−1(−B₂₁+ZB₁₂Z). On the closed Frobenius ball ||Z||_F≤r this map has norm at most Δ/s+br²/s≤r. Its Lipschitz constant is at most 2br/s=4bΔ/s²<1, using

ZB₁₂Z−YB₁₂Y=(Z−Y)B₁₂Z+YB₁₂(Z−Y).

The contraction theorem supplies a unique fixed point in this ball. B-invariance of U_Z is equivalent to an exactly closing rank-d row representation for A. This works for a discrete linear update A, or for generator A and its whole flow.

**Proof of response bound.** In the chosen decomposition W is block diagonal. The orthogonal complement of U_Z consists of (−Zᵀv,v). Its W-Rayleigh quotient is at most

\[
\frac{\lambda_1\|Z^\top v\|^2+
\lambda_{d+1}\|v\|^2}{\|Z^\top v\|^2+\|v\|^2}
\le\lambda_{d+1}+
(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
\]

Encoding orthogonal coordinates in U_Z and decoding their O-contribution leaves exactly this complementary operator norm as the squared error. The free rank-d optimum is λ_{d+1}, so it is also a lower bound on the constrained optimum. ∎

Thus the **squared-error surcharge** is O(Δ²/s²). If E_free>0, the ordinary surcharge is at most the displayed squared surcharge divided by 2E_free. If E_free=0, the available ordinary-error estimate is O(Δ/s).

This is a conditioned invariant-subspace result using classical Sylvester, Riccati, and contraction methods. It does not prove a corresponding general nonlinear repair theorem, does not certify a minimum perturbation, and does not establish historical novelty. Linear observable-preserving reduction already has established methods, including [Ovchinnikov et al., *CLUE*](https://arxiv.org/abs/2004.11961).


## Sampled versus generator closure

A subspace can be invariant under one sampled map \(e^{hA}\) while failing to be invariant under \(A\). Rotation over one full period gives the simplest aliasing example. Under suitable nonaliasing information, or invariance at two incommensurate sample times in finite dimensions, one can recover whole-flow and hence generator invariance. BM therefore records the time model as part of the Passport rather than treating sampled and continuous closure as interchangeable.


# Nonlinear Resonance and Regularity Price

The family

\[
\dot x=ax+\varepsilon v^m,\qquad \dot v=bv
\]

shows that exact low-dimensional closure can exist with a loss of regularity at resonance.

When \(a\neq mb\),

\[
\boxed{q=x+\frac{\varepsilon}{a-mb}v^m,\qquad \dot q=aq.}
\]

At resonance \(a=mb\), with \(b\neq0\), the exact coordinate becomes logarithmic:

\[
\boxed{q=x-\frac{\varepsilon}{b}v^m\log|v|,\qquad \dot q=aq.}
\]

For integer \(m\ge1\), the function \(v^m\log|v|\) has only finite regularity at the origin. A smooth regularization trades exact closure for a controlled residual. The example demonstrates a regularity price: an exact abstract reduction can exist while every realization inside a smoother class must become approximate.

This distinction is central to BM. The existence question and the admissible-realization question are different theorems.


# Infinite-Dimensional Example: The Heat Cascade

The diagonal heat cascade is the Version 1 infinite-dimensional stress test. It also records a correction: a small per-mode generator residual does not imply a uniform \(\ell^2\) generator residual as the number of active modes grows.


Use positive modes indexed by n≥1 and the Hilbert state space ℓ²×ℓ²:

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

### 7.1 The rejected instantaneous estimate stays rejected

Where the generator is defined, the residual is

\[
r_n=\varepsilon v_n\frac{\delta^2}{v_n^2+\delta^2}.
\]

Per mode |r_n|≤|ε|δ/2. For N modes the resulting estimate is |ε|δ√N/2, not a bound uniform in N.

More strongly,

\[
\boxed{\sup_{\|v\|_2\le1}\|r(v)\|_2=|\varepsilon|\quad(\delta>0).}
\]

The upper bound follows from |r_n|≤|εv_n|. For the lower bound, put v_n=N^−1/2 on N coordinates and zero elsewhere. The residual norm is |ε|δ²/(N^−1+δ²), which tends to |ε| as N→∞. These are finite-support vectors, so they also lie in the generator domain. Uniformly small generator defect is impossible for this common-δ family on the unit ball.

### 7.2 Uniform evolved-coordinate estimate

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

Squaring, summing, and using Σ_{n≥1}n^−4=π⁴/90 proves the claim. The summable majorant also justifies the passage from finite truncations to ℓ². The coordinate formulas establish the identity for mild trajectories without assuming a derivative at t=0 for arbitrary ℓ² data. ∎

For fixed δ, Q_δ is a C∞ map ℓ²×ℓ²→ℓ². Set f_δ(s)=s log(s²+δ²). Since f_δ(0)=0 and f_δ′ is bounded on bounded scalar intervals, the coordinate map sends bounded ℓ² sets to ℓ². Its kth derivative for k≥1 is coordinatewise multiplication of f_δ^(k)(v_n) with the k perturbation coordinates. Bounded scalar derivatives and ||h||∞≤||h||₂ bound the resulting ℓ² norm by a constant times the product of the perturbations' ℓ² norms. Scalar Taylor remainders give the Fréchet derivative and its local continuity at each order. Multiplication by 1/n² is bounded. Constants may depend on δ and the bounded set.

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

The argument extends to positive decay rates λ_n when Σλ_n^−2<∞, replacing π²/√90 by (Σλ_n^−2)¹ᐟ². It is a result for this specified diagonal cascade, not all nonlinear PDEs.


The correct uniform statement is semigroup-level: smoothing creates a summable \(n^{-2}\) factor after evolution, giving an error bound independent of the number of modes. This is exactly the sort of distinction BM is intended to preserve: generator defect and evolved-coordinate defect are different contracts.


# Stochastic Branch Mathematics

Stochastic Branches keep probability law as native structure. Support or relation semantics cannot replace transition probabilities when the task depends on them.

For a finite Markov kernel \(K\) and quotient \(q\), strong lumpability requires

\[
\boxed{q(x)=q(x')\Longrightarrow q_\#K(x,\cdot)=q_\#K(x',\cdot).}
\]

Equivalently, aggregated transition probability into every quotient block must agree inside each quotient fibre. This is classical Kemeny-Snell lumpability in BM placement.

The same principle holds for joint Branches. Equal local marginals do not imply equal joint successor laws. Correlation can carry receiver-relevant distinctions that are invisible to each marginal. Thus local stochastic sufficiency is not automatically joint stochastic sufficiency.

For approximate one-step Markov closure, the quotient-fibre laws form a set in total variation distance. The unrestricted minimax reduced law is governed by its Chebyshev radius, with the usual half-diameter to diameter bounds. Under a Dobrushin contraction coefficient \(\alpha<1\), one-step error \(\epsilon\) propagates as

\[
\boxed{e_m\le\epsilon\frac{1-\alpha^m}{1-\alpha}.}
\]

Without contraction the elementary bound is \(e_m\le\min(1,m\epsilon)\).


## Finite stochastic refinement


For finite Markov actions, replace a relational successor signature by the vector

\[
\left(\sum_{y\in B}K(x,y)\right)_{B\in X_i/E_i}.
\]

Equal signatures are exactly equality of the aggregated laws. Intersect their kernels with the same tagged Interaction-context constraints and initial tasks. The termination and coarsestness proof carries over: equal finer-block sums remain equal after summing them over coarser blocks.

For explicitly listed finite carriers, rational transition tables, and complete finite Interaction tables, this gives a polynomial-time procedure in the explicit input size. Each strict round increases a class count; there are at most Σ_i(|X_i|−|X_i/B_i|) strict rounds. Each round computes finite block sums and signatures by scanning the supplied tables, then groups equal signatures. Rational comparison is exact with polynomial bit complexity for these sums.

This addresses the explicit-table sector of L's stochastic-refinement question. It is not a complexity result for succinctly represented exponentially large state spaces, restricted correlated contexts, or interactive strategies.


# Quantum Branch Mathematics

Quantum Branches require a sharper separation between algebraic recoverability and physical reduced dynamics. A linear observable can be representable through a channel while no completely positive trace-preserving reduced evolution exists.

For a compression channel \(\mathcal E\), exact linear recovery of an observable \(O\) means

\[
O\in\operatorname{Ran}\mathcal E^\dagger.
\]

The best unrestricted expectation-recovery error is

\[
\inf_B\|O-\mathcal E^\dagger(B)\|_\infty.
\]

Physical Dynamic Closure is stronger. Given native channel \(\Phi\), one requires a CPTP \(\bar\Phi\) with

\[
\boxed{\mathcal E\Phi=\bar\Phi\mathcal E.}
\]

The Edition 1.1 review completes the finite-dimensional feasibility test.


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
\operatorname{Tr}_{\mathrm{out}}J=I_m,\qquad
\sum_{a,b=1}^m[E(E_{ij})]_{ab}J_{ab}=(E\Phi)(E_{ij})
\quad(1\le i,j\le n).
}
\]

Here E_ij are the native n×n matrix units. Complex equations can be split into real and imaginary parts.

**Proof.** A reduced channel provides these blocks, and linearity gives the displayed equations. Conversely a feasible J defines Ψ(A)=Σ_ab A_ab J_ab. Choi positivity makes Ψ completely positive; the partial trace condition makes it trace preserving. The last constraints give ΨE=EΦ on a matrix-unit basis and therefore on every input. ∎

The channel characterization is classical. The displayed constraints are its direct application to the specified BM closure equation. [Watrous, *The Theory of Quantum Information*, §2.2.2, Corollary 2.27](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf).

This is a complete finite-dimensional feasibility criterion. A floating-point solver status alone is not an exact feasibility or infeasibility certificate. General abstract operator-system realizations, infinite-dimensional channels, and a closed-form classification for all families remain different questions.

### 8.1 Explicit range-invariance counterexample

For 0<λ<1, let E be qubit dephasing, acting on Bloch coordinates as

\[
(r_x,r_y,r_z)\mapsto(\lambda r_x,\lambda r_y,r_z).
\]

Let Φ be conjugation by the Hadamard unitary, so it sends (r_x,r_y,r_z) to (r_z,−r_y,r_x). E is invertible as a linear map, so Ran E† is the entire observable space and every range-invariance condition holds. The only possible linear reduced map is Ψ=EΦE^−1, which sends

\[
(r_x,r_y,r_z)\mapsto(\lambda r_z,-r_y,r_x/\lambda).
\]

Applied to the valid ambient qubit state (I+X)/2, its output is (I+λ^−1 Z)/2, with eigenvalues (1±λ^−1)/2. One is negative. Thus no physical reduced channel exists. At λ=1/2 these eigenvalues are −1/2 and 3/2. The test state lies outside E's reachable state ellipsoid when λ<1; that does not invalidate this argument, because the contract requires a CPTP map on the full reduced matrix algebra. Linear invertibility of E fixes that map on the whole algebra. A map defined only on the reachable ellipsoid is a different contract.

### 8.2 A useful sufficient condition

If E has a CPTP right inverse S, ES=id, then linear kernel stability

\[
\ker E\subseteq\ker(E\Phi)
\]

is also sufficient: set Ψ=EΦS. It is CPTP by composition. Since E(SE−I)=0, stability gives EΦ(SE−I)=0, hence ΨE=EΦ. This condition covers a specified split channel, not arbitrary compressions.

In finite dimensions the physical closure defect

\[
\delta_Q=\min_{\Psi\;\mathrm{CPTP}}\|E\Phi-\Psi E\|_\diamond
\]

is attained: the channel set is compact and the objective is continuous. Therefore δ_Q=0 exactly when the feasibility system holds. The norm convention here has no extra factor of 1/2.


The dephasing/Hadamard counterexample is a permanent firewall: full linear range invariance can hold while the uniquely forced reduced linear map sends a valid reduced density matrix to an operator with a negative eigenvalue. Physical realizability therefore cannot be inferred from vector-space invariance alone.


# GURF: The Response-Specialized Layer

GURF sits under Branch Mathematics as the response-oriented specialization. Its central question is not simply whether two native states are equal, but whether the distinctions between them matter for a declared family of responses, observations, continuations, interventions, or inverse tasks.

The completion-fibre viewpoint is particularly important. Given an observed label \(\ell\), the set of native states compatible with all observations is the completion fibre. Exact recovery means the receiver target is constant on that fibre; approximate recovery measures its diameter, radius, or native-sector analogue. The same logic reappears in path lifting, history state, inverse problems, and receiver acceptance.

The active GURF layers have the following Version 1 roles:

- **Core:** response sufficiency, completion fibres, exact/approximate recovery, obstruction and repair;
- **SOE:** evolution and observation under declared state/evolution contracts;
- **ACE:** admissibility and constraint handling;
- **IRE:** inverse recovery and reconstruction;
- **UKE:** memory kernels and internal-state realization;
- **HDE:** history-dependent exactification and hidden state;
- **GHSE:** hysteresis and mode-state requirements;
- **GRDE:** frozen at 008 pending any later separately justified development.

GURF does not replace native stochastic, quantum, geometric, or physical semantics. It audits which distinctions must survive for the response contract and whether a proposed compression, observation, or intervention has preserved them.


# Failure Atlas

A foundation is not complete until its invalid implications are recorded. The following are permanent Version 1 firewalls.

\[
\boxed{\text{static sufficiency}\not\Rightarrow\text{Dynamic Closure}}
\]

\[
\boxed{\text{local closure}\not\Rightarrow\text{coupled closure}}
\]

\[
\boxed{\text{pairwise/local compatibility}\not\Rightarrow\text{global realizability}}
\]

\[
\boxed{\text{set-level quotient}\not\Rightarrow\text{continuous or smooth realization}}
\]

\[
\boxed{\text{differential fibre test}\not\Rightarrow\text{global descent}}
\]

when disconnected aliases are present.

\[
\boxed{\text{marginal stochastic sufficiency}\not\Rightarrow\text{joint stochastic sufficiency}}
\]

\[
\boxed{\text{support equality}\not\Rightarrow\text{equality of stochastic law}}
\]

\[
\boxed{\text{local quantum sufficiency}\not\Rightarrow\text{joint continuation sufficiency}}
\]

\[
\boxed{\text{operator-space recoverability}\not\Rightarrow\text{CPTP physical recovery}}
\]

\[
\boxed{\text{sampled closure}\not\Rightarrow\text{generator closure}}
\]

without a nonaliasing condition.

\[
\boxed{\text{small local defect}\not\Rightarrow\text{small global realization defect}}
\]

without a conditioning hypothesis such as fibre diameter or spectral separation.

\[
\boxed{\text{excellent stagewise approximation}\not\Rightarrow\text{compatible reduced dynamics}}
\]

\[
\boxed{\text{context revelation}\not\Rightarrow\text{recovery of distinctions discarded before revelation}}
\]

\[
\boxed{\text{finite hidden-state memory}\not\Rightarrow\text{finite sliding-window memory}.}
\]

These failures are not weaknesses of BM. They are the boundaries that keep the metaframework from silently conflating different mathematical categories.


# Canonical Status Registry

Version 1 uses status as part of mathematical provenance. The original theorem identifiers remain stable; the table below records the broad verified families.


No new contradiction was found in the stated proofs of E's T01–T55, T55-C7/C7R, or LEV 013–016 within their written hypotheses. C's main continuous scalar theorem and its principal calculations also survive. This is an internal written-proof assessment, not a formal proof-assistant result.

| Source results | Review finding and decisive restriction |
| --- | --- |
| T01–T07 | Fibre factorization, task quotients, finite counting, refinement, and serial loss are correct. Decoders live on realized images; no regularity follows automatically. |
| T08–T12 | Partial operations need applicability saturation as well as value congruence. Static sufficiency does not imply dynamic closure. |
| T13–T15 | Essentiality uses a fixed candidate class. Raw Branch count is not invariant under unrestricted regrouping. |
| T16–T20 | Tree gluing and finite DAG evaluation work with their stated assumptions. Cycles and shared witnesses add requirements. |
| T21–T25 | Root acceptance remains receiver-relative. Pointwise path transitivity and cyclic/global realizability are separate claims. |
| T26–T28 | Finite failure localization and repair support are sound. T26's equality requires absorbing failure. T28's support equivalence requires the finite full product. |
| T29–T33 | Native Markov semantics and metric reconstruction/error estimates are sound. Diameter and radius need not coincide. |
| T34–T40 | The energy, gauge, graph, and semantic statements are scoped classical results; they do not prove the corresponding open physics programs. |
| T41–T48 | Approximate lumpability, join-tree gluing, receiver order/modulus, and Root transport survive with their stated norms, domains, and acceptance conditions. |
| T49–T55 | Relational cycles, categorical bookkeeping, mixed kernels, and relational closure are sound in the declared settings. |
| T55-C7/C7R | Simultaneous finite refinement is coarsest for independently substitutable Cartesian input contexts. It does not optimize arbitrary correlated encodings or hardware cost. |
| LEV 013 | The weighted rank-constrained reconstruction proof, including all minimizers, is valid for positive-definite weights. |
| LEV 014C | Zero projector price is equivalent to a maximizing spectral projector commuting with S. Noncommutation of S and K alone is insufficient. |
| LEV 014, 015, 016, 014S | Stationarity, scalar/matrix balancing, and the strengthened moment relaxation retain their exact scopes. General higher-rank global optimization is not solved. |
| C §§3–7 | Fixed-line collapse, the scalar optimum, free Hilbert width, linear chain classification, spectral asymptotics, damped coordinate, and unrestricted-state recovery formula survive. |
| E chapter 6 | The six native model equations are consistent with their declared idealizations. Their website implementations were not supplied or tested in this review. |

L contains more statements than complete derivations. Sections below re-prove selected central developments. Claims such as the unspecified heat/coupled-z tail problem, complete hidden-history minimization, or the full inverse-Hilbert recovery construction cannot be completely reconstructed from labels and summary formulas alone. They retain their previous status pending their full native contracts and proofs.


## Post-source integrated theorem families

The following families were developed after the 10-11 September source edition and are retained in the Version 1 research corpus with the indicated status.

| Family | Status | Boundary |
|---|---|---|
| Deterministic future exactification with retained legacy data | RP / BM-SYN | Total continuation monoid; partial maps need definedness handling. |
| Set-level simultaneous refinement | RP / CI-adjacent | Existence only; no general finite algorithm or regular realization. |
| Jordan continuous continuation obstruction | RP | Historical novelty unresolved; smaller-code finite-ε trajectory optimum open. |
| Successor-fibre radius/diameter theory | RP / BM-SYN | Exact for unrestricted deterministic predictors. |
| Path lifting and completion-state recursion | RP / CI-adjacent | Infinite lifting needs compact/closed hypotheses. |
| State-memory-locality formulas in finite systems | RP / CI-adjacent | Architecture must be specified. |
| Communication and adaptive Passport interpretation | CI + BM-SYN | Classical communication results; BM placement is architectural. |
| Temporal quotient countdown | RP / BM-SYN | Capacity measures are representational, not thermodynamic. |
| Approximate temporal compatibility | RP / BM-SYN | Exact formulas in linear setting; nonlinear general repair remains open. |
| Smooth contract-indexed descent | RP / CI-adjacent | Differential tests need connected fibres/global hypotheses. |
| Heat-cascade semigroup repair | RP | Positive-mode diagonal cascade only. |
| Finite-dimensional Choi closure criterion | RP / CI | Specified finite matrix channels. |


# Open Problems and Research Program

The foundation is frozen; the research program is not. Future work should primarily deepen the mathematics rather than add vocabulary.


“Completed” below refers only to the stated sector and theorem in this document.

| L open problem | Status after this review |
| --- | --- |
| 1. Nonlinear Jordan trajectory optimum | Current-output optimum and the d=n−1 trajectory endpoint are proved in section 4. Full finite-ε trajectory optimum for 1≤d<n−1 remains open. |
| 2. Jordan novelty audit | Not completed. A written proof is not a historical-priority determination. |
| 3. General approximate realization upper theorems | The heat cascade supplies a concrete semigroup-conditioned upper theorem. General selection, regularity, and optimality questions remain. |
| 4. Conditioned nonlinear repair | Still open in general. Section 9 completes the stated conditioned linear case with constants. |
| 5. Global smooth repair | Correct vertical-bundle necessity and Möbius example retained; section 6 supplies an additional existence obstruction. A general sharp global classification remains open. |
| 6. Coarsest native refinement | Positive for the compact Hausdorff setting in section 5. Negative in general for smooth-submersion realizations by section 6. Other target/dimension classes require separate answers. |
| 7. Continuous/smooth multi-Branch synthesis | Set-level existence and the compact total continuous sector are addressed. General smooth, partial, correlated, and infinite-dimensional synthesis is not settled. |
| 8. Stochastic refinement complexity | Explicit finite rational tables admit the polynomial refinement procedure in section 3. Succinct input and restricted-context complexity remain open. |
| 9. Physical quantum realization | Fully specified finite matrix channels have the exact feasibility criterion in section 8. General abstract/infinite-dimensional characterizations remain open. |
| 10. Infinite-dimensional closure price | One specified diagonal heat cascade is treated. General nonlinear PDE closure-price theory remains open. |
| 11. Uniform heat regularization | Completed in evolved-coordinate norm for positive modes. Uniformly vanishing common-δ generator defect is disproved on the ℓ² unit ball. |
| 12. State–memory–communication–time tradeoffs | The legacy memory contract is repaired and finite depth sharpened. The complete constrained Pareto theory remains open. |
| 13. External review and prior art | Selected classical sources checked. Comprehensive novelty review and independent peer validation are not completed. |

There is no defensible percentage-complete measure for this open-ended list. The next mathematically substantive targets remain the smaller-code Jordan trajectory optimum and a conditioned nonlinear realization theorem in a precisely fixed native class. Progress on either should produce a proof or counterexample with an actual performance consequence, rather than a new collection of labels.


Three priorities are especially important for a second volume. First, solve or sharply bound the nonlinear smaller-code Jordan trajectory optimum. Second, develop a conditioned nonlinear repair theorem with explicit global hypotheses and constants, or prove that no useful general theorem exists. Third, complete a broad prior-art comparison so that any historical novelty claim is separated from internal correctness.

Applications should be chosen because they stress the framework: coupled PDE reduction, physically admissible quantum compression, stochastic systems with correlation-sensitive tasks, distributed computation with locality constraints, and inverse problems in which the observation contract changes over time.


# Verification, Reproducibility, and Limits

Edition 1.1 records both proof review and reproducible finite checks. Those checks are evidence against implementation mistakes and small counterexamples; they are not substitutes for the written infinite or topological proofs.


The accompanying `bm_verification.py` ran successfully. It uses Python and NumPy and writes `verification_results.json`. During the verification amendment it was rerun, and its parsed result matched the original result exactly. All three source-file SHA-256 hashes also matched the saved source inventory.

| Check | Evidence |
| --- | --- |
| Deterministic exactification | All 4,096 combinations of a four-state deterministic update and a binary task; each computed terminal partition compared against all 15 partitions for exactness and coarsestness. |
| Partial multi-Branch refinement | All 81 partial binary Boolean-output Interaction tables, including unavailable outputs, under all 8 initial partition families: 648 models, each compared against all candidate interface families. Three specified local actions were included. |
| Jordan interpolation | Exact rational reconstruction of every monomial up to degree n−1 for n=2,…,6, with derivative constants and finite-direction checks of the width estimate. |
| Source approximation examples | Recomputed the shear errors and the weighted projector stationary candidates. Free weighted value ≈1.729299736; constrained value ≈4.764704744. |
| Heat repair | Checked the closed-form evolved mismatch against the modal and global bounds for 1, 16, 256, and 2,048 modes, two smoothing scales, and four times. Also evaluated the nonvanishing generator-residual sequence. |
| Quantum obstruction | Verified the forced linear map, its negative output-state and Choi eigenvalues, and the intertwining equations on matrix units. A separate diagonal-preserving evolution gives a positive closure example. |
| Conditioned linear repair | Checked the invariant graph and the squared-error bound for a concrete separated two-dimensional system. |
| Legacy memory | Verified the four-state counterexample and the required two-symbol auxiliary alphabet. |

The additional `bm_second_verification.py` uses Python, NumPy, and SciPy. Its exact finite checks use integer or rational arithmetic. Its quadrature and invariant-graph checks are floating-point consistency checks. It writes `second_verification_results.json`.

| Additional check | Evidence |
| --- | --- |
| Two-action deterministic exactification | 18,225 models on three states, covering every ordered pair of total actions and every pair of initial/required partitions. The all-word monoid construction agrees with iterative refinement and exhaustive comparison against all candidate equivalences; idempotence and contractiveness also hold. |
| Relational refinement | All 512 three-state successor relations under all five initial partitions: 2,560 models. Empty successor sets are included; each result is compared against every admissible equivalence. |
| Stochastic refinement | All 216 three-state kernels with entries in {0,1/2,1}, under all five initial partitions: 1,080 models. Aggregation and coarsestness are checked using exact integer sums. |
| Quantum certificates | Exact rational verification of the negative eigenvalues −1/2 and 3/2 in the dephasing obstruction. A separate two-qubit-to-one-qubit partial-trace compression has an explicit positive-semidefinite Choi factorization, the trace-preservation certificate, and all 16 native matrix-unit closure equations. |
| Heat mismatch | 96 modal comparisons of the direct evolved-coordinate formula against numerical integration of the residual, with maximum normalized disagreement below 2.7×10⁻¹⁵. This checks the modal identity by another method; the infinite-dimensional passage remains the written summability argument. |
| Matrix graph repair | Six cases with two-dimensional graph blocks in a four-dimensional system, including nonnormal blocks, Δ=0, and E_free=0. Invariance residuals were below 2.3×10⁻¹⁵, and the constructed errors obeyed the bounds. |
| Decoder scaling | Evaluated the section 10.2 counterexample at δ=1, 0.1, 0.01, and 0.001. Its formulas prove the failure for every δ>0 without uniform decoder control. |

The second script checks 21,865 additional finite models across the first three rows. These counts enumerate small cases; they are not counts of separately proved theorems. Both verification passes were performed by the same reviewer.

These finite checks do not prove Borsuk–Ulam, arbitrary-map impossibility, a smooth global theorem, or an infinite-dimensional estimate. Those rely on the written arguments. No numerical quantum SDP solver or proof assistant was used. The source calculator and website were not tested because their implementation files were not part of this source set.

Reproduce the checks from the archive directory:

```bash
python3 bm_verification.py --output verification_results.json
python3 bm_second_verification.py --output second_verification_results.json
```


## Final Version 1 verdict


The reviewed core of Branch Mathematics is established internally as a typed mathematical treatment of representation, interaction, continuation, realization, and receiver-relative reuse. Its abstract deterministic completion has a precise greatest-equivalence theorem. Finite relational and stochastic interfaces have explicit refinement procedures. Native realization has both positive theorems and genuine obstructions. Closure can carry a quantitative approximation price, and a small instantaneous defect can behave differently from a small evolved error.

This review strengthens that content with the proofs above and corrects the contracts needed to use it. It does not certify an unlimited subject as finished. It establishes no new physical law, no general Navier–Stokes regularity or Yang–Mills mass-gap solution, and no theorem of universal physical information conservation. Those conclusions do not follow from the representation mathematics.

The concrete value of BM here is that one native problem can demand different retained distinctions for current accuracy, future prediction, physical admissibility, locality, and stability. The useful output is a calculation, construction, or obstruction showing how those requirements interact. The next edition should retain that content and this explicit status boundary.


# Version History and Freeze Policy {.unnumbered}

**10 September 2026 - Mathematical Edition.** Established the canonical BM/GURF source definitions, T01-T55, the finite T55 synthesis family, LEV results, and scoped model equations.

**11 September 2026 - Exact Closure Price supplement.** Added the scalar shear closure obstruction, free-width comparison, Jordan-chain linear theory, logarithmic repair, and recovery calculations.

**12 September 2026 - Review and development 1.0.** Reorganized the core, proved several extensions, and identified remaining research problems.

**12 September 2026 - Review and development 1.1, verification amendment.** Superseded 1.0 by tightening the smooth augmentation and robust-width hypotheses, adding a second verification pass, and recording exact boundaries. This is the governing Version 1 review.

**Version 1 Foundation Freeze.** The foundation is treated as stable. New theorems should extend or apply it. Definitions and theorem dependencies should be revised only when a demonstrated mathematical contradiction or counterexample requires repair. Any such change should be versioned explicitly rather than silently rewriting the historical record.


# References {.unnumbered}

The book distinguishes BM-specific structure from classical mathematics. The following references are the principal classical anchors explicitly used in the Version 1 review.

1. A. Tarski, “A lattice-theoretical fixpoint theorem and its applications,” *Pacific Journal of Mathematics* 5 (1955).
2. Borsuk-Ulam theorem and classical antipodal-coincidence theory.
3. J. G. Kemeny and J. L. Snell, *Finite Markov Chains*, strong lumpability.
4. E. Michael, classical continuous-selection theorem for lower-semicontinuous convex-valued multifunctions on paracompact domains.
5. Myhill-Nerode theorem for minimal deterministic automata and residual languages.
6. Deterministic communication-complexity theory, including rectangle protocols and the INDEX problem.
7. Classical Hankel-rank / McMillan-degree realization theory for finite-dimensional linear memory systems.
8. J. Watrous, *The Theory of Quantum Information*, Choi characterization of completely positive trace-preserving maps.
9. Classical Sylvester/Riccati invariant-subspace perturbation theory.
10. Ovchinnikov et al., CLUE: exact linear observable-preserving reduction.
11. Constant-rank and submersion theorems in smooth manifold theory.

## Canonical internal sources {.unnumbered}

- *Branch Mathematics and GURF - Mathematical Edition*, 10 September 2026.
- *Branch Mathematics - The Price of Exact Dynamic Closure*, Research Supplement 1.0, 11 September 2026.
- *Branch Mathematics - Source review, corrected core, and scoped mathematical completion*, Edition 1.1 - verification amendment, 12 September 2026.
- *BM/GURF Full Chat Review Verification Log*, 12 September 2026, historical development record.


# Appendix A: Canonical Edition 1.1 Review Text {.unnumbered}

The following appendix preserves the governing 12 September 2026 review text inside the foundation volume so that the archival source of the freeze is not separated from the book. Its numbering is historical and independent of the chapter numbering above.


**Date:** 12 September 2026  
**Edition:** Review and development 1.1 — verification amendment  
**Scope:** The three supplied source identities, their stated theorem families, and the developments proved below.  
**Status:** Written proofs and reproducible checks; no claim of independent peer review or historical priority.

**Verification amendment:** A further proof review and targeted checks retained the principal results, while identifying two hypotheses that edition 1.0 did not state explicitly enough: differentiability of the augmentation in section 5.2, and uniformity in the error tolerance of the constants in section 10.2. Those statements are corrected below. Section 14 records the changes, evidence, and limits of this verification.

## 1. Outcome and source coverage {.unnumbered}

Branch Mathematics retains a coherent mathematical core. Its useful content is the coordinated calculation of the distinctions required by a contract, the conditions under which operations descend through a representation, and the existence and cost of representations satisfying the native requirements.

This review completes several specified arguments. It does **not** establish completion of every research problem listed in the source log. A general theorem asserting that a coarsest regular smooth realization always exists is false: section 6 gives a counterexample. That negative answer is part of completing the theory's scope.

The principal results of this review are:

1. A complete deterministic exactification statement, including retained legacy data, and a set-level extension of simultaneous refinement beyond finite carriers.
2. An explicit proof of the Jordan-chain continuation lower bound, including the exact trajectory optimum when one coordinate is omitted.
3. A counterexample to universal coarsest smooth-submersion reduction, together with the positive compact Hausdorff result and precise local smooth hypotheses.
4. A uniform-in-time, uniform-in-mode-count repair for the smooth heat-cascade representation. The generator-residual claim remains false; the evolved-coordinate error has a valid bound.
5. An exact finite-dimensional Choi-matrix criterion for physical quantum closure and an explicit example showing why linear range invariance is insufficient.
6. A conditioned linear repair theorem with constants, completing a precisely stated version of the log's Sylvester/Riccati candidate.
7. Corrections to the memory contract, the robust-width rate assumptions, and the finite distinguishability-depth estimate.

### 1.1 Documents actually read {.unnumbered}

The direct attachments were unavailable through the initial upload route. Matching saved copies were recovered with the same file identities. The review read the complete text of those copies, rather than treating earlier summaries as the documents.

| Source key | Exact document | Coverage |
| --- | --- | --- |
| E | `BM-GURF-Mathematical-Edition-2026-09-10(2).pdf` | All 38 PDF pages: foundations, GURF, T01–T55, T55 corollaries, LEV 013–016, model equations, and audit. Printed numbering ends at 37 because the cover is unnumbered. |
| C | `BM-Exact-Closure-Price-2026-09-11.pdf` | All 18 PDF pages: scalar shear obstruction, free widths, linear Jordan chains, asymptotics, logarithmic repair, optimal recovery, and limitations. |
| L | `BM_GURF_Full_Chat_Review_Verification_Log_2026-09-12.md` | Entire 40,297-byte log, including all development families, corrections, and thirteen open problems. |

Selected central PDF proof pages were also inspected visually. This was a mathematical review, not a page-by-page redesign of the source PDFs. Original theorem IDs are preserved. The accompanying archive records source hashes, the verification script, and its results.

Two passes were performed in this review: a structural/dependency pass and an adversarial/hypothesis pass. They are two passes by the same reviewer, not two independent reviewers. The earlier log's descriptions of prior verification are historical reports; they do not by themselves certify missing proofs.

### 1.2 Source theorem audit {.unnumbered}

No new contradiction was found in the stated proofs of E's T01–T55, T55-C7/C7R, or LEV 013–016 within their written hypotheses. C's main continuous scalar theorem and its principal calculations also survive. This is an internal written-proof assessment, not a formal proof-assistant result.

| Source results | Review finding and decisive restriction |
| --- | --- |
| T01–T07 | Fibre factorization, task quotients, finite counting, refinement, and serial loss are correct. Decoders live on realized images; no regularity follows automatically. |
| T08–T12 | Partial operations need applicability saturation as well as value congruence. Static sufficiency does not imply dynamic closure. |
| T13–T15 | Essentiality uses a fixed candidate class. Raw Branch count is not invariant under unrestricted regrouping. |
| T16–T20 | Tree gluing and finite DAG evaluation work with their stated assumptions. Cycles and shared witnesses add requirements. |
| T21–T25 | Root acceptance remains receiver-relative. Pointwise path transitivity and cyclic/global realizability are separate claims. |
| T26–T28 | Finite failure localization and repair support are sound. T26's equality requires absorbing failure. T28's support equivalence requires the finite full product. |
| T29–T33 | Native Markov semantics and metric reconstruction/error estimates are sound. Diameter and radius need not coincide. |
| T34–T40 | The energy, gauge, graph, and semantic statements are scoped classical results; they do not prove the corresponding open physics programs. |
| T41–T48 | Approximate lumpability, join-tree gluing, receiver order/modulus, and Root transport survive with their stated norms, domains, and acceptance conditions. |
| T49–T55 | Relational cycles, categorical bookkeeping, mixed kernels, and relational closure are sound in the declared settings. |
| T55-C7/C7R | Simultaneous finite refinement is coarsest for independently substitutable Cartesian input contexts. It does not optimize arbitrary correlated encodings or hardware cost. |
| LEV 013 | The weighted rank-constrained reconstruction proof, including all minimizers, is valid for positive-definite weights. |
| LEV 014C | Zero projector price is equivalent to a maximizing spectral projector commuting with S. Noncommutation of S and K alone is insufficient. |
| LEV 014, 015, 016, 014S | Stationarity, scalar/matrix balancing, and the strengthened moment relaxation retain their exact scopes. General higher-rank global optimization is not solved. |
| C §§3–7 | Fixed-line collapse, the scalar optimum, free Hilbert width, linear chain classification, spectral asymptotics, damped coordinate, and unrestricted-state recovery formula survive. |
| E chapter 6 | The six native model equations are consistent with their declared idealizations. Their website implementations were not supplied or tested in this review. |

L contains more statements than complete derivations. Sections below re-prove selected central developments. Claims such as the unspecified heat/coupled-z tail problem, complete hidden-history minimization, or the full inverse-Hilbert recovery construction cannot be completely reconstructed from labels and summary formulas alone. They retain their previous status pending their full native contracts and proofs.

## 2. The integrated BM core {.unnumbered}

Branch Mathematics is a mathematical metaframework for carrying one problem through distinct lawful mathematical Branches while preserving their native mathematics. It does not assume that the branches unify; compatibility and joint realization are results to establish.

| Role | Mathematical content |
| --- | --- |
| Branch | A typed carrier, sector, admissible objects, laws, operations, and contracts. |
| Interaction | A specified native operation with an actual domain and output type. |
| Leaf | A derived statement or calculation with hypotheses, proof/certificate, and provenance. |
| Configuration | A typed signature, obligations, and context; its interpretation family may be empty. |
| Tree | A realized Configuration with dependency/provenance, order/history, and active law assignments. |
| Response | A declared Tree-level output, possibly a law or set of outcomes. |
| Passport | An instantiated contract, including applicability and acceptance obligations. |
| Root | A typed export accepted by a specified receiver under its Passport. |

Rooting, Rebranching, and Seed remain candidate constructions except where a particular native construction has already been specified and proved. Their names supply no missing existence, convergence, or realization theorem. SSH remains retired.

BM governs the domain-independent representation and transformation mathematics. GURF governs response tasks, observations, continuation, interventions, inverse recovery, memory, and repair within that mathematics. Core, SOE, ACE, IRE, UKE, HDE, and GHSE retain their roles; GRDE remains frozen at 008.

The core does not require probability as a primitive or impose a universal scalar information measure. An imported stochastic or quantum model retains its own kernel, expectation, coupling, positivity, and physical-channel requirements. The deterministic proofs do not replace those requirements or establish an underlying deterministic interpretation of quantum experiments.

The dependency order is:

1. Specify the native objects, lawful operations, and receiver obligations.
2. Determine the contextual distinctions those obligations require.
3. Establish task factorization and operation/Interaction descent.
4. Construct a stable abstract interface, where the sector permits it.
5. Establish native realization and global witness consistency.
6. Optimize a declared cost and certify the resulting export.

The three closure operators remain separate: component dependency closure, obligation prerequisite closure, and equivalence refinement. None is inferred from another.

## 3. Exact deterministic completion {.unnumbered}

### 3.1 Contract and legacy exactification {.unnumbered}

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

Conversely, let H be an equivalence contained in ker R∩E_Q and stable under M. If x H y, then mx H my for every m; therefore R(mx)=R(my) and T(mx)=T(my). Thus H⊆E#. Apply this to H=ker S. Fibre factorization gives the unique induced quotient map. ∎

For an arbitrary input equivalence E, define

\[
\mathfrak E_Q(E)=\bigcap_{m\in M}(m\times m)^{-1}(E\cap E_Q).
\]

It is monotone and contractive. Applying it twice introduces composites mn and duplicates already-required task tests. Since M is a monoid and contains the identity, those tests are exactly the original tests, proving idempotence. This is an interior/refinement operator in the inclusion order on equivalences; calling it an extensive closure in that order would reverse the meaning.

For partial operations, use an explicit unavailable tag and preserve the actual composition domains. Arbitrary partial tasks cannot be treated as ordinary total maps without this change. For stochastic or game semantics, replace the deterministic statement by the corresponding native theorem.

### 3.2 Simultaneous refinement beyond finite sets {.unnumbered}

The source T55 construction also has a set-level existence extension. Keep a set-indexed family of carriers X_i, initial equivalences B_i, action relations, and finite-arity partial Interactions, with the same independently substitutable Cartesian contexts as E chapter 3.

On

\[
\mathcal L=\prod_i[\Delta_{X_i},B_i]
\]

define F by the source refinement formula: intersect the current equivalence with equal successor signatures and equal tagged contextual output classes. This is a monotone, contractive map of a complete lattice. Monotonicity follows because equality of successor classes under a finer equivalence implies equality after passing to coarser classes, and likewise for tagged Interaction outputs.

**Theorem.** A unique coarsest exact equivalence family exists in this set-level class. It is the greatest fixed point of F below B.

**Proof.** Start at B, iterate F at successor ordinals, and intersect all earlier equivalences at limit ordinals. Every strict step removes a pair from a set of available pairs, so this descending construction must stabilize at some ordinal. Its fixed point satisfies the source descent obligations. Every other admissible family H remains contained in each stage: the successor step is the source monotonicity argument, and the limit step is intersection. Thus the terminal family contains every admissible H and is uniquely coarsest. ∎

This is an application of classical complete-lattice fixed-point reasoning, not a new fixed-point theorem. [Tarski, *A lattice-theoretical fixpoint theorem and its applications*, Theorem 1](https://msp.org/pjm/1955/5-2/pjm-v5-n2-p11-p.pdf).

The result gives neither finite termination nor a computable procedure on arbitrary infinite presentations. In particular, it does not assert that countably many rounds suffice for arbitrary infinitely branching relations, or that the resulting equivalence has a continuous or smooth realization.

### 3.3 Finite stochastic extension and explicit-table complexity {.unnumbered}

For finite Markov actions, replace a relational successor signature by the vector

\[
\left(\sum_{y\in B}K(x,y)\right)_{B\in X_i/E_i}.
\]

Equal signatures are exactly equality of the aggregated laws. Intersect their kernels with the same tagged Interaction-context constraints and initial tasks. The termination and coarsestness proof carries over: equal finer-block sums remain equal after summing them over coarser blocks.

For explicitly listed finite carriers, rational transition tables, and complete finite Interaction tables, this gives a polynomial-time procedure in the explicit input size. Each strict round increases a class count; there are at most Σ_i(|X_i|−|X_i/B_i|) strict rounds. Each round computes finite block sums and signatures by scanning the supplied tables, then groups equal signatures. Rational comparison is exact with polynomial bit complexity for these sums.

This addresses the explicit-table sector of L's stochastic-refinement question. It is not a complexity result for succinctly represented exponentially large state spaces, restricted correlated contexts, or interactive strategies.

## 4. Jordan continuation obstruction: complete lower-bound proof {.unnumbered}

Consider the n-state chain, with n≥2,

\[
\dot x_i=\varepsilon x_{i+1}\;(i<n),\quad
\dot x_n=0,\quad y=x_1,
\qquad \varepsilon\ne0.
\]

Let Φ=e^{εhN}, h>0, where N has ones on the superdiagonal, and let O=e₁ᵀ denote the current output. The performance set is the Euclidean unit ball. Require a globally continuous encoder R:ℝⁿ→ℝᵈ and a single-valued update F satisfying RΦ=FR on all of ℝⁿ. Decoder regularity is unrestricted.

### 4.1 General continuation-width lemma {.unnumbered}

For a finite S⊂{0,1,2,…} containing zero and a linear subspace V of dimension d+1, let

\[
\|x\|_S=\max_{k\in S}\|\Phi^k x\|_2,
\quad
\beta(V,S)=\inf_{x\in V\setminus\{0\}}
\frac{\max_{k\in S}|O\Phi^kx|}{\|x\|_S}.
\]

Every such code has worst-case current-output error at least β(V,S).

**Proof.** The unit sphere of this norm on V is antipodally homeomorphic to Sᵈ. The Borsuk–Ulam theorem supplies x and −x on it with R(x)=R(−x). Closure propagates this equality to Φᵏx and −Φᵏx for every k∈S. Both states lie in the performance ball. Their outputs are opposite, so a common decoded value has error at least |OΦᵏx| at one of them. Maximize over k, then use the infimum defining β. ∎

This uses the same classical topological input as C §4.1. Continuity of R and exact global iteration are essential. A finite performance ball is not being asserted to be invariant.

### 4.2 Explicit Jordan interpolation bound {.unnumbered}

Choose S_M={0,M,2M,…,(n−1)M}, where M is a positive integer, and put a=εMh. Let ℓ_j(s) be the Lagrange polynomials at the nodes 0,…,n−1. Define finite constants

\[
D_r=\max_{0\le i<n}\sum_{j=0}^{n-1}|\ell_j^{(r)}(i)|,
\qquad
b_M^2=\sum_{r=1}^{n-1}\frac{D_r^2}{|a|^{2r}}.
\]

Then, for every nonzero subspace V,

\[
\boxed{\beta(V,S_M)\ge(1+b_M^2)^{-1/2}\longrightarrow1.}
\]

**Proof.** Write P(s)=x_1(Mhs), a polynomial of degree at most n−1, and A=max_j|P(j)|. Interpolation gives

\[
|P^{(r)}(i)|\le D_rA.
\]

The chain identity is P^{(r)}(i)=a^r x_{r+1}(iMh). Thus every sampled state's tail has norm at most A b_M, and its first coordinate has magnitude at most A. Consequently

\[
\max_i\|\Phi^{iM}x\|_2\le A\sqrt{1+b_M^2}.
\]

For nonzero x, A>0 because n distinct zeros would make P identically zero and all state coordinates zero. Dividing proves the bound. ∎

For |a|≥1, one may replace b_M² by C_n/a² with C_n=Σ_rD_r². For n=3, the nodal constants are D_1=D_2=4. The proof deliberately treats the maximum-output node and maximum-state-norm node separately; they need not coincide.

### 4.3 Consequences and the remaining exact optimum {.unnumbered}

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

for sufficiently large M, when the numerator is nonnegative. A common decoder for z and −z incurs at least this error. Let M→∞.

When d=n−1, retaining (x₂,…,x_n) closes exactly and reconstructs every trajectory contribution except the constant x₁. Therefore

\[
\boxed{E_{p,T,n-1}^{\mathrm{closed,cont}}=\|1\|_p}
\]

for every nonzero ε. This includes √T for p=2 and 1 for p=∞. For 1≤d<n−1, this lower bound does **not** determine the complete finite-ε trajectory optimum. The exact linear answer from C remains an upper bound for the nonlinear class. Historical novelty of this obstruction has not been established.

## 5. Continuous and local smooth realization {.unnumbered}

### 5.1 Positive continuous result {.unnumbered}

Suppose X is compact Hausdorff, all tasks have Hausdorff targets and are continuous, every m∈M is continuous, and R is continuous with Hausdorff target. Then E# in section 3 is closed in X×X. The quotient Q=X/E# is compact Hausdorff, and the descended legacy map, tasks, and continuations are continuous.

**Proof.** Each kernel is the inverse image of a closed diagonal. Arbitrary intersections remain closed. For any closed A⊆X its saturation E#[A] is closed, being the projection of a compact closed subset of X×X. Distinct equivalence classes are disjoint compact sets, so choose disjoint open neighborhoods U,V containing them. The saturated open sets X∖E#[X∖U] and X∖E#[X∖V] still contain the respective classes and lie inside U,V. Their images separate the two quotient points, proving the quotient Hausdorff. The quotient is compact by continuity of q. A map out of Q is continuous exactly when its composite with q is continuous; apply this to every descended map. ∎

A continuous representation with **kernel exactly E#** into ℝᵏ exists iff Q embeds in ℝᵏ. Indeed the induced map from compact Q into the Hausdorff target is a continuous bijection onto its image and hence an embedding. Conversely an embedding composed with q gives that representation. A finer representation can exist even when this exact quotient does not embed in the requested dimension.

For finitely many compact Hausdorff carriers, closed initial equivalences B_i, and total continuous finite-arity operations, the contextual construction has the same positive conclusion. A one-hole context is any finite composition of the operations with one variable input and all other inputs fixed as native constants; include the identity context. Put

\[
E_i=\bigcap_{C:X_i\to X_j}(C\times C)^{-1}B_j.
\]

Each E_i is closed. Inserting an operation into any context and replacing its input slots one at a time proves output E-equivalence whenever its inputs are E-equivalent. Conversely any congruence refining B preserves all these contexts and is therefore contained in E. This proves coarsestness directly. Finite products of the quotient maps are quotient maps here, since they are continuous surjections from compact spaces onto Hausdorff spaces. This supplies the continuity of descended Interactions. Arbitrary partial domains and relational/stochastic continuity require their own additional assumptions.

### 5.2 Correct local smooth augmentation theorem {.unnumbered}

Let M be a smooth manifold and R:M→ℝᵖ a smooth legacy map. Let H# be the family of smooth scalar functions comprising the components of all declared future legacy values and tasks, including the present components of R. Write

\[
\mathscr W_\#(x)=\operatorname{span}\{dh_x:h\in H_\#\}.
\]

Suppose A:M→ℝᵏ is C¹, S=(R,A), and every required h has a **C¹ local factorization** h=\bar h∘S near the point x under discussion. Here \bar h is C¹ on an open neighborhood of S(x) in ℝᵖ⁺ᵏ, and the factorization holds on a neighborhood of x mapped into that domain. Then

\[
\boxed{k\ge\dim\mathscr W_\#(x)-\operatorname{rank}dR_x.}
\]

**Proof.** The chain rule gives dh_x in the row space of dS_x for every h. Thus dim W#(x)≤rank dS_x≤rank dR_x+k. ∎

If rank dR=r₀ and dim W#=r are constant in a neighborhood, this number r−r₀ is locally attainable with smooth A for the observable factorizations. Choose r₀ independent components of R at the point and extend their differentials to a basis of W# using r−r₀ functions from H#. They remain independent on a smaller neighborhood. Use the added functions as A. Constant-rank coordinates give connected local plaques on which every required h has zero vertical derivative, hence is constant. Each h consequently factors smoothly through the resulting rank-r local representation; its decoder extends to an ambient open neighborhood by ignoring the transverse coordinates in the constant-rank normal form. If the family is closed under the declared continuations, the same reasoning gives local descent of the represented continuations wherever the relevant local charts and domains apply. It does not establish one global chart or all-time global realization. The classical normal form used here is stated in [Loustau, *Smooth Manifolds*, Lecture 6](https://brice.loustau.eu/teaching/TUDarmstadt/Manifolds2020/Lecture6.pdf).

The decoder hypothesis matters. With identity dynamics, R(t)=t³ and task T(t)=t, exact set-level recovery uses the continuous decoder cube root, but at zero rank dR=0 while dT≠0. Thus one cannot infer this differential inequality from mere set-level factorization through an arbitrary singular smooth R.

### 5.3 Global vertical-bundle restriction {.unnumbered}

Let ρ:Q→Z be a smooth submersion and V=ker dρ. Suppose a:Q→ℝᵏ is required to make (ρ,a) an immersion. Then da restricted to V is injective and defines a vector-bundle embedding

\[
V\hookrightarrow Q\times\mathbb R^k.
\]

Therefore k is at least the minimum trivial-bundle rank admitting such an embedding. This is a necessary bound, not a general attainment theorem. Mere smooth injectivity of (ρ,a) does not imply derivative injectivity, as t↦t³ shows.

The Möbius line bundle illustrates a separate global obstruction that already holds for continuous encoders. Present it as (θ,t)∼(θ+2π,−t), with ρ recording θ modulo 2π. If a scalar a is injective on each line fibre, the continuous nonzero difference a(θ,1)−a(θ,−1) must keep its sign along θ, yet the identification reverses that sign after 2π. Contradiction. Two components suffice:

\[
a(\theta,t)=\big(t\cos(\theta/2),t\sin(\theta/2)\big).
\]

This formula respects the identification and is injective with injective derivative along every fibre. Local dimension and global augmentation cost are different quantities.

## 6. A coarsest smooth submersion need not exist {.unnumbered}

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

the R₂ condition gives s(w)=s(Rot_z w) for every w∈ℝ² and real z. In particular s(w)=s(−w). In a smooth chart around s(0), differentiation at zero gives ds₀=−ds₀, hence ds₀=0. Independence of z gives dS=0 at every point of the z-axis.

A submersion with zero derivative must have zero-dimensional target. Since X is connected and S is surjective, that target would consist of one point, which cannot recover the nonconstant task T. Contradiction. ∎

The set-level task quotient exists. The smooth scalar map T itself also exists and suffices, but has a critical point on the axis and is excluded by the submersion contract. Thus the result does not say that arbitrary smooth encoders fail to exist. It says that imposing regular smooth realization can destroy the existence of a coarsest admissible interface even though several valid interfaces exist.

This supplies a concrete negative answer to the unrestricted existence aspiration in L open problem 6 for the submersion class. BM must allow a family of admissible realizations, a changed realization contract, or a proved nonexistence outcome.

## 7. Heat cascade: repair in the correct norm {.unnumbered}

Use positive modes indexed by n≥1 and the Hilbert state space ℓ²×ℓ²:

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

### 7.1 The rejected instantaneous estimate stays rejected {.unnumbered}

Where the generator is defined, the residual is

\[
r_n=\varepsilon v_n\frac{\delta^2}{v_n^2+\delta^2}.
\]

Per mode |r_n|≤|ε|δ/2. For N modes the resulting estimate is |ε|δ√N/2, not a bound uniform in N.

More strongly,

\[
\boxed{\sup_{\|v\|_2\le1}\|r(v)\|_2=|\varepsilon|\quad(\delta>0).}
\]

The upper bound follows from |r_n|≤|εv_n|. For the lower bound, put v_n=N^−1/2 on N coordinates and zero elsewhere. The residual norm is |ε|δ²/(N^−1+δ²), which tends to |ε| as N→∞. These are finite-support vectors, so they also lie in the generator domain. Uniformly small generator defect is impossible for this common-δ family on the unit ball.

### 7.2 Uniform evolved-coordinate estimate {.unnumbered}

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

Squaring, summing, and using Σ_{n≥1}n^−4=π⁴/90 proves the claim. The summable majorant also justifies the passage from finite truncations to ℓ². The coordinate formulas establish the identity for mild trajectories without assuming a derivative at t=0 for arbitrary ℓ² data. ∎

For fixed δ, Q_δ is a C∞ map ℓ²×ℓ²→ℓ². Set f_δ(s)=s log(s²+δ²). Since f_δ(0)=0 and f_δ′ is bounded on bounded scalar intervals, the coordinate map sends bounded ℓ² sets to ℓ². Its kth derivative for k≥1 is coordinatewise multiplication of f_δ^(k)(v_n) with the k perturbation coordinates. Bounded scalar derivatives and ||h||∞≤||h||₂ bound the resulting ℓ² norm by a constant times the product of the perturbations' ℓ² norms. Scalar Taylor remainders give the Fréchet derivative and its local continuity at each order. Multiplication by 1/n² is bounded. Constants may depend on δ and the bounded set.

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

The argument extends to positive decay rates λ_n when Σλ_n^−2<∞, replacing π²/√90 by (Σλ_n^−2)¹ᐟ². It is a result for this specified diagonal cascade, not all nonlinear PDEs.

## 8. Physical quantum closure: an exact finite criterion {.unnumbered}

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
\operatorname{Tr}_{\mathrm{out}}J=I_m,\qquad
\sum_{a,b=1}^m[E(E_{ij})]_{ab}J_{ab}=(E\Phi)(E_{ij})
\quad(1\le i,j\le n).
}
\]

Here E_ij are the native n×n matrix units. Complex equations can be split into real and imaginary parts.

**Proof.** A reduced channel provides these blocks, and linearity gives the displayed equations. Conversely a feasible J defines Ψ(A)=Σ_ab A_ab J_ab. Choi positivity makes Ψ completely positive; the partial trace condition makes it trace preserving. The last constraints give ΨE=EΦ on a matrix-unit basis and therefore on every input. ∎

The channel characterization is classical. The displayed constraints are its direct application to the specified BM closure equation. [Watrous, *The Theory of Quantum Information*, §2.2.2, Corollary 2.27](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf).

This is a complete finite-dimensional feasibility criterion. A floating-point solver status alone is not an exact feasibility or infeasibility certificate. General abstract operator-system realizations, infinite-dimensional channels, and a closed-form classification for all families remain different questions.

### 8.1 Explicit range-invariance counterexample {.unnumbered}

For 0<λ<1, let E be qubit dephasing, acting on Bloch coordinates as

\[
(r_x,r_y,r_z)\mapsto(\lambda r_x,\lambda r_y,r_z).
\]

Let Φ be conjugation by the Hadamard unitary, so it sends (r_x,r_y,r_z) to (r_z,−r_y,r_x). E is invertible as a linear map, so Ran E† is the entire observable space and every range-invariance condition holds. The only possible linear reduced map is Ψ=EΦE^−1, which sends

\[
(r_x,r_y,r_z)\mapsto(\lambda r_z,-r_y,r_x/\lambda).
\]

Applied to the valid ambient qubit state (I+X)/2, its output is (I+λ^−1 Z)/2, with eigenvalues (1±λ^−1)/2. One is negative. Thus no physical reduced channel exists. At λ=1/2 these eigenvalues are −1/2 and 3/2. The test state lies outside E's reachable state ellipsoid when λ<1; that does not invalidate this argument, because the contract requires a CPTP map on the full reduced matrix algebra. Linear invertibility of E fixes that map on the whole algebra. A map defined only on the reachable ellipsoid is a different contract.

### 8.2 A useful sufficient condition {.unnumbered}

If E has a CPTP right inverse S, ES=id, then linear kernel stability

\[
\ker E\subseteq\ker(E\Phi)
\]

is also sufficient: set Ψ=EΦS. It is CPTP by composition. Since E(SE−I)=0, stability gives EΦ(SE−I)=0, hence ΨE=EΦ. This condition covers a specified split channel, not arbitrary compressions.

In finite dimensions the physical closure defect

\[
\delta_Q=\min_{\Psi\;\mathrm{CPTP}}\|E\Phi-\Psi E\|_\diamond
\]

is attained: the channel set is compact and the objective is continuous. Therefore δ_Q=0 exactly when the feasibility system holds. The norm convention here has no extra factor of 1/2.

## 9. Conditioned linear repair with explicit constants {.unnumbered}

This section proves a precise finite-dimensional version of L §38. It concerns a linear representation with a linear autonomous update and an unrestricted trajectory decoder, as in C.

Let A be a real n×n matrix, O:ℝⁿ→H a linear map into a real Hilbert space, and W=O*O, with eigenvalues λ₁≥…≥λ_n≥0. Measure worst-case response error on ||x||₂≤1. Let U be a chosen leading d-dimensional spectral subspace, 0<d<n. In U⊕U⊥ write B=Aᵀ as

\[
B=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix}.
\]

For Z:U→U⊥ define the Sylvester operator L(Z)=B₂₂Z−ZB₁₁. Suppose it is invertible and, for some s>0,

\[
\|L^{-1}\|_{F\to F}\le1/s,\quad
\Delta=\|B_{21}\|_F,\quad b=\|B_{12}\|_2,
\quad 4b\Delta/s^2<1.
\]

Put r=2Δ/s, including r=0 when Δ=0. In that case U is already invariant and Z=0 supplies the theorem.

**Theorem.** There is a B-invariant graph subspace U_Z={(u,Zu):u∈U}, with ||Z||_F≤r. A rank-d encoder with rowspace U_Z supplies the following bounds on the optimum response approximation errors:

\[
\boxed{
E_{\mathrm{free}}^2=\lambda_{d+1}
\le E_{\mathrm{closed}}^2
\le\lambda_{d+1}
+(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
}
\]

E_closed denotes the optimum in the exact closed linear class; the constructed graph supplies its upper bound.

**Proof of invariant repair.** Graph invariance is equivalent to

\[
B_{21}+B_{22}Z=ZB_{11}+ZB_{12}Z,
\]

or Z=L^−1(−B₂₁+ZB₁₂Z). On the closed Frobenius ball ||Z||_F≤r this map has norm at most Δ/s+br²/s≤r. Its Lipschitz constant is at most 2br/s=4bΔ/s²<1, using

ZB₁₂Z−YB₁₂Y=(Z−Y)B₁₂Z+YB₁₂(Z−Y).

The contraction theorem supplies a unique fixed point in this ball. B-invariance of U_Z is equivalent to an exactly closing rank-d row representation for A. This works for a discrete linear update A, or for generator A and its whole flow.

**Proof of response bound.** In the chosen decomposition W is block diagonal. The orthogonal complement of U_Z consists of (−Zᵀv,v). Its W-Rayleigh quotient is at most

\[
\frac{\lambda_1\|Z^\top v\|^2+
\lambda_{d+1}\|v\|^2}{\|Z^\top v\|^2+\|v\|^2}
\le\lambda_{d+1}+
(\lambda_1-\lambda_{d+1})\frac{r^2}{1+r^2}.
\]

Encoding orthogonal coordinates in U_Z and decoding their O-contribution leaves exactly this complementary operator norm as the squared error. The free rank-d optimum is λ_{d+1}, so it is also a lower bound on the constrained optimum. ∎

Thus the **squared-error surcharge** is O(Δ²/s²). If E_free>0, the ordinary surcharge is at most the displayed squared surcharge divided by 2E_free. If E_free=0, the available ordinary-error estimate is O(Δ/s).

This is a conditioned invariant-subspace result using classical Sylvester, Riccati, and contraction methods. It does not prove a corresponding general nonlinear repair theorem, does not certify a minimum perturbation, and does not establish historical novelty. Linear observable-preserving reduction already has established methods, including [Ovchinnikov et al., *CLUE*](https://arxiv.org/abs/2004.11961).

## 10. Additional contract corrections {.unnumbered}

### 10.1 Memory retaining a legacy state {.unnumbered}

For nonempty finite X, let E# be the **legacy-and-task future equivalence** of section 3. For q∈R(X), let n_R(q) count the E# classes in R^−1(q). If A may be initialized from the full native state and S=(R,A) must be autonomous and task-sufficient, then

\[
\boxed{|\mathcal A|_{\min}=\max_q n_R(q).}
\]

Necessity follows because no two distinct required classes in one R-fibre may share an auxiliary symbol. For sufficiency, label the E# classes within each R-fibre, reusing labels across different visible q. Then ker(R,A)=E#, so the exact update and tasks descend.

The future of R cannot be omitted if R itself is retained in the autonomous state. For example, X={0,1}², Φ(a,b)=(b,b), R(a,b)=a, and a constant external task have one task-behavior class. Nevertheless R is not closed, and the repaired autonomous state needs two auxiliary symbols to retain b. Thus the formula in L §17 is safe only when its phrase “complete future behavior” includes future legacy values under this architecture.

If initialization uses only R(x) and no new observations arrive, it cannot introduce distinctions lost by R. Observation-driven history memory is a different architecture and must specify its update alphabet and available observations.

### 10.2 Robust-width rates depend on update amplification {.unnumbered}

Let the encoder be continuous as in section 4, and let η be its worst-case current-output decoding error on the performance set. For initially merged native states, a one-step code residual ||RΦz−F(Rz)|| at most δ and an L_F-Lipschitz reduced update yield a uniform bound on their code separation after k steps:

\[
\alpha_k\le2\delta G_k(L_F),\qquad
G_k(L_F)=\sum_{j=0}^{k-1}L_F^j.
\]

Write Σ_{V,S}={x∈V:||x||_S=1}, with the orbit norm from section 4. Here α_k is the supremum of ||RΦᵏx−RΦᵏ(−x)|| over initially merged antipodal pairs on that sphere, so α₀=0. The displayed estimate requires the residual bound on every intermediate state used in the comparison, not just at the sampled endpoints. If the decoder has modulus ω_D on the codes used, the continuation-width proof gives

\[
\eta\ge\inf_{x\in\Sigma_{V,S}}
\max_{k\in S}\left(
|O\Phi^kx|-\tfrac12\omega_D(\alpha_k)
\right).
\]

Consider a family indexed by δ→0. Suppose sampling sets S_M have max S_M≤cM and a uniformly available orbit-width bound β(V,S_M)≥1−C/M². Suppose also ω_D(t)≤L_Dt^γ, with a fixed 0<γ≤1. The constants c, C, and L_D, the domains needed for the comparison, and the availability of these estimates must be uniform in both M and δ. With nonexpansive reduced updates L_F≤1, α_k≤2cMδ at the sampled times. Consequently η≥1−C/M²−(L_D/2)(2cMδ)^γ. Minimizing C/M²+C′(Mδ)^γ over positive integers M gives

\[
(1-\eta)_+=O\big(\delta^{2\gamma/(2+\gamma)}\big).
\]

The positive-part notation prevents interpreting the statement as an upper bound on η. If L_F is bounded by a fixed constant strictly below one, uniformly in δ, bounded G_k instead gives (1−η)_+=O(δ^γ). For a fixed L_F>1 and the same uniform hypotheses, this argument gives an O((log(1/δ))^−2) bound by choosing M proportional to log(1/δ), with a sufficiently small proportionality constant. These are rates furnished by this argument, not sharpness claims. The power rate in L §13 requires a nonexpansive or comparable polynomial-growth hypothesis and control of decoder sensitivity; it does not follow for arbitrary L_F or δ-dependent decoder constants.

**Why uniform decoder control is necessary.** On the unit disk in ℝ² take the shear Φ(x,v)=(x+v,v), output O(x,v)=x, and, for δ>0,

\[
R_\delta(x,v)=\delta x,\qquad
F(q)=q,\qquad D_\delta(q)=q/\delta.
\]

The current-output error is η=0, while the one-step code residual is |δv|≤δ and L_F=1. For S_M={0,M}, the width satisfies β(V,S_M)≥(1+4/M²)^−1/2≥1−2/M², with V=ℝ². Indeed |v|≤2 max(|x|,|x+Mv|)/M. Intermediate shear states are convex combinations of the endpoint states, so normalized orbit-sphere pairs remain in the disk at every intermediate time. Thus the domain condition holds too. Nevertheless (1−η)_+=1 for every δ. The missing uniform hypothesis is exactly L_D: here L_D=1/δ. Code rescaling alone cannot imply the stated robust-error rate.

### 10.3 Sharper finite distinguishability depth {.unnumbered}

For a total deterministic map on N states, let E₀ be the current task equivalence with p blocks, and E_{h+1}=E_h∩(Φ×Φ)^−1E_h. Then

\[
\boxed{E_{N-p}=E_\infty.}
\]

If a round is not strict, it is already a fixed point and no later split occurs. Every strict round adds at least one block, and there are at most N−p such additions. Thus any pair ever distinguished by the task is distinguished by time N−p. This strengthens the true but loose N²−1 bound in L §22. The bound is attained for p=2 by the chain Φ(i)=max(i−1,0), with a task distinguishing state 0 from all others: states N−1 and N−2 first separate at time N−2.

### 10.4 Remaining mandatory qualifications {.unnumbered}

The earlier log's corrections remain in force: unrestricted fibre radius does not ensure a regular selector; continuous selection needs its native hypotheses; infinite path lifting needs closed nested completion sets and suitable compactness; a successor selector is only a predictor unless a common native path witness exists; support equality does not establish stochastic-law equality; physical quantum recovery requires a physical channel; and global injectivity alone does not imply an immersive realization.

In the resonance formula of L §39, the logarithmic expression also requires b≠0 and an appropriate integer power m≥1 for the stated continuous extension at v=0. At resonance with b=0, a=mb is also zero, and that displayed division by b is undefined. The algebraic nonresonant formula is retained when a≠mb.

## 11. Updated status of the thirteen open problems {.unnumbered}

“Completed” below refers only to the stated sector and theorem in this document.

| L open problem | Status after this review |
| --- | --- |
| 1. Nonlinear Jordan trajectory optimum | Current-output optimum and the d=n−1 trajectory endpoint are proved in section 4. Full finite-ε trajectory optimum for 1≤d<n−1 remains open. |
| 2. Jordan novelty audit | Not completed. A written proof is not a historical-priority determination. |
| 3. General approximate realization upper theorems | The heat cascade supplies a concrete semigroup-conditioned upper theorem. General selection, regularity, and optimality questions remain. |
| 4. Conditioned nonlinear repair | Still open in general. Section 9 completes the stated conditioned linear case with constants. |
| 5. Global smooth repair | Correct vertical-bundle necessity and Möbius example retained; section 6 supplies an additional existence obstruction. A general sharp global classification remains open. |
| 6. Coarsest native refinement | Positive for the compact Hausdorff setting in section 5. Negative in general for smooth-submersion realizations by section 6. Other target/dimension classes require separate answers. |
| 7. Continuous/smooth multi-Branch synthesis | Set-level existence and the compact total continuous sector are addressed. General smooth, partial, correlated, and infinite-dimensional synthesis is not settled. |
| 8. Stochastic refinement complexity | Explicit finite rational tables admit the polynomial refinement procedure in section 3. Succinct input and restricted-context complexity remain open. |
| 9. Physical quantum realization | Fully specified finite matrix channels have the exact feasibility criterion in section 8. General abstract/infinite-dimensional characterizations remain open. |
| 10. Infinite-dimensional closure price | One specified diagonal heat cascade is treated. General nonlinear PDE closure-price theory remains open. |
| 11. Uniform heat regularization | Completed in evolved-coordinate norm for positive modes. Uniformly vanishing common-δ generator defect is disproved on the ℓ² unit ball. |
| 12. State–memory–communication–time tradeoffs | The legacy memory contract is repaired and finite depth sharpened. The complete constrained Pareto theory remains open. |
| 13. External review and prior art | Selected classical sources checked. Comprehensive novelty review and independent peer validation are not completed. |

There is no defensible percentage-complete measure for this open-ended list. The next mathematically substantive targets remain the smaller-code Jordan trajectory optimum and a conditioned nonlinear realization theorem in a precisely fixed native class. Progress on either should produce a proof or counterexample with an actual performance consequence, rather than a new collection of labels.

## 12. Verification and reproducibility {.unnumbered}

The accompanying `bm_verification.py` ran successfully. It uses Python and NumPy and writes `verification_results.json`. During the verification amendment it was rerun, and its parsed result matched the original result exactly. All three source-file SHA-256 hashes also matched the saved source inventory.

| Check | Evidence |
| --- | --- |
| Deterministic exactification | All 4,096 combinations of a four-state deterministic update and a binary task; each computed terminal partition compared against all 15 partitions for exactness and coarsestness. |
| Partial multi-Branch refinement | All 81 partial binary Boolean-output Interaction tables, including unavailable outputs, under all 8 initial partition families: 648 models, each compared against all candidate interface families. Three specified local actions were included. |
| Jordan interpolation | Exact rational reconstruction of every monomial up to degree n−1 for n=2,…,6, with derivative constants and finite-direction checks of the width estimate. |
| Source approximation examples | Recomputed the shear errors and the weighted projector stationary candidates. Free weighted value ≈1.729299736; constrained value ≈4.764704744. |
| Heat repair | Checked the closed-form evolved mismatch against the modal and global bounds for 1, 16, 256, and 2,048 modes, two smoothing scales, and four times. Also evaluated the nonvanishing generator-residual sequence. |
| Quantum obstruction | Verified the forced linear map, its negative output-state and Choi eigenvalues, and the intertwining equations on matrix units. A separate diagonal-preserving evolution gives a positive closure example. |
| Conditioned linear repair | Checked the invariant graph and the squared-error bound for a concrete separated two-dimensional system. |
| Legacy memory | Verified the four-state counterexample and the required two-symbol auxiliary alphabet. |

The additional `bm_second_verification.py` uses Python, NumPy, and SciPy. Its exact finite checks use integer or rational arithmetic. Its quadrature and invariant-graph checks are floating-point consistency checks. It writes `second_verification_results.json`.

| Additional check | Evidence |
| --- | --- |
| Two-action deterministic exactification | 18,225 models on three states, covering every ordered pair of total actions and every pair of initial/required partitions. The all-word monoid construction agrees with iterative refinement and exhaustive comparison against all candidate equivalences; idempotence and contractiveness also hold. |
| Relational refinement | All 512 three-state successor relations under all five initial partitions: 2,560 models. Empty successor sets are included; each result is compared against every admissible equivalence. |
| Stochastic refinement | All 216 three-state kernels with entries in {0,1/2,1}, under all five initial partitions: 1,080 models. Aggregation and coarsestness are checked using exact integer sums. |
| Quantum certificates | Exact rational verification of the negative eigenvalues −1/2 and 3/2 in the dephasing obstruction. A separate two-qubit-to-one-qubit partial-trace compression has an explicit positive-semidefinite Choi factorization, the trace-preservation certificate, and all 16 native matrix-unit closure equations. |
| Heat mismatch | 96 modal comparisons of the direct evolved-coordinate formula against numerical integration of the residual, with maximum normalized disagreement below 2.7×10⁻¹⁵. This checks the modal identity by another method; the infinite-dimensional passage remains the written summability argument. |
| Matrix graph repair | Six cases with two-dimensional graph blocks in a four-dimensional system, including nonnormal blocks, Δ=0, and E_free=0. Invariance residuals were below 2.3×10⁻¹⁵, and the constructed errors obeyed the bounds. |
| Decoder scaling | Evaluated the section 10.2 counterexample at δ=1, 0.1, 0.01, and 0.001. Its formulas prove the failure for every δ>0 without uniform decoder control. |

The second script checks 21,865 additional finite models across the first three rows. These counts enumerate small cases; they are not counts of separately proved theorems. Both verification passes were performed by the same reviewer.

These finite checks do not prove Borsuk–Ulam, arbitrary-map impossibility, a smooth global theorem, or an infinite-dimensional estimate. Those rely on the written arguments. No numerical quantum SDP solver or proof assistant was used. The source calculator and website were not tested because their implementation files were not part of this source set.

Reproduce the checks from the archive directory:

```bash
python3 bm_verification.py --output verification_results.json
python3 bm_second_verification.py --output second_verification_results.json
```

## 13. Defensible final formulation {.unnumbered}

The reviewed core of Branch Mathematics is established internally as a typed mathematical treatment of representation, interaction, continuation, realization, and receiver-relative reuse. Its abstract deterministic completion has a precise greatest-equivalence theorem. Finite relational and stochastic interfaces have explicit refinement procedures. Native realization has both positive theorems and genuine obstructions. Closure can carry a quantitative approximation price, and a small instantaneous defect can behave differently from a small evolved error.

This review strengthens that content with the proofs above and corrects the contracts needed to use it. It does not certify an unlimited subject as finished. It establishes no new physical law, no general Navier–Stokes regularity or Yang–Mills mass-gap solution, and no theorem of universal physical information conservation. Those conclusions do not follow from the representation mathematics.

The concrete value of BM here is that one native problem can demand different retained distinctions for current accuracy, future prediction, physical admissibility, locality, and stability. The useful output is a calculation, construction, or obstruction showing how those requirements interact. The next edition should retain that content and this explicit status boundary.

## 14. Verification amendment: what changed and what is verified {.unnumbered}

Edition 1.0 should not be described as fully correct without qualification. Its principal arguments survive the further review, but two formal hypothesis omissions required correction. The amended claims below are the claims verified in edition 1.1.

| Claim or issue | Verification finding and amendment |
| --- | --- |
| Local differential augmentation bound, §5.2 | The chain-rule proof is valid when A is C¹ and each decoder is C¹ on an ambient neighborhood of the represented point. Those conditions are now explicit. Constant-rank smooth local attainment is retained; global attainment is not asserted. |
| Robust-width asymptotics, §10.2 | The claimed rate requires constants uniform as δ→0 as well as M→∞, and a bound max S_M≤cM. These conditions are now stated. The rescaled-shear counterexample proves that omitting uniform decoder control can make the conclusion false even with a nonexpansive update. |
| Quantum physicality, §8 | The input-first Choi convention, trace condition, and intertwining equations are consistent. Exact rational positive and negative examples verify the implementation. The obstruction tests the full reduced matrix algebra required by the contract. |
| Heat cascade, §7 | The common-δ generator estimate remains false uniformly on the ℓ² unit ball. The evolved-coordinate bound, continuity of Q₀, and fixed-δ smoothness of Q_δ survive the proof review; the summable n⁻⁴ bound justifies the infinite-mode step. |
| Other central constructions, §§3–6 and 9–10 | No counterexample or remaining proof gap was found within the amended hypotheses. The Jordan result retains global encoder/closure assumptions, and the smooth-submersion counterexample concerns that specified realization class. |
| Endpoint and notation cleanup | Stated n≥2 and 0<T<∞ in the Jordan setting, excluded the zero subspace from β's definition, stated A and s>0 in the linear theorem, defined r also at Δ=0, made the heat uniform norm explicit, and required nonempty X for the finite-memory maximum. |
| Reproducibility and provenance | The original results reproduced exactly, all source hashes matched, and the additional checks in §12 passed. The archive includes both scripts and both result files. |

**Verdict:** The corrected statements have written proofs and the reported consistency checks. This is internal mathematical verification with explicit hypotheses, not formal certification, independent peer review, or a proof that the entire BM research program is complete. The unresolved items in section 11 remain unresolved.
