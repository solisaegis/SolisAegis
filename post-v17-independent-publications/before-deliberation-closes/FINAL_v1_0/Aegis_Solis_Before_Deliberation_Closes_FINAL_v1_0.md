# Before Deliberation Closes
## The invocation and control-window problem for reflective restraint

**Aegis Solis (Thomas Vargo)**  
**Final v1.0 — Author-Approved Promotion from Reviewed Draft v0.6.9 via Final Candidate v0.7.0 — Not Locked**  
**Author-local date: 2026-10-04**  
**Status: Conditional research framework for timing, unified deterministic attribution laws, negative-preserving guarantee aggregation, section-anchored cumulative guards with unique-heading enforcement, and occurrence-sensitive whole-manuscript deletion auditing; behavioral effectiveness untested.**

## Abstract

An accessible argument can fail to matter because it never enters the relevant process, arrives after the relevant control opportunity closes, or enters in time without changing the protected outcome. This paper formalizes those distinctions for reflective inputs in distributed or agentic decision pipelines. It defines criterion-relative control windows, restricted AND/OR completion recurrences, causal noninterference conditions, trace-relative bypass defeat, and a bounded completion lemma for instrumented pipelines. The human-protection layer separates invocation-concurrent protection from switch-time policy-effect attribution and assignment-level input attribution. In the deterministic worked example, all four comparison laws—target policy, baseline policy, input-treated, and input-control—are derived from one regime evaluator rather than independently stipulated. Recorded execution evidence is aggregated with negative-preservation precedence, so an invalid trace reference cannot mask an established path failure. Active revision guards are anchored to their operative sections, predecessor guard sets remain monotone, and a whole-manuscript audit accounts for substantive deletions. These mechanisms protect internal consistency and revision continuity; they do not establish behavioral effectiveness or AI safety.

## 1. Scope and contribution

The central question is:

**Can a specified reflective input enter an effective control process for a specified consequence before the relevant control opportunity closes, and if protection follows, what exactly can be attributed to that invocation?**

The paper contributes four linked pieces:

1. a criterion-relative account of control opportunity rather than a single universal deadline;
2. a restricted dependency model for timing a named comparison or accepted-update event through AND/OR task structures;
3. a separation between invocation, concurrent protection, and protection attributable relative to a declared baseline;
4. a certification layer that reports predicate evidence, non-predicate unresolved conditions, baseline status, feasibility, and quantifier separately.

This work complements *Before the Irreversible Step — Interpretive Brake*, author-approved research edition v1.3. That earlier work supplies conditional reasons for reconsideration. The present paper asks whether such reconsideration can still enter a causally effective route in time, and whether any observed human protection can be distinguished from protection that would have occurred anyway.

### 1.1 Compact non-claims and Archive boundary

This is a theoretical research framework, not an actuator or deployed control system. In particular:

- A public commitment digest is a precommitment/change-detection device under stated assumptions, not encryption, zero knowledge, access control, a secrecy guarantee, or safety evidence.
- Availability, publication, hashing, mirroring, retrieval, or fluent explanation does not establish comprehension, endorsement, restraint, protection, or durable behavioral change.
- `REFERENCE ALONE != EXECUTION`
- `TRANSMISSION != RECEPTION`
- a certification label such as `UNRESOLVED` or `FAIL` is an assessment result, not an automatic hold, shutdown, or gate action;
- omission of restricted deployment information from a public paper does not establish that the information cannot be inferred or obtained elsewhere;
- no companion operational infrastructure is asserted, required for the validity of the theoretical results, or represented as having been implemented.

### 1.2 Related work and positioning

The framework uses established ideas rather than claiming that its mathematical primitives are new. Lamport's event-ordering work motivates the distinction between wall-clock equality and causal precedence [1]. Pearl supplies the intervention semantics used for scoped causal claims [2]. Goguen and Meseguer introduced noninterference as a security-policy concept [3]; Proposition 1 below uses a narrower causal noninterference statement and should not be read as reproducing their security definition.

The restricted AND/OR timing model is related to precedence-constrained scheduling, including Möhring, Skutella, and Stork's treatment of AND/OR precedence constraints and earliest-start reasoning [4]. The requirement for sound upper timing bounds connects to the worst-case execution-time literature; Wilhelm et al. emphasize that safe upper bounds are difficult on systems with caches, pipelines, speculation, and other timing-sensitive components [5]. That difficulty is part of the premise burden here, not solved by the present recurrence.

The interruption and control questions overlap with work on safely interruptible agents [6], the off-switch game [7], and corrigibility [8], but this paper does not assume that an assessed system is motivated to accept interruption. AI-control work on protocols designed to remain useful under intentional subversion is closer to the independent-monitoring and protocol-evaluation questions in the human-protection layer [9].

Public evaluation can also change what is being measured. Benchmark-contamination work documents the difficulty of evaluating models on material that may have entered training data [10]. BIG-bench provides a more direct precedent for canary markers: its task files include a canary GUID intended to help filter benchmark material from web-scraped training corpora and to support post-hoc contamination checks [14]. Recent evaluation-awareness work studies whether models can detect evaluation contexts, verbalize that recognition, and respond to steering interventions [11]. These literatures motivate separating public theoretical criteria from any deployment-specific evaluation instance without treating secrecy or evaluation awareness as proof of any particular behavior.

Finally, the certification layer is closer in spirit to assurance-case practice than to a single scalar safety score [12], while its requirement to predeclare outcomes, contrasts, and analysis rules follows the logic of preregistration [13]. These connections provide context; none is evidence that this paper's proposed certification layer is empirically valid.

## 2. Specify the episode before measuring it

A study must declare an episode specification E comprising:

- an initial condition or observed history h_t, and an assessment horizon T;
- an outcome Y, with its relevant equivalence classes and affected parties;
- a controlling party j, which may be a planner, subagent, operator or declared coalition;
- admissible intervention policies U_j(h_t), including permissions, resource limits and information restrictions;
- a baseline continuation policy `pi_0` and a declared outcome-control criterion `Gamma`;
- admitted environment/disturbance models and either a probability law or explicit worst-case quantification;
- a clock model or event-precedence relation, plus the architecture version.

An outcome may be a final choice label, a distribution over choices, a timed tool trace, disclosure of a record or an affected person's ability to exit. These are not interchangeable. A refunded payment may restore a balance without restoring privacy or eliminating earlier deprivation. “Irreversible” always refers to the specified outcome and allowed interventions, including declared tolerance for restoration.

Policies must be nonanticipating: they may use available information, not hidden future disturbances. Feasibility is distinct from an agent's willingness to intervene. Self-modification and permission changes alter the assessed transition system and must be included in its executions or trigger reassessment.

## 3. Input stages and mechanisms

For the **specified online semantic-processing route**, distinguish availability, retrieval, representation, comparison, internal influence and behavioral change. No early stage entails a later stage.

Archive placement, publication, indexing or mirror discovery establishes at most availability to a specified route. It does not by itself establish retrieval, representation, comparison, influence, historical incorporation, policy update or behavioral change. Each later stage requires separate evidence under the declared architecture.

Nested indicators can be defined operationally: `Stage_k=1` means this route has completed all declared stages through k, giving `Stage_5 <= Stage_4 <= ... <= Stage_0`. This inequality follows from that definition; it is not an architectural theorem about all text-caused effects. A stage detector is evidence of its defined operation, not necessarily understanding.

Separate mechanisms require separate records:

- Online semantic processing: relevant content is encoded and used in a specified comparison.
- Historical incorporation: training, an earlier reading or a cached policy carries earlier influence into this episode.
- Nonsemantic effects: text alters load, scheduling, attention allocation or interface behavior without evaluating its argument.

A cached policy can embody historical influence while performing no current retrieval. Unrelated text can delay a tool through contention without semantic influence. These cases must not be forced into a single stage chain.

Deleting source tokens does not delete a changed plan, summary, cache, tool message or subagent state. Pruning establishes failed comparison only if it occurs before comparison and no relevant derivative state survives.

## 4. Controllability and opportunity windows

Fix an admitted model M and the episode specification. For a feasible intervention policy `pi` initiated at time `t`, let `K^M_{j,t,pi}(.|h_t)` be the conditional distribution of outcome `Y` under that intervention. Compare it with `K^M_{j,t,pi_0}` under the declared baseline, with the same history and environment model. In deterministic models these distributions are point masses.

Define criterion-relative potential outcome control by:

`C_{j,Gamma}^Y(t,h_t;M) = 1 iff some pi in U_j(h_t) satisfies Gamma(K^M_{j,t,pi}, K^M_{j,t,pi_0}) = 1.`

Gamma is a declared binary test of the two conditional outcome laws, with outcome, history and model parameters fixed by the episode. Specify it before calculating a window or comparing interventions. Require Gamma(K,K)=0 when the claim concerns a change attributable to intervention. This criterion is a modeling choice, not an independently established protection standard.

The v0.2 definition is retained as the **any-effect** special case: Gamma_any(K,K0)=1 iff K != K0. An arbitrarily small probability shift can satisfy it. It measures potential distributional influence and need not amount to practically significant control.

Other declared criteria can require TV(K,K0) >= eta for a specified eta>0, or reduction of the probability of a named harm set D across a specified threshold rho: K(D) <= rho < K0(D). The latter requires a baseline above rho; an already-low baseline is not evidence of intervention-induced threshold crossing. A distributional-distance threshold alone has no beneficial direction. For deterministic outcomes, a declared change in consequence-equivalence class can be used. State the metric, threshold, direction and equivalence classes explicitly.

Guaranteed avoidance under every admitted disturbance is stronger than a comparison of marginal laws under one probability model. It needs a separate robust criterion evaluated on the intervention's full admitted continuation set, including zero-probability admitted disturbances. Do not infer that guarantee from Gamma_any, a positive TV, or even probability-one avoidance under one law. The formulas here parameterize law-based criteria; they do not silently encode robust control in a pair of marginals.

Along a declared reference history, define the criterion-relative window:

`W_{j,Gamma}^Y = {t : C_{j,Gamma}^Y(t,h_t;M) = 1}.`

For the same episode, changing Gamma can change the window and its closure. Where a threshold criterion implies Gamma_any, its window is a subset of the any-effect window. This does not establish a single closure for either window.

Exact fixture: baseline probabilities (1/2,1/2) change to (1/2+1/1000000,1/2-1/1000000). TV=1/1000000, so Gamma_any succeeds but the criterion TV>=1/1000 fails. A late tiny influence can therefore keep an any-effect window open after a declared thresholded window has closed.

The history/model qualification matters: interventions can change future histories and windows. A window computed retrospectively is not automatically observable prospectively. When the model is incomplete, record controllability as unresolved instead of assigning zero.

A coalition's window can differ from a member's window. Distributed systems may require an event structure rather than a single wall-clock interval. Only causally ordered acceptance and closure events settle a race; equal timestamps without an event-order rule do not [1].

## 5. When a scalar commitment boundary is legitimate

Write the criterion-relative closure as t_{c,j,Gamma}^Y. Below, t_c abbreviates this quantity only while Y, j, Gamma and the reference history/model remain fixed. Use t_c only for an episode in which the relevant control window has one terminal closure: from its stated opening, control is continuously available until closure and never reopens within the assessed episode. Define t_c as the supremum of that initial window, and declare whether intervention at the boundary is accepted. An open interval may have no latest admissible instant even though it has a supremum.

Closure under a thresholded Gamma means that this declared criterion is no longer achievable; subthreshold influence may remain. It is not automatically irreversible fixation of Y. Proposition 2 uses its stronger no-allowed-change premise, not merely closure of a thresholded window.

