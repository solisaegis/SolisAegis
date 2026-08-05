$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Failed = $false
foreach ($Spec in @(@("SHA256SUMS.txt","SHA256"), @("SHA512SUMS.txt","SHA512"))) {
  $Manifest = Join-Path $Root (Join-Path "verification" $Spec[0])
  Get-Content $Manifest | ForEach-Object {
    if ($_ -match '^([0-9a-f]+)  (.+)$') {
      $Expected = $matches[1]
      $Relative = $matches[2]
      $Actual = (Get-FileHash -Algorithm $Spec[1] -LiteralPath (Join-Path $Root $Relative)).Hash.ToLower()
      if ($Actual -ne $Expected) { Write-Host "FAIL $($Spec[1]) $Relative"; $Failed = $true }
    }
  }
}
if ($Failed) { exit 1 }
Write-Host "PASS: all repository-tree manifest entries verified."
