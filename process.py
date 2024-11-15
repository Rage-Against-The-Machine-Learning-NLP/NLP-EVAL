import sys
import os

def process_file(input_path):
    with open(input_path, 'r') as f:
        generated_data = f.readlines()

    preprocessed_data = []
    for line in generated_data:
        # Split by EOS and take first part
        preprocessed_line = line.split("EOS")[0].strip()
        # Remove <UNK> tokens
        preprocessed_line = preprocessed_line.replace("<UNK>", "")
        preprocessed_line = preprocessed_line.replace("UNK", "")
        # Remove all remaining < and > characters
        preprocessed_line = preprocessed_line.replace("<", "").replace(">", "")
        # Remove any potential double spaces created by removals
        preprocessed_line = " ".join(preprocessed_line.split())
        preprocessed_data.append(preprocessed_line + '\n')

    base_name = os.path.basename(input_path)
    output_file = f"processed_{base_name}"

    with open(output_file, 'w') as f:
        f.writelines(preprocessed_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_file(input_path)
