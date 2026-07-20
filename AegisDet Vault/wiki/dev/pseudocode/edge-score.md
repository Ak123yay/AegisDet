# EdgeScore Pseudocode

```python
def edge_score(map_50_95_fraction: float, latency_ms: float, model_size_mb: float) -> float:
    if latency_ms <= 0 or model_size_mb <= 0:
        raise ValueError("latency and size must be positive")
    return map_50_95_fraction / (latency_ms * model_size_mb)
```

## Use rule

EdgeScore is a project comparison heuristic, not a universal standard. Calculate it only when models use the same dataset split, evaluator, hardware, runtime, precision, batch size, preprocessing, postprocessing, and input size. Always report its component metrics beside the combined value so a strong score cannot hide an unacceptable accuracy or tail-latency result.
