---
title: "EXP 043 — Quality-Aware Dual-Teacher Distillation"
project: "AegisDet-Pro v5.1"
area: "experiment"
phase: "Phase 6"
status: "blocked"
tags: ["experiment", "phase-6", "dual-teacher"]
---

# EXP 043 — Quality-Aware Dual-Teacher Distillation

## Research question

Can validation-calibrated fusion of YOLO26x and RT-DETRv4-X targets outperform progressive and single-teacher distillation?

## Hypothesis

Teacher agreement provides strong supervision, while calibrated teacher selection can exploit complementary strengths without averaging contradictory predictions.

## Frozen controls

- no-KD student,
- YOLO26x-only KD,
- RT-DETRv4-X-only KD,
- progressive YOLO26x → RT-DETRv4-X KD,
- equal total training budget.

## Fusion policy to test

1. Match teacher boxes to ground truth and each other.
2. Use agreement targets when class and localization agree.
3. Choose the better calibrated teacher when one is clearly more reliable.
4. Drop contradictory low-confidence pseudo labels.
5. Weight disagreement examples for hard-case analysis.

## Prohibited shortcut

Do not concatenate all teacher boxes or average unmatched boxes blindly.

## Required metrics

- overall and subset mAP,
- small-object recall,
- false-positive change,
- calibration,
- teacher agreement/disagreement statistics,
- training cost,
- unchanged inference latency.

## Acceptance criterion

Keep dual-teacher KD only if it beats the best single/progressive control with an equal budget and remains stable across a confirmatory seed.

## Result

**Not run.**
