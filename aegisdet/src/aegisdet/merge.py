from __future__ import annotations

from .geometry import intersection_over_union
from .types import Detection

def class_aware_nms(detections: list[Detection], iou_threshold: float = 0.50) -> list[Detection]:
    if not 0.0 <= iou_threshold <= 1.0:
        raise ValueError("iou_threshold must be in [0, 1]")
    ordered = sorted(detections, key=lambda d: d.confidence, reverse=True)
    kept: list[Detection] = []
    for candidate in ordered:
        duplicate = any(
            candidate.class_id == existing.class_id
            and intersection_over_union(candidate.box, existing.box) > iou_threshold
            for existing in kept
        )
        if not duplicate:
            kept.append(candidate)
    return kept
