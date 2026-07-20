from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--model", required=True); p.add_argument("--data", required=True)
    p.add_argument("--imgsz", type=int, default=416); p.add_argument("--output", default="reports/baseline_metrics.json")
    a=p.parse_args(); from ultralytics import YOLO
    metrics=YOLO(a.model).val(data=a.data, imgsz=a.imgsz)
    payload={"map50": float(metrics.box.map50), "map50_95": float(metrics.box.map),
             "precision_mean": float(metrics.box.mp), "recall_mean": float(metrics.box.mr)}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2))
    print(json.dumps(payload,indent=2))
if __name__ == "__main__": main()
