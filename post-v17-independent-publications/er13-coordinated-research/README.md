# Aegis Solis — ER-13 Coordinated Research Package v1.3

**Status:** FINAL PRESERVATION RELEASE (author-authorized and byte-specific) · independent scientific and human security reviews **pending** · research only · **not** operational or security certified.

**Author:** Aegis Solis (Thomas Vargo) · **Preservation date:** 2026-10-11.

This folder contains the publicly readable main Crosswalk PDF, the separately dated preservation records, corrective supplements, and AI-assisted dual-use review reports. The original research ZIP is **not** stored in this folder because its 29,932,834 bytes exceed GitHub's browser-upload limit. Attach it **unchanged** as a GitHub Release asset under tag `er13-preservation-v1.3-2026-10-11`.

## Frozen package identity

- **Filename:** `Aegis_Solis_ER13_SEC_CDP_Coordinated_Review_Package_v1_3.zip`
- **Length:** 29,932,834 bytes
- **SHA-256:** `a708a2775bfd20b7e29ccf9a41bac0c7b35a788162f0d771f032b27cb45b1a17`
- **Frozen contents:** ER-13 Evidence Crosswalk v0.6.4, SEC-CDP-001 Pilot v0.4.1, SEC-CDP-002 Infrastructure v0.1.3, review history and verification artifacts.
- **Standalone PDF:** `01_MAIN_DOCUMENT/Aegis_Solis_ER13_Evidence_Crosswalk_Draft_v0_6_4_EXACT_from_v1_3.pdf` is byte-identical to the Crosswalk PDF in the frozen ZIP.

## Directory map

- `01_MAIN_DOCUMENT/`: exact original Crosswalk PDF for readers and citation.
- `02_PRESERVATION/`: Final Preservation Lock, author-approved provenance records, and original three-file checksum register.
- `03_POST_LOCK_CORRECTIONS/`: separately versioned supplement ZIP and three readable PDF records for the historical restricted-label disposition, superseded-version warnings, and future evaluation/results policy.
- `04_AI_ASSISTED_REVIEWS/`: Claude v1.0 dual-use review and ChatGPT v0.1 initial review. **Both are AI-assisted, not independent human certification.**
- `SHA256SUMS_GITHUB_DEPOSIT.txt`: hashes of this folder's source artifacts plus the frozen Release ZIP (outside this folder).

## Research and implementation boundaries

SEC-CDP-002 v0.1/v0.1.1/v0.1.2: **SUPERSEDED — NOT FOR IMPLEMENTATION**. SEC-CDP-002 v0.1.3: **RESEARCH ONLY — NOT IMPLEMENTED / NOT TESTED**. No pilot has been executed; no recruitment, operational deployment, protection guarantee or human security certification is authorized by this release. All pilot and infrastructure execution gates remain open. Preserve null, adverse and preservation-unfavorable findings.

The public SEC-CDP-002 historical record still contains the old `ARCHIVE RESTRICTED` legend; an **author-approved post-lock handling disposition** documents why the historical public preservation was affirmed. It does not declassify future restricted material.

## Public reference records

- [Internet Archive](https://archive.org/details/aegis-solis-er-13-evidence-crosswalk-draft-v-0-6-4-exact-from-v-1-3)
- [Zenodo record 23303565](https://zenodo.org/records/23303565)
- [Aegis Solis Archive](https://aegissolisarchive.org/)

Remote Zenodo file checksums were **not independently confirmed** as of preparation; do not describe them as verified. Internet Archive MD5/SHA-1 and sizes were matched via server metadata by a separate AI-assisted reviewer, not by a fresh full SHA-256 re-download.

## Integrity versus authenticity

A passing `verify_package.py` is evidence of internal file/check consistency **only**, not external authorship authentication or scientific validity. A future release may supplement the frozen hash with signature and independent timestamp records.

## Licensing needs author reconciliation

The repository's existing root `LICENSE-AND-USE.md` currently states **CC BY-ND 4.0**, while a separately published Zenodo record was prepared under **GPLv3** and the user's preference evolved during publication. This folder **does not silently override** existing licenses or warrant rights over third-party works. Confirm the appropriate, explicit **file-scoped license and its applicability** before advertising all material as GPLv3 or another license. Public preservation and hash verification do not imply a specific reuse license.

## Archive integration

`MASTER_HASH_MANIFEST_EFFECT: NONE` — Manifest v17 remains unchanged; no v18. The Mirror Engine relationship is *discovery/reference only*; no source binding, calculator, preset, executable integration or mathematics is changed.
