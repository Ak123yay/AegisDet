---
title: "Result Archive Process"
project: "AegisDet-Pro v5.1"
area: "operations"
status: "reference"
tags: ["operations"]
---

# Result Archive Process

For every meaningful run, preserve the resolved config, commit hash, dataset version, environment/runtime versions, command, raw predictions or evaluator outputs, timing samples, summary table, plots, failure examples, and conclusion. Large weights may remain in external storage, but the vault must store their hash and location. Superseded results move to archive; they are not deleted or overwritten.

## Related notes
- [[TASKS]]
- [[logs/code-changes]]
