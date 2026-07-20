---
title: "DynamicDet"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research-model", "source-backed"]
---

# DynamicDet — Source Notes

## Summary
DynamicDet is the closest direct research inspiration for adaptive routing in object detection.

## What the source establishes
The work explores dynamic inference routes for detection to improve the speed-accuracy tradeoff according to input difficulty.

## AegisDet use
Use it as evidence that input-dependent detector compute is a legitimate research direction. AegisDet’s concrete contribution is domain-specific uncertainty routing to context/crop refinement with bounded tail latency.

## What not to copy blindly
Do not copy an opaque learned router first. Rule-based routing is required to establish interpretable behavior and labels.

## Implementation consequence
Log route signals, optional-path benefit, false skips, false refinements, route frequency, and expected extra compute.

## Required evaluation
Rule-versus-learned comparison, p90/p99 latency, route calibration, and corrected-error rate.

## Sources
- https://arxiv.org/abs/2304.05552

## Related notes
- [[architecture/router/rule-based-router-v1]]
- [[architecture/router/learned-router-v2]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
