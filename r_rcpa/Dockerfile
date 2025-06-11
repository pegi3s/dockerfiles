FROM r-base:4.4.2

RUN apt-get update -y \
    && apt-get install -y libssl-dev libcurl4-openssl-dev libxml2-dev libudunits2-dev libgdal-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV R_REMOTES_NO_ERRORS_FROM_WARNINGS=true

ADD list_r_packages.sh list_r_packages.sh
RUN chmod u+x list_r_packages.sh

RUN R -e "install.packages('BiocManager')" \
    && echo 'n' | R --no-save -e "BiocManager::install(c('AnnotationDbi', 'SummarizedExperiment', 'Biobase', 'DESeq2', 'GEOquery', 'edgeR', 'limma', 'graph', 'org.Hs.eg.db', 'fgsea', 'ROntoTools'))" \
    && echo 'n' | R --no-save -e "install.packages(c('gridExtra', 'RCPA', 'GSA', 'CePa'))"

CMD ["/list_r_packages.sh"]
