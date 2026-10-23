# About this edition {.unnumbered}

## Mathematical edition of 10 September 2026 {.unnumbered}

Branch Mathematics is a mathematical metaframework for carrying one problem through distinct mathematical Branches while preserving their native mathematics and governing representation, interaction, realization, comparison, export, and reuse. GURF is its response-specialized framework. This edition develops their operational core: determine which distinctions a receiver needs, test whether a representation preserves them, derive the additional distinctions needed for continued operation, and compare admissible representations quantitatively.

The main results are finite global interface synthesis, its relational extension, and an exact criterion for when an orthogonal representation attains an unrestricted reconstruction optimum. The proofs include hypotheses, constructions, necessity arguments, and failure boundaries. Supporting quotient and composition facts remain supporting results; their short proofs are not presented as discoveries of a new mathematical field.

The edition is complete for the statements proved here. It does not assert completion of all BM research, external priority, a universal physical law, or a solution of the Navier–Stokes or Yang–Mills existence problems. Definition, proof, numerical evidence, physical interpretation, and historical novelty are separate kinds of claims. SSH is retired and supplies no assumption to any result in this edition.

### Reading order {.unnumbered}

Chapters on foundations and GURF define the objects. The finite synthesis and representation chapters contain the principal developments. The numbered register supplies explicit statements and proofs for T01–T55. The model chapter specifies the animated experiments. The final audit records limitations, source reconciliation, and the prior-art crosswalk.

# Foundations

## Typed objects and lawful transformations

A problem specification fixes a scope, native mathematical sectors, terminal obligations, allowable interventions, and comparison rules. Distinct Branches are mathematical focuses of that problem; they need not be unrelated subproblems or identical kinds of object. A Branch may contain a relation, a state space, an operator system, or a complete subsystem. A useful record is

$$B=(\mathsf S_B,\tau_B,X_B,A_B,\mathcal L_B,\mathcal O_B,\mathcal P_B).$$

Here $\mathsf S_B$ is the native sector, $\tau_B$ the type, $X_B$ its carrier, $A_B$ its admissible objects, $\mathcal L_B$ its declared laws, $\mathcal O_B$ its operations, and $\mathcal P_B$ its contracts in context. This record imposes no common topology or universal notion of information amount. The native sector supplies domains, smoothness, measurability, units, algebra, positivity, or other needed structure.

An Operation is a specified native action. In a deterministic set sector it is a partial map $f:D_f\subseteq X\to Y$. An Interaction combines declared inputs; in that sector it is

$$G:D_G\subseteq A_1\times\cdots\times A_m\longrightarrow W.$$

Input admissibility does not establish membership in $D_G$. For example, positive lengths can each be admissible while their proposed triangle fails the triangle inequality. An output inherits a topology, conservation property, or algebraic operation only through a specified construction or proof. The names Branch and Interaction supply none of those properties.

A Leaf is a derived result with its native statement, hypotheses, actual derivation, and provenance. A numeric output without a validated domain and error model is a computed value, not a universal theorem. A Leaf can be reused if its hypotheses remain true at the new use.

## Contracts and Passports

A contract is a typed specification $\mathcal C^\rho=(\Sigma^\rho,\Phi^\rho)$; a Passport is its instantiation $\mathcal P^\rho_{\theta,c}$ at parameters and context. In a predicate sector, write $(D_{\mathcal P},A_{\mathcal P})$ with $A_{\mathcal P}\subseteq D_{\mathcal P}$. The three outcomes are not applicable, applicable and rejected, and accepted. Acceptance may include several explicit obligations; passing one does not pass all of them.

On a common applicability domain, $A_2\subseteq A_1$ means Passport 2 is at least as restrictive. If domains differ, record both domain and acceptance inclusion. Pullback along a total export $E:X\to Y$ is

$$E^*(D,A)=(E^{-1}D,E^{-1}A).$$

For a partial export, first restrict to its actual domain. Exact task requirements may be encoded by functions, but a general Passport is not automatically a deterministic observation function.

## Configuration and Tree

A Configuration is $C=(\Sigma_C,\Gamma_C,c)$. The signature $\Sigma_C$ declares typed objects and coordination data; $\Gamma_C$ declares obligations; $c$ declares context. The realization family is

