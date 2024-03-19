#!/bin/bash

product() {
    prod=1
    echo -n "The product of "
    for param in $@; do
        echo -n "$param "
        let prod*=$param
    done
    echo "is $prod"
}

if [ $# -eq 0 ]; then
    echo "Usage: ./$0 val [val [ ... ]]"
    echo "e.g., ./$0 17 49 3 466"
else
    product $@
fi

