# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [PyDock3](https://life.bsc.es/pid/pydock/), a software that facilitates the usage of `zdock` and `ftdock` protein-protein docking software.

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the version `3.2.3-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `3.2.3` tag. Starting with version `3.2.3-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

#### *Note 1*

Because of licensing issues we cannot make available `PyDock3` or `zdock` files. Therefore, they must be obtained from [https://life.bsc.es/pid/pydock/get_pydock.html](https://life.bsc.es/pid/pydock/get_pydock.html) and [https://zdock.umassmed.edu/software/](https://zdock.umassmed.edu/software/) respectively.

After obtaining the `pyDock3.tgz` and `zdock3.0.2_linux_x64.tar.gz` files, just put it in a empty folder and use the following command to create a working docker image called `pegi3s/pydock3`:

`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/pydock3-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/pydock3"`

#### *Note 2* 

You just need to do this once, unless you erase the `pegi3s/pydock3` image from your computer in which case you must repeat this step.

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the `pyDock3.tgz` and `zdock3.0.2_linux_x64.tar.gz` files.

# Using the PyDock3 image in Linux

Once the `pegi3s/pydock3` image is created, you can use the following commands to run `zdock`, `ftdock` and several other `ftdock` utilities:

# zdock

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_zdock project_name number_of_solutions best_PDB restraint"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB and .ini files (see test data for an example of a .ini file).
- `project_name` to the project name that is the same as the name of the .ini file.
- `number_of_solutions` to the number of solutions to be analysed (recommended: `100`; this number must be smaller or equal to `2000`).
- `best_PDB` to the number of the best solutions to be obtained (recommended: `5`).
- `restraint` to `R` or `r` if restrainsts are declared in the .ini file. Any other value if restraints are not declared.

#### *Note 3*

In the `run_zdock` script, `zdock` is invoked using `zdock -o project_name.zdock -R project_name_rec.pdb.H -L project_name_lig.pdb.H` and not `pyDock3 project_name zdock`, because the latter command requires the `libg2c.so.0` library that can only be installed in Ubuntu versions older than the oldest one available in DockerHub (`Ubuntu 14.04`).

# ftdock

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_ftdock project_name number_of_solutions best_PDB restraint"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB and .ini files  (see test data for an example of a .ini file).
- `project_name` to the project name that is the same as the name of the .ini file.
- `number_of_solutions` to the number of solutions to be analysed (recommended: `100`; this number must be smaller or equal to `10000`).
- `best_PDB` to the number of best solutions to be obtained (recommended: `5`).
- `restraint` to `R` or `r` if restrainsts are declared in the .ini file. Any other value if restraints are not declared.
	
#### *Note 4*

In the `run_ftdock` script, `ftdock` is invoked using `ftdock -static project_name_rec.pdb -mobile project_name_lig.pdb > output` and not `pyDock3 project_name zdock`, because the latter command requires the `libg2c.so.0` library that can only be installed in Ubuntu versions older than the oldest one available in DockerHub (`Ubuntu 14.04`).

# change chain ID

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_change_chain_ID PDB old new"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB file to be processed.
- `PDB` to the PDB file name.
- `old` to the old chain name.
- `new` to the new chain name.
	
# Remone non-standard and hydrogen atoms

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_preprocess PDB"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB file to be processed.
- `PDB` to the PDB file name.

# Optimal Docking Area (ODA) analysis / Interface prediction from protein surface desolvation energy

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_ODA PDB"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB file to be processed.
- `PDB` to the PDB file name.
	
# Test data

To test the previous commands, download the test data available [here](https://github.com/pegi3s/dockerfiles/tree/master/pydock3-builder/3.0/test_data/) and then run:

`docker run --rm -v /your/data/dir:/data pegi3s/pydock3 bash -c "./run_zdock test 100 5 R"`

# Using the PyDock3 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

In order to create the `PyDock3` image, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data -v /var/run/docker.sock:/var/run/docker.sock pegi3s/pydock3-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/pydock3"`
