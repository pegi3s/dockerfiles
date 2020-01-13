FROM pegi3s/r_project

ENV version 2.21.5
ENV PICARD /usr/local/bin/picard/picard.jar

WORKDIR /usr/local/bin/picard/

RUN apt-get update -y && apt-get install -y \
    libnss-sss \
    openjdk-8-jre \
    curl \
    less \
    vim  \
    wget

RUN mkdir -p /usr/local/bin/picard \
    && curl -SL https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar \
    > /usr/local/bin/picard/picard.jar

RUN chmod 0644 /usr/local/bin/picard/picard.jar

ENTRYPOINT ["java", "-Dpicard.useLegacyParser=false", "-jar", "/usr/local/bin/picard/picard.jar"]
