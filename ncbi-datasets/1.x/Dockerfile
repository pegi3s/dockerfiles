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

FROM ubuntu:22.04

ARG VERSION

RUN apt-get update && apt-get install -y wget
RUN apt-get install -y unzip

RUN wget "https://github.com/ncbi/datasets/releases/download/v${VERSION}/linux-amd64.cli.package.zip" -O /tmp/linux-amd64.cli.package.zip && \
	unzip /tmp/linux-amd64.cli.package.zip -d /usr/bin/ && rm /tmp/linux-amd64.cli.package.zip && \
	chmod +x /usr/bin/dataformat /usr/bin/datasets

RUN apt-get remove -y wget

CMD [ "datasets", "--help" ]
