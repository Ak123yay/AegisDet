# AegisDet-Mini Pseudocode

```python
base = detector(image)
route = router(base, image)
if route == "fast":
    return base
crops = crop_planner(image, base, max_crops=2)
local = [remap(detector(c.image), c.origin) for c in crops]
return merge(base, local)
```
