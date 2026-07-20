# AGENTS.md — AegisDet Knowledge Vault

## Purpose

This folder is the private knowledge, planning, decision, and experiment-record system. Actual implementation belongs in the sibling `../aegisdet/` folder.

## Read order

1. `TASKS.md`
2. `CURRENT_STATE.md`
3. `CONTEXT_LOCK.md`
4. `PROJECT_CONTEXT.md`
5. `FOUNDATION_MODEL.md`
6. `TEACHER_MODELS.md`
7. `wiki/_master-index.md`
8. `wiki/_code-map.md`
9. Notes relevant to the first active task

## Source priority

1. `TASKS.md`
2. `CONTEXT_LOCK.md`
3. `CURRENT_STATE.md`
4. Accepted ADRs
5. Project/model/domain lock files
6. Structured wiki notes
7. Generated state files
8. `raw/`

Generated state may report file activity but cannot override a manual architecture decision or experiment result.

## Allowed content

- Markdown knowledge
- task state and evidence
- architecture specifications
- research notes and citations
- human-readable experiment plans and conclusions
- decisions, logs, indexes, diagrams, and lightweight documentation assets

## Prohibited content

- production Python
- executable training or inference scripts
- datasets or private images
- model checkpoints
- cached teacher targets
- ONNX or TensorRT files
- large run directories

## Work-state rules

- `TASKS.md` is authoritative.
- Complete the first unchecked, non-deferred task in the active phase.
- Every completed task needs an entry in `TASK_EVIDENCE.md`.
- Do not mark training, evaluation, or benchmarks complete without actual output.
- Preserve rejected experiments.
- Update indexes rather than creating duplicate canonical notes.

## Automatic synchronization

Mechanical code state is updated by the sibling repository's hooks and watcher:

- `AUTO_STATE.md`
- generated blocks in `TASKS.md` and `CURRENT_STATE.md`
- `logs/auto-code-changes.md`
- `wiki/_code-inventory.generated.md`

Do not manually edit generated files or text between AUTO markers.

Semantic updates must be made with:

```bash
cd ../aegisdet
python tools/workspace_sync.py record --task TASK-ID --status complete \
  --summary "What changed" --verification "How it was verified"
```

## End-of-session requirement

Ensure:

- task state is accurate,
- evidence exists,
- code changes are logged,
- experiment notes state planned/running/completed correctly,
- the next task is explicit.
