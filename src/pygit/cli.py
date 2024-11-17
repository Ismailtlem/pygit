import random
import sys

import click

# from sorting_techniques import pysort


@click.group()
@click.version_option()
def cli() -> None:
    "python git client"


@cli.command(name="init", help="init an empty git repository")
def sort():
    "Command description goes here"
    print("hhellooooo init")
    return "hello"
