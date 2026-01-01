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

FROM alpine:latest

ARG SAMTOOLS_VERSION=1.22
ARG BCFTOOLS_VERSION=1.22

RUN apk add --no-cache \
    build-base \
    bzip2 \
    curl \
    autoconf \
    automake \
    libtool \
    zlib-dev \
    xz-dev \
    ncurses-dev \
	bzip2-dev \
	libcurl \
	curl-dev

WORKDIR /build

RUN curl -L -o samtools.tar.bz2 https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
    tar -xjf samtools.tar.bz2 && \
    cd samtools-${SAMTOOLS_VERSION} && \
    ./configure --prefix=/opt/samtools --enable-libcurl && \
    make && make install && \
    cd .. && rm -rf samtools*

RUN curl -L -o bcftools.tar.bz2 https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 && \
    tar -xjf bcftools.tar.bz2 && \
    cd bcftools-${BCFTOOLS_VERSION} && \
    ./configure --prefix=/opt/bcftools && \
    make && make install && \
    cd .. && rm -rf bcftools*

ENV PATH="/opt/samtools/bin:/opt/bcftools/bin:${PATH}"

WORKDIR /
