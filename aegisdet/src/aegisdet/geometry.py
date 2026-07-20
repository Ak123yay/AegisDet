from __future__ import annotations

from .types import Box

def box_area(box: Box) -> float:
    x1, y1, x2, y2 = box
    return max(0.0, x2 - x1) * max(0.0, y2 - y1)

def area_ratio(box: Box, image_width: int, image_height: int) -> float:
    if image_width <= 0 or image_height <= 0:
        raise ValueError("image dimensions must be positive")
    return box_area(box) / float(image_width * image_height)

def intersection_over_union(a: Box, b: Box) -> float:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0.0, ix2 - ix1) * max(0.0, iy2 - iy1)
    union = box_area(a) + box_area(b) - inter
    return inter / union if union > 0.0 else 0.0

def clamp_box(box: Box, image_width: int, image_height: int) -> Box:
    x1, y1, x2, y2 = box
    x1 = min(max(x1, 0.0), float(image_width))
    y1 = min(max(y1, 0.0), float(image_height))
    x2 = min(max(x2, 0.0), float(image_width))
    y2 = min(max(y2, 0.0), float(image_height))
    return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

def pad_box(box: Box, padding_fraction: float, image_width: int, image_height: int) -> Box:
    if padding_fraction < 0.0:
        raise ValueError("padding_fraction must be non-negative")
    x1, y1, x2, y2 = box
    px, py = (x2 - x1) * padding_fraction, (y2 - y1) * padding_fraction
    return clamp_box((x1 - px, y1 - py, x2 + px, y2 + py), image_width, image_height)

def remap_box(box: Box, origin_x: float, origin_y: float) -> Box:
    x1, y1, x2, y2 = box
    return (x1 + origin_x, y1 + origin_y, x2 + origin_x, y2 + origin_y)
