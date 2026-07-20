---
title: "Plug and Play Active Learning for Object Detection"
project: "AegisDet-Pro v5.1"
area: "paper-note"
status: "accepted-reference"
tags: ["research", "source-backed"]
---

# Plug and Play Active Learning for Object Detection — Source Notes

## Summary
PPAL combines uncertainty and diversity to choose object-detection images for annotation without changing detector architecture.

## Method or evidence
The method first builds candidates using difficulty-calibrated classification/localization uncertainty, then applies category-conditioned similarity and diversity selection.

## AegisDet lesson
Use a simpler version of this two-stage logic for AegisDet: rank uncertain failures, then remove near-duplicate frames before annotation.

## Caution
The original selection method and reported gains are dataset-dependent. Start with transparent signals and measure labeling value per round.

## Primary sources
- https://arxiv.org/abs/2211.11612
- https://github.com/ChenhongyiYang/PPAL

## Related notes
- [[data/active-learning/uncertainty-sampling]]
- [[data/active-learning/diversity-sampling]]

## Research-integrity rule
Source-reported results are context only. Local AegisDet claims require its own frozen experiment and benchmark.
