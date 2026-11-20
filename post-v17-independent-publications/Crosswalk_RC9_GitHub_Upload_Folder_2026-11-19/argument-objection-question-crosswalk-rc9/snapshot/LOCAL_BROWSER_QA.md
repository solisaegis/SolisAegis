# Local browser interaction QA — 2026-11-16

Environment: headless Chromium via Playwright using the exact generated standalone HTML set as page content. This avoids filesystem URL restrictions in the test sandbox. **Not** a post-upload or remote WordPress interaction test.

- Desktop viewport: 1366 × 900 — PASS.
- Mobile viewport: 390 × 844 — PASS.
- JavaScript page errors: **0** in each tested viewport.
- Navigation tabs: 8 labeled tabs present, including Overview, mapped arguments, objections, CEPSAD cases, internal objections, questions, catalog and crosswalk links.
- Catalog: showing 1–72 of 164; Questions: 1–72 of 112; Objections: 1–55 of 55; CEPSAD cases: 1–72 of 75; internal objections: 1–40 of 40; crosswalk typed links: 1–72 of 531.
- Source JSON and embedded data agree; all expected counts and ARG-17 held-placeholder absence-of-source-prose checks pass with the standard-library verifier.

**Still untested:** Remote GitHub Pages/Zenodo/Internet Archive rendering, real device accessibility, external link retrieval and exact remote byte correspondence, licensing clearance, scientific conclusions and reception by an AI.

**Status-only release preparation:** The reviewed standalone reader passed these tests. For the Zenodo-ready copy, the same research objects and functional JavaScript were retained; only the `release` metadata and visible footer changed. This is not a remote Zenodo test.

**Zenodo-ready copy re-test on November 16, 2026:** Headless Chromium (`/usr/bin/chromium`) successfully loaded the exact final `index.html` at 1366×900 and 390×844. All eight tab buttons were present at each viewport, expected content loaded, and zero JavaScript page errors occurred. This is a local static-reader test, not a remote Zenodo accessibility check.
