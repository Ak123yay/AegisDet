---
title: "RepViT"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# RepViT — Source Notes

## Summary
RepViT supports the decision to keep AegisDet CNN-first while using modern mobile design lessons.

## What the source establishes
The paper revisits mobile CNN design from a ViT perspective and reports strong mobile latency across vision tasks.

## AegisDet use
Use its block-design principles only as a later backbone ablation if the default YOLO backbone is a measured limitation.

## What not to copy blindly
Do not replace the baseline backbone before wrapper-level adaptivity is proven; that would confound experiments.

## Implementation consequence
Create one backbone-only configuration and keep the router, head, dataset, and training recipe fixed.

## Required evaluation
Backbone latency, export support, mAP, APS, memory, and EdgeScore.

## Sources
- https://arxiv.org/abs/2307.09283
- https://github.com/THU-MIG/RepViT

## Related notes
- [[architecture/backbone/cnn-first-backbone]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
