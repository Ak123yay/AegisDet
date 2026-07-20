---
title: "Experiment Philosophy"
project: "AegisDet-Pro v5.1"
area: "design"
status: "reference"
tags: ["design"]
---

# Experiment Philosophy

## Principle

AegisDet is a research project only when each module is treated as a falsifiable hypothesis. The diagram is not evidence. The vault therefore separates design, experiment specification, raw output, measured result, and final decision.

## Controlled progression

1. Establish a frozen YOLO26n domain baseline.
2. Change one main factor at a time.
3. Preserve the same split, evaluator, input size, and backend for model comparisons.
4. Measure the metric the module is supposed to affect: crop refinement should be judged on small-object behavior and tail latency; the router on corrected-error rate and refinement rate; global context on hard-case accuracy and real latency.
5. Keep neutral and negative results.

## Stop rule

A component is removed when its measured benefit is smaller than its implementation, export, latency, or reliability cost. The purpose is not to maximize the number of advanced modules; it is to find the strongest defensible accuracy-cost point.

## Related notes
- [[experiments/_experiments-moc]]
- [[benchmarking/same-backend-rule]]
