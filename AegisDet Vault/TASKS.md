# TASKS.md — AegisDet Master Work State

_This file is the single source of truth for execution. Agents must complete the first unchecked, non-deferred task in the active phase. Every completed task requires evidence._

<!-- AUTO-ACTIVITY:START -->
## Automated workspace activity

- Last sync: `2026-07-19T22:58:31+00:00`
- Reason: `check`
- Active task: **P0-001 — Copy `AegisDet Vault/`, `aegisdet/`, `data/`, `artifacts/`, `cache/`, and `scratch/` directly into the existing workspace root.**
- Git initialized: `True`
- Branch: `master`
- Commit: `(no commits)`
- Dirty entries: `24`
- Staged files: `0`

This block is mechanical state. Use `workspace_sync.py record` for semantic progress or completion.
<!-- AUTO-ACTIVITY:END -->

## Status legend

| Marker | Meaning |
|---|---|
| `[ ]` | Not started |
| `[x]` | Completed with evidence |
| `BLOCKED` | Cannot proceed until the named dependency is resolved |
| `DEFERRED` | Intentionally postponed; does not block the active phase |
| `OPTIONAL` | Run only if its prerequisite result justifies it |

## Execution rules

1. Work only in the **Active Phase**.
2. Complete tasks in ID order unless a dependency explicitly permits parallel work.
3. Do not check a task without adding evidence to `TASK_EVIDENCE.md`.
4. Code changes belong in `../aegisdet/`; knowledge and conclusions belong in this vault.
5. Generated data, weights, targets, exports, and benchmarks belong in `../data/` or `../artifacts/`.
6. Do not unlock a later phase until the current phase gate is passed.
7. Do not report AegisDet as outperforming YOLO26n until Phase 8 confirms it under equal conditions.
8. Do not fabricate metrics, dataset counts, command output, or completed work.
9. After code changes, run `python tools/workspace_sync.py record ...` from `../aegisdet/`.
10. Git hooks and the file watcher update mechanical state; the agent remains responsible for semantic task completion.

## Locked project decisions

- Student/base detector: `yolo26n.pt`
- Primary teacher: YOLO26x (`yolo26x.pt`)
- Secondary teacher: RT-DETRv4-X
- First domain: wildlife and roadside-animal detection
- Initial classes: cat, dog, bobcat, deer, opossum, raccoon, squirrel
- Initial input size: 416×416
- Initial implementation: frozen YOLO26n + rule router + selective crop refinement
- Architecture: CNN-first with bounded optional compute
- Teachers: training-only; never required in final inference
- Initial hardware: RTX 3060 Ti
- Baseline comparison rule: same data, split, input, device, runtime, precision, batch size, and timing method

---

# Completed project-definition work

- [x] **[PRE-001]** Define AegisDet as a CNN-first adaptive edge-detection family.
- [x] **[PRE-002]** Lock the fixed fast path plus conditional hard-case processing thesis.
- [x] **[PRE-003]** Lock YOLO26n as the student and experimental baseline family.
- [x] **[PRE-004]** Lock YOLO26x and RT-DETRv4-X as the two teacher candidates.
- [x] **[PRE-005]** Lock wildlife/roadside-animal detection as the first domain.
- [x] **[PRE-006]** Lock the initial seven-class taxonomy.
- [x] **[PRE-007]** Create the Obsidian/RAG knowledge vault.
- [x] **[PRE-008]** Separate the vault from the public code repository.
- [x] **[PRE-009]** Create starter router, crop, merge, metric, and pipeline code.
- [x] **[PRE-010]** Create initial unit tests for deterministic components.
- [x] **[PRE-011]** Add source-backed architecture and deployment research.
- [x] **[PRE-012]** Create the automatic workspace-state synchronization framework.

---

# Active Phase — Phase 0: Workspace, governance, and environment

## Objective

Place the supplied folders inside the existing workspace, initialize the code repository, install automatic synchronization, and produce a reproducible GPU-enabled Python environment.

## Workspace integration

