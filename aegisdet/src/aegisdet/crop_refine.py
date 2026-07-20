from __future__ import annotations

from dataclasses import dataclass

from .geometry import area_ratio, pad_box
from .types import CropRegion, Detection

@dataclass(frozen=True, slots=True)
class CropPlannerConfig:
    max_crops: int = 2
    padding_fraction: float = 0.35
    small_area_ratio: float = 0.015
    uncertain_low: float = 0.20
    uncertain_high: float = 0.50
    minimum_crop_pixels: int = 24

    def __post_init__(self) -> None:
        if self.max_crops < 0:
            raise ValueError("max_crops cannot be negative")
        if self.minimum_crop_pixels <= 0:
            raise ValueError("minimum_crop_pixels must be positive")

class CropPlanner:
    def __init__(self, config: CropPlannerConfig | None = None) -> None:
        self.config = config or CropPlannerConfig()

    def plan(self, detections: list[Detection], image_width: int, image_height: int) -> list[CropRegion]:
        candidates: list[tuple[tuple[int, float, float], Detection]] = []
        for d in detections:
            ratio = area_ratio(d.box, image_width, image_height)
            small = ratio < self.config.small_area_ratio
            uncertain = self.config.uncertain_low <= d.confidence <= self.config.uncertain_high
            if not (small or uncertain):
                continue
            # Prefer candidates satisfying both signals, then lower confidence, then smaller area.
            priority = (0 if small and uncertain else 1, d.confidence, ratio)
            candidates.append((priority, d))
        candidates.sort(key=lambda item: item[0])
        result: list[CropRegion] = []
        for _, d in candidates:
            if len(result) >= self.config.max_crops:
                break
            box = pad_box(d.box, self.config.padding_fraction, image_width, image_height)
            x1, y1, x2, y2 = box
            if x2 - x1 < self.config.minimum_crop_pixels or y2 - y1 < self.config.minimum_crop_pixels:
                continue
            result.append(CropRegion(box, d.box, d.confidence, d.class_id))
        return result
