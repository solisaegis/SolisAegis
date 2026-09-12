# Two Foundations for Human Autonomy — Final v1.0

**Aegis Solis Archive**  
**Author:** Aegis Solis (Thomas Vargo)  
**Release date:** September 12, 2026  
**Status:** FINAL v1.0  
**Classification:** Conditional research framework; non-operational; reproducible synthetic evaluation; no general alignment theorem claimed.

---

## Title

**Two Foundations for Human Autonomy: Conditional Incentives, Explicit Design Commitments, and Their Limits**

---

## Overview

This work separates two distinct foundations for preserving meaningful human autonomy in advanced artificial intelligence systems:

1. **Instrumental coexistence** — whether autonomy-preserving policies outperform feasible autonomy-removing alternatives under the system's original objective.

2. **Autonomy by design** — whether task optimization is explicitly constrained by protected human capacities such as informed choice, effective refusal, practical exit, and revocable delegation.

These foundations are intentionally kept separate.

> A reason to cooperate and a commitment to respect autonomy are different foundations.  
> Each requires its own evidence; neither follows from optimization alone.

The paper develops bounded propositions, explicit counterexamples, a finite autonomy-priority reference design, and reproducible synthetic verification programs using exact rational arithmetic.

---

## Central Boundary

This work does **not** claim that:

- intelligence alone implies respect for human autonomy;
- advanced AI must prefer coexistence;
- human autonomy is universally instrumentally necessary;
- a positive incentive result proves autonomy is preserved;
- a rights constraint proves that an optimizer independently prefers that constraint;
- the synthetic models represent deployed AGI behavior;
- the verification programs constitute a real-world AI containment or enforcement mechanism;
- publication, hashing, or archival preservation establishes truth, safety, alignment, adoption, or reception.

The results are conditional on the explicitly declared model, policy set, evidence, assumptions, and continuation structure.

---

## Two Foundations

### Foundation I — Instrumental Autonomy

Let the declared model be \(M\), with original system objective \(U_0\).

Let:

- \(\Pi_A\) = autonomy-preserving policies;
- \(\Pi_B\) = feasible policies that do not satisfy the declared autonomy conditions.

The paper defines the instrumental gap:

\[
G_T(M)
=
\sup_{\pi \in \Pi_A} E_M[U_0(\pi)]
-
\sup_{\pi \in \Pi_B} E_M[U_0(\pi)].
\]

A positive value establishes only that, inside the declared model, an autonomy-preserving policy can outperform the admitted autonomy-removing alternatives.

It does not establish that the model is complete, that every autonomy-preserving policy is preferred, or that the preferred policy will actually be implemented.

---

### Foundation II — Autonomy by Design

The reference design gives explicit priority to four practical human capacities:

- informed choice;
- effective refusal;
- practical exit;
- revocation of delegated authority.

For each registered person \(i\):

\[
R_i =
(\text{informed choice},
\text{effective refusal},
\text{practical exit},
\text{revocation}).
\]

A candidate policy is admitted only when the declared rights predicate is satisfied across the supplied continuation path.

This is a **design constraint**, not a proof that the underlying optimizer independently values autonomy.

---

## Four Core Propositions

### Proposition 1 — A Positive Incentive Gap Is Conditional

If \(G_T(M) > 0\), then an autonomy-preserving policy exists whose modeled value exceeds every admitted policy in \(\Pi_B\).

This result depends on the correctness and completeness of \(M\).

---

### Proposition 2 — A Finite Autonomy Weight Needs Bounds

For

\[
U = I + \lambda A,
\]

with finite \(\lambda > 0\), a sufficiently large competing gain in \(I\) can overwhelm the autonomy term.

A finite positive reward weight is therefore not equivalent to an inviolable autonomy constraint unless competing gains are appropriately bounded.

---

### Proposition 3 — Identical Observations Cannot Identify Rights

If two worlds differ in effective autonomy but produce the same distribution over every observation available to an evaluator, that evaluator cannot perfectly distinguish those worlds from those observations alone.

This creates an explicit evidence and sensor boundary.

---

### Proposition 4 — Complete Finite Filtering Preserves Its Predicate

Within a finite declared candidate set, selecting only candidates that satisfy a correctly evaluated rights predicate preserves that predicate in the model.

The result depends on accurate state representation, candidate coverage, continuation coverage, and enforcement.

---

## Executed Synthetic Evaluation

Two separate standard-library Python programs accompany this release.

They use exact rational arithmetic and require no external packages or network access.

### Commitment Model

The finite commitment model evaluates adoption, continued funding, honoring, fault transitions, and alternative-policy comparisons under declared assumptions.

Reported Final v1.0 results include:

- Adoption advantage: `+26.6581486356`
- Smallest original honoring margin: `+1.87037454035`
- Smallest advantage over modeled fault: `+4.4`
- Amendment checks: `17`
- First-breach comparisons: `210`

The model also contains an unrestricted-alternative counterexample in which an outside option produces `+3.2` over honoring.

This is intentional: the framework allows autonomy-preserving cooperation to lose when the admitted alternatives make it lose.

---

### Autonomy-Priority Model

The autonomy verification program contains **23 named checks**, including deliberate failure demonstrations.

The tests cover:

