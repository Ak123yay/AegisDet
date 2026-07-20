from __future__ import annotations
import argparse, json
from pathlib import Path
import cv2
from aegisdet.adapters import UltralyticsAdapter
from aegisdet.pipeline import AegisDetMini

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--model",required=True); p.add_argument("--image",required=True)
    p.add_argument("--output",default="reports/aegisdet_mini_result.json"); a=p.parse_args()
    image=cv2.imread(a.image)
    if image is None: raise FileNotFoundError(a.image)
    result=AegisDetMini(UltralyticsAdapter(a.model)).run(image)
    payload={"route":{"refine":result.route.refine,"reasons":result.route.reasons,
             "signals":result.route.signal_values},"crops":[c.box for c in result.crops],
             "detections":[{"box":d.box,"confidence":d.confidence,"class_id":d.class_id,"source":d.source} for d in result.detections]}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(payload,indent=2)); print(out)
if __name__ == "__main__": main()
