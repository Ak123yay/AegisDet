---
title: "Failure Case Curation"
project: "AegisDet-Pro v5.1"
area: "data"
status: "specification"
tags: ["data"]
---

# Failure Case Curation

## Purpose
Define the policy or workflow for a reproducible prediction error tied to a model, config, dataset version, and fix hypothesis.

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
aegisdet, case, curation, edge-ai, failure.
