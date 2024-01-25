#!/bin/bash

for dir in test*; do 
    echo "[test] Running test $dir"
    cd $dir

    docker run --rm -it \
        -v "$(pwd):$(pwd)" -w "$(pwd)" \
        -e HUMAN_PROT_ATLAS_FILE="human_prot_atlas.tsv" \
        pegi3s/human_prot_atlas \
            config.txt input.txt test_output.txt cache

    exit_status=$?

    if [ $dir == "test3" ]; then
        if  [ ${exit_status} -eq 1 ]; then
            echo "[test] $dir SUCCESS"
        else
            echo "[test] $dir FAILED"
            exit 1
        fi
    else
        if cmp --silent -- "expected_output.txt" "test_output.txt"; then
            echo "[test] $dir SUCCESS"
        else
            echo "[test] $dir FAILED"
            bat "expected_output.txt"
            bat "test_output.txt"
            exit 1
        fi

        rm -f test_output.txt
    fi

    cd ..
done

echo "[test] All tests passed! :-D"