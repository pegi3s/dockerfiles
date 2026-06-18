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

FROM continuumio/miniconda3:24.4.0-0

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

RUN conda install -c conda-forge -c bioconda -y \
    python=3.9 \
    biopython=1.79 \
    python-igraph=0.8.3 \
    leidenalg=0.8.3 \
    numpy=1.20.1 \
    pandas=1.2.2 \
    scipy=1.6.0 \
    mash=2.2.2 \
    mmseqs2=12.113e3 && \
    rm -rf /opt/conda/pkgs/*

RUN git clone https://github.com/phglab/ALFATClust /opt/alfatclust && \
    ln -s /opt/alfatclust/main/alfatclust.py /usr/local/bin/alfatclust

WORKDIR /home/work
CMD ["/bin/bash"]
