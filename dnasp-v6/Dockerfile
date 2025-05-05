#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
#   Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

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
