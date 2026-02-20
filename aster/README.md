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

## Using a Mapping File
Some tools (e.g., ASTRAL-IV, ASTRAL-Pro3) use a gene-to-species mapping file.

In that case, include the `-a` option:

``docker run --rm -v /your/data/dir:/data pegi3s/aster <tool_binary> -i /data/input_file -a /data/mapping_file.map -o /data/output_file``

## Input and Output Formats by Tool
**ASTRAL-IV** (`astral4`), **ASTRAL-Pro3** (`astral-pro3`), **Weighted ASTRAL** (`wastral`)
- **Input:** gene trees in Newick format (`.nw`)
- **Output:** species tree (`.tre`)

**CASTER-site** (`caster-site`), **CASTER-pair** (`caster-pair`)
- **Input:** sequence alignments (`.fas`, `.phy`)
- **Output:** species tree (`.tre`)

**WASTER** (`waster`)
- **Input:** list of FASTA/FASTQ files
- **Output:** species tree (`.tre`)

**D*statistic** (`dstar`)
- **Input:** alignment file (`.fas`)
- **Output:** D* statistic + sliding window table (`.tsv`)


To see the [ASTER](https://github.com/chaoszhang/ASTER.git) help, just run:
`docker run --rm pegi3s/aster <tool_binary> --help`