$$\mathfrak F(C;c)=\{\xi\in\operatorname{Int}(\Sigma_C;c):\xi\models_c\Gamma_C\}.$$

Interpretation and satisfaction are native-sector relative. Writing this family is not an existence proof. Well-formedness means the expressions are meaningful and correctly typed. Global realizability means $\mathfrak F(C;c)\ne\varnothing$. A realized Tree can be recorded as $\mathcal T=(C,\xi,\Pi,\omega,\Lambda)$, where $\xi$ is a realization, $\Pi$ the certified provenance/dependency record, $\omega$ the declared order or history context, and $\Lambda$ the active law assignments. The dependency structure may contain local trees inside a DAG or hypergraph; a name does not turn cycles into well-founded recursion.

A Response is a declared Tree-level output, possibly law-valued or set-valued. An export translates it to a receiver's type. A Root is an export accepted under that receiver's Passport, carrying the information and evidence required by that contract. Receiver-relative Root status does not imply acceptance by another receiver or under a later context. Re-entry is a new use requiring the receiving obligations. Candidate Rooting, Rebranching, and Seed constructions remain separately scoped research structures; none is needed to make the proved core work.

## Three different closure universes

Component dependency closure is $\operatorname{Cl}_C:2^{V_C}\to2^{V_C}$. Obligation prerequisite closure is $\operatorname{ReqCl}_C:2^{\Omega_C}\to2^{\Omega_C}$. Each must be extensive, monotone, and idempotent before least-closure language is used. Required obligations are $\mathscr Q_P=\operatorname{ReqCl}_C(\mathscr T_P)$. A third construction refines equivalence relations on state carriers. It is not either of the first two operators.

A Branch is essential relative to a fixed, independently specified coarsening class if every candidate removing its distinctions loses a required obligation. Defining that class by already preserving those same obligations would make the test circular. Essentiality need not be absolute, and Branch count is not an invariant of a mathematical object without an equivalence and irreducibility theorem.

## Representation and admissibility

For functions $R:X\to Z$ and $T:X\to W$, exact task sufficiency means $T=\bar T R$ on $X$, equivalently $\ker R\subseteq\ker T$. This is an exact set-level condition. It promises no continuous, computable, stable, positive, or physically implementable decoder. A strict embedding preserves the native embedding properties; a task-sufficient representation can be noninjective.

Structured quotients require congruence with every declared operation, including domain saturation for partial operations. A law transport must name the map on laws and prove its satisfaction condition. Coherence compares outputs in a common declared comparison space on a common domain. Equality-based path coherence is transitive. Pairwise local satisfiability and higher-order gluing are different obligations.

For $\Phi_t:D_t\to X$, exact partial Dynamic Closure through $R$ requires both

$$D_t=R^{-1}(\bar D_t),\qquad R\Phi_t=\bar\Phi_tR\quad\text{on }D_t.$$

The theorem assumes that $D_t$ and $\Phi_t$ are already specified. It neither constructs a PDE solution nor extends one through a singular endpoint. A separate availability tag records undefinedness; it is not a physical state or a diagnosis of why evolution failed.

## Distinctions and physical interpretation

An exact deterministic representation cannot recover distinctions it identifies using only subsequent deterministic processing. A repair can add another observation, retained history, or an independently specified source. It cannot invent a missing distinction. Injectivity of declared total evolution is a precise mathematical persistence condition. Universal physical information conservation is a modeling commitment requiring additional physical assumptions; it is not deduced from the word Passport or from a many-to-one representation.

BM need not take probability as a primitive of its core. When an external stochastic model is used, its kernels, coupling, and expectations retain their ordinary mathematical meanings. Relational reachable sets do not determine probability laws. Quantum density-matrix algebra, observable statistics, and physically admissible quantum channels are likewise different levels of description.

## Defect and repair

A defect records failure of a named obligation $\Psi$, not an unspecified scalar measure of badness. Repair is a declared admissible relation between Configurations with explicit change support and revalidation. Defect Calculus remains an active specialized program; no universal scalar or algebra of defects is assumed.

