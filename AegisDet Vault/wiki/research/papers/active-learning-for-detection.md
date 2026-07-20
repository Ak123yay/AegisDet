# Active Learning for Detection — Synthesis Note

AegisDet uses active learning to improve data efficiency after the frozen baseline exposes real failure modes.

## Workflow

1. Run the baseline on a large unlabeled pool.
2. Rank images using uncertainty and observed failure patterns.
3. Build a candidate pool larger than the annotation budget.
4. remove adjacent video frames and visually redundant samples;
5. enforce class, location, lighting, and failure-category diversity;
6. annotate and review;
7. create a new dataset version;
8. retrain with the same model recipe to isolate the data contribution.

## Primary anchor

PPAL combines uncertainty and diversity without changing the detector architecture: https://arxiv.org/abs/2211.11612

## Evaluation

Report annotation count, object count, category distribution, duplicate rate, baseline-vs-v2 performance, and which failure categories changed. Do not claim data efficiency without comparing against a random or simpler selection baseline when feasible.
