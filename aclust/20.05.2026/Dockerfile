#
#   Copyright 2018-2026 Hugo López-Fernández, Pedro M. Ferreira, Miguel
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

FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        make \
        libc-dev \
        git \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/GarryGippert/Aclust.git /opt/Aclust && \
    cd /opt/Aclust/src && \
    make && \
    install -m 755 aclust /usr/local/bin/ && \
    install -m 755 bclust /usr/local/bin/

WORKDIR /data

ENTRYPOINT ["aclust"]
CMD ["-h"]
