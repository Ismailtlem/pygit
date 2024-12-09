import argparse
import os
import sys
from pathlib import Path
from typing import Literal, TextIO

import click

# from pygit.commands import cat_file_cmd, hash_git_cmd, init_repo_cmd
# from pygit.commands.helpers import is_file_ignored
from . import base, data


@click.group()
@click.version_option()
def cli() -> None:
    """Welcome to Pygit."""
    pass


@cli.command(name="init", help="init an empty git repository")
def init() -> None:
    """Command description goes here."""
    data.init()
    print(f"Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}")


@cli.command(name="hash-object", help="Create a hash for a git object")
@click.argument("file_path", type=str)
def hash_object(file_path: str) -> None:
    """Convert an existing file into a git object."""
    with open(file_path, "rb") as f:
        print(data.hash_object(f.read()))


@cli.command(name="cat-file", help="Get the initially hashed object")
@click.argument("file_hash", type=str)
def cat_file(file_hash: str) -> None:
    """Read a git object to see its clear content."""
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(file_hash, expected=None))


@cli.command(name="commit", help="Create a commit")
# @click.option("-m", type=str)
@click.argument("message", type=str)
def comit(message: str) -> None:
    """Read a git object to see its clear content."""
    print(base.commit(message))


@cli.command(name="write-tree", help="Write the current directory to git objects")
def write_tree() -> None:
    """Read a git object to see its clear content."""
    print(base.write_tree())


# @cli.command(name="commit", help="Create a commit and write it to the tree")
# @click.option("-m", type=str)
# def commit() -> None:
#     """Read a git object to see its clear content."""
#     print(base.commit(args.message))


@cli.command(name="read-tree", help="Write the current directory to git objects")
def read_tree() -> None:
    """Read a git object to see its clear content."""
    print(base.write_tree())
