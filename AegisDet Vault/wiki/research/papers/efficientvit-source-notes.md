---
title: "EfficientViT"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# EfficientViT — Source Notes

## Summary
EfficientViT provides hardware-aware evidence for efficient global context in dense prediction.

## What the source establishes
The multi-scale linear-attention work targets high-resolution dense prediction using lightweight operations and reports speedups on multiple hardware classes.

## AegisDet use
Use it to justify measuring actual runtime and to inform a low-resolution linear-attention fallback.

## What not to copy blindly
Do not combine multiple EfficientViT modules with global tokens in the same first experiment.

## Implementation consequence
If tested, replace exactly one deep context block and preserve the rest of the student.

## Required evaluation
Accuracy, hardware latency, memory, export graph, and operator profiling.

## Sources
- https://arxiv.org/abs/2205.14756

## Related notes
- [[architecture/global-context/separable-attention-fallback]]
- [[benchmarking/latency-measurement-protocol]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
