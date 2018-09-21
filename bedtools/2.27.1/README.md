This image allows the usage of the `BedTools` suite - a fast and flexible toolset for genome arithmetic. `BedTools` allows to intersect, merge, count, complement, and shuffle genomic intervals from multiple files in widely-used genomic file formats such as BAM, BED, GFF/GTF, VCF.

By running the command `docker run --rm -v /your/data/dir:/data pegi3s/bedtools bedtools -h` you can list the tools included in this suite, namely:

- `annotateBed`: annotate coverage of features from multiple files.
- `bamToBed`: convert BAM alignments to BED (& other) formats.
- `bamToFastq`: convert BAM records to FASTQ records.
- `bed12ToBed6`: breaks BED12 intervals into discrete BED6 intervals.
- `bedToBam`: convert intervals to BAM records.
- `bedToIgv`: create an IGV snapshot batch script.
- `bedpeToBam`: convert BEDPE intervals to BAM records.
- `bedtools`: print help menu.
- `closestBed`: find the closest, potentially non-overlapping interval.
- `clusterBed`: cluster (but don’t merge) overlapping/nearby intervals.
- `complementBed`: extract intervals not represented by an interval file.
- `coverageBed`: compute the coverage over defined intervals.
- `expandCols`: replicate lines based on lists of values in columns.
- `fastaFromBed`: use intervals to extract sequences from a FASTA file.
- `flankBed`: create new intervals from the flanks of existing intervals.
- `genomeCoverageBed`: compute the coverage over an entire genome.
- `getOverlap`: computes the amount of overlap from two intervals.
- `groupBy`: group by common cols. & summarize oth. cols. (~ SQL “groupBy”)
- `intersectBed`: find overlapping intervals in various ways.
- `linksBed`: create a HTML page of links to UCSC locations.
- `mapBed`: apply a function to a column for each overlapping interval.
- `maskFastaFromBed`: use intervals to mask sequences from a FASTA file.
- `mergeBed`: combine overlapping/nearby intervals into a single interval.
- `multiBamCov`: counts coverage from multiple BAMs at specific intervals.
- `multiIntersectBed`: identifies common intervals among multiple interval files.
- `nucBed`: profile the nucleotide content of intervals in a FASTA file.
- `pairToBed`: find pairs that overlap intervals in various ways.
- `pairToPair`: find pairs that overlap other pairs in various ways.
- `randomBed`: generate random intervals in a genome.
- `shiftBed`: adjust the position of intervals.
- `shuffleBed`: randomly redistribute intervals in a genome.
- `slopBed`: adjust the size of intervals.
- `sortBed`: order the intervals in a file.
- `subtractBed`: remove intervals based on overlaps b/w two files.
- `tagBam`: tag BAM alignments based on overlaps with interval files.
- `unionBedGraphs`: combines coverage intervals from multiple BEDGRAPH files.
- `windowBed`: find overlapping intervals within a window around an interval.
- `windowMaker`: make interval “windows” across a genome.

*Note*: You may notice some mismatches between the tools names shown in the help list and the names of the corresponding executable functions. Check it please, by performing:

```
docker run -it pegi3s/bedtools
ls /opt/bedtools2/bin/
``` 
In case the mismatch happens, you should use the names of the executable functions.

To obtain the help of a particular application, you just need to run: `docker run --rm -v /your/data/dir:/data pegi3s/bedtools bedtools <bedtools-application-name>` (e.g. `docker run --rm -v /your/data/dir:/data pegi3s/bedtools bedtools fastaFromBed`)

# Using the BedTools image in Linux
To run an application, you should adapt and run the following command: `docker run --rm -v /your/data/dir:/data pegi3s/bedtools <bedtools-application-name> -fi <input FASTA> -bed <BED/GFF/VCF> -fo /data/stdout`

In this command, you should replace:
- `/your/data/dir` to point to the directory that contains the input files you want to analyze.
- `<bedtools-application-name>` to the name of the `BedTools` application you want to use.
- `<input FASTA>` to the actual name of your input FASTA file.
- `<BED/GFF/VCF>` to the actual name of your input BED/GFF/VCF file.
- `stdout` to the actual name of your output file.

For instance, to use the `fastaFromBed` application, you should run: `docker run --rm -v /your/data/dir:/data pegi3s/bedtools fastaFromBed -fi /data/input_fasta -bed /data/input_gff -fo /data/stdout`

*Note*: In order to use a less complex BED/GFF/VCF file you may want to filter it for exons first, for example, by performing:

```
grep -P "\texon\t" input_gff
``` 

# Using the BedTools image in Windows

Please, note that data must be under the same drive than the Docker Toolbox installation (usually `C:`) and in a folder with write permissions (e.g. `C:/Users/User_name/`).

As in the Linux case, to run an application, you should adapt and run the following command: `docker run --rm -v "/c/Users/User_name/dir/":/data pegi3s/bedtools <bedtools-application-name> -fi <input FASTA> -bed <BED/GFF/VCF> -fo /data/stdout`
