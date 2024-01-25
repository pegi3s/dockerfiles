# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)

The `pegi3s/human_prot_atlas` Docker image allows filtering lists of UniProtKB identifiers based on their presence in tissues from the [Human Protein Atlas](https://www.proteinatlas.org/) database.

# Using the human_prot_atlas image in Linux

You should adapt and run the following command:
```sh
docker run --rm -v /your/data/dir:/data -w /data pegi3s/human_prot_atlas config.txt input.txt output.txt cache_dir
```

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the file you want to process.
- `input.txt` to the actual name of your input TXT file with the UniProtKB identifiers. In case you need convert identifiers, have a look at the `pegi3s/id-mapping` Docker image [here](https://hub.docker.com/r/pegi3s/id-mapping).
- `output.txt` to the actual name of your output TXT file with the filtered identifiers.
- `config.txt` to the actual name of your input TXT file with the configuration parameters (see below).
- `cache_dir` to the actual name of the cache directory (optional but recommended).

## Help and useful information

To see program help, just run `docker run --rm pegi3s/human_prot_atlas --help`. 

To list the available tissues, just run `docker run --rm pegi3s/human_prot_atlas --list`.

## Configuration parameters

These are the configuration parameters that must be included in the configuration text file:

```
human_prot_atlas_tissue_include=*|TissueA;TissueB;TissueC
human_prot_atlas_tissue_include_mode=intersection|union
human_prot_atlas_tissue_exclude=TissueD;TissueF;TissueG
```
Where:
- `human_prot_atlas_tissue_include` can take the value `*` or a list of tissue names separated by `;`. Using `*` means that all available tissues are included (except those explicitly listed in the `human_prot_atlas_tissue_exclude`). If not provided, `*` is used by default.
- `human_prot_atlas_tissue_include_mode` can be `union` or `intersection` (see below). If not provided, `union` is used by default.
- `human_prot_atlas_tissue_exclude` can be empty or a list of tissue names separated by `;`.

## Filtering procedure

The program performs the following procedure:
1. Create a list of included UniProtKB identifiers:
   - In `union` mode, all identifiers are taken into account.
   - In `intersection` mode, only identifiers present in all included tissues at the same time are taken into account.
2. From the previous list, subtract the identifiers contained in each excluded tissue.
3. Filter the input list to retain only those identifiers present in the list obtained in step 2.

## Test data

To test the program, download this [ZIP file](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/human_prot_atlas/test_data/human_prot_atlas.zip) and decompress it. Then run the following command:

```sh
docker run --rm -v "$(pwd):$(pwd)" -w "$(pwd)" pegi3s/human_prot_atlas config.txt input.txt output.txt cache
```

The result will be available in the new `output.txt` file created at your current working directory. The `cache` directory contains the Human Protein Atlas files for the specified tissues and can be reused in future program runs.

# Changelog

The `latest` tag contains always the most recent version.

## [1.0.0] - 25/01/2024

- Initial `pegi3s/human_prot_atlas` version.