Use BM when several representations, interfaces, admissibility requirements, or response tasks require coordination. When the native mathematics already answers a question and BM adds no distinction, calculation, or certificate, use the native result directly. Adding role names alone does not add mathematical content.


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

GRDE remains frozen at GURF-GRDE-008. Existing diagrams describe declared response structure and provenance. This edition introduces no new GRDE axioms or approved structural iconography. A diagram records maps and obligations; it does not prove they exist, commute, or have limits. The animated models in this edition are native coordinate calculations, not animations of abstract Roots or Seeds.

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

$$u\ C_{b,p}(E_{r(b)})\ v\quad\Longleftrightarrow\quad
\widehat G_b(c_1,\ldots,u,\ldots,c_m)
\ E_{r(b)}^{\bot}\
\widehat G_b(c_1,\ldots,v,\ldots,c_m)
\quad\text{for every other input tuple }c.$$

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

The calculator stores each round and a reason for every split: distinct successor signatures, a defined/undefined mismatch, or an Interaction context with distinct receiver signatures. These witnesses can be replayed from the finite tables. They are certificates of this supplied finite model; they are not physical measurements or claims of optimal hardware cost.

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

The vertical direction must also be checked. Evaluating all real stationary directions and the vertical direction gives approximately $4.764704744$, with $t\approx1.13317887$. Those decimals are numerical illustrations; strict positivity of the price was already proved exactly.

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

At an exactly globally minimizing $\tau_*$, every unit minimum eigenvector $u$ is balanced and minimizes the product. Indeed its squared scalar value divided by four equals $m$; AM–GM gives $ab\le m$, while the definition of $m$ gives $ab\ge m$. Equality forces balance. Multiplying the eigen-equation by $\sqrt{ab}$ gives $bKu+aSu=2ab\,u$. This argument also covers a multiple minimum eigenvalue. A numerical or merely local scalar minimizer does not inherit this conclusion and must be checked. $\square$

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

The excess over $\operatorname{tr}(AB)$ is nonnegative by Frobenius Cauchy–Schwarz and vanishes exactly when $A$ and $B$ are positive scalar multiples. A scalar analogy cannot replace the matrix balancing proof. $\square$

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

The method is classical moment relaxation. The mathematical contribution here is the complete derivation from this representation Passport and its integration with the exact admissibility test. General noncommuting higher-rank global solution remains an active problem.


# Canonical supporting result register

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

The finite-product qualification is essential. On $\{0,1\}^{\mathbb N}$, the predicate “infinitely many coordinates are 1” has no individually essential coordinate but changes between the all-zero and all-one sequences. Constrained products also require an admissible-path argument; coordinate replacements may leave the source domain.

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

