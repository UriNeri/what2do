"""
Command-line interface for what2do.
"""

import argparse
from .core import find_todos, output_todos


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Find TODO comments in code files.')
    parser.add_argument('-p', '--path', nargs='?', default='.', 
                        help='Path to search (default: current directory)')
    parser.add_argument('-e', '--extensions', nargs='+', 
                        default=['.py', '.R', '.sh', '.c', '.cpp', '.pl'],
                        help='File extensions to search (default: .py .R .sh .c .cpp .pl)')
    parser.add_argument('-o', '--output', 
                        help='Output file path (optional, .tsv or .md)')
    parser.add_argument('--include-hidden', action='store_true', 
                        help='Include hidden files and directories (default: hidden files are ignored)')
    parser.add_argument('--ignore-paths', nargs='+', 
                        help='Additional paths to ignore')
    parser.add_argument('--git-history', action='store_true',
                        help='Include git history for TODOs (default: False)')
    parser.add_argument('--git-history-format', choices=['text', 'markdown'], default='text',
                        help='Format for git history output (default: text)')
    
    args = parser.parse_args()

    ignore_hidden_value = not args.include_hidden
    todos = find_todos(args.path, args.extensions, 
                      ignore_hidden=ignore_hidden_value, 
                      ignore_paths=args.ignore_paths,
                      include_git_history=args.git_history,
                      git_history_format=args.git_history_format)
    output_todos(todos, args.output)
    # TODO: this is literally a test todo lol


if __name__ == '__main__':
    main() 