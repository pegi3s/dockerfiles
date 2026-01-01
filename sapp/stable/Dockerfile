#
#   Copyright 2018-2026 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
#   Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential unzip wget && \
	apt-get install -y software-properties-common && \
	apt-get install libboost-iostreams1.62.0

RUN apt-get update && \
	apt-get install -y openjdk-8-jre && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

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
