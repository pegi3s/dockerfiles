FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y git libxml-libxml-perl libidn11 autoconf build-essential automake
WORKDIR /opt
RUN git clone https://github.com/tjunier/newick_utils
RUN apt-get install -y bison flex gcc libtool
WORKDIR /opt/newick_utils
RUN autoreconf -fi && ./configure && make && make install
ENV PATH /usr/local/lib:$PATH
RUN ldconfig
