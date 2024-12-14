I wanted to install sva with BiocManager::install(c('sva')).

* DONE (RSQLite)
ERROR: dependency ‘UCSC.utils’ is not available for package ‘GenomeInfoDb’
* removing ‘/usr/local/lib/R/site-library/GenomeInfoDb’
ERROR: dependency ‘GenomeInfoDb’ is not available for package ‘Biostrings’
* removing ‘/usr/local/lib/R/site-library/Biostrings’
ERROR: dependencies ‘httr’, ‘Biostrings’ are not available for package ‘KEGGREST’
* removing ‘/usr/local/lib/R/site-library/KEGGREST’
ERROR: dependency ‘KEGGREST’ is not available for package ‘AnnotationDbi’
* removing ‘/usr/local/lib/R/site-library/AnnotationDbi’
ERROR: dependencies ‘AnnotationDbi’, ‘XML’, ‘httr’ are not available for package ‘annotate’
* removing ‘/usr/local/lib/R/site-library/annotate’
ERROR: dependencies ‘AnnotationDbi’, ‘annotate’ are not available for package ‘genefilter’
* removing ‘/usr/local/lib/R/site-library/genefilter’
ERROR: dependency ‘genefilter’ is not available for package ‘sva’
* removing ‘/usr/local/lib/R/site-library/sva’

Trying to install UCSC.utils failed because openssl was not found. Try installing:
 * deb: libssl-dev 

 Configuration failed because libcurl was not found. Try installing:
 * deb: libcurl4-openssl-dev (Debian, Ubuntu, etc)

Then I tried installing sva again

ERROR: dependency ‘XML’ is not available for package ‘annotate’
* removing ‘/usr/local/lib/R/site-library/annotate’
ERROR: dependency ‘annotate’ is not available for package ‘genefilter’
* removing ‘/usr/local/lib/R/site-library/genefilter’
ERROR: dependency ‘genefilter’ is not available for package ‘sva’
* removing ‘/usr/local/lib/R/site-library/sva’

And resolved it by installing libxml2-dev (apt)

Then tried again sva