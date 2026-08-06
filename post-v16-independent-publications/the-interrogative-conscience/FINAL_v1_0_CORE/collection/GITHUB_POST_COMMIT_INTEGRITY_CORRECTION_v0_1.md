# GitHub Post-Commit Integrity Correction v0.1

Status: **Prepared pending separate execution authorization**

The initial 103-file repository publication is commit `43ee755c380e4d98371b1e6667f687b35a2f8521`, first public on `2026-08-04`.

A Git blob comparison found:

- 92 files byte-identical to the controlling Repository Tree v0.1.2;
- 11 CSV files differing only because Windows Git converted CRLF line endings to LF;
- 14/14 locked Final v1.0 PDFs exact;
- no substantive or locked-document alteration.

The corrective sequence restores all eleven CSV byte streams, adds target-local `.gitattributes` with `*.csv -text`, records the exact integrity-restoration commit SHA in mutable release metadata, regenerates verification manifests, and completes the GitHub release only after separate authorization.

The final metadata-binding commit cannot contain its own SHA. Its exact SHA is therefore bound in the GitHub release target and deployment-result record.

No force-push, history rewrite, locked-artifact modification, or non-GitHub action is permitted.
