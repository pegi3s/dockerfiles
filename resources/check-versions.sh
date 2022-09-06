#!/bin/bash 

echo -n "Checking seqkit ..."

LATEST_SEQKIT=$(curl -s -H "Accept: application/vnd.github+json" https://api.github.com/repos/shenwei356/seqkit/releases | jq '.[]."tag_name"' -r | sort -r | head -1 | sed 's/^v//')

grep -q ${LATEST_SEQKIT} seqkit/*/BUILD.md

if [ $? == 1 ]; then
    echo " new version available: ${LATEST_SEQKIT}"
else
    echo " up-to-date"
fi
