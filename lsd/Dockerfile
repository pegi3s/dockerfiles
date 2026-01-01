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

FROM pegi3s/lsd-base

# https://web.archive.org/web/20170916024357/http://www.markusbe.com:80/2009/09/about-running-32-bit-programs-on-64-bit-ubuntu-and-shared-libraries/
RUN apt-get install -y ia32-libs

ENV LD_LIBRARY_PATH=/usr/lib64/

COPY resources/sigdis.pl /opt/lineagesequencediscovery-master/sigdis/sigdis.pl

COPY resources/libraries/* /usr/lib/

RUN chmod +x /opt/lineagesequencediscovery-master/sigdis/*

RUN ln -s /usr/lib/libRmath.so /usr/lib/libRmath.so.1

RUN apt-get install -y tcl8.3

RUN cd /opt/lineagesequencediscovery-master && rm -rf SFBB.fasta SFBB_neg.fasta demo demo1 dist libgnome2-print-perl_1.000-1_i386.deb libgtk2-sourceview-perl_1.000-0ubuntu4_i386.deb lineage-sequence-discovery-0.3.5 lineage-sequence-discovery.tar.gz lineagesequencediscovery-0.3.4-i386-all.deb lineage-sequence-discovery-0.3.5-1.i686.rpm lineagesequencediscovery-0.3.5-i386-all.deb lineage-sequence-discovery-debuginfo-0.3.5-1.i686.rpm meme.pat neg_file_test.fasta negative.dnd negfile_1.dnd pats.pat pos_file_test.fasta proteins2000.fasta res.arff res.csv res.pat.arff res1.fasta res2.fasta retrovirus5000.fasta retrovirus5000.fasta.pat

CMD /opt/lineagesequencediscovery-master/LSD.sh
