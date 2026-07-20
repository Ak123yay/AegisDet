---
title: "EXP 001 — YOLO26n Wildlife Baseline"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 1"
status: "planned"
tags: ["experiment", "phase-1"]
---

# EXP 001 — YOLO26n Wildlife Baseline

## Research question
What accuracy, failure profile, and exported latency does the domain-fine-tuned YOLO26n control achieve?

## Hypothesis
A COCO-pretrained YOLO26n fine-tuned at 416×416 will provide a strong control but will retain measurable small, low-light, and occlusion failures.

## Frozen control
COCO-pretrained `yolo26n.pt`; dataset v1 and its split are frozen before training.

## Independent variable
Domain fine-tuning using the resolved baseline config.

## Procedure
1. Complete data/license/split audit.
2. Train using `configs/baseline_yolo26n.yaml`.
3. Select the checkpoint using validation policy only.
4. Evaluate validation and frozen test sets.
5. Export ONNX and create failure gallery.

## Required metrics
- mAP50-95 and mAP50
- precision and recall
- small-object AP/recall on the frozen subset
- p50, p90, and p99 end-to-end latency
- model/artifact size and refinement rate when applicable
- failure-category changes

## Acceptance criterion
The run is accepted as the control when training is reproducible, the checkpoint is identified, evaluation completes, export parity is acceptable, and all benchmark metadata exists. No minimum mAP is invented in advance.

## Rejection or rollback criterion
Block Phase 2 if labels/splits are unreliable, export changes predictions materially, or run metadata is incomplete.

## Required outputs
- `runs/<run-id>/resolved-config.yaml`
- `reports/baseline_metrics.json`
- `reports/baseline_predictions.jsonl`
- `reports/failure_gallery/`
- `reports/baseline_latency.json`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[FOUNDATION_MODEL]]
- [[DOMAIN_LOCK]]
- [[benchmarking/same-backend-rule]]
