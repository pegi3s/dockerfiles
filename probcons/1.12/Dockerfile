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

FROM debian:stable-slim

# Update commands and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        ca-certificates \
        patch \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/probcons

# Download and extract PROBCONS
RUN wget -q http://probcons.stanford.edu/probcons_v1_12.tar.gz \
    && tar -xzf probcons_v1_12.tar.gz \
    && rm probcons_v1_12.tar.gz

# Apply patches to the PROBCONS source files
RUN sed -i '25i#include <cstring>' probcons/Main.cc \
    && sed -i '20i#include <cstring>' probcons/CompareToRef.cc \
    && sed -i '1i#include <cstddef>' probcons/SafeVector.h \
    && sed -i 's/std::vector<TYPE>(size)/std::vector<TYPE>::vector(size)/g' probcons/SafeVector.h \
    && sed -i 's/std::vector<TYPE>(size, value)/std::vector<TYPE>::vector(size, value)/g' probcons/SafeVector.h \
    && echo '--- ProjectPairwise.cc.orig\n+++ ProjectPairwise.cc\n@@ -17,6 +17,7 @@\n #include <iostream>\n #include <fstream>\n #include <cerrno>\n+#include <cstring>\n #include <iomanip>\n #include <cassert>\n #include <cstdio>\n' > probcons.patch \
    && patch probcons/ProjectPairwise.cc probcons.patch

# Compile PROBCONS
RUN cd probcons \
    && make clean \
    && make \
    && mv probcons /usr/local/bin \
    && cd ../.. \
    && rm -r probcons
    
# General clear
RUN apt-get remove --purge -y build-essential wget patch \
    && apt-get autoremove -y \
    && apt-get clean
