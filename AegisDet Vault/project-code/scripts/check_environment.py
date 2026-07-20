from __future__ import annotations
import json, platform, sys

def main() -> int:
    report = {"python": sys.version, "platform": platform.platform()}
    try:
        import torch
        report.update({"torch": torch.__version__, "cuda_available": torch.cuda.is_available(),
                       "cuda_device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None})
    except Exception as exc:
        report["torch_error"] = repr(exc)
    try:
        import cv2
        report["opencv"] = cv2.__version__
    except Exception as exc:
        report["opencv_error"] = repr(exc)
    try:
        import ultralytics
        report["ultralytics"] = ultralytics.__version__
        from ultralytics import YOLO
        model = YOLO("yolo26n.pt")
        report["yolo26_load"] = True
        report["model_type"] = type(model.model).__name__
    except Exception as exc:
        report["yolo26_load"] = False
        report["yolo_error"] = repr(exc)
    print(json.dumps(report, indent=2))
    return 0 if report.get("yolo26_load") else 1
if __name__ == "__main__":
    raise SystemExit(main())
