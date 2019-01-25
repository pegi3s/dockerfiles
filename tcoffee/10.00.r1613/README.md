# Building the `t-coffee` image for the `10.00.r1613` version:

The `t-coffee` image for the [`10.00.r1613`](http://tcoffee.org/Packages/Stable/Version_10.00.r1613/linux/) version must be created manually following the steps described [here](https://tcoffee.readthedocs.io/en/latest/tcoffee_installation.html#unix-linux) (it is created from the `pegi3s/tcoffee:11.00.8` to reutilize the t-coffee dependencies that are already installed there).

First, run the following commands:

```bash
docker run --rm -it pegi3s/tcoffee:11.00.8 bash
apt remove t-coffee
cd /tmp
apt-get update && apt-get install -y wget
wget http://tcoffee.org/Packages/Stable/Version_10.00.r1613/linux/T-COFFEE_installer_Version_10.00.r1613_linux_x64.bin
chmod u+x T-COFFEE_installer_Version_10.00.r1613_linux_x64.bin

# Follow the wizard steps untill t-coffee is installed
./T-COFFEE_installer_Version_10.00.r1613_linux_x64.bin

ln -s /root/tcoffee/Version_10.00.r1613/bin/t_coffee /usr/bin/t_coffee
t_coffee -version
```

Now, without exiting the previous docker container, open a new terminal and run `docker ps -a` to see the container id:
```
CONTAINER ID        IMAGE                          COMMAND             CREATED             STATUS              PORTS                    NAMES
ef3905fc73b8        ubuntu:18.04                   "bash"              5 minutes ago       Up 5 minutes                                 naughty_chatelet
```

Commit this container with t-coffee installed into a new image:
```bash
docker commit ef3905fc73b8 pegi3s/tcoffee:10.00.r1613
```

Check that the new created image works by running `docker run --rm pegi3s/tcoffee:10.00.r1613 t_coffee -version`.

Upload it to Docker Hub by running `docker push pegi3s/tcoffee:10.00.r1613` (this command requires running `docker login` before).

And finally, go back to the container terminal and run `exit` to leave the container.
