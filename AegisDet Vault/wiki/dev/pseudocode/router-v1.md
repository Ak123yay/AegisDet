# Router V1 Pseudocode

```python
if small_count >= 1: return True, "small"
if uncertain_count >= 2: return True, "uncertain"
if overlap_count >= 2: return True, "overlap"
return False, "fast"
```
