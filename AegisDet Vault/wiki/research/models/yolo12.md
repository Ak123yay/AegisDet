---
title: "YOLO12"
project: "AegisDet-Pro v5.1"
area: "research-source"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# YOLO12

## Summary
YOLO12 is an attention-centric real-time detector and a useful counterpoint to AegisDet’s CNN-first direction.

## Method or evidence
The NeurIPS 2025 work introduces attention-centric YOLO design and reports competitive T4 accuracy/latency in its evaluated setup. Ultralytics documents it primarily as a research/community model and recommends YOLO11 or YOLO26 for more predictable production use.

## AegisDet lesson
Use YOLO12 as evidence that attention can help real-time detection and as a possible teacher/comparison—not as the initial edge student.

## Caution
Attention performance on T4 does not prove CPU/edge efficiency. Training stability, memory, backend, and implementation differences must be tested.

## Primary sources
- https://arxiv.org/abs/2502.12524
- https://proceedings.neurips.cc/paper_files/paper/2025/hash/7103444259031cc58051f8c9a4868533-Abstract-Conference.html
- https://github.com/sunsmarterjie/yolov12

## Related notes
- [[FOUNDATION_MODEL]]
- [[architecture/global-context/tiny-global-token-context]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
