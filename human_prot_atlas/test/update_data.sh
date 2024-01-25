#!/bin/bash

for dir in test*; do 
    rm -rf $dir/cache
    cp -R data/cache $dir
    cp data/input.txt $dir/input.txt
done