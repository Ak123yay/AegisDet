---
title: "EXP 033 — P4 versus P5 Context Placement"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 4"
status: "blocked"
tags: ["experiment", "phase-4"]
---

# EXP 033 — P4 versus P5 Context Placement

## Research question
At which deep feature level does the selected token count provide the best useful context?

## Hypothesis
P4 may retain more spatial detail while P5 may be cheaper and more semantic.

## Frozen control
Locked best token count, data, backbone, neck, head, training schedule, and runtime.

## Independent variable
Context insertion at P4, P5, and only if justified both.

## Procedure
1. Implement adapters with matched interfaces.
2. Shape/export test each placement.
3. Train matched variants.
4. Evaluate hard scale/occlusion categories.
5. Profile memory and latency.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
Select the non-dominated placement with stable export and the strongest intended hard-case result.

## Rejection or rollback criterion
Reject P4+P5 unless it provides benefit beyond either single placement that justifies added complexity.

## Required outputs
- `reports/context_placement.csv`
- `reports/context_placement_profiles/`
- `configs/context_locked.yaml`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[architecture/global-context/context-placement]]
