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

FROM ubuntu:18.04

WORKDIR /igv
RUN apt-get update && apt install -y default-jdk wget unzip
RUN wget https://data.broadinstitute.org/igv/projects/downloads/2.13/IGV_Linux_2.13.0_WithJava.zip
RUN unzip ./IGV_Linux_2.13.0_WithJava.zip
RUN rm ./IGV_Linux_2.13.0_WithJava.zip
WORKDIR /igv/IGV_Linux_2.13.0
RUN chmod +x igv.sh
CMD [ "./igv.sh" ]
