FROM ubuntu:19.04

RUN apt-get update && apt-get -y upgrade && \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV TZ=Europe/Lisbon\
	 DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y software-properties-common build-essential \
	wget libcurl4-openssl-dev libxml2-dev libssl-dev unzip littler

RUN ln -s /usr/lib/x86_64-linux-gnu/libncursesw.so.6 /usr/lib/x86_64-linux-gnu/libncursesw.so.5

#Install Java
RUN apt-get update && \
	apt-get install -y openjdk-8-jre && \
	rm -rf /var/lib/apt/lists/*

#Install R 3.6
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 51716619E084DAB9
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran35/"
RUN  apt update && apt install -y r-base

#Install Bioconductor packages required by Qualimap
RUN Rscript -e "install.packages('optparse')"
RUN Rscript -e "install.packages('BiocManager', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "BiocManager::install(c('NOISeq', 'Repitools'))"

#Install Qualimap
RUN cd /opt && wget https://bitbucket.org/kokonech/qualimap/downloads/qualimap_v2.2.1.zip
RUN cd /opt && unzip qualimap_v2.2.1.zip && rm qualimap_v2.2.1.zip
RUN Rscript /opt/qualimap_v2.2.1/scripts/installDependencies.r

ENV PATH="/opt/qualimap_v2.2.1:$PATH"