- [ ] **[P0-001]** Copy `AegisDet Vault/`, `aegisdet/`, `data/`, `artifacts/`, `cache/`, and `scratch/` directly into the existing workspace root.
- [ ] **[P0-002]** Confirm the vault and code repository are siblings: `AegisDet Vault/` and `aegisdet/`.
- [ ] **[P0-003]** Open `AegisDet Vault/` as an Obsidian vault and verify `START_HERE.md`, this file, and `wiki/_master-index.md`.
- [ ] **[P0-004]** Initialize or confirm Git inside `../aegisdet/`, then run `python tools/install_hooks.py`.
- [ ] **[P0-005]** Run `python tools/workspace_sync.py check` and save the successful output in `output/environment-check.txt`.
- [ ] **[P0-006]** Open the existing VS Code workspace with the `aegisdet/` folder included and approve the automatic watcher task if prompted.
- [ ] **[P0-007]** Modify a harmless tracked text file, verify `AUTO_STATE.md` updates, then revert the test modification.
- [ ] **[P0-008]** Make a test Git commit and verify `logs/auto-code-changes.md` receives the commit record.
- [ ] **[P0-009]** Confirm `aegisdet/AGENTS.md` is visible to Codex before code work.
- [ ] **[P0-010]** Confirm the vault contains no production Python, datasets, weights, ONNX files, or run folders.

## Python and GPU environment

- [ ] **[P0-011]** Confirm Python 3.10 or 3.11 is installed and selected.
- [ ] **[P0-012]** Create `../aegisdet/.venv`.
- [ ] **[P0-013]** Upgrade `pip`, `setuptools`, and `wheel` inside the virtual environment.
- [ ] **[P0-014]** Install a CUDA-enabled PyTorch build compatible with the local NVIDIA driver.
- [ ] **[P0-015]** Install the tracked project dependencies.
- [ ] **[P0-016]** Run `python ../aegisdet/scripts/check_environment.py`.
- [ ] **[P0-017]** Record Python, PyTorch, CUDA, cuDNN, GPU, driver, Ultralytics, OpenCV, ONNX, and ONNX Runtime versions.
- [ ] **[P0-018]** Confirm `torch.cuda.is_available()` is true and the GPU name matches the RTX 3060 Ti.
- [ ] **[P0-019]** Confirm a small CUDA tensor operation completes successfully.
- [ ] **[P0-020]** Confirm Ultralytics can load `yolo26n.pt`.
- [ ] **[P0-021]** Run one pretrained prediction on a legal sample image.
- [ ] **[P0-022]** Save the prediction image under `../artifacts/reports/environment-smoke-test/`.
- [ ] **[P0-023]** Confirm the model exposes training, validation, prediction, and export modes.
- [ ] **[P0-024]** Run all existing deterministic unit tests.
- [ ] **[P0-025]** Freeze exact dependencies into a lock file without replacing the primary project dependency strategy.
- [ ] **[P0-026]** Document environment recreation commands in `RUNBOOK.md`.
- [ ] **[P0-027]** Record all Phase 0 evidence in `TASK_EVIDENCE.md`.
- [ ] **[P0-028]** Pass [[wiki/timeline/phase-0-gate]].

## Phase 0 deliverables

- Working sibling folder structure
- Git repository with installed hooks
- Live watcher or manual sync command confirmed
- Reproducible virtual environment
- CUDA and pretrained-inference proof
- Passing deterministic tests
- Environment report and locked dependencies

---

# Phase 1 — Domain specification and dataset v1

## Objective

Create a legally usable, leakage-resistant, well-documented wildlife dataset that supports fair small-object and hard-case evaluation.

## Problem and class specification

- [ ] **[P1-001]** Reconfirm the exact deployment scenario: roadside camera, trail camera, rover camera, or mixed wildlife camera.
- [ ] **[P1-002]** Define the operational distance, field of view, expected lighting, motion, and frame rate.
- [ ] **[P1-003]** Re-evaluate whether cat and dog belong in the first wildlife taxonomy.
- [ ] **[P1-004]** Write inclusion and exclusion rules for every class.
- [ ] **[P1-005]** Define how ambiguous animals and unknown species are labeled.
- [ ] **[P1-006]** Define how people, vehicles, signs, and empty frames are handled.
- [ ] **[P1-007]** Define truncation, occlusion, crowd, and ignore-region policies.
- [ ] **[P1-008]** Lock the small-object definition before model evaluation.
- [ ] **[P1-009]** Version and freeze `class-map.yaml`.
- [ ] **[P1-010]** Update `DOMAIN_LOCK.md` with the finalized operating assumptions.

## Dataset source research and licensing

- [ ] **[P1-011]** Identify candidate public wildlife datasets and original source pages.
- [ ] **[P1-012]** Record license, attribution, redistribution, and derivative-work conditions for each source.
- [ ] **[P1-013]** Reject sources with unclear or incompatible licensing.
- [ ] **[P1-014]** Record whether each dataset permits public model release.
- [ ] **[P1-015]** Record geographic, seasonal, camera, and class biases.
- [ ] **[P1-016]** Decide which data may be committed, redistributed, or referenced only by download script.
- [ ] **[P1-017]** Create a source manifest with stable source identifiers.
- [ ] **[P1-018]** Add a dataset acquisition script or exact manual procedure.
- [ ] **[P1-019]** Verify checksums or counts after acquisition.
- [ ] **[P1-020]** Create the initial dataset card.

