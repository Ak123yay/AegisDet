from __future__ import annotations

from dataclasses import dataclass

from .geometry import area_ratio, intersection_over_union
from .types import Detection, RouteDecision

@dataclass(frozen=True, slots=True)
class RouterConfig:
    small_area_ratio: float = 0.015
    small_count_trigger: int = 1
    uncertain_low: float = 0.20
    uncertain_high: float = 0.50
    uncertain_count_trigger: int = 2
    overlap_iou: float = 0.60
    overlap_count_trigger: int = 2

    def __post_init__(self) -> None:
        if not 0.0 < self.small_area_ratio < 1.0:
            raise ValueError("small_area_ratio must be in (0, 1)")
        if not 0.0 <= self.uncertain_low <= self.uncertain_high <= 1.0:
            raise ValueError("uncertainty bounds must be ordered within [0, 1]")

class RuleBasedRouter:
    def __init__(self, config: RouterConfig | None = None) -> None:
        self.config = config or RouterConfig()

    def route(self, detections: list[Detection], image_width: int, image_height: int) -> RouteDecision:
        small = sum(
            area_ratio(d.box, image_width, image_height) < self.config.small_area_ratio
            for d in detections
        )
        uncertain = sum(
            self.config.uncertain_low <= d.confidence <= self.config.uncertain_high
            for d in detections
        )
        overlaps = 0
        for i, a in enumerate(detections):
            for b in detections[i + 1:]:
                if a.class_id == b.class_id and intersection_over_union(a.box, b.box) >= self.config.overlap_iou:
                    overlaps += 1
        reasons: list[str] = []
        if small >= self.config.small_count_trigger:
            reasons.append("small-object")
        if uncertain >= self.config.uncertain_count_trigger:
            reasons.append("uncertain-detections")
        if overlaps >= self.config.overlap_count_trigger:
            reasons.append("overlap-density")
        return RouteDecision(
            refine=bool(reasons),
            reasons=tuple(reasons) if reasons else ("fast",),
            signal_values={"small_count": small, "uncertain_count": uncertain, "overlap_count": overlaps},
        )
