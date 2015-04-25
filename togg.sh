#!/bin/bash

if [ ! $# == 1 ]; then
    echo "Uso: $0 ext"
    exit
fi
ext=$1
mkdir -p ogg
for i in *.$ext; do
    oggenc "$i" -q 6 -o ogg/"$i".ogg &
done
