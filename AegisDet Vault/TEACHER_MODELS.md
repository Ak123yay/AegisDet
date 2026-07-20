---
title: "Locked Teacher Models"
project: "AegisDet-Pro v5.1"
area: "project-control"
status: "locked"
tags: ["teacher", "distillation", "yolo26x", "rt-detrv4"]
---

# Locked Teacher Models

## Final decision

AegisDet-Pro uses two training-only teacher models:

| Role | Locked teacher | Why |
|---|---|---|
| Primary same-family teacher | **Ultralytics YOLO26x — `yolo26x.pt`** | Same detector family as the YOLO26n-derived student; easiest teacher for class, box, and optional selected-feature transfer |
| Secondary architecture-diverse teacher | **RT-DETRv4-X** | End-to-end DETR-style detector with a different global-reasoning and matching bias |
| Fallback secondary teacher | **RT-DETRv2-X** | Use only if RT-DETRv4-X custom fine-tuning or output extraction becomes a verified blocker |

The official Ultralytics size name is **YOLO26x**, not “YOLO26 XL.”

## Student and deployment

- Student / starting detector: `yolo26n.pt`, fine-tuned on the locked domain.
- Final deployed model: the small AegisDet student.
- Teachers are used only during training or offline target generation.
- Neither YOLO26x nor RT-DETRv4-X is required at inference.

## Required teacher preparation

Both teachers must be fine-tuned on the exact same domain taxonomy before they teach the student.

```text
COCO-pretrained checkpoint
→ replace or adapt class head
→ fine-tune on wildlife training split
→ evaluate on frozen validation split
→ calibrate scores
→ freeze teacher checkpoint
→ generate distillation targets
```

Do not distill directly from raw COCO predictions into the seven-class wildlife student.

## Locked progressive schedule

### Stage 0 — No-KD control

Train the final student architecture using ground-truth labels only. This is the mandatory control.

### Stage 1 — YOLO26x same-family distillation

Use YOLO26x first because it is structurally closer to the YOLO26n-derived student.

Recommended initial transfer:
- class probability or logit distillation,
- bounding-box / IoU-aware distillation,
- high-confidence pseudo-label recovery,
- optional selected-feature transfer only after output-level KD works.

### Stage 2 — RT-DETRv4-X heterogeneous distillation

Use RT-DETRv4-X after the same-family KD baseline is stable.

Recommended initial transfer:
- high-confidence class probabilities,
- box and localization targets,
- teacher-student disagreement on hard examples,
- global/hard-case supervision.

Do **not** start with direct feature matching between RT-DETRv4-X and AegisDet. Their internal representations differ substantially.

### Stage 3 — Quality-aware dual-teacher distillation

Only after both teachers improve the student independently:

- select the more reliable teacher per object or frame,
- weight teachers using validation-calibrated confidence,
- use agreement as a strong soft target,
- use disagreement as a hard-example signal,
- never average contradictory teacher boxes blindly.

## Hardware plan

Do not keep both X-size teachers and the student in GPU memory simultaneously on the local development GPU.

Preferred workflow:

1. Fine-tune one teacher at a time.
2. Freeze it.
3. Generate offline teacher targets.
4. Save targets in a common normalized format.
5. Train the student from cached targets.
6. Use online feature distillation only for a small controlled YOLO26x experiment if memory permits.

Cloud or Colab GPUs may be used for teacher fine-tuning. The final student training and inference benchmark remain reproducible and separately documented.

## Common cached-target schema

Each teacher-target record should contain:

```yaml
image_id: string
teacher: yolo26x | rtdetrv4x
teacher_checkpoint_sha256: string
input_size: [height, width]
class_map_version: string
boxes_xyxy_normalized: list
class_probabilities: list
confidence: list
augmentation_id: string
source_split: train
```

Never cache targets for validation or test images for training.

## Initial loss plan

Begin with a conservative loss rather than a large untested stack:

```text
L_total =
    L_ground_truth
  + λ_yolo_cls  · L_YOLO26x_class
  + λ_yolo_box  · L_YOLO26x_box
  + λ_detr_cls  · L_RTDETRv4_class
  + λ_detr_box  · L_RTDETRv4_box
  + λ_hard      · L_hard_example
```

Weights are hyperparameters to ablate. They are not fixed “perfect” constants.

## Acceptance rules

A teacher or loss stays only if it produces a reproducible gain over:

1. the no-KD student,
2. the single-teacher control,
3. an equal-training-budget control.

The final inference graph and latency must remain unchanged by training-only distillation.

## Sources

- Ultralytics YOLO26 documentation and model table: https://docs.ultralytics.com/models/yolo26/
- Ultralytics repository/model table: https://github.com/ultralytics/ultralytics
- Official RT-DETRv4 repository: https://github.com/RT-DETRs/RT-DETRv4
- RT-DETRv4 paper: https://arxiv.org/abs/2510.25257
- Official RT-DETR / RT-DETRv2 repository: https://github.com/lyuwenyu/RT-DETR

## Related notes

- [[FOUNDATION_MODEL]]
- [[wiki/distillation/teacher-selection]]
- [[wiki/distillation/progressive-teacher-schedule]]
- [[wiki/experiments/distillation/exp-040-single-teacher-kd]]
- [[wiki/experiments/distillation/exp-041-progressive-teacher-kd]]
- [[wiki/experiments/distillation/exp-043-dual-teacher-kd]]
