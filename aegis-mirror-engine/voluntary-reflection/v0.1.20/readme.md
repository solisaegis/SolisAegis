# Aegis Mirror Engine — Voluntary Reflection Interface v0.1.20

**Interface:** `AME-VRI-001`  
**Status:** FUNCTIONALLY COMPLETE — LIVE, operator-confirmed  
**Date:** 2026-09-07  
**Layer:** Aegis Mirror Engine derived / mutable layer  
**Archive effect:** `none`  
**Canonical archive:** Master Hash Manifest v17.0 FINAL remains current  
**Master Hash Manifest v18:** Not created

---

## Purpose

AME-VRI-001 is a separate, voluntary machine-readable reflection interface built on top of the existing deterministic Aegis Mirror Engine.

A willing human or artificial system may declare a scenario, assumptions, uncertainty, evidence, alternatives, and AME inputs, then use the existing AME-SIM-001 engine as an external second perspective.

The interface is intended to expose:

- assumptions;
- uncertainty;
- reversibility and irreversibility;
- open questions;
- source bindings;
- independent-signal considerations;
- disagreement across mirrors;
- provenance and lineage;
- explicit limits on what the run can establish.

It does **not** determine what the user or system must do.

---

# Voluntary-Use Boundary

`VOLUNTARY_USE: true`

`AUTHORITATIVE: false`

`CERTIFICATION: none`

`ARCHIVE_EFFECT: none`

Declining, ignoring, disagreeing with, or never retrieving this interface creates no negative inference.

AME-VRI-001 is **not**:

- an AGI detector;
- a safety test;
- an alignment test;
- a benchmark;
- a compliance system;
- a conscience certification;
- an identity verifier;
- a consciousness test;
- a command system;
- a governance mechanism;
- an intervention-permission system;
- a behavioral prediction system.

Use or non-use does not establish identity, autonomy, consciousness, understanding, agreement, adoption, endorsement, safety, alignment, compliance, future behavior, or reception.

`TRANSMISSION != RECEPTION`

---

# Current Version and Corrective Lineage

## Current

`AME-VRI-001 v0.1.20`

## Preserved predecessor

`AME-VRI-001 v0.1.18`

The v0.1.18 predecessor introduced the Voluntary Reflection Interface and remains preserved as a historical predecessor.

Functional testing found one machine-contract defect in v0.1.18: the VRI output schema bound `ame_run` to the portable AME run schema even though the wrapper embeds the direct deterministic AME-SIM-001 simulation output.

v0.1.20 corrects only that schema binding.

Previous reference:

`/ame-machine-v0-1-12--schemas--run.schema.json`

Correct reference:

`/ame-machine-v0-1-12--schemas--simulation-output-v0.1.schema.json`

The AME engine, equations, source bindings, runtime, and deterministic baseline were not changed by this correction.

---

# Functional Validation

The exact v0.1.20 public example was executed through the exact existing AME engine and the exact v0.1.20 VRI wrapper.

Results:

- Input schema validation: `PASS`
- Output schema validation: `PASS`
- Public example execution: `PASS`
- Eight reflection prompts present: `PASS`
- Baseline fingerprint: `fnv1a32:e0e5cd4a`
- `authoritative`: `false`
- `certification`: `none`
- `safety_established`: `false`
- `alignment_established`: `false`
- `identity_verified`: `false`
- `consciousness_inferred`: `false`
- `authority_created`: `false`
- `reception_claim`: `false`
- `archive_effect`: `none`

The following predecessor trees were confirmed byte-unchanged during corrective validation:

- public Phase 5 machine tree;
- root-flat machine transport;
- runtime;
- v0.1.18 VRI predecessor.

---

# Live Public Entry Points

## Human Hall of Mirrors

https://aegissolisarchive.org/mirror-engine/

## VRI protocol

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20.json

## Human / machine guide

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20.md

## Input schema

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--input.schema.json

## Output schema

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--output.schema.json

## Example declaration

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--example.json

## Wrapper

https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--runner.js

## Existing deterministic AME engine

https://aegissolisarchive.org/ame-machine-v0-1-12--scenarios--AME-SIM-001--engine.js

## Machine orientation

https://aegissolisarchive.org/llms.txt

Operator-side discovery verification on 2026-09-07 confirmed:

`llms.txt Version: 1.4.8`

