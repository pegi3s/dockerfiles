"""Draws clustering results back onto the original images: every object (or
cell) is outlined in the colour of its cluster, with a legend bar on top."""
from __future__ import annotations

from typing import Dict, List, Optional

import cv2
import numpy as np

# High-contrast categorical colours (RGB) that stay visible on light
# brightfield backgrounds and on blue/purple stains. Blue hues are avoided
# on purpose because most cell stains are blue/purple.
PALETTE = [
    (230, 25, 75),    # red
    (60, 180, 75),    # green
    (255, 140, 0),    # orange
    (240, 50, 230),   # magenta
    (0, 0, 0),        # black
    (255, 225, 25),   # yellow
    (128, 0, 0),      # maroon
    (0, 128, 128),    # teal
    (170, 110, 40),   # brown
    (145, 30, 180),   # purple
]


def cluster_color(label: int) -> tuple:
    return PALETTE[label % len(PALETTE)]


EXCLUDED_COLOR = (150, 150, 150)


def annotate_image(rgb: np.ndarray, contours_by_cluster: Dict[int, List[np.ndarray]], k: int,
                   title: str = "", excluded_contours: Optional[List[np.ndarray]] = None,
                   excluded_label: str = "excluded",
                   markers: Optional[List[tuple]] = None, marker_label: str = "") -> np.ndarray:
    """Returns a copy of ``rgb`` with each cluster's object contours drawn in
    that cluster's colour, plus a legend bar listing all ``k`` clusters and
    how many of this image's objects fall in each. ``excluded_contours`` (if
    given) are drawn thin and grey. ``markers`` is a list of (x, y, text):
    each is drawn as a white disc with a black ring and the text inside
    (used for the ranks of the most unusual cells)."""
    vis = rgb.copy()
    thickness = max(2, int(round(min(rgb.shape[:2]) / 220)))
    if excluded_contours:
        cv2.drawContours(vis, excluded_contours, -1, EXCLUDED_COLOR, 1, lineType=cv2.LINE_AA)
    for label, contours in contours_by_cluster.items():
        cv2.drawContours(vis, contours, -1, cluster_color(label), thickness, lineType=cv2.LINE_AA)
    radius = max(9, int(round(min(rgb.shape[:2]) / 45)))
    for x, y, text in markers or []:
        center = (int(x), int(y))
        cv2.circle(vis, center, radius, (255, 255, 255), -1, lineType=cv2.LINE_AA)
        cv2.circle(vis, center, radius, (0, 0, 0), 2, lineType=cv2.LINE_AA)
        (tw, th), _ = cv2.getTextSize(str(text), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.putText(vis, str(text), (center[0] - tw // 2, center[1] + th // 2), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Legend bar (wraps onto several lines if needed).
    font, scale, text_th = cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
    line_h, sw, pad = 24, 14, 8
    items = [(f"Cluster {c}: {len(contours_by_cluster.get(c, []))} obj", cluster_color(c)) for c in range(k)]
    if excluded_contours:
        items.append((f"{excluded_label}: {len(excluded_contours)}", EXCLUDED_COLOR))
    if markers and marker_label:
        items.append((marker_label, None))
    if title:
        items.insert(0, (title, None))
    lines, cur, cur_w = [], [], pad
    for text, color in items:
        tw = cv2.getTextSize(text, font, scale, text_th)[0][0] + (sw + 6 if color else 0) + 16
        if cur and cur_w + tw > vis.shape[1]:
            lines.append(cur)
            cur, cur_w = [], pad
        cur.append((text, color, cur_w))
        cur_w += tw
    lines.append(cur)

    bar = np.full((line_h * len(lines) + 4, vis.shape[1], 3), 255, np.uint8)
    for li, line in enumerate(lines):
        y = li * line_h + 17
        for text, color, x in line:
            if color is not None:
                cv2.rectangle(bar, (x, y - sw + 2), (x + sw, y + 2), color, -1)
                x += sw + 6
            cv2.putText(bar, text, (x, y), font, scale, (0, 0, 0), text_th, cv2.LINE_AA)
    return np.vstack([bar, vis])
