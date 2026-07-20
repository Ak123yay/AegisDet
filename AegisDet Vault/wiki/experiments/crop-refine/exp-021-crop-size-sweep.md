---
title: "EXP 021 — Crop Size Sweep"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 021 — Crop Size Sweep

## Research question
Which crop inference resolution balances target detail, context, and runtime?

## Hypothesis
An intermediate crop size will outperform very small crops that lose detail and large crops that add cost/background.

## Frozen control
Locked routed frame set, checkpoint, crop origins/padding, merge, and backend.

## Independent variable
Crop detector input resolution: planned 256, 320, and 416, adjusted only if model/runtime constraints require.

## Procedure
1. Precompute and freeze crop regions from validation.
2. Run each resolution on the same crops.
3. Measure local and merged outputs.
4. Compare detail recovery, context errors, and latency.
5. Select one resolution and lock it.

## Required metrics
- small-object AP/recall
- crop-only correction rate
- new false positives
- per-crop and end-to-end latency
- memory

## Acceptance criterion
Select a non-dominated resolution; no largest-resolution default without measured benefit.

## Rejection or rollback criterion
Reject a resolution with unstable resize behavior, export mismatch, or cost disproportionate to accuracy gain.

## Required outputs
- `reports/crop_size_sweep.csv`
- `reports/crop_size_examples/`
- `configs/crop_size_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/crop-refine/crop-selection]]
- [[benchmarking/latency-measurement-protocol]]
