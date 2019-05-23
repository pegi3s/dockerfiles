# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [WHISCY](https://github.com/haddocking/whiscy) (WHat Information does Surface Conservation Yield?), a program to predict protein-protein interfaces. It is primarily based on conservation, but it also takes into account structural information. A sequence alignment is used to calculate a prediction score for each surface residue of your protein.

# Using the WHISCY image in Linux

### *Step 1*

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/whiscy whiscy_setup.py /data/input.pdb <chain-protein>`

In this command, you should replace:
- `your/data/dir` to point to the directory that contains the input PDB file you want to analyze.
- `input.pdb` to the actual name of your input PDB file.
- `<chain-protein>` to the name of the chain protein you want to use.

For instance, to use chain A of a particular protein, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/whiscy whiscy_setup.py /data/input.pdb A`

To see the `whiscy_setup.py` help, just run `docker run --rm pegi3s/whiscy whiscy_setup.py --help`

### *Step 2*

After chain protein files are generated in `Step 1` you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/whiscy whiscy_protocol.sh /data/input_chainprotein`

In this command, you should replace:
- `your/data/dir` to point to the directory that contains the input chain protein files you want to analyze.
- `input_chainprotein` to the actual name of your input file and its chain protein.

For instance, to use chain A files of a particular protein after `Step 1`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/whiscy whiscy_protocol.sh /data/input_A`

# Using the WHISCY image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

*Step 1*

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/whiscy whiscy_setup.py /data/input.pdb <chain-protein>`

*Step 2*

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/whiscy whiscy_protocol.sh /data/input_chainprotein`
