#!/bin/bash 

echo -n "Checking seqkit ..."

LATEST_SEQKIT=$(curl -s -H "Accept: application/vnd.github+json" https://api.github.com/repos/shenwei356/seqkit/releases | jq '.[]."tag_name"' -r | head -1 | sed 's/^v//')

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/seqkit | grep -q "${LATEST_SEQKIT}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_SEQKIT}"
else
    echo " up-to-date"
fi

echo -n "Checking BLAST ..."

LATEST_BLAST=$(wget -q ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/VERSION -O-)

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/blast | grep -q "${LATEST_BLAST}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_BLAST}"
else
    echo " up-to-date"
fi

echo -n "Checking fastqc ..."

LATEST_FASTQC=$(wget -q https://www.bioinformatics.babraham.ac.uk/projects/download.html#fastqc -O- | grep 'fastqc_v' | grep 'zip' | sed 's/.*fastqc_v//g; s/.zip.*//')

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/fastqc | grep -q "${LATEST_FASTQC}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_FASTQC}"
else
    echo " up-to-date"
fi

echo -n "Checking sratoolkit ..."

LATEST_SRATOOLKIT=$(wget -q https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current.version -O-)

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/sratoolkit | grep -q "${LATEST_SRATOOLKIT}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_SRATOOLKIT}"
else
    echo " up-to-date"
fi

echo -n "Checking bedtools ..."

LATEST_BEDTOOLS=$(curl -s -L https://api.github.com/repos/arq5x/bedtools2/releases | jq '.[]."tag_name"' -r | head -1 | sed 's/^v//')

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/bedtools | grep -q "${LATEST_BEDTOOLS}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_BEDTOOLS}"
else
    echo " up-to-date"
fi

echo -n "Checking ncbi-datasets ..."

LATEST_NCBI_DATASETS=$(curl -s -L https://api.github.com/repos/ncbi/datasets/releases | jq '.[]."tag_name"' -r | head -1 | sed 's/^v//')

docker run --rm pegi3s/utilities dockerhub_list_repo_with_tags pegi3s/ncbi-datasets | grep -q "${LATEST_NCBI_DATASETS}"

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_NCBI_DATASETS}"
else
    echo " up-to-date"
fi
