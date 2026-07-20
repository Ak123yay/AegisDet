AegisDet-Pro v5.1
Adaptive Edge Perception with Selective Global Context
A 25+ page research, implementation, and benchmarking plan for a YOLO26-style adaptive edge object detector
Prepared for: Aarush Katam
Date: June 29, 2026
Project area: low-power edge AI, robotics perception, object detection, adaptive inference
Core thesis
AegisDet-Pro should not try to become a bigger transformer detector. Its strongest path is a CNN-first, YOLO26-style detector that spends extra compute selectively: only when uncertainty, small-object density, or temporal instability indicates that the frame is difficult. The project succeeds if it proves a better accuracy-latency-power tradeoff than a same-backend YOLO26n baseline on a domain-specific edge task.

Table of Contents
1. Executive Summary
2. Project Thesis and Research Question
3. What Existing Models Already Solve
4. Why AegisDet-Pro Should Not Become Attention-Heavy
5. Final Locked Architecture
6. End-to-End Dataflow
7. YOLO26-Style Detector Interface
8. CNN-First Backbone Design
9. Tiny Global-Token Context Block
10. Uncertainty Router
11. Selective Crop-Refine Branch
12. Temporal Stability Layer
13. Mathematical Formulation
14. Dataset Strategy
15. Hard-Negative Active Learning
16. Training Recipe
17. Progressive Multi-Teacher Distillation
18. Quantization and Export Strategy
19. Hardware Benchmarking Plan
20. Ablation Matrix
21. Implementation Roadmap
22. Timeline
23. Risk Register
24. Success Criteria
25. ASSIP/MIT Narrative Fit
26. Codebase Structure
27. Pseudocode Appendix
28. Experiment Log Template
29. Final Deliverables
30. References

1. Executive Summary
AegisDet-Pro v5.1 is a proposed lightweight object detection research project focused on low-power edge AI. The project is designed around one defensible claim: a detector can keep the deployment advantages of a modern YOLO-style architecture while improving accuracy-per-compute through selective global reasoning and selective small-object refinement. The model is not intended to beat every detector on every dataset. It is intended to beat a strong nano-scale YOLO26 baseline on a concrete edge task, measured under equal runtime and hardware conditions.
The newest YOLO26 literature reports several changes that are directly relevant to this project: native NMS-free end-to-end inference through a dual-head design, removal of Distribution Focal Loss for a lighter detection head, Progressive Loss to shift supervision toward the inference-time output, STAL to improve small-object positive assignment, and MuSGD as a hybrid optimizer intended to stabilize training. The YOLO26 paper reports 40.9-57.5 COCO mAP across model scales at 1.7-11.8 ms T4 TensorRT latency [1]. This makes YOLO26n a serious baseline rather than a weak target.
The strongest way to improve over YOLO26n is not to make a heavier transformer. MobileViTv2 shows that standard multi-head attention is a latency bottleneck on mobile devices and that separable linear-complexity attention is more practical [4]. Mobile-Former shows that very few learned global tokens can add global priors while keeping compute low [5]. RepViT shows that a pure lightweight CNN redesigned with ViT-era design lessons can reach strong mobile latency and accuracy [6]. EfficientViT shows that linear attention can support dense prediction with a global receptive field while remaining hardware-efficient [7]. DynamicDet and DynamicViT show that adaptive compute is a real research lever, not just a software trick [8][9].
The final proposed system is therefore a YOLO26-style detector core with a CNN-first backbone, one tiny global-token context insertion, an uncertainty router, selective crop refinement, progressive multi-teacher distillation, hard-negative active learning, optional temporal smoothing, and INT8 deployment. The most important success metric is not raw mAP alone. It is EdgeScore: mAP50-95 divided by latency and model size, plus energy-per-frame when power instrumentation is available.


2. Project Thesis and Research Question
The core research question is: can a lightweight detector outperform YOLO26n on a domain-specific edge task by spending extra compute only when the frame is difficult? This question is stronger than the vague goal of building a “better YOLO.” It is specific, measurable, and aligned with low-power AI. The project is not about universal state of the art. It is about a Pareto improvement under real constraints.
AegisDet-Pro v5.1 should be framed as an adaptive edge perception system. The mandatory path performs fast YOLO-style detection. Optional modules activate when uncertainty, small-object density, or temporal instability suggests that the fast path is likely to fail. This lets the model preserve a low average latency while improving hard-case accuracy. The system can be evaluated at three levels: model accuracy, runtime efficiency, and operational reliability.
The hypothesis is that many edge detection frames are easy. For example, in a road-sensing task, a large animal crossing near the camera may be easy to detect. In contrast, a small animal near the edge of the frame, a blurry object at dusk, or a shape partially hidden by bushes may require more context or local refinement. A fixed model spends the same compute on both easy and hard frames. AegisDet-Pro spends extra compute only on hard frames.
The project becomes research-grade when it includes controlled ablations. Each module must be tested separately: global tokens, router, crop refinement, distillation, hard-negative mining, temporal smoothing, and quantization. If a module does not improve EdgeScore or small-object AP, it should be removed. This discipline prevents the project from becoming a bloated collection of trendy modules.


