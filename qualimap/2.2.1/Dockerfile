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

FROM pegi3s/r_project:3.6.0

RUN apt-get update && apt-get -y upgrade && \
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV TZ=Europe/Lisbon\
	 DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y software-properties-common build-essential \
	wget libcurl4-openssl-dev libxml2-dev libssl-dev unzip littler

RUN ln -s /usr/lib/x86_64-linux-gnu/libncursesw.so.6 /usr/lib/x86_64-linux-gnu/libncursesw.so.5

#Install Java
RUN apt-get update && \
	apt-get install -y openjdk-8-jre && \
	rm -rf /var/lib/apt/lists/*

#Install Bioconductor packages required by Qualimap
RUN Rscript -e "install.packages('optparse')"
RUN Rscript -e "install.packages('BiocManager', repos = 'http://cran.us.r-project.org')"
RUN Rscript -e "BiocManager::install(c('NOISeq', 'Repitools'))"

#Install Qualimap
RUN cd /opt && wget https://bitbucket.org/kokonech/qualimap/downloads/qualimap_v2.2.1.zip
RUN cd /opt && unzip qualimap_v2.2.1.zip && rm qualimap_v2.2.1.zip
RUN Rscript /opt/qualimap_v2.2.1/scripts/installDependencies.r

ENV PATH="/opt/qualimap_v2.2.1:$PATH"
