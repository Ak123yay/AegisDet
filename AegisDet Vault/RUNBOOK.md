# AegisDet Runbook

## Phase 0 commands

```powershell
cd "AegisDet Vault\project-code"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# Install the CUDA PyTorch command selected at pytorch.org
pip install -r requirements.txt
pip install -e .
python scripts/check_environment.py | Tee-Object ..\output\environment-check.txt
python -m unittest discover -s tests -v
```

## Phase 1 commands

After editing `data/wildlife.yaml` and completing the data audit:

```powershell
python scripts/train_baseline.py --config configs/baseline_yolo26n.yaml
python scripts/evaluate_baseline.py --model runs/baseline_yolo26n/weights/best.pt --data data/wildlife.yaml
python scripts/export_onnx.py --model runs/baseline_yolo26n/weights/best.pt
```

## Phase 2 commands

```powershell
python scripts/run_aegisdet_mini.py --model runs/baseline_yolo26n/weights/best.pt --image path\to\image.jpg
python scripts/benchmark_latency.py --model runs/baseline_yolo26n/weights/best.pt --images data\wildlife\images\test
```

## Run discipline

Before each experiment, create or update its wiki note with the hypothesis and frozen setup. Afterward, attach the raw output, update TASKS, and write a keep/modify/remove conclusion.
