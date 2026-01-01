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

FROM pegi3s/r_project

#Install GIS-specific packages

RUN apt-get install -y libgeos-dev
RUN Rscript -e "install.packages(c('raster', 'dismo', 'maptools', 'rgeos', 'rJava', 'jsonlite', 'sp'))"
RUN apt install -y texlive-extra-utils

COPY /gis /opt/gis
