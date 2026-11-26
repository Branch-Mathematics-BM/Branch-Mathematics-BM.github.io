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
