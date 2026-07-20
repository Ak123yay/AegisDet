# PROJECT CONTEXT — AegisDet-Pro v5.1

## Definition

AegisDet-Pro is an independent edge-AI research project for adaptive object detection. It uses a strong CNN-first fast path and activates additional compute only when uncertainty or object scale suggests the frame is difficult.

## Research question

Can a domain-fine-tuned adaptive detector improve the accuracy-per-compute tradeoff over the same exported YOLO26n control by using global context and local refinement selectively?

## First complete system

```text
wildlife image
→ frozen YOLO26n at 416×416
→ route signals
├── easy: return baseline detections
└── hard: select ≤2 padded regions
          → rerun same detector
          → remap and merge detections
→ final output and route metadata
```

## Full research architecture

After the first system is proven, add one small learned-token context module at P4/P5, a learned router, progressive distillation, hard-negative active learning, and quantized deployment.

## Main measurements

- mAP50-95 and mAP50.
- Precision and recall.
- Small-object AP/recall on a frozen subset.
- p50, p90, p99 latency.
- Refinement rate.
- Model/engine size and memory.
- Power or energy per frame when measurable.
- Failure-category changes.

## Win condition

A defensible win is a domain-specific Pareto improvement, such as higher small-object accuracy with bounded tail latency, higher EdgeScore, or similar accuracy at lower cost. Universal COCO state of the art is not the goal.
