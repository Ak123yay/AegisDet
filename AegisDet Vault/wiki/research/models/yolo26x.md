---
title: "YOLO26x"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "locked-teacher"
tags: ["research-model", "teacher", "yolo26x", "source-backed"]
---

# YOLO26x

## Role

YOLO26x (`yolo26x.pt`) is the locked primary same-family teacher for AegisDet-Pro.

## Source-backed facts

The official Ultralytics model table lists YOLO26 detection variants n, s, m, l, and x. It reports YOLO26x at 640 pixels with 55.7 million parameters, 193.9 GFLOPs, 57.5 COCO validation mAP50-95, and 11.8 ms T4 TensorRT latency under the documented benchmark setup.

These are source benchmarks, not AegisDet wildlife results.

## Why it is the first teacher

- same YOLO26 family as the student starting point,
- compatible class and box semantics,
- strongest official YOLO26 size,
- likely easier output-level and selected-feature transfer than a heterogeneous teacher.

## Required project work

- fine-tune on the exact domain taxonomy,
- evaluate on the frozen validation split,
- calibrate confidence,
- freeze checkpoint and hash,
- generate train-only cached targets,
- compare against no-KD and RT-DETRv4-X-only runs.

## Sources

- https://docs.ultralytics.com/models/yolo26/
- https://github.com/ultralytics/ultralytics

## Related notes

- [[TEACHER_MODELS]]
- [[distillation/teacher-selection]]
- [[experiments/distillation/exp-040-single-teacher-kd]]