3. What Existing Models Already Solve
AegisDet-Pro must be designed with a realistic view of the current literature. Existing models already solve many obvious ideas. A simple CNN-transformer hybrid is not novel. MobileViT, MobileViTv2, Mobile-Former, EfficientViT, YOLO12, RepViT, and other models already explore the relationship between local convolutional processing and global attention. Therefore, AegisDet-Pro should not claim novelty from merely combining CNNs and transformers.
YOLO26 already addresses a major deployment bottleneck: NMS and heavy detection heads. Its paper reports native NMS-free inference through a dual-head design, removal of DFL, and training improvements targeted at small objects and training stability [1]. AegisDet-Pro should inherit these advantages rather than fighting them. The model should be compatible with YOLO-style training and export where possible.
MobileViTv2 demonstrates that transformer-style global context can be useful on mobile vision tasks, but also that classical multi-head self-attention is too expensive for many resource-constrained devices. The MobileViTv2 paper identifies MHA as a latency bottleneck and replaces it with separable self-attention of linear complexity [4]. This supports using tiny or separable attention, not broad attention at high resolution.
Mobile-Former shows that global reasoning does not require thousands of visual tokens. It uses a small transformer branch with very few tokens and a bridge to MobileNet features [5]. This is one of the strongest inspirations for AegisDet-Pro: global tokens should be sparse, learned, and deployed only at deep low-resolution stages. RepViT and EfficientViT further reinforce the same design principle: the best edge models are not necessarily transformer-heavy; they are hardware-aware and use global operations carefully [6][7].


4. Why AegisDet-Pro Should Not Become Attention-Heavy
The most tempting mistake is to keep adding transformer blocks. That would likely make the model worse for the intended goal. Edge models fail not only because they are inaccurate, but because they are hard to export, memory-heavy, slow on CPU, or unstable under INT8 quantization. AegisDet-Pro is supposed to be low-power and deployable. Therefore, the architecture must be constrained by operator support and real runtime behavior.
YOLO12 is useful as a warning. Attention-centric detectors can be competitive on GPU-oriented benchmarks, but heavy attention can increase memory use and CPU latency. The AegisDet-Pro strategy is to borrow the useful part of attention - global context - without adopting a transformer-heavy macro-architecture. The global context should be narrow, deep, and optional.
The strongest architecture is a hybrid at the system level, not a transformer at every stage. A CNN handles the dense local feature extraction. A tiny global-token block adds scene context. A router decides when extra computation is needed. A crop-refine branch targets small or uncertain objects. A temporal module stabilizes video detections. This creates a more realistic edge system than a monolithic attention-heavy detector.
There is also a research credibility issue. If AegisDet-Pro simply adds attention to YOLO, reviewers or judges can say that many models already do this. If it instead proves that uncertainty-driven selective compute improves edge accuracy-per-latency, the contribution is sharper. The project becomes about adaptive perception under constraints, not about copying attention trends.


5. Final Locked Architecture
The locked architecture is AegisDet-Pro v5.1: a YOLO26-inspired adaptive edge detector. The detector uses a fast mandatory path and optional hard-case modules. The mandatory path must be strong enough to run alone. The optional path must activate only when it can justify its latency.
The architecture has six major parts. First, the input is resized to a default resolution such as 416 or 512 pixels depending on the target hardware. Second, a CNN-first backbone extracts local features using YOLO26-style or RepViT-inspired blocks. Third, one tiny global-token context module adds global reasoning at a deep low-resolution stage. Fourth, a YOLO26-style neck and dual-head detector output fast predictions. Fifth, an uncertainty router reads the detections and feature summaries to decide whether extra processing is needed. Sixth, optional crop refinement and temporal smoothing improve small or unstable detections.
The key design rule is bounded adaptivity. AegisDet-Pro can spend more compute on hard frames, but the worst-case cost must be capped. For example, the system can allow at most four crop refinements per frame. That makes the model practical for real-time deployment because the average case and worst case are both measurable.
This version should be treated as the final architecture unless experiments prove a specific simplification or improvement. The project should not keep expanding the diagram. The research value now comes from implementing clean variants and proving which modules actually help.
AegisDet-Pro v5.1

Input frame: 416x416 or 512x512
  -> CNN-first YOLO26/RepViT-style backbone
  -> P3, P4, P5 multi-scale features
  -> Tiny global-token context block at P4/P5
  -> YOLO26-style PAN/FPN neck
  -> Dual-head detector interface
  -> Fast end-to-end output
  -> Router reads uncertainty + small-object density + temporal instability
      if easy: return fast output
      if hard: activate global context and/or crop refinement
      if video: apply ByteTrack or temporal smoothing
  -> Final boxes, classes, scores, optional track IDs



6. End-to-End Dataflow
The dataflow separates the fast mandatory path from the optional hard-case path. This is important because the base detector must remain useful even if optional modules are disabled. The system should be able to run in three modes: baseline mode, adaptive mode, and deployment-hardened mode.
Baseline mode runs YOLO26n and AegisDet-Pro without optional crop refinement or temporal logic. This establishes the real model-level difference. Adaptive mode activates the router, global-context path, and crop-refine branch. Deployment-hardened mode includes quantization, export fallback handling, and hardware-specific runtime measurements.
The router is placed after a fast first pass because this is easier to deploy than routing inside every layer. Internal dynamic routing can be powerful, but it is harder to export and benchmark. A fast-first-pass design has a practical advantage: the model always produces a valid answer quickly, and extra compute is added only if the frame deserves it.
For image-only datasets, the final output is boxes, classes, and confidence scores. For video deployments, the final output can include track IDs and smoothed detections. The video layer should be optional because it changes the evaluation problem from object detection to perception over time.
[Frame]
   |
   v
[Preprocess + resize]
   |
   v
