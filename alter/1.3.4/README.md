# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This images facilitates the usage of [ALTER](https://www.sing-group.org/index.php?option=com_content&view=article&id=66:alter&catid=5:software&Itemid=9) (ALigment Transformation EnviRonment), a public tool for MSA (Multiple Sequence Alignment) file format conversion. It performs a program-oriented conversion between different DNA and protein MSA formats.

# Using the ALTER image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/alter -i /data/input -o /data/output -ia -of <out_format> -oo Linux -op GENERAL`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to align.
- `input` to the actual name of your input file.
- `output` to the actual name of your output file.
- `<out_format>` to the output format you intend to obtain. The allowed standard formats are: ALN, FASTA, GDE, MEGA, MSF, NEXUS, PHYLIP and PIR.

For instance, in order to convert a NEXUS file into a FASTA file, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/alter -i /data/input.nexus -o /data/output.fasta -ia -of FASTA -oo Linux -op GENERAL`

# Test data
To test the previous command, you can copy and paste [this sample data](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/alter/1.3.4/test_data/input.nexus) into the `input`file.

To see the [ALTER](http://sing-group.org/ALTER/) help, just run `docker run --rm pegi3s/alter help`.

# Running the ALTER GUI in Linux
This docker image can be also used to run the ALTER GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/alter `

If the above command fails, try running `xhost +` first.

# Using the ALTER image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/alter -i /data/input -o /data/output -ia -of <out_format> -oo Windows -op GENERAL`
