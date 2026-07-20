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

FROM debian:12-slim

ARG VERSION

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/mafft

RUN wget -q "https://mafft.cbrc.jp/alignment/software/mafft-${VERSION}-with-extensions-src.tgz" \
    && tar xzf "mafft-${VERSION}-with-extensions-src.tgz"

RUN cd "mafft-${VERSION}-with-extensions/core/" \
    && make clean \
    && make \
    && make install \
    && cd ../extensions/ \
    && make clean \
    && make \
    && make install \
    && cd ../../ \
    && rm -rf "mafft-${VERSION}-with-extensions/"

RUN apt-get remove --purge -y build-essential wget \
    && apt-get autoremove -y \
    && apt-get clean
