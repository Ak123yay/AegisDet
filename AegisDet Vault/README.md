# AegisDet Vault

This is the private Obsidian/RAG knowledge vault for AegisDet-Pro. It contains the project roadmap, architecture decisions, research, experiment records, and agent context.

## Important separation

```text
AegisDet Vault/  = knowledge and project control
../aegisdet/     = actual public code repository
../data/         = local datasets
../artifacts/    = checkpoints, exports, runs, and reports
```

The vault must not contain production code, weights, datasets, or generated training runs.

## Start here

1. `START_HERE.md`
2. `TASKS.md`
3. `CURRENT_STATE.md`
4. `PROJECT_CONTEXT.md`
5. `CONTEXT_LOCK.md`
6. `wiki/_master-index.md`
7. `wiki/_code-map.md`

## Obsidian

Open this folder itself as an Obsidian vault. Open the sibling `../aegisdet/` folder in VS Code using the workspace file located one level above.
