---
title: "Domain Lock"
project: "AegisDet-Pro v5.1"
area: "project-control"
status: "locked"
tags: ["dataset", "wildlife"]
---

# Domain Lock

## First domain

> **Wildlife and roadside-animal detection from fixed or slowly moving edge cameras.**

This domain is locked for the first complete research cycle. It naturally contains the cases AegisDet is intended to improve: tiny distant targets, partial occlusion, low light, motion blur, confusing vegetation, and long stretches of easy background frames.

## Initial class taxonomy

| ID | Class | Notes |
|---:|---|---|
| 0 | cat | domestic or feral cat |
| 1 | dog | domestic dog; coyote is not included unless later added explicitly |
| 2 | bobcat | retain only if sufficient high-quality examples exist |
| 3 | deer | all deer grouped initially |
| 4 | opossum | North American opossum |
| 5 | raccoon | raccoon |
| 6 | squirrel | tree and ground squirrels grouped initially |

## Background policy

People, vehicles, birds, rabbits, foxes, coyotes, livestock, rocks, bushes, shadows, bags, posts, and empty frames are background unless the taxonomy is revised through a decision record. Background examples must be retained as hard negatives rather than deleted.

## Dataset constraints

- Split by source video, location, or capture session—not random adjacent frames.
- Keep the test set frozen before router tuning.
- Include empty frames and hard negatives.
- Store source, license, and permission metadata.
- Audit every class for enough examples before keeping it. If bobcat is too rare, merge or remove it through an ADR before training.

## Initial small-object definition

For the first controlled analysis, an object is small when its bounding-box area is less than **1.5% of the full image area**. Also report a pixel-area breakdown so this definition can be compared with standard small-object categories.

## Domain success condition

AegisDet should improve small-object or hard-case performance while preserving a bounded average and tail latency. It does not need to beat YOLO26n on every general-purpose dataset.

## Related notes

- [[FOUNDATION_MODEL]]
- [[wiki/data/datasets/wildlife-dataset-card]]
- [[wiki/data/labeling/bounding-box-rules]]
- [[wiki/data/datasets/small-object-definition]]
