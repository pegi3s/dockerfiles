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

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh

ENV PATH=/opt/conda/bin:$PATH

RUN conda create -y -n scannet python=3.6.12

SHELL ["conda", "run", "-n", "scannet", "/bin/bash", "-c"]

RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    h5py==2.10.0 \
    keras==2.2.5 \
    tensorflow==1.14.0 \
    biopython==1.78 \
    numba==0.52.0 \
    pandas==1.1.5 \
    scipy==1.5.4 \
    matplotlib==3.3.3 \
    scikit-learn==0.24.2 \
    ipywidgets==7.5.1 \
    ipywebrtc==0.5.0 \
    pythreejs

RUN git clone https://github.com/jertubiana/ScanNet /opt/ScanNet

COPY Visualize_spatio_chemical_filters.py /usr/local/bin/Visualize_spatio_chemical_filters.py
COPY main.py /usr/local/bin/main.py

CMD ["conda", "run", "--no-capture-output", "-n", "scannet", "python3", "/usr/local/bin/main.py"]
