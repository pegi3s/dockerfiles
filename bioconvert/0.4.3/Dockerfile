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

FROM continuumio/miniconda3:4.10.3

RUN conda update --yes conda && \
    conda install python=3.6 -y  && \
    conda config --add channels r && \
    conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda update -n base -c defaults conda -y && \
    conda update --all -y && \
    conda install python=3.6 mosdepth perl gotree goalign -y 

ADD resources/requirements.txt /resources/requirements.txt
ADD resources/requirements_tools.txt /resources/requirements_tools.txt

RUN conda install --yes --file /resources/requirements.txt && \
    conda install --yes --file /resources/requirements_tools.txt

RUN python3.6 -m pip install pypandoc && \
    python3.6 -m pip install bioconvert==0.4.3  && \
    python3.6 -m pip install --upgrade colorlog easydev

ENTRYPOINT ["bioconvert"]
