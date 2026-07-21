#
#   Copyright 2018-2026 Hugo López-Fernández, Miguel Reboiro-Jato, Cristina
#   P. Vieira, and Jorge Vieira
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

RUN apt-get update && apt-get install -y wget gcc

RUN wget "https://github.com/morgannprice/fasttree/archive/refs/tags/v${VERSION}.tar.gz" -O /tmp/fasttree.tar.gz && \
    tar zxvf /tmp/fasttree.tar.gz -C /tmp/ && rm /tmp/fasttree.tar.gz && \
    cd "/tmp/fasttree-${VERSION}" && \
    gcc -O3 -finline-functions -funroll-loops -Wall -o /usr/local/bin/FastTree FastTree.c -lm && \
    rm -rf "/tmp/fasttree-${VERSION}"
