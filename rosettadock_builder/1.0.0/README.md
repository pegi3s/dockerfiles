# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [RosettaDock](https://rosettacommons.org/2024/10/29/conda-channel-installation/), a tool to perform protein-protein docking inferences. Because of legal restrictions, we can only provide a docker image that facilitates the building of a functional docker image named pegi3s/rosettadock. Before building the image, please ensure that you have the appropriate licenses to use the RosettaDock software application.

# Building the RosettaDock image in Linux

You should adapt and run the following command: `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock pegi3s/rosettadock_builder bash -c "docker build ./ -t pegi3s/rosettadock:$(date +'%Y-%m-%d')"`

or if you prefer an image with the latest tag: `docker run --rm -v /var/run/docker.sock:/var/run/docker.sock pegi3s/rosettadock_builder bash -c "docker build ./ -t pegi3s/rosettadock:latest"`

# Using the RosettaDock image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir/:/data pegi3s/rosettadock bash -c "rosettadock -s /data/PDBfile -partners A_B -randomize1 -randomize2 -nstruct 100 -ex1 -ex2aro"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the PDB file with the two structures to be used.
- `PDBfile` to the actual name of your PDB file.

This is only one of the many commands that can be invoked. It should be noted that many more than 100 structures should be assessed (defined using the -nstruct parameter), that the name of the two chains should be A and B, and that the two structures should be near each other but without colliding when rotating around each other. A tutorial on the different options that can be used is available [here](https://docs.rosettacommons.org/docs/latest/application_documentation/docking/docking-protocol).