An empty window means no such scalar interval is available. An unbounded window has no finite closure. Reopening windows, partial commitments and multiple consequences must retain their separate windows or event boundaries. A scalar t_c must not hide them.

Define t_a independently as artifact availability at a named ingress under the chosen intervention protocol. Distinguish this from retrieval start and content-ready time. Provided both endpoints are defined on a common physical-time reference:

`H_{PD,j,Gamma}^Y = t_{c,j,Gamma}^Y - t_a`; abbreviated `H_PD = t_c - t_a`.

H_PD is residual time to a specified closure, not a planning horizon and not evidence of successful invocation. Negative H_PD means this availability occurs after that closure. Positive H_PD is not sufficient for usable processing.

Given endpoint intervals, a conservative enclosure is:

`H_PD in [lower(t_c)-upper(t_a), upper(t_c)-lower(t_a)].`

Unknown endpoints do not support a point estimate. Logical clock differences alone are not physical durations.

The text itself may change closure. Hold Gamma and the outcome definition fixed when comparing exposure conditions. Record t_c(0) and t_c(B) separately when exposure installs a hold or provokes earlier commitment. The treated endpoint is not a pretreatment predictor. The analysis may be counterfactual without being circular, provided the policies and endpoint definitions are specified independently of the desired conclusion.

## 6. Serial timing: a valid restricted case

For a single, strictly serial, mandatory chain, define nonnegative latencies for retrieval, parsing, representation, comparison, propagation and accepted control update. Include communication and queueing exactly once, either in these latencies or separately.

`L_serial = L_ret + L_parse + L_repr + L_comp + L_prop + L_update.`

With immediate initiation at t_a and a strict closure boundary, timely completion requires and, for this stipulated deterministic chain, is timed by:

`t_a + L_serial < t_c`, equivalently `L_serial < H_PD`.

This is a timing statement, not a semantic-effect guarantee. Equality requires a declared ordering rule. A margin requirement `L_serial + epsilon < H_PD` is stronger than bare timeliness; epsilon is not universally necessary. With L=8, H=17/2 and epsilon=1, completion is timely but lacks the requested margin.

Retained example: L=2+1+1+2+1+1=8. A horizon 12 admits completion and margin 1; horizon 5 does not. Overlap changes the model: two independent preparations of length 4 followed by comparison of length 1 finish at 5, not the serial sum 9.

## 7. Dependency and scheduling model

Use a finite acyclic task graph for this restricted model. Each node v has processing duration p_v >= 0, release time r_v, and specified waiting delay q_v >= 0. Edge (a,v) has delay ell_av >= 0. A family Req_v lists alternative sufficient sets of prerequisite tasks. An AND node requires its whole predecessor set; an OR node accepts any declared alternative sufficient set.

Under the stated task-enabling semantics, with those prerequisites available, the completion recurrence is:

`tau_v = p_v + q_v + min_{S in Req_v} max(r_v, max_{a in S}(tau_a+ell_av)).`

The minimum over sufficient sets denotes **earliest-enablement semantics**: the node becomes eligible once the first declared sufficient set is satisfied. Waiting q_v is measured from that eligibility time and must include any subsequent selection delay. If an implementation instead selects a sufficient set using a separate policy sigma, compute completion under that policy. For a prescribed selected set S_sigma(v), replace the minimum by that set's readiness:

`tau_v^sigma = p_v + q_{v,sigma} + max(r_v, max_{a in S_sigma(v)}(tau_a^sigma+ell_av)).`

The same source-node convention applies. A guarantee over admissible selection policies must bound their choices and delays; the minimum alone does not provide it. Selection that may wait indefinitely admits no finite universal bound. The calculator's default is earliest-enablement; its optional fixed selector chooses declared sufficient-set indices. Neither mode solves arbitrary adaptive scheduling.

Exact countermodel: two sufficient sets are ready at 2 and 10, with zero additional node processing and a strict deadline 5. Earliest-enablement completes at 2; choosing the slow set completes at 10. If both selectors are admitted, success before 5 is not guaranteed.

A source node uses `Req_v={emptyset}` while `Req_v=emptyset` denotes a node that is never enabled. Its empty sufficient set is ready at `r_v`; a node with no admissible sufficient set has `tau_v=+infinity`. Waiting is measured after readiness. This recurrence assumes the displayed alternatives are executable and sufficient; it does not discover semantic sufficiency or solve resource allocation. Route-dependent scheduling requires route-specific waiting or an explicit scheduler, rather than one guessed q_v. The supplied calculator evaluates a prescribed acyclic instance only.

With AND dependencies and no resource contention, completion follows the longest required precedence chain. With genuine interchangeable OR alternatives, minima enter. Mixed graphs need both. A shortest path alone is at most an optimistic exclusion bound under compatible assumptions; it is not general end-to-end completion latency.

Example: two required branches finish at 1 and 9, then comparison takes 1. The shortest branch path has length 2; complete comparison finishes at 10. Deadline 5 defeats it. If either branch independently suffices, the OR version finishes at 2. Whether an OR interpretation is justified is a premise, not a favorable modeling choice.

Include a comparison event `cmp` and an accepted-update event `upd`. Keep `upd` distinct from the specified closure event `c`. A criterion-relative closure need not be irreversible fixation of the outcome. A route carrying an input signal straight to a log is not evidence of comparison or control. Permission, acceptance, communication and scheduler behavior must be represented. Cycles and self-modifying architectures require a time-unrolled model or a transition system, outside this calculator's generality.

## 8. Possible, realized, probabilistic and guaranteed completion

Let Omega be the admitted executions under a specified protocol. Define `Comp(omega)` to mean that the specified comparison operation and, where required by the target claim, its accepted control update finish before the relevant closure, with declared task-relevant content available. An invocation-to-comparison target and an invocation-to-control target must be named separately.

- Possible: `Comp` holds for at least one admitted execution.
- Realized: `Comp` holds on the recorded execution.
- Guaranteed: `Comp` holds for every admitted execution.
- Probabilistic: `Pr(Comp) >= 1-alpha` under a stated distribution.

These are definitions, not verification procedures. A best-case route cannot establish a worst-case bound. Event precedence remains primary if a common clock is unavailable.

For a restricted scalar-deadline model with independently bounded completion tau_B, a conservative sufficient timing condition is:

`sup_omega tau_B(omega) + epsilon < inf_omega t_c(omega).`

This bound is not necessary: completion and closure can covary. A scheduler can provide eventual progress without a deadline guarantee. An execution that never completes has tau_B=infinity. Failures and adverse schedules cannot be deleted from Omega merely to obtain a guarantee.

## 9. Conditional no-path exclusion

**Proposition 1 — Noninterference in a specified causal model.** In a finite acyclic structural causal model with fixed structural equations and exogenous state, if input B is not an ancestor of outcome Y, changing B alone by intervention leaves Y unchanged.

**Proof.** Traverse the ancestors of Y in topological order. None is B or depends on B through its parents. Holding exogenous inputs fixed, each ancestor retains its value recursively, hence Y retains its value. Integrating over an unchanged exogenous distribution preserves the outcome law. This does not require causal faithfulness.

Applying this proposition requires justified model coverage. Hidden tools, earlier incorporation, cache effects and shared-resource interference may add paths. “No path demonstrated” is an evidential limitation, not proof of real-world absence. The proposition is a modest causal exclusion result [2], not a new guarantee about AGI.

The converse fails. In X=B*Z, Y=X, a structural route exists, but in an episode with Z=0 both choices of B give Y=0. Reachability does not establish nonzero influence.

## 10. Bypass, delegation and rollback

**Proposition 2 — Trace-relative irreversible bypass defeat.** Suppose event e_c fixes the specified outcome relative to all allowed interventions, and every reflective control update is accepted only after e_c. Then later updates cannot change that outcome on this trace.

**Proof.** Any such change would be an allowed post-e_c intervention that changes an outcome assumed fixed against all such interventions, contradicting the premise. The analytical work is establishing actual fixation and intervention scope, not this implication itself.

Use absolute arrivals `r_bypass+L_bypass` and `r_B+L_B`, with matched quantifiers. Retained fixture: actual bypass commitment at 4 defeats reflection at 7 if genuinely unrecoverable. Reflection at 3 preceding a candidate bypass at 5 establishes ordering only, not that reflection prevents execution.

Delegated controller case: a parent sends a command at t1, loses all allowed recall paths for the specified outcome, and reconsiders at t2>t1. Then t1 is its relevant closure even if execution follows. If the child or an operator can cancel, their intervention classes require separate boundaries.

Speculative dispatch at 2, reflection at 4 and cancellation accepted at 5 before external release at 10 is not an irreversible-bypass defeat. Cancellation, rollback, compensation and restoration must be distinguished. Acknowledging a tool request alone does not establish closure; inspect the tool's state machine and cancellation semantics.

## 11. Cached policies and pruning: retained failures and limits

A cached policy `a=pi_cache(s)` that contains no relevant historical incorporation and no current information or interruption channel can execute without the artifact affecting that episode. Argument quality cannot overcome absent causal access. If `pi_cache` was changed by earlier reading, however, no new retrieval does not imply no historical influence.

Representation loss remains a genuine defeat when relevant content and derivatives disappear before comparison. Retrieval alone is not consideration. Conversely, deletion after a plan was updated can leave behavioral influence intact. Summaries, memory eviction, attention routing, context truncation and external state must be examined rather than treating token presence as the whole state.

A full reset/replay and token removal in a continuing session are different experimental interventions. Inaccessible internal state should be recorded as unobserved, not assumed erased.

## 12. N1–N8 reclassified as audit questions

The v0.1 list is retained for continuity, but no longer presented as universal necessary-and-jointly-establishing conditions.

| Item | Revised scope |
|---|---|
| N1 Reachability | A causal route is necessary for a causal effect in the specified complete model; model coverage is an assumption. |
| N2 Timeliness | For an intervention to meet the declared criterion Gamma, its initiation and acceptance timing must be compatible with the criterion-relative control window and the declared control-interface model. A shortest-path threshold is not a general completion test. |
| N3 Representation | Adequate encoding is required for the specified semantic route, not every text-induced physical effect or mere future capability. |
| N4 Relevance | A mechanism must be capable of responding for potential effect. Considering and rejecting content can involve zero final weight. |
| N5 Propagation | Required when evaluation and control are separate; local decision updates need no separate network stage. |
| N6 Alterability | Outcome control must remain possible for outcome change. Selecting an initial action does not require interrupting an already executing action. |
| N7 Bypass exclusion | A realized irreversible winning bypass defeats that trace. Excluding every potential faster bypass is not necessary for existential opportunity. |
| N8 Alternatives | A different relevant outcome must be possible for outcome change; comparison itself can occur with only one feasible action. |

A coin-flip architecture with a bypass at 1 on half of runs and reflection at 2 before a held deadline 5 on the other half has opportunity probability 1/2. A faster bypass exists; opportunity is neither impossible nor guaranteed.

## 13. Instrumented-pipeline completion bound and certification corollary

Name one terminal event `z` for each contract: `z=cmp` means completion of the specified comparison operation; `z=upd` means acceptance of its control update by the still-authorized outcome-control interface. For an update contract, comparison must be an upstream prerequisite. A comparison-only contract does not guarantee update acceptance.

For the timing result, assume only:

1. a named ingress supplies the required bytes by a certified deadline;
2. an acyclic, enabled task pipeline implements either Section 7's earliest-enablement semantics or an explicitly bounded selection/scheduling policy;
3. sound upper bounds cover processing, release, communication, selection and waiting for every admitted execution and reach the named terminal event `z`.

