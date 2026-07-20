---
title: "EXP 031 — K6 Global Tokens"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 4"
status: "blocked"
tags: ["experiment", "phase-4"]
---

# EXP 031 — K6 Global Tokens

## Research question
Do six learned tokens improve the context-cost tradeoff relative to K4 and no context?

## Hypothesis
Six tokens, directly inspired by the few-token regime, may provide sufficient capacity at modest cost.

## Frozen control
Identical to K4 except token count and dependent parameter shape.

## Independent variable
Token count K=6.

## Procedure
1. Reuse the verified bridge.
2. Train with matched schedule/seed policy.
3. Export and benchmark.
4. Compare directly with no-context and K4.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
Keep only if K6 is non-dominated and improvement is reproducible.

## Rejection or rollback criterion
Reject if variance or overhead explains the apparent gain.

## Required outputs
- `reports/k6_metrics.json`
- `reports/k6_export_log.txt`
- `reports/k_token_comparison.csv`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[research/models/mobile-former]]
- [[global-context/exp-030-k4-global-tokens]]
