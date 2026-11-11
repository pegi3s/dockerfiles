# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# kcells: cell segmentation, clustering and unusual-cell detection

kcells finds the individual cells in microscopy images with the **Cellpose**
cyto3 deep-learning model, describes every cell with a user-selected set of
features, clusters all cells (from one or several images) into **K**
groups, and ranks every cell by how **unusual** it is. Each cell is outlined
on the original image in the colour of its cluster, and the most unusual
cells are marked with their rank.

## Usage

You should adapt and run the following command:

```
docker run --rm --user "$(id -u):$(id -g)" -v "/your/data/dir/input_folder:/app/input:ro" -v "/your/data/dir/results_folder:/app/output" pegi3s/kcells --input /app/input --output-dir /app/output --cellpose-diameter celldia --border-cells bcells --cluster-method cmethod --k nk --features feat --n-unusual nunusual
```

In this command, you should replace:

- `/your/data/dir` (twice) with the path to the working directory that contains your folder with the input images. Results are written in the working folder too.
- `celldia` by the typical cell diameter in pixels for Cellpose. If you leave as **auto** it will be estimated from the pictures.
- `bcells` by **include** or **exclude**. This will include or exclude the incomplete cells at the image borders.
- `cmethod` by the clustering method (either **ward** (hierarchical; lets a small, distinct group form its own cluster), **kmeans**, or **gmm** (Gaussian mixture; clusters may differ in spread))
- `nk` by the number of cell clusters
- `feat` by the features to consider (valid features are a comma-separated combination of `shape`, `color`, `texture`, `gradient`, `density`, `chromatin`, or `all`, for instance texture,gradient,chromatin)
- `nunusual` by the number of most unusual cells to mark on the images.

## Output

```
results/
├── annotated/<image>.png  # original image; every clustered cell outlined in
│                          # its cluster colour; the most unusual cells marked
│                          # with their rank (1 = most unusual); cells not
│                          # clustered (edge / no nucleus / irregular) in thin grey
├── cells.csv              # one row per cell: image, cell id, status
│                          # (clustered / edge / no nucleus / irregular),
│                          # cluster, unusualness, unusual rank, centroid,
│                          # cell and nucleus area, fragments, edge flag,
│                          # cell-likeness, every feature
└── summary.txt            # cells per cluster per image, the most distinctive
                           # features of each cluster, and the most unusual
                           # cells with the features that make them unusual
```

Cluster numbers are arbitrary: cluster 0 in one run is unrelated to cluster 0
in another run.

## Definitions

Terms used below:

- **Optical density (OD)**: the amount of stain in a pixel, computed from
  its brightness: `OD = −log(pixel brightness / brightness of an unstained
  area)`. 0 means no stain; the darker the pixel, the higher its OD.
- **Stain image**: a grayscale version of the image, rescaled per image so
  that 0 is the typical brightness outside the nuclei and 1 is black. It
  does not depend on the stain colour.
- **Median cell of the image**: values "relative to the median cell" are
  divided by the median value of the clustered cells of the *same* image,
  so they compare a cell with its neighbours rather than with other images.
- Names in brackets are the column names in `cells.csv` (each prefixed with
  the group name, e.g. `shape.nuc_circularity`).

### `shape`: geometry of the nucleus and the cell (18 features)

Eight shape measurements are made on the nucleus (columns `nuc_…`) and the
same eight on the whole cell outline (columns `cell_…`):
1. **Relative size** (`rel_log_area`): area divided by the median area of
   the image's nuclei (or cells), as a logarithm. 0 = typical size;
   positive = larger, negative = smaller.
2. **Circularity** (`circularity`): `4π × area / perimeter²`. 1 for a
   perfect circle, lower for irregular or ragged outlines.
3. **Solidity** (`solidity`): area divided by the area of its convex hull
   (the smallest outline without inward dents). 1 for any convex shape
   (circle, ellipse, rectangle), lower for notched or lobed shapes.
4. **Eccentricity** (`eccentricity`): of the ellipse with the same spread
   as the shape. 0 = circle, close to 1 = very stretched.
5. **Elongation** (`elongation`): length divided by width of the smallest
   rotated rectangle enclosing the shape, as a logarithm. 0 = as long as
   wide.
6. **Extent** (`extent`): area divided by the area of the horizontal/vertical
   bounding box. Lower for diagonal or irregular shapes.
