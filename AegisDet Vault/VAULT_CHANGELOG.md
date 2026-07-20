# Vault Changelog

## v2 — Perfected planning and starter release

- Locked `yolo26n.pt` as the primary base detector.
- Locked wildlife/roadside animals and the initial taxonomy.
- Replaced repeated generic notes with topic-specific specifications.
- Added source-backed notes for the load-bearing research literature.
- Imported the full deep-research plan and original DOCX.
- Added working deterministic router, crop planner, remapping, merge, metrics, and pipeline code.
- Added Ultralytics adapter and baseline/export/benchmark scripts.
- Added 13 passing unit tests.
- Added automated link, structure, syntax, placeholder, and test audits.
- Added Deep Research Coverage Map and Runbook.

## Honesty boundary

This release is “perfected” as an execution system and starter implementation. It does not fabricate dataset statistics or model results that do not exist yet.

## 2026-07-19 — Dual-teacher plan locked

- Corrected the official teacher name from “YOLO26 XL” to YOLO26x (`yolo26x.pt`).
- Locked YOLO26x as the primary same-family teacher.
- Locked RT-DETRv4-X as the secondary architecture-diverse teacher.
- Retained RT-DETRv2-X as a documented fallback only.
- Added progressive and quality-aware dual-teacher experiments.
- Added train-only cached-target requirements and hardware-safe sequencing.
- Removed the unsupported YOLO26 preprint reference; official Ultralytics documentation is canonical.


## 2026-07-20 — Workspace separation

- Removed the embedded code directory from the vault.
- Moved starter implementation into the sibling public `../aegisdet/` repository.
- Updated the vault code map and all project-code path references.
- Added workspace-level agent rules, VS Code multi-root configuration, setup script, external data/artifact folders, and verification tooling.
