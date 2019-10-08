FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common

RUN apt-get install -y git ant wget

RUN apt-get update && \
	apt-get install -y openjdk-8-jdk && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN git clone https://github.com/ddarriba/jmodeltest2.git

RUN cd jmodeltest2 && ant jar

RUN cd /jmodeltest2/dist/exe/phyml && \
	wget https://github.com/713/project/raw/master/dependencies/jmodeltest-2.1.3/exe/phyml/PhyML_3.0_linux64 && \
	chmod 777 PhyML_3.0_linux64
