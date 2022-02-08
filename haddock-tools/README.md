# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [Haddock-tools](https://github.com/haddocking/haddock-tools), a collection of useful programs for the preparation of `HADDOCK` runs.

# Using the Haddock-tools image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/<haddock-tool-and-parameters>"`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<haddock-tool-and-parameters>` to the name of the `Haddock-tool` you want to use and respective parameters.
    
## *Note*

For some `HADDOCK` tools their location is different than `/opt/haddock-tools/`

# Examples

Several examples of the usage of `Haddock-tools` are given below (the test files can be obtained [here](https://github.com/pegi3s/dockerfiles/tree/master/haddock-tools/test_data)):

## Examples 1

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/molprobity.py /data/1f3g.pdb > /data/1f3g_output"`

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/passive_from_active.py /data/1f3g.pdb 38,40,45,46,69,71,78,80,94,96,141 > /data/1f3g_passive"`

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/active-passive-to-ambig.py /data/1f3g_active_passive /data/1hdn_m1_cport_active_passive > /data/1f3g_1hdn_m1.tbl"`

### *Note 1* 

In the `Haddock-tools` manual the name of this script is incorrectly listed as `active-passive_to_ambig.py`

## Example 2

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "cd /opt/haddock-tools/haddock_tbl_validation && python validate_tbl.py /data/1f3g_1hdn_m1.tbl"`

### *Note 2*

The `validate_tbl.py` script is in a different place than the remaining scripts.

## Examples 3

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "cd /opt/haddock-tools && python calc-accessibility.py /data/1f3g.pdb 2> /data/output"`

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/pdb_blank_chain /data/1f3g.pdb > /data/1f3g_blank_chain.pdb"`

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/pdb_blank_segid /data/1f3g.pdb > /data/1f3g_blank_segid.pdb"`

`docker run --rm -v /your/data/dir:/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/pdb_setchain -v CHAIN=A /data/1f3g.pdb > /data/1f3g_chain.pdb"`

# Using the Haddock-tools image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/haddock-tools:git_07.06.2021 bash -c "/opt/haddock-tools/<haddock-tool-and-parameters>"`