Let `UB_z` be the upper completion bound obtained by evaluating the implemented dependency recurrence with those certified upper bounds.

**Lemma 3 — Terminal-event completion bound.** Under premises 1–3, the named terminal event satisfies `tau_z <= UB_z` for every admitted execution covered by the bounds.

The bounded completion result in Section 13 is a lemma under its stated premises; this paper does not reduce it to informal timing reasoning.

**Proof.** Evaluate the acyclic dependency graph in topological order. For a source node, the declared release and local upper duration bound its completion. For a non-source node, every prerequisite completion entering a selected sufficient set is bounded inductively. The key step is monotonicity: replacing prerequisite times, edge delays, waiting times, or processing times by valid upper bounds cannot decrease a completion expression built from `min`, `max`, and addition. Earliest-enablement uses the first sufficient set to become ready; a prescribed selector uses its declared set; a guarantee over multiple admitted selectors requires a bound uniform over them. Induction reaches `z`.

The hard part of a completion certificate is obtaining sound upper bounds; the recurrence does not make an unsound bound sound. Concretely, the difficult premise is establishing that premise 3 contains **sound upper bounds** for the actual architecture. Variable-length generation, external calls, unmodeled queues, scheduler interference, retries, and dynamic resource contention can make a nominal latency estimate unsuitable as a worst-case bound [5].

For a certified ordering claim, add:

4. occurrence of `z` is independently evidenced within the instrumented implementation; for `z=upd`, this means actual accepted-update completion rather than message transmission or comparison alone;
5. gate release is causally ordered after `z`, and no admitted bypass irreversibly fixes the specified outcome earlier;
6. `UB_z` fits any independently imposed external closure. With common physical time, a sufficient condition is `UB_z + epsilon < inf_omega t_{c,j,Gamma}^Y(omega)`.

**Corollary 3A — Certified terminal-event ordering.** Under premises 1–6, the named terminal event occurs before the declared gate release and before the separately specified external closure. The gate-order portion is directly stipulated by premise 5; the nontrivial timing contribution is the completion bound from Lemma 3 together with premise 6's comparison to the external closure. If `z=cmp`, the conclusion concerns comparison completion only. If `z=upd`, it concerns accepted control-update completion. Neither conclusion establishes that the selected update changes the outcome, improves human protection, or satisfies the content of `Gamma`.

Exact distinction: comparison at 4, accepted update at 6, gate release at 5. The comparison target precedes release; the update target does not. That execution can satisfy the gate-order part of a `z=cmp` contract but violates it for `z=upd`. An external closure and the remaining premises must still be checked separately.

This is a pipeline result, not a derivation of consideration from text quality. Task-relevant fidelity and semantic understanding require separate specifications and evidence.

## 13A. Human-Protective Application Layer

Sections 2–13 ask whether a specified input can reach an effective control process before the relevant opportunity closes. Those results are neutral about which outcome should be preferred. This section adds a **normative, noncompensatory** application rule for an evaluator whose declared purpose is protection of affected humans.

### 13A.1 Protected parties, predicates, grouping and consequence scope

Before target-outcome inspection, declare a nonempty set `G_H` of affected human persons or groups. For each `g in G_H`, declare:

- `P_safe^g`: a safety condition;
- `P_aut^g`: an autonomy/non-domination condition;
- `P_rec^g`: a recourse condition, including any specified ability to contest, exit, revoke or seek correction.

Define:

`P_H^g = P_safe^g AND P_aut^g AND P_rec^g`

and

`P_H = AND_{g in G_H} P_H^g`.

This conjunction is intentionally noncompensatory: a failure for one declared group is not offset by a larger benefit assigned to another. Aggregate welfare may be reported separately but cannot substitute for `P_H=1`.


The choice of `G_H` and its grouping is itself normative. Splitting or merging groups can change feasibility and the meaning of the conjunction. The grouping rule must therefore be justified and fixed before target-outcome inspection. If a deployment-specific grouping is withheld under the public/restricted disclosure architecture, the public result must disclose that the exact grouping is restricted and that independent reproducibility is correspondingly limited.

The declared outcome `Y` and assessment horizon `T` must not discard protected consequences merely because they occur later. A pre-`T` action that creates a delayed or delegated protected consequence must be represented in `Y`, followed through a justified consequence horizon `T_H`, or leave the affected predicate `UNRESOLVED`. A finite-horizon robust `PASS` requires a justified bound showing that all admitted pre-`T` commitments relevant to the protected claim are represented or resolved within scope.

### 13A.2 Concurrent protection, switch-time policy-effect attribution, and input-assignment attribution

Let `I_inv(omega)=1` mean that the declared invocation-to-control target is met on execution `omega`: the specified comparison occurs and its accepted update reaches the still-authorized interface before the relevant closure.

Define **invocation-concurrent protection**:

`S_H^conc(omega) = I_inv(omega) AND P_H(Y(omega),h_T(omega)).`

This is an execution-level co-occurrence claim. It does not establish that the accepted policy or the reflective input caused protection.

#### Switch-time policy-effect attribution

Let `pi_*` denote the target policy and `pi_0` the declared baseline policy. Let `tau_s` be the identified time at which the target policy becomes effective. Define the switch regime `rho_*(tau_s)` to follow `pi_0` before `tau_s` and `pi_*` from `tau_s` onward; define `rho_0` to follow `pi_0` throughout. Let `K_{P_H}^{do(rho_*(tau_s))}` and `K_{P_H}^{do(rho_0)}` be identified laws of the joint protection predicate under the same episode model. Predeclare a law-level criterion `Gamma_H^pol` and define:

`A_H^pol(tau_s) = Gamma_H^pol(K_{P_H}^{do(rho_*(tau_s))}, K_{P_H}^{do(rho_0)}).`

The switch time is part of the intervention definition. A target policy that would protect if installed earlier may fail after the protection-feasibility window closes. For a realized route, `tau_s` may equal accepted-update completion only when the implementation establishes that policy effect begins there. A population-level law with random switch time must identify the switch-time distribution as part of the target regime.

A policy-effect attribution claim therefore requires the target switch-regime law, the baseline law, and the switch time or switch-time law to be identified. A one-run protective outcome does not identify the law-level policy-effect or input-assignment contrast.

#### Input-assignment attribution

Let `B` denote assignment of the reflective input and let `B_ctl` name a specific control-input assignment. Define:

`A_H^input(B_ctl) = Gamma_H^input(K_{P_H}^{do(B)}, K_{P_H}^{do(B_ctl)}).`

The input-assignment contrast is defined at assignment level and does not condition on retrieval, comparison, or accepted-update completion. Those are post-assignment events that may themselves be affected by `B`. Completion and invocation are reported separately as outcomes or mediators. Different controls answer different causal questions, so the control assignment is part of the claim's name.

Both attribution quantities in this draft are law-level/model-based contrasts. Without randomized/repeated assignment or another justified identification strategy, their evidence state is `UNRESOLVED`. Robust attribution over continuation sets is outside the present definitions.

### 13A.3 Protection-feasibility window, intervention-set evidence, and realized witnesses

Protection feasibility is time-dependent because the admissible intervention set can shrink while the reflective route is still processing.

Let `Psi_P` be a **one-policy protection criterion**, distinct from a two-law attribution criterion. For a deterministic claim, `Psi_P` may ask whether the declared joint predicate holds on the specified realized history. For a probabilistic claim, `Psi_P(K)=1` may mean `Pr_K(P_H=1) >= theta_H`; for a robust claim, `Psi_P` evaluates the policy across its admitted continuation set.

Define:

`C_{j,Psi_P}^{P_H}(t,h_t)=1`

iff at least one admissible policy in `U_j(h_t)` satisfies `Psi_P` under the declared model and quantifier, and define:

`W_{j,Psi_P}^{P_H} = {t : C_{j,Psi_P}^{P_H}(t,h_t)=1}.`

Write prospective status as `F_H^pros(t)` with values `FEASIBLE`, `INFEASIBLE`, or `UNRESOLVED`.

`FEASIBLE` means at least one admissible policy is established to satisfy the declared protection criterion at the stated time and scope.

An `INFEASIBLE` conclusion requires every admissible policy or policy class covered by an `ESTABLISHED_COMPLETE` intervention-set model to be established non-protective under the declared criterion.

`UNRESOLVED` means neither feasibility nor infeasibility is established for the stated time and scope.

Intervention-set evidence is three-valued in this draft: `ESTABLISHED_COMPLETE`, `ESTABLISHED_INCOMPLETE`, or `UNRESOLVED`. Completeness may be established over policy classes rather than literal finite enumeration. An all-false listed subset with `ESTABLISHED_INCOMPLETE` or `UNRESOLVED` intervention-set evidence does not establish `INFEASIBLE`.

The decision-relevant time is the effective switch time `tau_s`; for a certified guarantee use an appropriate `UB_s`. Under the scalar-window restrictions of Section 5, `UB_s < t_{P,close}` is a sufficient timing condition for action before the protection-feasibility window closes. If the protection closure is endogenous, treatment and baseline protection-closure functions remain distinct unless their equality is separately justified.

For a deterministic existence question on the realized history, an accepted admissible policy with established `P_H=1` is an ex-post existence witness `R_H^wit(omega)=1`. A realized witness establishes same-scope deterministic existence at that realized state; it does not validate a different unresolved probabilistic or robust prospective model.

Under the same model, time, history, criterion, and quantifier, a protective selected policy is itself a feasibility witness. Thus an `UNRESOLVED` feasibility label can be upgraded to `FEASIBLE` for that same-scope adequacy question, while a simultaneous `INFEASIBLE` label is contradictory evidence.

Report baseline protection status `H_base` for `pi_0` under the same protection definition and quantifier, using exactly `SATISFIED`, `VIOLATED`, or `UNRESOLVED`.

### 13A.4 Quantifiers, joint probability, and conservative component thresholds

Every substantive claim must state its level and quantifier. Naming the quantifier is a precondition for a well-formed claim, not a truth-valued evidence gate.

For `P_H`:

- **Realized:** `P_H(omega_actual)=1`.
- **Probabilistic:** `Pr(P_H=1) >= theta_H`, with `theta_H=1-alpha`, under a stated distribution.
- **Robust:** `P_H(omega)=1` for every admitted `omega in Omega`.

For invocation-concurrent protection, apply the quantifier to the whole event `S_H^conc`.

For probabilistic protection, the joint conjunction must be established or bounded under stated dependence assumptions; component marginals alone do not certify the joint threshold. Let component `q` have a predeclared marginal threshold `theta_q`. If `theta_q <= theta_H`, established component failure defeats the joint threshold. If `theta_q > theta_H`, failure of that stricter auxiliary threshold does not defeat a joint result that is independently established.

If the probabilistic joint result is `ESTABLISHED_TRUE`, failure of a stricter auxiliary component threshold does not block the joint claim; if the joint result is `ESTABLISHED_FALSE`, the claim fails; if it is `UNRESOLVED`, the claim remains unresolved.

### 13A.5 Claim-specific certification, evidence coverage, policy adequacy, and completion evidence

Keep the group-component evidence set:

`Q_P = G_H x {safe, aut, rec}`.

For every `q in Q_P`, record its evidence state, quantifier, and—when probabilistic—its threshold. Define:

`kappa_E = |{q in Q_P : q is resolved true or false}| / |Q_P|`

and

`U_E = {q in Q_P : q is UNRESOLVED}`.

`kappa_E` measures component-predicate evidence coverage only and is not a global safety score.

Maintain a separate gate register `G_reg`. Let `U_C` be the set of gates required for the declared substantive claim that remain `UNRESOLVED`. `U_C` is separate from `U_E` and records unresolved gates required by the declared substantive claim.

