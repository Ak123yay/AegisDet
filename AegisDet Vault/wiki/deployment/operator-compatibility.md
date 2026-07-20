---
title: "Operator Compatibility"
project: "AegisDet-Pro v5.1"
area: "deployment"
status: "specification"
tags: ["deployment"]
---

# Operator Compatibility

## Purpose
Define the deployment requirements for the project concern named “Operator Compatibility” and its measurable effect on the AegisDet research question.

## Project specification
Start from the same validated ONNX/checkpoint artifact. Record runtime version, provider/engine, precision, graph options, input/output contract, preprocessing, postprocessing, unsupported operators, fallback path, loading time, and warm latency. Verify predictions before interpreting speed.

## Evidence required
- Artifact hash
- Runtime/provider configuration
- Prediction parity sample
- Latency and memory result
- Compatibility/fallback log

## Decision rule
A runtime is supported only if it loads reliably, preserves acceptable predictions, and has a reproducible benchmark. Faster but incorrect output is a failure.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[deployment/operator-compatibility]]
- [[experiments/quantization/exp-052-runtime-export-matrix]]

## Retrieval terms
aegisdet, compatibility, edge-ai, operator.
