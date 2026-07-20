---
title: "DynamicViT"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# DynamicViT — Source Notes

## Summary
DynamicViT provides a broad selective-compute principle: computation can be conditioned on input importance.

## What the source establishes
The paper dynamically prunes less informative visual tokens and reports substantial FLOP/throughput reductions with limited accuracy loss on its evaluated classifiers.

## AegisDet use
Use the principle that easy or uninformative content should not receive the same computation as hard content.

## What not to copy blindly
Do not add token pruning to the initial detector. AegisDet routes at frame and region level first.

## Implementation consequence
Keep dynamic token sparsification as a future comparison only after the core project is complete.

## Required evaluation
Actual runtime speedup, structured feature compatibility, and detector accuracy.

## Sources
- https://arxiv.org/abs/2106.02034
- https://github.com/raoyongming/DynamicViT

## Related notes
- [[architecture/system/bounded-adaptivity]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
