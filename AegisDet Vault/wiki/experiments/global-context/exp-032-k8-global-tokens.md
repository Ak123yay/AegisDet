---
title: "EXP 032 — K8 Global Tokens"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 4"
status: "blocked"
tags: ["experiment", "phase-4"]
---

# EXP 032 — K8 Global Tokens

## Research question
Does increasing capacity to eight tokens improve context enough to justify extra cost?

## Hypothesis
K8 may improve difficult scene representation but risks diminishing returns and memory/latency overhead.

## Frozen control
Identical no-context/K4/K6 setup.

## Independent variable
Token count K=8.

## Procedure
1. Train and export K8 with matched settings.
2. Measure actual rather than FLOP-only overhead.
3. Compare hard categories and calibration.
4. Add to K-token Pareto table.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
Keep only if K8 dominates or serves a justified high-accuracy operating point.

## Rejection or rollback criterion
Reject if it is dominated by K4/K6 or damages export/tail latency.

## Required outputs
- `reports/k8_metrics.json`
- `reports/k8_export_log.txt`
- `reports/k_token_comparison.csv`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[global-context/exp-031-k6-global-tokens]]
