# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)

This image facilitates the usage of the [Subread](https://subread.sourceforge.net/) package, which includes the read aligners (`subread-align`, `subjunc`), the read summarization program `featureCounts` and other related tools.

The following programs are available on the `PATH`:

- Alignment and related tools: `subread-align`, `subread-buildindex`, `subjunc`, `exactSNP`, `sublong`, `subindel` and `featureCounts`.
- Utilities: `flattenGTF`, `genRandomReads`, `propmapped`, `qualityScores`, `removeDup`, `repair`, `subread-fullscan`, `txUnique` and `detectionCall`.

To see the `featureCounts` help, just run `docker run --rm pegi3s/subread featureCounts -h`. To see the help of any other program, replace `featureCounts` by its name.

# Using the Subread image in Linux

You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/subread featureCounts -a /data/file.gff -o /data/output/output.txt /data/input.bam`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `file.gff` to the actual name of your annotation file in gff format.
- `output.txt` to the actual name of your output file.
- `input.bam` to the actual name of your alignment file in bam format.

# Test data

To test the previous command, you can download the following files:
- [annotation file](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/featurecounts/saccharomyces.gff) (12MB)
- [bam file](http://evolution6.i3s.up.pt/static/pegi3s/dockerfiles/featurecounts/saccharomyces_data.sorted.bam) (292MB).

The test BAM file contains paired-end reads, so the `-p` option is required, and `-g locus_tag` matches the gene identifier used in the annotation file. After replacing `/your/data/dir` by the actual working directory, run:

```
docker run --rm -v /your/data/dir:/data pegi3s/subread featureCounts -p -a /data/saccharomyces.gff -g locus_tag -o /data/saccharomyces_output.txt /data/saccharomyces_data.sorted.bam
```

# Using the Subread image in Windows

Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/subread featureCounts -a /data/file.gff -o /data/output/output.txt /data/input.bam`
