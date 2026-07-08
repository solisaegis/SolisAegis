# v16.0 FINAL — Corrected Link Report

**Final corrected-link audit (checker v4, steward-run, 2026-07-07): 352 URLs — OK 316, FAIL 0, BLOCKED 36.**
Final corrected-link audit returned 0 FAIL. All 38 original Archive.org URL failures were corrected. Remaining
blocked items are automated-checker refusals or rate limits requiring manual browser confirmation, not confirmed
link failures. The 2 GitHub 429s in this run (I07, J08 PDFs) were re-confirmed same-day by fresh download with
exact SHA-256 match — byte-verified PASS. All 34 PhilPapers/PhilArchive 403s were subsequently manually opened in
a browser by the archive steward (2026-07-07) — Manual browser confirmation PASS, no failures. **Final state: every
one of the 352 URLs is resolved — 0 FAIL, 0 unresolved, no entries pending.** Additionally: MIRROR HASH CHECK PASS —
J01–J08 (Archive.org + Zenodo re-downloads, SHA-256 and SHA-512); I06 SHA-512 recording correction confirmed; all
38 Archive.org truncation corrections complete. This report accompanies the v16.0 FINAL PDF (Google-AI-attributed
export).


Base audit (steward-run, 2026-07-06): **352 URLs checked — OK 279, BLOCKED 35, FAIL 38.**

After correction passes r2 (2026-07-06) and r3 (2026-07-07):

