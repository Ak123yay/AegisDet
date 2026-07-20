---
title: "ADR 004 Use Selective Crop Refinement"
project: "AegisDet-Pro v5.1"
area: "decision"
status: "specification"
tags: ["decision"]
---

# ADR 004 Use Selective Crop Refinement

## Purpose
Preserve the rationale and consequences of the decision: ADR 004 Use Selective Crop Refinement.

## Project specification
**Context:** The bounded crop-refinement path that gives small or uncertain regions more effective pixels affects research validity, implementation cost, or deployment.

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
004, adr, aegisdet, crop, edge-ai, refinement, selective, use.
