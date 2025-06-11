FROM r-base:4.4.2

RUN apt-get update -y \
    && apt-get install -y libssl-dev libcurl4-openssl-dev libxml2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e "install.packages('BiocManager')" \
    && echo 'n' | R --no-save -e "BiocManager::install(c('AnnotationDbi', 'org.Hs.eg.db', 'hgu95av2.db', 'GO.db', 'EnsDb.Hsapiens.v75', 'TxDb.Hsapiens.UCSC.hg19.knownGene'))"

CMD ["/list_r_packages.sh"]

