#!/bin/bash

if [ ! $# == 1 ]; then
    echo "Uso: $0 ext"
    exit
fi
ext=$1
mkdir -p ogg

if [ $ext == 'mp3' ]; then
    for i in *.mp3; do
        lame --decode "$i" "$i".wav
    done
    ext="wav"
fi

for i in *.$ext; do
    oggenc "$i" -q 6 -o ogg/"$i".ogg &
done
