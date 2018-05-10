FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common && \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java8-installer && \
	apt-get install -y libfontconfig1 libxrender1 libxtst6 libxi6 libgconf-2-4 && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get update && apt-get install -y git maven 

RUN wget https://github.com/sing-group/ALTER/archive/v1.3.4.tar.gz -O /tmp/alter.tar.gz && \
	tar zxvf /tmp/alter.tar.gz -C /opt/ && rm /tmp/alter.tar.gz && \
	mv /opt/ALTER-* /opt/ALTER && \
	cd /opt/ALTER && mvn package

RUN echo '#!/bin/bash \n\
java -jar /opt/ALTER/alter-lib/target/ALTER-1.3.4-jar-with-dependencies.jar $*' > /opt/ALTER/alter && chmod u+x /opt/ALTER/alter

ENV PATH="/opt/ALTER/:${PATH}"

ENTRYPOINT ["alter"]

