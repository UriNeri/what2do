"""
Core functionality for finding TODO comments in code files.
"""

import os
import re
import csv
from datetime import datetime
from typing import List, Dict, Optional, Union


def find_todos(path: str, file_extensions: List[str], ignore_hidden: bool = True, 
               ignore_paths: Optional[List[str]] = None) -> List[Dict[str, Union[str, datetime]]]:
    """
    Find TODO comments in code files.
    
    Args:
        path: Path to search for files
        file_extensions: List of file extensions to search (e.g., ['.py', '.js'])
        ignore_hidden: Whether to ignore hidden files and directories
        ignore_paths: List of path patterns to ignore
        
    Returns:
        List of dictionaries containing TODO information
    """
    todos = []
    todo_pattern = re.compile(r'#+\s*(?:TODO|todo)[\s:-](.+)', re.IGNORECASE)
    
    for root, _, files in os.walk(path):
        # Skip hidden directories if ignore_hidden is True
        if ignore_hidden:
            # Normalize the path and check if any part is hidden
            path_parts = os.path.normpath(root).split(os.sep)
            if any(part.startswith('.') and part not in ['.', '..'] for part in path_parts):
                continue
            
        # Skip ignored paths
        if ignore_paths and any(ignored in root for ignored in ignore_paths):
            continue
            
        for file in files:
            if file.endswith(tuple(file_extensions)):
                # Skip hidden files if ignore_hidden is True
                if ignore_hidden and file.startswith('.'):
                    continue
                    
                file_path = os.path.join(root, file)
                try:
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
                                print(f"Found todo in {file_path} at line {i+1} with scope {scope}")
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Warning: Could not read file {file_path}: {e}")
                    continue
                    
    return todos


def find_scope(lines: List[str]) -> str:
    """
    Find the scope (function, class, etc.) of a TODO comment.
    
    Args:
        lines: List of code lines up to and including the TODO line
        
    Returns:
        String describing the scope
    """
    for line in reversed(lines):
        if re.match(r'^\s*(def|class|namespace)\s+\w+', line):
            return line.strip()
    return 'main'


def output_todos(todos: List[Dict[str, Union[str, datetime]]], output_file: Optional[str] = None) -> None:
    """
    Output TODO list to console or file.
    
    Args:
        todos: List of TODO dictionaries
        output_file: Optional output file path (.md for markdown, otherwise TSV)
    """
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
            with open(output_file, 'w', encoding='utf-8') as f:
                for todo in todos:
                    f.write(f"- **File:** {todo['file']}\n")
                    f.write(f"  - Path: {todo['path']}\n")
                    f.write(f"  - TODO: {todo['todo']}\n")
                    f.write(f"  - Context: {todo['context']}\n")
                    f.write(f"  - Scope: {todo['scope']}\n")
                    f.write(f"  - Modified: {todo['modified']}\n\n")
        else:
            # Use TSV format for all other cases
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=todos[0].keys(), delimiter='\t')
                writer.writeheader()
                writer.writerows(todos) 