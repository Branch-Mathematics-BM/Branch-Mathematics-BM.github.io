# Branch Mathematics — Volume II Development Log
## Developments and Applications — 2026-09-12

**Status:** Development log above the frozen Version 1 foundation. Version 1 is unchanged. No T01–T55 renumbering or redesign. New statements remain CH-C/BM-SYN unless separately promoted after audit; classical ingredients remain CI.

## 1. Existing Volume II base

The already-developed Volume II families remain active: nonlinear fibre repair (NLR); topology/gauge/bundle descent (TOP/CIRC/GAUGE/BUNDLE); quantum operator-system/algebra carriers (QSYS/QALG); stochastic and finite exactification (STOCH/FIN/SFIN); structured repair (SRP); Pareto/duality (PAR/DUAL); Passport perturbation (PST); distinction geometry and dynamic distinction geometry (DIST/DYN); continuous latency and sensor design (CDL/SENS); exact and approximate end-to-end scheduling (E2E/AE2E); robustness and resource allocation (RES/ALLOC); failure localization and provenance (FLOC/PROV); compositional and hierarchical interfaces (COMP/HIS); exact and approximate semantic width (WIDTH/AWIDTH).

The common architecture remains

\[
\boxed{\text{Carrier}\to\text{Witness}\to\text{Repair modulus}\to\text{Propagation}\to\text{Pareto selection}.}
\]

## 2. Continuum/PDE semantic width

For an infinite-dimensional state space, admissible set \(K\), and receiver profile \(\mathcal P\), define

\[
N(\varepsilon)=\mathcal N(\mathcal P(K),\varepsilon),\qquad
w(\varepsilon)=\log_2N(\varepsilon).
\]

**PDEW-01 — Compact Profile Criterion.** In a complete profile metric space,

\[
\boxed{N(\varepsilon)<\infty\ \forall\varepsilon>0
\iff \mathcal P(K)\text{ is relatively compact}.}
\]

**PDEW-02 — Spectral Width Bound.** For compact linear profile operator \(\mathcal O\) with singular values \(\sigma_j\), if \(\sigma_{n+1}\le\varepsilon/2\),

\[
\boxed{N(\varepsilon)\le\prod_{j=1}^n\left(1+\frac{4\sigma_j}{\varepsilon}\right).}
\]

**PDEW-03 — Positive-Time Smoothing Gap.** Heat evolution gives a sector where exact/full-state approximate width is infinite at \(t=0\) but finite at every positive tolerance after any \(\tau>0\). With Weyl growth,

\[
w_\tau(\varepsilon)\asymp
\tau^{-d/2}\left(\log\frac1\varepsilon\right)^{1+d/2}
\]

up to the stated spectral/geometric assumptions.

**PDEW-04/05.** Nonlinear positive-time compactness gives finite approximate width; Kolmogorov \(n\)-width bounds imply semantic covering-number bounds. Small semantic width is not the same as small linear reduced dimension.

Permanent PDE firewall:

\[
\boxed{\text{small receiver-profile width}\not\Rightarrow\text{global PDE regularity}.}
\]

## 3. PDE ports and transfer operators

For a boundary trace \(g\), coupling response \(\Lambda g\), and receiver task \(Lg\):

**PORT-01**
\[
\boxed{E_{\rm port}=\ker\Lambda\cap\ker L.}
\]

Task-irrelevant distinctions cannot be discarded if they are still needed for native coupling.

**PORT-02.** A boundary operator bounded below on an infinite-dimensional trace subspace yields infinite approximate width below a nonzero scale for arbitrary full-trace coupling.

**PORT-03.** If lawful traces come from a compact transfer map \(\mathcal T\), the reachable port family is approximately finite-width even when the full trace space is not.

**PORT-04.** A task-filtered port is governed by

\[
\boxed{\mathcal T_{\mathcal P}=C\mathcal T.}
\]

**PORT-05.** For \(Sg=\sum_iB_if_i\), \(z=Cg\), subsystem \(i\)'s exact deployment-specific contribution is

\[
\boxed{G_i=CS^{-1}B_i.}
\]

**PORT-06.** Port approximation error propagates through Schur conditioning:

\[
\boxed{\|C(g-g_n)\|\le \|C\|\frac{M}{\alpha}\varepsilon_n.}
\]

