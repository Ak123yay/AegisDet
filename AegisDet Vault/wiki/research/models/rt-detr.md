---
title: "RT-DETR Family"
project: "AegisDet-Pro v5.1"
area: "research-model"
status: "accepted-reference"
tags: ["research-model", "source-backed", "rt-detr"]
---

# RT-DETR Family

## Summary

RT-DETR is an end-to-end real-time detector family. AegisDet uses the newest locked teacher variant, RT-DETRv4-X, while retaining RT-DETRv2-X as a fallback.

## AegisDet use

- RT-DETRv4-X: secondary architecture-diverse teacher.
- RT-DETRv2-X: fallback teacher only.
- Neither model is the edge student.
- Neither teacher is used during final inference.

## Why it is useful

The DETR-family representation and matching behavior differ from YOLO26, creating a plausible source of complementary supervision.

## What not to copy blindly

Do not replace the student with a DETR decoder. Do not assume heterogeneous feature distillation will work. Begin with common output-level boxes and class distributions.

## Sources

- https://github.com/RT-DETRs/RT-DETRv4
- https://arxiv.org/abs/2510.25257
- https://github.com/lyuwenyu/RT-DETR
- https://arxiv.org/abs/2407.17140
- https://arxiv.org/abs/2304.08069

## Related notes

- [[research/models/rt-detrv4-x]]
- [[distillation/teacher-selection]]
