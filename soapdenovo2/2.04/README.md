# Using the SOAPdenovo2 image in Linux
Please, note that the following instructions must be executed in Linux environments only.

The `SOAPdenovo2` manual can be found [here](https://github.com/aquaskyline/SOAPdenovo2). This image allows you to use the main `SOAPdenovo2` scripts, namely:
- `SOAPdenovo-127mer`
- `SOAPdenovo-63mer`
- `SOAPdenovo-fusion`

For instance, you can show the help associated to the `SOAPdenovo-127mer` program by running: `docker run --rm pegi3s/soapdenovo2 SOAPdenovo-127mer`

To run any of the three programs, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/soapdenovo2 SOAPdenovo-127mer <command> [option]`

In this command, you should replace `/your/data/dir` to point to the directory that contains the input files you want to analyze and specify the appropiate command and options in your case.
