#
#   Copyright 2018-2026 Hugo López-Fernández, Miguel Reboiro-Jato,
#   Cristina P. Vieira, and Jorge Vieira
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

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    cmake \
    git \
    libboost-iostreams-dev \
    libbz2-dev \
    libeigen3-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    mkdir -p /opt/bpp; \
    cd /opt/bpp; \
    for r in bpp-core bpp-seq bpp-phyl bpp-seq-omics bpp-phyl-omics bpp-popgen; do \
        git clone --depth 1 "https://github.com/BioPP/${r}.git"; \
        mkdir "${r}/build"; \
        cd "${r}/build"; \
        cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_TESTING=OFF; \
        make -j"$(nproc)"; \
        make install; \
        cd /opt/bpp; \
    done; \
    ldconfig

RUN set -eux; \
    git clone --depth 1 https://github.com/jydu/maffilter.git /opt/maffilter; \
    mkdir /opt/maffilter/build; \
    cd /opt/maffilter/build; \
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release; \
    make -j"$(nproc)"; \
    make install; \
    ldconfig

WORKDIR /data

ENTRYPOINT ["maffilter"]
