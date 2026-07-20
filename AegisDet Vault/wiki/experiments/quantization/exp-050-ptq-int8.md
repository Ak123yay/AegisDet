---
title: "EXP 050 — PTQ INT8"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 7"
status: "blocked"
tags: ["experiment", "phase-7"]
---

# EXP 050 — PTQ INT8

## Research question
Can post-training INT8 reduce deployment cost while preserving acceptable wildlife detection and routing behavior?

## Hypothesis
Representative calibration should retain most accuracy, but small-object confidence and router thresholds may shift.

## Frozen control
Validated FP32/FP16 exported model and runtime.

## Independent variable
PTQ calibration set and backend quantization configuration.

## Procedure
1. Freeze calibration manifest.
2. Quantize using target runtime.
3. Verify graph/input/output and prediction parity.
4. Evaluate full and hard subsets.
5. Benchmark latency, memory, and size; recalibration is a separate experiment.

## Required metrics
- mAP/small-object metrics
- confidence/calibration shift
- route/refinement rate shift
- p50/p90/p99 latency
- memory and artifact size

## Acceptance criterion
Accept when accuracy/calibration loss stays below the predeclared limit and real runtime/storage improves.

## Rejection or rollback criterion
Reject if backend falls back to slow ops, route behavior breaks, or savings are negligible.

## Required outputs
- `reports/ptq_int8_metrics.json`
- `reports/ptq_calibration_manifest.csv`
- `reports/ptq_runtime.json`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[quantization/ptq-plan]]
- [[quantization/calibration-set]]