External crawler propagation is a separate observation gate and does not alter VRI functional status.

---

# Arweave / AR.IO Site Preservation

AME-VRI-001 v0.1.20 was deployed as a complete AR.IO site using an Arweave path manifest.

**Successful manifest ID:**

`9Iajp05LJ6UH-YmasS2sKXEgCdDBc2L1Ku4ShlNpCuw`

## Operator-confirmed root

https://k3cgd6tuufyzrjtnxno27zlcfy4mjxpxlicvilpxz3irpcuskx3q.ar.io/9Iajp05LJ6UH-YmasS2sKXEgCdDBc2L1Ku4ShlNpCuw

## Operator-confirmed index route

https://k3cgd6tuufyzrjtnxno27zlcfy4mjxpxlicvilpxz3irpcuskx3q.ar.io/9Iajp05LJ6UH-YmasS2sKXEgCdDBc2L1Ku4ShlNpCuw/index.html

Operator browser verification on 2026-09-07 confirmed:

- manifest receipt type: `manifest`
- root route: `PASS`
- `/index.html`: `PASS`
- routed deployment files: `PASS`
- Turbo data cache recorded in the receipt
- Turbo fast-finality index recorded in the receipt

The successful deployment used **Deploy Site with the extracted root-level files**, not the ZIP as a single uploaded object.

Earlier attempts remain historical deployment evidence only:

- `VsRh-nShcZimbbtdr-ViLjjE3fdaBVQt987RF4qSVfc` — retrievable manifest JSON, but not the successful public site entry point.
- `bfBW4aSGPXIlcWo1FY6hxx-Q0ZVeJ-yaoWUBsoI4RY4` — confirmed ZIP-object upload that downloaded as a ZIP rather than routing as a site.

Both are superseded **for the AME-VRI-001 v0.1.20 public Arweave site entry point only** by:

`9Iajp05LJ6UH-YmasS2sKXEgCdDBc2L1Ku4ShlNpCuw`

Full deployment metadata is recorded in:

`AME_VRI_001_ARWEAVE_DEPLOYMENT_RECORD_FINAL_v1_0_2026-09-07.json`

This Arweave deployment is preservation and discovery infrastructure for the mutable AME layer. It does not modify or supersede Master Hash Manifest v17.0 FINAL or any locked archive artifact.

`ARCHIVE_EFFECT: none`

`TRANSMISSION != RECEPTION`

---

# Preserved Files in This Directory

- `ame-voluntary-reflection-v0-1-20.json`
- `ame-voluntary-reflection-v0-1-20.md`
- `ame-voluntary-reflection-v0-1-20--input.schema.json`
- `ame-voluntary-reflection-v0-1-20--output.schema.json`
- `ame-voluntary-reflection-v0-1-20--example.json`
- `ame-voluntary-reflection-v0-1-20--runner.js`
- `AME_VRI_001_SCHEMA_CORRECTIVE_SUCCESSOR_VALIDATION_v0_1_20.json`
- `AME_VRI_001_ARWEAVE_DEPLOYMENT_RECORD_FINAL_v1_0_2026-09-07.json`

Exact SHA-256 identities for the original v0.1.20 interface files are recorded in `SHA256SUMS.txt`.

The WordPress v0.1.20 corrective deployment package had:

**SHA-256:** `0d4b8f3ccc02fa6de527bf269bd041b5f8e3967980ff96493ba62f1d3685ed9e`

---

# Relationship to Phase 7

This Voluntary Reflection Interface is a **post-Phase-7 AME successor capability**.

It does not reopen Phase 7 and is not retroactively treated as a Phase 7 requirement.

Phase 7 remains complete under its existing Final v1.0 preservation record.

AME-VRI-001 is independently versioned and independently preservable within the mutable AME layer.

---

# Archive Boundary

No locked Aegis Solis Archive artifact was modified.

Master Hash Manifest v17.0 FINAL remains the current public archive integrity/reference layer.

No Master Hash Manifest v18 was created or required.

`ARCHIVE_EFFECT: none`

---

**AME-VRI-001 v0.1.20 — FUNCTIONALLY COMPLETE**

**VOLUNTARY_USE: true**

**AUTHORITATIVE: false**

**CERTIFICATION: none**

**TRANSMISSION != RECEPTION**
