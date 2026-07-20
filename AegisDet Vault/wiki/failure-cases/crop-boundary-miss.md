---
title: "Crop Boundary Miss"
project: "AegisDet-Pro v5.1"
area: "failure-case"
status: "specification"
tags: ["failure-case"]
---

# Crop Boundary Miss

## Purpose
Define and investigate a concrete failure involving the bounded crop-refinement path that gives small or uncertain regions more effective pixels.

## Project specification
Capture the source image or clip, immutable ground truth, full prediction output, route decision, crop regions, model checkpoint, thresholds, and dataset version. Classify the error as false positive, false negative, class confusion, localization, duplicate handling, or temporal instability.

Do not propose architecture changes from one anecdote. Count the failure on a frozen evaluation subset and determine whether the likely fix belongs to data, calibration, routing, crop selection, merge logic, model features, or temporal postprocessing.

## Evidence required
- At least one reproducible example
- Frequency on a defined subset
- Root-cause hypothesis separated from observation
- Follow-up experiment or dataset action
- Before/after evidence after the fix

## Decision rule
Close the failure note only when the error is either reduced by measured evidence, accepted as a documented limitation, or reclassified with justification.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[data/active-learning/hard-negative-mining-loop]]
- [[experiments/baseline/exp-003-baseline-failure-gallery]]

## Retrieval terms
aegisdet, boundary, crop, edge-ai, miss.
