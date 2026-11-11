"""Per-cell feature groups.

Pick any combination with ``--features`` (comma-separated, e.g.
``--features color,density`` or ``--features all``):

``shape`` (18)
    Nucleus shape (size relative to the other nuclei in the image,
    circularity, solidity, eccentricity, elongation, extent, Hu moments 1-2),
    nucleus-to-cell area ratio, number of stained fragments (the chromosomes
    of a dividing cell -> many), and the same 8 shape descriptors for the
    whole cell outline.
``color`` (8)
    Raw colour in CIE-Lab: nucleus mean L*, a*, b* and L* spread; cytoplasm
    (cell minus nucleus) mean L*, a*, b*; colour difference (Delta E) between
    nucleus and cytoplasm. Depends on the stain and white balance.
``texture`` (7)
    Chromatin texture inside the nucleus, on the per-image normalised stain
    image (stain-colour independent): GLCM contrast, homogeneity, energy,
    correlation; LBP entropy, flat-pattern fraction, edge-pattern fraction.
``gradient`` (6)
    Local gradients of the stain image: mean and spread of the gradient
    magnitude inside the nucleus, orientation coherence (structure tensor;
    high when chromosomes are aligned), orientation entropy, mean gradient
    over the whole cell, and edge sharpness along the nuclear border.
``density`` (6)
    Optical density (OD = -log(I/I0)): nucleus mean, 90th percentile and
    spread of OD, integrated OD relative to the median cell of the same image
    (log; proportional to DNA content for DNA stains), cytoplasm mean OD, and
    nucleus-to-cytoplasm OD ratio.

``chromatin`` (7)
    Condensed chromatin (the densest part of the stained content, found with
    a second Otsu threshold): fraction of the stained area that is
    condensed, number of condensed pieces (log), share of the largest piece,
    spread of the pieces (RMS distance from their centre / sqrt(nucleus
    area)), solidity of all pieces together, contrast (condensed OD /
    rest of the stained part), and condensed OD relative to the median cell
    of the same image. Dividing cells: many spread-out, high-contrast
    pieces (that make up a small share each).

Feature names are prefixed with their group (``density.nuc_mean_od``).
"""
from __future__ import annotations

from typing import List, Sequence

import cv2
import numpy as np

from object_pipeline.cell_segmentation import optical_density

FEATURE_GROUPS = ("shape", "color", "texture", "gradient", "density", "chromatin")

_SHAPE = ["rel_log_area", "circularity", "solidity", "eccentricity", "elongation", "extent", "hu1", "hu2"]
_NAMES = {
    "shape": ["nuc_" + n for n in _SHAPE] + ["nucleus_to_cell_area", "log_n_fragments"]
             + ["cell_" + n for n in _SHAPE],
    "color": ["nuc_L", "nuc_a", "nuc_b", "nuc_L_std", "cyto_L", "cyto_a", "cyto_b", "nuc_cyto_deltaE"],
    "texture": ["glcm_contrast", "glcm_homogeneity", "glcm_energy", "glcm_correlation",
                "lbp_entropy", "lbp_flat", "lbp_edge"],
    "gradient": ["nuc_grad_mean", "nuc_grad_std", "nuc_orient_coherence", "nuc_orient_entropy",
                 "cell_grad_mean", "nuc_border_sharpness"],
    "density": ["nuc_mean_od", "nuc_p90_od", "nuc_od_std", "nuc_rel_log_integrated_od",
                "cyto_mean_od", "nuc_cyto_od_ratio"],
    "chromatin": ["condensed_fraction", "log_n_pieces", "largest_piece_fraction", "piece_spread",
                  "condensed_solidity", "condensed_contrast", "condensed_rel_od"],
}
_GLCM_LEVELS = 16


def parse_feature_groups(spec: str) -> List[str]:
    """'color, density' -> ['color', 'density'] (canonical order, no
    duplicates). 'all' selects every group."""
    parts = [p.strip().lower() for p in spec.split(",") if p.strip()]
    if not parts:
        raise ValueError("No feature group given.")
    if "all" in parts:
        return list(FEATURE_GROUPS)
    bad = [p for p in parts if p not in FEATURE_GROUPS]
    if bad:
        raise ValueError(f"Unknown feature group(s) {bad}; choose from {', '.join(FEATURE_GROUPS)} or 'all'.")
    return [g for g in FEATURE_GROUPS if g in parts]


def cell_feature_names(groups: Sequence[str]) -> List[str]:
    return [f"{g}.{n}" for g in groups for n in _NAMES[g]]


def column_groups(groups: Sequence[str]) -> List[str]:
    """Group name of every feature column, in order."""
    return [g for g in groups for _ in _NAMES[g]]


def _crop(cell, *arrays):
    x, y, w, h = cell.bbox
    return [a[y:y + h, x:x + w] for a in arrays]


