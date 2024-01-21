FROM ubuntu:23.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y gzip wget
COPY getditasserpdb /opt
WORKDIR /opt
