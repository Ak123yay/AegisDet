---
title: "Foundation Model and Base Detector"
project: "AegisDet-Pro v5.1"
area: "project-control"
status: "locked"
tags: ["foundation-model", "baseline", "teacher-models"]
---

# Foundation Model and Base Detector

## Locked answer

AegisDet-Pro is not based on a language or vision-language foundation model at inference. Its pretrained starting point is an object detector:

> **Primary student/base detector: Ultralytics YOLO26n using the official COCO-pretrained `yolo26n.pt` checkpoint.**

YOLO11n is a temporary fallback only when a verified YOLO26 tooling or export issue blocks progress.

## Locked roles

| Role | Model |
|---|---|
| Pretrained student starting weights | `yolo26n.pt` |
| Frozen experimental control | Domain-fine-tuned YOLO26n at 416×416 |
| AegisDet-Mini fast path | Same frozen domain-fine-tuned YOLO26n |
| Primary teacher | **YOLO26x — `yolo26x.pt`** |
| Secondary diverse teacher | **RT-DETRv4-X** |
| Secondary fallback | RT-DETRv2-X, only if v4 is blocked |
| Final deployed student | Custom AegisDet-Pro configuration |

The official Ultralytics size suffix is **x**, not XL.

## Why YOLO26n is the student

YOLO26 officially provides nano through X checkpoints for training, validation, prediction, and export. YOLO26n is the correct small deployment control; YOLO26x is the strongest same-family teacher candidate.

## Why two teachers

- YOLO26x provides structurally compatible YOLO-family supervision.
- RT-DETRv4-X provides architecture-diverse end-to-end transformer supervision.
- Teachers are training-only; the final edge model remains small.
- Each teacher must prove independent value before combined use.

## Locked baseline configuration

```yaml
model: yolo26n.pt
input_size: 416
pretraining: COCO
initial_epochs: 50
primary_accuracy_metric: mAP50-95
secondary_metrics:
  - mAP50
  - precision
  - recall
  - small_object_AP
runtime_export: ONNX
initial_hardware: RTX 3060 Ti
```

## Required baseline discipline

- Fine-tune the student and both teachers on the same locked domain taxonomy.
- Freeze the YOLO26n baseline checkpoint for AegisDet-Mini comparisons.
- Do not alter weights, thresholds, image size, or validation data during an isolated router/crop experiment.
- Compare final models under the same runtime, device, precision, and input resolution.
- Do not use teacher predictions from the validation or test split to train the student.

## Sources

- Ultralytics YOLO26 documentation: https://docs.ultralytics.com/models/yolo26/
- Ultralytics repository: https://github.com/ultralytics/ultralytics
- Official RT-DETRv4 repository: https://github.com/RT-DETRs/RT-DETRv4
- RT-DETRv4 paper: https://arxiv.org/abs/2510.25257

## Related notes

- [[TEACHER_MODELS]]
- [[DOMAIN_LOCK]]
- [[wiki/research/models/yolo26]]
- [[wiki/research/models/yolo26x]]
- [[wiki/research/models/rt-detrv4-x]]
- [[wiki/experiments/baseline/exp-001-yolo-nano-baseline]]
- [[wiki/benchmarking/same-backend-rule]]
