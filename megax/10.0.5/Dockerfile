#
#   Copyright 2018-2021 Hugo López-Fernández, Pedro M. Ferreira, Miguel 
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

RUN apt-get update \
	&& apt-get install -y build-essential wget libgtk2.0-0 libgconf-2-4 libcanberra-gtk* chromium-browser

WORKDIR /data

RUN wget https://www.megasoftware.net/releases/megax_10.0.5-1_amd64.deb \
  && dpkg -i megax_10.0.5-1_amd64.deb \
  && rm megax_10.0.5-1_amd64.deb

ENV PATH="/usr/lib/:$PATH"

ENTRYPOINT ["megax"]
