---
title: "RT-DETRv4-X"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "locked-teacher"
tags: ["research-model", "teacher", "rt-detrv4", "source-backed"]
---

# RT-DETRv4-X

## Role

RT-DETRv4-X is the locked architecture-diverse secondary teacher.

## Source-backed facts

The official RT-DETRv4 repository provides code, configurations, checkpoints, ONNX export, TensorRT export, and inference tools. Its published table reports RT-DETRv4-X at 57.0 COCO AP and 12.90 ms T4 latency under its documented setup.

These are source benchmarks, not AegisDet wildlife results.

## Why it complements YOLO26x

RT-DETRv4-X is an end-to-end DETR-family detector with a different matching, decoder, and global-representation bias. It can supply complementary output-level targets and hard-case disagreement signals.

## Distillation restriction

Use output-level class and box transfer first. Do not start by forcing direct internal feature alignment between RT-DETRv4-X and the YOLO-derived student.

## Fallback

Use RT-DETRv2-X only if a documented RT-DETRv4-X custom fine-tuning or target-extraction issue blocks progress.

## Sources

- https://github.com/RT-DETRs/RT-DETRv4
- https://arxiv.org/abs/2510.25257
- https://github.com/lyuwenyu/RT-DETR

## Related notes

- [[TEACHER_MODELS]]
- [[distillation/teacher-selection]]
- [[experiments/distillation/exp-041-progressive-teacher-kd]]
- [[experiments/distillation/exp-043-dual-teacher-kd]]
