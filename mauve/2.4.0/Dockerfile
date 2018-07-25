FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common && \
	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
	add-apt-repository -y ppa:webupd8team/java && \
	apt-get update && \
	apt-get install -y oracle-java8-installer && \
	apt-get install -y libfontconfig1 libxrender1 libxtst6 libxi6 libgconf-2-4 && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN apt-get update \
	&& apt-get install -y wget

RUN wget http://darlinglab.org/mauve/snapshots/2015/2015-02-13/linux-x64/mauve_linux_snapshot_2015-02-13.tar.gz -O /tmp/mauve.tar.gz \
	&& tar zxvf /tmp/mauve.tar.gz -C /opt/ && rm /tmp/mauve.tar.gz

ENV PATH="/opt/mauve.2.4.0-ubuntu64/bin/:${PATH}"

RUN echo "java -jar /opt/mauve_snapshot_2015-02-13/Mauve.jar" > "/opt/mauve_snapshot_2015-02-13/run.sh"

CMD sh /opt/mauve_snapshot_2015-02-13/run.sh
