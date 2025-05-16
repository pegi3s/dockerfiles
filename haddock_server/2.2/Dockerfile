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

# Don't forget to keep a delay between requests or your IP address will be banned
# to see formfind information: cat ./opt/info

FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential unzip wget && \
	apt-get install -y ca-certificates software-properties-common
RUN apt-get install -y curl

COPY ./info ./opt/info
COPY ./run ./opt/run
COPY ./parameters.haddock ./opt/parameters.haddock
