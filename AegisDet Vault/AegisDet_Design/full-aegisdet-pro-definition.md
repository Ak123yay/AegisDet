# Full AegisDet-Pro Definition

AegisDet-Pro v5.1 is a CNN-first YOLO26-style detector plus bounded adaptive processing.

## Mandatory path
- domain-fine-tuned nano detector;
- P3/P4/P5 features;
- YOLO-style neck and head;
- fast output.

## Learned hybrid addition
- one tiny global-token or efficient separable-context block at P4/P5;
- K and placement selected by ablation.

## Adaptive control
- calibrated uncertainty router;
- selective crop refinement;
- explicit maximum compute;
- optional video stabilization.

## Training and deployment
- hard-negative active learning;
- teacher distillation after baseline stability;
- ONNX export;
- runtime comparison;
- PTQ then conditional QAT.

A module is part of the final system only if measured evidence justifies it.
