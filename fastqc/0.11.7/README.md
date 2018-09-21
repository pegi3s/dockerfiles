# Using the fastqc image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/fastqc /data/input.fq`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTQ file you want to analyze.
- `input.fq` to the actual name of your input file.

To see the [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) help, just run `docker run --rm pegi3s/fastqc --help`.

# Running the fastqc GUI in Linux
This docker image can be also used to run the fastqc GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/fastqc`

If the above command fails, try running `xhost +` first.

# Test data
To test the previous command, you can download [this fastq compressed file](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?cmd=dload&run_list=SRR1654650&format=fastq) (1.1GB). Note that it does not need to be descompressed as `fastqc` can deal with both compressed and uncompressed fastq files. 

In the previous command you just need to replace `/data/input.fq` with `/data/sra_data.fastq.gz`. You can also speed up the execution by adding `t 4` to tell `fastqc` to use 4 cores (it uses 1 core by default). This command will produce two files containing the `fastqc` reports in the `/data` directory: `sra_data_fastqc.html` and `sra_data_fastqc.zip`.

# Using the fastqc image in Windows

Please, note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/fastqc /data/input.fq`
