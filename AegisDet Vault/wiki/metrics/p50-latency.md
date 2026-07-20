---
title: "p50 Latency"
project: "AegisDet-Pro v5.1"
area: "metric"
status: "specification"
tags: ["metric"]
---

# p50 Latency

## Purpose
Define p50 Latency so every experiment calculates it consistently.

## Project specification
Median of warm, synchronized end-to-end latency samples. Store raw per-image or per-run values whenever possible; a rounded summary alone is insufficient for audit.

## Evidence required
- Formula or evaluator version documented
- Units and scale documented
- Frozen confidence and IoU policy
- Sanity test on known values
- Raw values linked from experiment output

## Decision rule
Do not compare this metric across experiments when its denominator, subset, evaluator, or benchmark conditions differ.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[DOMAIN_LOCK]]
- [[benchmarking/benchmark-result-template]]

## Retrieval terms
aegisdet, edge-ai, latency, p50.
