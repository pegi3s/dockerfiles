FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget make gcc

RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz -O /tmp/v8.2.12.tar.gz && \
    tar -xvzf /tmp/v8.2.12.tar.gz -C /opt/ && \
    rm /tmp/v8.2.12.tar.gz && \
	cd /opt/standard-RAxML-8.2.12 && \
    make -f Makefile.gcc  && \
    rm *.o  && \
    make -f Makefile.SSE3.gcc  && \
    rm *.o  && \
    make -f Makefile.PTHREADS.gcc  && \
    rm *.o  && \
    make -f Makefile.SSE3.PTHREADS.gcc  && \
    rm *.o  && \
    cp raxmlHPC* /usr/local/bin