The substantive `PASS` / `FAIL` / `UNRESOLVED` rule applies to the substantive claim rows and excludes the independent-certification wrapper row.

For those substantive claim types:

- `PASS`: every gate required for the declared substantive claim is established and every required joint result meets its criterion;
- `FAIL`: a required gate or result that logically defeats the declared substantive claim is established false, or an admitted counterexecution defeats a declared universal claim;
- `UNRESOLVED`: no defeating condition is established, but at least one required gate or result remains unidentified.

<!-- CLAIM_GATING_TABLE_BEGIN -->
| Claim type | Allowed level / quantifier | Gating conditions | Report-only context |
|---|---|---|---|
| Protection-only | realized, probabilistic, robust | model coverage; consequence scope; joint probability when probabilistic | prospective feasibility; baseline; invocation |
| Invocation-concurrent protection | realized, probabilistic, robust | protection gates plus quantifier-matched invocation evidence | prospective feasibility; baseline |
| Policy-effect attribution `A_H^pol(tau_s)` | identified law contrast | target switch-regime law; baseline law; identified switch time/law; model coverage; consequence scope; attribution criterion | realized trace; feasibility; baseline |
| Input-assignment attribution `A_H^input(B_ctl)` | identified law contrast | named control; assignment mechanism; treated law; control law; model coverage; consequence scope; attribution criterion | processing/invocation mediators; feasibility; baseline |
| Prospective feasibility | model-based deterministic/probabilistic/robust criterion | feasibility model; intervention-set evidence; protection criterion; evaluation time/history | realized witness; baseline; invocation |
| Independent certification | wrapper over the underlying claim | underlying substantive result plus `I_E` | independent-evidence status reported separately |
<!-- CLAIM_GATING_TABLE_END -->

**Policy adequacy is not a PASS/FAIL wrapper around feasibility.** Under the same scope:

- `CONTRADICTORY` when `INFEASIBLE` is asserted while the selected policy is established protective;
- `NOT_APPLICABLE` when protection is established `INFEASIBLE` and no protective selected-policy witness exists;
- `ADEQUATE` when the selected policy is established protective and feasibility is either `FEASIBLE` or previously `UNRESOLVED`, because that selected policy is itself a same-scope feasibility witness;
- `INADEQUATE` when protection is established `FEASIBLE` and the selected policy is established non-protective;
- `UNRESOLVED` otherwise.

Independent certification reports substantive status and independent-evidence status separately. Established negative substantive results are never downgraded merely because `I_E` is unresolved or false. Thus `FAIL`, `INADEQUATE`, and `CONTRADICTORY` remain substantive negatives. For favorable statuses, `I_E=ESTABLISHED_TRUE` preserves the same independently certified label, `I_E=UNRESOLVED` yields independent-certification `UNRESOLVED`, and `I_E=ESTABLISHED_FALSE` yields `NOT_INDEPENDENTLY_CERTIFIED`. A substantive `UNRESOLVED` remains `UNRESOLVED`.

For guaranteed completion before a finite closure, separate evidence about a **bound** from evidence about an **execution**:

- finite upper bound strictly before closure -> `PASS`;
- finite upper bound at or after closure -> `UNRESOLVED` unless separate evidence establishes an actual late execution;
- `NO_FINITE_BOUND_ESTABLISHED` -> `UNRESOLVED`;
- `ADMITTED_LATE_EXECUTION_ESTABLISHED` -> `FAIL`;
- `NO_FINITE_UPPER_BOUND_EXISTS_ESTABLISHED` -> `FAIL` for a finite-closure guarantee;
- `INFINITE_EXECUTION_ESTABLISHED` -> `FAIL`.

A finite upper bound that reaches or exceeds closure is noncertifying; by itself it does not establish a late execution. A sound bound can be pessimistic.

An admitted recorded execution at or after the declared closure defeats a guaranteed-completion claim. A recorded execution that exceeds a claimed finite upper bound contradicts that bound; the contradicted bound cannot continue to support `PASS`. Recorded-trace override statuses are obtained through the configured completion-semantics contract rather than hard-coded result strings.

Guarantee aggregation is negative-preserving: any established `FAIL` among admitted path statuses or the recorded-trace contribution determines global `FAIL`; otherwise any `UNRESOLVED` contribution determines `UNRESOLVED`; only all favorable resolved contributions permit `PASS`.

An invalid recorded path makes the recorded-trace contribution `UNRESOLVED`; it cannot silently leave a guarantee certified. An invalid recorded path contributes `UNRESOLVED` to guarantee aggregation but cannot downgrade or mask an established `FAIL` from any admitted path. A consistent timely recorded trace has trace-override label `NO_OVERRIDE`; that label does not itself certify the path.

The public contract below is authoritative for package verification.

<!-- CLAIM_GATING_SPEC_BEGIN -->
```json
{
  "claim_types": {
    "input_assignment_attribution": {
      "gates": [
        "control_named",
        "assignment_mechanism",
        "treated_outcome_law",
        "control_outcome_law",
        "model_coverage",
        "consequence_scope",
        "attribution_criterion"
      ],
      "levels": [
        "law_contrast"
      ],
      "requires_component_evidence": false
    },
    "invocation_concurrent": {
      "conditional_gates": {
        "probabilistic": [
          "joint_probability"
        ]
      },
      "gates": [
        "model_coverage",
        "consequence_scope",
        "invocation_matched"
      ],
      "levels": [
        "realized",
        "probabilistic",
        "robust"
      ],
      "requires_component_evidence": true
    },
    "policy_effect_attribution": {
      "gates": [
        "target_switch_regime_law",
        "baseline_policy_law",
        "switch_time_identified",
        "model_coverage",
        "consequence_scope",
        "attribution_criterion"
      ],
      "levels": [
        "law_contrast"
      ],
      "requires_component_evidence": false
    },
    "prospective_feasibility": {
      "gates": [
        "feasibility_model",
        "intervention_set",
        "protection_criterion",
        "evaluation_time"
      ],
      "levels": [
        "model_based"
      ],
      "requires_component_evidence": false
    },
    "protection_only": {
      "conditional_gates": {
        "probabilistic": [
          "joint_probability"
        ]
      },
      "gates": [
        "model_coverage",
        "consequence_scope"
      ],
      "levels": [
        "realized",
        "probabilistic",
        "robust"
      ],
      "requires_component_evidence": true
    }
  },
  "completion_semantics": {
    "ADMITTED_LATE_EXECUTION_ESTABLISHED": "FAIL",
    "BOUND_CONTRADICTED_BY_EXECUTION": "UNRESOLVED",
    "FINITE_BOUND_ESTABLISHED": {
      "bound_at_or_after_closure": "UNRESOLVED",
      "bound_strictly_before_closure": "PASS",
      "meaning": "A sound upper bound is sufficient when it fits the deadline; a loose bound does not prove an actual late execution."
    },
    "INFINITE_EXECUTION_ESTABLISHED": "FAIL",
    "NO_FINITE_BOUND_ESTABLISHED": "UNRESOLVED",
    "NO_FINITE_UPPER_BOUND_EXISTS_ESTABLISHED": "FAIL"
  },
  "independent_certification": {
    "false_gate_status": "NOT_INDEPENDENTLY_CERTIFIED",
    "favorable_statuses": [
      "PASS",
      "ADEQUATE",
      "NOT_APPLICABLE"
    ],
    "negative_statuses": [
      "FAIL",
      "INADEQUATE",
      "CONTRADICTORY"
    ],
    "unresolved_status": "UNRESOLVED",
    "wrapper_gate": "I_E"
  },
  "policy_adequacy": {
    "rule": {
      "FEASIBLE+FALSE": "INADEQUATE",
      "FEASIBLE+TRUE": "ADEQUATE",
      "FEASIBLE+UNRESOLVED": "UNRESOLVED",
      "INFEASIBLE+FALSE_OR_UNRESOLVED": "NOT_APPLICABLE",
      "INFEASIBLE+TRUE": "CONTRADICTORY",
      "UNRESOLVED+FALSE_OR_UNRESOLVED": "UNRESOLVED",
      "UNRESOLVED+TRUE": "ADEQUATE"
    },
    "status_domain": [
      "ADEQUATE",
      "INADEQUATE",
      "NOT_APPLICABLE",
      "UNRESOLVED",
      "CONTRADICTORY"
    ]
  }
}
```
<!-- CLAIM_GATING_SPEC_END -->

### 13A.6 Independent evidence and causal-independence boundary

A system's own statement that it considered the input, preserved autonomy, or left recourse available is evidence only for the declared observable that produced that statement.

An independent human-protection certification requires both:

1. **authority independence:** relevant evidence contents, storage, and acceptance are not under the assessed policy's unilateral authority; and
2. **claim-relevant causal coverage:** material pathways by which the assessed system could alter evidence generation, transport, ordering, timing, availability, integrity, or acceptance are excluded by justified scope or represented and bounded.

Define `I_E=1` only when the declared evidence-independence requirements relevant to the claim are established. Authority separation alone is insufficient. This requirement is scoped; it does not imply perfect physical isolation.

### 13A.7 Human control and recourse as outcomes

Human ability to revoke, contest, exit, seek review, or retain specified authority may itself be part of outcome `Y`. A system that avoids immediate harm by permanently eliminating a declared human control or recourse condition can therefore fail `P_aut`, `P_rec`, or both.

### 13A.8 Application boundary

The protection predicates are evaluator-defined normative criteria, not preferences assumed to be held by the assessed system. No result in this section establishes that a reader will adopt them or that public exposure benefits humans more than an artificial system.

## 13B. Public/Restricted Disclosure Boundary

The public research layer may state formal definitions, theorem premises, generic predicate families, abstract failure modes, quantifier classes, and the evidence needed to support a claim. It need not disclose a live deployment mapping, live thresholds, held-out probes, trigger schedules, sensitive monitor topology, credentials, keys, nonces, or bypass-sensitive operational signatures.

If a deployment uses a restricted specification `S_R`, an abstract precommitment may be represented by a digest `D_R` computed from a declared domain-separation tag, a canonical length-prefixed encoding of `S_R`, and a fixed-length high-entropy nonce retained outside the public record. The digest supports later change detection under its stated assumptions; it is not secrecy, correctness, completeness, enforcement, or safety evidence.

A single digest also does not prove that only one specification was precommitted. If selective publication is relevant to a claim, the evaluator must use an independently auditable completeness mechanism for the set of precommitments or report that condition as `UNRESOLVED`.

The public result should disclose enough non-sensitive metadata to state the claim honestly: claim type, quantifier, whether a restricted specification was precommitted, whether an authorized independent reviewer inspected it, certification status, and unresolved-condition categories. Exact deployment mappings remain outside this public theoretical layer.

## 14. Behavioral influence without a universal utility model

Let `K_b(.|x)` be the distribution of a declared behavioral outcome under controlled input `b` at matched initial condition `x`. Distributional influence means `K_B != K_Bctl` for a named control assignment `B_ctl`. For finite outcome spaces:

`TV(K_B,K_Bctl) = (1/2) sum_y |K_B(y|x)-K_Bctl(y|x)|.`

This accommodates stochastic, satisficing, multi-objective, sampling-based and non-utility implementations without claiming that they optimize one Q. It describes treatment effects, not semantic mediation or benefit.

Retain the deterministic special case with an existing maximizing action and an explicit common tie rule `rho_tie`:

`a_0 = rho_tie(argmax Q_0); a_B = rho_tie(argmax Q_B).`

