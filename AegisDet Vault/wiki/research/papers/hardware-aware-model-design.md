# Hardware-Aware Model Design — Synthesis

## Principle

Parameters and FLOPs are incomplete proxies for deployment performance. Memory movement, tensor shape, operator fusion, thread scheduling, quantization support, and backend graph conversion can dominate latency.

## AegisDet rules

- measure actual target runtimes;
- export after the earliest working custom module;
- prefer common operators and low-resolution context;
- include preprocessing, route logic, crop extraction, additional calls, remapping, and merge in end-to-end timing;
- report tail latency for adaptive paths;
- treat unsupported operators as architecture evidence, not a final packaging problem.

## Research anchors

- EfficientViT multi-scale linear attention: https://arxiv.org/abs/2205.14756
- RepViT mobile CNN design: https://arxiv.org/abs/2307.09283
- OpenCV 5 DNN engine notes: https://github.com/opencv/opencv/wiki/OpenCV-5

The chosen design is the one that performs well on the intended device/backend, not the one with the lowest theoretical FLOPs.
