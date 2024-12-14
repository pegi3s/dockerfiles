FROM pegi3s/docker:20.04

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    jq \
    bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY generate_dockerfile.sh /usr/local/bin/generate_dockerfile.sh

RUN chmod +x /usr/local/bin/generate_dockerfile.sh

CMD ["/bin/bash"]
