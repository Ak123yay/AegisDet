---
title: "EXP 040 — Single-Teacher Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6"]
---

# EXP 040 — Single-Teacher Distillation

## Research question
Does a stronger compatible teacher improve the fixed AegisDet student without inference cost?

## Hypothesis
A YOLO26s teacher may improve student logits/localization with a simpler stable baseline before progressive KD.

## Frozen control
Final pre-KD student architecture/data/training budget and no-KD run.

## Independent variable
One teacher and a minimal declared KD loss.

## Procedure
1. Evaluate teacher domain quality.
2. Map classes/outputs.
3. Train no-KD and KD matched runs.
4. Track loss stability.
5. Evaluate final student and confirm unchanged inference graph.

## Required metrics
- student mAP/hard metrics
- training stability
- inference latency parity
- teacher/student disagreement
- per-class gains

## Acceptance criterion
Keep only if student benefit is reproducible without inference overhead or severe training instability.

## Rejection or rollback criterion
Reject if teacher errors transfer, result is seed-sensitive, or complexity is not justified.

## Required outputs
- `reports/single_teacher_kd.json`
- `configs/kd_single_locked.yaml`
- `reports/kd_failures/`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[distillation/teacher-selection]]
- [[distillation/logit-distillation]]
