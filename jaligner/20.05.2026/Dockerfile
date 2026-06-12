#
#   Copyright 2018-2026 Hugo López-Fernández, Miguel Reboiro-Jato,
#   Cristina P. Vieira, and Jorge Vieira
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

FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk ant git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ahmedmoustafa/JAligner /opt/JAligner && \
    cd /opt/JAligner && \
    rm -f src/jaligner/ui/clipboard/ClipboardHandlerJNLP.java src/jaligner/ui/filechooser/FileChooserJNLP.java && \
    sed -i 's/new ClipboardHandlerJNLP()/new ClipboardHandlerAWT()/' src/jaligner/ui/clipboard/ClipboardHandlerFactory.java && \
    sed -i 's/new FileChooserJNLP()/new FileChooserTrusted()/' src/jaligner/ui/filechooser/FileChooserFactory.java && \
    sed -i 's/FileChooserJNLP.class/FileChooserTrusted.class/' src/jaligner/ui/filechooser/FileChooserTrusted.java && \
    ant build && \
    rm -rf /opt/JAligner/bin

ENTRYPOINT ["java", "-jar", "/opt/JAligner/jaligner.jar"]
