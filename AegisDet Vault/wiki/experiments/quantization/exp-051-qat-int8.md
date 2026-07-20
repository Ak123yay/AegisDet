---
title: "EXP 051 — QAT INT8"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 7"
status: "blocked"
tags: ["experiment", "phase-7"]
---

# EXP 051 — QAT INT8

## Research question
Can QAT recover a specifically documented PTQ regression?

## Hypothesis
QAT may restore confidence/localization behavior when PTQ exceeds the allowed loss.

## Frozen control
PTQ result, same quantized backend, calibration/test data, and final pre-quantized model.

## Independent variable
QAT training schedule and fake-quantization configuration.

## Procedure
1. State the exact PTQ failure that justifies QAT.
2. Train a short controlled QAT schedule.
3. Export through the same runtime.
4. Evaluate and benchmark.
5. Compare cost and complexity against FP16 and PTQ.

## Required metrics
- same metrics as PTQ
- recovered error categories
- training stability
- export success
- runtime benefit

## Acceptance criterion
Keep QAT only when it recovers enough of the declared PTQ loss and the target runtime still provides value.

## Rejection or rollback criterion
Skip or reject when PTQ already passes, QAT export is unstable, or FP16 is the better deployment point.

## Required outputs
- `reports/qat_int8_metrics.json`
- `configs/qat_locked.yaml`
- `reports/qat_runtime.json`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[quantization/qat-plan]]
- [[quantization/quantization-failure-modes]]
