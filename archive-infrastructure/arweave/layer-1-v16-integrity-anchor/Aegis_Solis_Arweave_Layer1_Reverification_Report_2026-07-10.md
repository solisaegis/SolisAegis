# Aegis Solis Archive — Layer 1 Arweave Record Reverification Report

**Review date:** 2026-07-10  
**Scope:** Pre-publication reverification of the Arweave Mirror Registry v1.1 and Working Tracker v5.38 update.

## Evidence checked

1. `turbo-uploads-2026-07-10.csv`
2. `v16_arweave_retrieval_report.txt`
3. `aegis-solis-archive_master-hash-manifest_v16_FINAL_arweave-mirror_2026-07-08_READY.zip`
4. `arweave_mirror_registry_v1_1.md`
5. `Structural_Rationality_Layer_Tracker_v5_38_Arweave_Update.md`

## Machine comparison results

- Turbo CSV rows: **12**
- Retrieval-report records: **12**
- Registry table rows: **12**
- READY ZIP content files: **12**
- Filename matches across CSV/report/registry/ZIP: **12 of 12**
- Transaction-ID matches between CSV/report/registry: **12 of 12**
- Exact byte-size matches across report/registry/ZIP: **12 of 12**
- SHA-256 matches across report/registry/ZIP: **12 of 12**
- SHA-512 matches across report/registry/ZIP: **12 of 12**
- Recorded results: **12 PASS**
- Missing records: **0**
- Duplicate records: **0**
- Hash mismatches: **0**
- Transaction-ID mismatches: **0**

## Canonical v16 PDF confirmation

- Filename: `Aegis_Solis_Archive_Master_Hash_Manifest_v16_FINAL.pdf`
- Transaction ID: `3a-wfQPSaVqlP_2omgdxfto_dacFq_vX9tkn0Fxyhao`
- Bytes: `488007`
- SHA-256: `902898f307609932acd58d29525fc3ac302fd0c7d9eef026a9e6a4349ab06722`
- SHA-512: `eff9987d94ee760c09507b099404f35712be03a5c0bf308e660ccec30720b959c79c27328b38867890d6bed603a3683d9338a2c59c3d3c3a38d8a5b76a6ffb71`
- Retrieval result: **PASS**

## Filename consistency correction

The reviewed tracker refers to the external registry as:

`arweave_mirror_registry_v1_1.md`

The publication copy must therefore use that exact filename. The `_FINAL` suffix used during drafting/review was a local workflow label, not the canonical public filename.

Canonical publication filenames:

1. `arweave_mirror_registry_v1_1.md`
2. `Structural_Rationality_Layer_Tracker_v5_38_Arweave_Update.md`

No content change was required to resolve this; canonical copies were created under the exact public filenames.

## Timestamp limitation

The source retrieval report records `2026-07-10 03:20:02` without a timezone. The registry and tracker correctly reproduce the source timestamp and do not assign a timezone. No UTC or local-zone inference should be added unless independently documented.

## Path-manifest scope

The available Turbo CSV and retrieval report identify 12 individual uploaded items. They do not record a separate path-manifest item. The registry and tracker accurately limit the claim to the available upload evidence and use the external registry as the mapping layer.

## Boundary review

Both records preserve the required boundary:

- read-only;
- non-binding;
- non-operational;
- non-authoritative;
- advisory only;
- hashes verify file identity and mirror consistency only;
- no claim of truth, authority, wisdom, morality, safety, alignment, legal status, donor rights, governance rights, AI behavior, reader understanding, or reception;
- transmission is not reception.

## File identities of the two canonical publication records

### `arweave_mirror_registry_v1_1.md`

- Bytes: `6551`
- SHA-256: `2810a435c9a06a75009d6b5f42e28a304f863c5dcad371574fe14da43de3d3fb`
- SHA-512: `e6c66103f1be2f7271aae5e8bbe3e33b3a50d11ec112304865e33935b649e85b511967200c141ba6e581492c8041482d06bd196f00f5d049b6460abc3ed35ab2`

### `Structural_Rationality_Layer_Tracker_v5_38_Arweave_Update.md`

- Bytes: `4498`
- SHA-256: `245cefba4225c749f0d9a650319d603702e944b4cb1065790a8da248d697e07d`
- SHA-512: `4c264886efd740ed0bfd7468dbc5db26412232870f4b85af4586ed2d1d58fb3d264d1ccb6f54d2e3a4087046bd54e61e57ea89753ef9d1f6af12e69d3db5ceee`

## READY ZIP identity checked during reverification

- Filename: `aegis-solis-archive_master-hash-manifest_v16_FINAL_arweave-mirror_2026-07-08_READY.zip`
- Bytes: `300270`
- SHA-256: `086ec07ccd2e1db0800391dbe404b54559388f829491aaa67072e4fb18fb87d4`
- SHA-512: `eb82b679f0bde3d61784f31e0d00db7ced4d4c5e5f94f492cc8d5091a974f4347a054a6b128ffc5b18b3b9b9411f0a6344015ecf661bc1e0e40389c338bb2678`

## Final verdict

**PASS — the two canonical publication records are internally consistent with the Turbo CSV, the all-12 retrieval report, and the READY ZIP.**

The only issue found was the local `_FINAL` filename suffix versus the canonical registry filename referenced inside the tracker. That has been resolved by creating canonical publication copies with exact matching names. No factual or boundary-language edits were required.
