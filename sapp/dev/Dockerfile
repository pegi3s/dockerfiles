#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN wget http://download.systemsbiology.nl/sapp/dev/Aragorn.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/BLAST.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/CRT.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/Conversion.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/EnzDP.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/GenomeInformation.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/HDTQuery.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/HMM.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/InterProScan.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/Loader.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/RDFLoader.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/TMHMM.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/Transcriptomics.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/WoLFPSort.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/assembly.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/genecaller.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/pathwayAnalysis.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/rnammer.jar
RUN wget http://download.systemsbiology.nl/sapp/dev/signalp.jar
RUN wget http://download.systemsbiology.nl/sapp/test.file
