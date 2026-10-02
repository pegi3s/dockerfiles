# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [ASTER](https://github.com/chaoszhang/ASTER.git), a family of optimization algorithms for species tree inference from gene trees, genome alignments, raw reads, and other phylogenomic data.

ASTER includes:

- ASTRAL-IV
- ASTRAL-Pro3
- Weighted ASTRAL
- CASTER-site
- CASTER-pair
- WASTER
- D* statistic

# Using the ASTER image in Linux

You should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster <tool_binary> -i /data/input_file -o /data/output_file`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `<tool_binary>` with the ASTER tool you want to execute (e.g., `astral4`, `astral-pro3`, `wastral`, `caster-site`).
- `input_file` - to the actual name of your input file.
- `output_file` - to the actual name of your output file.

<br>

**ASTRAL-IV** <a name="astral4"></a>

ASTRAL-IV infers an unrooted species tree from a set of gene trees under the Multi-Species Coalescent model, and is designed to scale to large phylogenomic datasets while handling incomplete lineage sorting and missing taxa.

If you want to run `astral4`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster astral4 -i /data/genetree.nw -o /data/species_tree_astral4.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `genetree.nw` - to the actual name of your input file (`.nw`).
- `species_tree_astral4.tre` - to the actual name of your output file (`.tre`).

<br>

**ASTRAL-Pro3** <a name="astral-pro3"></a>

ASTRAL-Pro3 infers an unrooted species tree from multi-copy gene trees (including paralogs and orthologs) under the Multi-Species Coalescent model, providing a faster and more memory-efficient implementation with branch length estimation in substitution-per-site units.

If you want to run `astral-pro3`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster astral-pro3 -i /data/multitree.nw -o /data/species_tree_astral-pro3.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `multitree.nw` - to the actual name of your input file (`.nw`).
- `species_tree_astral-pro3.tre` - to the actual name of your output file (`.tre`).

<br>

**Weighted ASTRAL** <a name="wastral"></a>

Weighted ASTRAL infers species trees from gene trees using threshold-free weighting schemes (based on branch support and/or branch length) to reduce the impact of low-confidence signals and improve accuracy over the standard unweighted ASTRAL approach.

If you want to run `wastral`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster wastral -i /data/genetree.nw -o /data/species_tree_wastral.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `genetree.nw` - to the actual name of your input file (`.nw`).
- `species_tree_wastral.tre` - to the actual name of your output file (`.tre`).

<br>

**CASTER-SITE** <a name="caster-site"></a>

CASTER-site infers species trees directly from genome-wide alignments using site pattern information, providing a scalable, gene-tree–free method that is statistically consistent under the MSC model and highly efficient for large phylogenomic datasets.

If you want to run `caster-site`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster caster-site -i /data/genetrees.tre_1.fas -o /data/species_tree_caster-site.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `genetrees.tre_1.fas` - to the actual name of your input file (`.fas`, `.phy`).
- `species_tree_caster-site.tre` - to the actual name of your output file (`.tre`).

<br>

**CASTER-PAIR** <a name="caster-pair"></a>

CASTER-pair infers species trees from genome-wide alignments using pairwise site patterns, offering a scalable and statistically consistent alternative to gene tree–based methods for large-scale phylogenomics.

If you want to run `caster-pair`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster caster-pair -i /data/example.phylip -o /data/species_tree_caster-pair.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `example.phylip` - to the actual name of your input file (`.fas`, `.phy`).
- `species_tree_caster-pair.tre` - to the actual name of your output file (`.tre`).

<br>

**WASTER** <a name="waster"></a>

WASTER is a coalescent-aware species tree inference tool that works directly from raw sequencing reads (e.g., FASTQ), calling SNPs and then using CASTER to reconstruct accurate species trees — even from low-coverage data.

If you want to run `waster`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster waster -i /data/input_list.txt -o /data/species_tree_waster.tre`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `input_list.txt` - to the actual name of your file containing a list of input files (`.fa`, `.fq`).
- `species_tree_waster.tre` - to the actual name of your output file (`.tre`).

<br>

**D*statistic** <a name="dstar"></a>

D*statistic detects signals of introgression (gene flow) between species by computing sliding-window statistics from genome alignments.

If you want to run `dstar`, you should adapt and run the following command:
`docker run --rm -v /your/data/dir:/data pegi3s/aster dstar /data/ape.fa /data/mapping.tsv 10000 > slidingwindow.tsv`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `ape.fa` - to the actual name of your input file (`.fa`, `.fas` or `.fasta`).
- `mapping.tsv` - to the actual name of your mapping file (`.tsv`).
- `slidingwindow.tsv` - to the actual name of your output file (`.tsv`).


## Using a Mapping File
Some tools (e.g., ASTRAL-IV, ASTRAL-Pro3) use a gene-to-species mapping file.

In that case, include the `-a` option:

``docker run --rm -v /your/data/dir:/data pegi3s/aster <tool_binary> -i /data/input_file -a /data/mapping_file.map -o /data/output_file``

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains your input data.
- `<tool_binary>` with the ASTER tool you want to execute (e.g., `astral4`, `astral-pro3`, `wastral`).
- `input_file` - to the actual name of your input file.
- `mapping_file.map` -to the actual name of your mapping file (`.map`).
- `output_file` - to the actual name of your output file.

<br>

To see the [ASTER](https://github.com/chaoszhang/ASTER.git) help, just run:
`docker run --rm pegi3s/aster <tool_binary> --help`
