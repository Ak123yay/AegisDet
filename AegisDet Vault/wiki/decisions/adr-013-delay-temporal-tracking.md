---
title: "ADR 013 Delay Temporal Tracking"
project: "AegisDet-Pro v5.1"
area: "decision"
status: "specification"
tags: ["decision"]
---

# ADR 013 Delay Temporal Tracking

## Purpose
Preserve the rationale and consequences of the decision: ADR 013 Delay Temporal Tracking.

## Project specification
**Context:** Video-level stabilization kept separate from image detector accuracy affects research validity, implementation cost, or deployment.

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
013, adr, aegisdet, delay, edge-ai, temporal, tracking.
