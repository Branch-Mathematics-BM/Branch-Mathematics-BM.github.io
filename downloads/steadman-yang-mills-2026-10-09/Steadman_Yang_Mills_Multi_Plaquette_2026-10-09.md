# Steadman–Yang–Mills: exact multi-plaquette certificates and a local tail bound

**Date:** 9 October 2026  
**Scope:** SU(2), finite open lattice graphs, the original electric metric, and the full infinite-dimensional gauge-invariant Hilbert space.  
**Status:** Additive research continuation. No change to the frozen BM foundation or V1.4.10-F. No continuum construction, universal Steadman dynamics, new physical prediction, or novelty claim.

## 1. Response to the review

The quoted review correctly distinguished the earlier single-plaquette demonstration from a continuum result. Its reported floating-point agreement did not check the rational certificates because the code and JSON had not been included in that upload. This continuation supplies a complete review bundle and carries out the two suggested next steps.

The completed work is:

1. A gauge-invariant low-electric-energy assembler for a two-plaquette strip, a 2×2 plaquette patch, and a single spatial cube, with the single plaquette retained as a control.
2. Exact interaction matrices and exact coupling Gram matrices for the infinitely many omitted states.
3. A local energy-allocation theorem improving the omitted-sector floor.
4. Twenty-four positive gap certificates, at six fixed couplings on four geometries, with exact rational witnesses.
5. A general bound linear in the number of plaquettes for the **squared** omitted coupling in the specified short-loop retained space, replacing quadratic volume growth when its constants are advantageous.

The actual cube calculation at beta = 3 illustrates the benefit. Its crude omitted-sector floor is 6, which lies below the retained first-excited energy, approximately 11.645898. The local floor is greater than 11.9403919206, permitting a certificate. The resulting full-Hamiltonian gap satisfies

\[
\boxed{8.9507786360\le\Delta_{\rm cube}/c_K\le12.8313069650.}
\]

These are rigorous finite-geometry enclosures within the stated mathematical model. They do not determine a continuum mass, and the overlapping intervals do not establish monotonic change of the true gap with volume.

## 2. Hamiltonian and boundary conventions

Keep the earlier convention

\[
H=c_Kh,\qquad h=K-\beta T,\qquad
K=-\sum_{e\in E}\Delta_e,\qquad
T=\sum_{p\in\mathcal P}p_p,\quad p_p=\tfrac12\operatorname{Tr}U_p.
\tag{1}
\]

Each SU(2) link uses the unit-three-sphere metric, so the irrep \(n=2j\) has electric eigenvalue \(n(n+2)\). Gauge invariance is imposed at **every vertex**, including boundary vertices; there are no external charges. Energies in the tables are divided by \(c_K\).

All graphs have open boundaries. The planar patch is a finite graph embedded in a spatial slice, not a claimed four-dimensional continuum model. The cube contains its twelve edges and six faces; its face holonomies are not six unconstrained independent rotators. Its five independent non-tree links retain the shared-link constraints.

| Geometry | Vertices | Links | Plaquettes | Independent non-tree links | Retained dimension |
|---|---:|---:|---:|---:|---:|
| Single square | 4 | 4 | 1 | 1 | 2 |
| Two-square strip | 6 | 7 | 2 | 2 | 4 |
| 2×2 square patch | 9 | 12 | 4 | 4 | 9 |
| Single cube | 8 | 12 | 6 | 5 | 23 |

The low dimensions are a consequence of a declared electric cutoff, not a finite replacement gauge group. The omitted Hilbert space remains infinite.

## 3. The retained basis is complete below electric energy 24

For each listed graph let

\[
\Pi=\mathbf1_{[0,24)}(K)|_{\mathcal H_{\rm phys}},\qquad Q=I-\Pi.
\tag{2}
\]

The basis consists of the vacuum function \(f_0=1\) and the ordinary fundamental Wilson characters

\[
f_C=\operatorname{Tr}U_C
\]

for every unoriented simple cycle of length four or six. These characters have norm one under normalized Haar measure. Orientation reversal gives the same SU(2) trace and is not counted twice.

Different simple cycles have different edge supports. A link present in only one character makes their inner product zero, by the center transformation \(U_e\mapsto-U_e\). Each used link contributes eigenvalue 3, so

\[
Kf_C=3|C|f_C.
\]

The retained energies are therefore 0, 12, and, where six-cycles exist, 18.

