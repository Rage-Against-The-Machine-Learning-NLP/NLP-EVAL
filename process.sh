#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: Please provide the input directory name."
    echo "Usage: $0 <input_directory_name>"
    exit 1
fi

INPUT_DIR="$1/trg"
PYTHON_SCRIPT="process.py"

if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Directory $INPUT_DIR does not exist."
    exit 1
fi

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