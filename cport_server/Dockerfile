FROM pegi3s/utilities

RUN apt-get update && \
	apt-get install -y wget && \
	apt-get install -y curl && \
	apt-get install -y lynx

COPY ./run /opt/run
COPY ./info /opt/info

RUN chmod u+x /opt/run
RUN chmod u+x /opt/info
