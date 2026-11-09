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
        bioperl \
        build-essential \
        ca-certificates \
        cpanminus \
        git \
        libexpat1-dev \
        libfile-which-perl \
        libjson-perl \
        liblist-moreutils-perl \
        liblwp-protocol-https-perl \
        libwww-perl \
        mash \
        quicktree \
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN cpanm --notest Bio::Sketch::Mash Bio::Kmer@0.26

RUN git clone https://github.com/lskatz/mashtree /opt/mashtree \
    && cd /opt/mashtree \
    && perl Makefile.PL \
    && make \
    && make install \
    && rm -rf /opt/mashtree

WORKDIR /data

ENTRYPOINT ["mashtree"]
