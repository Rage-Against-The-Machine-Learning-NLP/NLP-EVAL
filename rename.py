import os
import shutil

def move_lambda_files():
    # Ensure the target directory exists
    target_dir = 'results/lambda_same'
    os.makedirs(target_dir, exist_ok=True)
    
    # Get all files in current directory
    files = os.listdir('.')
    
    # Move lambda files
    for file in files:
        if file.startswith('lambda_') and file.endswith('.txt'):
            shutil.move(file, os.path.join(target_dir, file))
            print(f'Moved: {file} -> {target_dir}/{file}')

if __name__ == '__main__':
    move_lambda_files()