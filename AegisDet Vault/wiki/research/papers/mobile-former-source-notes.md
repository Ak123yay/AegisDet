---
title: "Mobile-Former"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# Mobile-Former — Source Notes

## Summary
Mobile-Former is the closest literature anchor for the small learned-token context branch.

## What the source establishes
The paper couples a MobileNet branch with a transformer branch through a two-way bridge and uses very few global tokens—six or fewer in examples—to learn global priors at low cost.

## AegisDet use
Use only a few tokens at a deep low-resolution feature stage. Test K=4, K=6, and K=8 rather than a large token sequence.

## What not to copy blindly
Do not copy the full classifier/detector architecture or claim that few tokens guarantee speed on the chosen runtime.

## Implementation consequence
Create a narrow token-feature bridge at P4 or P5 with residual return to the CNN feature map. Export immediately after the first forward pass works.

## Required evaluation
K-token ablation, P4/P5 placement, operator support, memory traffic, mAP, hard-case recall, and measured latency.

## Sources
- https://arxiv.org/abs/2108.05895

## Related notes
- [[architecture/global-context/tiny-global-token-context]]
- [[experiments/global-context/exp-030-k4-global-tokens]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
