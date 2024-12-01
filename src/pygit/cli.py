import os
from typing import Literal, TextIO

import click

from pygit.commands.hash_git_object import hash_git_object
from pygit.commands.init_repo import init_repo


@click.group()
@click.version_option()
def cli() -> None:
    "python git client"  # noqa: D300, D403
    click.echo("Welcome to pygit!")


@cli.command(name="init", help="init an empty git repository")
def init() -> Literal["hello"]:
    """Command description goes here."""
    init_repo()
    return "hello"


@cli.command(name="hash_object", help="init an empty git repository")
@click.argument("file", type=str)
def hash_object(file: str) -> None:
    """Command description goes here."""
    print("fille", file)
    with open(f"{file}", "rb") as f:
        print(hash_git_object(f.read()))
