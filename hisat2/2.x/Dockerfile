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

FROM ubuntu:20.04

ARG VERSION=2.2.3

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y wget python3 make g++ zlib1g-dev libtbb-dev && \
    ln -s /usr/bin/python3 /usr/bin/python

RUN wget "https://github.com/DaehwanKimLab/hisat2/archive/refs/tags/v${VERSION}.tar.gz" -O /tmp/hisat.tar.gz && \
    tar zxvf /tmp/hisat.tar.gz -C /opt/ && \
    rm /tmp/hisat.tar.gz && \
    cd "/opt/hisat2-${VERSION}" && \
    make -j$(nproc)

ENV PATH="/opt/hisat2-${VERSION}/:/opt/hisat2-${VERSION}/scripts:${PATH}"
