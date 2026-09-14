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

FROM continuumio/miniconda3:26.5.3

ARG VERSION

RUN conda create -y -n bioconvert -c bioconda -c conda-forge \
        "python=3.12" \
        "bioconvert=${VERSION}" \
    && conda clean -afy

ENV PATH="/opt/conda/envs/bioconvert/bin:${PATH}"

ENTRYPOINT ["bioconvert"]
