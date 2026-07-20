---
title: "YOLO26"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# YOLO26

## Summary
YOLO26 is the locked primary detector family. The official nano checkpoint is the pretrained starting point and the frozen control after domain fine-tuning.

## What the source establishes
Official documentation describes `yolo26n.pt` as supporting prediction, training, validation, and export. The detection family uses a default one-to-one end-to-end path and a one-to-many alternative, removes DFL, and documents Progressive Loss, STAL, and MuSGD.

## AegisDet use
Use the COCO-pretrained nano checkpoint for baseline training. Preserve both end-to-end and one-to-many export tests when runtime compatibility differs.

## What not to copy blindly
Do not assume official COCO/T4 numbers are local wildlife results. Do not reproduce the entire training recipe before a basic domain baseline works.

## Implementation consequence
Load `yolo26n.pt`, fine-tune at 416×416, freeze the best checkpoint, export ONNX, and compare all wrapper variants using the same checkpoint.

## Required evaluation
Prediction parity, mAP50-95, small-object metrics, p50/p90/p99 latency, model size, and one-to-one versus one-to-many runtime behavior.

## Sources
- https://docs.ultralytics.com/models/yolo26/
- https://arxiv.org/abs/2606.03748
- https://github.com/ultralytics/ultralytics

## Related notes
- [[FOUNDATION_MODEL]]
- [[experiments/baseline/exp-001-yolo-nano-baseline]]
- [[deployment/operator-compatibility]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
