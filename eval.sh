#!/bin/bash

INPUT_DIR="quora/trg" # processed files

REF_FILE="quora/test_trg.txt" # ref file

EXM_DIR="quora/exm" # exm files

PYTHON_SCRIPT="eval.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: $PYTHON_SCRIPT not found in the current directory."
    exit 1
fi

source "venv/bin/activate"

for input_file in "$INPUT_DIR"/processed_trg_gen*.txt; do
    if [ -f "$input_file" ]; then
        echo "Processing $input_file..."
        
        number=$(echo "$input_file" | grep -o '[0-9]\+')
        
        exm_file="$EXM_DIR/exm$number.txt"
        
        if [ ! -f "$exm_file" ]; then
            echo "Warning: Example file $exm_file not found. Skipping this evaluation."
            continue
        fi
        
        python "$PYTHON_SCRIPT" -i "$input_file" -r "$REF_FILE" -t "$exm_file"
        
        echo "Finished processing $input_file"
        echo "----------------------------------------"
    fi
done

echo "All files processed."