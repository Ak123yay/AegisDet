---
title: "EXP 042 — Hard-Example Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6"]
---

# EXP 042 — Hard-Example Distillation

## Research question
Does weighting teacher guidance on mined difficult examples improve the target failure categories?

## Hypothesis
Focused KD may help small/occluded/uncertain cases more efficiently than uniform weighting.

## Frozen control
Best KD recipe and same training budget.

## Independent variable
Hard-example definition and KD weight schedule.

## Procedure
1. Define hard examples without test data.
2. Create weights from failure/uncertainty labels.
3. Train matched uniform and hard-weighted KD.
4. Evaluate category-level changes.
5. Inspect overfitting to mined examples.

## Required metrics
- hard-category AP/recall
- overall mAP
- calibration
- training stability
- unseen-hard-case performance

## Acceptance criterion
Keep only if the targeted category improves without unacceptable overall or calibration regression.

## Rejection or rollback criterion
Reject if it memorizes mined examples or harms normal/easy performance disproportionately.

## Required outputs
- `reports/hard_example_kd.json`
- `reports/hard_kd_categories.csv`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[distillation/hard-example-distillation]]
