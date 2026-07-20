from __future__ import annotations

from typing import Protocol

import numpy as np

from .crop_refine import CropPlanner
from .geometry import remap_box
from .merge import class_aware_nms
from .router import RuleBasedRouter
from .types import Detection, PipelineOutput

class Detector(Protocol):
    def predict(self, image: np.ndarray) -> list[Detection]: ...

class AegisDetMini:
    def __init__(self, detector: Detector, router: RuleBasedRouter | None = None,
                 crop_planner: CropPlanner | None = None, merge_iou: float = 0.50) -> None:
        self.detector = detector
        self.router = router or RuleBasedRouter()
        self.crop_planner = crop_planner or CropPlanner()
        self.merge_iou = merge_iou

    def run(self, image: np.ndarray) -> PipelineOutput:
        if image.ndim < 2:
            raise ValueError("image must have height and width dimensions")
        height, width = image.shape[:2]
        base = self.detector.predict(image)
        route = self.router.route(base, width, height)
        if not route.refine:
            return PipelineOutput(list(base), list(base), [], route, [])
        crops = self.crop_planner.plan(base, width, height)
        crop_detections: list[Detection] = []
        for region in crops:
            x1, y1, x2, y2 = (int(round(v)) for v in region.box)
            crop_image = image[y1:y2, x1:x2]
            if crop_image.size == 0:
                continue
            for d in self.detector.predict(crop_image):
                crop_detections.append(Detection(
                    box=remap_box(d.box, x1, y1), confidence=d.confidence,
                    class_id=d.class_id, source="crop",
                ))
        merged = class_aware_nms([*base, *crop_detections], self.merge_iou)
        return PipelineOutput(merged, list(base), crop_detections, route, crops)
