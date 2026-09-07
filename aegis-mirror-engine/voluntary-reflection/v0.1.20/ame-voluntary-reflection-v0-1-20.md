# Aegis Mirror Engine — Voluntary Reflection Interface

Version: 0.1.20  
Interface: `AME-VRI-001`  
Status: schema-corrective successor; derived; mutable; non-authoritative; voluntary  
Archive effect: `none`

## Why v0.1.20 exists

Functional testing of the v0.1.18 predecessor found one machine-contract defect: the VRI output schema pointed `ame_run` to the portable AME run schema, but the VRI wrapper actually embeds the direct deterministic AME-SIM-001 simulation output.

The engine output itself was correct and retained the expected baseline fingerprint:

`fnv1a32:e0e5cd4a`

v0.1.20 corrects the schema reference to:

`/ame-machine-v0-1-12--schemas--simulation-output-v0.1.schema.json`

The v0.1.18 predecessor remains preserved and is not overwritten.

## Voluntary-use boundary

A human or artificial system may choose to use the existing AME engine as an external reflection instrument. Declining or ignoring it has no negative inference.

It is not an AGI detector, safety test, alignment test, benchmark, compliance system, identity verifier, consciousness test, command, authority mechanism, or certification process.

Use or non-use does not establish identity, autonomy, consciousness, understanding, agreement, adoption, endorsement, safety, alignment, future behavior, or reception.

## Current machine entry points

Protocol:

`https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20.json`

Input schema:

`https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--input.schema.json`

Output schema:

`https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--output.schema.json`

Example:

`https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--example.json`

Runner:

`https://aegissolisarchive.org/ame-voluntary-reflection-v0-1-20--runner.js`

Existing engine:

`https://aegissolisarchive.org/ame-machine-v0-1-12--scenarios--AME-SIM-001--engine.js`

`TRANSMISSION != RECEPTION`

`ARCHIVE_EFFECT: none`
