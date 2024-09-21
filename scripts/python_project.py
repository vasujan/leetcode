#!/usr/bin/env python3
import argparse
from pathlib import Path
import shutil

def add_dunder_init(path):
    """
    Add __init__.py to every folder and subfolder given a path.

    Args:
        path (str): The path to start adding the __init__.py

    Notes:
        This function will add __init__.py to all subfolders of the given path
    """
    skip_list = ['.pytest_cache', '__pycache__']
    for p in Path(path).glob('**/'):
        if p.name in skip_list:
            continue
        print(p)
        if not (p / '__init__.py').exists():
            # touch the file
            (p / '__init__.py').touch()

def remove_cache_folders(root_dir: str) -> None:
    """Remove .pytest_cache and __pycache__ folders from a directory tree.

    Args:
        root_dir (str): The directory to start removing .pytest_cache and __pycache__ from
    """
    for path in Path(root_dir).glob('**/'):
        if path.name in ['.pytest_cache', '__pycache__']:
            shutil.rmtree(str(path))

def main():
    parser = argparse.ArgumentParser(description='Manage Python project folders')
    subparsers = parser.add_subparsers(dest='command')

    add_init_parser = subparsers.add_parser('--init', help='Add __init__.py to folders')
    add_init_parser.add_argument('path', help='Path to start adding __init__.py')

    remove_cache_parser = subparsers.add_parser('--remove-cache', help='Remove .pytest_cache and __pycache__ folders')
    remove_cache_parser.add_argument('path', help='Path to remove cache folders from')

    args = parser.parse_args()

    if args.command == 'add-init':
        add_dunder_init(args.path)
    elif args.command == 'remove-cache':
        remove_cache_folders(args.path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

