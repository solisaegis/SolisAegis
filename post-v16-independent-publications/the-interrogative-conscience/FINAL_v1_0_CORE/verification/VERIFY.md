# Verification Instructions

Run either:

- Python: `python verification/verify_repository.py`
- Windows PowerShell: `powershell -ExecutionPolicy Bypass -File verification/Verify_Repository_Windows.ps1`

The scripts verify every manifest-covered repository file against both SHA-256 and SHA-512. The continuity ZIP is not present in the Git tree; verify it separately using the hashes in `release/CONTINUITY_PACKAGE_RELEASE_ASSET_RECORD.json`.

A hash match confirms byte identity. It does not independently establish claim truth or external peer review.
