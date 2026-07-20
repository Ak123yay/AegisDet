---
title: "EXP 012 — Learned Router"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 5"
status: "blocked"
tags: ["experiment", "phase-5"]
---

# EXP 012 — Learned Router

## Research question
Can a compact learned router outperform the locked rule router at the same refinement budget?

## Hypothesis
A learned model using detection summaries may improve benefit prediction, but only if route labels are reliable and compute overhead is negligible.

## Frozen control
Locked rule router, same base/crop outputs, same train/validation/test route-label split.

## Independent variable
Learned router architecture, features, loss, and compute penalty.

## Procedure
1. Build labels from whether optional processing corrects each frame.
2. Train a tiny MLP or shallow model using training route labels.
3. Tune threshold/penalty on validation.
4. Measure router inference overhead.
5. Compare at matched refinement rates on test.

## Required metrics
- benefit precision/recall and AUROC where applicable
- final detector metrics
- matched refinement rate
- router latency and size
- false-skip analysis

## Acceptance criterion
Keep only when the learned router produces a reproducible Pareto improvement over rules after including its own overhead.

## Rejection or rollback criterion
Reject if labels leak test information, overhead erases gains, or improvement disappears at matched route rate.

## Required outputs
- `reports/learned_router_metrics.json`
- `reports/router_comparison.csv`
- `models/router_artifact.*`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/router/learned-router-v2]]
- [[distillation/compute-penalty]]
