FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y curl libssl-dev build-essential libio-socket-ssl-perl libxml-simple-perl

RUN sh -c "$(curl -fsSL ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"

ENV PATH="/root/edirect/:${PATH}"
