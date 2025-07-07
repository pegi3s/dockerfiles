FROM pegi3s/docker

# Install dependencies (Java for Nextflow, curl to download)
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Nextflow
RUN curl -fsSL https://get.nextflow.io | bash && \
    mv nextflow /usr/local/bin/

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["bash"]
