#!/bin/bash

sum() {
    sum=0
    echo -n "The sum of "
    for param in $@; do
        echo -n "$param "
        let sum+=$param
    done
    echo "is $sum"
}

if [ $# -eq 0 ]; then
    echo "Usage: bash $0 val [val [ ... ]]"
    echo "e.g., bash $0 17 49 3 466"
else
    sum $@
fi