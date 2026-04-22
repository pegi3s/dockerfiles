FROM ubuntu:24.04

ARG IQTREE_VERSION=3.1.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    tar \
    libgomp1 \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/iqtree3 \
    && wget -qO /tmp/iqtree.tar.gz \
       https://github.com/iqtree/iqtree3/releases/download/v${IQTREE_VERSION}/iqtree-${IQTREE_VERSION}-Linux-intel.tar.gz \
    && tar -xzf /tmp/iqtree.tar.gz -C /opt/iqtree3 --strip-components=1 \
    && rm -f /tmp/iqtree.tar.gz

ENV PATH="/opt/iqtree3/bin:${PATH}"

WORKDIR /data