7. and 8. **Hu moments 1 and 2** (`hu1`, `hu2`): two standard numbers
   describing how the area is distributed around its centre, independent of
   position, size and rotation. Hu moment 1 is smallest for a disc and grows
   as the shape becomes elongated or irregular; Hu moment 2 is 0 for a disc
   or square and grows as the shape becomes elongated. They are stored as
   `−log10(value)`, so a *larger* moment gives a *smaller* number (and a
   perfect disc gives a very large `hu2`).

Plus two features about the content of the cell:
- **Nucleus-to-cell area** (`nucleus_to_cell_area`): nucleus area divided
  by cell area.
- **Number of stained fragments** (`log_n_fragments`): separate stained
  pieces in the cell, as `log(1 + number)`. One for an interphase nucleus,
  several for the chromosomes of a dividing cell.

### `color`: raw colour (8 features)

Colours are measured in the CIE-Lab colour space, which separates
brightness from colour: **L\*** = lightness (0 black to 100 white),
**a\*** = green (negative) to red/magenta (positive), **b\*** = blue
(negative) to yellow (positive).
- **Nucleus mean L\*, a\*, b\*** (`nuc_L`, `nuc_a`, `nuc_b`).
- **Nucleus lightness variation** (`nuc_L_std`): standard deviation of L\*
  inside the nucleus.
- **Cytoplasm mean L\*, a\*, b\*** (`cyto_L`, `cyto_a`, `cyto_b`).
- **Nucleus–cytoplasm colour difference** (`nuc_cyto_deltaE`): the distance
  between their mean colours in Lab space (known as ΔE; about 2 is the
  smallest difference a person notices).

These depend directly on the stain, the illumination and the camera's white
balance.

### `texture`: chromatin pattern inside the nucleus (7 features)

Measured on the stain image, inside the nucleus only.

Four features compare each pixel with the pixels 1 and 2 pixels away, in
four directions (averaged), after reducing the stain image to 16 grey
levels (a "grey-level co-occurrence matrix", GLCM):
- **Contrast** (`glcm_contrast`): how different neighbouring pixels are.
  High for coarse, high-contrast chromatin.
- **Homogeneity** (`glcm_homogeneity`): how similar neighbouring pixels
  are. High for smooth chromatin.
- **Energy** (`glcm_energy`): how few distinct neighbour combinations occur.
  High for uniform areas or simple, repetitive patterns.
- **Correlation** (`glcm_correlation`): how predictable a pixel is from its
  neighbour. High when the pattern is made of large blobs rather than fine
  grain.

Three features look at the 8 pixels immediately around each pixel and
classify the local pattern ("local binary patterns", LBP):
- **Pattern variety** (`lbp_entropy`): how varied the local patterns are,
  as an entropy. High for complex, granular texture.
- **Flat/spot fraction** (`lbp_flat`): share of pixels whose neighbours are
  all darker or all lighter than (or equal to) them: flat areas and isolated
  spots.
- **Edge fraction** (`lbp_edge`): share of pixels with about half their
  neighbours lighter and half darker: pixels on an edge between light and
  dark, such as the border of a chromosome.

### `gradient`: local edges and their directions (6 features)

The gradient at a pixel is how fast the stain image changes there (its
strength) and in which direction. Measured after slight smoothing.
- **Mean edge strength in the nucleus** (`nuc_grad_mean`).
- **Variation of edge strength in the nucleus** (`nuc_grad_std`): standard
  deviation.
- **Direction coherence** (`nuc_orient_coherence`): 0 when the edges in the
  nucleus point in all directions, 1 when they all point the same way.
  High when chromosomes are aligned (e.g. metaphase, anaphase).
- **Direction variety** (`nuc_orient_entropy`): how evenly the edge
  directions are spread over 8 direction classes (weighted by edge
  strength), from 0 (one direction) to 1 (all directions equally). Low when
  chromosomes are aligned.
- **Mean edge strength in the whole cell** (`cell_grad_mean`).
- **Sharpness of the nuclear border** (`nuc_border_sharpness`): mean edge
  strength along the outline of the nucleus. High for a crisp border, low
  for a blurred one.

### `density`: how much stain the nucleus holds (6 features)

Based on optical density (OD, see above).
- **Mean OD of the nucleus** (`nuc_mean_od`).
- **High OD of the nucleus** (`nuc_p90_od`): the 90th percentile, i.e. the
  value that 10% of the nucleus pixels exceed. Reflects the darkest parts.
- **OD variation in the nucleus** (`nuc_od_std`): standard deviation.
- **Total stain relative to the median cell** (`nuc_rel_log_integrated_od`):
  the sum of OD over all nucleus pixels, divided by that of the median cell
  of the image, as a logarithm. 0 = typical; `log 2 ≈ 0.69` = twice as much
  stain. With a stain that binds DNA in proportion to its amount (e.g.
  Feulgen), this approximates relative DNA content.
