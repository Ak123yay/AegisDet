---
title: "Dataset Split Test"
project: "AegisDet-Pro v5.1"
area: "test-spec"
status: "specification"
tags: ["test-spec"]
---

# Dataset Split Test

## Purpose
Define a deterministic test for the licensed, versioned wildlife image/label collection with leakage-resistant splits.

## Project specification
Create the smallest input that exposes the behavior, define the exact expected output, and ensure the test fails when the implementation is intentionally broken. Geometry, routing, merge, and metric tests must not require model weights. Integration/export tests may require optional dependencies and should be labeled accordingly.

## Evidence required
- Known input and expected output
- Automated test path
- Failure-mode check
- Pass result in audit
- No reliance on test order

## Decision rule
The related module cannot pass its phase gate while this required test is missing or failing.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[testing/test-strategy]]
- [[_code-map]]

## Retrieval terms
aegisdet, dataset, edge-ai, split, test.
