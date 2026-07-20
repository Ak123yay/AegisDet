---
title: "Canonical Build Path"
project: "AegisDet-Pro v5.1"
area: "project-control"
status: "locked"
tags: ["roadmap"]
---

# Canonical Build Path

## Phase 0 — Environment and smoke test

**Output:** reproducible Python environment, working CUDA, successful `yolo26n.pt` inference.

1. Install Python 3.11 and create `.venv`.
2. Install CUDA-compatible PyTorch separately using the official PyTorch selector.
3. Install `../aegisdet/requirements.txt`.
4. Run `python scripts/check_environment.py`.
5. Run a pretrained YOLO26n prediction on one image.
6. Freeze `pip freeze` to `requirements-lock.txt`.
7. Pass [[wiki/timeline/phase-0-gate]].

## Phase 1 — Frozen YOLO26n baseline

**Output:** trained, exported, benchmarked control checkpoint.

1. Collect and label dataset v1 using [[DOMAIN_LOCK]].
2. Run duplicate/leakage and label audits.
3. Train at 416×416 using `configs/baseline_yolo26n.yaml`.
4. Save the exact checkpoint used as the control.
5. Evaluate accuracy and class-level failures.
6. Export ONNX and test prediction parity.
7. Benchmark p50/p90/p99 latency.
8. Pass [[wiki/timeline/phase-1-gate]].

## Phase 2 — AegisDet-Mini

**Output:** working adaptive wrapper with a fair baseline comparison.

1. Run the frozen baseline.
2. Compute rule-router signals.
3. Select at most two small or uncertain regions.
4. Add context padding and rerun the same detector on each crop.
5. Remap crop boxes to original coordinates.
6. Merge class-aware detections.
7. Measure refinement rate, APS, false positives, and tail latency.
8. Pass [[wiki/timeline/phase-2-gate]].

## Phase 3 — Data improvement

**Output:** dataset v2 and measured hard-negative improvement.

Mine false positives, false negatives, low-light misses, blur, occlusion, and tiny-object misses. Add uncertainty plus diversity sampling. Retrain without changing the frozen test set.

## Phase 4 — True neural hybrid

**Output:** one justified global-context variant.

Implement a small learned-token bridge only at P4 or P5. Test K=4, K=6, and K=8 with isolated experiments. Remove it if EdgeScore or hard-case metrics do not improve.

## Phase 5 — Learned router

Build labels from whether optional processing actually corrected each baseline frame. Train a small router with an expected-compute penalty. Compare it against the rule router.

## Phase 6 — Distillation

Use **YOLO26x (`yolo26x.pt`)** as the primary same-family teacher and **RT-DETRv4-X** as the secondary architecture-diverse teacher. Fine-tune and freeze both teachers on the domain dataset. Establish no-KD, YOLO26x-only, and RT-DETRv4-X-only controls before progressive YOLO26x → RT-DETRv4-X training. Test quality-aware dual-teacher fusion only after both teachers provide independent value. Prefer cached output targets; do not require either teacher at inference.

## Phase 7 — Deployment

Export ONNX, test OpenCV 5 DNN, ONNX Runtime, OpenVINO, and TensorRT. Run PTQ before QAT. Measure prediction parity and real latency on each supported runtime.

## Phase 8 — Final research release

Complete the ablation matrix, Pareto plots, failure analysis, technical report, README, model card, dataset card, demo, and reproducibility instructions.
