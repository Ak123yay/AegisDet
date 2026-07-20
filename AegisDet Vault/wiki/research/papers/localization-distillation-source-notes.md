---
title: "Localization Distillation for Dense Object Detection"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# Localization Distillation — Source Notes for Dense Object Detection

## Summary
Localization Distillation transfers teacher localization distributions/logits and identifies valuable localization regions for dense detectors.

## Method or evidence
The CVPR 2022 paper argues localization knowledge is especially important for detector distillation and reports improvements in its evaluated dense-detector setup.

## AegisDet lesson
Use it as a possible box/localization KD comparison after the simple distillation baseline.

## Caution
Its formulation is tied to dense detector outputs; compatibility with YOLO26’s head must be designed and validated rather than assumed.

## Primary sources
- https://openaccess.thecvf.com/content/CVPR2022/html/Zheng_Localization_Distillation_for_Dense_Object_Detection_CVPR_2022_paper.html

## Related notes
- [[distillation/box-distillation]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
