---
title: "OpenCV 5 DNN"
project: "AegisDet-Pro v5.1"
area: "deployment-runtime"
status: "accepted-reference"
tags: ["opencv", "deployment", "cpu"]
---
# OpenCV 5 DNN

## Current role

OpenCV 5 DNN is an additional **CPU inference backend** for AegisDet ONNX models and the natural image-processing layer for camera input, resizing, crop extraction, visualization, and coordinate work.

## Official engine behavior

OpenCV 5 adds explicit DNN engine selection. The automatic mode tries the new engine and can fall back to the classic engine. Builds can also integrate ONNX Runtime. The new DNN engine currently runs on CPU; GPU users must use the classic path or an ONNX Runtime build/provider until new-engine GPU support is available.

## Benchmark requirements

- record exact OpenCV build/version and engine selection;
- use the same validated ONNX artifact as other CPU runtime tests;
- confirm input layout, normalization, output head, and postprocessing;
- verify prediction parity before latency;
- report model load time, p50/p90/p99, memory, and fallback behavior;
- compare with ONNX Runtime and OpenVINO on the same CPU.

## Not the NVIDIA default

TensorRT remains the main NVIDIA/Jetson deployment path. OpenCV DNN is not substituted merely because OpenCV is already used for image operations.

## Official source

- https://github.com/opencv/opencv/wiki/OpenCV-5

## Related notes

- [[deployment/runtimes/onnx-runtime]]
- [[deployment/runtimes/openvino]]
- [[deployment/runtimes/tensorrt]]
- [[experiments/quantization/exp-052-runtime-export-matrix]]
