This image facilitates the usage of [`T-Coffee`](http://www.tcoffee.org/Projects/tcoffee/index.html), a multiple sequence alignment package. T-Coffee is used to align sequences or to combine the output of alignment methods (Clustal, Mafft, Probcons, Muscle, etc.) into one unique alignment (M-coffee). Please note that these alignment methods are not included in this image. 
T-Coffee can align Protein, DNA and RNA sequences. It is also able to combine sequence information with protein structural information (Expresso), profile information (PSI-Coffee) or RNA secondary structures (R-Coffee).

# Using T-Coffee image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/tcoffee t_coffee /data/input -run_name /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to analyze.
- `input` to the actual name of your input file.
- `data` to the actual name of the directory where output files will be created.
- `output` to the actual name of your output file.

*Note*: When aligning, T-Coffee will always at least generate three output files:
- `output.aln`: Multiple Sequence Alignment (ClustalW format by default).
- `output.dnd`: guide tree (Newick format).
- `output.html`: colored MSA according to consistency (html format).

To see T-Coffee general parameters help, you just need to run: `docker run --rm pegi3s/tcoffee t_coffee -help`. To obtain the help of a specific parameter, just run: `docker run --rm pegi3s/tcoffee t_coffee -help -<tcoffee-parameter-name>` (e.g. `docker run --rm pegi3s/tcoffee -help -align`)

# Using T-Coffee image in Windows

Please, note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/tcoffee t_coffee /data/input -run_name /data/output`