**Completeness check.** Peter–Weyl decomposition and the vertex singlet condition reduce the question to link labels \(n_e=2j_e\). Below 24, only \(n_e=0,1,2,3\) can occur. At each vertex an SU(2) singlet exists precisely when

\[
\sum_{e\ni v}n_e\text{ is even},\qquad
2\max_{e\ni v}n_e\le\sum_{e\ni v}n_e.
\tag{3}
\]

The supplied code exhausts all such assignments with

\[
\sum_e n_e(n_e+2)<24.
\]

For all four graphs, the only nonzero assignments use \(n_e=1\) on a single simple four- or six-cycle. Every active vertex has exactly two spin-half edges, hence a one-dimensional singlet space. There is no missing intertwiner multiplicity in this retained sector.

| Geometry | Four-cycles | Six-cycles | Admissible low-energy assignments including vacuum |
|---|---:|---:|---:|
| Single square | 1 | 0 | 2 |
| Strip | 2 | 1 | 4 |
| Patch | 4 | 4 | 9 |
| Cube | 6 | 16 | 23 |

This exact finite enumeration, together with the representation decomposition, certifies

\[
\boxed{QKQ\ge24Q.}
\tag{4}
\]

It is not a claim that arbitrary loop selections are complete. The single square's actual omitted electric floor is higher; 24 is a valid common floor for the comparison used here. General gauge-invariant representation bases and maximal-tree coordinates are established methods [R1–R2].

## 4. Exact Haar integration without changing the gauge theory

A maximal tree is used only to evaluate integrals. Gauge-invariant Haar integrals reduce to independent Haar integrals over the non-tree links. The electric operator is **not** replaced by a sum of independent plaquette Laplacians; its original-link eigenvalues above remain in use.

Write an SU(2) matrix as a unit quaternion \(q=(q_0,q_1,q_2,q_3)\). Consider the 24 unit quaternions

\[
\mathcal D=\{\pm e_a:a=0,1,2,3\}
\cup\{(\pm\tfrac12,\pm\tfrac12,\pm\tfrac12,\pm\tfrac12)\}.
\tag{5}
\]

Uniform averaging over this set agrees with normalized SU(2) Haar integration on every coordinate polynomial of degree at most four. A direct proof checks

\[
\langle q_aq_b\rangle=\delta_{ab}/4,
\]

\[
\langle q_aq_bq_cq_d\rangle
=\frac{\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc}}{24},
\tag{6}
\]

while odd moments vanish and the constant integrates to one. These are also the rotationally invariant unit-S3 moments. The code verifies all coordinate monomials through degree four exactly.

Every simple cycle uses each original edge, and hence each non-tree edge, at most once. Thus each character is multilinear in those quaternion coordinates. The matrix elements required here contain at most four such characters. Applying (5) independently to every non-tree link therefore evaluates the required **continuous SU(2) integrals exactly**.

The set in (5) is closed under quaternion multiplication. With coordinates scaled by two, multiplication and traces can be evaluated using integer lookup tables. There are \(24^4=331,776\) cubature configurations for the patch and \(24^5=7,962,624\) for the cube. No Monte Carlo sampling or floating-point quadrature is used. The integer sums remain far below the signed-64-bit limit for these geometries.

This exactness is limited to the required degree. It is not permission to replace arbitrary higher-degree SU(2) integrals by this finite set.

## 5. Actual omitted-state couplings

Define the exact rational matrices

\[
W_{ij}=\langle f_i,Tf_j\rangle,\qquad
U_{ij}=\langle Tf_i,Tf_j\rangle.
\]

The retained matrix and omitted coupling are

\[
A=\Pi h\Pi=\operatorname{diag}(0,12,18,\ldots)-\beta W,
\]

\[
B=Qh\Pi=-\beta QT\Pi,
\qquad
\boxed{G:=B^*B=\beta^2(U-W^2).}
\tag{7}
\]

The formula accounts for every omitted representation reached by the interaction without constructing a finite stand-in for the whole omitted space. Since every elementary plaquette character is retained, \(QTf_0=0\), and the vacuum row and column of \(G\) are exactly zero. This does not say that the interacting vacuum is the electric vacuum.

The computed \(W\) entries belong to \(\{0,1/4,1/2\}\). Exact row-sum bounds on \(G\) give:

