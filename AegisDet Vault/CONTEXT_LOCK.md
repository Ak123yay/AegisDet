# CONTEXT LOCK — Permanent Rules

## Architecture

- Primary base: official `yolo26n.pt`.
- Initial input: 416×416.
- First domain: wildlife/roadside animals.
- Architecture remains CNN-first.
- Build AegisDet-Mini before model surgery.
- Global context is tiny and deep only; no broad high-resolution attention.
- Maximum crop count is explicit and benchmarked.
- Temporal processing is optional and late.

## Experimental integrity

- Same dataset split, hardware, runtime, image size, precision, and batch size for direct comparisons.
- Test set remains frozen and is not used for router threshold tuning.
- Warmup and synchronization are required for latency.
- Report p50/p90/p99, not a single best timing.
- Results are recorded only after execution.
- Failed and negative experiments remain in the history.

## Scope gate

Do not begin learned routing, distillation, QAT, tracking, custom heads, NAS, or multi-device expansion before the required phase gate passes.
