import os
from prettytable import PrettyTable
import re

def extract_metrics(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        # Find the line with metrics
        pattern = r'bleu: ([\d.]+), rouge-1: ([\d.]+), rouge-2: ([\d.]+), rouge-l: ([\d.]+), meteor: ([\d.]+), syntax-TED: ([\d.]+), Template-TED: ([\d.]+)'
        match = re.search(pattern, content)
        if match:
            return {
                'BLEU': float(match.group(1)),
                'ROUGE-1': float(match.group(2)),
                'ROUGE-2': float(match.group(3)),
                'ROUGE-L': float(match.group(4)),
                'METEOR': float(match.group(5)),
                'Syntax-TED': float(match.group(6)),
                'Template-TED': float(match.group(7))
            }
    return None

def create_comparison_table(directory, title):
    table = PrettyTable()
    table.title = title
    table.field_names = ["Model", "BLEU", "ROUGE-1", "ROUGE-2", "ROUGE-L", "METEOR", "Syntax-TED", "Template-TED"]
    table.float_format = '.3'

    # Get all files and their metrics
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            metrics = extract_metrics(os.path.join(directory, filename))
            if metrics:
                model_name = filename.replace('.txt', '')
                results.append((model_name, metrics))
    
    # Sort alphabetically by model name
    results.sort(key=lambda x: x[0].lower())
    
    # Add rows to table
    for model_name, metrics in results:
        table.add_row([
            model_name,
            metrics['BLEU'],
            metrics['ROUGE-1'],
            metrics['ROUGE-2'],
            metrics['ROUGE-L'],
            metrics['METEOR'],
            metrics['Syntax-TED'],
            metrics['Template-TED']
        ])
    
    return table

# Create tables for each directory
directories = {
    'results/lambda_same': 'Lambda (Same) Comparison',
    'results/lambda_different': 'Lambda (Different) Comparison',
    'results/bert': 'BERT Model Comparison',
    'results/bert_layers': 'BERT Layer Configuration Comparison',
    'results/quantized': 'Quantization Comparison',
    'results/seq2seq_variation': 'Seq2Seq Variation Comparison'
}

for directory, title in directories.items():
    if os.path.exists(directory):
        table = create_comparison_table(directory, title)
        print(table)
        print("\n" + "="*100 + "\n")