# Creating `alias` in `.bashrc` to be used as shortcut for a (complete) command

`.bashrc` is the configuration file for bash, a linux shell/command interpreter.
An `alias` is a substitute for a (complete) command. It can be thought of as a shortcut. 

This guide demonstrates how to create an `alias` in `.bashrc` to be used as a shortcut for (complete) commands available at the [Bioinformatics Docker Images Project](https://pegi3s.github.io/dockerfiles/).

## 1. Edit the `.bashrc` file

To add the `alias` to the `.bashrc` file, you need to edit the `.bashrc` using a text editor. 
Open the Terminal app and type the following command:

```
gedit ~/.bashrc
```

## 2. Append the `bash` `alias`

Add the `alias` at the bottom of the `.bashrc` file:

```
dockerc() { docker run -v /var/run/docker.sock:/var/run/docker.sock "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -t pegi3s/"$1" ${@:2};}
```

How it should look like:

```
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

dockerc() { docker run -v /var/run/docker.sock:/var/run/docker.sock "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -t pegi3s/"$1" ${@:2};}
```

Note that `"$(pwd)"` is the current working directory from which you are running the command (i.e. the `dockerc` alias). Therefore, data files specified as parameters must be relative and under to this working directory.

## 3. Save and close the file

After saving the file and closin the text editor, the new `alias` will be set for the next shell you start.

## 4. Using the alias: an example

For instance, using `dockerc()` `alias` created at `2.`, you should adapt and run the following command:

```
dockerc <docker_image> <docker_image_parameters>
```

In this command, you should replace:
- `<docker_image>` to the name of the Docker image you intend to use.
- `<docker_image_parameters>` to the respective parameters of the Docker image you are using.

The following example provided runs the `SAMtools-BCFtools` Docker image, which can be pulled [here](https://hub.docker.com/r/pegi3s/samtools_bcftools/), to view a file called `chr11.bam` available in the current working directory.

```
dockerc samtools_bcftools samtools view chr11.bam
```

## Creating an `alias` for GUI-based Docker images

An `alias` can also be used to replace a command that invokes a Docker image that opens a Graphical User Interface (`GUI`).

As shown in `2.`, just add the `alias` at the bottom of the `.bashrc` file:
```
dockergui() { xhost + && docker run -v "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -ti  -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v /var/run/docker.sock:/var/run/docker.sock pegi3s/"$1" ${@:2}; }
```

How it should look like:

```
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

dockergui() { xhost + && docker run -v "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -ti  -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp:/tmp -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v /var/run/docker.sock:/var/run/docker.sock pegi3s/"$1"}
```

For instance, the following command would open the [SEDA](https://hub.docker.com/r/pegi3s/seda/) GUI: `dockergui seda`.