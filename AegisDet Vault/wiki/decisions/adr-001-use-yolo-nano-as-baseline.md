---
title: "ADR 001 Use YOLO Nano as Baseline"
project: "AegisDet-Pro v5.1"
area: "decision"
status: "specification"
tags: ["decision"]
---

# ADR 001 Use YOLO Nano as Baseline

## Purpose
Preserve the rationale and consequences of the decision: ADR 001 Use YOLO Nano as Baseline.

## Project specification
**Context:** The frozen yolo26n control and its supported training/export interface affects research validity, implementation cost, or deployment.

**Decision:** follow the behavior stated by the title.

**Consequences:** future tasks and experiments must respect this constraint. A new result may supersede it only through a new ADR that links the evidence and migration impact.

## Evidence required
- Context and alternatives captured
- Decision unambiguous
- Consequences listed
- Review trigger specified
- Affected notes linked

## Decision rule
Status remains accepted until a later ADR explicitly supersedes it; do not rewrite history silently.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[CONTEXT_LOCK]]
- [[_decision-log]]

## Retrieval terms
001, adr, aegisdet, baseline, edge-ai, nano, use, yolo.
