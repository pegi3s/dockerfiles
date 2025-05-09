# Using our Docker images with Singularity

[Singularity](https://sylabs.io/docs/) is a container platform specially created to run complex applications on HPC clusters in a simple, portable, and reproducible way, with a focus on security. As described [in the documentation](https://sylabs.io/guides/3.5/user-guide/singularity_and_docker.html), Singularity has interoperability with Docker.

This guide demonstrates how to run Docker images from our *Bioinformatics Docker Images Project* using Singularity. To do so, the [`pegi3s/alter`](https://hub.docker.com/r/pegi3s/alter) Docker image in the examples.

## 1. Pulling a Docker image

To pull a public Docker image from Docker Hub, you should run the following command:

```shell
singularity pull docker://pegi3s/alter
```

## 2. Running GUI applications

To run a GUI application, you can simply run the following command (run `xhost +` first if it fail):

```shell
singularity run docker://pegi3s/alter
```

By default, this gives acces to host files since the directories `$HOME`, `/tmp`, `/proc`, `/sys`, and `/dev` are among the system-defined bind points in the default Singularity configuration (read more about this [here](https://singularity.lbl.gov/docs-mount)).

If you want to mount a specific directory, you can do it by using the `-B` parameter as follows:

```shell
singularity run -B /mnt/data:/data docker://pegi3s/alter
```

## 3. Running CLI commands

To run CLI commands, you should simply run the following command:

```shell
singularity run docker://pegi3s/alter -i /home/user/data/input.nexus -o /home/user/data/output_1.fasta -ia -of FASTA -oo Linux -op GENERAL
```

As explained in the previous section, the `$HOME` is automatically mounted in the image in the default configuration and thus it is possible to execute the commands in such way.

If you want to mount a specific directory, you can do it by using the `-B` parameter as follows:

```shell
singularity run -B /mnt/data:/data docker://pegi3s/alter -i /data/input.nexus -o /data/output_2.fasta -ia -of FASTA -oo Linux -op GENERAL
```
