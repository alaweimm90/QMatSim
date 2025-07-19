#!/bin/bash

# Loop through each folder
for folder in GGA GGA-SOC LDA; do
    # Loop through each .psml file in the folder
    for file in "$folder"/*.psml; do
        # Check if the file exists
        [ -e "$file" ] || continue
        
        # Extract the base name without extension
        base_name=$(basename "$file" .psml)
        
        # Set the output file name
        output_file="$folder/$base_name.psf"
        
        # Perform the conversion
        echo "Converting $file to $output_file"
        psml2psf -d -o "$output_file" "$file"
    done
done
