---
title: "MobileViTv2"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# MobileViTv2

## Summary
MobileViTv2 supports an efficient fallback design for global interaction.

## What the source establishes
The work identifies standard multi-head attention as a mobile latency bottleneck and proposes separable self-attention with linear complexity in the number of patches.

## AegisDet use
Use one low-resolution separable-attention block as a fallback comparison if the learned-token bridge is unstable or difficult to export.

## What not to copy blindly
Do not place attention at every stage or infer hardware speed from FLOPs alone.

## Implementation consequence
Implement one isolated deep block and test ONNX/runtime support before training a full model.

## Required evaluation
Export parity, latency on actual target runtime, mAP, and comparison with K-token context.

## Sources
- https://arxiv.org/abs/2206.02680

## Related notes
- [[architecture/global-context/separable-attention-fallback]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
