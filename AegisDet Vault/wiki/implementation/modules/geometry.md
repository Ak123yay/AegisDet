# Geometry Module

Owns box area, relative area, IoU, image-bound clamping, padding, and crop-to-image remapping. All coordinates are pixel-space `xyxy` values.

## Invariants

- boxes use `(x1, y1, x2, y2)`;
- `x2 >= x1` and `y2 >= y1`;
- crop boxes are clamped to image bounds;
- remapping adds crop origin exactly once;
- geometry functions are pure and unit tested.

Implementation: `project-code/src/aegisdet/geometry.py`.