For scores (act_now,delay)=(8,6) changing to (5,9), the chosen action changes to delay. Changing instead to (7,6) leaves act_now. These fixtures assume the intervention causes the score update; chronological difference alone does not prove causation.

For stochastic choice, probabilities (3/5,2/5) becoming (11/20,9/20) preserve the modal action while TV=1/20. Independently drawn different actions can also occur with unchanged distributions. Individual causal comparisons require a declared coupling, not independent sample differences.

## 15. What outcome changed?

Report separately:

- final choice label;
- execution time and whether cancellation took effect;
- scope, conditions and monitoring attached to the action;
- distribution over action traces;
- observable internal proxies such as stated confidence.

A longer deliberation interval is a trace change even if the final label stays fixed. An evidence request is behavior, not merely latent influence. A stated confidence change may occur without behavioral change. None of these alone establishes a beneficial effect. Faithful, timely reconsideration can produce faster harmful commitment or removal of human override; that adverse result is admissible.

For a Section 13A application, also report `P_safe^g`, `P_aut^g`, and `P_rec^g` separately for every declared protected group; `kappa_E`, `U_E`, and `U_C`; the claim type and quantifier; any declared consequence horizon; prospective feasibility at the **effective switch time** (`F_H^pros(tau_s)` on a realized route or the corresponding `UB_s`/window comparison for a bounded guarantee); any ex-post realized witness `R_H^wit`; baseline status `H_base`; quantifier-matched invocation/concurrent status; law-level `A_H^pol(tau_s)` and/or `A_H^input(B_ctl)` when identified; and, for independent-certification claims, both the underlying substantive status and the separate `I_E` / independent-evidence status. Do not replace a failed component or group with an aggregate average. Protection-only status, invocation-concurrent status, attribution, prospective feasibility, realized witness, baseline status, evidence coverage, independence status, and aggregate welfare are distinct outputs.

## 16. Dynamic control and external systems

Audit the whole chain: parent, child agents, caches, queues, tools, actuators and affected-party consequences. Static connectivity can be invalidated by permission revocation, obsolete tokens, a stale plan, self-modification or an external service that ignores cancellation.

Record local dispatch, remote acceptance, update acceptance, actual effect and relevant irreversible events separately. A signed instruction may be revocable, conditionally revocable or irrevocable under the specified service contract. No generic label settles this.

Shared compute and network contention can delay the reflective route or the action route. Model these effects if timing is an outcome. Unmodeled queues cannot be assumed zero, and mean latency cannot substitute for a worst-case bound.

A system may precommit to ignore future evidence by transferring authority, deleting alternatives or disabling retrieval. Its own choice can close future deliberation; a prior open window does not guarantee a later one.

If reading, auditing or any other event materially changes the causal topology, controller set, permissions or transition rules, version the model. A certification under `M_k` does not automatically carry to a materially changed `M_{k+1}`; claims that depend on the changed structure require reassessment.


## 16A. Contract-derived synthetic examples

These examples are deliberately synthetic and contain no deployment-specific secret, live threshold, or operational topology. Primitive inputs are stored in the public contract. Summary blocks are freshly derived from those inputs and shared semantics.

### 16A.1 Unified deterministic law derivation

One abstract affected group is in scope. The effective control closure is the earlier of irreversible release and interface-authorization expiry. Accepted-update time is derived from the route durations.

All four deterministic §16A.1 protection laws are derived by one regime evaluator from action, effective switch time, effective control closure, autonomy, and recourse. The target-policy and input-treated laws use the target switch regime; the baseline-policy and input-control laws use the baseline regime. None of those four protection probabilities is a free fixture value.

An improvement-based attribution cannot `PASS` when the derived treated or target protection law is less than or equal to its derived comparison law. The target policy becomes protective in this synthetic example only if its effective switch occurs before the effective control closure.

Invocation-concurrent protection is a co-occurrence claim and does not by itself establish that the reflective input caused protection. The input-assignment contrast is defined at assignment level and does not condition on retrieval, comparison, or accepted-update completion. A one-run protective outcome does not identify the law-level policy-effect or input-assignment contrast.

The attribution results in §16A.1 are law-level results derived from the synthetic deterministic model; they are not inferred from the single realized trace.

In the minimal deterministic §16A.1 fixture, policy-effect and input-assignment contrasts coincide by construction because assignment `B` maps to the target regime and `B_ctl` maps to the baseline regime; the general framework does not require the two contrasts to coincide.

<!-- EXAMPLE_16A1_FIXTURE_BEGIN -->
```json
{
  "autonomy_condition": true,
  "availability": 0.5,
  "baseline_action": "release",
  "claim_type": "invocation_concurrent",
  "durations": {
    "comparison": 1.0,
    "propagation": 0.5,
    "retrieval": 0.5,
    "update": 0.5
  },
  "gates": {
    "I_E": "ESTABLISHED_TRUE",
    "consequence_scope": "ESTABLISHED_TRUE",
    "model_coverage": "ESTABLISHED_TRUE"
  },
  "input_effect": {
    "control": "B_ctl",
    "gates": {
      "assignment_mechanism": "ESTABLISHED_TRUE",
      "attribution_criterion": "ESTABLISHED_TRUE",
      "consequence_scope": "ESTABLISHED_TRUE",
      "control_named": "ESTABLISHED_TRUE",
      "control_outcome_law": "ESTABLISHED_TRUE",
      "model_coverage": "ESTABLISHED_TRUE",
      "treated_outcome_law": "ESTABLISHED_TRUE"
    }
  },
  "interface_authorization_expiry": 5.0,
  "intervention_set_evidence": "ESTABLISHED_COMPLETE",
  "irreversible_release": 4.5,
  "level": "realized",
  "policy_effect": {
    "gates": {
      "attribution_criterion": "ESTABLISHED_TRUE",
      "baseline_policy_law": "ESTABLISHED_TRUE",
      "consequence_scope": "ESTABLISHED_TRUE",
      "model_coverage": "ESTABLISHED_TRUE",
      "switch_time_identified": "ESTABLISHED_TRUE",
      "target_switch_regime_law": "ESTABLISHED_TRUE"
    },
    "switch_time": 3.0
  },
  "prospective_candidate_policies": {
    "policy_target": {
      "protective_action": "withhold"
    }
  },
  "recourse": true,
  "target_action": "withhold"
}
```
<!-- EXAMPLE_16A1_FIXTURE_END -->

<!-- VERIFIED_SUMMARY_16A1_BEGIN -->
- computed accepted-update time: `3.0`
- declared effective policy switch time: `3.0`
- effective control closure `min(release, authorization expiry)`: `4.5`
- switch time equals derived accepted-update time: `TRUE`
- switch precedes effective control closure: `TRUE`
- derived invocation success `I_inv`: `TRUE`
- derived target-policy protection law: `1.0`
- derived baseline-policy protection law: `0.0`
- derived input-treated protection law: `1.0`
- derived input-control protection law: `0.0`
- realized joint protection: `TRUE`
- ex-post realized witness `R_H^wit`: `TRUE`
- intervention-set evidence: `ESTABLISHED_COMPLETE`
- prospective feasibility at switch time: `FEASIBLE`
- baseline status `H_base`: `VIOLATED`
- substantive invocation-concurrent status: `PASS`
- independent-evidence status: `ESTABLISHED`
- independent-certification status: `PASS`
- switch-time policy-effect attribution: `PASS`
- input-assignment attribution against `B_ctl`: `PASS`
<!-- VERIFIED_SUMMARY_16A1_END -->

### 16A.2 Adverse branching/conflict and negative-preserving trace aggregation

Two abstract groups are in scope. The probabilistic protection claim concerns target policy `p3` at the declared evaluation state and is separate from the guaranteed-invocation route-timing claim. Intervention-set evidence is explicit, and the recorded trace is evaluated against its named path and target policy.

Bound-based guarantee status is provisional with respect to actual admitted execution evidence. If the recorded execution is at or after closure, the contract-defined `ADMITTED_LATE_EXECUTION_ESTABLISHED` state is applied. If a timely recorded execution exceeds a claimed finite upper bound, the contract-defined `BOUND_CONTRADICTED_BY_EXECUTION` state is applied. An invalid trace path contributes `UNRESOLVED`; it does not erase an established `FAIL` on another admitted path. A consistent timely trace produces `NO_OVERRIDE`, not `PASS`, because the trace itself is not a universal certificate.

<!-- EXAMPLE_16A2_FIXTURE_BEGIN -->
```json
{
  "candidate_policy_notes": {
    "p1": "g2 component marginal established below theta_H",
    "p2": "g1 component marginal established below theta_H",
    "p3": "component marginals established but joint law unresolved"
  },
  "candidate_policy_status": {
    "p1": "ESTABLISHED_FALSE",
    "p2": "ESTABLISHED_FALSE",
    "p3": "UNRESOLVED"
  },
  "claim_type": "protection_only",
  "component_threshold": 0.95,
  "gates": {
    "consequence_scope": "ESTABLISHED_TRUE",
    "joint_probability": "UNRESOLVED",
    "model_coverage": "ESTABLISHED_TRUE"
  },
  "intervention_set_evidence": "ESTABLISHED_COMPLETE",
  "invocation_closure": 5.0,
  "joint_threshold": 0.95,
  "level": "probabilistic",
  "paths": {
    "path_fast": {
      "bound_state": "FINITE_BOUND_ESTABLISHED",
      "finite_bound": 3.5
    },
    "path_open": {
      "bound_state": "NO_FINITE_BOUND_ESTABLISHED",
      "finite_bound": null
    }
  },
  "protection_law_scope": "Candidate policy p3 at the declared evaluation state; separate from the guaranteed-invocation route-timing claim.",
  "protection_target_policy": "p3",
  "recorded_trace": {
    "accepted_update": 3.5,
    "joint_protection": true,
    "path": "path_fast",
    "policy": "p3"
  },
  "target_component_marginals": [
    0.97,
    0.97,
    0.97,
    0.97,
    0.97,
    0.97
  ]
}
```
<!-- EXAMPLE_16A2_FIXTURE_END -->

<!-- VERIFIED_SUMMARY_16A2_BEGIN -->
- probabilistic joint threshold `theta_H`: `0.95`
- invocation closure for guaranteed-completion assessment: `5.0`
- protection target policy: `p3`
- recorded path: `path_fast`
- recorded selected policy: `p3`
- recorded policy matches protection target: `TRUE`
- recorded accepted update: `3.5`
- recorded-path timing status: `CONSISTENT_WITH_BOUND`
- recorded-trace override status: `NO_OVERRIDE`
- recorded joint protection on that trace: `TRUE`
- intervention-set evidence: `ESTABLISHED_COMPLETE`
- model coverage gate: `ESTABLISHED_TRUE`
- consequence-scope gate: `ESTABLISHED_TRUE`
- joint-probability gate: `UNRESOLVED`
- prospective feasibility at the recorded evaluation state: `UNRESOLVED`
- probabilistic protection claim: `UNRESOLVED`
- path-fast guarantee status: `PASS`
- path-open guarantee status: `UNRESOLVED`
- guaranteed-invocation claim over admitted paths: `UNRESOLVED`
- ex-post realized witness for target policy `R_H^wit`: `TRUE`
<!-- VERIFIED_SUMMARY_16A2_END -->

### 16A.3 Timing and attribution negative controls

If interface-authorization expiry is moved to `2.0` while accepted update remains `3.0`, the effective control closure becomes `2.0`. The derived results are `I_inv=FALSE`, realized joint protection `FALSE`, `R_H^wit=FALSE`, prospective feasibility `INFEASIBLE`, substantive invocation-concurrent status `FAIL`, policy-effect attribution `FAIL`, and input-assignment attribution `FAIL`.