## Label conversion and quality

- [ ] **[P1-021]** Convert all source labels into one normalized internal representation.
- [ ] **[P1-022]** Convert normalized labels into the YOLO training format.
- [ ] **[P1-023]** Validate every label file against image dimensions.
- [ ] **[P1-024]** Reject zero-area, negative, inverted, or out-of-bounds boxes.
- [ ] **[P1-025]** Detect missing images and orphan labels.
- [ ] **[P1-026]** Detect exact duplicate images by cryptographic hash.
- [ ] **[P1-027]** Detect perceptual near-duplicates.
- [ ] **[P1-028]** Manually audit a stratified sample from every source and class.
- [ ] **[P1-029]** Audit small and heavily occluded boxes separately.
- [ ] **[P1-030]** Record annotation corrections in a changelog.
- [ ] **[P1-031]** Create safe visual label previews.
- [ ] **[P1-032]** Calculate per-class image and object counts.
- [ ] **[P1-033]** Calculate box-size and aspect-ratio distributions.
- [ ] **[P1-034]** Calculate empty-frame and hard-negative counts.
- [ ] **[P1-035]** Document unresolved labeling limitations.

## Split design

- [ ] **[P1-036]** Group related frames by video, burst, location, or capture session.
- [ ] **[P1-037]** Prevent groups from crossing train, validation, and test splits.
- [ ] **[P1-038]** Preserve class and difficulty coverage across splits.
- [ ] **[P1-039]** Create a dedicated hard-case validation subset.
- [ ] **[P1-040]** Create small-object, low-light, occlusion, blur, and hard-negative subsets.
- [ ] **[P1-041]** Run duplicate and near-duplicate leakage checks across splits.
- [ ] **[P1-042]** Freeze split manifests before baseline tuning.
- [ ] **[P1-043]** Assign a dataset and split version.
- [ ] **[P1-044]** Store manifests under `../data/` and tracked summaries under `../aegisdet/data/manifests/`.
- [ ] **[P1-045]** Pass the dataset validation test suite.
- [ ] **[P1-046]** Record Phase 1 evidence.
- [ ] **[P1-047]** Pass [[wiki/timeline/phase-1-gate]].

## Phase 1 deliverables

- Locked domain and class policy
- Source/license inventory
- Dataset v1 and reproducible acquisition process
- Label audit and dataset card
- Frozen leakage-resistant splits and difficulty subsets
- Machine-readable validation report

---

# Phase 2 — YOLO26n baseline and reproducible benchmark

## Objective

Train, export, and benchmark the strongest fair YOLO26n control before changing the architecture or inference policy.

## Training infrastructure

- [ ] **[P2-001]** Finalize the baseline configuration schema.
- [ ] **[P2-002]** Add deterministic seed handling.
- [ ] **[P2-003]** Add run-directory naming by experiment ID.
- [ ] **[P2-004]** Save Git commit, config, dataset version, environment, and command with every run.
- [ ] **[P2-005]** Add resume-from-checkpoint support.
- [ ] **[P2-006]** Add disk-space and output-path checks.
- [ ] **[P2-007]** Add training-failure capture and incomplete-run markers.
- [ ] **[P2-008]** Add a one-epoch smoke-test mode.
- [ ] **[P2-009]** Run the one-epoch smoke test.
- [ ] **[P2-010]** Verify metrics and checkpoints are written to `../artifacts/runs/`.

## Baseline tuning

- [ ] **[P2-011]** Train the initial 416×416 YOLO26n baseline.
- [ ] **[P2-012]** Inspect loss curves for divergence or overfitting.
- [ ] **[P2-013]** Evaluate the best checkpoint on validation.
- [ ] **[P2-014]** Run a controlled epoch-budget ablation.
- [ ] **[P2-015]** Run a controlled learning-rate or optimizer ablation only if training is unstable.
- [ ] **[P2-016]** Run an augmentation ablation focused on small and low-light objects.
- [ ] **[P2-017]** Compare 320, 416, and 512 input sizes under a documented budget.
- [ ] **[P2-018]** Select and freeze the official baseline training recipe.
- [ ] **[P2-019]** Retrain the official baseline with at least one confirmation seed.
- [ ] **[P2-020]** Freeze the official baseline checkpoint and hash.

## Accuracy evaluation

