---
title: "EXP 030 — K4 Global Tokens"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 4"
status: "blocked"
tags: ["experiment", "phase-4"]
---

# EXP 030 — K4 Global Tokens

## Research question
Do four learned global tokens improve hard-case context over AegisDet-Mini?

## Hypothesis
Four tokens may add scene context with minimal overhead but may underrepresent complex scenes.

## Frozen control
Best Phase-3 student/data, same head/neck/router/crop path and training recipe.

## Independent variable
One K=4 context bridge at the locked initial stage.

## Procedure
1. Implement and shape-test the module.
2. Export ONNX before full training.
3. Train with the frozen recipe.
4. Evaluate full and hard subsets.
5. Measure real runtime and memory.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
Keep as a candidate only if context improves the predeclared hard-case target and export/runtime remain viable.

## Rejection or rollback criterion
Reject if it adds no measurable benefit or creates unsupported/slow graph operations.

## Required outputs
- `reports/k4_metrics.json`
- `reports/k4_export_log.txt`
- `reports/k4_failures/`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/global-context/tiny-global-token-context]]
- [[research/models/mobile-former]]