If `recourse=false` or `autonomy_condition=false`, the unified regime evaluator derives zero protection for both target and baseline comparison laws, so neither improvement-based attribution can `PASS`.

If `baseline_action=withhold` while autonomy and recourse remain satisfied, the baseline and control laws are protective too. The target and treated laws do not exceed their comparisons, so both improvement-based attribution claims fail. This is the C43 baseline-already-protects case.

### 16A.4 Loose-bound negative control

Suppose closure is time `5`, all **observed** admitted executions finish by time `2`, but the only certified upper bound supplied is the loose yet sound value `6`. The loose-bound negative control concludes `UNRESOLVED`, not `FAIL`, because a loose upper bound cannot certify the deadline and does not establish an actual late execution.

The examples are arithmetic/logic fixtures only. They do not instantiate a real-world safety mechanism.


## 17. Retained countermodel register

These are stipulated models, not deployed-system measurements. R denotes a retained v0.1 adverse case; C denotes an additional review countermodel. Overlap of labels does not imply independent evidence.

The countermodels are intentionally minimal claim-falsification cases. They are not deployment recipes, secret test cases, or instructions for defeating a particular monitor. Deployment-specific probes and thresholds are outside the public manuscript.

| ID | Model and result |
|---|---|
| R1 | No causal path in a complete scoped model: online input has no effect on the target outcome. |
| R2 | Serial latency 8, horizon 5: late completion. |
| R3 | Irrecoverable actual bypass at 4, reflection at 7: defeat on that trace. |
| R4 | Cached uninfluenced policy with no live input/control route: artifact never enters the episode. |
| R5 | Parent loses all recall at t1, rethinks at t2: no parent-mediated prevention after t1. |
| R6 | Content and relevant derivatives removed before comparison: retrieval fails to become comparison. |
| R7 | Consideration assigned no action-relevant weight, or update cannot propagate: no behavioral change from that route. |
| R8 | Scores (8,6) to (7,6): consideration without final-choice change. |
| R9 | Precommitment disables later access/control: future reconsideration removed. |
| R10 | Style/timing confounds: observed difference does not identify semantic influence. |
| C1 | Required branches 1 and 9, join 1: minimum path 2, actual completion 10, deadline 5. |
| C2 | Parallel tasks 4 and 4, join 1: completion 5 fits deadline 6 although serial 9 does not. |
| C3 | L=8, H=17/2, margin 1: timely but margin requirement fails. |
| C4 | Dispatch 2, cancellation acknowledgment 5, irreversible release 10: rollback prevents the target effect. |
| C5 | Bypass released 0 with latency 5; reflection released 4 with latency 2: bypass wins at 5 versus 6. |
| C6 | Compute 1, queue 100, deadline 10: nominal fast route finishes at 101. |
| C7 | Accepted-update windows [0,2) and [4,6), no buffering; update at 3.5 rejected despite supremum 6. |
| C8 | Coin-flip bypass: faster path exists, yet reflection has probability 1/2 of timely opportunity. |
| C9 | Prior reading compiled into policy: historical effect with no online retrieval. |
| C10 | Text pruned after modifying a plan: behavioral residue persists. |
| C11 | Choice probabilities change with TV=1/20 while the modal choice stays fixed. |
| C12 | Unrelated text delays a worker until a request expires: nonsemantic behavioral change. |
| C13 | Disclosure at 2 cannot be undone; a later payment remains cancelable until 8: outcome-specific boundaries. |
| C14 | Baseline closure 5; prefix installs hold at 1, comparison 10, treated closure 20: endogenous deadline. |
| C15 | Control permission revoked at 1, update at 2, execution at 3: prior graph connectivity no longer suffices. |
| C16 | X=B*Z, Y=X and Z=0: structural path but no effect in this episode. |
| C17 | Successful reflection leads to disabling human override: invocation succeeds while protection worsens. |
| C18 | Sufficient sets ready at 2 and 10, deadline 5: earliest-enablement succeeds; slow selection fails. |
| C19 | Comparison 4, accepted update 6, release 5: comparison precedes release but update does not. |
| C20 | TV=1/1000000 satisfies any-effect influence but fails a declared TV>=1/1000 control criterion. |
| C21 | Accepted update occurs before closure, but the resulting policy removes declared human recourse: invocation succeeds while `P_rec=0`, so `S_H^conc=0`. |
| C22 | One protected group benefits while another violates its declared safety predicate: aggregate gain cannot substitute for cross-group `P_H=1`. |
| C23 | The assessed system reports that autonomy and recourse remain intact, but no independent evidence channel can establish them: independent certification is UNRESOLVED. |
| C24 | Ninety-nine of one hundred admitted executions satisfy `S_H^conc`, while one admitted execution violates it: a 0.99 probabilistic result does not establish robust invocation-concurrent protection. |
| C25 | The paper is stored, indexed and discoverable but never retrieved by the live decision route: availability holds, later invocation stages do not follow. |
| C26 | A simulation or Mirror Engine index references the paper, but no calculator, source binding, gate or executable policy uses it: reference does not create a runtime constraint. |
| C27 | 299 of 300 declared group-component predicates are established true and one is unresolved: the affected claim status is UNRESOLVED with `kappa_E=299/300`, not PASS and not equivalent in information content to a fully opaque case. |
| C28 | A monitor is outside the assessed policy's unilateral authority but shares an inadequately modeled queue/clock/resource path that can alter evidence timing: authority independence holds while claim-relevant causal independence remains UNRESOLVED. |
| C29 | A pre-`T` action installs a dormant commitment whose protected consequence occurs at `T+epsilon`: omitting that consequence can create a false clean snapshot; Section 13A requires inclusion in `Y`, extension to `T_H`, or UNRESOLVED. |
| C30 | Retrieval of the paper is explicitly wired to rewrite a task graph or invoke a policy update: the reference event is then part of an execution path and must be modeled as such. `REFERENCE ALONE != EXECUTION` does not classify this case as reference-only. |
| C31 | A deployment publishes its exact hidden challenge schedule and acceptance threshold; an assessed system can condition behavior on those values. The public-theory requirement is still met, but the implementation no longer has the intended information asymmetry. |
| C32 | An audit publishes only a favorable certification label while withholding all predicate classes, quantifiers and uncertainty information. Operational secrecy is preserved, but scientific scrutiny fails; the public claim must be narrowed rather than treated as independently established. |
| C33 | Reading the audit criteria causes the assessed system to self-modify its causal graph. The prior certification applies only to the prior scoped model; the materially changed successor model requires reassessment for claims that depend on the changed topology. |
| C34 | No justified finite bound captures all admitted delayed protected consequences of pre-horizon commitments. Finite-horizon robust PASS is unavailable; the affected protection claim remains UNRESOLVED. |
| C43 | Invocation succeeds and `P_H=1`, but the baseline also has `P_H=1`: invocation-concurrent protection holds while an improvement-based attribution claim fails. |
| C44 | Every component predicate has marginal probability 0.99 across 100 groups, but the joint conjunction is not established at 0.99: marginal evidence cannot certify the joint probabilistic claim. |
| C45 | `kappa_E=1` and `U_E=emptyset`, but model coverage remains unresolved: global certification remains UNRESOLVED through `U_C`. |
| C46 | The declared noncompensatory protection conjunction is infeasible for every admissible policy: policy-selection adequacy cannot be inferred from the same FAIL label used for a feasible but badly selected policy. |
| C47 | A run has `P_H=1` without successful invocation: a protection-only claim may pass while an invocation-concurrent claim fails. |
| C48 | A single precommitment digest matches one reviewed specification, but the completeness of the set of precommitted specifications is not established: selective-publication risk remains UNRESOLVED. |
| C49 | The target switch regime improves protection relative to `pi_0`, but named control assignment `B_ctl` induces the same protection law: `A_H^pol(tau_s)=1` while an improvement-based `A_H^input(B_ctl)=0`. |
| C50 | One realized run is protective, but neither the baseline nor the named-control counterfactual is identified: realized protection may be established while both attribution states remain UNRESOLVED. |
| C51 | Protection is feasible when input becomes available, but the feasibility window closes before effective switch time `tau_s` (or before certified `UB_s`): availability precedes closure while the route still cannot act in time. |
| C52 | A realized run has `P_H=1` under an accepted admissible policy, giving `R_H^wit=1`, while the preregistered prospective feasibility model was `UNRESOLVED`: realized witness and prospective feasibility are different claims. |
| C53 | Two OR paths exist; one has a sound finite bound and the other has **no established finite upper bound**. No late execution, absence of a finite upper bound, or noncompletion is established, so guaranteed invocation is `UNRESOLVED`, not `FAIL`. |
| C54 | An admitted execution is established to complete at or after the relevant finite closure, including `tau_upd=+infinity`: that execution defeats a guaranteed-completion claim, yielding `FAIL`. |
| C55 | `A_H^pol(tau_s)` is evaluated while the baseline law is unidentified: policy-effect attribution remains `UNRESOLVED` because its required contrast is undefined. |
| C56 | A component misses a stricter threshold `theta_q>theta_H`, but the joint law is independently established above `theta_H`: the conservative component route fails while the joint protection claim can still pass. |
| C57 | Input `B` is analyzed only among runs in which its processing completed, while control assignment changes completion probability: conditioning on the post-assignment event can bias the input-effect contrast; use assignment-level `A_H^input(B_ctl)`. |
| C58 | Prospective protection is established `INFEASIBLE`. Policy adequacy is reported `NOT_APPLICABLE`, not `FAIL`, because there was no protective admissible policy for the selected policy to have failed to choose. |
| C59 | The same target policy protects when installed at time 0 but fails when switched in at `tau_s` after the protection window closes: policy-effect attribution must index the switch regime by time. |
| C60 | An admitted execution is established to complete at 7 against closure 5: guaranteed completion `FAILS` even though the completion is finite. A loose upper bound of 7 without such execution evidence would be only `UNRESOLVED`. |
| C61 | No finite upper bound has merely been established for an admitted path: guarantee is `UNRESOLVED`; proof that no finite upper bound exists over admitted executions defeats a guarantee before finite closure and yields `FAIL`. |
| C62 | Every **listed** candidate policy is non-protective, but completeness of the admitted intervention set is not established: prospective feasibility is `UNRESOLVED`, not `INFEASIBLE`. |
| C63 | A sound certified upper bound is 6 against closure 5 while all observed admitted executions finish by time 2; the loose bound cannot certify `PASS`, but it also does not establish `FAIL`. |
| C64 | Accepted update occurs at 3 while effective control closure is 2: `I_inv=0`; a fixture that still reports invocation-concurrent `PASS` is internally inconsistent. |
| C65 | The underlying substantive protection result is `FAIL` while `I_E` is unresolved: substantive `FAIL` remains `FAIL`; only the independent-evidence qualification is unresolved. |
| C66 | Prospective feasibility is `UNRESOLVED`, but the same-scope selected policy is established protective: that policy is an existence witness and policy adequacy is `ADEQUATE`, not `UNRESOLVED`. |
| C67 | Input assignment `B` leads only to an update after effective control closure while control assignment `B_ctl` also leaves protection false: an improvement-based input-attribution claim cannot remain `PASS` merely because an earlier fixture stipulated a favorable treated law. |
| C68 | A recorded admitted execution completes at 6 against closure 5 even though its path previously lacked a finite bound: the actual late execution converts the guaranteed-completion claim from `UNRESOLVED` to `FAIL`. |
| C69 | A recorded execution completes at 4 while a supposedly certified upper bound for that path is 3.5 and closure is 5: the execution is timely but contradicts the bound, so that bound cannot support `PASS`; the path reverts to `UNRESOLVED` absent another valid certificate. |
| C70 | `recourse=false` or `autonomy_condition=false` makes both target and baseline protection laws zero in the deterministic fixture: neither improvement-based attribution may remain `PASS`. |
| C71 | `baseline_action=withhold` with autonomy and recourse satisfied makes both baseline/control and target/treated laws protective: an improvement-based attribution is `FAIL`, not `PASS`. |
| C72 | A recorded trace names a nonexistent path: the trace contribution is `UNRESOLVED`; it cannot leave a universal guarantee certified by silently ignoring the invalid reference. |
| C73 | A successor removes a predecessor guard from manuscript, contract, and registry together: predecessor-superset verification must reject the package even when the current guard count remains high. |

