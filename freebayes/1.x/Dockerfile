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

FROM debian:13-slim

ARG VERSION

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
    && curl -fsSL "https://github.com/freebayes/freebayes/releases/download/v${VERSION}/freebayes-${VERSION}-linux-amd64-static.gz" \
        -o /tmp/freebayes.gz \
    && gunzip -c /tmp/freebayes.gz > /usr/local/bin/freebayes \
    && chmod +x /usr/local/bin/freebayes \
    && rm -f /tmp/freebayes.gz \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

COPY rCRS.fasta .

COPY rCRS.fasta.fai .

ENTRYPOINT ["freebayes"]
