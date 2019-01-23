FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common

RUN wget https://www.maths.otago.ac.nz/~dbryant/software/PhiPack.tar -O /tmp/PhiPack.tar && \
    tar -xvf /tmp/PhiPack.tar && \
    rm /tmp/PhiPack.tar -f && \
    cd /PhiPack/src && \
    make

ENV PATH="/PhiPack:${PATH}"
