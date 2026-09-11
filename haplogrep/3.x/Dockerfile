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

FROM ubuntu:22.04

ARG VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/haplogrep3 \
    && wget -qO /tmp/haplogrep3.tar.gz \
       "https://github.com/genepi/haplogrep3/releases/download/v${VERSION}/haplogrep3-${VERSION}-linux.tar.gz" \
    && tar -xzf /tmp/haplogrep3.tar.gz -C /opt/haplogrep3 \
    && rm -f /tmp/haplogrep3.tar.gz \
    && chmod +x /opt/haplogrep3/haplogrep3

# Pre-install the phylogenetic trees configured in haplogrep3.yaml so that they
# are not downloaded on every container run.
RUN cd /opt/haplogrep3 && ./haplogrep3 >/dev/null 2>&1 || true

ENV PATH="/opt/haplogrep3:${PATH}"

ENTRYPOINT ["haplogrep3"]
