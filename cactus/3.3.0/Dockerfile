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

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential git python3 python3-dev python3-pip zlib1g-dev wget ca-certificates libbz2-dev pkg-config \
      libhdf5-dev liblzo2-dev libtokyocabinet-dev liblzma-dev libxml2-dev libssl-dev libpng-dev \
      uuid-dev libcurl4-gnutls-dev libffi-dev python3-virtualenv rsync python-is-python3 \
      libdeflate-dev cmake libjemalloc-dev python3-distutils pybind11-dev autoconf libzstd-dev \
      liblz4-dev libhts-dev libblas-dev liblapack-dev libpcre3-dev gfortran libjansson-dev libboost-dev zstd \
      net-tools time parallel libgomp1 libatomic1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/ComparativeGenomicsToolkit/cactus.git /home/cactus

RUN cd /home/cactus \
    && find /home/cactus -name include.local.mk -exec rm -f {} \; \
    && rm -rf bin/* \
    && make clean -j "$(nproc)" \
    && ./build-tools/downloadPhast \
    && ./build-tools/downloadUcscLib

RUN cd /home/cactus \
    && env ENABLE_PHYLOP=1 ENABLE_UDC=1 KENTSRC=/home/cactus/submodules/kent/src avx2=1 CACTUS_PORTABLE_BUILD=1 make -j "$(nproc)"

ENV avx2=1 \
    CACTUS_PORTABLE_BUILD=1 \
    ENABLE_PHYLOP=1 \
    ENABLE_UDC=1 \
    KENTSRC=/home/cactus/submodules/kent/src

RUN cd /home/cactus/bin \
    && for i in wigToBigWig faToTwoBit bedToBigBed bigBedToBed axtChain pslPosTarget bedSort hgGcPercent mafToBigMaf hgLoadMafSummary hgLoadChain genePredSingleCover gff3ToGenePred gtfToGenePred; do \
        wget -nv "http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/${i}" || \
        wget -nv --no-check-certificate "https://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/${i}"; \
        chmod ugo+x "${i}"; \
       done \
    && cd /home/cactus && ./build-tools/downloadPangenomeTools \
    && cd /home/cactus && ./build-tools/downloadMafTools \
    && cd /home/cactus/bin && rm -f *test *tests *Test *Tests \
    && /bin/bash -O extglob -c "cd /home/cactus && strip -d bin/!(cactus_consolidated) 2> /dev/null || true"

RUN cd /home/cactus \
    && python3 -m virtualenv -p python3 cactus_env \
    && . cactus_env/bin/activate \
    && python3 -m pip install -U --no-cache-dir setuptools pip \
    && python3 -m pip install -U --no-cache-dir -r ./toil-requirement.txt \
    && python3 -m pip install -U --no-cache-dir . \
    && rm -rf /home/cactus/hal_lib \
    && rsync -avm --include='*.py' -f 'hide,! */' /home/cactus/submodules/hal /home/cactus/hal_lib

RUN mkdir -p /opt/cactus \
    && cp /home/cactus/runtime/wrapper.sh /opt/cactus/wrapper.sh \
    && chmod 777 /opt/cactus/wrapper.sh \
    && mkdir -p /data \
    && mkdir -p /home/cactus_user && chmod 777 /home/cactus_user

ENV PATH="/home/cactus/cactus_env/bin:/home/cactus/bin:${PATH}"
ENV PYTHONPATH="/home/cactus"
ENV LD_LIBRARY_PATH="/home/cactus/lib:${LD_LIBRARY_PATH}"
ENV CACTUS_LOG_MEMORY=1
ENV CACTUS_INSIDE_CONTAINER=1
ENV HOME="/home/cactus_user"

WORKDIR /data
