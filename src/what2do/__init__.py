"""
what2do - Find TODO comments in code files
"""

__version__ = "0.1.3"

from .core import find_todos, find_scope, output_todos
from .git_history import get_todo_history, format_todo_history

__all__ = [
    "find_todos",
    "find_scope", 
    "output_todos",
    "get_todo_history",
    "format_todo_history",
    "__version__"
] 