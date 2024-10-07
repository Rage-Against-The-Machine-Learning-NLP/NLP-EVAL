#!/bin/bash

INPUT_DIR="out/trg"

PYTHON_SCRIPT="process.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: $PYTHON_SCRIPT not found in the current directory."
    exit 1
fi

for file in "$INPUT_DIR"/*; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        python3 "$PYTHON_SCRIPT" "$file"
        
        processed_file="processed_$(basename "$file")"
        if [ -f "$processed_file" ]; then
            mv "$processed_file" "$INPUT_DIR/"
            echo "Moved processed file to $INPUT_DIR/$processed_file"
        else
            echo "Warning: Processed file $processed_file not found."
        fi
    fi
done

echo "All files processed."