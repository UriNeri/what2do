# WhatToDo

command-line tool that scans directories for TODO comments in code files and generates a report.

## Features

- Searches for TODO comments in specified file types
- Collects context, scope, and metadata for each TODO
- Outputs results to console, TSV, or Markdown format
- Tracks TODO history through git commits (when enabled)
  - Shows when TODOs were added or removed
  - Includes commit information (author, date, message)
  - Supports both text and markdown output formats

** _Note: this script is not intended to be a full-featured code analysis tool, it's just some regexs - the scope identification is very basic and could be improved._

## Usage

```
python whattodo.py [path] [--extensions EXT [EXT ...]] [--output OUTPUT] [--git-history] [--git-history-format {text,markdown}]
```

### Arguments

- `-p` or `--path`: Directory to search (default: current directory)
- `-e` or `--extensions`: File extensions to search (default: .py .R .sh .c .cpp .pl)
- `-o` or `--output`: Output file path (optional, .tsv or .md)
- `--git-history`: Include git history for TODOs (tracks when TODOs were added/removed)
- `--git-history-format`: Format for git history output ('text' or 'markdown', default: text)
- `--include-hidden`: Include hidden files and directories
- `--ignore-paths`: Additional paths to ignore

### Examples

1. Search current directory with default settings:
   ```
   python whattodo.py
   ```

2. Search a specific directory:
   ```
   python whattodo.py /path/to/project
   ```

3. Specify custom file extensions:
   ```
   python whattodo.py --extensions .py .js .html
   ```

4. Output to a TSV file:
   ```
   python whattodo.py --output todos.tsv
   ```

5. Output to a Markdown file:
   ```
   python whattodo.py --output todos.md
   ```

6. Include git history in markdown format:
   ```
   python whattodo.py --git-history --git-history-format markdown
   ```

7. Combine options:
   ```
   python whattodo.py /path/to/project --extensions .py .js --output todos.md --git-history
   ```

## Requirements

- Python 
- Git (optional, required for git history functionality)

## Installation

There are two ways to install what2do:

### 1. Using pip (recommended)

```bash
pip install what2do
```

After installation, you can run the tool directly:
```bash
what2do --help
```

### 2. From source

1. Clone this repository:
```bash
git clone https://github.com/urineri/what2do.git
cd what2do
```

2. Install in development mode:
```bash
pip install -e .
```

3. Run the tool:
```bash
what2do --help
```

## License
[MIT License](LICENSE)