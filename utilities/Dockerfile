FROM ubuntu:18.04

RUN echo "#!/bin/bash \n\
find /opt/scripts -type f -print | sed 's/\/opt\/scripts\///g'" > /usr/local/bin/help && chmod u+x /usr/local/bin/help

ADD scripts /opt/scripts

ENV PATH="/opt/scripts:${PATH}"
