---
title: "EfficientDet"
project: "AegisDet-Pro v5.1"
area: "research-source"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# EfficientDet

## Summary
EfficientDet is an efficiency-oriented detector family built around weighted BiFPN and compound scaling.

## Method or evidence
The paper systematically studies scalable object-detection design and introduces bidirectional weighted feature fusion. Its published results are from its own COCO/model/runtime setup.

## AegisDet lesson
Use BiFPN as a possible neck-only ablation if measured small-object fusion is limiting the default YOLO neck.

## Caution
Do not change backbone, neck, input resolution, and router simultaneously. FLOP reductions are not a substitute for real runtime measurement.

## Primary sources
- https://arxiv.org/abs/1911.09070
- https://github.com/google/automl/tree/master/efficientdet

## Related notes
- [[architecture/neck/pan-fpn-neck]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
