FROM ubuntu:16.04

ADD http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz /opt

RUN ln -s /opt/FLASH-1.2.11-Linux-x86_64/flash /usr/bin

RUN cd /opt && \
	tar -xvzf FLASH-1.2.11-Linux-x86_64.tar.gz && \
	rm FLASH-1.2.11-Linux-x86_64.tar.gz
	
ENV PATH="/opt/FLASH-1.2.11-Linux-x86_64/:${PATH}"

ENTRYPOINT ["flash"]
