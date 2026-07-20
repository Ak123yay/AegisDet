"""AegisDet-Pro adaptive detection primitives."""

from .crop_refine import CropPlanner, CropPlannerConfig
from .merge import class_aware_nms
from .pipeline import AegisDetMini
from .router import RuleBasedRouter, RouterConfig
from .types import CropRegion, Detection, PipelineOutput, RouteDecision

__all__ = [
    "AegisDetMini", "CropPlanner", "CropPlannerConfig", "CropRegion", "Detection",
    "PipelineOutput", "RouteDecision", "RuleBasedRouter", "RouterConfig", "class_aware_nms",
]
