# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# ID mapping

The `pegi3s/id-mapping` Docker image allows mapping identifiers using the [UniProt server](https://www.uniprot.org/id-mapping/) through the [Unipressed](https://github.com/multimeric/Unipressed) API client.

# General ID mapping (UniProt)

The main script is `map-ids`, so you should adapt and run the following command:
```sh
docker run --rm -v /your/data/dir:/data -w /data pegi3s/id-mapping map-ids --from-db <FROM_DB> --to-db <TO_DB> --input input.txt --output output.tsv
```

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to process.
- `input.txt` to the actual name of your input TXT file with the identifiers to map (one per line).
- `output.tsv` to the actual name of your output TSV file.
- `<FROM_DB>` to the actual name of the source database of the input identifiers.
- `<TO_DB>` to the actual name of the destination database.

The valid names for `<FROM_DB>` and `<TO_DB>` can be obtained with `docker run --rm pegi3s/id-mapping list-from-dbs` and `docker run --rm pegi3s/id-mapping list-to-dbs`, respectively.

The script help can be obtained with `docker run --rm pegi3s/id-mapping map-ids --help`.

Advanced script options are described in the next subsections.

## Cache

To avoid repeating time and again the same mapping queries it is possible to enable a cache mechanism by using the `--cache-dir <cache_dir_name>` parameter. This way, the script will maintain a cache of previous queries for each different combination of `<FROM_DB>` and `<TO_DB>`.

## Batch size and delay

By default, the script has a batch size of 10, which means that it will send queries with at most ten identifiers to the server. The default delay between queries is 1 second, which means that the script will wait for this time before sending a new batch query.

These values can be changed by specifying `--batch-size <BATCH_SIZE> --delay <DELAY_SECONDS>`.

## Test data

To test the `map-ids` script, start creating a new file named `ids.txt` with the following identifiers:

```
A1L190
A0JP26
A0PK11
```

And then run the following command (change `/your/data/dir` to the actual path to the `ids.txt` file)

```sh
docker run --rm -v /your/data/dir:/data -w /data \
    pegi3s/id-mapping map-ids \
        --from-db UniProtKB_AC-ID \
        --to-db Gene_Name \
        --input ids.txt \
        --output mapping.tsv \
        --cache-dir id_mapping_cache
```

The result will be available in the new `mapping.tsv` file created at `/your/data/dir`.

# Gene ID to reference UniProtKB

Conversions using the `map-ids` can produce multiple mappings for the same identifier. To overcome this issue for the specific case of mapping Gene IDs into UniProtKB IDs, the `gene-id-to-uniprotkb` script is provided. This script opens the corresponding NCBI page of the specified Gene ID (e.g. https://www.ncbi.nlm.nih.gov/gene/4287/ for Gene ID 4297) and retrieves the reference protein accession that appears at the bottom of the page (e.g. UniProtKB/Swiss-Prot:P54252 in this case). This way a single UniProtKB ID for a given gene can be found.

You should adapt and run the following command: 
```sh
docker run --rm -v /your/data/dir:/data -w /data pegi3s/id-mapping gene-id-to-uniprotkb input.txt output.tsv
```

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to process.
- `input.txt` to the actual name of your input TXT file with the Gene IDs to map (one per line).
- `output.tsv` to the actual name of your output file.

The script help can be obtained with `docker run --rm pegi3s/id-mapping gene-id-to-uniprotkb --help`.

Notes:
- The default output format (`--format` or `-f`) is `tsv`. This means that a two-column TSV file is produced (see test data below): original Gene IDs in the first column and converted UniProtKB IDs in the second one. The output format `txt` allows obtaining only a list of the mapped UniProtKB IDs.
- If an identifier cannot be found at NCBI it will appear in the output files as `Not found`. They can be ignored by adding `--ignore-missing` or `-i` to the command before.

Advanced script options are described in the next subsections.

## Cache

To avoid repeating time and again the same mapping queries it is possible to enable a cache mechanism by using the `--cache-dir <cache_dir_name>` parameter. This way, the script will maintain a cache of previous queries for each input Gene ID.

## Delay

The default delay between queries is 1 second, which means that the script will wait for this time before sending a new batch query.

These values can be changed by specifying `--delay <DELAY_SECONDS>`.

# Test data

To test the `gene-id-to-uniprotkb` script, start creating a new file named `gene_ids.txt` with the following identifiers:

```
4287
411
```

And then run the following command (change `/your/data/dir` to the actual path to the `gene_ids.txt` file)

```sh
docker run --rm -v /your/data/dir:/data -w /data \
    pegi3s/id-mapping gene-id-to-uniprotkb \
        gene_ids.txt \
        gene_ids_to_uniprotkbs_mapping.tsv \
        --format tsv \
        --cache-dir id_mapping_cache
```

The result will be available in the new `gene_ids_to_uniprotkbs_mapping.tsv` file created at `/your/data/dir`. It looks like the following:
```ts
GeneID  UniProtKB
4287    P54252
411     P15848
```

# Changelog

The `latest` tag contains always the most recent version.

## [1.1.0] - 22/01/2024

- Adds the `gene-id-to-uniprotkb` script.

## [1.0.0] - 28/07/2022

- Initial `id-mapping` image containing the `map-ids`, `list-from-dbs` and `list-to-dbs` scripts.