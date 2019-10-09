# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of [jModelTest2](https://github.com/ddarriba/jmodeltest2/blob/master/README.md), a  tool to carry out statistical selection of best-fit models of nucleotide substitution. It implements five different model selection strategies: hierarchical and dynamical likelihood ratio tests (`hLRT` and `dLRT`), Akaike and Bayesian information criteria (`AIC` and `BIC`), and a decision theory method (`DT`). It also provides estimates of model selection uncertainty, parameter importances and model-averaged parameter estimates, including model-averaged tree topologies.

# Using the jModelTest2 image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/jmodeltest2 java -jar /jmodeltest2/dist/jModelTest.jar -d /data/input -g <number_rate_categories> -i -f -AIC -BIC -a -o /data/output`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to analyze.
- `input` to the actual name of your input file.
- `<number_rate_categories>` to the gamma models rate categories number.
- `output` to the actual name of your output file.

For instance, in order to test gamma models with 4 rate categories and then perform the model selection using Akaike (`AIC`) and Bayesian (`BIC`) criteria, calculating also a model averaged phylogeny, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/jmodeltest2 java -jar /jmodeltest2/dist/jModelTest.jar -d /data/input -g 4 -i -f -AIC -BIC -a -o /data/output`

# Test data
To test the previous command, you can copy and paste [this sample data](https://raw.githubusercontent.com/pegi3s/dockerfiles/master/jmodeltest2/2.1.10/test_data/input) into the `input`file.

# Running the jModelTest2 GUI in Linux
This docker image can be also used to run the `jModelTest2` GUI. To do so, just run: `docker run --rm -ti -e USERID=$UID -e USER=$USER -e DISPLAY=$DISPLAY -v /var/db:/var/db:Z -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/developer/.Xauthority -v "/your/data/dir:/data" pegi3s/jmodeltest2 java -jar /jmodeltest2/dist/jModelTest.jar `

If the above command fails, try running `xhost +` first.

# Using the jModelTest2 image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/jmodeltest2 java -jar /jmodeltest2/dist/jModelTest.jar -d /data/input -g <number_rate_categories> -i -f -AIC -BIC -a -o /data/output`
