FROM continuumio/miniconda3:24.9.2-0

ARG VERSION

SHELL ["/bin/bash","-l", "-c"]

RUN apt-get update && apt-get upgrade -y && apt-get install -y g++

RUN pip install HTSeq==${VERSION}