## 4. Time-dependent PDE ports

With reachability \(\mathcal R_t\) and future Passport observation \(\mathcal O^{\mathcal P}_{t,T}\), define the finite-horizon Hankel map

\[
\boxed{\mathcal H_t^{\mathcal P}=\mathcal O^{\mathcal P}_{t,T}\mathcal R_t.}
\]

**TPORT-01/02.** The exact causal state is the future-profile quotient, equivalently the past-history quotient by \(\ker\mathcal H_t^{\mathcal P}\).

**TPORT-03.** Compact Hankel map iff bounded past-history families have finite positive-tolerance semantic width.

**TPORT-04.** The quotient descends causally under evolution.

**TPORT-05.** For pure transport with delay \(\tau\), cut time \(t\), deadline \(T\), the exact live delay memory is

\[
\boxed{u|_{[t-\tau,T-\tau]\cap[0,t]}.}
\]

**TPORT-06/07.** Finite propagation gives exact deadline pruning; parabolic systems can have \(\tau_0=0\) but \(\tau_\varepsilon>0\), so exact influence time and usable distinction time are different.

## 5. Distributed causal cuts and spacetime width

For a cut \(\Sigma\), exact joint messages must satisfy

\[
\ker R_\Sigma\subseteq E_\Sigma.
\]

Hence

\[
\boxed{\sum_{e\in\Sigma}\log_2|Q_e|\ge\log_2|Q_\Sigma^*|.}
\]

This is necessary but not sufficient under distributed locality.

**DCUT-02.** In the linear sector, route \(j\) adds no new semantic content beyond route set \(S\) iff \(H_j=K_jH_S\).

**DCUT-03/04.** Exact \(f\)-route survivability requires every allowed survivor set to remain sufficient. Necessary total cut capacity obeys

\[
\boxed{C_{\rm total}\ge\frac{m}{m-f}C_{\rm semantic}.}
\]

**STW-01/02.** For prefix \(p\), residual response \(\rho_p(s)=\widehat T(p,s)\) gives the exact spacetime equivalence. Residual equivalence is a right congruence and therefore forms a canonical causal quotient machine.

**STW-03.** Exact streaming width along order \(\pi\):

\[
\boxed{W_{\rm ST}(\pi)=\max_k\log_2|Q_k^*|.}
\]

**STW-05.** Approximate residual covering numbers lower-bound causal state size, but independent approximate optimum covers need not compose causally.

**STW-06/07.** Centralized, causal, and distributed/locality-respecting width are different. Bounded semantic width plus efficiently constructible interfaces can yield hierarchical scalability; small width alone does not guarantee easy discovery.

## 6. Coupling, locality, and many-body structure

For coupling parameter \(\lambda\) and contextual distance \(D_\lambda\):

**COUP-01.** Uniform response perturbation \(\delta\) gives

\[
\boxed{|D_\lambda-D_0|\le2\delta.}
\]

**COUP-02.** Hausdorff profile perturbation gives width sandwich

\[
\boxed{N_0(\varepsilon+\delta)\le N_\lambda(\varepsilon)\le N_0(\varepsilon-\delta).}
\]

**COUP-03/04.** Exact equivalence can split for arbitrarily small nonzero coupling; the first nonzero perturbative order controls the approximate splitting threshold.

**COUP-06.** A positive tolerance margin yields a certified coupling-stability radius.

**COUP-09.** For bounded linear generator perturbation,

\[
\boxed{\delta_H(\lambda)\le |\lambda|\|C\|M^2\|V\|He^{\omega H}.}
\]

Many-body semantic interaction radius:

\[
\boxed{r_{\rm sem}(H,\varepsilon)=\inf\{r:\eta(r,H)\le\varepsilon\}.}
\]

Under exponential influence decay,

\[
\boxed{r_{\rm sem}\lesssim vH+\mu^{-1}\log(C/\varepsilon).}
\]

**LOC-02/03.** Exact or approximate semantic Markov blankets factor exterior response through a boundary statistic.

**LOC-04.** Conditional semantic area law:

\[
\boxed{w_A(\varepsilon)\lesssim |\partial_{r_{\rm sem}}A|\log q.}
\]

