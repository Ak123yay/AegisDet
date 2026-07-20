---
title: "EXP 002 — Baseline ONNX Parity"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 1"
status: "planned"
tags: ["experiment", "phase-1"]
---

# EXP 002 — Baseline ONNX Parity

## Research question
Does the exported YOLO26n ONNX graph preserve the validated PyTorch predictions?

## Hypothesis
The supported export path should preserve class, confidence, and localization closely enough for runtime benchmarking.

## Frozen control
Frozen PyTorch checkpoint and a fixed parity image set.

## Independent variable
Export head mode, simplification, opset, and ONNX inference backend.

## Procedure
1. Export one-to-one default ONNX.
2. If required, export one-to-many fallback separately.
3. Run both PyTorch and ONNX on the parity set with identical preprocessing.
4. Match predictions and summarize score/box differences.
5. Record unsupported operators and fallbacks.

## Required metrics
- load success
- class agreement
- confidence deviation
- box IoU/deviation
- detection-count difference
- runtime initialization errors

## Acceptance criterion
Accept only when differences are within a threshold declared before inspection and no systematic class/localization drift exists.

## Rejection or rollback criterion
Reject or change export settings when detections disappear, confidence distributions shift materially, or runtime graph support is unstable.

## Required outputs
- `reports/onnx_parity.json`
- `reports/onnx_parity_examples/`
- `reports/export_log.txt`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[deployment/operator-compatibility]]
- [[deployment/runtimes/onnx-runtime]]
