# Bioinformatics Docker Images Contributing Guide 

This guide is for anyone interested in contributing to the project with new images.

Creating a new image involves:
1. Providing image files (at least `Dockerfile`, `README.md`, and `BUILD.md`) in a new folder named `image_name/image_version`.
2. Adding image metadata by editing the `metadata/metadata.json` file.
3. Classifying the image by editing the `metadata/dio.diaf` file.
4. Publishing the image on Docker Hub.

# 1. Image files

Image files should be placed in `image_name/image_version`. This way, images will be created as `pegi3s/image_name:image_version`.

It is strongly recommended to create images with fixed versions. Thus, Dockerfiles must be fully reproducible.

The tag `latest` will always point to the most recent version available. In case of creating a generic `Dockerfile` that allows building several images, as described in [the building guide](BUILD.md), image files can be placed, for instance, at `image_name/2.x` (`blast` or `seqkit` are examples of this).

At least three files must be provided for any image:
- `Dockerfile`: A reproducible Dockerfile that builds an image with a specific version of the software and its dependencies. Some of them may declare a default command or an entrypoint.
- `README.md`: Details about the image and instructions on how to run it.
- `BUILD.md`: Instructions on how to build the image if necessary.

See [the building guide](BUILD.md) for more details about build images.

## Choosing a base image

The most common base images to use as `FROM` in the Dockerfiles are:
- `ubuntu` with different tags (`23.04`, `22.04`, and so on).
- `python` with different tags (`3.9`, `3.9.19-bullseye`, `3.9.19-slim-bullseye`). Useful when Python is the main dependency required.
- `pegi3s/docker` with different tags (`20.04`, `18.04`). Useful when Docker is required for _docker-in-docker_ images.
- `continuumio/miniconda3`. Useful when conda is required to install dependencies.
- `pegi3s/utilities`. Useful when utility scripts from this image are required. It can be used in multi-stage builds (see `blast_utilities` for an example of this).

# 2. Image metadata

The `metadata/metadata.json` file must be edited to add metadata about the image. This allows our website and other applications to know which images are available in a dynamic fashion.

Consider this entry for `cutadapt` as reference:

```json
{
    "name": "cutadapt",
    "description": "Sequence read trimming",
    "status": "Usable",
    "recommended": "1.16",
    "latest": "1.16",
    "useful": [""],
    "bug_found": [""],
    "not_working": [""],
    "recommended_last_tested": "",
    "no_longer_tested": [""],
    "pegi3s_url": "https://hub.docker.com/r/pegi3s/cutadapt/",
    "manual_url": "https://cutadapt.readthedocs.io/en/stable/guide.html",
    "github_url": "https://github.com/pegi3s/dockerfiles/tree/master/cutadapt",
    "comments": ["To see the Cutadapt⁠ help, just run -h."],
    "gui": false,
    "podman": "untested",
    "singularity": "untested",
    "invocation_general": "docker run --rm -v /your/data/dir:/data pegi3s/cutadapt ",
    "invocation_general_comments": ["/your/data/dir to point to the directory that contains the input file you want to process."],
    "usual_invocation_specific": "-u 10 /data/input.fq -o /data/output.fq",
    "usual_invocation_specific_comments": ["input.fq to the actual name of your input file.","output.fq to the actual name of your output file.","A negative value after -u would trims reads at the end."],
    "test_invocation_specific": "",
    "test_data_url": "",
    "test_results_url": "",
    "icon": "",
  },
```

The following fields are mandatory:
- `name`: image name (i.e. the folder name).
- `description`: brief description of the image.
- `status`: one of `Usable`, `Unusable`, `Not_recommended`, or `Useful`.
- `latest`: version of the software available as latest.
- `pegi3s_url`: URL to the pegi3s Docker Hub.
- `manual_url`: external URL to the software user manual or documentation.
- `github_url`: URL to the pegi3s GitHub folder.
- `gui`: true or false.
- `podman`: one of `untested` or `tested`.
- `singularity`": one of `untested` or `tested`.
- `invocation_general`: the base `docker run` command without arguments.
- `invocation_general_comments`: comments about `invocation_general`.
- `usual_invocation_specific`: command arguments to add to `invocation_general` and obtaining a full working command.
- `usual_invocation_specific_comments`: comments about `usual_invocation_specific`.

Other fields may remain empty although it is encouraged to provide them, specially test data.

# 3. Image classification

We have developed an ontology for images classification, provided in the OBO format at `metadata/dio.obo`.

The final step is assigning one or more ontology terms to the new image. These classifications are assigned in the `metadata/dio.diaf` file (_Docker Images Annotation File_).

This file is just a TSV file with two columns: the ontology term and the image name. Consider `seda` as reference, which has two classifications associated:

```ts
DIO:0000022	seda
DIO:0000029	seda
```

In case you need a new classification, please inform us using a GitHub issue and we will update the ontology.

# 4. Image release

Releasing the image at Docker Hub must be done by our team. Thus, if you contribute with a new image, please inform us using a GitHub issue and we will publish it after checking it meets the above guidelines.