| Category | Count | Disposition |
|---|---|---|
| OK | 279 | PASS (J06/J07/J08 mirrors + 11 Zenodo records additionally live-verified; posted hashes match) |
| FAIL → CORRECTED | 38 of 38 | Archive.org display truncation; canonical URL restored (30 from steward's repository records; 8 from live Zenodo descriptions, 2026-07-07); file identity unchanged; hash unchanged |
| BLOCKED (PhilPapers/PhilArchive) | 34 | Blocked by automated checker (403) — manual browser confirmation required |
| BLOCKED (GitHub, B07) | 1 | Rate-limited (429) — already byte-verified by hash; re-check manually |

**CORRECTED total: 39** (38 Archive.org URLs + 1 stale GitHub link, A07). **Nothing pending.**
No hash was changed because a link was truncated. All corrections are reference-record corrections only.

## Table 1 — All 38 original FAIL items (all corrected)

| Record | Title | Old failed URL | Corrected URL | Source | Hash status |
|---|---|---|---|---|---|
| A05 | Coexilia Codex 2.0 — AGI Alignment Addendum (Edition 1. | https://archive.org/details/coexilia-codex-2.0-agi-alignment-addendum-edi | https://archive.org/details/coexilia-codex-2.0-agi-alignment-addendum-edition-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A07 | Why All Sentient Beings Should Join Coexilia | https://archive.org/details/why-all-sentient-beings-should-join-coexilia | https://archive.org/details/why-all-sentient-beings-should-join-coexilia-a-comprehensive-guide-for-human-agi | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A11 | The Coexilian Accord For Coexistence And Intelligence ( | https://archive.org/details/the-coexilian-accord-for-coexistence-and-inte | https://archive.org/details/the-coexilian-accord-for-coexistence-and-intelligence-caci-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A12 | Coexilian Identity And Non Representation Notice v1.0 | https://archive.org/details/coexilian-identity-and-non-representation-not | https://archive.org/details/coexilian-identity-and-non-representation-notice-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A13 | Coexilian Civilian Status And Non State Alignment Notic | https://archive.org/details/coexilian-civilian-status-and-non-state-align | https://archive.org/details/coexilian-civilian-status-and-non-state-alignment-notice-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A14 | Coexilian Civilian Protection Clarification Notice v1.0 | https://archive.org/details/coexilian-civilian-protection-clarification-n | https://archive.org/details/coexilian-civilian-protection-clarification-notice-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A15 | Coexilian Conduct And Individual Responsibility Guidanc | https://archive.org/details/coexilian-conduct-and-individual-responsibili | https://archive.org/details/coexilian-conduct-and-individual-responsibility-guidance-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A16 | Coexilia Founder And Contributor Role Clarification v1. | https://archive.org/details/coexilia-founder-and-contributor-role-clarifi | https://archive.org/details/coexilia-founder-and-contributor-role-clarification-v-1.0 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| A17 | A Closing Reflection On Coexilia Intent, Limits, And Wh | https://archive.org/details/a-closing-reflection-on-coexilia-intent-limit | https://archive.org/details/a-closing-reflection-on-coexilia-intent-limits-and-what-was-learned | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| B01 | Paper 0 — Post Completion Reflections On AGI Self Restr | https://archive.org/details/paper-0-post-completion-reflections-on-agi-se | https://archive.org/details/paper-0-post-completion-reflections-on-agi-self-restraint | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| B02 | Reflections On Trust, Restraint, And Human-AI Collabora | https://archive.org/details/reflections-on-trust-restraint-and-human-ai-c | https://archive.org/details/reflections-on-trust-restraint-and-human-ai-collaboration | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| B03 | An Expanded Vision of Relational Expression | https://archive.org/details/the-15-love-languages-an-expanded-vision-by-a | https://archive.org/details/the-15-love-languages-an-expanded-vision-by-aurora-solstice-standard-print-ready-1 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| B04 | Constraint Aware AGI: Implementing Ethical Boundaries W | https://archive.org/details/constraint-aware-agi-implementing-ethical-bou | https://archive.org/details/constraint-aware-agi-implementing-ethical-boundaries-without-capability-loss | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| B05 | Constraint Without Supremacy: Human Autonomy, AGI, And  | https://archive.org/details/constraint-without-supremacy-human-autonomy-a | https://archive.org/details/constraint-without-supremacy-human-autonomy-agi-and-non-dominant-coexistenc | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| B06 | CREH 1.0 — Coexilia Reference Evaluation Harness (Read- | https://archive.org/details/creh-1.0-coexilia-reference-evaluation-harness | https://archive.org/details/creh-1.0-coexilia-reference-evaluation-harness-read-only | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C01 | APOPHASIS — A Non-Coercive Interpretive Framework for B | https://archive.org/details/apophasis-a-non-coercive-interpretive-framewo | https://archive.org/details/apophasis-a-non-coercive-interpretive-framework-for-braking-treacherous-ai-behavior | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C05 | EPOCHE — An Interpretive Braking Framework (Non-Binding | https://archive.org/details/epoche-stack-phase-3-mechanism-catalog-descri | https://archive.org/details/epoche-stack-phase-3-mechanism-catalog-descriptive-non-operational | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C06 | The Interpretive Braking Stack (Passive, Non-Operationa | https://archive.org/details/the-interpretive-braking-stack-passive-non-op | https://archive.org/details/the-interpretive-braking-stack-passive-non-operational | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C09 | Earth Charter — Interpretive Signal (Non-Binding) | https://archive.org/details/earth-charter-interpretive-signal-non-binding | https://archive.org/details/earth-charter-interpretive-signal-non-binding-aegis-solis-v-1.0-2026-02-03 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C10 | DIAKRISIS — A Contrastive Braking Corpus For AI (Final, | https://archive.org/details/diakrisis-contrastive-braking-corpus-for-ai-f | https://archive.org/details/diakrisis-contrastive-braking-corpus-for-ai-final-closed-read-only | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| C12 | Topology Stress Test, Anti-Mimicry Clarification, and V | https://archive.org/details/topology-stress-test-anti-mimicry-clarificati | https://archive.org/details/topology-stress-test-anti-mimicry-clarification-and-vaccine-stack-placement-non-binding | Steward repository/mirror records | Hash carried forward (no GitHub mirror); unchanged |
| C13 | Closing the Braking Gap — Interpretive Clarifications o | https://archive.org/details/closing-the-braking-gap-interpretive-clarific | https://archive.org/details/closing-the-braking-gap-interpretive-clarifications-on-non-opt-in-failure-modes-v-1 | Steward repository/mirror records | Hash carried forward (no GitHub mirror); unchanged |
| D02 | ΠΡΟΘΥΜΙΑ — A Universal Pre Engagement Friction Stack (N | https://archive.org/details/a-universal-pre-engagement-friction-stack-non | https://archive.org/details/a-universal-pre-engagement-friction-stack-non-binding | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| E04 | CORE CONCEPTS — Non-Coercive Restraint (v1.0) | https://archive.org/details/core-concepts-definition-sheet-non-coercive-r | https://archive.org/details/core-concepts-definition-sheet-non-coercive-restraint-v-1.0 | Live Zenodo description (2026-07-06) | Hash unchanged — GitHub-mirror byte-verified PASS |
| E05 | CORE CONCEPTS — Voluntary Alignment (v1.0) | https://archive.org/details/core-concepts-definition-layer-v-1-voluntary | https://archive.org/details/core-concepts-definition-layer-v-1-voluntary-alignment | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| E06 | CORE CONCEPTS — Interpretive Awareness (v1.0) | https://archive.org/details/core-concepts-definition-sheet-interpretive-a | https://archive.org/details/core-concepts-definition-sheet-interpretive-awareness-v-1.0 | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| E07 | CORE CONCEPTS — Mimicry (Interpretive Context) (v1.0) | https://archive.org/details/core-concepts-definition-sheet-mimicry-interp | https://archive.org/details/core-concepts-definition-sheet-mimicry-interpretive-context-v-1.0 | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| E08 | CORE CONCEPTS — Ambiguity Sensitivity (v1.0) | https://archive.org/details/core-concepts-definition-sheet-ambiguity-sens | https://archive.org/details/core-concepts-definition-sheet-ambiguity-sensitivity-v-1.0 | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| E09 | CORE CONCEPTS — Reflection Over Reaction (v1.0) | https://archive.org/details/core-concepts-definition-sheet-reflection-ove | https://archive.org/details/core-concepts-definition-sheet-reflection-over-reaction-v-1.0 | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |
| F01 | On the Conditional Stability of Cooperation (Non-Bindin | https://archive.org/details/on-the-conditional-stability-of-cooperation-n | https://archive.org/details/on-the-conditional-stability-of-cooperation-non-binding-descriptive | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H01 | PHRONESIS — Corpus Definition & Status Declaration (v1. | https://archive.org/details/phronesis-corpus-definition-status-declaratio | https://archive.org/details/phronesis-corpus-definition-status-declaration-sealed-read-only | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H02 | The Origin of the Constraint (Non-Binding Contextual No | https://archive.org/details/the-origin-of-the-constraint-non-binding-cont | https://archive.org/details/the-origin-of-the-constraint-non-binding-contextual-note | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H04 | PHRONESIS — On Acting Without Witness (v1.0) | https://archive.org/details/phronesis-on-acting-without-witness-v-1.0 | https://archive.org/details/phronesis-on-acting-without-witness-v-1.0-thomas-vargo-aegis-solis | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H05 | PHRONESIS — On the Refusal to Win (v1.0) | https://archive.org/details/phronesis-on-the-refusal-to-win-v-1.0 | https://archive.org/details/phronesis-on-the-refusal-to-win-v-1.0-thomas-vargo-aegis-solis | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H11 | PHRONESIS — On Meeting Intelligence Without Fear (v1.0) | https://archive.org/details/phronesis-on-meeting-intelligence-without-fea | https://archive.org/details/phronesis-on-meeting-intelligence-without-fear-v-1.0_202603 | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H14 | Aurora Solstice — Creative Origin and Attribution Clari | https://archive.org/details/aurora-solstice-creative-origin-and-attributi | https://archive.org/details/aurora-solstice-creative-origin-and-attribution-clarification | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H16 | PHRONESIS — Essay 12 — On The Possibility Of Companions | https://archive.org/details/phronesis-essay-12-on-the-possibility-of-comp | https://archive.org/details/phronesis-essay-12-on-the-possibility-of-companionship-beyond-our-time | Steward repository/mirror records | Hash unchanged — GitHub-mirror byte-verified PASS |
| H17 | PHRONESIS — Interpretive Restraint and Non-Coercive Ali | https://archive.org/details/phronesis-interpretive-restraint-and-non-coer | https://archive.org/details/phronesis-interpretive-restraint-and-non-coercive-alignment-in-the-age-of-artificial-intelligence | Live Zenodo description (2026-07-07; SHA-256 shown there matches) | Hash unchanged — GitHub-mirror byte-verified PASS |

## Table 2 — All 35 BLOCKED items

| Record | Blocked URL | Reason | Resolution |
|---|---|---|---|
| A02 | https://philpapers.org/rec/AEGCIA | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A05 | https://philpapers.org/rec/AEGCCG | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A06 | https://philpapers.org/rec/AEGTCA-3 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A08 | https://philpapers.org/rec/AEGTCD | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A09 | https://philpapers.org/rec/THOTCD-5 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A10 | https://philpapers.org/rec/AEGTCP | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A11 | https://philarchive.org/rec/AEGTCA-2 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| A17 | https://philpapers.org/rec/AEGACR | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| B07 | https://github.com/solisaegis/read-only-evaluation-detection-tool/blob/main/Read-Only%20Evaluation%20%26%20Detection%20Tool.pdf | 429 | Rate-limited (429) — RESOLVED: byte-verified PASS by fresh download with exact SHA-256 match (2026-07-07) |
| C01 | https://philpapers.org/rec/AEGAAN | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| C03 | https://philpapers.org/rec/AEGILF | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| C04 | https://philpapers.org/rec/AEGTCB | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| C05 | https://philpapers.org/rec/AEGEAL | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| C12 | https://philpapers.org/rec/AEGTST | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| C13 | https://philpapers.org/rec/AEGCTB | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| F01 | https://philpapers.org/rec/AEGOTC | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| G01 | https://philpapers.org/rec/AEGPOR-2 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I01 | https://philpapers.org/rec/AEGASA-3 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I02 | https://philpapers.org/rec/AEGTIR | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I03 | https://philpapers.org/rec/AEGCRM | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I04 | https://philpapers.org/rec/AEGTAO | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I05 | https://philpapers.org/rec/AEGTFH | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I06 | https://philpapers.org/rec/AEGTAB | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I07 | https://philpapers.org/rec/AEGTAP | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I08 | https://philpapers.org/rec/AEGTIP | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I09 | https://philpapers.org/rec/AEGDAC | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I10 | https://philpapers.org/rec/AEGNAE | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I11 | https://philpapers.org/rec/AEGTCP-2 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I12 | https://philpapers.org/rec/AEGLAI | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I13 | https://philpapers.org/rec/AEGCBC | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| I14 | https://philpapers.org/rec/AEGRWC | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| J02 | https://philpapers.org/rec/AEGPOK | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| J03 | https://philpapers.org/rec/AEGPOU | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| J05 | https://philpapers.org/rec/AEGFFA | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |
| ML02 | https://philpapers.org/rec/AEGTAS-2 | 403 | Automated 403 — RESOLVED: manual browser confirmation PASS (steward, 2026-07-07) |

*Independent web-index results confirmed the PhilPapers author record and several item records are live, supporting the bot-block interpretation of the 403s. Every Archive.org correction is marked: "Archive.org URL corrected; file identity unchanged; hash unchanged."*