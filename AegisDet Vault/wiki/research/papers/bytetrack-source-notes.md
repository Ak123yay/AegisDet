---
title: "ByteTrack"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "optional-reference"
tags: ["research-model", "source-backed"]
---

# ByteTrack — Source Notes

## Summary
ByteTrack is the preferred later tracking reference for video stability.

## What the source establishes
The method associates low-score detections instead of discarding all of them, improving multi-object tracking in its evaluated settings.

## AegisDet use
Use it only after image-level accuracy and threshold calibration are stable.

## What not to copy blindly
Do not let tracking hide detector errors in image benchmarks or mix tracking metrics with detector mAP.

## Implementation consequence
Create a separate video evaluation path and preserve image-only outputs.

## Required evaluation
Track continuity, false-trigger persistence, missed-frame gaps, ID switches if applicable, and added latency.

## Sources
- https://arxiv.org/abs/2110.06864
- https://github.com/ifzhang/ByteTrack

## Related notes
- [[architecture/temporal/temporal-stability]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
