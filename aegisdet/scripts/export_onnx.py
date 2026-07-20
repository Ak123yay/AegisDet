from __future__ import annotations
import argparse

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--model", required=True); p.add_argument("--imgsz",type=int,default=416)
    p.add_argument("--end2end", action=argparse.BooleanOptionalAction, default=True); a=p.parse_args()
    from ultralytics import YOLO
    result=YOLO(a.model).export(format="onnx", imgsz=a.imgsz, simplify=True, end2end=a.end2end)
    print(result)
if __name__ == "__main__": main()
