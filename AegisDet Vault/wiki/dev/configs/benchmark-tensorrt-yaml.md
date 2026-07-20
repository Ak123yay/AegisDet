---
title: "benchmark-tensorrt.yaml"
project: "AegisDet-Pro v5.1"
area: "configuration"
status: "specification"
tags: ["configuration"]
---

# benchmark-tensorrt.yaml

## Purpose
Define every parameter required by the configuration `benchmark-tensorrt.yaml`.

## Project specification
The real machine-readable config belongs in `../aegisdet/configs/`. This note explains ownership and expected fields: model/checkpoint, data version, image size, training or inference parameters, router thresholds, crop limits, merge policy, precision, device, seed, output name, and phase.

No experiment may be identified only by a run-folder name; the exact config must be archived with results.

## Evidence required
- Machine-readable config exists
- Schema/required fields checked
- Config copied into run output
- No hidden command-line override
- Linked experiment note

## Decision rule
A config is frozen once the run begins. Any material change creates a new run/config identity.

## Next action
- [ ] Convert this specification into the active phase artifact only when [[TASKS]] unlocks it.

## Related notes
- [[_code-map]]
- [[experiments/_experiments-moc]]

## Retrieval terms
aegisdet, benchmark, edge-ai, tensorrt, yaml.
