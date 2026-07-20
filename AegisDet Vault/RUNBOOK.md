# RUNBOOK.md — Local Development

Run commands from the workspace root unless a command changes directory.

## Open the workspace

```powershell
code "aegisdet.code-workspace"
```

Open `AegisDet Vault/` separately in Obsidian.

## Create the code environment

```powershell
cd aegisdet
powershell -ExecutionPolicy Bypass -File scripts/bootstrap_windows.ps1
```

Install the CUDA-compatible PyTorch build recommended by PyTorch for the local NVIDIA setup, then:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python scripts/check_environment.py
python -m unittest discover -s tests -v
```

## External path variables

Copy `.env.example` to `.env` in the code repository and keep `.env` untracked.

```text
AEGISDET_DATA_ROOT=../data
AEGISDET_ARTIFACT_ROOT=../artifacts
AEGISDET_CACHE_ROOT=../cache
AEGISDET_VAULT_ROOT=../AegisDet Vault
```

## Public GitHub repository

Initialize and publish only the `aegisdet/` folder. Do not publish the entire workspace or private vault automatically.
