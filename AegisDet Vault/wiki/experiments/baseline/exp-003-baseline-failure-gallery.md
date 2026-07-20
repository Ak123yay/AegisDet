---
title: "EXP 003 — Baseline Failure Gallery"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 1"
status: "planned"
tags: ["experiment", "phase-1"]
---

# EXP 003 — Baseline Failure Gallery

## Research question
Which failure categories dominate the frozen YOLO26n baseline?

## Hypothesis
Tiny distance, occlusion, low light, blur, and hard-negative textures will account for a meaningful fraction of errors and guide later routing/data work.

## Frozen control
Frozen checkpoint, test predictions, confidence policy, and ground truth.

## Independent variable
Error-category labeling of baseline predictions.

## Procedure
1. Export per-image predictions and matching information.
2. Sample and review true positives, false positives, false negatives, and localization errors.
3. Assign one primary and optional secondary failure tags.
4. Count frequency by class, scale, lighting, and category.
5. Select examples for later regression tests.

## Required metrics
- false positives and false negatives by category
- small/occluded/low-light recall
- confidence distributions
- class confusion
- localization-error frequency

## Acceptance criterion
Accept when at least the major error categories are reproducibly defined and every example links to model/config/data metadata.

## Rejection or rollback criterion
Reject anecdotal galleries with no counts, cherry-picked successes, or ambiguous ground truth.

## Required outputs
- `reports/failure_gallery/index.csv`
- `reports/failure_gallery/images/`
- `reports/failure_summary.json`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[failure-cases/_failure-index]]
- [[data/active-learning/failure-case-curation]]
