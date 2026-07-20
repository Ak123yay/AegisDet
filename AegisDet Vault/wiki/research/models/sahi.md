---
title: "SAHI"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# SAHI

## Summary
SAHI is the main full-slicing reference and an upper-bound comparison for small-object refinement.

## What the source establishes
The method applies tiled inference/fine-tuning to improve small-object detection and reported gains on aerial datasets for several detectors.

## AegisDet use
Use full SAHI as a comparison. AegisDet’s hypothesis is that selective crops recover some small-object benefit at much lower average cost.

## What not to copy blindly
Do not cite SAHI gains as expected wildlife gains, and do not run full slicing on every frame as the final edge design without measuring cost.

## Implementation consequence
Match slice size and overlap fairly; compare full slicing, selective crops, and baseline.

## Required evaluation
APS/recall, duplicate rate, average/p90/p99 latency, number of detector calls, and merge behavior.

## Sources
- https://arxiv.org/abs/2202.06934
- https://github.com/obss/sahi

## Related notes
- [[architecture/crop-refine/selective-crop-refinement]]
- [[research/comparisons/selective-crop-refine-vs-full-sahi]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
