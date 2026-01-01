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

FROM pegi3s/utilities:0.22.0 as base_pegi3s_utilities

FROM pegi3s/blast:2.6.0-1

ADD scripts /opt/scripts

COPY --from=base_pegi3s_utilities /opt/scripts/fasta_remove_line_breaks /opt/scripts/fasta_remove_line_breaks

RUN chmod 777 /opt/scripts/*

ENV PATH="/opt/scripts:${PATH}"

ENV TERM=xterm-256color