Local physical interactions alone do not imply this area law; a full-state Passport can force volume width.

**CLUST-01/02.** Cluster truncation error composes with representation error; on cluster trees, semantic separator quotients can replace raw separator configurations.

## 7. Quantum many-body semantic carriers

Let \(\mathcal S_R\) be the receiver operator system and pull it backward:

\[
\mathcal S_H=\operatorname{span}\{I,\Phi_t^\dagger(O):O\in\mathcal S_R,0\le t\le H\}.
\]

**QLOC-01.** A local CPTP carrier \(\mathcal E_A\) is exact when every required pulled-back observable factors through

\[
\boxed{\mathcal E_A^\dagger\otimes\operatorname{id}_B.}
\]

This preserves correlations with the exterior and is stronger than preserving local marginals.

**QLOC-02.** If the contextual operator system on \(A\) has dimension \(r\) and the carrier Hilbert space has dimension \(k\),

\[
\boxed{r\le k^2.}
\]

**QLOC-03.** Bounded-range finite-depth circuits give an exact task light-cone collar carrier.

**QLOC-04.** Under a Lieb–Robinson-type bound, a collar of radius

\[
\boxed{r\ge vH+\mu^{-1}\log(C/\varepsilon)}
\]

is an \(\varepsilon\)-sufficient quantum carrier.

**QLOC-05.** Locality first restricts to the light-cone collar; BM semantic reduction can then compress inside the collar according to the actual task operator system.

Permanent firewall:

\[
\boxed{\text{entanglement entropy}\not\equiv\text{BM quantum semantic width}.}
\]

## 8. Task-relative QEC and distributed quantum cuts

A surviving route set is authorized when there exists a CPTP recovery fixing the required logical operator system/algebra.

**QDIST-01.** Full QEC is only the special case \(\mathcal S_L=\mathcal B(\mathcal H_L)\).

**QDIST-02.** Exact algebra correction obeys the OAQEC commutant criterion

