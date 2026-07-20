from __future__ import annotations

def edge_score(map_50_95: float, latency_ms: float, model_size_mb: float) -> float:
    if not 0.0 <= map_50_95 <= 1.0:
        raise ValueError("map_50_95 must be expressed as a fraction in [0, 1]")
    if latency_ms <= 0.0 or model_size_mb <= 0.0:
        raise ValueError("latency and model size must be positive")
    return map_50_95 / (latency_ms * model_size_mb)

def percentile(values: list[float], percent: float) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    if not 0.0 <= percent <= 100.0:
        raise ValueError("percent must be in [0, 100]")
    ordered = sorted(values)
    index = round((len(ordered) - 1) * percent / 100.0)
    return ordered[index]
