#
#   Copyright 2018-2025 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
#   Reboiro-Jato, Cristina P. Vieira, and Jorge Vieira
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

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