- **Mean OD of the cytoplasm** (`cyto_mean_od`).
- **Nucleus-to-cytoplasm OD ratio** (`nuc_cyto_od_ratio`): mean OD of the
  nucleus divided by mean OD of the cytoplasm.

### `chromatin`: condensation and fragmentation (7 features)

**Condensed chromatin** is the darkest part of the nucleus: inside the
nucleus, pixels with OD above a threshold chosen automatically from that
nucleus's own OD values (Otsu's method, which splits the values into a
darker and a lighter group). It forms one or more separate **pieces**; in a
dividing cell these are the chromosomes.
- **Condensed fraction** (`condensed_fraction`): area of condensed chromatin
  divided by nucleus area.
- **Number of pieces** (`log_n_pieces`): as `log(1 + number)`.
- **Share of the largest piece** (`largest_piece_fraction`): area of the
  largest piece divided by the total condensed area. 1 = a single piece;
  low = many pieces of similar size.
- **Spread of the pieces** (`piece_spread`): the average distance of
  condensed pixels from their common centre (root-mean-square), divided by
  the square root of the nucleus area so that it does not depend on nucleus
  size.
- **Compactness of the pieces together** (`condensed_solidity`): condensed
  area divided by the area of the convex hull around all pieces. Low when
  the pieces are scattered with gaps between them.
- **Contrast** (`condensed_contrast`): mean OD of the condensed chromatin
  divided by mean OD of the rest of the nucleus.
- **Relative darkness** (`condensed_rel_od`): mean OD of the condensed
  chromatin divided by that of the median cell of the image.

Dividing cells typically have many pieces, each a small share of the total,
spread out, with high contrast.

If a nucleus has no condensed chromatin, its values are set to: fraction 0,
number of pieces 0, largest share 1, spread 0, compactness 1, contrast 1,
and relative darkness = its whole-nucleus mean OD relative to the median
cell.

### Before choosing groups

`texture`, `gradient` and `color` are sensitive to how the image was taken
(sharpening, focus, resolution, stain, white balance). When images were
taken differently, these groups also separate the *images*, not only the
cells.


## How it works

1. **Cell outlines.** [Cellpose](https://github.com/MouseLand/cellpose) 3,
   a generalist `cyto3` model, run on the grayscale image on the CPU. It is a
   neural network trained on many thousands of hand-outlined cells, so it
   closes faint walls and ignores nuclear rims and spindle fibres. The cell
   diameter is set with `--cellpose-diameter` (pixels, or `auto` to estimate
   it per image).
   About 5–60 s per image on a CPU, depending on image size.
2. **Stain density.** The image is converted to optical density
   (`OD = −log(I/I₀)`, `I₀` = the image's own bright level), i.e. the amount
   of stain per pixel.
3. **Stained content per cell.** Inside each cell, the nucleus (or the
   chromosomes) is separated from the cytoplasm by Otsu's threshold on *that
   cell's own* OD values. A cell counts as **nucleated** only if both:
   - its stained part is clearly denser than the image's typical cytoplasm
     (median OD + 4 × median absolute deviation), and
   - it is at least 15% of the image's median nucleus size.

   Empty cells, gaps between cells, out-of-focus nuclei and slivers of a
   neighbour's nucleus at the image edge are therefore not clustered. A
   nucleated cell whose outline is not cell-like (solidity < 0.8, i.e.
   notched or ring-shaped; very elongated outlines, longer than 4:1, also
   count as less cell-like) is reported as **irregular** and not clustered.
4. **Condensed chromatin.** Inside each stained part, a second, stricter
   Otsu threshold keeps only the densest chromatin, e.g. the individual
   chromosomes of a dividing cell without the faint haze between them.
5. **Features** for every nucleated cell, from the groups chosen with
   `--features` (see Definitions above).
6. **Clustering and unusualness.** Features are standardised, and every
   selected **group** gets the same total weight (each feature is divided by
   √(number of features in its group)). Then:
   - all cells from all images are clustered into K groups
     (`--cluster-method`: Ward, K-Means or Gaussian mixture);
   - every cell gets an **unusualness** score: the mean distance to its 5
     most similar cells, as a robust z-score over all cells. 0 means a
     typical cell; above about 3 is clearly unusual. The `--n-unusual` most
     unusual cells are marked on the images.
7. **Output.** Every original image with each cell outlined in its cluster
   colour and the most unusual cells numbered, a per-cell CSV, and a
   summary.

