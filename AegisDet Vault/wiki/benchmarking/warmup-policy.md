---
title: "Warmup Policy"
project: "AegisDet-Pro v5.1"
area: "benchmarking"
status: "specification"
tags: ["benchmarking"]
---

# Warmup Policy

## Purpose
Define a reproducible benchmark for the project concern named “Warmup Policy” and its measurable effect on the AegisDet research question.

## Project specification
Record hardware model, OS, power mode, runtime/version, model artifact hash, input shape, batch size, precision, warmup, synchronization, number of samples, preprocessing, postprocessing, and whether timing is end-to-end. Preserve all timing samples rather than only the fastest value.

## Evidence required
- Environment metadata
- Warmup and synchronization documented
- Raw timing samples
- p50/p90/p99 and mean
- Accuracy parity checked where relevant

## Decision rule
Reject a timing comparison if conditions differ, sample count is inadequate, asynchronous work is unsynchronized, or preprocessing/postprocessing coverage is inconsistent.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[benchmarking/same-backend-rule]]
- [[metrics/p90-latency]]

## Retrieval terms
aegisdet, edge-ai, policy, warmup.
