---
title: "ADR 013 — Lock YOLO26x and RT-DETRv4-X Teachers"
project: "AegisDet-Pro v5.1"
area: "decision"
status: "accepted"
tags: ["decision", "teacher", "distillation"]
---

# ADR 013 — Lock YOLO26x and RT-DETRv4-X Teachers

## Context

The student requires a strong same-family teacher and a complementary architecture-diverse teacher.

## Decision

- Primary teacher: YOLO26x (`yolo26x.pt`).
- Secondary teacher: RT-DETRv4-X.
- Fallback secondary teacher: RT-DETRv2-X only after a documented v4 blocker.
- Use staged or cached-target training rather than loading both teachers online simultaneously.
- Deploy only the student.

## Consequences

Phase 6 requires matched no-KD, single-teacher, progressive, and optional quality-aware dual-teacher controls. Teacher fine-tuning and target caching increase training complexity but not inference cost.

## Review condition

Change this decision only if a teacher cannot be fine-tuned on the domain, produces lower domain quality than another candidate, or fails to improve the student in controlled experiments.
