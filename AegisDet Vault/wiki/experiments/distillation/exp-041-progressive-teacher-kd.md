---
title: "EXP 041 — Progressive Teacher Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6"]
---

# EXP 041 — Progressive Teacher Distillation

## Research question
Does a sequence of teachers outperform the single-teacher KD baseline?

## Hypothesis
Gradual transfer from a close teacher to a stronger or heterogeneous teacher may reduce mismatch.

## Frozen control
Locked student, data, budget, and best single-teacher recipe.

## Independent variable
Teacher sequence/order and stage schedule.

## Procedure
1. Define teacher sequence and stage checkpoints.
2. Train matched total-budget control.
3. Preserve intermediate student states.
4. Compare final and stage-wise behavior.
5. Analyze whether gains come from extra training time.

## Required metrics
- student accuracy/hard metrics
- total training compute
- stage stability
- inference parity
- comparison with equal-budget single teacher

## Acceptance criterion
Keep only if it beats the equal-budget single-teacher control reproducibly.

## Rejection or rollback criterion
Reject if improvement is attributable only to extra epochs or if heterogeneous transfer destabilizes localization.

## Required outputs
- `reports/progressive_kd.json`
- `reports/kd_stage_metrics.csv`
- `configs/kd_progressive_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[research/papers/progressive-multi-teacher-distillation]]
