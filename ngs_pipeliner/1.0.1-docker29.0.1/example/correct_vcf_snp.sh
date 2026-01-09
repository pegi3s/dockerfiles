#!/bin/bash

blacklisted=(302 303 304 305 306 307 308 309 310 311 312 313 314 315 16184 16185 16186 16187 16188 16189 16190 16191 16192 16193)

if [[ $1 == "-h" ]]; then
    echo "Correct vcf files from Freebayes"
    echo "Only SNPs"
    echo "Remove mutations in blacklisted positions when using the -b flag"
    echo "Usage:"
    echo "  bash correct_vcf_snp.sh <input.vcf> <output.vcf> <-b>"
    echo "Get help with:"
    echo "  bash correct_vcf_snp.sh -h"
    exit
fi

if [[ $# -lt 2 ]]; then
    echo "Not enough arguments. Please provide input and output files."
    exit 1
fi

file=$1
out_file=$2

if [[ $3 == "-b" ]]; then
    blacklisted_enabled=true
else
    blacklisted_enabled=false
fi

while IFS=$'\t' read -r line || [[ -n $line ]]; do
    if [[ ${line:0:1} == "#" ]]; then
        echo "$line" >> "$out_file"
    else
        IFS=$'\t' read -ra line_split <<< "$line"
        if [[ " ${blacklisted[@]} " =~ " ${line_split[1]} " ]] && $blacklisted_enabled; then
            continue
        else
            if [[ ${#line_split[3]} -eq 1 ]]; then
                echo "$line" >> "$out_file"
            else
                ref=${line_split[3]}
                alt=${line_split[4]}
                if [[ ${#ref} -eq ${#alt} ]]; then
                    for (( n=0; n<${#ref}; n++ )); do
                        if [[ ${ref:n:1} != ${alt:n:1} ]]; then
                            new_line=""
                            for (( x=0; x<${#line_split[@]}; x++ )); do
                                if [[ $x -eq 1 ]]; then
                                    new_line+="$(( ${line_split[x]} + n ))"$'\t'
                                elif [[ $x -eq 3 ]]; then
                                    new_line+="${ref:n:1}"$'\t'
                                elif [[ $x -eq 4 ]]; then
                                    new_line+="${alt:n:1}"$'\t'
                                elif [[ $x -eq 9 ]]; then
                                    new_line+="${line_split[x]}"
                                else
                                    new_line+="${line_split[x]}"$'\t'
                                fi
                            done
                            echo "$new_line" >> "$out_file"
                        fi
                    done
                fi
            fi
        fi
    fi
done < "$file"
