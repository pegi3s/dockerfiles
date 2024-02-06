FROM debian:stable-slim

# Update commands and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        patch \
        libstdc++5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/probcons

# Download and extract PROBCONS
RUN wget -q http://probcons.stanford.edu/probconsRNA.tar.gz \
    && tar -xzf probconsRNA.tar.gz \
    && rm probconsRNA.tar.gz

# Give permissions to PROBCONS_RNA
RUN cd /opt/probcons/probconsRNA \
    && chmod 777 * && mv probcons /usr/local/bin

WORKDIR /usr/local/bin