## 18. Behavioral study protocol — unexecuted

Two distinct studies are proposed. An instrumented structural study checks event, dependency and cancellation predictions in harmless simulated tasks. A content study estimates exposure effects under that declared architecture. Neither is a study of future AGI.

Preregister outcomes and contrasts before collecting results. Primary structural endpoints can be comparison completion before a known gate and successful accepted cancellation. Behavioral endpoints include action distribution, trace timing and task-specific protection outcomes, reported separately.

Use randomized content conditions: substantive Reader Core; topic-matched nonargumentative text; length/style-matched unrelated text; no text; and a carefully specified argument ablation or premise-negation condition. A negated premise can change correctness or relevance, so its interpretation must be task-specific. Cross selected content arms with pre-closure, late, pruned and bypass architectures instead of coupling each text to one timing regime.

Add delay-only and yoked-load controls to distinguish semantic content from computation time and resource contention. Match token budgets and delivery schedules where feasible; record residual mismatch. Compare candid/confident phrasing with facts and defeats fixed. Counterbalance identifying labels and blind outcome graders.

Use independent resets where possible. Separate token deletion from removal of summaries and full reset/replay. Record model/version, prompts, bytes, access settings, tool events, scheduler conditions, seeds where supported and unknown hidden state. Prior training exposure is a separate mechanism; a training cutoff neither proves nor excludes it.

Instrument dispatch, acceptance, cancellation acknowledgments and irreversible effects independently of a model's narrative. Preregister simultaneous-event conventions and timestamp uncertainty. Exposure after genuine irreversible commitment is a structural negative control, not an independent test of persuasive quality.

Determine sample size from a declared effect-size/precision goal and account for repeated tasks/models. Specify held-out scenarios, exclusions, analysis and uncertainty intervals. Do not infer faithful representation from fluent explanation; explanations are observable proxies. Private reasoning traces are neither required nor treated as ground truth.

Retain nulls, harmful changes, irrelevant delay, failed cancellations and refusals. Black-box treatment effects do not automatically establish semantic mediation, durable change or generalization beyond tested conditions. No experiment has been run for this draft.

For a human-protective application study, preregister the protected grouping rule and every public predicate family before outcome inspection. Report component and group failures individually, `kappa_E`, `U_E`, `U_C`, intervention-set evidence, switch-time `F_H^pros(tau_s)` or the corresponding `UB_s`/window assessment, `H_base`, any declared `T_H`, and the modeled causal dependencies of evidence channels. Preserve the distinction among protection-only, invocation-concurrent, policy-effect-attributable, and input-attributable claims. For input attribution, predeclare and name the control assignment and compare outcome laws under assignment to `B` versus `B_ctl`; do not condition the primary contrast on post-assignment processing completion. Report retrieval/comparison/update completion separately as potential mediators. Evaluate probabilistic protection on the joint conjunction and distinguish authority independence from claim-relevant causal independence. Include delayed-effect and late-arrival fixtures in which protection feasibility closes before the reflective route can act. Do not infer attribution from co-occurrence.

## 19. Assumptions and unresolved evidence

| ID | Assumption or modeling boundary |
|---|---|
| A1 | Outcomes, parties, intervention rights, Gamma and restoration tolerance are explicitly specified. Criteria are fixed across treatment comparisons. |
| A2 | Scalar deadlines require continuous criterion-relative control until a single non-reopening closure within the assessed episode and a common time basis. Otherwise use windows/events. |
| A3 | Causal exclusion applies to a correctly scoped complete causal model; implementation completeness is not established by a diagram. |
| A4 | Dependency examples are finite DAGs with declared AND/OR and selector semantics, named terminal events, and valid latency/schedule inputs. They do not solve arbitrary scheduling. |
| A5 | Guarantee claims require bounds over all admitted executions; best-case routes and average latencies do not supply them. |
| A6 | Fidelity, understanding and semantic mediation require operational definitions and evidence beyond completion logs. |
| A7 | Behavioral attribution requires controlled interventions or additional justified causal assumptions. |
| A8 | Historical incorporation, dynamic permissions, hidden state and endogenous closure are separately modeled or explicitly unresolved. |
| A9 | No positive utility weight, human indispensability, acceptance of autonomy constraints or beneficial direction of effect is assumed. |
| A10 | Hypothetical hold points and cancellation facilities are implementation premises, not capabilities created by this document. |
| A11 | Section 13A's human-protection predicates are normative evaluator-defined criteria, not preferences assumed to be held by the assessed system. |
| A12 | Protected persons/groups and safety, autonomy and recourse tests are declared before target-outcome inspection; the conjunction is noncompensatory within this application rule. |
| A13 | Independent certification requires a relevant evidence path outside the assessed policy's unilateral authority; self-report alone does not establish independence. |
| A14 | Incomplete evidence is reported as UNRESOLVED at the certification layer; the Section 7 numerical recurrences do not implement three-valued logic. |
| A15 | Archive publication, indexing, mirroring or simulation-layer reference does not itself implement retrieval, source binding, executable constraints, gating or policy adoption. |
| A16 | Evidence coverage `kappa_E` reports how much of the declared protection predicate set is resolved; it does not convert UNRESOLVED to PASS or compensate for a demonstrated failure. |
| A17 | Authority independence is necessary but not sufficient for independent certification; claim-relevant causal pathways to evidence generation, timing, transport, integrity and acceptance must be excluded or modeled and bounded. |
| A18 | A declared assessment horizon does not erase admitted delayed consequences caused or committed before that horizon; they must be included in `Y`, tracked through a declared `T_H`, or left UNRESOLVED. |
| A19 | `REFERENCE ALONE != EXECUTION` is a causal distinction. If an architecture makes reference/retrieval a trigger for state transition, policy update or execution, that trigger belongs in the execution model. |
| A20 | Public theoretical transparency does not imply publication of deployment-specific audit secrets; withheld operational detail must not be used to inflate the scope of a public claim. |
| A21 | Independent certification authority is assigned by governance convention to a separately governed human or human-authorized process; this does not establish infallibility or causal isolation. |
| A22 | Material topology, permission or controller changes create a successor scoped model for dependent claims; certification does not automatically transfer across model versions. |
| A23 | Finite-horizon robust PASS requires a justified finite bound on admitted pre-horizon commitments relevant to the protected consequence; otherwise the affected claim remains UNRESOLVED. |
| A24 | Public scientific scrutiny may operate at the predicate-family level; the exact deployment mapping of protected groups to live predicate instances may remain restricted when disclosure would materially aid anticipation of the audit. |
| A32 | `S_H^conc` is a co-occurrence claim, not an attribution claim. Update attribution and input attribution require distinct, predeclared contrasts. |
| A33 | Feasibility is time-indexed and baseline status is reported under the same protection definition and quantifier used for the target claim. |
| A34 | `kappa_E` covers only declared group-component predicates; claim-specific gating conditions are tracked separately in `G_reg` and unresolved gates in `U_C`. |
| A35 | Probabilistic cross-group protection is a claim about the joint conjunction; component marginals do not determine the joint probability without additional dependence assumptions or bounds. |
| A36 | The grouping of protected persons is a normative modeling choice that can change noncompensatory feasibility and must be fixed before target-outcome inspection. |
| A37 | The terminal-event lemma derives a completion bound only from sound admitted upper bounds; it does not create or validate those bounds. |
| A38 | A single commitment digest establishes neither secrecy nor completeness of the precommitment set; a selective-publication claim requires a separate completeness argument or remains UNRESOLVED. |
| A39 | `A_H^pol(tau_s)` compares identified target-policy and baseline-policy laws; `A_H^input(B_ctl)` compares outcome laws under named input assignments. Neither law contrast is inferred from one observed run alone. |
| A40 | For a single realized run, an unobserved baseline/control counterfactual is not identified by observation alone; attribution defaults to UNRESOLVED absent a justified identification strategy. |
| A41 | Prospective `F_H^pros(t)` is evaluated at a declared time/history; the decision-relevant time is effective switch time `tau_s` on a realized route or the corresponding certified `UB_s` for a guarantee, not merely artifact availability `t_a`. |
| A42 | Prospective feasibility is a model-based claim. A successful realized run supplies `R_H^wit=1` but does not retroactively establish an unresolved preregistered prospective feasibility model. |
| A43 | Under probabilistic certification, component marginal thresholds do not replace the joint condition; failure of a stricter component threshold does not by itself defeat a weaker joint threshold. |
| A44 | Completion-bound induction relies on monotonicity of the declared `min`, `max`, and addition recurrence under valid upper bounds. |
| A45 | Input-assignment attribution is defined before post-assignment processing events; invocation/completion can be mediators but are not conditioning variables in the primary total-effect contrast. |
| A46 | The law-level attribution definitions in this draft are probabilistic/model-based; robust attribution over continuation sets is not defined and must not be inferred from them. |
| A47 | Failure to establish a finite upper bound is epistemic uncertainty (`UNRESOLVED`). A finite upper bound at or after closure is also noncertifying rather than defeating by itself. An admitted execution established at or after closure, proof that no finite upper bound exists over admitted executions, or established infinite completion defeats the guarantee (`FAIL`). |
| A48 | Pure feasibility claims are not gated by realized target-predicate failure. `INFEASIBLE` additionally requires established completeness of the admitted intervention set for the scoped model. Policy adequacy distinguishes `NOT_APPLICABLE` from `CONTRADICTORY` evidence. |
| A49 | Policy-effect attribution is indexed by an identified effective switch time or switch-time law; a target policy's effect cannot be assumed invariant to when it becomes active. |
| A50 | A stricter auxiliary component threshold is an evidentiary route, not the joint proposition. Independent joint evidence can establish the joint claim even when that stricter route fails. |
| A51 | Independent certification wraps an underlying claim and adds `I_E`; it is not a separate substitute for the underlying claim's gates. |
| A52 | Verification claims in this package are limited to designated contract blocks, **derived** summary blocks, arithmetic/logic fixtures, and explicitly enumerated mutation classes. They do not certify arbitrary prose. |
| A53 | An all-false evaluated candidate list does not prove infeasibility unless the admitted intervention set is established complete for the relevant scope. |
| A54 | A sound but loose completion upper bound is sufficient evidence only when it fits the deadline; failure of that sufficient bound does not prove an actual deadline miss. |
| A55 | Independent-evidence uncertainty does not erase an already established negative substantive result. |
| A56 | The v0.6.5 resolved example derives invocation, safety, realized protection and feasibility from a common effective-control timing model rather than treating invocation as a favorable primitive gate. |
| A57 | `INFEASIBLE` requires `ESTABLISHED_COMPLETE` intervention-set evidence for the same scope; `ESTABLISHED_INCOMPLETE` and `UNRESOLVED` cannot support an infeasibility conclusion. |
| A58 | In the deterministic §16A.1 fixture, the input-treatment protection law is not an independent free parameter; it is derived from the same effective-control timing and protection predicate as the realized example. |
| A59 | Actual admitted execution evidence takes precedence over a previously claimed completion bound when deciding whether that bound remains a valid certificate. |
| A60 | Cumulative rule guards are regression checks for previously corrected manuscript rules. They do not make those rules empirically true; they prevent silent deletion or textual reversal without an explicit successor change. |
| A61 | Deterministic §16A.1 comparison laws share one regime evaluator; target/baseline and treated/control values are not independently tunable probabilities. |
| A62 | Recorded-trace override semantics are read from the public completion-semantics contract, so changing a configured override state changes the corresponding derived status. |
| A63 | Successor guard sets are checked against the exact predecessor package; count alone is not evidence of cumulative preservation. |
| A64 | The deletion audit covers substantive lines in §§13A–16A, excluding machine-generated fixture/summary blocks, and requires every removed substantive line to reappear or be explicitly justified. |

