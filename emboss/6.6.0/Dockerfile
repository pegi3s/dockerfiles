FROM ubuntu:18.04

LABEL emboss.version="6.6.0" \
      emboss.web="http://emboss.sourceforge.net"

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y emboss=6.6.0+dfsg-6build1
