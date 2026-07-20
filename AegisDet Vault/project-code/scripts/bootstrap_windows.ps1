$ErrorActionPreference = "Stop"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
Write-Host "Install CUDA PyTorch using the command from https://pytorch.org/get-started/locally/"
Write-Host "Then run: pip install -r requirements.txt; pip install -e ."
