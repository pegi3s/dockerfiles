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

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

ARG GENERAX_COMMIT=e4fab40

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      git \
      ca-certificates \
      bison \
      flex \
      libopenmpi-dev \
      openmpi-bin \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --recursive \
      https://github.com/BenoitMorel/GeneRax \
      /opt/generax \
    && cd /opt/generax \
    && git checkout ${GENERAX_COMMIT} \
    && git submodule update --init --recursive \
    && mkdir build \
    && cd build \
    && cmake .. \
        -DCMAKE_BUILD_TYPE=Release \
        -DCORAX_ENABLE_AVX=OFF \
        -DCORAX_ENABLE_AVX2=OFF \
    && make -j2

ENV PATH="/opt/generax/build/bin:${PATH}"

ENTRYPOINT ["generax"]
