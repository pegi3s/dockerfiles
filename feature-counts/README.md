# This image belongs to a larger project called Bioinformatics Docker Images Project (http://pegi3s.github.io/dockerfiles)
## (Please note that the original software licenses still apply)
This image facilitates the usage of [FeatureCounts](https://www.rdocumentation.org/packages/Rsubread/versions/1.22.2/topics/featureCounts) a general-purpose read summarization function.
To see the [FeatureCounts](https://www.rdocumentation.org/packages/Rsubread/versions/1.22.2/topics/featureCounts) help, just run `docker run --rm pegi3s/feature-counts -h`.

# Using the FeatureCounts image in Linux
You should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/feature-counts featureCounts -a /data/file.gff -o /output/output.txt /data/input.bam`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input file you want to process.
- `file.gff` to the actual name of your annotation file in gff.
- `output.txt` to the actual name of your output file.
- `input.bam` to the actual name of your alignment file in bam.

# Test data
To test the previous command, you can download the following files:
- [annotation file]() (12MB)
- [bam file]() (292MBB).

In the previous command you just need to replace `/data/file.gff` with `/data/saccharomyces.gff` and `/data/input.bam` with `/data/saccharomyces_data.sorted.bam`.

# Using the FeatureCounts image in Windows
Please note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

You should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/feature-counts featureCounts -a /data/file.gff -o /output/output.txt /data/input.bam`
