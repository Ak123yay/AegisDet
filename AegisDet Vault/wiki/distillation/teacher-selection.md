---
title: "Teacher Selection"
project: "AegisDet-Pro v5.1"
area: "distillation"
status: "locked-specification"
tags: ["distillation", "yolo26x", "rt-detrv4-x"]
---

# Teacher Selection

## Locked teachers

1. **YOLO26x (`yolo26x.pt`)** — primary same-family teacher.
2. **RT-DETRv4-X** — secondary architecture-diverse teacher.
3. **RT-DETRv2-X** — fallback only if v4 custom training or target extraction is blocked.

## Selection rationale

YOLO26x and the YOLO26n-derived student share a detector family, making class and localization transfer more direct. RT-DETRv4-X provides a different end-to-end transformer bias and stronger global representation. The purpose of the second teacher is complementary supervision, not merely a second set of similar predictions.

## Required preparation

- Fine-tune each teacher on the same domain classes and training split.
- Evaluate each teacher separately on the frozen validation split.
- Calibrate class confidence before teacher fusion.
- Freeze checkpoint hashes and class mappings.
- Generate training targets only for training images.

## Output-level transfer first

Start with common output targets:
- normalized boxes,
- class probabilities,
- confidence,
- object matching,
- hard-example disagreement.

Do not begin cross-architecture feature distillation from RT-DETRv4-X.

## Independent controls

Required matched runs:
1. no distillation,
2. YOLO26x only,
3. RT-DETRv4-X only,
4. progressive YOLO26x → RT-DETRv4-X,
5. dual-teacher quality-aware fusion.

## Decision rule

Keep a teacher only when it produces a reproducible student gain at equal inference cost. Keep the two-teacher plan only when it beats the best single-teacher result under an equal training budget.

## Related notes

- [[TEACHER_MODELS]]
- [[distillation/progressive-teacher-schedule]]
- [[experiments/distillation/exp-040-single-teacher-kd]]
- [[experiments/distillation/exp-041-progressive-teacher-kd]]
- [[experiments/distillation/exp-043-dual-teacher-kd]]
