# AegisDet

**An adaptive CNN-first edge object detector using selective global context, uncertainty routing, and crop refinement for efficient hard-case detection.**

AegisDet is being developed as a family of adaptive edge-detection models and systems. The first implementation, AegisDet-Mini, uses a YOLO26n-derived fast path, a rule-based uncertainty router, selective crop refinement, coordinate remapping, and class-aware merging.

> Current status: research and starter implementation. No claim of outperforming YOLO26n is made until controlled benchmarks are complete.

## Repository scope

This public repository contains source code, tests, configurations, scripts, and public documentation. The private Obsidian knowledge vault and local datasets/checkpoints are intentionally stored outside this repository.

## Starter architecture

```text
image
  ↓
YOLO26n fast detector
  ↓
rule-based uncertainty router
  ├── easy → return detections
  └── hard → select crops → rerun detector → remap → merge
```

Later phases add hard-negative learning, tiny deep-stage global context, learned routing, YOLO26x + RT-DETRv4-X distillation, and INT8 deployment.

## Setup on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
# Install the CUDA-compatible PyTorch build from pytorch.org first.
pip install -r requirements.txt
pip install -e .
python scripts/check_environment.py
python -m unittest discover -s tests -v
```

## External workspace paths

Copy `.env.example` to `.env` and update paths when required:

```text
AEGISDET_DATA_ROOT=../data
AEGISDET_ARTIFACT_ROOT=../artifacts
AEGISDET_CACHE_ROOT=../cache
AEGISDET_VAULT_ROOT=../AegisDet Vault
```

## Current deterministic core

- detection data types
- box geometry and IoU
- rule-based routing
- bounded crop planning
- coordinate remapping
- class-aware NMS
- EdgeScore and latency percentiles
- AegisDet-Mini pipeline
- Ultralytics adapter

## Research integrity

All comparisons must use the same dataset split, resolution, hardware, runtime, precision, batch size, warmup, and timing method. External benchmark numbers are references, not AegisDet results.


## Automatic vault synchronization

The private knowledge vault is a sibling folder named `AegisDet Vault`.

Install hooks once:

```bash
python tools/install_hooks.py
python tools/workspace_sync.py check
```

See `HOOKS.md`.