\[
\boxed{PE_a^\dagger E_bP\in(V\mathcal A_LV^\dagger)'.}
\]

**QDIST-03.** Exact finite-dimensional task recovery for a fixed operator-system Passport is SDP feasibility in the recovery Choi matrix.

**QDIST-04.** Quantum erasure-cut dimension bounds are necessary but not sufficient because no-cloning can forbid capacity-feasible layouts.

**QDIST-05.** Same hardware can be unrecoverable as a full quantum state but exactly recoverable for a smaller classical observable algebra.

## 9. No-broadcasting and access geometry

**QBCAST-01.** If two disjoint regions each exactly recover the same finite-dimensional task algebra, that algebra must be commutative.

Therefore noncommutative task access structures are intersecting hypergraphs.

**QBCAST-03.** Symmetric quantum threshold structures require

\[
\boxed{2k>m.}
\]

**QBCAST-04.** Fixed-size minimal authorized sets obey classical Erdős–Ko–Rado bounds when applicable.

**QBCAST-05.** Task erasure distance equals the transversal number of the minimal authorized-set hypergraph:

\[
\boxed{d_{\mathcal A}=\tau(\operatorname{MinAuth}(\mathcal A)).}
\]

**QBCAST-06.** Failures can leave different commutative “classical shadows” of an originally noncommutative task.

## 10. Greatest recoverable task algebra and exact graceful degradation

For compressed error algebra

\[
\mathfrak E_{\mathcal N}=C^*(PE_a^\dagger E_bP),
\]

define

\[
\boxed{\mathfrak A_{\max}(\mathcal N)=\mathfrak E_{\mathcal N}'.}
\]

**QDEG-01.** A logical algebra \(\mathcal A\) is exactly recoverable iff

\[
\boxed{\mathcal A\subseteq\mathfrak A_{\max}(\mathcal N).}
\]

**QDEG-02.** More failure yields a smaller greatest recoverable algebra:

\[
F_1\subseteq F_2\Longrightarrow
\boxed{\mathfrak A_{\max}(F_2)\subseteq\mathfrak A_{\max}(F_1).}
\]

**QDEG-03.** Canonical strongest surviving sub-Passport:

\[
\boxed{\mathcal A_{\rm surv}(F)=\mathcal A_{\rm req}\cap\mathfrak A_{\max}(F).}
\]

This is technical capability, not permission to weaken the external contract.

**QDEG-04.** Robust exact Passport algebra for failure family \(\mathfrak F\):

\[
\boxed{\mathfrak A_{\rm robust}(\mathfrak F)=\bigcap_{F\in\mathfrak F}\mathfrak A_{\max}(F).}
\]

**QDEG-05.** Exact recoverable algebra Passports form a lattice under intersection and generated algebra.

**QDEG-06.** The quantum-to-classical degradation boundary occurs when the greatest recoverable finite-dimensional algebra becomes commutative.

**QDEG-07.** Exact repair succeeds iff

\[
\boxed{\mathfrak E^{\rm repaired}\subseteq\mathcal A_{\rm req}'.}
\]

## 11. Approximate algebraic degradation — newest result

Let the compressed error operator system be

\[
\mathcal K_{\mathcal N}=\operatorname{span}\{PE_a^\dagger E_bP\}.
\]

Define the normalized commutator defect

\[
\boxed{
\kappa_{\mathcal A}(\mathcal N)=
\sup_{\substack{Z\in\mathcal K_{\mathcal N},\|Z\|\le1\\X\in\mathcal A,\|X\|\le1}}
\|[Z,X]\|.
}
\]

Define distance-to-commutant defect

\[
\boxed{
\eta_{\mathcal A}(\mathcal N)=
\sup_{\substack{Z\in\mathcal K_{\mathcal N}\\\|Z\|\le1}}
\operatorname{dist}(Z,\mathcal A').
}
\]

**QAPP-01 — Commutator/Commutant Equivalence Bound.** In finite dimension,

\[
\boxed{\eta_{\mathcal A}\le\kappa_{\mathcal A}\le2\eta_{\mathcal A}.}
\]

The first inequality follows by Haar averaging over the unitary group of \(\mathcal A\), producing the norm-one conditional expectation onto \(\mathcal A'\). The second follows from replacing \(Z\) by its nearest commutant element.

At zero defect,

\[
\boxed{\kappa_{\mathcal A}=0\iff\eta_{\mathcal A}=0\iff\mathcal A\text{ is exactly correctable}.}
\]

**QAPP-02 — Physical Task-Recovery Defect.** Define

\[
\boxed{
\delta_{\mathcal A}(\mathcal N)=
\inf_{\mathcal R\,\mathrm{CPTP}}
\sup_{\substack{X\in\mathcal A\\\|X\|\le1}}
\left\|X-\mathcal E^\dagger\mathcal N^\dagger\mathcal R^\dagger(X)\right\|.
}
\]

Then \(\delta_{\mathcal A}=0\) iff the algebra is exactly correctable.

The algebraic defects \(\kappa,\eta\) and physical defect \(\delta\) must remain separate. No universal dimension-free quantitative implication \(\kappa\ll1\Rightarrow\delta\ll1\) is claimed without a specific approximate-QEC stability theorem or conditioning hypothesis.

**QAPP-03 — Diamond Stability.** For fixed encoding and task algebra,

\[
\boxed{
|\delta_{\mathcal A}(\mathcal N)-\delta_{\mathcal A}(\mathcal M)|
\le\|\mathcal N-\mathcal M\|_\diamond.
}
\]

Thus physical recovery margin gives a certified channel-perturbation reserve.

**QAPP-04 — Approximate Capability Down-Set.** Define

\[
\boxed{\mathfrak C_\varepsilon(\mathcal N)=\{\mathcal A:\delta_{\mathcal A}(\mathcal N)\le\varepsilon\}.}
\]

If \(\mathcal B\subseteq\mathcal A\) and \(\mathcal A\in\mathfrak C_\varepsilon\), then \(\mathcal B\in\mathfrak C_\varepsilon\). Positive-tolerance capability is downward closed.

Unlike the exact sector, there is no general reason for one unique greatest approximate algebra; incompatible approximate decoders can produce incomparable maximal capabilities.

**QAPP-05 — Passport Survival Threshold.** Define

\[
\boxed{\varepsilon_*(\mathcal A;\mathcal N)=\delta_{\mathcal A}(\mathcal N).}
\]

Then task weakening is monotone:

\[
\mathcal B\subseteq\mathcal A
\Longrightarrow
\boxed{\varepsilon_*(\mathcal B;\mathcal N)\le\varepsilon_*(\mathcal A;\mathcal N).}
\]

For failure family \(\mathfrak F\),

\[
\boxed{\varepsilon_*^{\mathfrak F}(\mathcal A)=\max_{F\in\mathfrak F}\delta_{\mathcal A}(\mathcal N_F).}
\]

**QAPP-06 — Approximate Repair Cost.** For intervention \(u\) producing channel \(\mathcal N_u\) at cost \(c(u)\),

\[
\boxed{
J_{\mathcal A}^{\rm repair}(\varepsilon)
=
\inf\{c(u):\delta_{\mathcal A}(\mathcal N_u)\le\varepsilon\}.
}
\]

**QAPP-07 — Exact-to-Approximate Degradation Firewall.** Exact algebraic recovery has a canonical greatest object \(\mathfrak A_{\max}\). Positive-tolerance recovery may instead be Pareto-valued over incomparable approximate algebras and decoders.

Example: for single-qubit dephasing

\[
\mathcal N_p(\rho)=(1-p)\rho+pZ\rho Z,
\]

\(C^*(Z)\) is preserved exactly for every \(p\), while \(X/Y\)-type capability is degraded for \(0<p<1\). Identity recovery gives

\[
\|\mathcal N_p^\dagger(X)-X\|=2p.
\]

## 12. Consolidated firewalls

The logged development preserves the following distinctions:

\[
\boxed{\text{finite approximate width}\not\Rightarrow\text{finite native dimension};}
\]
\[
\boxed{\text{small semantic width}\not\Rightarrow\text{easy interface discovery};}
\]
\[
\boxed{\text{task-irrelevant}\not\Rightarrow\text{coupling-irrelevant};}
\]
\[
\boxed{\text{multiple routes}\not\Rightarrow\text{multiple semantic distinctions};}
\]
\[
\boxed{\text{enough network capacity}\not\Rightarrow\text{distributed realizability};}
\]
\[
\boxed{\text{weak coupling}\not\Rightarrow\text{small exact semantic change};}
\]
\[
\boxed{\text{local dynamics}\not\Rightarrow\text{semantic area law};}
\]
\[
\boxed{\text{entanglement entropy}\not\equiv\text{quantum semantic width};}
\]
\[
\boxed{\text{classical route duplication}\not\Rightarrow\text{quantum cloning};}
\]
\[
\boxed{\text{capacity-feasible quantum routing}\not\Rightarrow\text{code realizability};}
\]
\[
\boxed{\text{recoverable weaker Passport}\not\Rightarrow\text{contractually acceptable weakening};}
\]
\[
\boxed{\text{small algebraic commutator defect}\not\Rightarrow\text{a universal physical recovery bound}.}
\]

## 13. Current unified synthesis

Across finite systems, PDEs, causal systems, networks, many-body systems and quantum systems, the same typed pattern now appears:

\[
\boxed{
\text{Native system}
\to
\text{lawful contexts/futures}
\to
\text{receiver Passport}
\to
\text{contextual response profile}
\to
\text{minimal exact/approximate carrier}
\to
\text{physical realization}
\to
\text{robustness/repair}.
}
\]

The current Volume II principle is therefore:

\[
\boxed{
\textbf{Retain exactly those distinctions that can still alter a declared lawful receiver response, in a carrier type capable of preserving the native structure required by the task.}
}
\]

## 14. Immediate next targets

The next hard targets are: obtain a rigorous dimension-aware approximate-QEC stability theorem relating \(\kappa_{\mathcal A}\) or \(\eta_{\mathcal A}\) to \(\delta_{\mathcal A}\) under explicit hypotheses; characterize the Pareto geometry of incomparable approximately recoverable algebras; compute failure-indexed exact and approximate algebra landscapes for concrete small quantum codes; and perform a dedicated prior-art scrub against OAQEC, approximate QEC, quantum secret sharing, Hankel/model reduction, port reduction, communication complexity, treewidth, metric entropy and Lieb–Robinson theory before any novelty claim.

---

**Canonical status of this file:** development log only. It does not replace or modify the frozen Version 1 foundation.
