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

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      ca-certificates \
      cmake \
      git \
      libopenmpi-dev \
      openmpi-bin \
    && rm -rf /var/lib/apt/lists/*

RUN git config --global http.sslVerify false \
    && git clone --recursive https://github.com/BenoitMorel/AleRax /opt/AleRax

RUN mkdir -p /opt/AleRax/build \
    && cd /opt/AleRax/build \
    && cmake .. \
        -DCMAKE_BUILD_TYPE=Release \
        -DCORAX_ENABLE_AVX=OFF \
        -DCORAX_ENABLE_AVX2=OFF \
    && make -j"$(nproc)" alerax \
    && cp /opt/AleRax/build/bin/alerax /usr/local/bin/alerax

WORKDIR /data

ENTRYPOINT ["alerax"]
