# Source Inventory

## Primary implementation and baseline sources

| Source | Type | Project use |
|---|---|---|
| https://docs.ultralytics.com/models/yolo26/ | Official documentation | YOLO26 architecture, model names, modes, export, dual-head behavior |
| https://arxiv.org/abs/2606.03748 | Preprint | YOLO26 method and reported benchmark context |
| https://github.com/ultralytics/ultralytics | Official repository | Implementation and licensing |
| https://github.com/opencv/opencv/wiki/OpenCV-5 | Official project wiki | OpenCV 5 DNN engine selection and current CPU/GPU constraints |

## Architecture and efficiency literature

| Paper | URL | AegisDet lesson |
|---|---|---|
| Mobile-Former | https://arxiv.org/abs/2108.05895 | Very few learned tokens can carry global priors |
| MobileViTv2 | https://arxiv.org/abs/2206.02680 | Efficient separable global interaction |
| RepViT | https://arxiv.org/abs/2307.09283 | Modern mobile design can remain pure CNN |
| EfficientViT | https://arxiv.org/abs/2205.14756 | Hardware-aware multi-scale linear attention for dense prediction |
| DynamicViT | https://arxiv.org/abs/2106.02034 | Input-dependent compute allocation |
| DynamicDet | https://arxiv.org/abs/2304.05552 | Dynamic routes for object detection |
| SAHI | https://arxiv.org/abs/2202.06934 | Slicing improves small-object detection but adds compute |
| ByteTrack | https://arxiv.org/abs/2110.06864 | Lightweight video association using low-score detections |
| Multi-Teacher Progressive Distillation | https://proceedings.mlr.press/v202/cao23c.html | Sequential teachers can improve lightweight detectors |

## Source policy

Prefer official docs, original papers, and official repositories. Record what the source actually establishes separately from what AegisDet hypothesizes.
