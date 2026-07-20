---
title: "Foundation Model and Base Detector"
project: "AegisDet-Pro v5.1"
area: "project-control"
status: "locked"
tags: ["foundation-model", "baseline"]
---

# Foundation Model and Base Detector

## Locked answer

AegisDet-Pro is **not** built on a general-purpose foundation model such as a vision-language model. Its pretrained starting point is an object detector:

> **Primary base detector: Ultralytics YOLO26n using the official COCO-pretrained `yolo26n.pt` checkpoint.**

YOLO11n is a temporary fallback only when a verified YOLO26 tooling or export issue blocks progress. A fallback run must be labeled clearly and must not replace the final YOLO26n comparison silently.

## Roles

| Role | Locked model |
|---|---|
| Pretrained starting weights | `yolo26n.pt` |
| Frozen experimental control | Domain-fine-tuned YOLO26n at 416×416 |
| AegisDet-Mini fast path | Same frozen fine-tuned YOLO26n |
| First close teacher candidate | YOLO26s |
| Stronger later teacher candidates | YOLO26m or RT-DETR, after teacher evaluation |
| Final student | Custom AegisDet-Pro configuration |

## Why YOLO26n

YOLO26 officially supports training, validation, prediction, and export for `yolo26n.pt`. Its deployment-oriented design includes an end-to-end one-to-one path, a one-to-many fallback, DFL-free regression, and a documented training recipe. This makes it a stronger and more defensible control than an outdated nano detector.

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

- Fine-tune the detector on the locked wildlife dataset.
- Freeze the resulting checkpoint for all AegisDet-Mini wrapper comparisons.
- Do not alter weights, thresholds, image size, or validation data during a supposedly isolated router/crop experiment.
- Compare final models under the same runtime, device, precision, and input resolution.

## Sources

- Ultralytics YOLO26 documentation: https://docs.ultralytics.com/models/yolo26/
- Ultralytics supported models: https://docs.ultralytics.com/models/
- YOLO26 preprint: https://arxiv.org/abs/2606.03748

## Related notes

- [[DOMAIN_LOCK]]
- [[wiki/research/models/yolo26]]
- [[wiki/experiments/baseline/exp-001-yolo-nano-baseline]]
- [[wiki/benchmarking/same-backend-rule]]
