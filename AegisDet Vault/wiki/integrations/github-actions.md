---
title: "GitHub Actions"
project: "AegisDet-Pro v5.1"
area: "integration"
status: "reference"
tags: ["integration"]
---

# GitHub Actions

Add CI only after the repository exists. Initial workflow: install lightweight package dependencies, run Python syntax checks, run deterministic unit tests, and optionally run the vault audit. Do not download model weights or datasets in basic CI. Protect credentials and keep GPU training outside CI.

## Related notes
- [[legal/credential-policy]]
- [[AegisDet_Design/claims-and-non-claims]]
