from __future__ import annotations
import argparse, json, time
from pathlib import Path
import cv2
from aegisdet.adapters import UltralyticsAdapter
from aegisdet.metrics import percentile
from aegisdet.pipeline import AegisDetMini

def synchronize() -> None:
    try:
        import torch
        if torch.cuda.is_available(): torch.cuda.synchronize()
    except ImportError: pass

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--model",required=True); p.add_argument("--images",required=True)
    p.add_argument("--limit",type=int,default=100); p.add_argument("--warmup",type=int,default=10); a=p.parse_args()
    paths=[x for x in Path(a.images).rglob("*") if x.suffix.lower() in {".jpg",".jpeg",".png"}][:a.limit]
    images=[cv2.imread(str(x)) for x in paths]; images=[x for x in images if x is not None]
    if not images: raise RuntimeError("No readable images")
    pipe=AegisDetMini(UltralyticsAdapter(a.model));
    for i in range(a.warmup): pipe.run(images[i%len(images)])
    times=[]; refined=0
    for image in images:
        synchronize(); start=time.perf_counter(); output=pipe.run(image); synchronize()
        times.append((time.perf_counter()-start)*1000); refined += int(output.route.refine)
    report={"images":len(images),"refinement_rate":refined/len(images),"p50_ms":percentile(times,50),
            "p90_ms":percentile(times,90),"p99_ms":percentile(times,99),"mean_ms":sum(times)/len(times)}
    print(json.dumps(report,indent=2))
if __name__ == "__main__": main()