def _stain_image(rgb: np.ndarray, cells) -> np.ndarray:
    """Per-image normalised stain image in [0, 1]: 0 = cytoplasm level,
    1 = maximally darker (brightfield) / brighter (fluorescence)."""
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(np.float32)
    nuclei = np.zeros(gray.shape, bool)
    for c in cells:
        nuclei |= c.nucleus_mask > 0
    bg = float(np.median(gray[~nuclei])) if (~nuclei).any() else 255.0
    fg = float(np.median(gray[nuclei])) if nuclei.any() else 0.0
    stain = (bg - gray) / max(bg, 1.0) if fg <= bg else (gray - bg) / max(255.0 - bg, 1.0)
    return np.clip(stain, 0.0, 1.0)


# --------------------------------------------------------------------------
# Groups
# --------------------------------------------------------------------------

def _shape_rows(masks: List[np.ndarray], areas: List[int]) -> np.ndarray:
    median_area = float(np.median(areas)) or 1.0
    rows = []
    for crop, area in zip(masks, areas):
        contours, _ = cv2.findContours(crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contour = max(contours, key=cv2.contourArea)
        perimeter = cv2.arcLength(contour, True) or 1.0
        hull_area = cv2.contourArea(cv2.convexHull(contour)) or area
        h, w = crop.shape
        m = cv2.moments(crop, binaryImage=True)
        mu20, mu02, mu11 = m["mu20"] / m["m00"], m["mu02"] / m["m00"], m["mu11"] / m["m00"]
        common = np.sqrt(4 * mu11 ** 2 + (mu20 - mu02) ** 2)
        l1, l2 = (mu20 + mu02 + common) / 2, (mu20 + mu02 - common) / 2
        if len(contour) >= 5:
            (_, _), (rw, rh), _ = cv2.minAreaRect(contour)
            elongation = float(np.log(max(rw, rh, 1.0) / max(min(rw, rh), 1.0)))
        else:
            elongation = 0.0
        hu = cv2.HuMoments(m).flatten()[:2]
        rows.append([
            np.log(area / median_area),
            min(1.0, 4 * np.pi * area / perimeter ** 2),
            min(1.0, area / hull_area),
            float(np.sqrt(1 - l2 / l1)) if l1 > 0 else 0.0,
            elongation,
            area / float(max(w * h, 1)),
            *(-np.sign(hu) * np.log10(np.abs(hu) + 1e-30)),
        ])
    return np.array(rows, dtype=np.float64)


def _shape(cells) -> np.ndarray:
    nuc = _shape_rows([_crop(c, c.nucleus_mask)[0] for c in cells], [c.nucleus_area for c in cells])
    cell = _shape_rows([_crop(c, c.mask)[0] for c in cells], [c.area for c in cells])
    content = np.array([[c.nucleus_area / max(c.area, 1), np.log1p(c.n_fragments)] for c in cells])
    return np.hstack([nuc, content, cell])


def _color(rgb, cells) -> np.ndarray:
    lab = cv2.cvtColor(rgb.astype(np.float32) / 255.0, cv2.COLOR_RGB2LAB)
    rows = []
    for c in cells:
        lab_c, cm, nm = _crop(c, lab, c.mask, c.nucleus_mask)
        nuc = lab_c[nm > 0]
        cyto = lab_c[(cm > 0) & (nm == 0)]
        if len(cyto) == 0:
            cyto = nuc
        n_mean, c_mean = nuc.mean(axis=0), cyto.mean(axis=0)
        rows.append([*n_mean, float(nuc[:, 0].std()), *c_mean, float(np.linalg.norm(n_mean - c_mean))])
    return np.array(rows, dtype=np.float64)


def _texture(stain, cells) -> np.ndarray:
    from skimage.feature import graycomatrix, graycoprops, local_binary_pattern

    lbp = local_binary_pattern((stain * 255).astype(np.uint8), P=8, R=1, method="uniform")  # codes 0..9
    rows = []
    for c in cells:
        s, nm, codes = _crop(c, stain, c.nucleus_mask, lbp)
        inside = nm > 0
        # GLCM restricted to nucleus pixels: levels 1.._GLCM_LEVELS inside, 0 outside, then drop 0.
        q = np.zeros(s.shape, np.uint8)
        q[inside] = 1 + np.minimum((s[inside] * _GLCM_LEVELS).astype(int), _GLCM_LEVELS - 1)
        glcm = graycomatrix(q, distances=[1, 2], angles=[0, np.pi / 4, np.pi / 2, 3 * np.pi / 4],
                            levels=_GLCM_LEVELS + 1, symmetric=True, normed=False)[1:, 1:].astype(np.float64)
        totals = glcm.sum(axis=(0, 1), keepdims=True)
        totals[totals == 0] = 1.0
        glcm /= totals
        props = [float(np.nan_to_num(np.mean(graycoprops(glcm, p))))
                 for p in ("contrast", "homogeneity", "energy", "correlation")]
        hist = np.bincount(codes[inside].astype(int), minlength=10)[:10].astype(np.float64)
        hist /= max(hist.sum(), 1.0)
        nz = hist[hist > 0]
        rows.append([*props, float(-(nz * np.log2(nz)).sum()), float(hist[0] + hist[8]), float(hist[3:6].sum())])
    return np.array(rows, dtype=np.float64)


def _gradient(stain, cells) -> np.ndarray:
    stain = cv2.GaussianBlur(stain, (0, 0), 1.0)
    gx = cv2.Sobel(stain, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(stain, cv2.CV_32F, 0, 1, ksize=3)
    mag = np.hypot(gx, gy)
    kernel = np.ones((3, 3), np.uint8)
    rows = []
    for c in cells:
        gx_c, gy_c, mag_c, cm, nm = _crop(c, gx, gy, mag, c.mask, c.nucleus_mask)
        inside = nm > 0
        m = mag_c[inside]
        jxx, jyy = float((gx_c[inside] ** 2).sum()), float((gy_c[inside] ** 2).sum())
        jxy = float((gx_c[inside] * gy_c[inside]).sum())
        coherence = np.sqrt((jxx - jyy) ** 2 + 4 * jxy ** 2) / (jxx + jyy) if jxx + jyy > 0 else 0.0
        theta = np.mod(np.arctan2(gy_c[inside], gx_c[inside]), np.pi)
        hist, _ = np.histogram(theta, bins=8, range=(0, np.pi), weights=m)
        hist = hist / hist.sum() if hist.sum() > 0 else np.full(8, 1 / 8)
        nz = hist[hist > 0]
        nm8 = inside.astype(np.uint8)
        border = (nm8 - cv2.erode(nm8, kernel)) > 0
        rows.append([float(m.mean()), float(m.std()), float(coherence), float(-(nz * np.log2(nz)).sum() / 3.0),
                     float(mag_c[cm > 0].mean()), float(mag_c[border].mean()) if border.any() else 0.0])
    return np.array(rows, dtype=np.float64)


def _density(rgb, cells) -> np.ndarray:
    od = optical_density(rgb)
    rows = []
    for c in cells:
        od_c, cm, nm = _crop(c, od, c.mask, c.nucleus_mask)
        nuc = od_c[nm > 0]
        cyto = od_c[(cm > 0) & (nm == 0)]
        cyto_mean = float(cyto.mean()) if len(cyto) else 0.0
        rows.append([float(nuc.mean()), float(np.percentile(nuc, 90)), float(nuc.std()),
                     float(nuc.sum()), cyto_mean, float(nuc.mean()) / max(cyto_mean, 1e-3)])
    rows = np.array(rows, dtype=np.float64)
    median_iod = float(np.median(rows[:, 3])) or 1.0
    rows[:, 3] = np.log(np.maximum(rows[:, 3], 1e-6) / median_iod)
    return rows


def _chromatin(rgb, cells) -> np.ndarray:
    from scipy import ndimage as ndi

    od = cv2.GaussianBlur(optical_density(rgb), (0, 0), 0.7)
    rows = []
    for c in cells:
        od_c, nm, ch = _crop(c, od, c.nucleus_mask, c.chromatin_mask)
        nuc, cond = nm > 0, ch > 0
        area = int(cond.sum())
        if area == 0:
            rows.append([0.0, 0.0, 1.0, 0.0, 1.0, 1.0, float(od_c[nuc].mean())])
            continue
        lab, n = ndi.label(cond)
        sizes = np.asarray(ndi.sum(cond, lab, index=np.arange(1, n + 1)))
        ys, xs = np.nonzero(cond)
        spread = np.sqrt(((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2).mean()) / np.sqrt(max(nuc.sum(), 1))
        hull = cv2.contourArea(cv2.convexHull(np.column_stack([xs, ys]).astype(np.int32))) if area >= 3 else area
        rest = od_c[nuc & ~cond]
        cond_mean = float(od_c[cond].mean())
        rows.append([
            area / max(nuc.sum(), 1),
            float(np.log1p(n)),
            float(sizes.max() / area),
            float(spread),
            min(1.0, area / max(hull, 1.0)),
            cond_mean / max(float(rest.mean()) if rest.size else cond_mean, 1e-3),
            cond_mean,
        ])
    rows = np.array(rows, dtype=np.float64)
    rows[:, 6] /= float(np.median(rows[:, 6])) or 1.0
    return rows


def cell_features(rgb: np.ndarray, cells: list, groups: Sequence[str]) -> np.ndarray:
    """Feature matrix (n_cells x n_features) for nucleated cells, columns in
    the order given by ``cell_feature_names(groups)``."""
    if not cells:
        return np.empty((0, len(cell_feature_names(groups))), dtype=np.float64)
    stain = _stain_image(rgb, cells) if {"texture", "gradient"} & set(groups) else None
    parts = []
    for g in groups:
        if g == "shape":
            parts.append(_shape(cells))
        elif g == "color":
            parts.append(_color(rgb, cells))
        elif g == "texture":
            parts.append(_texture(stain, cells))
        elif g == "gradient":
            parts.append(_gradient(stain, cells))
        elif g == "density":
            parts.append(_density(rgb, cells))
        elif g == "chromatin":
            parts.append(_chromatin(rgb, cells))
    return np.hstack(parts)
