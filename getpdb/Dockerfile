FROM ubuntu:23.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gzip wget
COPY getpdb /opt
WORKDIR /opt
