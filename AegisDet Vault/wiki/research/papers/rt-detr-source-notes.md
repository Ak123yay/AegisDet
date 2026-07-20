---
title: "RT-DETR"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "teacher-candidate"
tags: ["research-model", "source-backed"]
---

# RT-DETR — Source Notes

## Summary
RT-DETR is a possible stronger teacher, not the initial deployment student.

## What the source establishes
It is a real-time end-to-end transformer detector and may provide global localization/classification supervision.

## AegisDet use
Evaluate it as a teacher only after a same-family YOLO teacher baseline exists.

## What not to copy blindly
Do not replace the student with a DETR decoder or assume heterogeneous distillation will work automatically.

## Implementation consequence
Cache teacher outputs, map classes exactly, and compare student gains against teacher cost-free inference.

## Required evaluation
Teacher domain accuracy, distillation stability, student result, and training cost.

## Sources
- https://arxiv.org/abs/2304.08069

## Related notes
- [[distillation/teacher-selection]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
