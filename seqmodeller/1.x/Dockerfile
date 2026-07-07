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

FROM ubuntu:24.04

ARG VERSION

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y \
	wget \
	unzip \
	fontconfig \
	libasound2t64 \
	libdbus-1-3 \
	libegl1 \
	libfreetype6 \
	libgl1 \
	libglib2.0-0t64 \
	libice6 \
	libnss3 \
	libsm6 \
	libx11-6 \
	libxcomposite1 \
	libxkbcommon0 \
	libxkbcommon-x11-0 \
	libxcb-cursor0 \
	libxcb-icccm4 \
	libxcb-image0 \
	libxcb-keysyms1 \
	libxcb-render0 \
	libxcb-render-util0 \
	libxcb-randr0 \
	libxcb-shape0 \
	libxcb-xinerama0 \
	libxcursor1 \
	libxdamage1 \
	libxext6 \
	libxfixes3 \
	libxi6 \
	libxrandr2 \
	libxrender1 \
	libxtst6

RUN wget "https://github.com/Dannyzimmer/SeqModeller/releases/download/v${VERSION}/SeqModeller-v${VERSION}_Linux_x86-64.zip" -O /tmp/SeqModeller.zip && \
	unzip /tmp/SeqModeller.zip -d /opt && \
	ln -s /opt/SeqModeller /usr/local/bin/SeqModeller && \
	rm /tmp/SeqModeller.zip

RUN apt-get remove -y wget unzip && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["SeqModeller"]
