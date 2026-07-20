from __future__ import annotations

from typing import Any

import numpy as np

from ..types import Detection

class UltralyticsAdapter:
    """Convert Ultralytics Results into AegisDet internal detections."""
    def __init__(self, model_path: str, imgsz: int = 416, confidence: float = 0.20, device: Any = None) -> None:
        try:
            from ultralytics import YOLO
        except ImportError as exc:
            raise RuntimeError("Install ultralytics before using UltralyticsAdapter") from exc
        self.model = YOLO(model_path)
        self.imgsz = imgsz
        self.confidence = confidence
        self.device = device

    def predict(self, image: np.ndarray) -> list[Detection]:
        result = self.model.predict(
            source=image, imgsz=self.imgsz, conf=self.confidence,
            device=self.device, verbose=False,
        )[0]
        output: list[Detection] = []
        if result.boxes is None:
            return output
        for box in result.boxes:
            xyxy = tuple(float(x) for x in box.xyxy[0].tolist())
            output.append(Detection(
                box=xyxy, confidence=float(box.conf[0]), class_id=int(box.cls[0]), source="base"
            ))
        return output
