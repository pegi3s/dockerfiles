FROM scottyhardy/docker-wine

WORKDIR /wineuser

RUN usermod -d /wineuser wineuser

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y mono-complete

RUN chown wineuser:wineuser /wineuser

ENV WINEDEBUG=-all

ENTRYPOINT ["/usr/bin/entrypoint"]
CMD ["/bin/bash"]

# Enter the Docker image and run the following commands:
# winecfg && winetricks -q dotnet45 && winetricks vb6run
# wine DnaSP_v61203_x64.exe
