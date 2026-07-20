---
title: "Deployment User Story"
project: "AegisDet-Pro v5.1"
area: "product"
status: "reference"
tags: ["product"]
---

# Deployment User Story

A deployment operator exports the same validated model to ONNX, verifies parity, and benchmarks it on a named backend. The operator can see model hash, runtime version, engine/provider, precision, input contract, p50/p90/p99 latency, memory, and known fallbacks. Unsupported operators or prediction drift block support even if a timing result looks fast.

## Related notes
- [[DOMAIN_LOCK]]
- [[AegisDet_Design/claims-and-non-claims]]
