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

FROM ubuntu:24.04

ARG VERSION
ARG MAXK=192
ARG BTLLIB_VERSION=1.7.8

# ABySS >= 2.3 requires btllib, which is not bundled in the ABySS release
# tarball (there is neither a btllib directory nor a git submodule), so btllib
# is built from its own release tarball. Build dependencies are installed and
# purged within this layer to keep the final image small.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3 \
        python3-dev \
        python3-pip \
        meson \
        ninja-build \
        cmake \
        wget \
        ca-certificates \
    && wget -qO /tmp/btllib.tar.gz \
       "https://github.com/BirolLab/btllib/releases/download/v${BTLLIB_VERSION}/btllib-${BTLLIB_VERSION}.tar.gz" \
    && tar -xzf /tmp/btllib.tar.gz -C /opt \
    && cd /opt/btllib-${BTLLIB_VERSION} \
    && ./compile --prefix /opt/btllib \
    && cd / \
    && rm -rf /opt/btllib-${BTLLIB_VERSION} /tmp/btllib.tar.gz /tmp/btllib-build-* \
    && apt-get purge -y --auto-remove \
        build-essential python3-dev python3-pip meson ninja-build cmake wget \
    && rm -rf /var/lib/apt/lists/*

# Build ABySS. Build dependencies are installed and purged within this layer.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        autoconf \
        automake \
        libtool \
        pkg-config \
        wget \
        ca-certificates \
        libboost-dev \
        libopenmpi-dev \
        libsparsehash-dev \
        make \
        openmpi-bin \
        ssh \
        bsdmainutils \
        libgomp1 \
        gzip \
        bzip2 \
        xz-utils \
        perl \
    && wget -qO /tmp/abyss.tar.gz \
       "https://github.com/BirolLab/abyss/releases/download/${VERSION}/abyss-${VERSION}.tar.gz" \
    && tar -xzf /tmp/abyss.tar.gz -C /opt \
    && cd /opt/abyss-${VERSION} \
    && ./configure \
       --with-mpi=/usr/lib/x86_64-linux-gnu/openmpi \
       --with-btllib=/opt/btllib \
       --enable-maxk=${MAXK} \
       --disable-werror \
    && make -j"$(nproc)" install-strip \
    && cd / \
    && rm -rf /opt/abyss-${VERSION} /tmp/abyss.tar.gz \
    && apt-get purge -y --auto-remove \
        build-essential autoconf automake libtool pkg-config wget \
        libboost-dev libopenmpi-dev libsparsehash-dev \
    && rm -rf /var/lib/apt/lists/*
