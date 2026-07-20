---
title: "Progressive Teacher Schedule"
project: "AegisDet-Pro v5.1"
area: "distillation"
status: "locked-specification"
tags: ["distillation", "progressive-kd", "multi-teacher"]
---

# Progressive Teacher Schedule

## Stage 0 — Ground-truth-only control

Train the fixed student architecture without distillation. Preserve this checkpoint and training budget as the mandatory control.

## Stage 1 — YOLO26x

Distill from the fine-tuned YOLO26x teacher.

Initial losses:
- class/logit distillation,
- box or IoU-aware localization distillation,
- high-confidence missed-object recovery.

Selected feature distillation is optional only after output-level KD demonstrates value.

## Stage 2 — RT-DETRv4-X

Continue from the best Stage 1 student or run a matched independent RT-DETRv4-X-only control.

Initial transfer:
- class distributions,
- matched boxes,
- difficult-object targets,
- disagreement-based hard-example weighting.

Avoid direct feature matching initially because the DETR and YOLO internal structures are heterogeneous.

## Stage 3 — Quality-aware dual teacher

Use both teachers only after they independently improve the student.

Fusion rules:
- trust teacher agreement strongly,
- choose a teacher per object/frame using validation-calibrated reliability,
- use disagreement as a signal for hard-example review,
- reject low-confidence or contradictory pseudo labels,
- never average boxes merely because two teachers emitted them.

## Equal-budget requirement

The progressive schedule must be compared to:
- the same number of total epochs without KD,
- the best single-teacher run with the same compute budget,
- and a fresh-seed repeat.

## Hardware strategy

Prefer cached output targets to running both X-size teachers online. Train or infer teachers one at a time. Online feature KD is a separate optional experiment.

## Acceptance rule

Progressive KD stays only if it produces a reproducible gain beyond the strongest equal-budget single-teacher result while preserving the final student inference graph.
