FROM ubuntu:18.04

LABEL edena.version="V3.131028" \
      edena.web="http://www.genomic.ch/edena.php"

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y wget build-essential

RUN wget http://www.genomic.ch/edena/EdenaV3.131028.tar.gz -O /tmp/edena.tar.gz && \
	tar -xvzf /tmp/edena.tar.gz -C /opt && \
	rm /tmp/edena.tar.gz && \
	cd /opt/EdenaV3.131028 && \
	make

ENV PATH="/opt/EdenaV3.131028/bin/:${PATH}"

RUN apt-get autoremove -y wget build-essential	

ENTRYPOINT ["edena"]
CMD ["-h"]


