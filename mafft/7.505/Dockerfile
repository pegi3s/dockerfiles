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

FROM debian:stable-slim

# Update commands and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/mafft

# Download and extract MAFFT
RUN wget -q https://mafft.cbrc.jp/alignment/software/mafft-7.505-with-extensions-src.tgz \
    && tar xzf mafft-7.505-with-extensions-src.tgz 

# Compile MAFFT    
RUN cd mafft-7.505-with-extensions/core/ \   
    && make clean \
    && make \
    && make install \
    && cd ../extensions/ \
    && make clean \
    && make \
    && make install \
    && cd ../../ \
    && rm -rf mafft-7.505-with-extensions/ 

# General clear
RUN apt-get remove --purge -y build-essential wget \
    && apt-get autoremove -y \
    && apt-get clean
