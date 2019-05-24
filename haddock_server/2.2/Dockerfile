# Don't forget to keep a delay between requests or your IP address will be banned
# to see formfind information: cat ./opt/info

FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common
RUN apt-get install -y curl

COPY ./info ./opt/info
COPY ./run ./opt/run
COPY ./parameters.haddock ./opt/parameters.haddock
