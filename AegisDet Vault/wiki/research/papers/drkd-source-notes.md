---
title: "Dual Relation Knowledge Distillation for Object Detection"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# Dual Relation Knowledge Distillation for Object Detection — Source Notes

## Summary
DRKD distills pixel-wise and instance-wise relations, with explicit motivation around foreground/background imbalance and small-object representation.

## Method or evidence
The paper represents pixel features in relation space and adds filtered instance-relation supervision; it reports improvements on Faster R-CNN and RetinaNet COCO setups.

## AegisDet lesson
It is relevant as a later hard-case/small-object distillation comparison, not as the first KD implementation.

## Caution
Relation losses add training complexity and may not transfer cleanly to YOLO26 feature/head structure. A simple teacher baseline is mandatory.

## Primary sources
- https://arxiv.org/abs/2302.05637

## Related notes
- [[distillation/hard-example-distillation]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
