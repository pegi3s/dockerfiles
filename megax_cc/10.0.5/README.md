# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [MEGA X CC](https://www.megasoftware.net/web_help_10/MEGA-CC.htm) Command Line, which is particularly useful for iterative and batch analysis of multiple input data files. For a single input data file we recommend the usage of `pegi3s` [MEGA X GUI](https://hub.docker.com/r/pegi3s/megax) docker image.

The Command Line interface requires a special input file called a [MEGA Analysis Options](https://www.megasoftware.net/web_help_10/MEGA_Analysis_Options_File.htm)`(.mao)`file, which specifies the analysis to run as well as the analysis options to use. This `.mao` file can only be created by using the `GUI` interface. We provide an example of a `.mao` file [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/megax_cc/10.0.5/options_menu/infer_NJ_nucleotide.mao). If you intend to generate your own `.mao` file make sure you follow the steps described [here](https://www.megasoftware.net/web_help_10/Running_in_Command-Line_Mode.htm) in the section `Generating the MEGA Analysis Options File`.

To see `megacc` options, just run `docker run --rm pegi3s/megax_cc megacc -h`.

# Using the MEGA X CC image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/megax_cc megacc -a <mao_file> -d <meg_seq_align> -o output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<mao_file>` to the name of the `.mao` file with the analysis options to use.
- `<meg_seq_align> ` to the name of the `.meg` sequence alignment file you want to analyze.

### *Note*
The previous command generates two files:
- `*.nwk`: a newick file with the newly created phylogeny.
- `*_summary.txt`: a text file that contains a summary of the analysis.

For instance, to run the `Phylogeny | Construct/Test Neighbor-Joining Tree` analysis using the `Drosophila_Adh.meg` sequence alignment, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/megax_cc megacc -a /data/infer_NJ_nucleotide.mao -d /data/Drosophila_Adh.meg -o /data/output`

# Test data
To test the previous command, the sequence alignment file used is available [here](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/megax_cc/10.0.5/test_data/Drosophila_Adh.meg).

# Using the MEGA X CC image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/megax_cc megacc -a <mao_file> -d <meg_seq_align> -o output`
