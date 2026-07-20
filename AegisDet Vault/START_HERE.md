# START HERE — AegisDet Vault

This vault is the operational brain for AegisDet-Pro. It is designed for Obsidian, retrieval-augmented coding agents, and rigorous experiment tracking.

## Read in this exact order

1. [[TASKS]] — current work state.
2. [[CURRENT_STATE]] — where the project actually is today.
3. [[PROJECT_CONTEXT]] — system definition and research question.
4. [[CONTEXT_LOCK]] — decisions that may not drift silently.
5. [[FOUNDATION_MODEL]] — exact model baseline and fallback.
6. [[DOMAIN_LOCK]] — first dataset domain and class taxonomy.
7. [[BUILD_PATH]] — stage-by-stage execution path.
8. [[wiki/_master-index]] — structured knowledge map.
9. [[wiki/_code-map]] — concept-to-code ownership.

## The one task to do now

Complete Phase 0. Do not build global tokens, learned routing, distillation, or quantization yet.

```text
verify environment
→ run yolo26n.pt inference
→ lock dataset sources
→ create dataset audit
→ train the frozen baseline
```

## Definition of a trustworthy vault

A note is authoritative only when it distinguishes:
- **locked decision**,
- **working hypothesis**,
- **implementation specification**,
- **measured result**,
- **open question**.

No measured results are included yet because the experiments have not been run.
