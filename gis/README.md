# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [GIS](https://en.wikipedia.org/wiki/Geographic_information_system) (Geographic Information System), a system designed to capture, store, manipulate, analyze, manage, and present spatial or geographic data.

# Using the GIS image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/gis bash -c "Rscript /opt/gis && pdfcrop --margins '0 0 0 0' /data/Rplots.pdf && rm /data/Rplots.pdf"`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.

# Test data
Please make sure you first create a file named `data.csv` containing the latitude and longitude coordinates where your species was observed. The file header must be `"latitude,longitude"`. 

Your `data.csv` should present the following format:
```
latitude,longitude
-37.4,145
-35,-65
-34.4,-58.3
-33.3,-70.4
...
```

### *Note 1*
The previous command generates two files:
- `statistics`: a results file containing some statistics on the species presence points.
- `Rplots-crop.pdf`: a PDF file  showing the presence and predicted distribution of the species (probabilities are given as color codes). The prediction model used is the [Bioclim](https://support.bccvl.org.au/support/solutions/articles/6000083201-bioclim) model.

### *Note 2*
A folder named `wc2-5` containing data on 19 abiotic variables from [WorldClim](https://www.worldclim.org/) will be created, if not present.

# Using the GIS image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/gis bash -c "Rscript /opt/gis && pdfcrop --margins '0 0 0 0' /data/Rplots.pdf && rm /data/Rplots.pdf"`