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

RUN apt-get -qq update && apt-get -y upgrade && \
	apt install -y wget libfindbin-libs-perl software-properties-common unzip

RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.7.zip -O /tmp/fastqc.zip && \ 
    unzip /tmp/fastqc.zip -d /opt/ && \
    rm /tmp/fastqc.zip && \
    chmod 777 /opt/FastQC/fastqc

ENV PATH="/opt/FastQC/:${PATH}"

ENTRYPOINT ["fastqc"]
