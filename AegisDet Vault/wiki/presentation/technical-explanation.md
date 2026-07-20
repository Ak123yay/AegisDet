---
title: "Technical Explanation"
project: "AegisDet-Pro v5.1"
area: "presentation"
status: "reference"
tags: ["presentation"]
---

# Technical Explanation

AegisDet-Pro is a CNN-first adaptive detector built around a fine-tuned YOLO26n control. Its initial contribution is a bounded selective-inference wrapper: output-derived route signals trigger at most a fixed number of padded local reinferences, followed by coordinate remapping and class-aware merge. Later ablations add a deep low-resolution learned-token context block, a learned router with compute regularization, detector distillation, and quantized export. The main evidence is a same-backend accuracy/latency Pareto comparison on a frozen wildlife test set.

## Related notes
- [[AegisDet_Design/architecture-diagram]]
- [[PROJECT_CONTEXT]]