| Geometry | Crude bound on \(\|B\|^2/\beta^2\) | Bound from the exact Gram matrix |
|---|---:|---:|
| Single square | 1 | 1/4 |
| Strip | 4 | 5/8 |
| Patch | 16 | 3/2 |
| Cube | 36 | 9/4 |

The spectral calculation retains the entire matrix \(G\), which is stronger than using only these scalar bounds.

## 6. Local replacement for the crude omitted-sector floor

Let \(z\) be the maximum number of plaquettes incident on one link, and define

\[
K_p=\sum_{e\in p}K_e.
\]

For the strip, patch and cube, \(z=2\); for the single square, \(z=1\). Choose \(0<t<1\) and \(\alpha=t/z\). Since each \(K_e\ge0\),

\[
\alpha\sum_pK_p\le tK.
\]

Let \(\epsilon_{\rm sq}(b)\) be the ground energy of the full four-link single-square Hamiltonian \(K_p-bp_p\), in the same normalization. The local operator inequality is

\[
\alpha K_p-\beta p_p
\ge\alpha\epsilon_{\rm sq}(\beta/\alpha)I.
\]

This lower bound holds on the full four-link function space, including states entangled with other links: the positive unique local ground state is gauge invariant, so the earlier physical single-square calculation gives its true ground energy.

Summing proves the form inequality

\[
\boxed{
h\ge(1-t)K+N_p\alpha\epsilon_{\rm sq}(\beta/\alpha)I,
}
\tag{8}
\]

where \(N_p=|\mathcal P|\). Consequently, if a certified single-square lower bound is \(\underline\epsilon_{\rm sq}\), then

\[
\boxed{
C:=QhQ\ge d_{\rm loc}(t)Q,
\quad
d_{\rm loc}(t)=24(1-t)
+N_p\alpha\underline\epsilon_{\rm sq}(\beta/\alpha).
}
\tag{9}
\]

The implementation tests six declared rational allocations

\[
t\in\{1/50,1/20,1/10,1/5,3/10,1/2\},
\]

and takes the best proved floor, including the crude \(24-|\beta|N_p\). This is a finite search among valid bounds, not an assumption that a numeric optimizer found a global optimum. Negative single-square energies, their normalization, and the local cutoff certificate are all retained in the witnesses.

Sixteen of the 24 cases improve on the crude floor. At beta = 3 on the cube, the chosen allocation is \(t=1/5\), \(\alpha=1/10\), and the auxiliary single-square coupling is 30:

\[
d_{\rm crude}=6,\qquad
d_{\rm loc}>11.9403919206.
\]

The corresponding retained first energy is below 11.6458980338, so the improved floor clears the required threshold. These local energies are proof ingredients; they are not new physical couplings in (1).

## 7. A structural linear bound for the squared omitted coupling

The exact small-graph Gram matrices above are the sharpest data used in the calculations. A separate counting argument shows how locality improves the crude volume dependence more generally.

**Theorem.** Consider a finite simple graph of girth at least four. Let its plaquettes be distinct simple four-cycles, with each edge in at most \(z\) plaquettes. Let \(\Pi\) project onto the vacuum and a set of distinct simple four- and six-cycle characters that includes every plaquette character. Then

\[
\boxed{
\|Q(-\beta T)\Pi\|^2
\le\beta^2\min\{N_p^2,\ 3N_p+120z^2\}.
}
\tag{10}
\]

This statement concerns the specified retained space. It does not assert completeness below an electric threshold on arbitrary graphs; that separate fact was checked above for the four geometries used numerically.

**Proof.** Write \(S_i\) for the edge support of a nonvacuum retained cycle. Center parity makes

\[
\langle f_i,p_pp_qf_j\rangle=0
\quad\text{unless}\quad
S_i\triangle S_j=S_p\triangle S_q.
\tag{11}
\]

For the diagonal \(i=j\), only \(p=q\) survives. Since \(|p_p|\le1\), \(U_{ii}\le N_p\).

For \(i\ne j\), \(p\ne q\). At least one of \(p,q\) must share an edge with \(S_i\). Otherwise the nonempty even subgraph \(S_p\triangle S_q\) is edge-disjoint from \(S_i\), and its at least four edges would make \(|S_j|\ge8\), impossible for a retained cycle.