**Stochastic quantitative theorem.** In the finite setting of T29, suppose aggregated rows in each observation block have total-variation diameter at most $\varepsilon$. Choose one representative row per block to form $\bar K$. Then $d_{\rm TV}(R_\#(\mu K),(R_\#\mu)\bar K)\le\varepsilon$ for every initial law $\mu$.

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

**Quantitative specialization.** For nonempty metric task family $T_i:X\to W_i$, use the product output with sup distance (possibly extended) and $\omega(R)=\sup_{R(x)=R(x')}\sup_i d_i(T_i(x),T_i(x'))$. Unrestricted joint-task decoders satisfy $\omega/2\le e^*\le\omega$ when fibre representatives exist. Moreover $\omega=0$ iff every task factors through $R$.

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



# The animated universe model page

## What the figures represent

The page offers six moving three-dimensional views: galactic orbits, incompressible fluid trajectories, qubit precession, Newtonian gravity, electromagnetic waves, and heat diffusion. Each view has its native equations, parameter domain, state variables, receiver task, observation loss, and computational method. BM coordinates those branches and audits the retained distinctions. These figures do not establish a BM cosmology or a new physical force law.

Three-dimensional display coordinates need not all be spatial coordinates. The qubit sphere is state geometry. The heat surface uses two spatial coordinates and temperature as height. The wave curves encode field components. Those distinctions are stated on the page. Camera rotation changes only the view, while the animation changes variables defined by the equations.

## Galactic circular orbits

For $\Phi(r)=-\mu/\sqrt{r^2+a^2}$, acceleration is $-\nabla\Phi=-\mu x/(r^2+a^2)^{3/2}$. A circular trajectory $x=r(\cos\omega t,\sin\omega t,0)$ has acceleration $-\omega^2x$. Hence it is an exact solution when $\omega^2=\mu/(r^2+a^2)^{3/2}$. Orthogonal rotation to another orbital plane preserves this central-force equation. The page initializes a fixed deterministic family of nearly coplanar circular orbits. No distribution is fitted and the particles do not interact gravitationally with one another.

Radius is exactly constant within this family. A radius-only representation suffices for radial tasks and cannot recover phase-sensitive position tasks. There is no inferred energy addition, dark-matter explanation, or galaxy-formation mechanism. The potential is a declared classical input model.

## Incompressible ABC flow

For $u=(\sin z+\cos y,\sin x+\cos z,\sin y+\cos x)$, each component is independent of its matching coordinate, so $\nabla\cdot u=0$. Direct differentiation gives $\nabla\times u=u$ and $\Delta u=-u$. The vector identity $(u\cdot\nabla)u=\nabla(|u|^2/2)-u\times(\nabla\times u)$ therefore reduces to the gradient term. With $p=-|u|^2/2$, the field solves stationary incompressible Euler. If viscosity is included, forcing $f=\nu u$ balances $\nu\Delta u$ and gives a specific forced stationary Navier–Stokes solution.

The displayed tracers solve $\dot x=u(x)$ numerically with fourth-order Runge–Kutta on the periodic cube. This computes trajectories in a supplied field, not unknown general fluid evolution. The mean kinetic energy of the field is $3/2$ for unit amplitude, because cross sine-cosine terms average to zero and each squared trigonometric term averages to $1/2$.

## Qubit state geometry

Let $H=\hbar\Omega\sigma_z/2$, $U(t)=\exp(-iHt/\hbar)$, and $\rho=(I+r\cdot\sigma)/2$. Computing $U\rho U^*$ rotates $(r_x,r_y)$ by angle $\Omega t$ and leaves $r_z$ fixed. Equivalently $\dot r=\Omega e_z\times r$, so $d|r|^2/dt=2\Omega r\cdot(e_z\times r)=0$. For $|r|=1$ the state remains pure. The page shows this state vector, its circular orbit at fixed polar angle, and the three observable expectation values.

A $\sigma_z$ observation alone cannot distinguish transverse phases. The page describes the density-matrix/observable model and does not assert that the Bloch vector is an electron position or that a single measurement reveals its components exactly.

## Kepler gravity and tidal response

For $0\le e<1$, $a>0$, and $\mu>0$, let $n^2=\mu/a^3$ and solve $E-e\sin E=nt+M_0$. Since $1-e\cos E>0$, the mean anomaly determines a unique eccentric anomaly on each unwrapped period. Then

$$x=a(\cos E-e),\qquad y=a\sqrt{1-e^2}\sin E.$$

Differentiating the anomaly equation gives $\dot E=n/(1-e\cos E)$. With $r=a(1-e\cos E)$, a second differentiation of $x,y$ gives $\ddot{\mathbf x}=-\mu\mathbf x/r^3$. The specific energy is $-\mu/(2a)$ and angular momentum magnitude is $\sqrt{\mu a(1-e^2)}$. The differential acceleration tensor is $\mu(3\hat r\hat r^\top-I)/r^3$, with radial eigenvalue $2\mu/r^3$ and transverse eigenvalues $-\mu/r^3$. The page shows a radial tidal direction and computes its current magnitude.

Newton iteration solves the anomaly equation numerically and reports its residual. The model is a weak-field classical test-particle system. It is not an Einstein-equation solution or a derivation of gravity from information.

## Electromagnetic plane wave

Set $E=A\cos(kz-\omega t)e_x$ and $B=(A/c)\cos(kz-\omega t)e_y$, with $\omega=ck$. Both divergences vanish. Direct differentiation gives $\partial_t B=-\nabla\times E$ and $\partial_tE=c^2\nabla\times B$. Thus these fields satisfy source-free Maxwell equations in vacuum. The display uses normalized $c=1$. The cyan and gold curves are field-component plots, not matter trajectories. Squared field intensity identifies opposite signs and therefore does not retain all phase-sensitive tasks.

## Heat diffusion surface

For $T=1+A e^{-2\kappa t}\cos x\cos y$, differentiation gives $\partial_tT=-2\kappa A e^{-2\kappa t}\cos x\cos y$ and $\Delta T=-2A e^{-2\kappa t}\cos x\cos y$. Hence $\partial_tT=\kappa\Delta T$ with periodic boundaries. The spatial mean is 1 and the mean squared deviation is $A^2e^{-4\kappa t}/4$. The mean-only representation is insufficient for recovering the nonconstant mode. The rendered height is the declared display coordinate $1.7(T-1)$, not physical geometry.

# Counterexample atlas and final mathematical audit

## Corrections made in this edition

| Issue | Correct mathematical treatment |
|---|---|
| Local compatibility called path coherence | T24 remains pointwise transitivity; T25 is a cyclic separator/gluing obstruction. |
| Partial operations compared only by outputs | Preserve domain saturation and a distinct undefined tag. |
| Finite repair support extended to arbitrary products | T28 requires finite coordinates, or an additional finite-change/continuity argument. |
| Local closure assumed sufficient for coupled closure | Require Interaction descent or audit the joint transition directly. |
| Minimum exact interface called cheapest representation | Coarsest equivalence only; implementation cost needs a declared optimization problem. |
| Approximate distance threshold called a quotient | Nontransitivity prevents this in general. |
| Empty Hausdorff successor sets ignored | Restrict to nonempty compact sets or provide a separate dead-end metric convention. |
| Exact matrix inversion called physical quantum reversal | Distinguish known-matrix algebra, stable inversion, and an admissible recovery channel. |
| Stationarity or floating-point SDP called a global proof | Use exact equality cases, feasible primal/dual certificates, or a stated numerical error analysis. |
| Noncommutation used as a universal positive-price test | LEV 014C tests compatibility of the maximizing spectral subspace with $S$. |
| Degenerate eigenvector warning at an exact scalar global minimum | LEV 015's equality argument proves every minimum eigenvector is balanced there. |
| Probability treated as relational reachability | Preserve imported stochastic kernel semantics; use T29, T41, T42, T53. |
| UKE implicitly renamed by a later summary | Retain Unified Kernel Extension and its native kernel/operator roles. |

## Additional important proof boundaries

For $x(t)=1/(1-t)$ on $[0,1)$ every finite-time value exists, yet no finite endpoint exists at 1. The representation $R(x)=x/(1+x)$ stays bounded and tends to 1; its inverse $y/(1-y)$ is singular there. On $[0,1-\delta]$ the inverse derivative is at most $\delta^{-2}$, so an approximate inverse bound depends explicitly on the distance to the boundary. Finite legal steps and bounded reduced coordinates do not establish analytic continuation.

For qubit dephasing $\mathcal D_\lambda(\rho)_{01}=\lambda\rho_{01}$ with unchanged diagonal and known $0<\lambda<1$, the full output matrix determines the input algebraically by dividing the off-diagonal entry by $\lambda$. That inversion amplifies coherence error by $1/\lambda$. It is not a positive map on all density matrices: applied to a matrix with every entry $1/2$, the candidate inverse has eigenvalues $(1\pm1/\lambda)/2$, one negative. At $\lambda=0$, opposite coherences have the same output, so even exact matrix recovery fails. Physical recovery, exact algebra, and stable inference must not be conflated.

For relations, let $xRa,xRb$, let $a$ have no $S$-successor, and let $bSz$ with $z\in U$. The composite has a nonempty set of successors all in $U$. Nevertheless the intermediate state $a$ fails nonblocking safety. Thus requiring nonblocking at every stage is stronger than requiring one nonblocking composite continuation. Ordinary box composition cannot be reused after silently changing box semantics.

## GURF and application status

Core, SOE, ACE, IRE, UKE, HDE, and GHSE retain their declared roles; GRDE remains frozen at 008. HDE does not create a halo substance or hidden energy source. GHSE does not add binding energy by terminology. Seeds, Rooting, and Rebranching remain candidate constructions except for the particular ordinary mathematics explicitly instantiated and proved. A physical experiment may use such a candidate, but its outcome would have to test an independently specified model.

The NS and Yang–Mills research programs retain their native hypotheses and open application gates. T34 and the fluid view provide specific exact identities/models; they do not establish general regularity. T35 provides gauge invariance; it does not establish a continuum mass gap. Earlier archived NS and YM Leaves require their complete original derivations and analytic assumptions before they can be promoted to a self-contained theorem in this edition. Corpus A's 200-equation review remains historical validation work, not 200 new BM theorems.

The LEV 001–012 sequence contains threshold, dimension, weighting, and control specializations leading to the weighted reconstruction problem. Their sixteen labels are retained as research provenance, not represented as sixteen independent discoveries. Their strongest current reconstruction statements are consolidated in LEV 013–016 here. Any full-state-informed control repair must state its lawful information source; minimizing an omniscient repair cost does not make that information available to a compressed controller.

## How to audit a claim with BM

1. Write the native objects, types, domains, units, and context.
2. State the receiver task and every acceptance obligation.
3. Name the representation and the candidate comparison class.
4. Test fibre sufficiency, definedness, and the appropriate successor semantics.
5. Check Interaction descent, shared witnesses, and global realization separately.
6. Give the actual proof or numerical certificate, including approximation and limit assumptions.
7. Record what is proved, what is classical, what is only modeled, and what remains unresolved.

## Source reconciliation and coverage

The source baseline is the public BM/GURF website retrieved from its repository on 10 September 2026, the September 9 website synchronization package, the prior Branch Mathematics book, the T01–T53 consolidation and dependency register, the continuation amendment, LEV 013–016 and the strengthened certificate notes, the canonical review log dated 10 September, and the recovered September 9 status registry (all 17 stable BM-STATUS identifiers are retained). The later canonical corrections govern conflicting older formulations. The book and site preserve stable T identifiers; the old detailed theorem page is retained as an additional supporting-proof reference with its existing anchors.

This edition gives explicit proofs for the corrected T01–T55 entries, the finite T55 corollary family, and the selected representation results. The interface and optimization chapters supply their own constructions and necessity proofs. Historical application notes, unavailable full derivations, and uncompleted research programs are not silently certified by inclusion in a registry. External validation and historical priority remain unresolved; mathematical completion is a property of a specified theorem under hypotheses, not of an unlimited research subject.

## Prior-art crosswalk

The weighted reconstruction argument is a direct specialization of classical low-rank approximation. The BM use specifies the task metric and representation admissibility; LEV 014C adds the exact equality test for the stricter projector class. The historical source is [Eckart and Young, The approximation of one matrix by another of lower rank, 1936](https://link.springer.com/article/10.1007/BF02288367).

The finite refinement theorem belongs to the established stable-partition/bisimulation tradition. Its BM development carries receiver requirements, partial Interaction domains, and explicit contextual witnesses together. This is not evidence of historical novelty over general refinement methods. See [Paige and Tarjan, Three Partition Refinement Algorithms, 1987](https://epubs.siam.org/doi/10.1137/0216062) and [Ranzato and Tapparo, Generalizing the Paige–Tarjan Algorithm by Abstract Interpretation](https://arxiv.org/abs/cs/0612120).

Join-tree gluing, congruences, satisfaction-preserving translations, Markov lumpability, matrix balancing, and moment relaxations likewise have classical owners. The complete proofs here establish the scoped results without claiming priority for those ingredients. A comprehensive theorem-level novelty audit would need explicit reductions against institutions, contract/interface theory, abstract interpretation, bisimulation, decision theory, categorical semantics, and polynomial optimization; a short crosswalk does not complete that task.

The symbolic calculator uses the versioned Pyodide/SymPy runtime described by the [official Pyodide setup documentation](https://pyodide.org/en/stable/usage/quickstart.html). The finite BM engine and six moving coordinate models use local JavaScript and require no symbolic-runtime download. The formal source and computational implementation have different roles: passing finite tests supports the implementation; it is not a substitute for the general proofs.
