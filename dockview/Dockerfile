FROM pegi3s/docker:29.0.1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y python3-docker

ARG dockview_version
ENV DOCKVIEW_VERSION=${dockview_version}

COPY dockview.py /opt/dockview.py

ENTRYPOINT ["python3", "/opt/dockview.py"] 