- [ ] **[P2-021]** Measure mAP50 and mAP50-95.
- [ ] **[P2-022]** Measure precision and recall.
- [ ] **[P2-023]** Measure per-class AP and recall.
- [ ] **[P2-024]** Measure the locked small-object metrics.
- [ ] **[P2-025]** Measure low-light, occlusion, blur, and hard-negative subsets.
- [ ] **[P2-026]** Generate calibration and confidence-reliability plots.
- [ ] **[P2-027]** Select a frozen baseline confidence threshold without using the test set.
- [ ] **[P2-028]** Generate confusion matrix and class-confusion examples.
- [ ] **[P2-029]** Generate a baseline failure gallery.
- [ ] **[P2-030]** Categorize false positives, false negatives, localization errors, and duplicate detections.

## Export and runtime benchmark

- [ ] **[P2-031]** Export the frozen baseline to ONNX.
- [ ] **[P2-032]** Verify PyTorch/ONNX box, class, and score parity.
- [ ] **[P2-033]** Record unsupported operators and export warnings.
- [ ] **[P2-034]** Implement synchronized warm latency measurement.
- [ ] **[P2-035]** Benchmark p50, p90, and p99 latency.
- [ ] **[P2-036]** Benchmark throughput separately from single-image latency.
- [ ] **[P2-037]** Measure model, ONNX, and runtime memory sizes.
- [ ] **[P2-038]** Record model-load time separately.
- [ ] **[P2-039]** Save raw benchmark samples and environment metadata.
- [ ] **[P2-040]** Calculate baseline EdgeScore using the locked formula.
- [ ] **[P2-041]** Freeze the baseline benchmark report.
- [ ] **[P2-042]** Evaluate the frozen baseline on the test set once the recipe is final.
- [ ] **[P2-043]** Record Phase 2 evidence.
- [ ] **[P2-044]** Pass [[wiki/timeline/phase-2-gate]].

## Phase 2 deliverables

- Frozen YOLO26n checkpoint and hash
- Reproducible training configuration
- Accuracy and subset report
- ONNX parity report
- Same-device latency/memory/size benchmark
- Baseline failure gallery and calibrated threshold

---

# Phase 3 — AegisDet-Mini adaptive inference system

## Objective

Prove the adaptive-compute idea without changing YOLO26n internals.

## Adapter and output normalization

- [ ] **[P3-001]** Complete the Ultralytics adapter.
- [ ] **[P3-002]** Normalize boxes to a documented internal coordinate format.
- [ ] **[P3-003]** Normalize class IDs, scores, image IDs, and metadata.
- [ ] **[P3-004]** Add CPU and CUDA inference-path tests.
- [ ] **[P3-005]** Add empty-detection and malformed-output handling.
- [ ] **[P3-006]** Verify adapter results against direct Ultralytics output.

## Router signals

- [ ] **[P3-007]** Implement small-box count.
- [ ] **[P3-008]** Implement near-threshold detection count.
- [ ] **[P3-009]** Implement class-margin or entropy proxy where available.
- [ ] **[P3-010]** Implement overlap-density signal.
- [ ] **[P3-011]** Implement detection-density safeguards.
- [ ] **[P3-012]** Return structured route reason codes.
- [ ] **[P3-013]** Log all signal values per image.
- [ ] **[P3-014]** Build a router calibration dataset from validation outputs.
- [ ] **[P3-015]** Measure correlation between router signals and baseline failures.
- [ ] **[P3-016]** Sweep router thresholds on validation.
- [ ] **[P3-017]** Select operating points for conservative, balanced, and aggressive refinement.
- [ ] **[P3-018]** Freeze the balanced rule-router configuration.

## Crop planning and inference

- [ ] **[P3-019]** Select candidate boxes by smallness and uncertainty.
- [ ] **[P3-020]** Rank candidates deterministically.
- [ ] **[P3-021]** Add configurable crop padding.
- [ ] **[P3-022]** Clamp crops to image boundaries.
- [ ] **[P3-023]** Merge heavily overlapping crop proposals.
- [ ] **[P3-024]** Enforce a hard maximum crop count.
- [ ] **[P3-025]** Prevent recursive refinement.
- [ ] **[P3-026]** Add crop-size configuration and letterbox handling.
- [ ] **[P3-027]** Rerun the same frozen detector on selected crops.
- [ ] **[P3-028]** Remap crop detections into full-image coordinates.
- [ ] **[P3-029]** Verify remapping on deterministic boundary fixtures.

## Merge and duplicate control

