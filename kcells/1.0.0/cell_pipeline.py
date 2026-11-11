#!/usr/bin/env python3
"""Find unusual cells in microscopy images by clustering them.

1. For every image, outline the individual cells with the Cellpose
   deep-learning model, then find each cell's stained content (nucleus / chromosomes)
   and its condensed chromatin (see object_pipeline/cell_segmentation.py).
2. Describe every nucleated cell with a feature vector built from the
   feature groups chosen with ``--features`` (any combination of shape,
   color, texture, gradient, density, chromatin; see
   object_pipeline/cell_features.py).
3. Standardise the features, give every selected group the same total
   weight, and
   - cluster all cells from all images into K clusters (``--cluster-method``:
     Ward hierarchical clustering, K-Means, or a Gaussian mixture);
   - give every cell an **unusualness** score: its mean distance to its
     nearest neighbours in feature space, as a robust z-score (median / MAD
     over all cells). The ``--n-unusual`` highest-scoring cells are marked.
4. Save each original image with every cell outlined in its cluster colour
   and the most unusual cells marked with their rank
   (``annotated/<image>.png``), plus ``cells.csv`` (one row per cell) and
   ``summary.txt``.

``--input`` can be a folder of images or a single image file.
"""
from __future__ import annotations

import argparse
import csv
import logging
import sys
import warnings
from pathlib import Path
from typing import Dict, List

import cv2
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler

# Library deprecation notices (PyTorch, Cellpose, scikit-image) say nothing
# about the results; keep the output to the pipeline's own messages.
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message="Sparse invariant checks are implicitly disabled")

from object_pipeline.cell_features import (
    FEATURE_GROUPS, cell_feature_names, cell_features, column_groups, parse_feature_groups,
)
from object_pipeline.cell_segmentation import Cell, segment_cells
from object_pipeline.visualization import annotate_image

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff", ".tif"}
CLUSTER_METHODS = ("ward", "kmeans", "gmm")
# Segmented regions that do not look like a cell (cell-likeness below this,
# see cell_segmentation.cell_likeness) are segmentation failures: they are
# reported but not clustered or ranked.
MIN_CELL_LIKENESS = 0.8

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("cell_pipeline")


def list_input_images(input_path: Path) -> list:
    """A folder -> its supported images; a single image file -> [that file]."""
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() in SUPPORTED_EXTENSIONS else []
    return sorted(p for p in input_path.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS)


def _outline(mask: np.ndarray) -> np.ndarray:
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(contours, key=cv2.contourArea)


def _status(cell: Cell, include_border_cells: bool) -> str:
    if not cell.has_nucleus:
        return "no nucleus"
    if cell.cell_likeness < MIN_CELL_LIKENESS:
        return "irregular"
    if cell.touches_border and not include_border_cells:
        return "edge"
    return "clustered"


def cluster(X: np.ndarray, k: int, method: str) -> np.ndarray:
    """Cluster labels for the rows of X.

    - ward: agglomerative clustering that repeatedly merges the two groups
      whose merge increases the within-group variance least. Unlike K-Means
      it does not force equally sized groups, so a small distinct group can
      survive as its own cluster.
    - kmeans: K-Means (10 restarts).
    - gmm: Gaussian mixture with one diagonal covariance per cluster, so
      clusters can have different spreads.
    """
    if k <= 1:
        return np.zeros(len(X), int)
    if method == "ward":
        from sklearn.cluster import AgglomerativeClustering
        return AgglomerativeClustering(n_clusters=k, linkage="ward").fit_predict(X)
    if method == "kmeans":
        from sklearn.cluster import KMeans
        return KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    if method == "gmm":
        from sklearn.mixture import GaussianMixture
        return GaussianMixture(n_components=k, covariance_type="diag", n_init=5, random_state=42).fit_predict(X)
    raise ValueError(f"Unknown cluster method {method!r}; choose from {CLUSTER_METHODS}")


def unusualness(X: np.ndarray, n_neighbors: int = 5) -> np.ndarray:
    """Robust z-score of each cell's mean distance to its nearest neighbours.

    A cell whose most similar cells are still far away is unusual. 0 = a
    typical cell; values above ~3 are clearly unusual.
    """
    n = len(X)
    if n < 3:
        return np.zeros(n)
    k = min(n_neighbors, n - 1)
    d = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)
    np.fill_diagonal(d, np.inf)
    knn = np.sort(d, axis=1)[:, :k].mean(axis=1)
    med = np.median(knn)
    mad = 1.4826 * np.median(np.abs(knn - med)) or 1e-9
    return (knn - med) / mad


