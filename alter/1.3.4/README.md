# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the ALTER image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/alter -i /data/input -o /data/output.fasta -ia -of FASTA -oo Linux -op GENERAL`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the FASTA file you want to align.
- `input` to the actual name of your input file.
- `output.fasta` to the actual name of your output file.

To see the [ALTER](http://sing-group.org/ALTER/) help, just run `docker run --rm pegi3s/alter help`.

# Running the ALTER GUI in Linux
This docker image can be also used to run the ALTER GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/alter `

If the above command fails, try running `xhost +` first.

# Test data
To test the previous command, you can copy and paste [this sample data](https://github.com/pegi3s/dockerfiles/blob/master/alter/1.3.4/test_data/input.nexus) into the `input`file.

# Using the ALTER image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/alter -i /data/input -o /data/output.fasta -ia -of FASTA -oo Linux -op GENERAL`
