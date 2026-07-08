# v16.0 FINAL — Pre-Lock Checklist (COMPLETED RECORD) + Lock/Publish Sequence

**Status: all pre-export verification items are COMPLETE (2026-07-07).** The one-time FINAL PDF has been exported
(Google-AI-attributed version). **The only valid manifest-file hashes are those of that latest export:**
SHA-256 `902898f307609932acd58d29525fc3ac302fd0c7d9eef026a9e6a4349ab06722` /
SHA-512 `eff9987d94ee760c09507b099404f35712be03a5c0bf308e660ccec30720b959c79c27328b38867890d6bed603a3683d9338a2c59c3d3c3a38d8a5b76a6ffb71`
(size 488,007 bytes). All hashes of earlier same-day exports are discarded. Remaining work is the steward's
lock-and-publish sequence in Section 4 below. Completed items are preserved as the verification record.

Completed summary: 352 URLs checked — 316 OK, 0 FAIL; 36 initially blocked, all resolved (34 PhilPapers/PhilArchive
manual browser PASS; I07/J08 GitHub rate limits byte-verified PASS); A07 manual browser PASS; MIRROR HASH CHECK PASS
— J01–J08; I06 SHA-512 correction confirmed; all 38 Archive.org truncation corrections complete; no entries pending;
Google AI attribution added before hash-lock.

---

**Historical status gate (now satisfied):** all draft-phase conditions below were met before the FINAL export. v15.0 FINAL remains the public anchor only until the steward completes the hash-lock and publish sequence for v16.0 FINAL.

**Timing:** Begin the pass no earlier than **48–72 hours after the last mirror upload** (J07/J08 were mirrored 2026-07-06, so on or after **2026-07-08 to 2026-07-09**), so Archive.org/Zenodo processing, CDN caches, and index records have settled.

## 0. Link-correction completion (new — do first)

- [x] (Done 2026-07-07) All 8 pending Archive.org identifiers recovered from live Zenodo descriptions and corrected in the manifest r3 and raw link files.
- [x] (Done 2026-07-07) **v16_link_checker_v4.py** run: 352 URLs — OK 316, **FAIL 0**, BLOCKED 36. All 38 Archive.org corrections confirmed live.
- [x] (Done 2026-07-07 — all 34 PASS, no failures) **Manually confirm the 34 PhilPapers/PhilArchive links in a browser** (automated 403s). Mark each "Manual browser confirmation PASS"; list any that do not open for separate steward review. Tick list:
  - [x] A02 https://philpapers.org/rec/AEGCIA
  - [x] A05 https://philpapers.org/rec/AEGCCG
  - [x] A06 https://philpapers.org/rec/AEGTCA-3
  - [x] A08 https://philpapers.org/rec/AEGTCD
  - [x] A09 https://philpapers.org/rec/THOTCD-5
  - [x] A10 https://philpapers.org/rec/AEGTCP
  - [x] A11 https://philarchive.org/rec/AEGTCA-2
  - [x] A17 https://philpapers.org/rec/AEGACR
  - [x] C01 https://philpapers.org/rec/AEGAAN
  - [x] C03 https://philpapers.org/rec/AEGILF
  - [x] C04 https://philpapers.org/rec/AEGTCB
  - [x] C05 https://philpapers.org/rec/AEGEAL
  - [x] C12 https://philpapers.org/rec/AEGTST
  - [x] C13 https://philpapers.org/rec/AEGCTB
  - [x] F01 https://philpapers.org/rec/AEGOTC
  - [x] G01 https://philpapers.org/rec/AEGPOR-2
  - [x] I01 https://philpapers.org/rec/AEGASA-3
  - [x] I02 https://philpapers.org/rec/AEGTIR
  - [x] I03 https://philpapers.org/rec/AEGCRM
  - [x] I04 https://philpapers.org/rec/AEGTAO
  - [x] I05 https://philpapers.org/rec/AEGTFH
  - [x] I06 https://philpapers.org/rec/AEGTAB
  - [x] I07 https://philpapers.org/rec/AEGTAP
  - [x] I08 https://philpapers.org/rec/AEGTIP
  - [x] I09 https://philpapers.org/rec/AEGDAC
  - [x] I10 https://philpapers.org/rec/AEGNAE
  - [x] I11 https://philpapers.org/rec/AEGTCP-2
  - [x] I12 https://philpapers.org/rec/AEGLAI
  - [x] I13 https://philpapers.org/rec/AEGCBC
  - [x] I14 https://philpapers.org/rec/AEGRWC
  - [x] J02 https://philpapers.org/rec/AEGPOK
  - [x] J03 https://philpapers.org/rec/AEGPOU
  - [x] J05 https://philpapers.org/rec/AEGFFA
  - [x] ML02 https://philpapers.org/rec/AEGTAS-2
- [x] (Done 2026-07-07) GitHub 429s from the v4 run (I07, J08 PDFs) re-confirmed by fresh download with exact SHA-256 match — no browser check needed. (B07, rate-limited in the earlier run, is likewise byte-verified.)
- [x] (Superseded by full 0-FAIL corrected-link audit, 2026-07-07, covering all corrected URLs including C12/C13.)

