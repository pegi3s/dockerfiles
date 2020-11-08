FROM ubuntu:20.04

ENV TZ=Europe/Lisbon

RUN apt-get update && \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
	apt-get install -y libqt5gui5 pymol
