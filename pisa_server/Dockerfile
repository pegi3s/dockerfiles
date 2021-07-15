FROM pegi3s/utilities

RUN apt-get update && \
	apt-get install -y wget && \
	apt-get install -y curl && \
	apt-get install -y lynx

COPY ./run /opt/run
RUN cp /opt/scripts/pisa_xml_extract /opt

RUN chmod a+x /opt/run