- [ ] **[P3-030]** Implement class-aware NMS across full-image and crop predictions.
- [ ] **[P3-031]** Define confidence handling for base versus refined detections.
- [ ] **[P3-032]** Test same-class duplicates.
- [ ] **[P3-033]** Test cross-class conflicts.
- [ ] **[P3-034]** Test overlapping crop outputs.
- [ ] **[P3-035]** Test empty base and empty crop results.
- [ ] **[P3-036]** Add visual merge-debug output.

## Controlled experiments

- [ ] **[P3-037]** Run baseline versus AegisDet-Mini on validation.
- [ ] **[P3-038]** Measure refinement rate.
- [ ] **[P3-039]** Measure average extra detector calls.
- [ ] **[P3-040]** Measure p50, p90, and p99 system latency.
- [ ] **[P3-041]** Measure overall and small-object accuracy changes.
- [ ] **[P3-042]** Measure new false positives introduced by crop refinement.
- [ ] **[P3-043]** Run crop-size ablation.
- [ ] **[P3-044]** Run max-crop ablation for 1, 2, and 4.
- [ ] **[P3-045]** Compare selective refinement against full SAHI on a fixed subset.
- [ ] **[P3-046]** Select and freeze the AegisDet-Mini configuration.
- [ ] **[P3-047]** Confirm results with a fresh seed or repeat evaluation.
- [ ] **[P3-048]** Evaluate the frozen variant on the test set.
- [ ] **[P3-049]** Record Phase 3 evidence.
- [ ] **[P3-050]** Pass [[wiki/timeline/phase-3-gate]].

## Phase 3 deliverables

- Working AegisDet-Mini pipeline
- Calibrated rule router
- Tested bounded crop and merge system
- Accuracy/refinement/tail-latency comparison
- Keep/modify/reject decision for the adaptive wrapper

---

# Phase 4 — Hard-negative mining and dataset engine v2

## Objective

Improve real-world reliability through model-guided data collection before adding architectural complexity.

- [ ] **[P4-001]** Run the frozen baseline and AegisDet-Mini over an unlabeled pool.
- [ ] **[P4-002]** Save false-positive candidates with model/config metadata.
- [ ] **[P4-003]** Save low-confidence and missed-object candidates.
- [ ] **[P4-004]** Rank candidates using uncertainty.
- [ ] **[P4-005]** Add teacher-student disagreement only after teacher checkpoints exist.
- [ ] **[P4-006]** Add temporal spacing or embedding-based diversity filtering.
- [ ] **[P4-007]** Limit redundant frames from the same clip or burst.
- [ ] **[P4-008]** Create a hard-negative taxonomy: rocks, bushes, shadows, debris, posts, lights, partial shapes, and other observed confusers.
- [ ] **[P4-009]** Manually verify every selected hard negative.
- [ ] **[P4-010]** Correct missed and inaccurate labels found during mining.
- [ ] **[P4-011]** Create dataset v2 without modifying the frozen validation and test sets.
- [ ] **[P4-012]** Update source, license, count, and changelog records.
- [ ] **[P4-013]** Retrain the frozen baseline recipe on dataset v2.
- [ ] **[P4-014]** Retrain or reevaluate AegisDet-Mini on dataset v2.
- [ ] **[P4-015]** Compare v1 versus v2 false positives.
- [ ] **[P4-016]** Compare v1 versus v2 missed small objects.
- [ ] **[P4-017]** Check whether router thresholds require recalibration.
- [ ] **[P4-018]** Freeze dataset v2 and updated router thresholds.
- [ ] **[P4-019]** Build a repeatable active-learning command or workflow.
- [ ] **[P4-020]** Document labeling efficiency and selected-example yield.
- [ ] **[P4-021]** Record Phase 4 evidence.
- [ ] **[P4-022]** Pass [[wiki/timeline/phase-4-gate]].

---

# Phase 5 — True hybrid model and learned routing

## Objective

Add the minimum neural global-context capacity and test learned compute allocation, retaining only modules that improve the measured Pareto frontier.

## Global-context implementation

- [ ] **[P5-001]** Identify the exact YOLO26 feature insertion API.
- [ ] **[P5-002]** Record P4 and P5 tensor shapes and channels.
- [ ] **[P5-003]** Implement the smallest K=4 global-token module.
- [ ] **[P5-004]** Add residual integration and normalization.
- [ ] **[P5-005]** Add shape and gradient tests.
- [ ] **[P5-006]** Export the untrained module path to ONNX immediately.
- [ ] **[P5-007]** Replace unsupported operations before long training.
- [ ] **[P5-008]** Train K=4 at P5 under the frozen recipe.
- [ ] **[P5-009]** Train K=6 at P5.
- [ ] **[P5-010]** Train K=8 at P5.
- [ ] **[P5-011]** Train the best K at P4.
- [ ] **[P5-012]** Test P4+P5 only if single-stage context provides measurable value.
- [ ] **[P5-013]** Test separable attention only as an export-safe fallback.
- [ ] **[P5-014]** Measure overall, small, occluded, and hard-case metrics.
- [ ] **[P5-015]** Measure FLOPs, parameters, ONNX size, and runtime latency.
- [ ] **[P5-016]** Select the best context variant by EdgeScore and hard-case performance.
- [ ] **[P5-017]** Reject global context entirely if it does not earn its cost.

