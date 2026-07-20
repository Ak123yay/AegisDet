# AGENTS.md — AegisDet Code Repository

## Purpose

This folder is the public implementation repository. The sibling `../AegisDet Vault/` is the authoritative knowledge, task, decision, and human-readable experiment system.

## Mandatory session initialization

Read in this order before modifying code:

1. `../AegisDet Vault/TASKS.md`
2. `../AegisDet Vault/CURRENT_STATE.md`
3. `../AegisDet Vault/CONTEXT_LOCK.md`
4. `../AegisDet Vault/PROJECT_CONTEXT.md`
5. `../AegisDet Vault/FOUNDATION_MODEL.md`
6. `../AegisDet Vault/TEACHER_MODELS.md`
7. `../AegisDet Vault/wiki/_master-index.md`
8. `../AegisDet Vault/wiki/_code-map.md`
9. relevant architecture and experiment notes
10. existing source, config, and tests

## Source-of-truth priority

1. Vault `TASKS.md`
2. Vault `CONTEXT_LOCK.md`
3. Vault `CURRENT_STATE.md`
4. Accepted ADRs
5. Locked project/model/domain documents
6. Vault code map and structured notes
7. Existing implementation
8. Raw notes

If code and the vault disagree, stop and record the mismatch. Do not silently choose one.

## Task execution

- Execute the first unchecked, non-deferred task in the active phase.
- Do not implement work absent from `TASKS.md`.
- Add newly discovered required work to `TASKS.md` before implementation.
- Do not skip phase gates.
- Do not mark a task complete without evidence.

## Repository ownership

Allowed:

- production Python
- scripts and CLIs
- tracked configs
- tests and CI
- public documentation and small safe fixtures

Prohibited:

- datasets and private images
- checkpoints and pretrained weights
- ONNX/TensorRT exports
- cached teacher targets
- secrets and `.env`
- large run or benchmark directories

## Before code changes

1. Check `../AegisDet Vault/wiki/_code-map.md`.
2. Read the related architecture or experiment note.
3. Inspect current code and tests.
4. Define the smallest scoped change.
5. Define verification before implementation.
6. Update the code map first when adding a canonical path.

## Implementation rules

- Use type annotations for reusable interfaces.
- Keep training, evaluation, inference, export, and benchmarking separate.
- Store experiment parameters in tracked configs.
- Never hard-code local absolute paths.
- Validate shapes, class maps, coordinates, and input assumptions.
- Add deterministic tests for logic that can invalidate results.
- Export architecture additions early.
- Avoid unrelated refactoring.
- Do not add dependencies without documenting the reason.

## Locked architecture

- CNN-first YOLO26n-derived student
- bounded adaptive compute
- maximum crop count
- no recursive refinement
- no full high-resolution attention
- YOLO26x primary teacher
- RT-DETRv4-X secondary teacher
- teachers are training-only
- optional modules require controlled ablations

## Automatic update protocol

Hooks and the watcher maintain mechanical code/Git state. They do not invent semantic conclusions.

After a meaningful code change, run:

```bash
python tools/workspace_sync.py record \
  --task TASK-ID \
  --status progress \
  --summary "What changed" \
  --verification "Tests or checks run"
```

Use `--status complete` only when the task is fully verified. This command:

- updates the task checkbox when complete,
- appends task evidence,
- updates current workspace state,
- appends the human-readable change log,
- refreshes the generated code inventory.

Git hooks run fallback synchronization before and after commits.

## Verification

Before completing implementation work:

1. run targeted unit tests;
2. run the applicable integration or smoke test;
3. inspect generated output;
4. record the command and result;
5. ensure unrelated tests did not regress.

## End-of-session output

```text
Completed:
Code files changed:
Vault files updated:
Verification:
Current blockers:
Next task:
```
