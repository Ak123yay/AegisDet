# Minimum Viable AegisDet

## Definition

AegisDet-Mini is the smallest system that tests the adaptive-compute thesis without changing neural architecture.

```text
frozen domain YOLO26n
→ rule router
→ at most 2 padded crops
→ same detector on crops
→ coordinate remapping
→ class-aware NMS
→ output plus route metadata
```

## Required artifacts

- frozen baseline checkpoint;
- validation and test splits;
- route configuration;
- tested remap and merge functions;
- baseline and adaptive raw predictions;
- accuracy/latency comparison;
- failure gallery;
- keep/modify/remove conclusion.

## Not part of the minimum version

Global tokens, learned router, distillation, quantization, and tracking.