## Learned router

- [ ] **[P5-018]** Define the correct routing label: refinement materially fixes the fast result.
- [ ] **[P5-019]** Generate router-training records without test data.
- [ ] **[P5-020]** Include base-output summaries and cheap feature summaries only.
- [ ] **[P5-021]** Train a small MLP router.
- [ ] **[P5-022]** Measure route precision, recall, and false-skip rate.
- [ ] **[P5-023]** Add expected-extra-compute penalty.
- [ ] **[P5-024]** Sweep compute-penalty weights.
- [ ] **[P5-025]** Calibrate thresholds for target refinement rates.
- [ ] **[P5-026]** Compare learned and rule routing under equal downstream paths.
- [ ] **[P5-027]** Measure router inference overhead.
- [ ] **[P5-028]** Select rule, learned, or hybrid routing.
- [ ] **[P5-029]** Confirm the selected hybrid architecture exports.
- [ ] **[P5-030]** Freeze the pre-distillation student architecture.
- [ ] **[P5-031]** Record Phase 5 evidence.
- [ ] **[P5-032]** Pass [[wiki/timeline/phase-5-gate]].

---

# Phase 6 — Teacher preparation and distillation

## Objective

Improve the frozen lightweight student using training-only YOLO26x and RT-DETRv4-X supervision without changing the final inference graph.

## Teacher preparation

- [ ] **[P6-001]** Confirm official teacher code, checkpoint, license, and export requirements.
- [ ] **[P6-002]** Prepare a cloud/Colab training plan for X-size teachers.
- [ ] **[P6-003]** Fine-tune YOLO26x on the exact dataset v2 class map.
- [ ] **[P6-004]** Validate and calibrate YOLO26x.
- [ ] **[P6-005]** Freeze YOLO26x checkpoint, hash, config, and metrics.
- [ ] **[P6-006]** Fine-tune RT-DETRv4-X on the same classes and train split.
- [ ] **[P6-007]** Validate and calibrate RT-DETRv4-X.
- [ ] **[P6-008]** Freeze RT-DETRv4-X checkpoint, hash, config, and metrics.
- [ ] **[P6-009]** Use RT-DETRv2-X only if a documented v4 blocker is confirmed.
- [ ] **[P6-010]** Compare teacher strengths by class and difficulty subset.

## Cached target engine

- [ ] **[P6-011]** Define the common cached-target schema.
- [ ] **[P6-012]** Store checkpoint hash, class-map version, input geometry, and augmentation identity.
- [ ] **[P6-013]** Generate YOLO26x targets for training images only.
- [ ] **[P6-014]** Generate RT-DETRv4-X targets for training images only.
- [ ] **[P6-015]** Validate class mapping and normalized coordinates.
- [ ] **[P6-016]** Detect missing, duplicated, or stale target records.
- [ ] **[P6-017]** Add target-cache versioning and manifest hashes.
- [ ] **[P6-018]** Verify validation/test targets cannot enter training.

## Distillation controls

- [ ] **[P6-019]** Train the frozen student architecture with ground truth only.
- [ ] **[P6-020]** Match total epochs and augmentation budget for every KD control.
- [ ] **[P6-021]** Run YOLO26x output-level class distillation.
- [ ] **[P6-022]** Add YOLO26x box/IoU distillation.
- [ ] **[P6-023]** Test selected YOLO26x feature transfer only if output KD helps.
- [ ] **[P6-024]** Run RT-DETRv4-X output-level class distillation.
- [ ] **[P6-025]** Add RT-DETRv4-X box/localization distillation.
- [ ] **[P6-026]** Avoid heterogeneous direct feature matching initially.
- [ ] **[P6-027]** Compare no-KD, YOLO-only, and RT-DETR-only results.
- [ ] **[P6-028]** Run progressive YOLO26x → RT-DETRv4-X distillation.
- [ ] **[P6-029]** Test the reverse sequence only if justified by independent results.
- [ ] **[P6-030]** Use agreement as a strong target in the dual-teacher experiment.
- [ ] **[P6-031]** Use calibrated teacher selection for disagreement.
- [ ] **[P6-032]** Reject contradictory low-confidence pseudo labels.
- [ ] **[P6-033]** Test hard-example-weighted KD.
- [ ] **[P6-034]** Repeat the best result with a fresh seed.
- [ ] **[P6-035]** Confirm the final student inference graph and latency are unchanged.
- [ ] **[P6-036]** Freeze the final training recipe.
- [ ] **[P6-037]** Record Phase 6 evidence.
- [ ] **[P6-038]** Pass [[wiki/timeline/phase-6-gate]].

