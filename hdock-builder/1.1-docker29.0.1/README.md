# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [HDOCK](http://hdock.phys.hust.edu.cn/), a docking software that can be used to predict the binding complexes between two proteins.

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the version `1.1-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `1.1` tag. Starting with version `1.1-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

#### *Note 1*

Because of licensing issues we cannot make available the `hdock` and `createpl` executables. Therefore, they must be obtained from [here](http://huanglab.phys.hust.edu.cn/software/hdocklite/).

After obtaining those files, just put the two executables in a folder and use the following command to create a working docker image called `pegi3s/hdock`: 

`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /your/data/dir:/data pegi3s/hdock-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/hdock"`

#### *Note 2* 

You just need to do this once, unless you erase the `pegi3s/hdock` image from your computer in which case you must repeat this step.

In this command, you should replace:

- `/your/data/dir`  to point to the directory that contains the `hdock` and `createpl` executables.

# Using the HDOCK image in Linux

Once the `pegi3s/hdock` image is created, you can use the following command to run a local instance of the software:

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/hdock bash -c "/exe/hdock /data/PDB1.pdb /data/PDB2.pdb -out /exe/Hdock.out && /exe/createpl /exe/Hdock.out /exe/top100.pdb -nmax 100 -complex -models && mkdir -p /data/output && cp *.pdb /data/output"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB files and the list of binding sites residues (optional) you want to use.
- `<PDB1.pdb>` to the name of the receptor PDB file you want to use.
- `<PDB2.pdb>` to the name of the ligand PDB file you want to use.
- `<output>` to the name of the directory under `/your/data/dir` where the output will be saved. Please note that this variable appears twice in the above command.
  
For instance, using the PDB files provided as test cases, together with the `hdock` and `createpl` executables, you should run:

`docker run --rm -v /your/data/dir:/data pegi3s/hdock bash -c "/exe/hdock /data/1CGI_r_b.pdb /data/1CGI_l_b.pdb -out /exe/Hdock.out && /exe/createpl /exe/Hdock.out /exe/top100.pdb -nmax 100 -complex -models && mkdir -p /data/output && cp *.pdb /data/output"`

In this command, if you only change the `/your/data/dir`, the results will be saved on a folder named `output` under `/your/data/dir`.

To see the `HDOCK` help, just run: `docker run --rm pegi3s/hdock bash -c "/exe/hdock -help"`.

# Using the HDOCK image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

In order to create the `HDOCK` image, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data -v /var/run/docker.sock:/var/run/docker.sock pegi3s/hdock-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/hdock"`

and then run: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/hdock bash -c "/exe/hdock /data/PDB1.pdb /data/PDB2.pdb -out /exe/Hdock.out && /exe/createpl /exe/Hdock.out /exe/top100.pdb -nmax 100 -complex -models && mkdir -p /data/output && cp *.pdb /data/output"`
