FROM pegi3s/utilities

RUN apt-get update && \
	apt-get install -y wget && \
	apt-get install -y curl

COPY ./run /opt/run
COPY ./info /opt/info