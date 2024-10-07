import sys
import os

def process_file(input_path):
    with open(input_path, 'r') as f:
        generated_data = f.readlines()

    preprocessed_data = []
    for line in generated_data:
        preprocessed_line = line.split("EOS")[0].strip()
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