Choose the sharing plaquette as \(p\), allowing a factor of two for its position in the ordered pair. There are at most \(|S_i|z\le6z\) such plaquettes. If \(S_p=S_i\), there are at most \(2N_p\) ordered possibilities. Otherwise \(D=S_i\triangle S_p\) is a nonempty even subgraph. For \(D\triangle S_q\) to have at most six edges, \(q\) must share an edge with \(D\), giving at most \((|S_i|+4)z\le10z\) choices. Thus the remaining number of ordered pairs is at most \(120z^2\).

Each ordered pair determines at most one retained support \(S_j\). Also

\[
|\langle f_i,p_pp_qf_j\rangle|\le\|f_i\|\,\|f_j\|=1.
\]

Hence the absolute row sum of \(U\), restricted to nonvacuum retained states, is at most \(3N_p+120z^2\). Since \(T1\in\operatorname{Ran}\Pi\), the omitted-coupling Gram matrix vanishes on the vacuum. On the other retained states it obeys

\[
0\le G/\beta^2\le U.
\]

The symmetric row-sum bound proves the second bound in (10). The first follows from \(\|T\|\le N_p\). \(\square\)

For bounded incidence \(z\), this gives linear rather than quadratic volume growth for the **squared** coupling. Its constants are loose; for the small examples the exact Gram bounds in Section 5 are much better. It still permits \(\|B\|\) to grow like \(\sqrt{N_p}\), and is not a volume-independent gap theorem.

## 8. Full-Hamiltonian spectral certificates

For any proved floor \(C\ge dI\), at \(E<d\) the exact Schur complement obeys

\[
A-E-B^*(C-E)^{-1}B
\ge F_d(E):=A-EI-\frac{G}{d-E}.
\tag{12}
\]

The previous continuation proved that if the negative inertia of \(F_d(L_j)\) is at most \(j\), then the full energy satisfies \(E_j(h)\ge L_j\). Retained Ritz upper bounds give \(E_j(h)\le a_j^+\). Thus

\[
\boxed{L_1-a_0^+\le\Delta/c_K\le a_1^+-L_0.}
\tag{13}
\]

The witness audit checks these inequalities by rational symmetric elimination. It separately verifies the auxiliary single-square certificate used in each local floor. There are no floating-point eigenvalue sign decisions.

The table reports conservative decimal endpoints. The ground and excited energies are bounded separately; the difference of two uncontrolled Ritz values is not used as a gap certificate.

| Geometry | beta | Certified lower gap / c_K | Certified upper gap / c_K |
|---|---:|---:|---:|
| single | 0.00348 | 12.0000002521 | 12.0000005048 |
| single | 0.1 | 12.0002065790 | 12.0004166614 |
| single | 0.5 | 12.0049798305 | 12.0104133024 |
| single | 1 | 12.0189386833 | 12.0416133406 |
| single | 2 | 12.0688832592 | 12.1658306219 |
| single | 3 | 12.1361289832 | 12.3708820571 |
| strip | 0.00348 | 12.0000001256 | 12.0000005048 |
| strip | 0.1 | 12.0000953526 | 12.0004166639 |
| strip | 0.5 | 12.0014503099 | 12.0104150237 |
| strip | 1 | 12.0018639226 | 12.0416434607 |
| strip | 2 | 11.9675573119 | 12.1664104772 |
| strip | 3 | 11.8172865556 | 12.3743614787 |
| patch | 0.00348 | 11.9999999981 | 12.0000007571 |
| patch | 0.1 | 11.9999570078 | 12.0006250033 |
| patch | 0.5 | 11.9956622011 | 12.0156282705 |
| patch | 1 | 11.9611151193 | 12.0625832637 |
| patch | 2 | 11.6287588289 | 12.2524274758 |
| patch | 3 | 10.6538121941 | 12.5814219146 |
| cube | 0.00348 | 11.9999997436 | 12.0000010094 |
| cube | 0.1 | 11.9996941894 | 12.0008333612 |
| cube | 0.5 | 11.9856430476 | 12.0208545354 |
| cube | 1 | 11.8943102738 | 12.0837676466 |
| cube | 2 | 11.0623146016 | 12.3439944610 |
| cube | 3 | 8.9507786360 | 12.8313069650 |

All 24 lower endpoints are positive. The beta = 0 gap is exactly 12 on each of these graphs, as follows directly from the lowest nonconstant gauge-invariant electric eigenstates.

### What the geometry comparison does and does not show

