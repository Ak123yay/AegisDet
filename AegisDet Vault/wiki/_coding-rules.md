# _coding-rules.md

- Production code belongs only in the sibling `../aegisdet/` repository.
- The vault contains specifications, decisions, and human-readable experiment records.
- Check `wiki/_code-map.md` before creating or moving code.
- Use Python 3.10 or 3.11 and type annotate reusable interfaces.
- Keep training, evaluation, inference, export, and benchmarking separate.
- Store parameters in tracked configs; never hard-code local absolute paths.
- Add deterministic tests for coordinate transforms, routing, merging, and metrics.
- Record dataset version, commit, config, hardware, runtime, precision, image size, and seed for experiments.
- Never alter more than one major variable in a controlled ablation.
- Export architecture changes early to detect unsupported operators.
