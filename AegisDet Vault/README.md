# AegisDet Vault

A source-backed, implementation-ready Obsidian/RAG workspace for **AegisDet-Pro v5.1**.

## Open

Unzip the archive, open Obsidian, choose **Open folder as vault**, and select `AegisDet Vault`.

## Start

Read [[START_HERE]], then [[TASKS]]. The project is currently at Phase 0. No experimental results are prefilled.

## Source-of-truth hierarchy

1. `TASKS.md`
2. `CONTEXT_LOCK.md`
3. `FOUNDATION_MODEL.md` and `DOMAIN_LOCK.md`
4. `wiki/_master-index.md`
5. `wiki/_code-map.md`
6. relevant wiki notes
7. `raw/`

## Directory responsibilities

- `wiki/` — atomic structured knowledge and experiment specifications.
- `project-code/` — working implementation, configs, tests, and scripts.
- `raw/` — imported planning text and unprocessed ideas.
- `attachments/` — source documents.
- `logs/` — code, research, experiment, and decision history.
- `output/` — environment reports, metrics, plots, and audit reports.
- `archive/` — superseded material; preserve history.

## Base detector

Official COCO-pretrained `yolo26n.pt`, fine-tuned on the locked wildlife domain. See [[FOUNDATION_MODEL]].
