# Deep Research Coverage Map

| Research-plan area | Canonical vault location |
|---|---|
| Thesis and question | [[PROJECT_CONTEXT]] |
| Locked architecture | [[CONTEXT_LOCK]], [[AegisDet_Design/full-aegisdet-pro-definition]] |
| Base detector | [[FOUNDATION_MODEL]], [[wiki/research/models/yolo26]] |
| CNN-first backbone | [[wiki/architecture/backbone/cnn-first-backbone]] |
| Tiny global tokens | [[wiki/architecture/global-context/tiny-global-token-context]] |
| Router | [[wiki/architecture/router/rule-based-router-v1]], [[wiki/architecture/router/learned-router-v2]] |
| Crop refinement | [[wiki/architecture/crop-refine/selective-crop-refinement]] |
| Temporal stability | [[wiki/architecture/temporal/temporal-stability]] |
| Dataset strategy | [[DOMAIN_LOCK]], [[wiki/data/_data-moc]] |
| Hard-negative learning | [[wiki/data/active-learning/hard-negative-mining-loop]] |
| Training recipe | [[BUILD_PATH]], [[wiki/experiments/_experiments-moc]] |
| Distillation | [[wiki/distillation/progressive-teacher-schedule]] |
| Quantization | [[wiki/quantization/int8-strategy]] |
| Hardware benchmark | [[wiki/benchmarking/same-backend-rule]], [[wiki/deployment/runtimes/opencv-5-dnn]] |
| Ablations | [[wiki/experiments/_experiments-moc]] |
| Timeline and gates | [[BUILD_PATH]], `wiki/timeline/` |
| Claims and limitations | [[AegisDet_Design/claims-and-non-claims]] |
| Starter implementation | [[wiki/implementation/starter-code-guide]], `../aegisdet/` |

## Coverage policy

The vault includes all planning content, but result tables remain empty until actual experiments run. New measured evidence should be added to the existing experiment notes rather than creating disconnected result documents.
