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

FROM ubuntu:14.04

RUN apt-get update && apt-get install -y software-properties-common wget unzip

RUN apt-get install -y openjdk-6-jre && rm -rf /var/lib/apt/lists/*

RUN wget https://www.cs.hhu.de/fileadmin/redaktion/Fakultaeten/Mathematisch-Naturwissenschaftliche_Fakultaet/Informatik/Computational_Cell_Biology/Folien/TreeSnatcherPlus_June2010_Linux.zip

RUN mkdir /opt/TreeSnatcherPlus

RUN unzip TreeSnatcherPlus_June2010_Linux.zip -d /opt

CMD java -jar -Dsun.java2d.opengl=true -Xms256m -Xmx1500m /opt/TreeSnatcherPlus.jar
