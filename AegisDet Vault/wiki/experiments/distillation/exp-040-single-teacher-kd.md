---
title: "EXP 040 — YOLO26x Single-Teacher Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6", "yolo26x"]
---

# EXP 040 — YOLO26x Single-Teacher Distillation

## Research question

Does a domain-fine-tuned YOLO26x teacher improve the fixed AegisDet student without changing inference cost?

## Hypothesis

YOLO26x is the most compatible first teacher because it shares the YOLO26 family with the YOLO26n-derived student.

## Frozen control

Final pre-KD student architecture, dataset, augmentation, total epochs, and no-KD seed-matched run.

## Independent variable

YOLO26x output-level distillation:
- class/logit term,
- box/IoU term,
- optional high-confidence missed-object recovery.

## Procedure

1. Fine-tune YOLO26x on the locked training split.
2. Evaluate and calibrate it on validation.
3. Freeze the checkpoint and hash.
4. Generate cached targets for training images.
5. Train no-KD and KD matched runs.
6. Confirm the student inference graph and latency remain unchanged.

## Required metrics

- student mAP50-95,
- small-object AP and recall,
- per-class change,
- calibration,
- training stability,
- inference latency parity,
- teacher-student disagreement.

## Acceptance criterion

Keep if the gain is reproducible across at least two seeds or is large enough to justify a confirmatory run, with no inference overhead.

## Required outputs

- `reports/yolo26x_single_teacher_kd.json`
- `reports/yolo26x_teacher_validation.json`
- `configs/kd_yolo26x_locked.yaml`
- cached-target manifest with teacher checkpoint hash

## Result

**Not run.** Do not use official COCO values as project results.

## Related notes

- [[TEACHER_MODELS]]
- [[distillation/teacher-selection]]
- [[distillation/logit-distillation]]
- [[distillation/box-distillation]]
