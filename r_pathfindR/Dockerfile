FROM r-base:4.4.0

RUN apt-get update -y \
    && apt-get install -y libssl-dev libcurl4-openssl-dev libxml2-dev libfontconfig1-dev libmagick++-dev openjdk-8-jre pandoc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e "install.packages('BiocManager')" \
    && echo 'n' | R --no-save -e "BiocManager::install(c('AnnotationDbi', 'org.Hs.eg.db', 'ggkegg'))" \
    && echo 'n' | R --no-save -e "install.packages(c('pathfindR'))"

CMD ["/list_r_packages.sh"]
