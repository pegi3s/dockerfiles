# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [GBIF](https://www.gbif.org/) (Global Biodiversity Information Facility - an international network and research infrastructure funded by the world’s governments and aimed at providing anyone, anywhere, open access to data about all types of life on Earth) data to predict species distributions.

# Using the GBIF image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/gbif_gis bash -c "/opt/run <species_name>"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<species_name>` to the actual name of the species.

For instance, if the selected species is `Solanum acaule*`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/gbif_gis bash -c "/opt/run Solanum acaule*"`

### *Note 1*
The previous command generates three files:
- `data.csv`:  a coordinates file showing the geographic coordinates of where the species was recorded.
- `statistics`: a results file containing some statistics on the species presence points.
- `Rplots-crop.pdf`:  a PDF file showing the presence and predicted distribution of the species (probabilities are given as color codes). The prediction model used is the [Bioclim](https://support.bccvl.org.au/support/solutions/articles/6000083201-bioclim) model.

### *Note 2*
A folder named `wc2-5` containing data on 19 abiotic variables from [WorldClim](https://www.worldclim.org/) will be created, if not present.

# Using the GBIF image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/gbif_gis bash -c "/opt/run <species_name>"`