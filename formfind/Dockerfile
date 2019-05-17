# https://github.com/Chronic-Dev/curl/blob/master/perl/contrib/formfind

FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common
RUN apt-get install -y curl

COPY ./formfind.pl /opt/formfind.pl
COPY ./run /opt/run