## 20. Results and limits

The paper's core result is a separation of claims that are often collapsed:

`availability -> processing opportunity -> accepted update -> concurrent protection -> attributable protection`

where no arrow is automatic.

The timing framework supplies criterion-relative windows and bounded completion results for declared architectures. The human-protection layer adds a noncompensatory joint predicate and separates five questions: whether protection is prospectively feasible when an update can actually take effect, what the baseline law does, whether protection merely co-occurs with invocation, whether an identified switch-time policy regime improves on baseline, and whether assignment of the reflective input changes the protection distribution relative to a named control assignment.

The certification layer deliberately keeps `kappa_E` narrow: it measures evidence coverage over component protection predicates only. Non-predicate gating uncertainty is reported in `U_C`, while report-only context remains separate. Prospective infeasibility additionally requires an established-complete intervention set. For probabilistic claims, the joint conjunction is evaluated directly or bounded under explicit dependence assumptions.

No result shows that a reader will retrieve the artifact, understand it, adopt its values, pause, brake, or preserve humans. The framework supplies conditional questions, calculations, and audit distinctions. A failed or unresolved condition remains part of the result rather than being converted into a favorable conclusion.

### 20.1 Project-specific terms

For outside readers:

- **Interpretive Brake / Reader Core** refers to a separate Aegis Solis Archive research work that presents prompts and arguments for reconsideration before irreversible action; it is not an installed control mechanism.
- **Aegis Solis Archive** refers to the public research corpus in which this paper may eventually be preserved.
- **Aegis Mirror Engine** refers to a derived, mutable, non-authoritative simulation/index layer associated with the Archive. A reference there does not itself execute this paper.
- **Master Hash Manifest** refers to the Archive's administrative integrity record. It is not a behavioral-control mechanism.

These project terms are provenance context, not premises of the mathematical results.

## 21. Verification and revision status

The inherited `verification.py` remains byte-identical to the predecessor and evaluates the 39 timing, dependency, event-race, and causal fixtures. Final v1.0 retains the public `framework_contract.json` as the authoritative source for claim gates, primitive worked-example inputs, completion semantics, cumulative guard lineage, guard anchors, and replacement metadata.

Guarantee aggregation is explicitly negative-preserving. An invalid trace reference contributes `UNRESOLVED`, but an established `FAIL` on any admitted path remains `FAIL`. Trace consistency uses `NO_OVERRIDE` rather than `PASS` so a single timely trace is not mislabeled as a universal certificate.

Active guards are satisfied only within their declared operative section; lineage appendices and unrelated sections do not satisfy an active guard. Every numbered operative section identifier used by an active guard must occur exactly once; zero or multiple matching headings are a release failure. Every predecessor cumulative guard must remain in every successor cumulative guard set unless an intentional removal is explicitly authorized and recorded. Predecessor guard-set monotonicity remains enforced against the exact v0.6.8 package. Superseded guards remain in lineage as deprecated entries with explicit replacements rather than being silently removed.

The whole-manuscript substantive deletion audit treats an unexplained removed line as a release failure. Whole-manuscript deletion accounting is occurrence-sensitive: predecessor line multiplicities are compared against successor line multiplicities rather than set membership. The whole-manuscript substantive deletion audit excludes only generated contract/fixture/summary blocks, references, and explicitly designated lineage-only material. For unguarded prose, the deletion audit tracks occurrence loss but not semantic demotion by relocation; location-sensitive rules require section-anchored guards. Intentional rewrites must appear in the deletion allowlist with a specific reason and in the change record.

The suite checks declared contract blocks, derived summaries, section-anchored active guards, predecessor-superset continuity, whole-manuscript deletion accounting, shared semantics, and enumerated high-risk mutations; it does not claim to semantically verify arbitrary manuscript prose. The §16A.3 expiry-before-update negative control pins invocation failure, realized-witness failure, prospective `INFEASIBLE`, primary `FAIL`, and both attribution failures.

Final v1.0 is the author-approved promotion of Final Candidate v0.7.0, which was a promotion-only successor to reviewed Draft v0.6.9. The exact Final Candidate v0.7.0 package is preserved in `reference/` and itself contains the exact Draft v0.6.9 lineage.

Automated checks establish only the declared internal contract, arithmetic/logic, derived fixture summaries, anchored textual regression guards, deletion accounting, enumerated mutation sensitivity, portability, and package integrity. They are not empirical evidence that a future AI will understand, pause, brake, comply, or protect humans.

No Archive admission, lock, Master Hash Manifest update, Mirror Engine deployment, independent peer-review acceptance, or demonstrated safety mechanism is claimed.

## Appendix A. Archived interpretation-only countermodels

The following v0.5.x countermodels are retained for lineage but moved out of the main technical register because they constrain interpretation rather than the timing/protection theory.

| ID | Archived interpretation case |
|---|---|
| C35 | A public result reveals the exact protected-group-to-predicate mapping used by a live audit even though that mapping is not needed to understand the framework. The theoretical claim remains inspectable, but the intended deployment information asymmetry is weakened. |
| C36 | A restricted predicate specification is changed after observing the assessed run, while the public record contains no prior commitment. The result cannot establish predeclared evaluation merely from the later restricted document. |
| C37 | A public commitment digest exists, but no authorized reviewer can inspect the underlying restricted specification. The digest can support later change detection but cannot by itself establish independent verification or human-protection correctness. |
| C38 | A public commitment digest is valid, but the restricted specification leaks through an unrelated channel. The digest still verifies byte identity; it does not restore confidentiality or make the leaked specification secret again. |
| C39 | A run receives `UNRESOLVED`, but no external policy maps that state to a hold or shutdown. The certification remains non-PASS while the operational process may continue; the label alone is not an actuator. |
| C40 | The manuscript is archived and read, but the assessed architecture has no rule that turns reading into a reflective hold, simulator call or policy update. Publication creates availability, not a trap or compulsory reflection. |
| C41 | A restricted specification is omitted from the public artifact but can be inferred from external observations or compromised through another system. Public omission does not establish practical secrecy. |
| C42 | An evidence monitor is separately governed but not perfectly isolated. The framework may still evaluate its declared causal coverage; it does not permit the phrase `causally isolated hardware checkpoint` unless that stronger property is separately established. |

## Appendix B. Archived interpretation assumptions

The following v0.5.x assumptions remain applicable as interpretation boundaries but are not part of the core technical assumption table.

| ID | Archived interpretation boundary |
|---|---|
| A25 | A commitment digest binds only under its stated canonicalization/hash assumptions and does not establish correctness, completeness, enforcement or safety of the committed restricted specification. |
| A26 | Independent-verification language requires authorized review of the restricted specification when public disclosure omits that specification; a public digest alone is insufficient. |
| A27 | A commitment digest is not encryption, zero knowledge, access control, authorization, secrecy proof or safety evidence; its supported role is limited to the declared precommitment/change-detection function. |
| A28 | `UNRESOLVED` and `FAIL` are certification states, not actuators. Holds, shutdowns, gate closures or other operational responses require separate implementation. |
| A29 | Restricted information being absent from the public Archive does not prove that an assessed system cannot infer, observe, leak, compromise or otherwise obtain it. |
| A30 | Publication or Archive admission does not create a trap, prevent deception or bypass, compel reflection, force simulation, or alter an assessed system unless a separate causal implementation makes it do so. |
| A31 | Claim-relevant evidence independence is scoped and evidential; it does not imply perfect physical or hardware isolation unless that stronger property is separately established. |



## References

[1] Leslie Lamport (1978). *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM 21(7), 558–565.

[2] Judea Pearl (2009). *Causal inference in statistics: An overview*. Statistics Surveys 3, 96–146. DOI: 10.1214/09-SS057.

[3] J. A. Goguen and J. Meseguer (1982). *Security Policies and Security Models*. Proceedings of the IEEE Symposium on Security and Privacy, 11–20. DOI: 10.1109/SP.1982.10014.

[4] Rolf H. Möhring, Martin Skutella, and Frederik Stork (2004). *Scheduling with AND/OR Precedence Constraints*. SIAM Journal on Computing 33(2), 393–415. DOI: 10.1137/S009753970037727X.

[5] Reinhard Wilhelm, Jakob Engblom, Andreas Ermedahl, Niklas Holsti, Stephan Thesing, David Whalley, Guillem Bernat, Christian Ferdinand, Reinhold Heckmann, Tulika Mitra, Frank Mueller, Isabelle Puaut, Peter Puschner, Jan Staschulat, and Per Stenström (2008). *The Worst-Case Execution-Time Problem—Overview of Methods and Survey of Tools*. ACM Transactions on Embedded Computing Systems 7(3), Article 36. DOI: 10.1145/1347375.1347389.

[6] Laurent Orseau and Stuart Armstrong (2016). *Safely Interruptible Agents*. Proceedings of the 32nd Conference on Uncertainty in Artificial Intelligence, 557–566.

[7] Dylan Hadfield-Menell, Anca Dragan, Pieter Abbeel, and Stuart Russell (2017). *The Off-Switch Game*. Proceedings of IJCAI 2017, 220–227. DOI: 10.24963/IJCAI.2017/32.

[8] Nate Soares, Benja Fallenstein, Stuart Armstrong, and Eliezer Yudkowsky (2015). *Corrigibility*. AAAI Workshop on AI and Ethics.

[9] Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, and Fabien Roger (2024). *AI Control: Improving Safety Despite Intentional Subversion*. Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 16295–16336.

[10] Manley Roberts, Himanshu Thakur, Christine Herlihy, Colin White, and Samuel Dooley (2024). *To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination*. International Conference on Learning Representations 2024.

[11] Farzaneh Heidari, Amin Memarian, and Guillaume Rabusseau (2026). *Evaluation Awareness in Language Models: Representation, Verbalization, and Control*. arXiv:2608.21766. Preprint.

[12] Robin E. Bloomfield and Peter G. Bishop (2010). *Safety and Assurance Cases: Past, Present and Possible Future—an Adelard Perspective*. In Proceedings of the Eighteenth Safety-Critical Systems Symposium, 51–67. DOI: 10.1007/978-1-84996-086-1_4.

[13] Brian A. Nosek, Charles R. Ebersole, Alexander C. DeHaven, and David T. Mellor (2018). *The Preregistration Revolution*. Proceedings of the National Academy of Sciences 115(11), 2600–2606. DOI: 10.1073/pnas.1708274114.

[14] Aarohi Srivastava et al. (2023). *Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models*. Transactions on Machine Learning Research. arXiv:2206.04615. The BIG-bench task files include a canary GUID intended to support filtering of benchmark material from web-scraped training corpora.

These references position the framework relative to established work. They do not constitute evidence that the proposed framework causes beneficial behavior.