[Fast YOLO26-style detector]
   |
   +--> [Direct boxes/classes]
   |
   v
[Uncertainty router]
   |               |             \ hard / small / dense / unstable
   | easy            v              v
[Return]      [Global-token context and/or crop-refine]
                    |
                    v
              [Merge refined boxes]
                    |
                    v
              [Optional tracker / temporal smoothing]
                    |
                    v
              [Final output]


7. YOLO26-Style Detector Interface
AegisDet-Pro should preserve a YOLO26-style detector interface because the detector head and export path matter as much as the backbone. The YOLO26 paper reports a dual-head design for native NMS-free end-to-end inference and a lighter DFL-free head [1]. The project should not throw away this deployment advantage by using a heavy or exotic decoder.
The practical design is to retain two output personalities. The first is an end-to-end one-to-one output for runtimes that support the needed operators. The second is a traditional one-to-many fallback path for runtimes that cannot efficiently support the end-to-end postprocess graph. This prevents the model from becoming locked to a single hardware target.
The head should remain lightweight. It should avoid large transformer decoders, complex dynamic kernels, and post-processing nodes that are known to fail on strict NPUs. Most of the research value should come from routing, global context, and crop refinement, not from redesigning the entire detection head from scratch.
The best baseline for this module is simply the exported YOLO26n detector under the same runtime. If YOLO26n is not usable in a specific package or device setup, the fallback baseline should be YOLO11n or YOLOv8n, but the document should clearly label that as a practical fallback rather than the strongest current baseline.


8. CNN-First Backbone Design
The backbone should be CNN-first. This does not mean old-fashioned or weak. RepViT shows that a pure lightweight CNN redesigned from a ViT perspective can reach strong accuracy and latency on mobile devices [6]. This supports using convolution as the default operator while borrowing design principles from modern transformer architectures.
AegisDet-Pro should begin with a YOLO26n-like or RepViT-inspired local backbone. The backbone should include efficient convolutional blocks, depthwise separable operations where appropriate, reparameterizable blocks if the framework supports them, and a clear multi-scale feature output. The core purpose is to produce P3, P4, and P5 features efficiently.
The global context block should not replace the whole backbone. Instead, it should be inserted once, after enough spatial downsampling has occurred. This keeps memory low and makes the attention block more hardware-friendly. If a separable attention block is used, it should follow MobileViTv2-style logic: low-resolution features, linear or separable operations, and no broad quadratic attention [4].
The first backbone milestone should be simple: reproduce YOLO26n baseline performance on the target dataset. Only then should the architecture be changed. If the baseline is not stable, adding new blocks will create confusion. The project should move from baseline to minimal modification to adaptive system, not from zero directly to v5.1.


9. Tiny Global-Token Context Block
The tiny global-token block is the cleanest way to add transformer-style reasoning without making the model transformer-heavy. Mobile-Former shows that a transformer branch can use very few learned tokens, such as six or fewer, to learn global priors and interact with MobileNet features through a two-way bridge [5]. This is directly relevant to AegisDet-Pro because object detection often benefits from scene context but cannot afford full high-resolution attention.
The default setting should be K = 6 learned global tokens. The tokens interact with P4 and/or P5 features through lightweight cross-attention. The feature map sends a compressed summary into the tokens; the tokens return global context to the feature map. This creates a global memory without converting every image patch into a full transformer sequence.
Three variants should be tested. GToken-S uses four tokens at P5 only. GToken-M uses six tokens with P4-to-token and token-to-P5 interaction. GToken-L uses eight tokens with both P4 and P5. The expected sweet spot is GToken-M because it balances context and cost. If token attention is too fragile to implement, the fallback is one MobileViTv2-style separable attention block at the deepest stage.
The global-token module should be judged by EdgeScore, not raw mAP. A one-point mAP gain is not worth it if latency doubles. Conversely, a small mAP gain on small objects may be valuable if latency increases only slightly and false positives drop.
Tiny global-token bridge

Input feature map: X in R^(H x W x C)
Learned global tokens: T in R^(K x C), where K = 4, 6, or 8

1. Compress local features into token updates:
   T' = CrossAttention(query=T, key=X, value=X)

2. Send global context back to feature map:
   X' = X + Gate(X) * CrossAttention(query=X_lowrank, key=T', value=T')

