FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential unzip wget && \
	apt-get install -y software-properties-common && \
	apt-get install libboost-iostreams1.62.0

#INSTALL JAVA
RUN add-apt-repository ppa:webupd8team/java -y && \
	apt-get update && \
	echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
	apt-get install -y oracle-java8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN wget http://download.systemsbiology.nl/sapp/Aragorn.jar
RUN wget http://download.systemsbiology.nl/sapp/BLAST.jar
RUN wget http://download.systemsbiology.nl/sapp/CRT.jar
RUN wget http://download.systemsbiology.nl/sapp/Conversion.jar
RUN wget http://download.systemsbiology.nl/sapp/EnzDP.jar
RUN wget http://download.systemsbiology.nl/sapp/GenomeSync.jar
RUN wget http://download.systemsbiology.nl/sapp/HDTQuery.jar
RUN wget http://download.systemsbiology.nl/sapp/HMM.jar
RUN wget http://download.systemsbiology.nl/sapp/InterProScan.jar
RUN wget http://download.systemsbiology.nl/sapp/Loader.jar
RUN wget http://download.systemsbiology.nl/sapp/TMHMM.jar
RUN wget http://download.systemsbiology.nl/sapp/WoLFPSort.jar
RUN wget http://download.systemsbiology.nl/sapp/assembly.jar
RUN wget http://download.systemsbiology.nl/sapp/genecaller.jar
RUN wget http://download.systemsbiology.nl/sapp/pathwayAnalysis.jar
RUN wget http://download.systemsbiology.nl/sapp/rnammer.jar
RUN wget http://download.systemsbiology.nl/sapp/signalp.jar
RUN wget http://download.systemsbiology.nl/sapp/test.file
