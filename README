# WhatToDo

command-line tool that scans directories for TODO comments in code files and generates a report.

## Features

- Searches for TODO comments in specified file types
- Collects context, scope, and metadata for each TODO
- Outputs results to console, TSV, or Markdown format

** _Note: this script is not intended to be a full-featured code analysis tool, it's just some regexs - the scope identification is very basic and could be improved._

## Usage

```
python whattodo.py [path] [--extensions EXT [EXT ...]] [--output OUTPUT]
```

### Arguments

- `-p` or `--path`: Directory to search (default: current directory)
- `-e` or `--extensions`: File extensions to search (default: .py .R .sh .c .cpp .pl)
- `-o` or `--output`: Output file path (optional, .tsv or .md)

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

6. Combine options:
   ```
   python whattodo.py /path/to/project --extensions .py .js --output todos.md
   ```

## Requirements

- Python 

## Installation

1. Clone this repository or download the `whattodo.py` file.
2. write `python whattodo.py` to the command line.
3. success!

## License
[MIT License](LICENSE)