from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Box = tuple[float, float, float, float]

@dataclass(frozen=True, slots=True)
class Detection:
    box: Box
    confidence: float
    class_id: int
    source: Literal["base", "crop"] = "base"

    def __post_init__(self) -> None:
        x1, y1, x2, y2 = self.box
        if x2 < x1 or y2 < y1:
            raise ValueError(f"Invalid box ordering: {self.box}")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be in [0, 1]")
        if self.class_id < 0:
            raise ValueError("class_id must be non-negative")

@dataclass(frozen=True, slots=True)
class RouteDecision:
    refine: bool
    reasons: tuple[str, ...]
    signal_values: dict[str, float | int] = field(default_factory=dict)

@dataclass(frozen=True, slots=True)
class CropRegion:
    box: Box
    trigger_box: Box
    trigger_confidence: float
    trigger_class_id: int

@dataclass(slots=True)
class PipelineOutput:
    detections: list[Detection]
    base_detections: list[Detection]
    crop_detections: list[Detection]
    route: RouteDecision
    crops: list[CropRegion]
