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
