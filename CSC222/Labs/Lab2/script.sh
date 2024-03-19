#!/bin/bash

tot=0
while read line; do
    echo -n "$line" | grep -c '^'
    
done < "${1:-/dev/stdin}"
