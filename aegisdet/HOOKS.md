# Hooks and Automatic Vault Updates

## Install

From this repository:

```bash
python tools/install_hooks.py
python tools/workspace_sync.py check
```

The installer sets:

```bash
git config core.hooksPath .githooks
```

## Hook behavior

- `pre-commit`: scans staged files, refreshes generated vault state, and blocks obvious secrets/large artifacts.
- `post-commit`: records the new commit in the vault activity log.
- `post-checkout`: refreshes branch and code inventory.
- `post-merge`: refreshes branch and code inventory.

## Live file updates

`.vscode/tasks.json` starts `tools/watch_workspace.py` when this folder opens in VS Code. The watcher polls source/config/script/test files and updates generated vault state after saves.

The watcher and hooks update mechanical state. Task completion remains evidence-based and is performed with `workspace_sync.py record`.
