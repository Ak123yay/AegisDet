---
title: "Session Workflow"
project: "AegisDet-Pro v5.1"
area: "operations"
status: "reference"
tags: ["operations"]
---

# Session Workflow

At session start, read TASKS, CURRENT_STATE, CONTEXT_LOCK, FOUNDATION_MODEL, DOMAIN_LOCK, the master index, and code map. Open the first unchecked task and its specification. Before modifying code, identify the experiment or test that validates the change. After work, run relevant tests, update TASKS, write a dated code-change entry, update the experiment note, and leave exactly one next action. Do not leave code changes unlogged or phase status ambiguous.

## Related notes
- [[TASKS]]
- [[logs/code-changes]]
