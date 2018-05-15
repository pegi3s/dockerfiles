FROM ubuntu:18.04

RUN apt-get -qq update && \
	apt-get install -y --no-install-recommends wget \
	bsdmainutils libgomp1 make openmpi-bin ssh \
	automake g++ libboost-dev libopenmpi-dev libsparsehash-dev

RUN wget --no-check-certificate https://github.com/bcgsc/abyss/releases/download/2.1.0/abyss-2.1.0.tar.gz -O /tmp/abyss.tar.gz && \
	tar zxvf /tmp/abyss.tar.gz -C /opt/ && rm /tmp/abyss.tar.gz && \
	cd /opt/abyss-2.1.0 && \
	./autogen.sh && \
	mkdir build && cd build && \
	../configure --with-mpi=/usr/lib/openmpi --enable-maxk=128 && \
	make install-strip && \
	rm -rf /tmp/abyss

RUN apt-get autoremove -y binutils automake g++ libboost-dev libopenmpi-dev libsparsehash-dev wget
