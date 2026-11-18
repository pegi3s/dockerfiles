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

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        wget \
        zlib1g-dev \
        python3 \
        python3-dev \
        python3-pip \
        hmmer \
        ncbi-blast+ \
        augustus \
        metaeuk \
        bbmap \
        prodigal \
        mafft \
        fasttree \
    && rm -rf /var/lib/apt/lists/*

RUN printf '#!/bin/bash\nexec java -ea -Xmx4g -cp /usr/share/java/bbmap.jar jgi.AssemblyStats2 "$@"\n' > /usr/local/bin/stats.sh \
    && chmod +x /usr/local/bin/stats.sh

RUN pip install --no-cache-dir --break-system-packages \
        "numpy==1.26.4" \
        "pandas==2.2.3" \
        "scipy==1.13.1" \
        "biopython==1.84" \
        "matplotlib==3.9.2" \
        "seaborn==0.13.2" \
        "psutil==6.0.0" \
        "pyyaml==6.0.2" \
        "requests==2.32.3"

RUN git clone https://github.com/lh3/miniprot /opt/miniprot \
    && cd /opt/miniprot \
    && make \
    && cp miniprot /usr/local/bin/miniprot \
    && rm -rf /opt/miniprot

RUN git clone https://gitlab.com/ezlab/busco.git /opt/busco \
    && pip install --no-cache-dir --break-system-packages --no-deps /opt/busco

ENV AUGUSTUS_CONFIG_PATH=/usr/share/augustus/config

WORKDIR /data
