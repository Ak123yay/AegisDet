---
title: "Credential Policy"
project: "AegisDet-Pro v5.1"
area: "responsible-release"
status: "reference"
tags: ["responsible-release"]
---

# Credential Policy

Never store API keys, access tokens, private dataset URLs, passwords, or personal credentials in the vault or repository. Use `.env` files excluded by Git, OS credential storage, or a secret manager. Example files use placeholders only. Rotate a credential immediately if it appears in a committed or shared artifact.

## Related notes
- [[DOMAIN_LOCK]]
- [[AegisDet_Design/claims-and-non-claims]]
