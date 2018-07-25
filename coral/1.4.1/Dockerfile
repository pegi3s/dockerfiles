FROM ubuntu:18.04

LABEL coral.version="1.4.1" \
      coral.web="https://www.cs.helsinki.fi/u/lmsalmel/coral/"

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y wget build-essential

RUN  wget https://www.cs.helsinki.fi/u/lmsalmel/coral/coral-1.4.1.tar.gz -O /tmp/coral.tar.gz && \
	tar -xvzf /tmp/coral.tar.gz -C /opt/ && \
	rm /tmp/coral.tar.gz && \
	cd /opt/coral-1.4.1 && \
	make

ENV PATH="/opt/coral-1.4.1/:${PATH}"

RUN apt-get autoremove -y wget

ENTRYPOINT ["coral"]
CMD ["-h"]