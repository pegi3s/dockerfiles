

# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of HADDOCK2.4, which is an information-driven docking approach for the modelling of biomolecular complexes. A script is provided to facilitate the use of the protein-protein docking mode starting with PDB files from either AlphaFold, I-TASSER or PDB databases, as well as the analysis of the results, as performed in [Rocha et al. 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6814966/).

> [!WARNING]
> This image runs Docker in Docker. Users that are already running Docker 29 should start using the image with the version `2.4.2-docker29.0.1`, while users that did not yet update their Docker version to Docker 29 should use the image with the `2.4.2` tag. Starting with version `2.4.2-docker29.0.1`, from now on, only images that are compatible with Docker 29 or above will be released. You can check your Docker version by running the command: docker --version".

#### *Note 1*
Due to licensing issues, we are unable to provide the `cns_solve_1.3_all_intel-mac_linux` and `haddock2.4-2023-08` executables. They must be downloaded from the following pages: http://cns-online.org/cns_request/ and https://www.bonvinlab.org/software/haddock2.4/download/. We only guarantee that the docker image will work with haddock2.4-2023-08 version.
After obtaining those files, just put the two executables in a folder and use the following command to create a working docker image called pegi3s/haddock24:

`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v your/data/dir:/data pegi3s/haddock24-builder bash -c "cp /data/* ./ && docker build ./ -t pegi3s/haddock24"`

You just need to do this once, unless you erase the pegi3s/haddock24 image from your computer in which case you must repeat this step. In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the cns_solve and haddock2.4 executables.

# Using the haddock24 (protein-protein docking mode) image in Linux

Once the pegi3s/haddock24 image is created, you prepare a configuration file with the name `config` and the following structure:

ACTIVE1=active_sites1
ACTIVE2=active_sites2
PASSIVE1=passive_sites1
PASSIVE2=passive_sites2
PDB1=your_pdb1
PDB2=your_pdb2
ALL_FILES=y/n

Where `active_sites1` and `active_sites2` are the names of the active sites files, `passive_sites1` and `passive_sites2` are the names of the passive sites files and `your_pdb1` and `your_pdb2` are the names of your pdb files. The last line is a variable that allows you to return all the output files that are produced by HADDOCK or just the most important ones. If you want all the files just write y, otherwise put n.
	
You can now use the following command to run a local instance of the HADDOCK 2.4 software:

You should adapt and run the following command: 
`docker run --rm -v /your/data/dir:/data pegi3s/haddock24 bash -c “python3 main”`

In this command, you should replace:

- `/your/data/dir` to point to the directory that contains the PDB files, the lists of binding sites residues you want to use and the config file.

# Test data
We have created scripts that simplify the use of the examples provided by HADDOCK 2.4 to test all the possible docking modes. You can run the examples by changing `your_mode` in the following command to the chosen mode:

`docker run --rm -v /your/data/dir:/data pegi3s/haddock24 bash -c “./your_mode”`

Here are the list of the available modes:

    • pdna_run for protein-DNA docking.
    • plig_run for protein-ligand docking.
    • pligshape_run for template-based protein-ligand docking with shape restraints.
    • pp_run for protein-protein docking from an ensemble of NMR structures using CSP data.
    • ppdani_run for protein-protein docking from an ensemble of NMR structures using CSP data and diffusion anisotropy restraints.
    • ppem_run for protein-protein docking into a cryo-EM map.
    • ppepensemble_run for an example of ensemble-averaged PRE restraints. Docking with two copies of a peptide not seeing each other.
    • pppcs_run for protein-protein docking using NMR PCS restraints.
    • pprdc_run for protein-protein docking using NMR RDC restraints.
    • prefinepcs_run for an example of single structure water refinement with NMR PCS restraints.
    • ptetraCG_run for multi-body docking of a C4 tetramer with a coarse grained representation.
    • ptrimer_run for three body docking of a homotrimer using bioinformatic predictions.
    • refinecomplex_run for refinement of a complex in water (it0 and it1 skipped).
    • solvateddocking_run for solvated protein-protein docking (barnase-barstar) using bioinformatic predictions.

#### *Note 2*
We guarantee that HADDOCK (protein-protein docking mode) works with pdb files from AlphaFold, I-TASSER and PDB database. Therefore, there is no need to parse those files.


