---
title: "make_failure_gallery.py"
project: "AegisDet-Pro v5.1"
area: "script-spec"
status: "specification"
tags: ["script-spec"]
---

# make_failure_gallery.py

## Purpose
Specify the command-line contract and outputs for `make_failure_gallery.py`.

## Project specification
The implementation belongs in `project-code/scripts/`. It must expose explicit arguments, validate paths and required dependencies, fail with useful errors, print or save structured metadata, and avoid hidden global state. The script should be rerunnable from the project-code root.

Research scripts must preserve model, dataset, config, device, runtime, precision, command, and output location.

## Evidence required
- CLI help works
- Happy-path smoke test
- Invalid input produces clear error
- Structured output documented
- Code path matches _code-map

## Decision rule
Mark implemented only when the code exists and its smoke test is logged.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[_code-map]]
- [[implementation/starter-code-guide]]

## Retrieval terms
aegisdet, edge-ai, failure, gallery, make.
