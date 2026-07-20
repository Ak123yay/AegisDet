---
title: "EXP 052 — Runtime Export Matrix"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 7"
status: "blocked"
tags: ["experiment", "phase-7"]
---

# EXP 052 — Runtime Export Matrix

## Research question
Which supported runtime provides the best reliable deployment point for the same validated model?

## Hypothesis
Runtime rankings will differ by device and precision; no single backend will dominate universally.

## Frozen control
Same model artifact where possible, same inputs/evaluator, named device, batch 1, and consistent end-to-end coverage.

## Independent variable
Runtime/provider/engine and precision.

## Procedure
1. Hash all artifacts.
2. Verify prediction parity per runtime.
3. Record engine/provider and unsupported ops.
4. Benchmark loading, warm latency, memory, and size.
5. Create device-specific Pareto tables.

## Required metrics
- load/export success
- prediction parity
- p50/p90/p99
- memory and loading time
- artifact size
- fallback behavior

## Acceptance criterion
Select one final backend per tested device based on correctness and Pareto position, not a global winner.

## Rejection or rollback criterion
Mark unsupported when predictions drift or execution depends on undocumented fallback.

## Required outputs
- `reports/runtime_matrix.csv`
- `reports/runtime_parity/`
- `reports/runtime_environment.json`

## Result

**Not run.** Do not fill this section from expected values or paper results.

## Conclusion

Pending execution. Final wording must be keep, modify, or remove with evidence.

## Related notes
- [[deployment/runtimes/opencv-5-dnn]]
- [[deployment/runtimes/onnx-runtime]]
- [[deployment/runtimes/openvino]]
- [[deployment/runtimes/tensorrt]]
