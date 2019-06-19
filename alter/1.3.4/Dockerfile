FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common

RUN apt-get update && \
	apt-get install -y openjdk-8-jdk && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update && apt-get install -y git maven

RUN wget https://github.com/sing-group/ALTER/archive/v1.3.4.tar.gz -O /tmp/alter.tar.gz && \
	tar zxvf /tmp/alter.tar.gz -C /opt/ && rm /tmp/alter.tar.gz && \
	mv /opt/ALTER-* /opt/ALTER && \
	cd /opt/ALTER && mvn package

RUN echo '#!/bin/bash \n\
java -jar /opt/ALTER/alter-lib/target/ALTER-1.3.4-jar-with-dependencies.jar $*' > /opt/ALTER/alter && chmod u+x /opt/ALTER/alter

ENV PATH="/opt/ALTER/:${PATH}"

ENTRYPOINT ["alter"]
