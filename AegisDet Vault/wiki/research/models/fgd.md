---
title: "Focal and Global Knowledge Distillation for Detectors"
project: "AegisDet-Pro v5.1"
area: "research-source"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# Focal and Global Knowledge Distillation for Detectors

## Summary
FGD separates foreground/background emphasis and global feature relations for detector distillation.

## Method or evidence
The CVPR 2022 work applies feature-map distillation to multiple detector families and reports gains in its COCO experiments.

## AegisDet lesson
Use it as a candidate feature-distillation mechanism after a basic single-teacher logit/box baseline exists.

## Caution
Do not start with a complex combination of focal and global losses. Feature-shape mapping and loss weight sensitivity can confound the student experiment.

## Primary sources
- https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Focal_and_Global_Knowledge_Distillation_for_Detectors_CVPR_2022_paper.html
- https://github.com/yzd-v/FGD

## Related notes
- [[distillation/foreground-background-distillation]]
- [[distillation/feature-distillation]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