---

# Phase 7 — Export, quantization, runtimes, and optional video

## Objective

Produce a deployable final student and prove its behavior across appropriate edge runtimes.

## Export and parity

- [ ] **[P7-001]** Export the final student to ONNX.
- [ ] **[P7-002]** Verify PyTorch/ONNX parity on easy and hard routes.
- [ ] **[P7-003]** Verify dynamic or fixed input behavior as intended.
- [ ] **[P7-004]** Inspect the ONNX graph for unsupported or fallback operators.
- [ ] **[P7-005]** Record preprocessing and postprocessing exactly.

## Runtime matrix

- [ ] **[P7-006]** Benchmark PyTorch eager as a development reference.
- [ ] **[P7-007]** Benchmark ONNX Runtime on the selected provider.
- [ ] **[P7-008]** Benchmark OpenCV 5 DNN CPU execution.
- [ ] **[P7-009]** Benchmark OpenVINO on compatible Intel hardware when available.
- [ ] **[P7-010]** Build and benchmark TensorRT FP16 on NVIDIA hardware.
- [ ] **[P7-011]** Record runtime versions, optimization flags, and model formats.
- [ ] **[P7-012]** Verify prediction parity for every retained runtime.
- [ ] **[P7-013]** Record p50, p90, p99, throughput, memory, size, and load time.
- [ ] **[P7-014]** Select the primary deployment runtime by target hardware.

## Quantization

- [ ] **[P7-015]** Define the maximum acceptable accuracy loss before quantization.
- [ ] **[P7-016]** Build a representative calibration set.
- [ ] **[P7-017]** Run PTQ INT8.
- [ ] **[P7-018]** Measure overall and small-object accuracy loss.
- [ ] **[P7-019]** Measure router-signal and confidence-calibration changes.
- [ ] **[P7-020]** Measure actual latency, memory, and size improvement.
- [ ] **[P7-021]** Run QAT only if PTQ exceeds the locked loss threshold.
- [ ] **[P7-022]** Compare FP32, FP16, and INT8 Pareto points.
- [ ] **[P7-023]** Freeze the final deployable format.

## Optional video path

- [ ] **[P7-024] OPTIONAL** Build a representative labeled video-clip set.
- [ ] **[P7-025] OPTIONAL** Measure one-frame false triggers and threshold flicker.
- [ ] **[P7-026] OPTIONAL** Add exponential confidence smoothing.
- [ ] **[P7-027] OPTIONAL** Add a bounded multi-frame trigger rule.
- [ ] **[P7-028] OPTIONAL** Add ByteTrack only if identity continuity is required.
- [ ] **[P7-029] OPTIONAL** Measure clip-level recall and false-trigger persistence.
- [ ] **[P7-030] OPTIONAL** Confirm temporal logic does not hide real short appearances.

## Deployment package

- [ ] **[P7-031]** Create reproducible inference commands.
- [ ] **[P7-032]** Create a model card with intended use and limitations.
- [ ] **[P7-033]** Create runtime-specific troubleshooting notes.
- [ ] **[P7-034]** Create a demo inference application.
- [ ] **[P7-035]** Test the deployment package on a clean environment.
- [ ] **[P7-036]** Record Phase 7 evidence.
- [ ] **[P7-037]** Pass [[wiki/timeline/phase-7-gate]].

---

# Phase 8 — Final ablations, research report, public release, and Stardance

## Objective

Turn the measured system into a defensible research artifact and a usable open-source Stardance submission.

## Final experimental matrix

