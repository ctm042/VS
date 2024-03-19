#!/bin/bash

gcd(){
    local gcd=1
    local a=$1
    local b=$2
    if [ $a -eq 0 ]; then
        let gcd=$2
    fi
    if [ $b -eq 0 ]; then
        let gcd=$1
    fi
    local r=0
    while [ $b -gt 0 ]; do
        let r=$a%$b     #remainder
        let a=$b   #a becomes b
        let b=$r    #b becomes r
    done
    let gcd=$a
    echo -n "$gcd"
}

echo -n "gcd of $1 and $2 is "
gcd $@