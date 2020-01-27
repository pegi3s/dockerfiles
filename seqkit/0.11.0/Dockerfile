FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget

RUN wget https://github.com/shenwei356/seqkit/releases/download/v0.11.0/seqkit_linux_amd64.tar.gz -O /tmp/seqkit.tar.gz && \
	tar zxvf /tmp/seqkit.tar.gz -C /usr/bin/ && rm /tmp/seqkit.tar.gz

RUN apt-get remove -y wget

ENTRYPOINT ["seqkit"]
CMD ["-h"]
