---
title: "Easy Frame User Story"
project: "AegisDet-Pro v5.1"
area: "product"
status: "reference"
tags: ["product"]
---

# Easy Frame User Story

Given a clear, large deer detection with high confidence and no ambiguous overlaps, the router selects the fast route. The system makes one detector call, returns the frozen baseline detections, records `reason=fast`, and avoids crop overhead. This path should dominate average operation if the router is calibrated correctly.

## Related notes
- [[DOMAIN_LOCK]]
- [[AegisDet_Design/claims-and-non-claims]]
