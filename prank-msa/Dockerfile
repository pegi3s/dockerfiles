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

FROM ubuntu:24.04

ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/prank-msa \
    && wget -qO /tmp/prank.tgz \
       "https://github.com/ariloytynoja/prank-msa/releases/download/v.${VERSION}/prank.linux64.${VERSION}.tgz" \
    && tar -xzf /tmp/prank.tgz -C /opt/prank-msa --strip-components=1 \
    && rm -f /tmp/prank.tgz

ENV PATH="/opt/prank-msa/bin:${PATH}"

ENTRYPOINT ["prank"]
