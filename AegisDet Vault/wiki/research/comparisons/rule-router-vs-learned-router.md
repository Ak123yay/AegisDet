---
title: "Rule router vs learned router"
project: "AegisDet-Pro v5.1"
area: "comparison"
status: "specification"
tags: ["comparison"]
---

# Rule router vs learned router

## Purpose
Compare Rule router vs learned router without confounding unrelated model, data, or runtime changes.

## Project specification
Create a paired comparison table. Lock the dataset split, input size, evaluator, hardware, batch size, and precision. If the comparison is between runtimes, use the same exported model; if it is between model variants, use the same runtime. Include accuracy, latency percentiles, size, memory where available, and failure-category changes.

State which option lies on the useful Pareto frontier rather than declaring a winner from one metric.

## Evidence required
- Paired configs
- Same-backend or same-model rule applied correctly
- Complete metric table
- Raw results and examples
- Tradeoff conclusion

## Decision rule
Select an option only if it is non-dominated for the intended deployment point or offers a justified domain-specific advantage.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[benchmarking/same-backend-rule]]
- [[metrics/edgescore]]

## Retrieval terms
aegisdet, edge-ai, learned, router, rule.
