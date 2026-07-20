# TODO.md — AegisDet Build Path

## Phase 0 — Setup
- [ ] Confirm wildlife or roadside-animal detection.
- [ ] Lock the initial class list.
- [ ] Create the GitHub repository.
- [ ] Create Python 3.10/3.11 environment.
- [ ] Install CUDA-enabled PyTorch.
- [ ] Confirm RTX 3060 Ti access.
- [ ] Install Ultralytics, OpenCV, ONNX, ONNX Runtime, NumPy, Pandas, Matplotlib, and PyYAML.
- [ ] Run one pretrained YOLO inference.
- [ ] Freeze `requirements.txt`.

## Phase 1 — Baseline
- [ ] Build and audit dataset v1.
- [ ] Create leakage-resistant train/validation/test splits.
- [ ] Write the dataset card.
- [ ] Train the YOLO nano baseline at 416×416.
- [ ] Evaluate mAP50, mAP50-95, precision, recall, and small-object metrics.
- [ ] Export ONNX and verify prediction parity.
- [ ] Benchmark p50, p90, p99 latency and model size.
- [ ] Build the failure gallery.

## Phase 2 — AegisDet-Mini
- [ ] Implement rule-based router.
- [ ] Implement crop selection and padding.
- [ ] Implement coordinate remapping.
- [ ] Implement class-aware merge logic.
- [ ] Add unit tests.
- [ ] Benchmark baseline versus AegisDet-Mini.
- [ ] Measure refinement rate and tail latency.

## Phase 3 — Data improvement
- [ ] Mine false positives and false negatives.
- [ ] Build hard-negative library.
- [ ] Add uncertainty and diversity sampling.
- [ ] Create dataset v2 and retrain.

## Phase 4 — True hybrid model
- [ ] Add one tiny global-context block.
- [ ] Test K=4, K=6, K=8.
- [ ] Test P4 versus P5.
- [ ] Verify ONNX export.

## Phase 5 — Learned router
- [ ] Build route labels.
- [ ] Train a small router.
- [ ] Add compute penalty.
- [ ] Calibrate threshold.

## Phase 6 — Distillation
- [ ] Select teacher.
- [ ] Test single-teacher KD.
- [ ] Test progressive KD.
- [ ] Test hard-example KD.

## Phase 7 — Deployment
- [ ] Benchmark OpenCV 5 DNN.
- [ ] Benchmark ONNX Runtime.
- [ ] Benchmark OpenVINO.
- [ ] Benchmark TensorRT.
- [ ] Run PTQ INT8.
- [ ] Use QAT only if necessary.

## Phase 8 — Final research
- [ ] Complete ablation matrix.
- [ ] Create Pareto plots.
- [ ] Write final report.
- [ ] Create README, model card, dataset card, demo, and slides.
