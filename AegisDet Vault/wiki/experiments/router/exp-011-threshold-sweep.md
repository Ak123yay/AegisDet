---
title: "EXP 011 — Router Threshold Sweep"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 011 — Router Threshold Sweep

## Research question
Which validation-tuned threshold combination provides the best accuracy/latency operating point?

## Hypothesis
A moderate small-area and confidence interval will outperform extremely aggressive or conservative routing.

## Frozen control
Frozen checkpoint, validation predictions, crop policy, merge policy, and benchmark implementation.

## Independent variable
Small-area ratio, uncertainty interval/count, overlap trigger, and maximum route frequency.

## Procedure
1. Declare a finite threshold grid.
2. Evaluate every setting on validation only.
3. Plot corrected-error rate and accuracy against refinement rate and latency.
4. Choose one operating point using a written deployment preference.
5. Lock it before test evaluation.

## Required metrics
- mAP50-95
- small-object AP/recall
- refinement rate
- benefit precision/recall
- p50/p90/p99 latency

## Acceptance criterion
Select a non-dominated validation point with bounded tail latency and a clearly stated reason.

## Rejection or rollback criterion
Reject any threshold chosen from the test set or from one qualitative example.

## Required outputs
- `reports/router_threshold_grid.csv`
- `reports/router_pareto.png`
- `configs/router_v1_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/router/router-thresholds]]
- [[metrics/refinement-rate]]
