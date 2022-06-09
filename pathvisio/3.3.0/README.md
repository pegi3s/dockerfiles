# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

# Using the PathVisio image in Linux
Please note that the following instructions must be executed in Linux environments only.

You should adapt and run the following command: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp -v /your/data/dir:/data pegi3s/pathvisio bash -c "java -jar pathvisio.jar"`

If the above command fails, try running `xhost +` first. In this command, you should replace:
- `/your/data/dir` to point to the directory that you want to have available at `PathVisio`.

### *Note*
The `/your/data/dir` folder must not have any file name with special characters.

Running this command opens the [PathVisio](https://pathvisio.org/) Graphical User Interface. Your data directory will be available through the file browser at `/data`.

# Test data

To test the previous commands, the `Kennedy Pathway` GPML file obtained from [WikiPathways](https://www.wikipathways.org/instance/WP1771) is available [here](https://github.com/pegi3s/dockerfiles/tree/master/pathvisio/3.3.0/test_data/WP1771_107199.gpml).
