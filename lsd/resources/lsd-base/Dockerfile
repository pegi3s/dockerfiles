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

FROM ubuntu:10.04

RUN sed -ie 's/archive/old-releases/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
perl \
make \
curl \
wget \
expat \
git-core \
unzip \
libglib-perl \
libgtk2-perl 

RUN apt-get update && apt-get install -y \
pkg-config \
bioperl \
libglib2.0-dev \
libart-2.0-dev \
libpango1.0-dev \
libxml2-dev 

RUN apt-get update && apt-get install -y \
t-coffee \
libcanberra-gtk-module

# RUN cd /opt && wget https://github.com/nunofonseca/lineagesequencediscovery/archive/master.zip \
#	&& unzip master.zip
	
RUN cd /opt && curl -L -O -tlsv2 https://github.com/nunofonseca/lineagesequencediscovery/archive/master.zip && unzip master.zip
	
RUN cd /opt && wget http://meme-suite.org/meme-software/4.10.0/meme_4.10.0_4.tar.gz \
	&& tar zxvf meme_4.10.0_4.tar.gz && cd meme_4.10.0 && ./configure && make && make install
	
RUN chmod +x /opt/lineagesequencediscovery-master/sigdis/sigdis.pl
	
RUN cpan install CPAN; exit 0;
RUN cpan App:cpanminus
RUN cpanm File::HomeDir
RUN cpanm Number::Format
RUN cpanm ExtUtils::Depends
RUN cpanm ExtUtils::PkgConfig

RUN apt-get install -y libgnomeprintui2.2-dev libgtksourceview-dev
RUN cpanm Gnome2::Print
RUN cpanm Gtk2::SourceView --force

RUN wget -O /opt/lineagesequencediscovery-master/LSD.sh https://sing.ei.uvigo.es/owncloud/index.php/s/nZj0QZrvPKJkQaG/download --no-check-certificate && chmod +x /opt/lineagesequencediscovery-master/LSD.sh 

CMD export PATH=$PATH:/opt/lineagesequencediscovery-master/sigdis/ && cd /opt/lineagesequencediscovery-master/ && perl LSD.pl
