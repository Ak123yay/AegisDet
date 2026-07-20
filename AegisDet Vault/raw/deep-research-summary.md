# Deep Research Summary

## Central conclusion

AegisDet-Pro should not compete by becoming a larger attention-heavy detector. Its strongest research position is a **CNN-first adaptive edge system** that applies extra global or local reasoning only to difficult frames.

## Locked system

1. Fine-tuned YOLO26n fast path.
2. Tiny deep global-context module, tested only after AegisDet-Mini.
3. Router using uncertainty, small-object density, overlap, and optional temporal instability.
4. Selective crop refinement instead of full slicing on every frame.
5. Hard-negative active learning.
6. Progressive teacher distillation only after a stable student exists.
7. ONNX and INT8 deployment with measured backend performance.

## Main research contribution

The broad combination of CNNs and attention is not novel. The defensible contribution is the **bounded allocation of additional compute** and the evidence that this allocation improves a domain-specific edge accuracy/cost tradeoff.

## Success measurements

- mAP50-95 and small-object AP;
- p50/p90/p99 latency;
- refinement rate;
- model size and memory;
- power/energy when measurable;
- failure categories and calibration;
- EdgeScore under equal benchmark conditions.

## Imported source

The complete planning text is stored in `raw/deep-research-full-text.md`. The original DOCX is stored in `attachments/AegisDet-Pro_v5.1_Deep_Research_Plan.docx`.
