---
title: "Teacher Selection"
project: "AegisDet-Pro v5.1"
area: "distillation"
status: "specification"
tags: ["distillation"]
---

# Teacher Selection

## Purpose
Define the training-only method for the stronger detector used to provide soft or feature supervision.

## Project specification
Specify teacher checkpoint, class mapping, cached versus online outputs, student checkpoint, loss formula, temperature/weight, schedule, hard-example policy, and baseline with no KD. Distillation must not alter inference architecture unless separately declared.

## Evidence required
- Teacher quality evaluated
- No-KD control
- Loss and schedule recorded
- Training stability plots
- Student accuracy and unchanged inference latency

## Decision rule
Keep only a distillation term that provides reproducible student benefit. A larger training loss stack is not automatically better.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[experiments/distillation/exp-040-single-teacher-kd]]
- [[research/papers/progressive-multi-teacher-distillation]]

## Retrieval terms
aegisdet, edge-ai, selection, teacher.
