#
#   Copyright 2018-2026 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

FROM debian:12.2-slim

ARG VERSION

RUN apt-get update && apt-get install -y wget

RUN wget "https://github.com/bbuchfink/diamond/releases/download/v${VERSION}/diamond-linux64.tar.gz" -O /tmp/diamond.tar.gz && \
	tar zxvf /tmp/diamond.tar.gz -C /usr/bin/ && rm /tmp/diamond.tar.gz

RUN apt-get remove -y wget

ENTRYPOINT ["diamond"]
CMD ["help"]
