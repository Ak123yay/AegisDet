# Ultralytics Adapter

The adapter is the only module that knows the Ultralytics `Results`/`Boxes` API. It converts predictions into internal `Detection` objects.

## Boundary

The adapter must not decide routes, create crops, merge boxes, or tune thresholds. This isolation lets deterministic core tests run without model weights and reduces vendor lock-in.

Implementation: `project-code/src/aegisdet/adapters/ultralytics_adapter.py`.
