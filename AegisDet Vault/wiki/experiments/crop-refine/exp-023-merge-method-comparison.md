---
title: "EXP 023 — Merge Method Comparison"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 023 — Merge Method Comparison

## Research question
Which merge method best resolves base/crop duplicates without suppressing valid nearby animals?

## Hypothesis
Class-aware NMS will be a strong simple default; a merge/fusion alternative may help localization but could create score artifacts.

## Frozen control
Identical base and crop prediction sets, classes, thresholds, and evaluator.

## Independent variable
Merge algorithm and its IoU/score parameters.

## Procedure
1. Cache raw base and remapped crop detections.
2. Apply class-aware NMS and one justified alternative offline.
3. Evaluate crowded/overlap and isolated subsets.
4. Inspect class conflicts and localization.
5. Lock the simplest adequate method.

## Required metrics
- precision/recall/mAP
- duplicate count
- nearby-object suppression errors
- localization IoU
- postprocessing latency

## Acceptance criterion
Keep the simplest method on the Pareto frontier with no systematic crowded-scene failure.

## Rejection or rollback criterion
Reject complex fusion when gains are negligible, scores become miscalibrated, or runtime/export integration worsens.

## Required outputs
- `reports/merge_comparison.csv`
- `reports/merge_failure_examples/`
- `configs/merge_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/crop-refine/crop-merge-logic]]
- [[dev/tests/merge-logic-test]]
