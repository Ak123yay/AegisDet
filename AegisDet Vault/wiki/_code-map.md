# CODE MAP

| Responsibility | Canonical code path | Specification |
|---|---|---|
| Data types | `project-code/src/aegisdet/types.py` | [[implementation/modules/data-types]] |
| Geometry and IoU | `project-code/src/aegisdet/geometry.py` | [[implementation/modules/geometry]] |
| Rule router | `project-code/src/aegisdet/router.py` | [[architecture/router/rule-based-router-v1]] |
| Crop planning | `project-code/src/aegisdet/crop_refine.py` | [[architecture/crop-refine/selective-crop-refinement]] |
| Detection merge | `project-code/src/aegisdet/merge.py` | [[architecture/crop-refine/crop-merge-logic]] |
| Pipeline | `project-code/src/aegisdet/pipeline.py` | [[architecture/system/end-to-end-system]] |
| Ultralytics integration | `project-code/src/aegisdet/adapters/ultralytics_adapter.py` | [[implementation/modules/ultralytics-adapter]] |
| Metrics | `project-code/src/aegisdet/metrics.py` | [[metrics/edgescore]] |
| Environment check | `project-code/scripts/check_environment.py` | [[implementation/workflows/environment-setup]] |
| Baseline training | `project-code/scripts/train_baseline.py` | [[experiments/baseline/exp-001-yolo-nano-baseline]] |
| Baseline evaluation | `project-code/scripts/evaluate_baseline.py` | [[experiments/baseline/exp-001-yolo-nano-baseline]] |
| ONNX export | `project-code/scripts/export_onnx.py` | [[experiments/baseline/exp-002-baseline-onnx-parity]] |
| AegisDet-Mini demo | `project-code/scripts/run_aegisdet_mini.py` | [[experiments/crop-refine/exp-020-selective-crop-refine]] |
| Latency benchmark | `project-code/scripts/benchmark_latency.py` | [[benchmarking/latency-measurement-protocol]] |
| Unit tests | `project-code/tests/` | [[testing/test-strategy]] |

Do not create production code in `wiki/`. Update this map before adding a new module.
