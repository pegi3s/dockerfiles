FROM ubuntu:18.04

RUN apt-get -qq update && apt-get -y upgrade && \
	apt-get install -y bsdmainutils gawk bwa=0.7.17-1 abyss=2.0.2-3

RUN rm /usr/bin/DistanceEst /usr/bin/abyss-fixmate /usr/bin/abyss-pe && \
	ln -s /usr/lib/abyss/* /usr/bin/
