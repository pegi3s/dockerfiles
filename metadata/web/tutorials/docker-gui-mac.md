# Running GUI applications from our Docker images on macOS

Docker Desktop allows you to run our Bioinformatics Docker Images on macOS. However, running graphical applications requires additional configuration because Linux containers cannot directly access the macOS graphical environment.

This guide explains how to run graphical applications from our Docker images using [XQuartz](https://www.xquartz.org/), an X11 server for macOS.

## 1. Install XQuartz

If you have not installed XQuartz yet, you can install it using Homebrew:

```shell
brew install --cask xquartz
```

Once the installation is complete, open XQuartz:

```shell
open -a XQuartz
```

## 2. Configure XQuartz

Note that the only visual change when you open XQuartz is the macOS **Menu Bar** (the top bar with the Apple logo). XQuartz options are accessed from that menu.

Follow these steps to configure XQuartz:

- Open XQuartz and, from the **Menu Bar**, navigate to **XQuartz → Settings... → Security**.
- Enable the **Allow connections from network clients** option.
- Close and reopen XQuartz for the changes to take effect. If necessary, log out of macOS and log in again.

Remember to keep XQuartz running while using graphical applications from Docker containers.

## 3. Prepare a directory for your data

Create a directory to store the input and output files that you want to access from the Docker containers:

```shell
mkdir -p "$HOME/Documents/Docker"
```

Place your input files in this directory. The following examples assume that this directory will be mounted inside the container at `/data`.

## 4. Allow local connections to the X11 server

Open a macOS Terminal and run:

```shell
/opt/X11/bin/xhost +localhost
```

This allows local connections to the X11 server.

**Important:** You must run this command **every time XQuartz is closed and reopened**, not just once. Even if it was run in a previous session, reopening XQuartz requires running it again.

## 5. Run a graphical Docker application

Once XQuartz is running and configured, you can launch a graphical application from a Docker container.

For example, to run the graphical interface of SEDA, execute the following command in the macOS Terminal:

```shell
docker run --rm -ti \
  --platform linux/amd64 \
  -e USERID=$(id -u) \
  -e USER=$(whoami) \
  -e DISPLAY=host.docker.internal:0 \
  -v "$HOME/Documents/Docker:/data" \
  pegi3s/seda:1.7.5-docker29.0.1
```

This command:

- Specifies the `linux/amd64` architecture used by the image.
- Sets the user-related environment variables.
- Configures the display so that the application can connect to XQuartz running on macOS.
- Mounts the local `Documents/Docker` directory at `/data` inside the container, allowing the application to access input files and save output files.

The SEDA graphical interface should now open on your macOS desktop.

You can adapt this command to run other graphical applications available in our [Bioinformatics Docker Images Project](https://bdip.i3s.up.pt/). Replace the image name and tag with those of the application you want to run, and check its documentation for any additional parameters or mounted directories it requires.

**Note for Apple Silicon users:** The pegi3S images used in this example are built for `linux/amd64`. Docker Desktop can run them on Apple Silicon through emulation, but performance and compatibility may vary.

### 5.1 Running Docker in Docker

Some graphical applications, such as SEDA, need to run Docker commands themselves, for example to launch sibling containers that execute their tools. On macOS, this requires exposing the Docker Desktop daemon to the container and configuring the Docker client inside it. The complete command for SEDA is:

```shell
docker run --rm -ti \
  --platform linux/amd64 \
  -e USERID=$(id -u) \
  -e USER=$(whoami) \
  -e DISPLAY=host.docker.internal:0 \
  -e DOCKER_HOST=unix:///var/run/docker.sock \
  -e DOCKER_API_VERSION=1.43 \
  -v "$HOME/Documents/Docker:/data" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  pegi3s/seda:1.7.5-docker29.0.1
```

This command adds the following options to the example above:

- `-v /var/run/docker.sock:/var/run/docker.sock` exposes the Docker Desktop daemon to the container. Use `/var/run/docker.sock`, not the socket path of the active Docker context.
- `-e DOCKER_HOST=unix:///var/run/docker.sock` tells the Docker client inside the container where to connect.
- `-e DOCKER_API_VERSION=1.43` sets the API version used by the client. Adjust or omit it depending on the API version supported by your Docker Desktop daemon.

XQuartz must be running and `/opt/X11/bin/xhost +localhost` must have been executed since the last time XQuartz was started. The Docker-in-Docker on macOS tutorial describes the full configuration and troubleshooting.

## 6. Troubleshooting

If the graphical application does not open, check the following:

- **XQuartz is running.** Open it with `open -a XQuartz` if necessary.
- **Network client connections are enabled.** Check the XQuartz security settings.
- **The X11 access permissions are configured.** Run `/opt/X11/bin/xhost +localhost` in the macOS Terminal. Remember to run it again every time XQuartz is closed and reopened.
- **The display variable is set correctly.** The Docker command must include `-e DISPLAY=host.docker.internal:0`.
- **Docker Desktop is running.** Test the Docker installation with `docker run hello-world`.

If the application still fails to start, check the error messages printed in the Terminal and consult the documentation for the specific Docker image.

For further information about installing Docker on macOS, see our [Docker installation instructions](https://bdip.i3s.up.pt/getting-started#install-docker).

## 7. Uninstall XQuartz

If you no longer need XQuartz, you can uninstall it like any other application: open the Finder, go to **Applications**, find **XQuartz** and drag it to the Trash.

Alternatively, you can uninstall it from the macOS Terminal:

```shell
# 1. Close XQuartz
osascript -e 'tell application "XQuartz" to quit'

# 2. Uninstall XQuartz via Homebrew
brew uninstall --cask xquartz

# 3. Check that it has been uninstalled
ls -d /Applications/Utilities/XQuartz.app 2>/dev/null || echo "XQuartz uninstalled"
```

---

**Compatibility note:** This procedure was tested on a MacBook Pro with an Apple M4 processor running macOS 26.2, using the `pegi3s/seda:1.7.5-docker29.0.1` image and the graphical interface opened successfully. Running Docker containers from within the SEDA image (Docker in Docker) was also tested successfully using the configuration described in section 5.1. However, compatibility with other macOS versions, Docker images, and Apple Silicon configurations cannot be guaranteed.
