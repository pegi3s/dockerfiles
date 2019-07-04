# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [TaxoDros](http://www.taxodros.uzh.ch/) (the database on Taxonomy of Drosophilidae) data to predict species distributions.

# Using the TaxoDros image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/taxodros_gis bash -c "/opt/run <unique_short_form>"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<unique_short_form>` to the actual [TaxoDros unique short form](https://www.taxodros.uzh.ch/search/bin/names_lookup.php?what=vnm&letter=m&from=dist_sreg.php).

For instance, if the selected short form is `'melanogaster 1'`, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/taxodros_gis bash -c "/opt/run 'melanogaster 1'"`

### *Note 1*
The previous command generates three files: 
- `data.csv`: a coordinates file showing the geographic coordinates of where the species was recorded.
- `statistics`: a results file containing some statistics on the species presence points.
- `Rplots-crop.pdf`: a PDF file showing the presence and predicted distribution of the species (probabilities are given as color codes). The prediction model used is the [Bioclim](https://support.bccvl.org.au/support/solutions/articles/6000083201-bioclim) model.

### *Note 2*
A folder named `wc2-5` containing data on 19 abiotic variables from [WorldClim](https://www.worldclim.org/) will be created, if not present.

# Using the TaxoDros image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/taxodros_gis bash -c "/opt/run <unique_short_form>"`