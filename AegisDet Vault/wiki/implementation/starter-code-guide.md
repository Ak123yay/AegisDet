# Starter Code Guide

The included code is a tested framework for the first non-neural adaptive pipeline. It deliberately does not pretend to contain the final global-token model.

## What works without model weights

- Detection and crop data structures.
- IoU calculation.
- Small/uncertain rule routing.
- Deterministic crop planning and padding.
- Coordinate remapping.
- Class-aware NMS merge.
- EdgeScore calculation.
- Unit tests.

## What requires the environment and weights

- Ultralytics model loading.
- Baseline training and evaluation.
- ONNX export.
- Real image inference.
- Runtime latency measurement.

## First commands

```powershell
cd project-code
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Install CUDA PyTorch using pytorch.org instructions first
pip install -r requirements.txt
python scripts/check_environment.py
python -m unittest discover -s tests -v
```

Then edit `configs/baseline_yolo26n.yaml` and `data/wildlife.yaml` before training.
