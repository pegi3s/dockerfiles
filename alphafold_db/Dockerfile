FROM pegi3s/docker

RUN apt-get update && \
	apt-get install -y wget

COPY ./run /opt/run

RUN chmod a+x /opt/run
