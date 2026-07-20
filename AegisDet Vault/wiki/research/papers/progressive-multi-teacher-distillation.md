---
title: "Progressive Multi-Teacher Distillation"
area: "paper-note"
status: "accepted-reference"
tags: ["distillation", "paper"]
---
# Progressive Multi-Teacher Distillation

## Source

Cao et al., *Learning Lightweight Object Detectors via Multi-Teacher Progressive Distillation*, ICML 2023: https://proceedings.mlr.press/v202/cao23c.html

## What it establishes

The method transfers knowledge through a sequence of teachers so a lightweight detector gradually adapts. The authors report successful transfer from transformer teachers to convolutional students in their evaluated detection settings.

## AegisDet use

Test a close YOLO26s teacher before introducing a stronger heterogeneous teacher. Preserve a single-teacher baseline so progressive training has a fair control.

## Required ablation

1. no distillation;
2. one YOLO26s teacher;
3. progressive YOLO26s → stronger teacher;
4. optional hard-example weighting.

Distillation remains training-only; inference latency must not increase.

## Related notes

- [[distillation/progressive-teacher-schedule]]
- [[experiments/distillation/exp-041-progressive-teacher-kd]]
