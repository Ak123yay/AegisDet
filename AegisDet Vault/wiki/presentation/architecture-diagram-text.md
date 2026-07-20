---
title: "Architecture Diagram Text"
project: "AegisDet-Pro v5.1"
area: "presentation"
status: "reference"
tags: ["presentation"]
---

# Architecture Diagram Text

`416×416 frame → YOLO26n-derived CNN fast path → detections → router`. Easy frames return immediately. Hard frames select no more than two padded small/uncertain regions, rerun the detector, remap local boxes, and merge them with the base output. In Phase 4 only, a K-token context block is inserted at P4 or P5 and evaluated independently. Output includes boxes, classes, confidence, route reason, crop count, and timing metadata.

## Related notes
- [[AegisDet_Design/architecture-diagram]]
- [[PROJECT_CONTEXT]]
