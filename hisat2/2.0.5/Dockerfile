FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && apt-get install -y unzip wget python2.7 && \
    ln -s /usr/bin/python2.7 /usr/bin/python

RUN wget https://cloud.biohpc.swmed.edu/index.php/s/hisat2-205-Linux_x86_64/download -O /tmp/hisat.zip && \
    unzip /tmp/hisat.zip -d /opt/ && \
    rm /tmp/hisat.zip

ENV PATH="/opt/hisat2-2.0.5/:/opt/hisat2-2.0.5/scripts:${PATH}"