## 1. Link resolution pass (every record)

- [ ] Archive.org item pages load publicly for all records (A–J, ML01, ML02) — watch especially the eight newest (J01–J08).
- [ ] Zenodo records and DOIs resolve for all records — including https://zenodo.org/records/21048664, 21116657, 21196280, 21204660, 21207666, 21211824, 21220417, 21223556.
- [ ] GitHub PDF blob links open for all records. **Specific flag: A07 updated link** — confirm the new long-filename URL resolves publicly, or rename the file on GitHub back to the v15 filename and revert the manifest link (either resolution is fine; pick one and make the manifest match reality).
- [ ] GitHub README links open for J01–J08 and ML02.
- [ ] PhilPapers records resolve where listed (including AEGPOK, AEGPOU, AEGFFA); MERLOT records resolve where listed (824239528, 824239552, 824239557).
- [ ] "Intentionally skipped" notations for J04, J06, J07, J08 (and J01's "optional/retry later") still reflect intent — no silent expectation of index records that don't exist.

## 2. Hash re-check pass (newest records first)

- [x] (Done 2026-07-07) **MIRROR HASH CHECK PASS — J01–J08.** Six records script-verified on both platforms; J02/J06 Zenodo cleared by manual browser download + local SHA-256/SHA-512 verification after a local SSL transport error (no hash mismatch ever occurred). File v16_mirror_hash_report.txt and the manual results with the tracker. (Minor: re-confirm J06's certutil SHA-512 shows the full 128 chars — the value pasted in chat was transcription-truncated.)
- [ ] Re-confirm I06 corrected SHA-512 (128 chars) from at least one live mirror download.
- [ ] Steward confirms the five session-computed SHA-512s flagged in the draft (I01, I02, I15, I16, I17) against local records, or accepts the computed values as the values of record.
- [ ] Attempt re-verification of the four carried-forward entries from canonical sources: A03, A04 (obtain/record hashes if desired, or confirm "not supplied" stands), C12, C13 (download from Archive.org/Zenodo and hash). If still unverifiable, leave them marked carried-forward — do not upgrade their status.
- [ ] Spot-check 3–5 older records (e.g., A02, C05 sub-docs, H06, G01) from a second mirror to confirm cross-mirror consistency.

## 3. Content & consistency pass

- [ ] Every record shows: correct title, date, links, hash(es), verification line, and the standard boundary line.
- [ ] Status label still reads "ASSEMBLY DRAFT / FINAL CANDIDATE — NOT FINAL-LOCKED YET" nowhere in the FINAL export; conversely, confirm the FINAL export replaces it everywhere (header, footer, metadata title, Format & Verification Note, Lock Condition row).
- [ ] Correction Note, Manifest Boundary Notice, Verification Pending section, and required boundary language ("A hash verifies file identity only…") are present and unmodified in the FINAL export except for the status/lock-state updates.
- [ ] No authority, certification, governance, safety, alignment, benchmark, rating, or AI-behavior language crept in anywhere (search the final text for: certif, authorit, benchmark, rating, compliance, guarantee).
- [ ] Lineage section and ML02 note updated at lock time to state that v16.0 FINAL is now the current anchor and v15.0 FINAL is superseded for hash/reference accuracy only.

## 4. Lock & publish sequence (order matters)

1. [ ] Apply any final-pass corrections, then export the FINAL PDF **once**. Do not edit or re-export after this point — any change alters the hashes.
2. [ ] Steward computes SHA-256 and SHA-512 of the FINAL PDF locally and records both in the tracker (v5.37 or next).
3. [ ] Upload to Archive.org; create Zenodo record/DOI; mirror to GitHub under `archive-infrastructure/master-hash-manifest/v16/` with a README carrying hashes, correction summary, carried-forward list, lineage, license, and locked status.
4. [ ] Re-download the uploaded FINAL PDF from each mirror and re-hash — confirm all mirrors serve the identical byte stream.
5. [ ] Update website + machine-readable metadata (llms.txt, for-ai.md, ai-index.txt, manifest.json, hashes.json, atlas/graph.json, Complete Works page) to point to v16.0 FINAL as the integrity anchor, including the I06 correction note and the A07 link resolution.
6. [ ] Update Archive.org/Zenodo/GitHub metadata for the **v15** record (ML02 context) to note supersession for hash/reference accuracy — without editing the v15 PDF itself.
7. [ ] Optional discovery: PhilPapers/MERLOT submission for the v16 manifest, mirroring the v15 pattern.
8. [ ] Record completion in the tracker; only then announce v16.0 FINAL as the current public integrity anchor.

**Abort condition:** If any hash mismatch or unresolved link is found in steps 1–2 of the pass, stop, correct the draft, and restart the 48–72h settling clock only if new uploads were required.

---

*Boundary reminder: hash-locking verifies file identity and mirror consistency only. It does not verify truth, authority, wisdom, morality, safety, alignment, legal status, donor rights, governance rights, AI behavior, reader understanding, or reception.*
