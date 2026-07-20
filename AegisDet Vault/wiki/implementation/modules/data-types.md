# Data Types

The internal representation is intentionally independent of Ultralytics so router, crop, merge, metrics, and tests remain deterministic.

## Canonical objects

- `Detection`: pixel-space `xyxy`, confidence, class ID, and source (`base` or `crop`).
- `RouteDecision`: refine flag, reason codes, and raw signal values.
- `CropRegion`: padded crop box plus the triggering detection.
- `PipelineOutput`: final, base, and crop detections plus route and crops.

Implementation: `project-code/src/aegisdet/types.py`.
