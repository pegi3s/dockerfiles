FROM ubuntu:22.04

ARG COMMIT

RUN apt-get update
RUN apt-get -y upgrade 
RUN apt-get install -y git pip

WORKDIR /opt

RUN git clone https://github.com/pegi3s/cport.git && \
    cd cport && \
    pip install . 

WORKDIR /


