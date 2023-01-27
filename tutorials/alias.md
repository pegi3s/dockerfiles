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
dockerc() { docker run -v "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -t pegi3s/"$1" ${@:2};}
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

dockerc() { docker run -v "$(pwd)":/data -w /data -u "$(id -u)":"$(id -g)" --rm -t pegi3s/"$1" ${@:2};}
```

## 3. Save and close the file

## 4. Quit the editor

The new `alias` will be set for the next shell you start.

## Example

For instance, using `dockerc()` `alias` created at `2.`, you should adapt and run the following command:

```
dockerc <docker_image> <docker_image_parameters>
```

In this command, you should replace:
- `<docker_image>` to the name of the Docker image you intend to use.
- `<docker_image_parameters>` to the respective parameters of the Docker image you are using.

E.g.:

```
dockerc samtools samtools view chr11.bam
```