3. Continue detector neck/head:
   P4/P5_context = ConvNormAct(X')



10. Uncertainty Router
The router is the brain of AegisDet-Pro. Without the router, the system is just a hybrid detector. With the router, the model becomes adaptive. The router decides when the frame is easy enough for the fast path and when it deserves global reasoning, crop refinement, or temporal confirmation.
The router should not be based on a single confidence threshold. Confidence alone can be poorly calibrated. Instead, the router should combine several cheap signals: class entropy, margin between top classes, number of near-threshold boxes, small-object density, density of overlapping boxes, and track instability for video. These signals are cheap because they use outputs the detector already computes.
The first implementation can be rule-based. A learned router can come later. A rule-based router is easier to debug and gives a clear baseline. For example, activate crop refinement if there are at least two small near-threshold boxes or if the maximum class entropy exceeds a threshold. Once the rule-based version works, a small MLP router can be trained to approximate the hard-case decision.
The router objective includes a compute penalty. AegisDet-Pro should not always route to the expensive path. If it does, the router has failed. The training and evaluation should report activation rate: the percentage of frames that trigger extra compute. This lets you prove that the model uses selective compute instead of hiding a slow model behind averages.

Router score example

score = 0.30 * mean_class_entropy
      + 0.20 * near_threshold_count_norm
      + 0.25 * small_object_density
      + 0.15 * overlap_density
      + 0.10 * temporal_instability

if score < tau_fast:
    return fast_path_output
elif small_object_density is high:
    run selective crop_refine
else:
    activate global_context_refinement


11. Selective Crop-Refine Branch
Selective crop refinement is the most important small-object upgrade. Small objects are difficult because they occupy few pixels, disappear through downsampling, and are easy to confuse with background. SAHI shows that slicing can substantially improve small-object detection by running inference on overlapping image slices [10]. However, full slicing on every frame is too expensive for a real-time edge model.
AegisDet-Pro should use selective crop refinement instead. The fast detector runs first. The router identifies small, uncertain, dense, or near-threshold regions. Only those regions are cropped and reprocessed at higher local resolution. The refined boxes are then merged with the global detections.
This design preserves the benefit of slicing while avoiding its biggest weakness. If the frame is easy, no crop refinement runs. If the frame contains a possible small object, the model spends additional compute only in the relevant area. This is a strong edge-specific research contribution because it converts small-object inference into a conditional operation.
The branch should initially reuse the same detector weights or a tiny shared refinement head. Reusing the detector is simpler and reduces training complexity. Later, a specialized crop-refine head can be trained on difficult small-object crops. The worst-case latency must be bounded by limiting maximum crops per frame.


12. Temporal Stability Layer
If AegisDet-Pro is deployed on video, temporal stability can improve real-world reliability without changing the neural network much. Many false positives and false negatives are one-frame events. A detector might briefly see a shadow as an animal or miss a true object for one blurred frame. A temporal layer can reduce these errors.
The simplest temporal rule is confirmation over time: trigger an alert only if the object appears in three of the last five frames. This is useful for alerts, but it may delay response. A smoother version uses an exponential moving average over confidence scores and box coordinates. For applications where identity matters, ByteTrack is a strong default because it associates almost every detection box, including low-score boxes that may correspond to occluded objects [11].
Temporal logic should be optional. If the benchmark is image detection, it should be disabled. If the benchmark is video perception, it should be evaluated separately. This keeps the evaluation fair and prevents mixing detection accuracy with tracking stability.
For robotics, temporal smoothing can also connect perception to control. A robot should not react violently to one unstable detection. AegisDet-Pro can output a stable confidence signal rather than a noisy per-frame decision. That makes the model more useful for real systems such as autonomous robots, roadside alerts, or fire/smoke exploration platforms.


13. Mathematical Formulation
The mathematical objective should express the actual research idea: improve detection while controlling extra compute. The base detection loss follows the YOLO-style training objective. Additional terms handle distillation, routing, calibration, and compute cost.
Let f_base(x) be the fast detector output. Let r(x) be the router score. Let g(x) be the global-context feature update and c(x) be the crop-refine output. The final output is a conditional function. In easy cases, the model returns f_base(x). In hard cases, it returns a merged output from f_base, g, and/or c.
The key is that extra compute is penalized. If the router activates expensive modules too often, the model loses its edge advantage. This makes the optimization aligned with the deployment goal. The objective should not reward raw accuracy without cost.
For distillation, the student learns from stronger teachers. The teacher sequence can start with YOLO26s or YOLO26m, then optionally include a model with stronger global context such as RT-DETR or an attention-centric YOLO variant. The student should learn logits, boxes, and intermediate features, but the feature distillation should be focused on foreground or predictive regions rather than every background pixel.
Notation

x: input frame
B: ground-truth boxes and classes
f_base(x): fast YOLO26-style output
r(x): router score in [0, 1]
g(x): global-token context module
c(x): crop-refine module
M(.): merge operator for boxes

Conditional inference

if r(x) < tau:
    y_hat = f_base(x)
else:
    y_hat = M(f_base(x), g(x), c(x))

Training objective

L_total = L_det
        + lambda_kd  * L_distill
        + lambda_feat * L_feature
        + lambda_route * E[extra_compute]
        + lambda_calib * L_calibration

EdgeScore = mAP50-95 / (latency_ms * model_size_MB)


14. Dataset Strategy
The dataset determines whether AegisDet-Pro becomes impressive or generic. A model trained on a common benchmark only becomes another detector comparison. A model trained on a domain-specific edge task can produce a stronger story. The target domain should connect to robotics, sensing, low-power AI, or real-world deployment.
The best domains for this project are wildlife/road animal detection, fire/smoke robot perception, robotics field-object detection, and low-power roadside sensing. These domains share the same technical theme: real-world perception under edge constraints. They also produce hard cases such as small objects, occlusion, motion blur, low light, clutter, and false positives.
The dataset should be divided into seed training data, validation data, test data, and deployment-style unlabeled data. The deployment-style unlabeled data is important for active learning. It lets the model discover failure cases that are not represented in the clean labeled set.
A minimum serious dataset might contain 3,000-5,000 labeled images for early ablations. A stronger version should target 10,000-25,000 labeled images or a smaller number of images with high annotation quality and dense hard negatives. For a high-school/ASSIP-level project, quality and failure analysis matter more than enormous scale.


15. Hard-Negative Active Learning
Hard-negative active learning may improve AegisDet-Pro more than any architecture change. General detectors fail on domain-specific false positives because they were not trained on the exact background traps in that environment. A wildlife model may confuse rocks, bushes, shadows, trash bags, or fence posts with animals. A robotics model may confuse reflections, field elements, and same-color objects. The model needs to learn these failures directly.
The active learning loop is simple. Train a baseline. Run it on unlabeled real-world images or video. Score frames by uncertainty, small-object density, near-threshold detections, and false-positive likelihood. Select diverse hard examples. Label only those selected examples. Retrain or fine-tune. Repeat. This creates a dataset that is targeted at the model's weaknesses.
The active learning set should include both hard positives and hard negatives. Hard positives are real objects that the model misses or scores too low. Hard negatives are background regions the model falsely detects. Both are critical. If the dataset only adds positive examples, the model may improve recall but produce too many false alerts.
The final report should show examples of failure cases before and after active learning. This makes the project understandable to judges and reviewers. A visual failure gallery can be more convincing than a small mAP change alone.
Active learning loop

1. Train YOLO26n baseline and AegisDet-Pro initial model.
2. Run both models on unlabeled deployment frames.
3. Compute acquisition score:
      uncertainty + small-object density + false-positive likelihood + diversity.
4. Select top frames with temporal spacing to avoid duplicates.
5. Label selected frames.
6. Add to training data.
7. Retrain or fine-tune.
8. Repeat for 2-3 rounds.
9. Report before/after mAP, false positives, false negatives, and EdgeScore.



16. Training Recipe
The training recipe should be staged. Do not start with every advanced module enabled. The project should progress from baseline training to minimal architecture changes, then to adaptive modules, then to distillation and quantization. This reduces debugging complexity and creates clean ablation results.
The base training recipe should use strong but standard object detection augmentations: mosaic, mixup if appropriate, HSV/color jitter, random crop, random scale, blur, brightness variation, and domain-specific augmentations such as night or smoke simulation if relevant. However, augmentations should not distort the domain beyond realism. For example, wildlife images should not be transformed so heavily that shadows and animals become unrealistic.
YOLO26-style training ideas should be adopted conceptually: Progressive Loss for a dual-head detector, STAL-style emphasis for small objects, and MuSGD for longer training runs. If implementation becomes difficult, the project can begin with SGD or AdamW and later compare MuSGD. The training plan should document every compromise.
A final training run should include the best architecture, hard-negative data, distillation, and quantization fine-tuning if needed. Smaller ablations can be trained for fewer epochs. Only the final models need full-length training. This keeps the project feasible.


17. Progressive Multi-Teacher Distillation
Progressive multi-teacher distillation is one of the strongest training upgrades. Lightweight detectors often struggle to match larger models because the student has less capacity. Distillation transfers the teacher's behavior into the student. Multi-teacher progressive distillation is especially relevant because the student can learn from a sequence of teachers rather than being forced to imitate a very large teacher immediately [12].
The teacher sequence should start with a model close to the student, such as YOLO26s or YOLO26m. This teaches detection geometry and head behavior. The next teacher can be a larger model or a model with stronger global context. The final teacher can be the strongest task-specific model trained on the dataset. The final model remains small; only training uses the larger teachers.
The distillation loss should include class logits, box regression, and selected feature maps. Feature distillation should focus on foreground and hard regions. Distilling every background feature may waste capacity and make the student less focused. If the target domain has many small objects, relation-based or foreground-focused feature distillation is especially valuable.
The distillation stage should also include hard examples from the active learning loop. The teacher should guide the student on cases that the baseline struggles with: tiny objects, occlusion, low light, and clutter. This aligns distillation with the purpose of AegisDet-Pro rather than simply copying teacher outputs everywhere.

Distillation loss

L_distill = lambda_cls * KL(student_logits, teacher_logits / T)
           + lambda_box * GIoU(student_boxes, teacher_boxes)
           + lambda_feat * ForegroundFeatureKD(student_features, teacher_features)
           + lambda_rel * RelationKD(student_relations, teacher_relations)

Use higher KD weight on:
- small objects
- occluded targets
- low-light images
- false-positive-prone backgrounds
- active-learning hard cases


18. Quantization and Export Strategy
A low-power detector is not real until it exports and runs efficiently. AegisDet-Pro should support at least one desktop/server backend and one true edge backend. The export strategy should be built into the design, not added at the end.
The first export target should be ONNX because it is a common interchange format. After that, test TensorRT if an NVIDIA GPU or Jetson device is available. OpenVINO is useful for CPU and Intel hardware. TFLite or CoreML is useful for mobile. Edge TPU or similar strict NPUs require full integer quantization and may not support every post-processing operator.
Quantization should start with post-training quantization because it is faster. If accuracy drops too much, use quantization-aware training. QAT is especially important for strict INT8 deployments. The global-token block and router should use hardware-friendly operators: convolutions, additions, simple reductions, linear layers, and low-resolution attention.
The project should preserve two export personalities: an end-to-end output where the runtime supports it and a fallback output for runtimes that cannot support certain operations. This is a practical deployment detail that makes the project more credible.


19. Hardware Benchmarking Plan
Benchmarking must be fair. AegisDet-Pro should be compared against YOLO26n exported through the same backend, with the same image size, same validation split, same confidence settings, and same device. Paper mAP numbers are not enough because runtime performance changes across hardware and export formats.
The primary device should be whichever device is actually available. If using a laptop GPU, report it honestly as a development benchmark. If using a Jetson, Raspberry Pi, Coral, or mobile phone, report true edge results. The strongest project will include at least one development GPU benchmark and one edge hardware benchmark.
Latency should include warm-up. Report p50, p90, and p99 latency, not only average FPS. Average FPS can hide long-tail delays caused by crop refinement. Since AegisDet-Pro uses conditional modules, p90 latency is especially important. A model with good average latency but unacceptable worst-case latency may not be deployable.
Power measurement is ideal but not always easy. If available, use device tools such as tegrastats on Jetson or external power measurement for Raspberry Pi. If precise power is unavailable, report latency, model size, and memory honestly and leave power as future work. Do not fake power measurements.


20. Ablation Matrix
The ablation matrix is the backbone of the research report. It proves which parts of AegisDet-Pro matter. Without ablations, the project becomes a black box. With ablations, even partial success becomes valuable because the results explain what worked and what failed.
Each ablation should change one variable at a time. For example, do not add global tokens, crop refinement, and distillation in the same experiment and then claim the whole system works. First test global tokens alone. Then routing. Then crop refinement. Then distillation. Then quantization. The final model can combine the winning choices.
The most important ablation is YOLO26n versus AegisDet-Pro under equal backend conditions. The second most important is crop refinement on/off because this is likely the largest small-object improvement. The third most important is routing on/off because the project depends on selective compute.
The report should include both numeric tables and qualitative failure examples. Numeric metrics show performance; failure examples show why the model is useful. A good project includes images where YOLO26n fails and AegisDet-Pro succeeds, plus images where AegisDet-Pro fails and why.


21. Implementation Roadmap
The implementation roadmap should minimize risk. Start with the simplest model that can run. Do not build the entire architecture at once. A working baseline is more valuable than a complex broken system.
Milestone 1 is dataset and baseline. Choose the domain, prepare labels, train or fine-tune YOLO26n, and export it. Record accuracy and latency. Milestone 2 is a CNN-only AegisDet control. Milestone 3 adds the smallest global-context block. Milestone 4 adds the router. Milestone 5 adds crop refinement. Milestone 6 adds hard-negative active learning. Milestone 7 adds distillation. Milestone 8 adds INT8 export and hardware benchmarking.
At every milestone, save logs, configuration files, model checkpoints, and failure images. This matters because the final writeup depends on reproducibility. A good research project is not just code that works once; it is a documented chain of experiments.
The implementation should use the Ultralytics ecosystem where possible. Custom modules should be small and isolated. Avoid rewriting the training framework from scratch. The goal is research and benchmarking, not building an entire detection library.


22. Timeline
A realistic timeline should be built around milestones, not arbitrary dates. The project can be compressed or expanded depending on the summer schedule, but the sequence should not change. Baseline first, then minimal architecture, then adaptive modules, then training improvements, then deployment.
The first two weeks should produce a working baseline and dataset pipeline. If this does not happen, the project is at risk. Weeks three and four should create the first AegisDet variants and global-token ablations. Weeks five and six should focus on routing and crop refinement. Weeks seven and eight should focus on hard-negative active learning and distillation. Weeks nine and ten should focus on export, quantization, and benchmarking. The final weeks should focus on analysis, writing, and demo preparation.
If the project has less time, cut the hardest optional modules first. Do not cut baseline benchmarking or failure analysis. The minimum strong version is YOLO26n baseline, AegisDet with one global-token block, crop-refine routing, and one edge benchmark. The full version adds distillation, active learning rounds, QAT, and temporal tracking.
A schedule should also include buffer time. Object detection projects often fail because of dataset issues, annotation errors, training bugs, or export incompatibilities. A project plan that has no buffer is not realistic.


23. Risk Register
The project is ambitious, so risk management matters. The highest risks are implementation complexity, weak dataset quality, unfair baselines, and export failure. Each risk needs a fallback plan.
If YOLO26n cannot be installed or exported reliably, use YOLO11n or YOLOv8n as a fallback while clearly noting the limitation. If the global-token block is difficult to train, use a MobileViTv2-style separable attention block as the first context variant. If crop refinement is too slow, reduce max crops per frame or use it only as an offline hard-case analysis. If quantization causes large accuracy loss, use FP16 as the deployable baseline and treat QAT as a stretch goal.
The biggest conceptual risk is overclaiming. AegisDet-Pro should not claim universal SOTA. It should claim a specific Pareto improvement on a specific dataset and hardware setup. This is more honest and more defensible.
The second biggest risk is spending too much time on architecture before validating data. A poor dataset will ruin the project. The fastest path to improvement is often better hard negatives, cleaner labels, and stronger evaluation splits.


24. Success Criteria
Success should be defined before experiments begin. Otherwise, it becomes too easy to reinterpret results after the fact. The project should have minimum, strong, and stretch success levels.
Minimum success means building a working detector pipeline, training a baseline, implementing one meaningful architecture change, and producing honest benchmarks. Strong success means beating YOLO26n on EdgeScore or small-object AP under equal runtime conditions. Stretch success means showing the improvement on two device classes or after INT8 quantization.
The most credible win is not necessarily highest raw mAP. AegisDet-Pro can win by keeping similar mAP while reducing average latency, improving small-object AP with bounded p90 latency, or reducing false positives on hard negatives. The exact success metric should match the target domain.
The final report should include a clear statement of what was proven and what was not proven. If AegisDet-Pro does not beat YOLO26n overall but improves small-object AP or failure-case precision, that is still valuable. Negative results are useful if the ablation study explains them.


25. ASSIP / MIT Narrative Fit
AegisDet-Pro fits a coherent personal theme: efficient intelligent systems that sense the real world and make decisions on low-power hardware. This connects robotics, edge AI, sensing, and practical deployment. It is stronger than a random AI app because it has a research question, a measurable hypothesis, and hardware constraints.
For ASSIP, the project connects to low-power AI, NPUs, efficient inference, sensing signals, and embedded deployment. Even if the ASSIP research topic is not exactly object detection, the core ideas overlap: accuracy-per-watt, model compression, quantization, hardware-aware design, and robust sensing under constraints.
For an MIT-style profile, the project is strongest if it includes real implementation and honest experiments. MIT does not need another claim that a student “used AI.” AegisDet-Pro is stronger because it asks a technical question and measures the result. It connects to VEX autonomous robotics, prior RoadGuard-style ideas, and a long-term theme of building real systems.
The narrative should not be that the model beats all detectors. The narrative should be that the project taught how to convert AI research into a deployable perception system. That is a more mature and credible story.


26. Codebase Structure
The codebase should be organized like a research project, not a pile of scripts. Clean structure makes debugging easier and makes the final repository more credible. Each experiment should be reproducible from a config file.
The repository should separate dataset utilities, model modules, training scripts, evaluation scripts, export scripts, and reports. Custom modules should be isolated so that the baseline remains unchanged. Logs should be saved automatically.
A simple experiment registry is enough. Every run should have a name, dataset version, model config, training config, checkpoint path, validation result, export result, and notes. This prevents confusion when many ablations are trained.
The final repository should include a README that explains the research question, not just installation. It should also include model cards for the final models and a limitations section that honestly describes what the model was and was not tested on.
aegisdet-pro/
  README.md
  configs/
    dataset.yaml
    train_yolo26n_baseline.yaml
    aegisdet_global_tokens_k4.yaml
    aegisdet_global_tokens_k6.yaml
    aegisdet_router_crop.yaml
    aegisdet_int8_export.yaml
  datasets/
    README.md
    splits/
    label_checks/
  models/
    modules/
      global_tokens.py
      uncertainty_router.py
      crop_refine.py
      temporal_smoothing.py
    aegisdet.py
  train/
    train_baseline.py
    train_aegisdet.py
    distill.py
  eval/
    evaluate_map.py
    benchmark_latency.py
    benchmark_power.py
    failure_gallery.py
  export/
    export_onnx.py
    export_tensorrt.py
    export_openvino.py
    export_tflite.py
  reports/
    experiment_log.csv
    ablation_tables/
    figures/
  notebooks/
    error_analysis.ipynb


27. Pseudocode Appendix
This appendix gives implementation-level pseudocode. It is not final code, but it defines the intended behavior of the main modules. The goal is to make the architecture concrete enough to implement.
The most important pseudocode is the inference loop. It starts with a fast detector pass, calculates router signals, decides whether to trigger crop refinement, merges boxes, and optionally applies temporal smoothing. This structure is easier to implement than routing inside every network block.
Training pseudocode should include baseline training, architecture ablation, active learning, distillation, and export. Each stage should produce logged metrics and failure examples. The project should never rely on memory or screenshots for experiment tracking.
The pseudocode should be converted into real scripts gradually. First build the simple baseline scripts, then add the optional modules.
def infer_aegisdet(frame, state=None):
    x = preprocess(frame)
    base_pred, features = fast_detector(x, return_features=True)

    router_features = summarize(
        class_entropy=entropy(base_pred.scores),
        margin=top1_top2_margin(base_pred),
        near_threshold=count_near_threshold(base_pred),
        small_density=count_small_boxes(base_pred),
        overlap_density=count_overlaps(base_pred),
        temporal_instability=state.instability if state else 0.0,
    )
    score = router(router_features)

    outputs = [base_pred]
    if score > TAU_GLOBAL:
        outputs.append(global_context_refine(features, base_pred))

    if should_crop_refine(base_pred, score):
        crops = select_crops(frame, base_pred, max_crops=MAX_CROPS)
        for crop in crops:
            crop_pred = crop_detector(preprocess(crop))
            outputs.append(project_to_frame(crop_pred, crop))

    merged = merge_predictions(outputs)
    if state is not None:
        merged = temporal_smoother.update(merged, state)
    return merged


def train_pipeline():
    train_yolo26n_baseline()
    train_aegisdet_cnn_only()
    train_aegisdet_global_tokens()
    train_router_with_compute_penalty()
    train_or_enable_crop_refine()
    run_active_learning_rounds()
    run_progressive_distillation()
    export_and_benchmark()


28. Experiment Log Template
Every experiment should be logged in a consistent format. This prevents the project from becoming confusing once multiple variants exist. The log should record dataset version, model config, training settings, metrics, export status, and notes about failures.
The experiment log is also useful for the final writeup. Instead of trying to reconstruct what happened later, the results are already organized. Judges, mentors, and readers can see that the project was conducted systematically.
A good experiment log includes qualitative notes. For example, if a model improves mAP but produces more false positives at night, that matters. If crop refinement improves small objects but increases p90 latency too much, that matters. The project should not hide tradeoffs.
The final report can include a shortened version of this table. The full CSV or spreadsheet can be kept in the repository.


29. Final Deliverables
The final project should produce more than a trained model. It should produce a research package: code, trained checkpoints, benchmarks, ablation tables, failure galleries, a written report, and a short demo video.
The demo video should show the system running, not just slides. It should compare YOLO26n and AegisDet-Pro on a few hard examples. It should show when the router activates crop refinement. It should also show at least one case where AegisDet-Pro fails, because that makes the presentation more honest and mature.
The written report should explain the problem, literature context, architecture, dataset, experiments, results, limitations, and next steps. The poster should be simplified: problem, idea, diagram, key results, and why it matters. The repository should contain enough information for someone else to understand the experiment.
The strongest final story is not “I built a perfect model.” It is “I designed and tested an adaptive edge detector and measured where selective compute helps under real deployment constraints.”


30. References
These references support the design choices in this plan. The citations are intentionally focused on current object detection, mobile hybrid vision models, dynamic inference, small-object refinement, tracking, and distillation. The final research report should cite the exact papers and official documentation used in implementation.
[1] Jocher et al., "Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models," arXiv, 2026. https://arxiv.org/abs/2606.03748
[2] Chakrabarty, "YOLO26: An Analysis of NMS-Free End to End Framework for Real-Time Object Detection," arXiv, 2026. https://arxiv.org/abs/2601.12882
[3] Oguine et al., "Multiscale Real-Time Object Detection in the NMS-Free Era: YOLOv8 and YOLO26," arXiv, 2026. https://arxiv.org/abs/2605.24831
[4] Mehta and Rastegari, "Separable Self-attention for Mobile Vision Transformers," arXiv, 2022. https://arxiv.org/abs/2206.02680
[5] Chen et al., "Mobile-Former: Bridging MobileNet and Transformer," arXiv, 2021. https://arxiv.org/abs/2108.05895
[6] Wang et al., "RepViT: Revisiting Mobile CNN From ViT Perspective," arXiv, 2023. https://arxiv.org/abs/2307.09283
[7] Cai et al., "EfficientViT: Multi-Scale Linear Attention for High-Resolution Dense Prediction," arXiv, 2022. https://arxiv.org/abs/2205.14756
[8] Lin et al., "DynamicDet: A Unified Dynamic Architecture for Object Detection," arXiv, 2023. https://arxiv.org/abs/2304.05552
[9] Rao et al., "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification," arXiv, 2021. https://arxiv.org/abs/2106.02034
[10] Akyon et al., "Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection," arXiv, 2022. https://arxiv.org/abs/2202.06934
[11] Zhang et al., "ByteTrack: Multi-Object Tracking by Associating Every Detection Box," arXiv, 2021. https://arxiv.org/abs/2110.06864
[12] Cao et al., "Learning Lightweight Object Detectors via Multi-Teacher Progressive Distillation," arXiv, 2023. https://arxiv.org/abs/2308.09105
[13] Sapkota et al., "YOLO26: Key Architectural Enhancements and Performance Benchmarking for Real-Time Object Detection," arXiv, 2025. https://arxiv.org/abs/2509.25164
[14] Hidayatullah and Tubagus, "YOLO26: A Comprehensive Architecture Overview and Key Improvements," arXiv, 2026. https://arxiv.org/abs/2602.14582
[15] Shaker et al., "SwiftFormer: Efficient Additive Attention for Transformer-based Real-time Mobile Vision Applications," arXiv, 2023. https://arxiv.org/abs/2303.15446

Appendix A. Detailed Component Checklist
This checklist should be used before claiming that a component is complete. A component is not complete when code runs once. It is complete when it has an ablation, logs, failure examples, and export status if relevant.
For the global-token block, completion requires a comparison against the CNN-only student, at least two token counts, latency measurement, and one visualization or qualitative analysis showing which cases improved. For the router, completion requires activation-rate reporting and p90 latency. For crop refinement, completion requires small-object AP and a latency breakdown. For distillation, completion requires a teacher-student comparison and a no-distillation control. For quantization, completion requires FP32/FP16/INT8 comparison.
The checklist also prevents accidental overclaiming. If a module was not ablated, it should be described as part of the implementation, not as a proven contribution.


Appendix B. Example Result Tables to Fill Later
The following tables are templates for the final results. They should not be filled with guesses. They are included now so the project knows exactly what must be measured.


Appendix C. Final Research Abstract Draft
AegisDet-Pro v5.1 is an adaptive edge object detector designed to improve accuracy-per-compute on domain-specific low-power vision tasks. Instead of replacing efficient convolutional detectors with a transformer-heavy architecture, AegisDet-Pro preserves a YOLO26-style detection interface and adds selective global reasoning only when uncertainty indicates that the frame is difficult. The system combines a CNN-first backbone, a tiny learned global-token context block, an uncertainty router, selective crop refinement for small objects, progressive multi-teacher distillation, active hard-negative learning, and INT8 deployment. The model is evaluated against YOLO26n under equal dataset, image-size, runtime, and hardware conditions. The primary metric is EdgeScore, defined as mAP50-95 divided by latency and model size, with additional reporting of small-object AP, p90 latency, activation rate, memory footprint, and quantization loss. The goal is not universal object-detection state of the art, but a measurable Pareto improvement for practical edge perception.

Appendix D. What This Project Must Not Claim
AegisDet-Pro should not claim to invent CNN-transformer hybrids. That area already exists. It should not claim to beat all YOLO models unless experiments prove it. It should not claim production readiness without real export and hardware tests. It should not claim low power without either measuring power or clearly limiting the claim to latency and model size.
The correct claim is narrower and stronger: AegisDet-Pro is an adaptive edge detector that attempts to improve the accuracy-latency tradeoff by selectively activating global context and crop refinement on hard frames. If the experiments show a higher EdgeScore than YOLO26n on a specific domain and hardware backend, that is enough. A carefully proven narrow claim is more impressive than an exaggerated broad claim.