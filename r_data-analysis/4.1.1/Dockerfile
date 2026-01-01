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

FROM pegi3s/r_project:4.1.1

RUN R -e "install.packages('dplyr')"  && \
    R -e "install.packages('data.table')"  && \
    R -e "install.packages('caret')"  && \
    R -e "install.packages('tidyr')"  && \
    R -e "install.packages('mlr3')"  && \
    R -e "install.packages('knitr')"  && \
    R -e "install.packages('rmarkdown')"  && \
    R -e "install.packages('stringr')"  && \
    R -e "install.packages('readr')"  && \
    R -e "install.packages('readxl')"  && \
    R -e "install.packages('purrr')"  && \
    R -e "install.packages('openxlsx')"  && \
    R -e "install.packages('tidytext')" && \
    R -e "install.packages('gplots')"  && \
    R -e "install.packages('dendextend')" && \
    R -e "install.packages('amap')"
