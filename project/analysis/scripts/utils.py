"""Utils function"""

# std import
import json
import os
import pathlib

# pip import


def get_relative_script_path(work_path: str, script_path: str) -> str:
    """Generate script path relative to working directory"""

    return os.path.relpath(script_path, work_path)


def chunk(word: str, chunk_size: int = 1):
    """
    Take an string yield chunk of word with size n.

    If last chunk isn't complete return incomplete chunk.
    """

    return [word[i : i + chunk_size] for i in range(0, len(word), chunk_size)]
