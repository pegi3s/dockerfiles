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

ARG VERSION

FROM ubuntu:24.04

ARG VERSION

RUN apt-get update -y && \
	apt-get install -y \
		wget \
		libx11-6 \
		libxext6 \
		libxi6 \
		libxrender1 \
		libxtst6 \
		libxxf86vm1 \
		libgl1 \
		libatk1.0-0 \
		libcairo2 \
		libgtk-3-0 \
		libgdk-pixbuf-2.0-0 \
		libglib2.0-0 \
		libpango-1.0-0 \
		libpangocairo-1.0-0 \
		libpangoft2-1.0-0 \
		libfreetype6 \
		libfontconfig1 && \
	rm -rf /var/lib/apt/lists/*

RUN cd /opt && \
	wget "https://github.com/husonlab/splitstree6/releases/download/v${VERSION}/SplitsTree-${VERSION}-linux-x86_64.tar.gz" && \
	tar xzf "SplitsTree-${VERSION}-linux-x86_64.tar.gz" && \
	rm "SplitsTree-${VERSION}-linux-x86_64.tar.gz" && \
	ln -s /opt/SplitsTree/bin/SplitsTree /usr/local/bin/SplitsTree

ENTRYPOINT ["SplitsTree"]
