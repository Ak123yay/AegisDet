$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python was not found. Install Python 3.10 or 3.11 and reopen PowerShell."
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -e .

Write-Host "Core AegisDet package installed."
Write-Host "Next: install the CUDA-compatible PyTorch build from the official PyTorch selector."
Write-Host "Then run:"
Write-Host "  .\.venv\Scripts\python.exe -m pip install -r requirements.txt"
Write-Host "  .\.venv\Scripts\python.exe scripts\check_environment.py"
Write-Host "  .\.venv\Scripts\python.exe -m unittest discover -s tests -v"
