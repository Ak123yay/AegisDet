---
title: "MobileViT"
project: "AegisDet-Pro v5.1"
area: "research-source"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# MobileViT

## Summary
MobileViT combines convolutional local processing with transformer-style global processing in a mobile-oriented architecture.

## Method or evidence
The ICLR 2022 paper treats transformers as a form of global convolution inside a lightweight network and evaluates classification, detection, and segmentation.

## AegisDet lesson
It supports the broad hybrid premise, while AegisDet narrows the global component and tests it inside an adaptive detector.

## Caution
Do not use “CNN + ViT” itself as the novelty claim. MobileViT already establishes that family of designs.

## Primary sources
- https://arxiv.org/abs/2110.02178
- https://machinelearning.apple.com/research/vision-transformer
- https://github.com/apple/ml-cvnets

## Related notes
- [[PROJECT_CONTEXT]]
- [[research/models/mobilevitv2]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
