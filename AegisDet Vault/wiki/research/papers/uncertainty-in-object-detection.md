# Uncertainty in Object Detection — Synthesis Note

## Scope

A detector can be uncertain about class identity, object existence, localization, or stability across transforms/frames. AegisDet initially uses transparent proxy signals because most deployed YOLO outputs provide confidence and boxes rather than a complete Bayesian uncertainty estimate.

## Initial signals

- confidence within a near-threshold interval;
- top-class margin or entropy when full class probabilities are available;
- number and density of small detections;
- high-overlap same-class predictions;
- localization variation under light augmentation;
- temporal flicker for video.

## Calibration requirement

Plot each signal against actual baseline error and whether refinement corrected the frame. Tune thresholds on validation data only. Confidence is not automatically calibrated, and quantization may change its distribution.

## Source anchors

- PPAL: https://arxiv.org/abs/2211.11612
- DynamicDet: https://arxiv.org/abs/2304.05552

## AegisDet consequence

The rule router is an interpretable measurement instrument. Learned routing begins only after it has generated correction labels and signal/error data.
