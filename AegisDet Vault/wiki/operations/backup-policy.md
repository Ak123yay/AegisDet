---
title: "Backup Policy"
project: "AegisDet-Pro v5.1"
area: "operations"
status: "reference"
tags: ["operations"]
---

# Backup Policy

Keep the vault and code repository in version control, but exclude datasets, private footage, model weights, engines, `.env`, and generated run folders. Maintain at least one additional encrypted or trusted backup of the vault, dataset manifests, labels, and critical checkpoints. Before a major refactor or dataset version change, tag or snapshot the current state. Test restoration instead of assuming the backup works.

## Related notes
- [[TASKS]]
- [[logs/code-changes]]
