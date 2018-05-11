# Using the SPAdes image

The `SPAdes` manual can be found [here](http://spades.bioinf.spbau.ru/release3.11.1/manual.html). This image allows you to use the main `SPAdes` scripts, namely:
- `spades.py` (main executable script)
- `dipspades.py` (main executable script for dipSPAdes)
- `metaspades.py` (main executable script for metaSPAdes)
- `plasmidspades.py` (main executable script for plasmidSPAdes)
- `rnaspades.py` (main executable script for rnaSPAdes)
- `truspades.py` (main executable script for truSPAdes)

For instance, you can show the help associated to the `spades.py` main script by running: `docker run --rm pegi3s/spades spades.py --help`

To run this main script, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/spades spades.py [options] -o /data`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `data` to the actual results directory.
- `[options]` with the input data and other parameters. Refer to the [SPAdes manual](http://spades.bioinf.spbau.ru/release3.11.1/manual.html#sec3.2) to know how this information should be given.