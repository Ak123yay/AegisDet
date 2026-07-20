---
title: "Separable Attention Fallback"
project: "AegisDet-Pro v5.1"
area: "architecture"
status: "specification"
tags: ["architecture"]
---

# Separable Attention Fallback

## Purpose
Specify the responsibility and boundaries of the project concern named “Separable Attention Fallback” and its measurable effect on the AegisDet research question.

## Project specification
This component must have a single interface and be isolated from unrelated changes. Define its inputs, outputs, parameters, maximum compute, failure behavior, export constraints, and logging. The mandatory fast path must remain usable when optional components are disabled.

The first implementation should use the simplest operator set that can test the hypothesis.

## Evidence required
- Interface documented
- Standalone test or shape test
- Controlled ablation
- Export/compatibility result
- Latency and failure analysis

## Decision rule
Keep the component only when its isolated experiment improves the intended Pareto point. Remove or simplify it when benefit does not justify complexity.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[PROJECT_CONTEXT]]
- [[CONTEXT_LOCK]]

## Retrieval terms
aegisdet, attention, edge-ai, fallback, separable.
