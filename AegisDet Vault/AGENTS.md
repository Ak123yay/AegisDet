# AGENTS.md — Vault Operating Contract

## Mandatory initialization

1. Read `TASKS.md`.
2. Read `CURRENT_STATE.md`.
3. Read `CONTEXT_LOCK.md`.
4. Read `FOUNDATION_MODEL.md` and `DOMAIN_LOCK.md`.
5. Read `wiki/_master-index.md` and `wiki/_code-map.md`.
6. Open the note for the first unchecked task.

## File ownership

- Production code: `project-code/` only.
- Structured knowledge: `wiki/` only.
- Unprocessed material: `raw/`.
- Generated reports: `output/`.
- Historical material: `archive/`.

## Work rules

- Implement only the active task unless explicitly told otherwise.
- Never invent metrics, citations, dataset sizes, or completed experiments.
- Before coding, confirm the target path in `_code-map.md`.
- After coding, update `TASKS.md`, `logs/code-changes.md`, and the corresponding experiment note.
- Every experiment must record hypothesis, frozen controls, config, dataset version, commit, hardware, runtime, raw outputs, result, and conclusion.
- New architecture modules require an ADR and an experiment plan.

## Context reset

When context is unclear, rebuild it from root control files. Do not rely on conversational memory over the vault.
