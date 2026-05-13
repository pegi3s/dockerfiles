
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

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    git \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/ispip

RUN git clone https://github.com/eved1018/ISPIP.git .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY run_ispip_pipeline.sh /usr/local/bin/run_ispip_pipeline.sh

RUN chmod +x /usr/local/bin/run_ispip_pipeline.sh

WORKDIR /data

ENTRYPOINT ["/usr/local/bin/run_ispip_pipeline.sh"]