FROM ubuntu:20.04

ARG VERSION=2.1.0

RUN apt-get update && apt-get upgrade -y && apt-get install -y unzip wget python2.7 && \
    ln -s /usr/bin/python2.7 /usr/bin/python

RUN DOWNLOAD_VERSION=$(echo $VERSION | sed 's/\.//g') && \
    wget https://cloud.biohpc.swmed.edu/index.php/s/hisat2-${DOWNLOAD_VERSION}-Linux_x86_64/download -O /tmp/hisat.zip && \
    unzip /tmp/hisat.zip -d /opt/ && \
    rm /tmp/hisat.zip

ENV PATH="/opt/hisat2-${VERSION}/:/opt/hisat2-${VERSION}/scripts:${PATH}"
