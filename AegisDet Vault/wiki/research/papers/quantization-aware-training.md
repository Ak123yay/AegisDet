# Quantization-Aware Training — Project Synthesis

QAT simulates quantization effects during training so a model can adapt to lower-precision arithmetic. It is not the first deployment step.

## Locked sequence

1. export and validate FP32/FP16;
2. run post-training INT8 quantization with a representative calibration set;
3. evaluate accuracy, small-object behavior, confidence calibration, and runtime;
4. define the unacceptable-loss reason;
5. run QAT only if the runtime benefits and PTQ loss justify it.

## AegisDet-specific risk

The router depends on score distributions. Quantization can shift confidence even when aggregate mAP changes little. Recalibrate route thresholds or train a quantized router only as a measured follow-up.

## Documentation sources

Use the official documentation for the selected export/runtime version (Ultralytics, TensorRT, OpenVINO, ONNX Runtime, or TFLite). Store exact versions in the experiment record because quantization behavior changes with tooling.
