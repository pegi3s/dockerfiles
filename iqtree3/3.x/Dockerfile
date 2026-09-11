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

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    tar \
    libgomp1 \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/iqtree3 \
    && wget -qO /tmp/iqtree.tar.gz \
       https://github.com/iqtree/iqtree3/releases/download/v${VERSION}/iqtree-${VERSION}-Linux-intel.tar.gz \
    && tar -xzf /tmp/iqtree.tar.gz -C /opt/iqtree3 --strip-components=1 \
    && rm -f /tmp/iqtree.tar.gz

ENV PATH="/opt/iqtree3/bin:${PATH}"

WORKDIR /data
