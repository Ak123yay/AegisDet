# _code-map.md — Vault Knowledge to Sibling Code

Actual implementation is in the sibling public repository `../aegisdet/`.

| Concept | Code path from vault | Knowledge note |
|---|---|---|
| Data types | `../aegisdet/src/aegisdet/types.py` | [[implementation/modules/data-types]] |
| Geometry and IoU | `../aegisdet/src/aegisdet/geometry.py` | [[implementation/modules/geometry]] |
| Rule router | `../aegisdet/src/aegisdet/router.py` | [[architecture/router/rule-based-router-v1]] |
| Crop planning | `../aegisdet/src/aegisdet/crop_refine.py` | [[architecture/crop-refine/selective-crop-refinement]] |
| Detection merge | `../aegisdet/src/aegisdet/merge.py` | [[architecture/crop-refine/crop-merge-logic]] |
| AegisDet-Mini pipeline | `../aegisdet/src/aegisdet/pipeline.py` | [[architecture/system/end-to-end-system]] |
| Ultralytics adapter | `../aegisdet/src/aegisdet/adapters/ultralytics_adapter.py` | [[implementation/modules/ultralytics-adapter]] |
| Metrics | `../aegisdet/src/aegisdet/metrics.py` | [[metrics/edgescore]] |
| Environment check | `../aegisdet/scripts/check_environment.py` | [[implementation/workflows/environment-setup]] |
| Baseline training | `../aegisdet/scripts/train_baseline.py` | [[experiments/baseline/exp-001-yolo-nano-baseline]] |
| Baseline evaluation | `../aegisdet/scripts/evaluate_baseline.py` | [[experiments/baseline/exp-001-yolo-nano-baseline]] |
| ONNX export | `../aegisdet/scripts/export_onnx.py` | [[experiments/baseline/exp-002-baseline-onnx-parity]] |
| AegisDet-Mini runner | `../aegisdet/scripts/run_aegisdet_mini.py` | [[experiments/crop-refine/exp-020-selective-crop-refine]] |
| Latency benchmark | `../aegisdet/scripts/benchmark_latency.py` | [[benchmarking/latency-measurement-protocol]] |
| Baseline model config | `../aegisdet/configs/models/baseline_yolo26n.yaml` | [[dev/configs/baseline-yolo-yaml]] |
| AegisDet-Mini config | `../aegisdet/configs/models/aegisdet_mini.yaml` | [[dev/configs/aegisdet-mini-yaml]] |
| Wildlife data config | `../aegisdet/configs/data/wildlife.yaml` | [[data/datasets/wildlife-dataset-card]] |
| Teacher configs | `../aegisdet/configs/distillation/` | [[TEACHER_MODELS]] |
| Unit tests | `../aegisdet/tests/` | [[testing/test-strategy]] |
| Workspace synchronization | `../aegisdet/tools/workspace_sync.py` | [[HOOKS_AND_AUTO_SYNC]] |
| Live file watcher | `../aegisdet/tools/watch_workspace.py` | [[HOOKS_AND_AUTO_SYNC]] |
| Git hook installer | `../aegisdet/tools/install_hooks.py` | [[HOOKS_AND_AUTO_SYNC]] |

## Rule

Do not create a new canonical code path without updating this map first. The vault specifies and records; the sibling repository implements.
