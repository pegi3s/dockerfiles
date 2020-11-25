FROM pegi3s/docker

RUN apt-get update && \
	apt-get install -y wget

RUN mkdir -p /opt/scripts && wget https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 -O /opt/scripts/jq-linux64 

RUN echo "#!/bin/bash \n\
find /opt/scripts -type f -print | sed 's/\/opt\/scripts\///g'" > /usr/local/bin/help && chmod u+x /usr/local/bin/help

ADD scripts /opt/scripts

RUN chmod 777 /opt/scripts/*

ENV PATH="/opt/scripts:${PATH}"

ENV TERM=xterm-256color
