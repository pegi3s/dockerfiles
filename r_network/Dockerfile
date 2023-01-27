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

ARG R_DATA_ANALYSIS_VERSION

FROM pegi3s/r_data-analysis:${R_DATA_ANALYSIS_VERSION}

RUN apt-get -qq update && apt-get -y upgrade && \
    apt-get install -y pandoc

RUN R -e "install.packages('igraph')"  && \
    R -e "install.packages('networkD3')"  && \
    R -e "install.packages('htmlwidgets')" && \
    R -e "install.packages('pandoc')"
