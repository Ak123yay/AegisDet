# Hooks and Automatic Vault Synchronization

## What is automated

The sibling `../aegisdet/` repository contains:

- `.githooks/pre-commit`
- `.githooks/post-commit`
- `.githooks/post-checkout`
- `.githooks/post-merge`
- `tools/workspace_sync.py`
- `tools/watch_workspace.py`
- `tools/install_hooks.py`
- `.vscode/tasks.json`

The system automatically maintains:

- `AUTO_STATE.md`
- the automated block in `CURRENT_STATE.md`
- the automated activity block in `TASKS.md`
- `logs/auto-code-changes.md`
- `wiki/_code-inventory.generated.md`

## What is not safely automatable

A hook can identify changed files and commits, but it cannot honestly decide that a research task is complete. Codex must use:

```bash
python tools/workspace_sync.py record \
  --task P0-016 \
  --status complete \
  --summary "Verified the environment" \
  --verification "Environment script passed"
```

That command marks the task, adds evidence, updates current state, and writes the human-readable change log.

## Installation

From the sibling code repository:

```bash
python tools/install_hooks.py
python tools/workspace_sync.py check
```

Git hooks run on commits, checkouts, and merges. The VS Code watcher provides live file-change updates while the code folder is open.
