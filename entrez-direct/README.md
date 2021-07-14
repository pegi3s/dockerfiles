# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image allows the usage of the [Entrez Direct](https://www.ncbi.nlm.nih.gov/books/NBK179288/) utilities, including:

- Navigation functions support exploration within the Entrez databases:
    - `esearch` performs a new Entrez search using terms in indexed fields.
    - `elink` looks up neighbors (within a database) or links (between databases).
    - `efilter` filters or restricts the results of a previous query.

- Records can be retrieved in specified formats or as document summaries:

    - `efetch` downloads records or reports in a designated format.

- Desired fields from XML results can be extracted without writing a program:

    - `xtract` converts EDirect XML output into a table of data values.

- Several additional functions are also provided:

    - `einfo` obtains information on indexed fields in an Entrez database.
    - `epost` uploads unique identifiers (UIDs) or sequence accession numbers.
    - `nquire` sends a URL request to a web page or CGI service.

# Using the Entrez Direct image in Linux

To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/entrez-direct <entrez-direct-command> <options>`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<entrez-direct-command>` to the name of the Entrez Direct command you want to use.
- `<options>` with the specific options of the Entrez Direct command. These options will include the input/output files if required, which should be referenced under `/data/`.

# Examples

## Example 1: retrieve FASTA sequences from accession numbers

To download the FASTA sequences from the accession numbers *XM_016057909.1* and *XM_030992799.1*, the `epost` and `efetch` commands can be used. The steps are:
- Create a file named `accessions.txt` with these accessions.
- Run `epost` using the accessions file as input and write the result to `epost.result`.
- Run `efetch` using the `epost.result` as input and write result to `sequences.fastap`.

```
echo -e "XM_016057909.1\nXM_030992799.1" > accessions.txt
docker run --rm -v /your/data/dir:/data pegi3s/entrez-direct epost -db nuccore -format uid -input /data/accessions.txt > epost.result
docker run --rm -v /your/data/dir:/data pegi3s/entrez-direct bash -c "efetch -format fasta < /data/epost.result > /data/sequences.fasta"
```

Alternatively, the output of the `epost` command can be piped to the `efetch` command:

```
docker run --rm -v /your/data/dir:/data pegi3s/entrez-direct bash -c "echo -e \"XM_016057909.1\nXM_030992799.1\" | epost -db nuccore -format uid | efetch -format fasta > /data/sequences.fasta"
```

## Example 2: retrieve taxonomy information for a given species

To retrieve the taxonomy information for a for a given species, the `esearch` and `efetch` commands can be used. For instance, the following commands downloads the taxonomy of *Homo sapiens* into a `taxonomy.xml` file:

```
docker run --rm -v /your/data/dir:/data pegi3s/entrez-direct bash -c "esearch -db taxonomy -query "Homo+sapiens" | efetch -db taxonomy -format xml > /data/taxonomy.xml"
```

# Using the Entrez Direct image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/entrez-direct <entrez-direct-command> <options>`