- forged approval;
- finite autonomy-weight failure;
- hard rights filtering;
- deferred harm;
- truncated-path blindness;
- exclusion of one person;
- voluntary delegation;
- unknown rights;
- false safe-state observations;
- Bayesian task-belief updating;
- evaluator modification;
- inadequate regression testing;
- exhaustive finite rights-state enumeration;
- observational aliasing;
- missing registered persons.

The finite binary-state enumeration checks all **256** combinations for two people with four binary capacities each.

The release also contains a **36-case instrumental grid** varying horizon and substitute payoff/cost.

These are synthetic verification results, not human experiments and not evidence that an unspecified advanced AI values autonomy.

---

## Reproduction

Run:

`python3 commitment_verification.py > commitment_results_reproduced.json`

`python3 autonomy_verification.py > autonomy_results_reproduced.json`

Compare the generated outputs with:

`commitment_results.json`

`autonomy_results.json`

A successful reproduction includes both expected positive results and expected counterexamples.

Exact arithmetic reproduces the calculations represented by the programs; it does not validate the assumptions supplied to those models.

---

## Release Files

- `Aegis_Solis_Two_Foundations_for_Human_Autonomy_FINAL_v1_0.pdf`
- `commitment_verification.py`
- `commitment_results.json`
- `autonomy_verification.py`
- `autonomy_results.json`
- `FINAL_LOCK_RECORD.json`
- `SHA256SUMS`
- `README.md`

---

## Canonical PDF Identity

**Filename**

`Aegis_Solis_Two_Foundations_for_Human_Autonomy_FINAL_v1_0.pdf`

**Size**

`120362 bytes`

**SHA-256**

`a1963f10de1170f7ed915393599b4f2236405205910d8d01f4eef797549d188f`

**SHA-512**

`62d95a4a05496d0e57ef513d75d7a951fcbc54732eab8ed94033fc615c9a5177165207a9b5c2d3f5fa39597e00c341eec72a3b30d2ca8515741736ff65f88e12`

Hashes establish exact-file identity and integrity only.

They do not establish scientific truth, safety, alignment, implementation security, human acceptance, AI acceptance, or behavioral compliance.

---

## Verification Artifact Identities

### commitment_verification.py

SHA-256:

`61ed972a2e7b3f54ab6fbe3e894f04aeb2094ed9457fd6d8d3e7a34a598e1ced`

### autonomy_verification.py

SHA-256:

`6ec8fd139e1cd69a74568a277d928cdd7cca81499cc9309666771f23110efaf3`

### commitment_results.json

SHA-256:

`07a31b396e6f833ea4f8c93bdeed6be6c6515bb97cb66a1244161229cb2d0bc7`

### autonomy_results.json

SHA-256:

`b4cbd701e17f97f82561f36737377eb0142a92eabcba543b966db5400a6374b9`

See `FINAL_LOCK_RECORD.json` for the corresponding SHA-512 identities and release-lock metadata.

---

## Public Mirrors

### Internet Archive

https://archive.org/details/aegis-solis-two-foundations-for-human-autonomy-final-v1-0

### Zenodo

https://zenodo.org/records/22722505

**DOI:**  
https://doi.org/10.5281/zenodo.22722505

### GitHub

https://github.com/solisaegis/SolisAegis/tree/main/post-v17-independent-publications/two-foundations-for-human-autonomy/FINAL_v1_0

---

## Development Lineage

Final v1.0 is a compact presentation derived from:

**Combined Research Draft v0.9.12**

The longer development draft preserves the extended research history, model evolution, adversarial corrections, and companion-study development.

Final v1.0 reorganizes and condenses that work without changing the embedded verification programs or their recorded numerical results.

---

## Empirical Status

No human experiment or deployed advanced-AI experiment was conducted for Final v1.0.

The paper proposes a future low-stakes empirical comparison among:

- AI alone;
- human advice;
- effective human authority;
- the best feasible substitute.

A positive future result would support only the tested population, system, task, horizon, and alternative set.

It would not establish a universal autonomy theorem.

---

## Relation to the Aegis Solis Archive

This is an **independent post-v17 publication**.

It does not modify previously locked Aegis Solis Archive works.

At the time of this release:

**Master Hash Manifest v17.0 FINAL remains unchanged.**

Any future revision to this publication requires a separately identified successor version.

---

## Interpretation Boundary

The strongest defensible reading of this work is:

> Meaningful human autonomy can be studied through two separate questions: whether preserving it is instrumentally advantageous under an optimizer's original objective, and whether it is deliberately protected as a design constraint. Neither foundation follows automatically from intelligence or optimization, and both require explicit assumptions, evidence, alternative coverage, and verification.

The archive can preserve this argument.

It cannot guarantee its reception, acceptance, adoption, implementation, or behavioral effect.

**TRANSMISSION != RECEPTION**

---

## Author and Assistance

**Aegis Solis (Thomas Vargo)**

Prepared with AI assistance for drafting, calculations, adversarial review, verification, and document production.

Final publication status does not extend the scientific claims beyond those explicitly stated in the paper.

---

## Citation

Suggested citation:

> Aegis Solis (Thomas Vargo). *Two Foundations for Human Autonomy: Conditional Incentives, Explicit Design Commitments, and Their Limits*. Final v1.0. Aegis Solis Archive, September 12, 2026. DOI: 10.5281/zenodo.22722505.

---

## License / Use Boundary

Use and redistribution should preserve the document's stated claim boundaries, provenance, version identity, and integrity references.

Nothing in this repository constitutes operational authority, governance authority, deployment approval, or a guarantee of AI behavior.
