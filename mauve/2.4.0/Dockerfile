FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common && \
	apt-get install -y libfontconfig1 libxrender1 libxtst6 libxi6 libgconf-2-4

RUN apt-get update && \
	apt-get install -y openjdk-8-jre && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update \
	&& apt-get install -y wget

RUN wget http://darlinglab.org/mauve/snapshots/2015/2015-02-13/linux-x64/mauve_linux_snapshot_2015-02-13.tar.gz -O /tmp/mauve.tar.gz \
	&& tar zxvf /tmp/mauve.tar.gz -C /opt/ && rm /tmp/mauve.tar.gz

RUN echo "java -jar /opt/mauve_snapshot_2015-02-13/Mauve.jar" > "/opt/mauve_snapshot_2015-02-13/run.sh"

CMD sh /opt/mauve_snapshot_2015-02-13/run.sh

ENV PATH="/opt/mauve_snapshot_2015-02-13/linux-x64/:${PATH}"
