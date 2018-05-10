FROM ubuntu:18.04

# Install Java
RUN apt-get update && apt-get install -y software-properties-common && \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java8-installer && \
	apt-get install -y libfontconfig1 libxrender1 libxtst6 libxi6 libgconf-2-4 && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get update && apt-get install -y autoconf build-essential unzip muscle

RUN wget http://www.tcoffee.org/Packages/Stable/Latest/linux/T-COFFEE_installer_Version_11.00.8cbe486_linux_x64.tar.gz -O /tmp/tcoffee.tar.gz && \
	tar zxvf /tmp/tcoffee.tar.gz -C /opt/ && \
	rm /tmp/tcoffee.tar.gz 

ENV PATH="/opt/T-COFFEE_installer_Version_11.00.8cbe486_linux_x64/bin:${PATH}"

RUN wget https://sourceforge.net/projects/mrbayes/files/mrbayes/3.2.2/mrbayes-3.2.2.tar.gz/download -O /tmp/mrbayes.tar.gz &&  \
	tar zxvf /tmp/mrbayes.tar.gz -C /opt/ && \
	rm /tmp/mrbayes.tar.gz && \
	cd /opt/mrbayes_3.2.2/src && \
	autoconf && ./configure --with-beagle=no && make

ENV PATH="/opt/mrbayes_3.2.2/src:${PATH}"

RUN wget http://abacus.gene.ucl.ac.uk/software/paml4.9h.tgz -O /tmp/paml.tgz && \
	tar zxvf /tmp/paml.tgz -C /opt/ && \
	rm /tmp/paml.tgz && \
	cd /opt/paml4.9h && \
	rm -rf bin/*.exe && \
	cd src && \
	make -f Makefile && \
	mv baseml basemlg codeml pamp evolver yn00 chi2 ../bin && \
	ln -s /opt/paml4.9h/bin/codeml /usr/bin/codeml

ENV PATH="/opt/paml4.9h/bin:${PATH}"

RUN wget http://static.sing-group.org/ADOPS/ADOPS_v0.7.1.zip -O /tmp/ADOPS.zip && \
	unzip /tmp/ADOPS.zip -d /opt/ && \
	mv /opt/ADOPS* /opt/ADOPS && \
	rm /tmp/ADOPS.zip -f

CMD sh /opt/ADOPS/run.sh
