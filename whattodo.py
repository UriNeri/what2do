import os
import re
import argparse
import csv
from datetime import datetime

def find_todos(path, file_extensions):
    todos = []
    todo_pattern = re.compile(r'#+\s*(?:TODO|todo)[\s:-](.+)', re.IGNORECASE)
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        match = todo_pattern.search(line)
                        if match:
                            context = lines[i-1].strip() if i > 0 else ''
                            scope = find_scope(lines[:i+1])
                            todos.append({
                                'file': file,
                                'path': os.path.abspath(file_path),
                                'todo': match.group(1).strip(),
                                'context': context,
                                'scope': scope,
                                'modified': datetime.fromtimestamp(os.path.getmtime(file_path))
                            })
                            print(f"Found todo in {file_path} at line {i} with scope {scope}")
    return todos

def find_scope(lines):
    for line in reversed(lines):
        if re.match(r'^\s*(def|class|namespace)\s+\w+', line):
            return line.strip()
    return 'main'

def output_todos(todos, output_file):
    if not todos:
        print("No TODOs found")
        return
        
    if not output_file:
        for todo in todos:
            print(f"File: {todo['file']}")
            print(f"Path: {todo['path']}")
            print(f"TODO: {todo['todo']}")
            print(f"Context: {todo['context']}")
            print(f"Scope: {todo['scope']}")
            print(f"Modified: {todo['modified']}")
            print()
    else:
        # Default to TSV if extension isn't .md
        if output_file.endswith('.md'):
            with open(output_file, 'w') as f:
                for todo in todos:
                    f.write(f"- **File:** {todo['file']}\n")
                    f.write(f"  - Path: {todo['path']}\n")
                    f.write(f"  - TODO: {todo['todo']}\n")
                    f.write(f"  - Context: {todo['context']}\n")
                    f.write(f"  - Scope: {todo['scope']}\n")
                    f.write(f"  - Modified: {todo['modified']}\n\n")
        else:
            # Use TSV format for all other cases
            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=todos[0].keys(), delimiter='\t')
                writer.writeheader()
                writer.writerows(todos)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find TODO comments in code files.')
    parser.add_argument('-p', '--path', nargs='?', default='.', help='Path to search (default: current directory)')
    parser.add_argument('-e', '--extensions', nargs='+', default=['.py', '.R', '.sh', '.c', '.cpp', '.pl'],
                        help='File extensions to search (default: .py .R .sh .c .cpp .pl)')
    parser.add_argument('-o', '--output', help='Output file path (optional, .tsv or .md)')
    args = parser.parse_args()

    todos = find_todos(args.path, args.extensions)
    output_todos(todos, args.output)
    # TODO: this is literatlly a test todo lol

