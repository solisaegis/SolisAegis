# How to upload the GitHub Crosswalk mirror

The upload package contains an `argument-objection-question-crosswalk-rc9` folder with `README.md`, `GITHUB_PUBLICATION_SCOPE.md`, and `snapshot/` (12 exact source files). Do not upload this instruction file into GitHub.

1. Extract this ZIP on your computer.
2. Open the existing public repository: https://github.com/solisaegis/SolisAegis/tree/main/post-v17-independent-publications
3. Click Add file > Upload files.
4. Drag the entire `argument-objection-question-crosswalk-rc9` folder from the extracted package to GitHub. Before committing, confirm GitHub shows `argument-objection-question-crosswalk-rc9/snapshot/DATA.json`, `argument-objection-question-crosswalk-rc9/snapshot/index.html`, all 12 original files, and the two root documentation files. If your browser flattens the folder, cancel and use a directory-preserving upload method.
5. Commit message: `Add public RC9 argument-objection-question Crosswalk GitHub mirror (G0)`.
6. After committing, copy the commit SHA and the GitHub directory link; check that `snapshot/DATA.json`, `snapshot/index.html`, and `snapshot/SHA256SUMS.txt` are all downloadable.
7. Run `python verify_package.py` from within the `snapshot` directory after downloading it, or compare all individual SHA-256s to `snapshot/SHA256SUMS.txt`.

Do not upload the outer ZIP directly as a single opaque file if you want browsable GitHub records; extract and upload the folder contents. The existing repository and locked files should not be replaced.
