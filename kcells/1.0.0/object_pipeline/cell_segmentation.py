"""Cell segmentation with Cellpose, then per-cell stained content.

1. **Cell outlines**: the Cellpose deep-learning model (generalist ``cyto3``
   model, grayscale input, CPU) outlines every cell. The typical cell
   diameter is estimated from the image unless given.
2. **Stain density**: the image is converted to optical density
   (Beer-Lambert, ``OD = -log(I / I0)``, ``I0`` = the image's bright level),
   i.e. the amount of stain per pixel.
3. **Stained content per cell**: inside every cell, the stained part
   (nucleus, or the chromosomes of a dividing cell) is separated from the
   cytoplasm with Otsu's threshold on that cell's own OD values. A cell is
   *nucleated* only if its stained part is clearly denser than the image's
   typical cytoplasm and at least 15% of the image's median nucleus size
   (smaller stained bits are wall fragments or slivers of a neighbour's
   nucleus).
4. **Condensed chromatin**: inside each stained part, a second, stricter
   Otsu threshold keeps only the densest chromatin (e.g. the individual
   chromosomes of a dividing cell, without the haze between them).

All lengths scale with the shorter image side.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage as ndi


@dataclass
class Cell:
    cell_id: int
    mask: np.ndarray            # uint8 0/255, full image size: the whole cell
    nucleus_mask: np.ndarray    # uint8 0/255: stained content of this cell
    chromatin_mask: np.ndarray  # uint8 0/255: condensed chromatin inside the stained content
    bbox: tuple                 # (x, y, w, h) of the cell
    area: int
    nucleus_area: int
    n_fragments: int            # connected stained pieces inside the cell
    has_nucleus: bool           # False if the cell has no clearly stained content
    touches_border: bool
    centroid: tuple             # (x, y)
    cell_likeness: float = 1.0  # solidity-based shape score (1 = convex, ellipse/rectangle-like)


def optical_density(rgb: np.ndarray) -> np.ndarray:
    """Per-pixel stain amount (sum of OD over the RGB channels)."""
    rgb_f = rgb.astype(np.float32) + 1.0
    i0 = np.percentile(rgb_f.reshape(-1, 3), 99, axis=0)
    return (-np.log(np.clip(rgb_f / i0, 1e-3, 1.0))).sum(axis=2)


def _ellipse(size: float) -> np.ndarray:
    size = max(3, int(size) | 1)
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))


def cell_likeness(area: float, hull_points: np.ndarray, max_aspect: float = 4.0) -> float:
    """How much a region looks like a plant cell (ellipse- or rectangle-like):
    its solidity (area / convex-hull area; 1 for any convex shape such as an
    ellipse or a rectangle, lower for notched, branched or ring-shaped
    regions), reduced for shapes more elongated than ``max_aspect``:1."""
    hull = cv2.convexHull(hull_points.astype(np.int32))
    hull_area = max(cv2.contourArea(hull), 1.0)
    solidity = min(1.0, area / hull_area)
    if len(hull) >= 3:
        (_, _), (rw, rh), _ = cv2.minAreaRect(hull)
        aspect = max(rw, rh) / max(min(rw, rh), 1.0)
        if aspect > max_aspect:
            solidity *= max_aspect / aspect
    return solidity


def _mask_likeness(mask: np.ndarray) -> float:
    ys, xs = np.nonzero(mask)
    if len(xs) < 3:
        return 0.0
    return cell_likeness(float(len(xs)), np.column_stack([xs, ys]))


# --------------------------------------------------------------------------
# Stained content
# --------------------------------------------------------------------------

def _otsu_inside(values: np.ndarray) -> float:
    from skimage.filters import threshold_otsu
    return float(threshold_otsu(values)) if values.size >= 10 and np.ptp(values) > 1e-6 else np.inf


def _fill_small_holes(mask: np.ndarray, min_area: int) -> np.ndarray:
    """Fill holes (4-connected background regions) smaller than ``min_area``
    pixels. Same as skimage's ``remove_small_holes(mask, area_threshold=...)``,
    whose parameters differ between scikit-image versions."""
    holes, _ = ndi.label(~mask)
    sizes = np.bincount(holes.ravel())
    small = sizes < min_area
    small[0] = False
    return mask | small[holes]


def _stained_content(od: np.ndarray, cell: np.ndarray, min_fragment_area: int, open_kernel: np.ndarray):
    """Stained part of one cell (Otsu on the cell's own OD values)."""
    t = _otsu_inside(od[cell])
    stained = (od > t) & cell
    stained = cv2.morphologyEx(stained.astype(np.uint8), cv2.MORPH_OPEN, open_kernel) > 0
    lab, n = ndi.label(stained)
    if n:
        sizes = ndi.sum(stained, lab, index=np.arange(1, n + 1))
        stained = np.isin(lab, 1 + np.flatnonzero(np.asarray(sizes) >= min_fragment_area))
    stained = _fill_small_holes(stained, max(1, int(cell.sum() * 0.05)))
    return stained, float(od[stained].mean()) if stained.any() else 0.0


def _condensed_chromatin(od_fine: np.ndarray, stained: np.ndarray, min_piece_area: int) -> np.ndarray:
    """Densest chromatin inside a stained part (second Otsu threshold)."""
    if not stained.any():
        return stained
    cond = (od_fine > _otsu_inside(od_fine[stained])) & stained
    lab, n = ndi.label(cond)
    if n:
        sizes = ndi.sum(cond, lab, index=np.arange(1, n + 1))
        cond = np.isin(lab, 1 + np.flatnonzero(np.asarray(sizes) >= min_piece_area))
    return cond


class _Params:
    def __init__(self, h: int, w: int):
        side = min(h, w)
        self.scale = side / 500.0
        self.open_kernel = _ellipse(0.008 * side)
        self.smooth_kernel = _ellipse(0.012 * side)
        self.min_fragment = max(4, int(0.0003 * h * w))
        self.min_chromatin_piece = max(4, int((0.006 * side) ** 2))

# --------------------------------------------------------------------------
# Main entry point
# --------------------------------------------------------------------------

_CELLPOSE_MODEL = None


def _cellpose_labels(rgb: np.ndarray, diameter=None) -> np.ndarray:
    """Cell label image from Cellpose (generalist ``cyto3`` model, grayscale
    input, CPU). ``diameter`` is the typical cell diameter in pixels; None
    lets Cellpose estimate it from the image."""
    global _CELLPOSE_MODEL
    try:
        from cellpose import models
    except ImportError as exc:  # pragma: no cover - depends on the install
        raise RuntimeError("kcells needs the cellpose package (see README).") from exc
    if _CELLPOSE_MODEL is None:
        _CELLPOSE_MODEL = models.Cellpose(gpu=False, model_type="cyto3")
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    # Keep Cellpose's model-loading messages, but not its per-image progress
    # messages (channels, diameter estimation, timings).
    import logging
    cp_logger = logging.getLogger("cellpose")
    old_level = cp_logger.level
    cp_logger.setLevel(logging.WARNING)
    try:
        masks, _, _, _ = _CELLPOSE_MODEL.eval(gray, diameter=diameter, channels=[0, 0])
    finally:
        cp_logger.setLevel(old_level)
    return masks.astype(np.int32)


def segment_cells(image: Image.Image, cellpose_diameter=None) -> List[Cell]:
    """Outline the cells of one image with Cellpose, then find each cell's
    stained content and condensed chromatin."""
    rgb = np.array(image.convert("RGB"))
    h, w = rgb.shape[:2]
    p = _Params(h, w)
    od_raw = optical_density(rgb)
    od = cv2.GaussianBlur(od_raw, (0, 0), max(1.0, p.scale))
    od_fine = cv2.GaussianBlur(od_raw, (0, 0), 0.7)

    # A stained part only counts as a nucleus if it is clearly denser than
    # the image's typical cell content (empty cells and gaps between cells
    # only contain cytoplasm-level stain).
    cyto_level = float(np.median(od))
    nucleated_level = cyto_level + 4 * (float(np.median(np.abs(od - cyto_level))) or 1e-3)

    labels = _cellpose_labels(rgb, cellpose_diameter)
    return _build_cells(labels, od, od_fine, p, nucleated_level)

def _build_cells(labels: np.ndarray, od: np.ndarray, od_fine: np.ndarray, p: "_Params",
                 nucleated_level: float) -> List[Cell]:
    """Per-cell masks, stained content and condensed chromatin for every
    label (0 = background)."""
    h, w = labels.shape
    # Final cells, their stained content and condensed chromatin.
    cells: List[Cell] = []
    for lab in np.unique(labels):
        if lab == 0:
            continue
        region = cv2.morphologyEx((labels == lab).astype(np.uint8), cv2.MORPH_OPEN, p.smooth_kernel)
        comp, n = ndi.label(region)
        if n == 0:
            continue
        if n > 1:
            region = (comp == 1 + np.argmax(ndi.sum(region, comp, index=np.arange(1, n + 1)))).astype(np.uint8)
        region = ndi.binary_fill_holes(region)
        stained, stained_mean = _stained_content(od, region, p.min_fragment, p.open_kernel)
        chromatin = _condensed_chromatin(od_fine, stained, p.min_chromatin_piece)
        ys, xs = np.nonzero(region)
        x0, y0, x1, y1 = xs.min(), ys.min(), xs.max(), ys.max()
        cells.append(Cell(
            cell_id=len(cells) + 1,
            mask=region.astype(np.uint8) * 255,
            nucleus_mask=stained.astype(np.uint8) * 255,
            chromatin_mask=chromatin.astype(np.uint8) * 255,
            bbox=(int(x0), int(y0), int(x1 - x0 + 1), int(y1 - y0 + 1)),
            area=int(region.sum()),
            nucleus_area=int(stained.sum()),
            n_fragments=int(ndi.label(stained)[1]),
            has_nucleus=bool(stained.any()) and stained_mean >= nucleated_level,
            touches_border=bool(x0 <= 1 or y0 <= 1 or x1 >= w - 2 or y1 >= h - 2),
            centroid=(float(xs.mean()), float(ys.mean())),
            cell_likeness=_mask_likeness(region),
        ))

    # Stained parts much smaller than a typical nucleus (wall fragments,
    # slivers of neighbouring nuclei at the image edge) do not count.
    nucleated = [c.nucleus_area for c in cells if c.has_nucleus]
    if nucleated:
        min_nucleus = 0.15 * float(np.median(nucleated))
        for c in cells:
            if c.nucleus_area < min_nucleus:
                c.has_nucleus = False
    return cells