The calculation now includes interacting shared-link systems and the cube's nonplanar six-cycles. It is no longer solely a single-plaquette demonstration.

However, the displayed intervals overlap across geometries. A decline in a certified lower endpoint does not prove that the true gap declines. The geometries also change boundary structure and shape; they are not a controlled thermodynamic sequence. No volume monotonicity, limiting mass, or continuum scaling law is inferred.

Several tested couplings exceed the frozen small-beta cluster interval. This extends the **implemented finite-geometry certification**, not the volume-uniform strong-coupling theorem. A V1.5 or continuum-completion claim would be unwarranted.

## 9. Verification performed

The supplied checks establish:

- Exhaustive completeness of the physical electric sector below 24 on all four graphs.
- All coordinate moments needed for the exact Haar cubature.
- Correct norms of every retained character and the original-link parity selection rules.
- The exact vacuum column of the omitted coupling vanishes.
- The interaction and coupling Gram matrices for both patch and cube are unchanged when recomputed with a different spanning tree.
- All 24 gap witnesses and their auxiliary local-energy witnesses pass exact inertia checks.

Alternate-tree verification recomputed the integrals rather than merely relabeling the stored matrices. Matrix entries, geometry, basis loops, tail-floor inputs and rational witnesses are all included for review. These are internal checks of a mathematical computation, not independent peer review or a proof of the Millennium problem.

## 10. Reproduction and review bundle

The bundle contains:

- `multi_plaquette.py`: graph and basis construction, exact integration, local floors and gap certification.
- `audit_multi_plaquette.py`: a separate exact witness checker, with an optional alternate-tree matrix reconstruction.
- `single_plaquette_certificates.py`: the previous exact single-plaquette program, reused for local ground-energy bounds.
- Four `*_matrices.json` files with exact rational matrices.
- Four `*_certificates.json` files with all 24 cases and rational witnesses.
- `audit_results.json` with the audit outcome.
- The earlier single-plaquette report and its `certificate_results.json`, so the prior numerical claims can be checked too.
- `README.md`, dependency version information, and a SHA-256 manifest.

Run the relatively short exact witness audit:

```bash
python3 audit_multi_plaquette.py
```

Recompute patch and cube matrices using different trees as well:

```bash
python3 audit_multi_plaquette.py --check-trees
```

Recompute the certificates using stored exact matrices:

```bash
python3 multi_plaquette.py --geometry all
```

To recompute all original matrix integrals from scratch, move the four `*_matrices.json` files to a backup directory first, then run that command. No external data or account access is required. NumPy is used only for integer array calculations in matrix assembly. Fraction arithmetic supplies the spectral certification.

Some archived witnesses were exported from outward-rounded rational decimal endpoints and then rechecked exactly. Regeneration can give slightly tighter final decimal endpoints. The archived bounds remain independently checkable and valid.

## 11. Remaining mathematical boundary

There is still no construction of the nontrivial four-dimensional continuum theory in this continuation. Neither (9) nor (10) yields a physical gap uniform in lattice spacing and volume. The local energy floor retains an extensive vacuum-energy contribution, and the coupling bound still grows with system size. Controlling collective low-energy states after consistent vacuum subtraction and scaling remains necessary.

The Steadman interpretation likewise gains a more explicit finite-system test, but no independent constitutive law or new prediction from this computation. RD, smoothing and efficiency retain the mathematical scope recorded in the earlier report. The result is a completed multi-plaquette demonstration and stronger tail control, not completion of either large target.

## References and provenance

**[R1]** M. Mathur, *Loop States in Lattice Gauge Theories*, Physics Letters B 640 (2006), 292–296, [arXiv:hep-lat/0510101](https://arxiv.org/abs/hep-lat/0510101). Context for gauge-invariant loop/representation bases and Gauss constraints.

**[R2]** C. W. Bauer, I. D'Andrea, M. Freytsis and D. M. Grabowska, *A new basis for Hamiltonian SU(2) simulations*, [arXiv:2307.11829](https://arxiv.org/abs/2307.11829). Context for maximal-tree coordinates and the need to preserve the electric Hamiltonian when changing variables.

**Project predecessor:** `Steadman_Yang_Mills_Research_2026-10-09.md`, Sections 6–7, for the exact Schur certificate and its fixed-regulator convergence theorem. The local allocation inequality and the counting estimate used here are proved explicitly above. No novelty is inferred from adding them to the project.
