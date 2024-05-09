

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

[Newick Utilities](https://gensoft.pasteur.fr/docs/newick-utils/1.6/nwutils_tutorial.pdf) are a set of UNIX (including Mac OS X) and UNIX-like (Cygwin) shell programs for working with phylogenetic trees.

# Using the newick_utils image in Linux

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/newick_utils bash -c "your_command"`

In this command, you should replace:
- `/your/data/dir` to point to the working directory.
- `your_command` to the Newick Utilities command you want to perform.

For instance, for displaying a newick tree file as an svg image, change `your_command` to `nw_display -s /data/file_name > /data/file_name.svg`

where:
- `file_name` is the name of the newick file you want to process.
