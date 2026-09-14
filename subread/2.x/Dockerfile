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

FROM ubuntu:24.04

ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/subread \
    && wget -qO /tmp/subread.tar.gz \
       "https://sourceforge.net/projects/subread/files/subread-${VERSION}/subread-${VERSION}-Linux-x86_64.tar.gz/download" \
    && tar -xzf /tmp/subread.tar.gz -C /opt/subread --strip-components=1 \
       "subread-${VERSION}-Linux-x86_64/bin" \
    && rm -f /tmp/subread.tar.gz

ENV PATH="/opt/subread/bin:/opt/subread/bin/utilities:${PATH}"
