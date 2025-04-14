# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/), a quality control tool for high throughput sequence data.

# Using the FastQC image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/fastqc /data/input.fq`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze.
- `input.fq` to the actual name of your input file.

To see the `FastQC` help, just run `docker run --rm pegi3s/fastqc --help`.

# Running the FastQC GUI in Linux
This docker image can be also used to run the `FastQC` GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/fastqc`

If the above command fails, try running `xhost +` first.

