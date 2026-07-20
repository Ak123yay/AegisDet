# TASKS.md — AegisDet Work State

_This file is the single source of truth. Update it after every session._

## Done

- [x] Define the AegisDet-Pro thesis.
- [x] Lock CNN-first selective-compute architecture.
- [x] Lock `yolo26n.pt` as the primary base detector.
- [x] Lock wildlife/roadside-animal detection as the first domain.
- [x] Lock initial seven-class taxonomy.
- [x] Build the Obsidian/RAG vault and starter code.
- [x] Add source-backed research notes.
- [x] Add vault quality audit scripts.

## Active — Phase 0

Execution rule: complete the first unchecked task. Do not jump to later phases.

- [ ] Run `project-code/scripts/bootstrap_windows.ps1` or manually create `.venv`.
- [ ] Install the correct CUDA-enabled PyTorch build.
- [ ] Install `project-code/requirements.txt`.
- [ ] Run `python project-code/scripts/check_environment.py`.
- [ ] Save environment output to `output/environment-check.txt`.
- [ ] Run one pretrained `yolo26n.pt` inference.
- [ ] Confirm training/export modes are available.
- [ ] Freeze dependencies to `project-code/requirements-lock.txt`.
- [ ] Pass [[wiki/timeline/phase-0-gate]].

## Phase 1 — Baseline

- [ ] Finalize dataset sources and licenses.
- [ ] Collect and label dataset v1.
- [ ] Audit labels, class balance, duplicates, and split leakage.
- [ ] Train frozen YOLO26n baseline at 416×416.
- [ ] Evaluate mAP50, mAP50-95, precision, recall, and small-object AP.
- [ ] Export ONNX and verify parity.
- [ ] Benchmark p50, p90, p99, memory, and model size.
- [ ] Build baseline failure gallery.
- [ ] Pass [[wiki/timeline/phase-1-gate]].

## Phase 2 — AegisDet-Mini

- [ ] Connect `UltralyticsAdapter` to the frozen checkpoint.
- [ ] Calibrate rule-router thresholds on validation data.
- [ ] Run selective crop refinement.
- [ ] Verify remapping and merge tests.
- [ ] Compare baseline and AegisDet-Mini under equal conditions.
- [ ] Pass [[wiki/timeline/phase-2-gate]].

## Later phases

- [ ] Phase 3: hard-negative active learning and dataset v2.
- [ ] Phase 4: K-token global context and placement ablations.
- [ ] Phase 5: learned router and compute penalty.
- [ ] Phase 6: distillation.
- [ ] Phase 7: ONNX, OpenCV 5, ORT, OpenVINO, TensorRT, PTQ/QAT.
- [ ] Phase 8: final ablations, report, release, and demo.
