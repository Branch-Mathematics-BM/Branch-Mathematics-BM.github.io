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
