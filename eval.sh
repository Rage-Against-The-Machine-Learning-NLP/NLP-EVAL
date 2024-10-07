#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: Please provide the input directory name."
    echo "Usage: $0 <input_directory_name>"
    exit 1
fi

BASE_DIR="$1"
INPUT_DIR="$BASE_DIR/trg" # processed files
REF_FILE="$BASE_DIR/test_trg.txt" # ref file
EXM_DIR="$BASE_DIR/exm" # exm files

PYTHON_SCRIPT="eval.py"

if [ ! -d "$BASE_DIR" ]; then
    echo "Error: Directory $BASE_DIR does not exist."
    exit 1
fi

if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Directory $INPUT_DIR does not exist."
    exit 1
fi

if [ ! -f "$REF_FILE" ]; then
    echo "Error: Reference file $REF_FILE does not exist."
    exit 1
fi

if [ ! -d "$EXM_DIR" ]; then
    echo "Error: Directory $EXM_DIR does not exist."
    exit 1
fi

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