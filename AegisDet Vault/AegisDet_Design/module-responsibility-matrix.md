# Module Responsibility Matrix

| Module | Owns | Must not own |
|---|---|---|
| Base detector | initial boxes/classes/scores | route policy |
| Router | decide optional work and reason | modify boxes directly |
| Crop planner | choose bounded regions | classify objects |
| Adapter | translate model outputs to internal types | business logic |
| Remapper | coordinate translation | confidence tuning |
| Merger | duplicate/conflict handling | crop selection |
| Metrics | deterministic calculation | run selection |
| Benchmark harness | timing and metadata | cherry-pick fastest run |
| Experiment note | hypothesis, setup, evidence, conclusion | production code |
