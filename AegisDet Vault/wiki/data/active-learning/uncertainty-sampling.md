---
title: "Uncertainty Sampling"
project: "AegisDet-Pro v5.1"
area: "data"
status: "specification"
tags: ["data"]
---

# Uncertainty Sampling

## Purpose
Define the policy or workflow for confidence, margin, entropy, and instability signals used for routing or sample selection.

## Project specification
Apply this note to the locked wildlife domain and seven-class taxonomy. Record source and license, prevent frame leakage, preserve hard negatives, and version changes. Any selection or labeling rule must be applied consistently and audited with examples.

Data changes are independent variables: retraining on new data must use a frozen model recipe when measuring the data contribution.

## Evidence required
- Written policy
- Representative positive and negative examples
- Audit result
- Dataset version/changelog
- Linked training experiment

## Decision rule
Do not use data that lacks permission, reliable labels, or a traceable split assignment. Revise taxonomy through an ADR, not ad hoc relabeling.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[DOMAIN_LOCK]]
- [[data/_data-moc]]

## Retrieval terms
aegisdet, edge-ai, sampling, uncertainty.
