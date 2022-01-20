FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

ENV TZ=Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y && \
	apt-get install -y samtools gnuplot
