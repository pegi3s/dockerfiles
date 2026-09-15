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

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        unzip \
        wget \
        ca-certificates \
        zlib1g-dev \
        libblas-dev \
        libcurl4-openssl-dev \
        openmpi-bin \
        libopenmpi-dev \
        libgomp1 \
    && wget -qO /tmp/hyphy.zip \
       "https://github.com/veg/hyphy/archive/refs/tags/${VERSION}.zip" \
    && unzip -q /tmp/hyphy.zip -d /opt \
    && cd /opt/hyphy-${VERSION} \
    && cmake . \
    && make -j"$(nproc)" install \
    && cd / \
    && rm -rf /opt/hyphy-${VERSION} /tmp/hyphy.zip \
    && apt-get purge -y --auto-remove build-essential cmake unzip wget \
    && rm -rf /var/lib/apt/lists/*
