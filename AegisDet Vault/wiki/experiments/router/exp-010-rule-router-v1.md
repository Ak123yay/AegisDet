---
title: "EXP 010 — Rule Router V1"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 2"
status: "planned"
tags: ["experiment", "phase-2"]
---

# EXP 010 — Rule Router V1

## Research question
Can interpretable output-derived signals identify frames that benefit from optional refinement?

## Hypothesis
Small-object count, near-threshold count, and overlap density will enrich for baseline errors/corrections compared with routing all frames or none.

## Frozen control
Frozen baseline predictions; optional crop result can be computed offline to label whether refinement helps.

## Independent variable
Rule-router signal combination and initial thresholds.

## Procedure
1. Compute signals for every validation frame.
2. Run optional refinement offline to determine correction benefit.
3. Compare signal distributions for benefited versus non-benefited frames.
4. Apply default rules without test-set tuning.
5. Log false skips, false refinements, and route reasons.

## Required metrics
- refinement rate
- benefit precision: fraction of routed frames helped
- benefit recall: fraction of helpable frames routed
- false-skip rate
- p90/p99 latency after integration
- final detection metrics

## Acceptance criterion
Keep V1 when it routes a meaningfully enriched set of helpful frames and preserves bounded compute. The numeric target must be written into the run note before test evaluation.

## Rejection or rollback criterion
Modify or reject if it refines nearly every frame, misses most helpable frames, or signal distributions do not correlate with correction.

## Required outputs
- `reports/router_signals.parquet`
- `reports/router_validation.json`
- `reports/router_curves.png`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/router/router-signals]]
- [[architecture/router/rule-based-router-v1]]
