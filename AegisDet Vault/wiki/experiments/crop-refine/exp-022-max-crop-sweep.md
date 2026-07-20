---
title: "EXP 022 — Maximum Crop Sweep"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 022 — Maximum Crop Sweep

## Research question
How many crops per frame provide useful recall before tail latency and duplicates become unacceptable?

## Hypothesis
Two crops will likely provide a better bounded tradeoff than one or four on this domain, but the result must be measured.

## Frozen control
Locked checkpoint, routed frames, crop ranking, crop resolution, padding, and merge.

## Independent variable
Maximum crops per frame: 1, 2, and 4.

## Procedure
1. Freeze candidate ranking.
2. Run each cap on the same images.
3. Record selected and discarded candidates.
4. Measure corrected objects and duplicates.
5. Compare latency percentiles and worst frames.

## Required metrics
- mAP/small-object recall
- corrections per extra crop
- refinement detector calls
- p90/p99 latency
- duplicate/false-positive rate

## Acceptance criterion
Select the smallest cap on the useful Pareto frontier, with an explicit p99 bound.

## Rejection or rollback criterion
Reject higher caps when marginal corrections do not justify extra tail cost.

## Required outputs
- `reports/max_crop_sweep.csv`
- `reports/max_crop_tail_frames/`
- `configs/max_crops_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/crop-refine/maximum-crops-per-frame]]
- [[architecture/system/bounded-adaptivity]]
