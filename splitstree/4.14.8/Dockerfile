FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y build-essential && \
	apt-get install -y ca-certificates software-properties-common -y wget && \
        apt install apt-transport-https

RUN cd /opt && \ 
	wget https://ab.inf.uni-tuebingen.de/data/software/splitstree4/download/splitstree4_unix_4_14_8.sh && \
	chmod 777 /opt/splitstree4_unix_4_14_8.sh
RUN apt install -y default-jre
RUN { echo 'o' ; echo '1' ; echo '/opt/splitstree4' ; echo 'X,2,3' ; echo "n" ; echo '5' ; echo '1000' ; } | /opt/splitstree4_unix_4_14_8.sh

ENTRYPOINT [ "sh", "-c", "/opt/splitstree4/SplitsTree" ]

WORKDIR /data
