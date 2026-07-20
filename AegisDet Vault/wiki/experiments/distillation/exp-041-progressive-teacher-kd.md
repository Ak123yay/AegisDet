---
title: "EXP 041 — Progressive YOLO26x to RT-DETRv4-X Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6", "progressive-kd"]
---

# EXP 041 — Progressive YOLO26x to RT-DETRv4-X Distillation

## Research question

Does a progressive sequence of YOLO26x followed by RT-DETRv4-X outperform the strongest equal-budget single-teacher run?

## Hypothesis

The same-family teacher can stabilize class and localization transfer first; the architecture-diverse teacher may then improve hard cases and global context.

## Frozen control

Locked student, data, augmentation, total training budget, best YOLO26x-only result, and RT-DETRv4-X-only result.

## Independent variable

Teacher sequence and stage allocation:
1. YOLO26x,
2. RT-DETRv4-X.

## Procedure

1. Fine-tune and freeze both teachers.
2. Cache output-level targets separately.
3. Train the YOLO26x stage.
4. Continue with RT-DETRv4-X hard-case/output KD.
5. Preserve intermediate checkpoints.
6. Compare against equal-total-epoch controls.
7. Repeat the best configuration with a fresh seed.

## Required metrics

- final student accuracy,
- small/occluded/low-light subset results,
- total training compute,
- stage-wise stability,
- teacher disagreement,
- calibration,
- inference parity.

## Acceptance criterion

Keep only if it beats the best equal-budget single-teacher control reproducibly.

## Required outputs

- `reports/progressive_yolo26x_rtdetrv4x_kd.json`
- `reports/kd_stage_metrics.csv`
- `configs/kd_progressive_yolo26x_rtdetrv4x.yaml`

## Result

**Not run.**

## Related notes

- [[TEACHER_MODELS]]
- [[distillation/progressive-teacher-schedule]]
- [[research/models/yolo26x]]
- [[research/models/rt-detrv4-x]]
