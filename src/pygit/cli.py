import os
from typing import (
    Literal,
)

import click

# from commands.hash_object import hash_git_object
from commands.init import init_repo


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


# @cli.command(name="hash_object", help="init an empty git repository")
# @click.argument("file", type=click.File("r"))
# def hash_object(file: str) -> None:
#     """Command description goes here."""
#     with open(file, "rb") as f:
#         print(hash_git_object(f.read()))
