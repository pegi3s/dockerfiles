FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common \
	              make libcrypto++-dev libssl-dev openmpi-bin libopenmpi-dev \
                      cmake build-essential unzip wget

RUN wget https://github.com/veg/hyphy/archive/2.3.14.zip -O /tmp/hyphy-2.3.14.zip && \
    unzip /tmp/hyphy-2.3.14.zip -d /opt/ && \
    rm /tmp/hyphy-2.3.14.zip -f

RUN cd /opt/hyphy-2.3.14/ && \
    cmake . && make HYPHYMP && make install
