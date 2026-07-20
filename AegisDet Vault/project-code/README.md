# AegisDet-Pro Starter Code

This directory contains the working starter for AegisDet-Mini. The deterministic router/crop/merge core and unit tests run without model weights. Ultralytics scripts require the environment and data.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Install CUDA PyTorch using pytorch.org instructions
pip install -r requirements.txt
pip install -e .
python scripts/check_environment.py
python -m unittest discover -s tests -v
```

## Baseline

Edit `data/wildlife.yaml`, then:

```powershell
python scripts/train_baseline.py --config configs/baseline_yolo26n.yaml
python scripts/evaluate_baseline.py --model runs/baseline_yolo26n/weights/best.pt --data data/wildlife.yaml
python scripts/export_onnx.py --model runs/baseline_yolo26n/weights/best.pt
```

No performance values are prefilled. Record real results in the vault experiment notes.
