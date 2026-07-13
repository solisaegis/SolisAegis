# Aegis Solis Archive

# Layer 2 Arweave Complete Works Preservation Record

**Final v1.0 - 2026-07-13**  
**Author:** Aegis Solis (Thomas Vargo)  
**Status:** COMPLETE

## 1. Purpose

This record documents the second Arweave preservation layer for the Aegis Solis Archive: a complete-works upload derived from the canonical FINAL LOCKED Layer 2 package. It preserves the mapping between canonical archive paths, flat upload filenames, cryptographic hashes, public Arweave data-item IDs, receipts, and retrieval evidence.

## 2. Canonical source

- Canonical package: `Aegis_Solis_Archive_Complete_Works_Layer2_FINAL_LOCKED_v1_0`
- Files: **120**
- Total bytes: **55,547,663**
- Payload files: **109**
- Metadata/evidence/checksum support files: **11**
- Canonical package modified during upload preparation: **No**

The associated Master Hash Manifest v16 FINAL has SHA-256 `902898f307609932acd58d29525fc3ac302fd0c7d9eef026a9e6a4349ab06722` and SHA-512 `eff9987d94ee760c09507b099404f35712be03a5c0bf308e660ccec30720b959c79c27328b38867890d6bed603a3683d9338a2c59c3d3c3a38d8a5b76a6ffb71`.

## 3. Arweave architecture

The Layer 2 upload consists of **120 separate Arweave data items**. No folder deployment and no path manifest were used. Original hierarchy and filenames are reconstructed through the transaction registry and flat-upload mapping.

- Unique transaction IDs: **120**
- Recorded bytes: **55,547,663**
- Recorded Turbo credits: **0.496128**
- Arweave owner address: `3NdgyEYWi44PsKJBWIUZRGW9dw9dzMP-gHItz12gCIg`

## 4. Integrity chain

1. The canonical FINAL LOCKED package completed its local lock process.
2. Post-lock verification passed the recorded SHA-256 and SHA-512 scope.
3. A separate flat upload copy was created with 120 top-level files and zero subfolders.
4. All 120 flat files matched the canonical source by exact SHA-256 and SHA-512.
5. The Turbo export reconciled to 120 unique Layer 2 data-item IDs.
6. Every transaction-registry filename and byte count matched the flat mapping.

## 5. Retrieval chronology

The first corrected Arweave-only checkpoint verified **119 of 120** data items by exact byte size, SHA-256, and SHA-512. `054_E08.pdf` initially returned 404 from the tested direct routes.

The E08 signed receipt and live status API nevertheless reported `FINALIZED`, the correct 74,496-byte PDF payload, and root bundle `8dhejwKw5g4b8XphJRikgNOuQF1ey7JaIEJR7K_k7sU`. That root bundle was confirmed on Arweave. The individual public URL later resolved successfully to the canonical *Ambiguity Sensitivity (v1.0)* document.

No re-upload was performed. The original checkpoint and subsequent resolution are both preserved so the chronology remains auditable.

## 6. Final result

**Layer 2 Arweave complete-works preservation is COMPLETE.**

- 120 of 120 files mapped
- 120 of 120 upload records present
- 120 unique transaction IDs
- 120 of 120 byte counts reconciled
- 119 of 120 exact matches in the automated checkpoint
- E08 FINALIZED receipt and confirmed root bundle
- E08 later public retrieval resolved
- 120 of 120 accounted for and publicly retrievable by close of sequence
- canonical FINAL LOCKED package unchanged

## 7. Navigation

- Human-readable record: this document
- Transaction registry CSV: `Aegis_Solis_Layer2_Arweave_Individual_Upload_Registry_v1_0.csv`
- Transaction registry JSON: `Aegis_Solis_Layer2_Arweave_Individual_Upload_Registry_v1_0.json`
- Machine preservation record: `layer2_arweave_preservation_record_v1_0.json`
- E08 resolution record: `E08_RETRIEVAL_RESOLUTION_RECORD_v1_0.md`
- Evidence index: `EVIDENCE_INDEX_v1_0.csv`
- Source evidence: `evidence/`
- Cryptographic lists: `checksums/`

## 8. Interpretation boundary

This record verifies file identity, mapping consistency, upload registration, receipt evidence, bundle status, and retrieval checkpoints only. It does not verify truth, authority, wisdom, morality, safety, alignment, legal status, authorship rights, donor rights, governance rights, AI behavior, reader understanding, permanence guarantees, or reception.

The archive and this preservation layer are read-only, non-binding, non-operational, non-authoritative, and advisory only.

**Transmission is not reception.**
