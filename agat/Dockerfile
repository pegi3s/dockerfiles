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

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    git \
    perl \
    cpanminus \
    libbio-perl-perl \
    libclone-perl \
    libfile-chdir-perl \
    libgraph-perl \
    liblwp-useragent-determined-perl \
    libstatistics-r-perl \
    libcarp-clan-perl \
    libsort-naturally-perl \
    libfile-share-perl \
    libfile-sharedir-perl \
    libfile-sharedir-install-perl \
    libyaml-perl \
    liblwp-protocol-https-perl \
    libterm-progressbar-perl \
    libparallel-forkmanager-perl \
    libtest-tempdir-perl \
    liblist-moreutils-perl \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/NBISweden/AGAT.git /opt/AGAT \
    && cd /opt/AGAT \
    && perl Makefile.PL \
    && make \
    && make install \
    && rm -rf /opt/AGAT

WORKDIR /data
