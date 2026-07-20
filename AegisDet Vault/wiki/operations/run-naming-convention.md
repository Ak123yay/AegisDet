---
title: "Run Naming Convention"
project: "AegisDet-Pro v5.1"
area: "operations"
status: "reference"
tags: ["operations"]
---

# Run Naming Convention

Use `YYYYMMDD_expNNN_model_data_variant_seed` for run folders, for example `20260725_exp001_yolo26n_wildlife-v1_baseline_s42`. Store a resolved config and metadata file inside the run. A run name must never be the only record of settings. Exported artifacts should include the experiment and precision, such as `exp050_aegisdet-mini_int8_openvino.onnx`.

## Related notes
- [[TASKS]]
- [[logs/code-changes]]
