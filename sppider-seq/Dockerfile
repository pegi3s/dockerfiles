
#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira,
#   Miguel Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
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

# LABEL contributor="pegi3s"

FROM ubuntu:24.04

LABEL description="SPPIDER-seq: Sequence-based partner-aware prediction of protein-protein interaction sites"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    git \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages \
    torch \
    transformers \
    biopython \
    statsmodels \
    scipy \
    numpy \
    matplotlib \
    ipywidgets \
    ipython

RUN git clone https://github.com/aporollo-lab/SPPIDER-seq.git /opt/SPPIDER-seq

COPY sppider_seq.py /opt/SPPIDER-seq/notebooks/sppider_seq.py
COPY scramble_fasta.py /opt/SPPIDER-seq/notebooks/scramble_fasta.py
COPY alanine_scanning.py /opt/SPPIDER-seq/notebooks/alanine_scanning.py
COPY amplify_sequence_signal.py /opt/SPPIDER-seq/notebooks/amplify_sequence_signal.py
COPY run_sppider_seq.py /usr/local/bin/run_sppider_seq.py

RUN chmod +x /usr/local/bin/run_sppider_seq.py

WORKDIR /data

ENTRYPOINT ["python3", "/usr/local/bin/run_sppider_seq.py"]
CMD ["--help"]