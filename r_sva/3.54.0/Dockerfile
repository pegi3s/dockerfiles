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

FROM r-base:4.4.0

RUN apt-get update -y \
    && apt-get install -y libssl-dev libcurl4-openssl-dev libxml2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e "install.packages('BiocManager')" \
    && echo 'n' | R --no-save -e "install.packages(c('ggplot2'))" \
    && echo 'n' | R --no-save -e "BiocManager::install(c('sva'))"

CMD ["/list_r_packages.sh"]

