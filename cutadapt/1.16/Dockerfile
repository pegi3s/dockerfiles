FROM ubuntu:18.04

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y python3-pip python3-dev build-essential

RUN pip3 install --upgrade pip==9.0.1 && \
	pip3 install --upgrade virtualenv

RUN pip3 install --user --upgrade cutadapt==1.16 && \
	ln -s /root/.local/bin/cutadapt /usr/bin/

ENTRYPOINT ["cutadapt"]
