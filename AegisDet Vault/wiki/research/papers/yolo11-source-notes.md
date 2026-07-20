---
title: "YOLO11"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "fallback-reference"
tags: ["research-model", "source-backed"]
---

# YOLO11 — Source Notes

## Summary
YOLO11n is the temporary tooling fallback, not the final primary baseline.

## What the source establishes
Ultralytics maintains stable support for YOLO11 training, validation, prediction, and export.

## AegisDet use
Use it only when a documented YOLO26 problem blocks Phase 0 or Phase 1. The method and code can be validated with YOLO11n while the block is resolved.

## What not to copy blindly
Do not silently present YOLO11n results as YOLO26n results or mix checkpoints within one comparison.

## Implementation consequence
Make the model name configurable. Add the fallback reason to the run metadata.

## Required evaluation
Environment smoke test, export compatibility, and a clearly labeled fallback run.

## Sources
- https://docs.ultralytics.com/models/yolo11/
- https://docs.ultralytics.com/models/

## Related notes
- [[FOUNDATION_MODEL]]
- [[implementation/workflows/environment-setup]]

## Status rule
The source summary is evidence; AegisDet performance remains a hypothesis until its own experiment is run.
