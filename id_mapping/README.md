# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

# ID mapping

The `pegi3s/id-mapping` Docker image allows mapping identifiers using the [UniProt server](https://www.uniprot.org/id-mapping/) through the [Unipressed](https://github.com/multimeric/Unipressed) API client.

The main script is `map-ids`, so you should adapt and run the following command: 
```sh
docker run --rm -v /your/data/dir:/data -w /data pegi3s/id-mapping --from-db <FROM_DB> --to-db <TO_DB> --input input.txt --output output.tsv
```

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to process.
- `input.txt` to the actual name of your input TXT file with the identifiers to map (one per line).
- `output.tsv` to the actual name of your output TSV file.
- `<FROM_DB>` to the actual name of the source database of the input identifiers.
- `<TO_DB>` to the actual name of the destination database.

The valid names for `<FROM_DB>` and `<TO_DB>` can be obtained with `docker run --rm pegi3s/id-mapping list-from-dbs` and `docker run --rm pegi3s/id-mapping list-to-dbs`, respectively.

The script help can be obtained with `docker run --rm pegi3s/id-mapping map-ids -h`.

Advanced script options are described in the next subsections.

## Cache

To avoid repeating time and again the same mapping queries it is possible to enable a cache mechanism by using the `--cache-dir <cache_dir_name>` parameter. This way, the script will maintain a cache of previous queries for each different combination of `<FROM_DB>` and `<TO_DB>`.

## Batch size and delay

By default, the script has a batch size of 10, which means that it will send queries with at most ten identifiers to the server. The default delay between queries is 1 second, which means that the script will wait for this time before sending a new batch query.

These values can be changed by specifying `--batch-size <BATCH_SIZE> --delay <DELAY_SECONDS>`.

# Test data

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

# Changelog

The `latest` tag contains always the most recent version.

## [1.0.0] - 28/07/2022

- Initial `id-mapping` image containing the `map-ids`, `list-from-dbs` and `list-to-dbs` scripts.