---
title: "QAT Plan"
project: "AegisDet-Pro v5.1"
area: "quantization"
status: "specification"
tags: ["quantization"]
---

# QAT Plan

## Purpose
Define the quantization behavior for quantization-aware retraining used only when PTQ loss exceeds the locked limit.

## Project specification
Use a representative calibration set spanning easy backgrounds, hard negatives, small objects, low light, and occlusion. Compare FP32/FP16/INT8 on the same test data and runtime. Inspect score calibration, small-object recall, localization, and router behavior—not only average mAP.

## Evidence required
- Calibration-set manifest
- Artifact and runtime configuration
- Pre/post accuracy and latency
- Failure-category comparison
- Acceptable-loss threshold applied

## Decision rule
Use PTQ first. Run QAT only when PTQ fails a predeclared accuracy or calibration threshold and the target runtime provides a meaningful deployment benefit.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[quantization/int8-strategy]]
- [[experiments/quantization/exp-050-ptq-int8]]

## Retrieval terms
aegisdet, edge-ai, plan, qat.
