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
ENV PATH=/opt/conda/bin:$PATH

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends wget ca-certificates git bzip2; \
    rm -rf /var/lib/apt/lists/*; \
    wget -q https://repo.anaconda.com/miniconda/Miniconda3-py311_24.1.2-0-Linux-x86_64.sh -O /tmp/miniconda.sh; \
    bash /tmp/miniconda.sh -b -p /opt/conda; \
    rm /tmp/miniconda.sh; \
    /opt/conda/bin/conda install -y -c conda-forge -c bioconda repeatmodeler=2.0.9; \
    /opt/conda/bin/conda clean -afy; \
    mkdir -p /opt/conda/share/famdb-3.0.0/Libraries/famdb; \
    wget -q -P /opt/conda/share/famdb-3.0.0/Libraries/famdb https://www.dfam.org/releases/Dfam_4.0/families/FamDB/dfam40.0.h5.gz; \
    wget -q -P /opt/conda/share/famdb-3.0.0/Libraries/famdb https://www.dfam.org/releases/Dfam_4.0/families/FamDB/dfam40.curated.consensus.0.h5.gz; \
    gunzip /opt/conda/share/famdb-3.0.0/Libraries/famdb/dfam40.0.h5.gz /opt/conda/share/famdb-3.0.0/Libraries/famdb/dfam40.curated.consensus.0.h5.gz; \
    git clone https://github.com/Dfam-consortium/RepeatModeler /opt/RepeatModeler

WORKDIR /data
