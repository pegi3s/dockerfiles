FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential && \
	apt-get install -y ca-certificates software-properties-common && \
        apt install apt-transport-https

#Install R

ENV TZ=Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' && apt update
RUN apt install -y r-base r-base-dev default.jdk

WORKDIR /data
