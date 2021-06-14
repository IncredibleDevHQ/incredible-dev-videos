#!/bin/bash 
dir="$1"
for file in "$dir"/*
do
    mv "$file" "$file.new"
done
