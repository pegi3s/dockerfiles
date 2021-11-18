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

FROM pegi3s/r_project:4.1.1

RUN apt-get install -y gfortran libblas-dev liblapack-dev && \
    apt install -y libxml2-dev  && \
    R -e "install.packages('XML')"  && \
    apt install -y libcurl4-openssl-dev  && \
    R -e "install.packages('RCurl')"  && \
    apt install -y libssl-dev  && \
    R -e "install.packages('httr')"  && \
    apt install -y libpng-dev  && \
    R -e "install.packages('png')"

RUN R -e "install.packages('BiocManager'); library('BiocManager'); BiocManager::install('EnhancedVolcano')"
