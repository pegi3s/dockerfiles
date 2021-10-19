# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# Biopython utilities

This Docker image contains Biopython-based scripts to perform different tasks. 

# `convert_tree.py`

The `convert_tree.py` script allows converting between different Phylogenetic Tree formats using the [Phylo module](https://biopython.org/wiki/Phylo).

Run the following command to show the script help: `docker run --rm pegi3s/biopython_utilities convert_tree.py -h`

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/biopython_utilities convert_tree.py -i /data/<input_tree> -if <input_format> -o /data/<output_tree> -of <output_format>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input phylogenetic tree you want to convert.
- `<input_tree>` to the actual name of your input file.
- `<input_format>` to the format of your input file (one of: `newick`, `nexus`, `nexml`, `phyloxml`, or `cdao`).
- `<output_tree>` to the actual name of your output file.
- `<output_format>` to the format of your output file (one of: `newick`, `nexus`, `nexml`, `phyloxml`, or `cdao`).

## Test data

To test this utility, the input NEXUS file is available [here]([here](https://github.com/pegi3s/dockerfiles/tree/master/test_data/tree.1.nex)).

# `plot_gene_distribution.py`

The `plot_gene_distribution.py` script represents a list of genes in a *GenomeDiagram*. The input data must be a TSV file with four columns: (1) the group to wich the gene belongs to (each group is drawn in a different color), (2) the name of the gene, (3) the start coordinate, and (4) the end coordinate. For instance, the test data available [here](https://github.com/pegi3s/dockerfiles/tree/master/biopython_utilities/test_data/test_plot_gene_distribution.tsv) contains the following 9 genes:

```
F-Box	Fbox1	320276	321550
F-Box	Fbox2	363707	364915
F-Box	Fbox3	473425	472151
F-Box	Fbox4	805518	807710
F-Box	Fbox5	812394	813713
F-Box	Fbox6	1542754	1541522
F-Box	Fbox7	1551260	1550496
F-Box	Fbox8	3672240	3673466
SRNase	SRNase	1545618	1547318
```

By default, the script:
- Represents all genes in a single horizontal line. It is possible to set the number of axis breaks with the `--breaks`parameter (default is 20).
- Determines the start and end positions by taking the minimum and maximum from all the genes. Nevertheless, it is possible to use the `--start` and `--end` parameters to define a custom interval.
- Represents all genes above the horizontal line. To preserve the genes strand and draw genes with *start > end* bellow the line, use the `--preserve-strand` parameter.
- Saves the figure in PDF. Use the `--format` to specify a different one.

Run the following command to show the script help: `docker run --rm -it pegi3s/biopython_utilities plot_gene_distribution.py -h`

You should adapt and run the following command: `docker run --rm -it -v /your/data/dir:/data pegi3s/biopython_utilities plot_gene_distribution.py /data/<input_TSV> -o /data/<output_image>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input TSV file you want to process.
- `<input_TSV>` to the actual name of your input TSV file.
- `<output_image>` to the actual name of your output file (without the extension, which is automatically added by the script).

## Test data

To test this utility, the input NEXUS file is available [here]([here](https://github.com/pegi3s/dockerfiles/tree/master/biopython_utilities/test_data/tree.nex)).

# Changelog

The `latest` tag contains always the most recent version.

## [0.2.0] - 18/10/2021
- Add the `convert_tree.py` utility.

## [0.1.0] - 16/02/2021
- Initial `biopython_utilities` image containing the `plot_gene_distribution.py` utility.

# Building the image

To build this image, the version of the `pegi3s/biopython` image to use as base must be provided. When building from the command line, use `--build-arg biopython_version=1.78`. See the `BUILD.md` for more information.
