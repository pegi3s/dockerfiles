library(org.Hs.eg.db)

#
# This function is a wrapper around AnnotationDbi::mapIds that allows for mapping multiple columns at once
# using "first" or "asNA" for the multiVals parameter.
# 
# The function also handles the behaviour of AnnotationDbi::mapIds when any of the keys are not found in 
# the database. By default, the function raises an error, which is not raises if at least one key is mapped.
#
multipleMapIds <- function(db, keys, keytype, multiVals, columns) {
    mapping_list <- lapply(columns, function(column) {
        tryCatch({
            AnnotationDbi::mapIds(db, keys = keys, column = column, keytype = keytype, multiVals = multiVals)
        }, error = function(e) {
            rep(NA, length(keys))
        })
    })
    
    mapping_df <- data.frame(keys)
    colnames(mapping_df) <- keytype
    
    for (i in seq_along(columns)) {
        mapping_df[[columns[i]]] <- as.vector(mapping_list[[i]])
    }
    
    return(mapping_df)
}

columns <- c("ENTREZID", "SYMBOL", "GENENAME")

ensembl_ids = c("ENSG00000207389", "ENSG00000264940", "ENSG00000261136", "ENSG00000290535")
(mapping <- multipleMapIds(org.Hs.eg.db, ensembl_ids, "ENSEMBL", "first", columns))


# Write the mapping to a TSV file

args <- commandArgs(TRUE)
out_dir <- args[1]
write.table(mapping, file = paste0(out_dir, "/ensembl_mapping.tsv"), sep = "\t", row.names = FALSE, quote = FALSE)