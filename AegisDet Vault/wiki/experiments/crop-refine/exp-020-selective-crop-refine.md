---
title: "EXP 020 — Selective Crop Refinement"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 020 — Selective Crop Refinement

## Research question
Does bounded selective crop reinference improve difficult wildlife detections over the frozen baseline?

## Hypothesis
Rerunning the same detector on at most two padded small/uncertain regions will improve small-object recall/AP while adding less average cost than full slicing.

## Frozen control
Frozen YOLO26n checkpoint and baseline predictions; router, crop, remap, and merge settings are recorded.

## Independent variable
Enable versus disable selective crop refinement.

## Procedure
1. Validate remap and merge unit tests.
2. Run baseline and adaptive pipeline on identical validation/test images.
3. Record every selected crop and route reason.
4. Measure end-to-end time including all Python/OpenCV logic.
5. Compare failure categories and duplicates.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
Keep when it meets the predeclared small-object or EdgeScore improvement and tail-latency limit. Declare the numeric threshold before the final test run.

## Rejection or rollback criterion
Modify/reject if duplicates or false positives erase recall gains, refinement rate is excessive, or p99 violates the deployment budget.

## Required outputs
- `reports/crop_refine_predictions.jsonl`
- `reports/crop_refine_metrics.json`
- `reports/crop_visualizations/`
- `reports/crop_latency_samples.csv`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/crop-refine/selective-crop-refinement]]
- [[research/models/sahi]]
