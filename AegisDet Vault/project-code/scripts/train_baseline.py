from __future__ import annotations
import argparse
from pathlib import Path
import yaml

def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--config", default="configs/baseline_yolo26n.yaml")
    args=parser.parse_args(); cfg=yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    from ultralytics import YOLO
    model=YOLO(cfg.pop("model")); model.train(**cfg)
if __name__ == "__main__": main()