def run(image_paths: List[Path], output_dir: Path, k: int, groups: List[str], include_border_cells: bool,
        method: str, n_unusual: int, cellpose_diameter) -> bool:
    output_dir.mkdir(parents=True, exist_ok=True)
    feature_set = "+".join(groups)
    logger.info("Features: %s | K=%d | method: %s | %d image(s)",
                feature_set, k, method, len(image_paths))

    # 1. Segment cells; 2. compute features of the cells to cluster.
    per_image: Dict[Path, List[Cell]] = {}
    feats, owners = [], []          # owners[i] = (image_path, cell)
    for path in image_paths:
        image = Image.open(path).convert("RGB")
        cells = segment_cells(image, cellpose_diameter)
        per_image[path] = cells
        used = [c for c in cells if _status(c, include_border_cells) == "clustered"]
        status = [_status(c, include_border_cells) for c in cells]
        logger.info("%s: %d cell(s) found; %d clustered, %d without nucleus, %d irregular shape, "
                    "%d edge cell(s) skipped.", path.name, len(cells), len(used), status.count("no nucleus"),
                    status.count("irregular"), status.count("edge"))
        if used:
            feats.append(cell_features(np.array(image), used, groups))
            owners.extend((path, c) for c in used)

    if len(owners) < k:
        logger.error("Only %d cell(s) available for clustering, fewer than K=%d.", len(owners), k)
        return False

    # 3. Standardise, give every feature group the same total weight (divide
    #    each column by sqrt(number of features in its group)), cluster, score.
    raw = np.vstack(feats)
    X = np.nan_to_num(StandardScaler().fit_transform(raw))
    col_groups = column_groups(groups)
    X_weighted = X / np.sqrt([col_groups.count(g) for g in col_groups])
    labels = cluster(X_weighted, k, method)
    score = unusualness(X_weighted)
    order = np.argsort(-score)
    rank = np.empty(len(score), int)
    rank[order] = np.arange(1, len(score) + 1)
    row_of = {(p, c.cell_id): i for i, (p, c) in enumerate(owners)}

    # 4a. Annotated originals.
    ann_dir = output_dir / "annotated"
    ann_dir.mkdir(exist_ok=True)
    for path, cells in per_image.items():
        by_cluster: Dict[int, List[np.ndarray]] = {}
        skipped, markers = [], []
        for c in cells:
            i = row_of.get((path, c.cell_id))
            if i is None:
                skipped.append(_outline(c.mask))
                continue
            by_cluster.setdefault(int(labels[i]), []).append(_outline(c.mask))
            if rank[i] <= n_unusual:
                markers.append((*c.centroid, rank[i]))
        vis = annotate_image(np.array(Image.open(path).convert("RGB")), by_cluster, k,
                             f"{feature_set} | {method} | {path.name}", excluded_contours=skipped,
                             excluded_label="not clustered (edge / no nucleus / irregular)", markers=markers,
                             marker_label=f"numbers = {n_unusual} most unusual cells (1 = most)" if n_unusual else "")
        Image.fromarray(vis).save(ann_dir / f"{path.stem}.png")

    # 4b. Per-cell table.
    names = cell_feature_names(groups)
    with open(output_dir / "cells.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["image", "cell_id", "status", "cluster", "unusualness", "unusual_rank", "centroid_x",
                    "centroid_y", "cell_area_px", "nucleus_area_px", "n_fragments", "touches_border",
                    "cell_likeness"] + names)
        for path, cells in per_image.items():
            for c in cells:
                i = row_of.get((path, c.cell_id))
                w.writerow([path.name, c.cell_id, _status(c, include_border_cells),
                            "" if i is None else int(labels[i]),
                            "" if i is None else f"{score[i]:.2f}",
                            "" if i is None else int(rank[i]),
                            f"{c.centroid[0]:.1f}", f"{c.centroid[1]:.1f}", c.area, c.nucleus_area,
                            c.n_fragments, int(c.touches_border), f"{c.cell_likeness:.3f}"]
                           + ([f"{v:.5g}" for v in raw[i]] if i is not None else [""] * len(names)))

    # 4c. Summary.
    with open(output_dir / "summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Features: {feature_set}\nK: {k}\nCluster method: {method}\n")
        f.write(f"Most unusual cells marked: {n_unusual}\n")
        f.write(f"Border cells: {'include' if include_border_cells else 'exclude'}\n")
        f.write(f"Cellpose diameter: {'auto' if cellpose_diameter is None else cellpose_diameter}\n\n")
        f.write("Cells per cluster per image\n")
        f.write(f"{'image':<20}" + "".join(f"{'C' + str(c):>7}" for c in range(k))
                + f"{'edge':>7}{'no nuc':>8}{'irreg':>7}\n")
        totals = np.zeros(k, int)
        for path, cells in per_image.items():
            counts = np.zeros(k, int)
            for c in cells:
                i = row_of.get((path, c.cell_id))
                if i is not None:
                    counts[labels[i]] += 1
            totals += counts
            n_edge = sum(_status(c, include_border_cells) == "edge" for c in cells)
            n_none = sum(not c.has_nucleus for c in cells)
            n_irr = sum(_status(c, include_border_cells) == "irregular" for c in cells)
            f.write(f"{path.name:<20}" + "".join(f"{v:>7}" for v in counts) + f"{n_edge:>7}{n_none:>8}{n_irr:>7}\n")
        f.write(f"{'TOTAL':<20}" + "".join(f"{v:>7}" for v in totals) + "\n\n")

        f.write("Most distinctive features per cluster (mean z-score vs. all cells)\n")
        for c in range(k):
            sel = labels == c
            if sel.any():
                z = X[sel].mean(axis=0)
                top = np.argsort(-np.abs(z))[:4]
                f.write(f"  Cluster {c}: " + ", ".join(f"{names[j]} {z[j]:+.1f}" for j in top) + "\n")

        f.write(f"\nMost unusual cells (unusualness = robust z-score of nearest-neighbour distance)\n")
        for i in order[:max(n_unusual, 10)]:
            path, c = owners[i]
            top = np.argsort(-np.abs(X[i]))[:3]
            f.write(f"  #{rank[i]:<3} {path.name} cell {c.cell_id:<4} unusualness {score[i]:+.1f}  cluster {labels[i]}"
                    f"  ({', '.join(f'{names[j]} {X[i, j]:+.1f}' for j in top)})\n")

    logger.info("Results written to %s", output_dir)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", "--input-dir", dest="input", required=True, type=Path,
                        help="Folder of images, or a single image file.")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--k", required=True, type=int, help="Number of cell clusters.")
    parser.add_argument("--cellpose-diameter", required=True,
                        help="Typical cell diameter in pixels for Cellpose, or 'auto' to let Cellpose "
                             "estimate it for each image.")
    parser.add_argument("--features", required=True,
                        help="Feature groups to use, comma-separated, in any combination: "
                             f"{', '.join(FEATURE_GROUPS)}; or 'all'.")
    parser.add_argument("--cluster-method", required=True, choices=CLUSTER_METHODS,
                        help="ward (hierarchical, allows small distinct clusters), kmeans, or gmm "
                             "(Gaussian mixture).")
    parser.add_argument("--n-unusual", required=True, type=int,
                        help="Number of most unusual cells to mark on the images (0 = none).")
    parser.add_argument("--border-cells", required=True, choices=("include", "exclude"),
                        help="'include': also cluster cells cut by the image edge (their shape is "
                             "incomplete); 'exclude': draw them in grey and do not cluster them.")
    args = parser.parse_args()

    if not args.input.exists():
        parser.error(f"Input does not exist: {args.input}")
    if args.k < 1:
        parser.error("--k must be >= 1")
    if args.n_unusual < 0:
        parser.error("--n-unusual must be >= 0")
    if args.cellpose_diameter.lower() == "auto":
        diameter = None
    else:
        try:
            diameter = float(args.cellpose_diameter)
        except ValueError:
            diameter = -1.0
        if diameter <= 0:
            parser.error("--cellpose-diameter must be 'auto' or a positive number of pixels")
    try:
        groups = parse_feature_groups(args.features)
    except ValueError as exc:
        parser.error(str(exc))
    images = list_input_images(args.input)
    if not images:
        parser.error(f"No supported images in {args.input}")

    ok = run(images, args.output_dir, args.k, groups, args.border_cells == "include", args.cluster_method,
             args.n_unusual, diameter)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
