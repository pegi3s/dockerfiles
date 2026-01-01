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

FROM pegi3s/docker

WORKDIR /opt
COPY cp_dockerfile /opt
RUN mv cp_dockerfile dockerfile

COPY local_config_file /opt

#scripts
COPY run-example.csh /opt
COPY main /opt
COPY zscore_run /opt
COPY restraints_run /opt
COPY prepare_data /opt
COPY important_files /opt
COPY create_runparam /opt
COPY prepare_pdb /opt

#examples
COPY pdna_run /opt
COPY plig_run /opt
COPY pligshape_run /opt
COPY pp_run /opt
COPY ppdani_run /opt
COPY ppem_run /opt
COPY ppep_run /opt
COPY ppepensemble_run /opt
COPY pppcs_run /opt
COPY pprdc_run /opt
COPY prefinepcs_run /opt
COPY ptetraCG_run /opt
COPY ptrimer_run /opt
COPY refinecomplex_run /opt
COPY solvateddocking_run /opt

COPY change_haddock_version.rtf /opt

#docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /home/jorge/Documents/mariana/builder:/data pegi3s/haddock24-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/haddock24"






