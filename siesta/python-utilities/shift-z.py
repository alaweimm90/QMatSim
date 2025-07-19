#!/bin/bash

# Find all files with .STRUCT_IN and .STRUCT_OUT extensions in the current directory and subdirectories
find . -type f \( -name "*.STRUCT_IN" -o -name "*.STRUCT_OUT" \) | while read -r file; do
    # Process the file
    awk 'NR < 5 {print $0} NR >= 5 {$NF = $NF - 0.5; print $0}' "$file" > tmpfile && mv tmpfile "$file"
done
