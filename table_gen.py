import subprocess
import re
from prettytable import PrettyTable

def extract_metrics(filename):
    try:
        cmd = f"grep 'bleu:' {filename}"
        output = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        
        match = re.search(r'bleu: ([\d.]+), rouge-1: ([\d.]+), rouge-2: ([\d.]+), rouge-l: ([\d.]+), meteor: ([\d.]+), syntax-TED: ([\d.]+), Template-TED: ([\d.]+)', output)
        
        if match:
            return {
                'bleu': float(match.group(1)),
                'rouge-1': float(match.group(2)),
                'rouge-2': float(match.group(3)),
                'rouge-l': float(match.group(4)),
                'meteor': float(match.group(5)),
                'syntax-ted': float(match.group(6)),
                'template-ted': float(match.group(7))
            }
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {filename}: {e}")
    return None

def create_metrics_table():
    files = ['l_0.001txt', 'l_0.01txt', 'l_0.3txt', 'l_0.5txt', 'l_0.7txt', 'l_1.0txt', 'l_1.3txt', 'l_1.5txt', 'l_1.7txt', 'l_2.5txt']
    results = {}
    
    for file in files:
        l_val = float(file[2:-3])
        metrics = extract_metrics(file)
        if metrics:
            results[l_val] = metrics

    # Create PrettyTable
    table = PrettyTable()
    table.field_names = ["L Value", "BLEU", "ROUGE-1", "ROUGE-2", "ROUGE-L", "METEOR", "Syntax-TED", "Template-TED"]
    
    # Set floating point precision
    table.float_format = '.3'
    
    # Add rows
    for l_val in sorted(results.keys()):
        metrics = results[l_val]
        table.add_row([
            f"{l_val:.1f}",
            metrics['bleu'],
            metrics['rouge-1'],
            metrics['rouge-2'],
            metrics['rouge-l'],
            metrics['meteor'],
            metrics['syntax-ted'],
            metrics['template-ted']
        ])

    print(table)

if __name__ == "__main__":
    create_metrics_table()