- [ ] **[P8-001]** Freeze all final checkpoints, configs, dataset versions, and code commit.
- [ ] **[P8-002]** Run the final YOLO26n baseline.
- [ ] **[P8-003]** Run baseline + selective crop refinement.
- [ ] **[P8-004]** Run dataset v2 baseline.
- [ ] **[P8-005]** Run the best global-context model.
- [ ] **[P8-006]** Run the selected router.
- [ ] **[P8-007]** Run the best distillation recipe.
- [ ] **[P8-008]** Run the final quantized deployment model.
- [ ] **[P8-009]** Repeat key results with fresh seeds or repeated timing runs.
- [ ] **[P8-010]** Report negative and rejected experiments.
- [ ] **[P8-011]** Create the complete ablation table.
- [ ] **[P8-012]** Create mAP versus latency Pareto plot.
- [ ] **[P8-013]** Create small-object AP versus p90 latency plot.
- [ ] **[P8-014]** Create accuracy versus model-size plot.
- [ ] **[P8-015]** Create refine-rate versus accuracy curve.
- [ ] **[P8-016]** Create per-class and difficulty-subset tables.
- [ ] **[P8-017]** Create final failure and recovery gallery.
- [ ] **[P8-018]** State whether AegisDet actually outperforms YOLO26n and under which exact metric/budget.
- [ ] **[P8-019]** Avoid broad claims unsupported by the final matrix.

## Documentation and reproducibility

- [ ] **[P8-020]** Write the public README.
- [ ] **[P8-021]** Add architecture diagram and simple explanation.
- [ ] **[P8-022]** Add installation and environment instructions.
- [ ] **[P8-023]** Add dataset acquisition and licensing instructions.
- [ ] **[P8-024]** Add training, evaluation, export, and benchmark commands.
- [ ] **[P8-025]** Add expected directory structure.
- [ ] **[P8-026]** Add model and dataset cards.
- [ ] **[P8-027]** Add benchmark methodology and raw-result links.
- [ ] **[P8-028]** Add limitations, failure modes, and prohibited safety claims.
- [ ] **[P8-029]** Add citation and third-party license notices.
- [ ] **[P8-030]** Run repository tests and linting on a clean checkout.
- [ ] **[P8-031]** Verify no secrets, private data, weights, caches, or large artifacts are committed.
- [ ] **[P8-032]** Tag the first public release.

## Report and presentation

- [ ] **[P8-033]** Write abstract and research question.
- [ ] **[P8-034]** Write introduction and motivation.
- [ ] **[P8-035]** Write related work with primary citations.
- [ ] **[P8-036]** Write architecture and adaptive-routing method.
- [ ] **[P8-037]** Write dataset and ethics/licensing sections.
- [ ] **[P8-038]** Write training and distillation method.
- [ ] **[P8-039]** Write benchmark protocol.
- [ ] **[P8-040]** Write results and ablations.
- [ ] **[P8-041]** Write failure analysis and limitations.
- [ ] **[P8-042]** Write conclusion and future work.
- [ ] **[P8-043]** Create a technical slide deck or poster.
- [ ] **[P8-044]** Record a concise demo showing easy and routed hard frames.

## Stardance submission

- [ ] **[P8-045]** Confirm the public repository is suitable as a separate Stardance software project.
- [ ] **[P8-046]** Add a clear GitHub description without unproven performance claims.
- [ ] **[P8-047]** Add frequent meaningful commits and preserve development history.
- [ ] **[P8-048]** Create devlogs explaining design decisions and failed attempts.
- [ ] **[P8-049]** Create a usable image/video demo.
- [ ] **[P8-050]** Create a concise project story and technical explanation.
- [ ] **[P8-051]** Verify all public claims match measured results.
- [ ] **[P8-052]** Submit the working release rather than the private vault.
- [ ] **[P8-053]** Record Phase 8 evidence.
- [ ] **[P8-054]** Pass [[wiki/timeline/phase-8-gate]].

---

# Deferred and optional future work

- [ ] **[FUT-001] DEFERRED** Train a full 80-class COCO AegisDet variant.
- [ ] **[FUT-002] DEFERRED** Add additional deployment domains.
- [ ] **[FUT-003] DEFERRED** Add neural crop proposal generation.
- [ ] **[FUT-004] DEFERRED** Explore hardware-aware neural architecture search.
- [ ] **[FUT-005] DEFERRED** Benchmark on Jetson hardware.
- [ ] **[FUT-006] DEFERRED** Benchmark on Raspberry Pi plus accelerator.
- [ ] **[FUT-007] DEFERRED** Add energy-per-frame measurement.
- [ ] **[FUT-008] DEFERRED** Create AegisDet-S, M, and Video family variants.
- [ ] **[FUT-009] DEFERRED** Integrate a proven AegisDet variant into the SLAM car.
- [ ] **[FUT-010] DEFERRED** Release teacher-target generation tooling as a separate package.

---

# Current next action

Complete **P0-001**. After the folders are placed inside the existing workspace, complete P0-002 through P0-005 and install the synchronization hooks.
