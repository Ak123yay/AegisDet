---
title: "EXP 035 — Hard-Negative Dataset V2"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 3"
status: "blocked"
tags: ["experiment", "phase-3"]
---

# EXP 035 — Hard-Negative Dataset V2

## Research question
Does a curated hard-negative/active-learning round reduce real baseline false positives and misses?

## Hypothesis
Dataset v2 will improve hard-negative precision and selected hard-case recall without architecture changes.

## Frozen control
Frozen model architecture, training recipe, validation/test splits, evaluator, and runtime.

## Independent variable
Training data changes from v1 to documented v2.

## Procedure
1. Mine failures on an unlabeled/training pool only.
2. Select uncertain then diverse samples.
3. Annotate/review and create v2 manifest.
4. Retrain baseline and AegisDet-Mini with the same recipe.
5. Evaluate on the unchanged test set.

## Required metrics
- mAP/precision/recall
- false-positive categories
- hard-case recall
- per-class data counts
- annotation count and selection diversity

## Acceptance criterion
Accept v2 when improvement is reproducible and not explained by leakage or changed test labels.

## Rejection or rollback criterion
Reject/repair if licensing, label quality, split leakage, or class imbalance invalidates comparison.

## Required outputs
- `data/wildlife-v2-manifest.csv`
- `reports/dataset_v2_audit.json`
- `reports/v1_v2_comparison.csv`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[data/active-learning/hard-negative-mining-loop]]
- [[research/models/ppal]]
