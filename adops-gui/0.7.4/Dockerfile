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

FROM pegi3s/tcoffee:10.00.r1613

# Install Java
RUN apt-get update && apt-get install -y software-properties-common && \
	apt-get install -y libfontconfig1 libxrender1 libxtst6 libxi6 libgconf-2-4

RUN apt-get update && \
	apt-get install -y openjdk-8-jre && \
	rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

RUN apt-get update && apt-get install -y autoconf build-essential unzip

RUN wget https://github.com/NBISweden/MrBayes/releases/download/v3.2.2/mrbayes-3.2.2.tar.gz -O /tmp/mrbayes.tar.gz &&  \
	tar zxvf /tmp/mrbayes.tar.gz -C /tmp/ && \
	mv /tmp/mrbayes_3.2.2 /opt/mrbayes_3.2.2 && \
	cd /opt/mrbayes_3.2.2/src && \
	autoconf && ./configure --with-beagle=no && make

ENV PATH="/opt/mrbayes_3.2.2/src:${PATH}"

RUN wget https://github.com/abacus-gene/paml/releases/download/pre-v4.10/paml4.9h.tgz -O /tmp/paml.tgz && \
	tar zxvf /tmp/paml.tgz -C /opt/ && \
	rm /tmp/paml.tgz && \
	cd /opt/paml4.9h && \
	rm -rf bin/*.exe && \
	cd src && \
	make -f Makefile && \
	mv baseml basemlg codeml pamp evolver yn00 chi2 ../bin && \
	ln -s /opt/paml4.9h/bin/codeml /usr/bin/codeml

ENV PATH="/opt/paml4.9h/bin:${PATH}"

RUN wget http://static.sing-group.org/ADOPS/ADOPS_v0.7.4.zip -O /tmp/ADOPS.zip && \
	unzip /tmp/ADOPS.zip -d /opt/ && \
	mv /opt/ADOPS* /opt/ADOPS && \
	rm /tmp/ADOPS.zip -f && \
	sed -i "s/^mrbayes\.dir.*/mrbayes\.dir=\/opt\/mrbayes_3\.2\.2\/src/g" /opt/ADOPS/system.conf

RUN for f in /root/tcoffee/Version_10.00.r1613/plugins/linux/*; do \
      ln -sf "$f" "/usr/bin/$(basename "$f")"; \
    done

CMD sh /opt/ADOPS/run.sh
