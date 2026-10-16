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

ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    libssl-dev \
    build-essential \
    libio-socket-ssl-perl \
    libxml-simple-perl \
    && rm -rf /var/lib/apt/lists/*

RUN cd /opt \
    && curl -fsSL "https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/${VERSION}/edirect.tar.gz" | tar xz \
    && cd /opt/edirect \
    && for exc in xtract rchive transmute; do \
        curl -fsSL "https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/${VERSION}/${exc}.Linux.gz" -o "${exc}.Linux.gz" \
        && gunzip -f "${exc}.Linux.gz" \
        && chmod +x "${exc}.Linux"; \
    done

ENV PATH="/opt/edirect:${PATH}"
