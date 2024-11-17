import os

import click


@click.group()
@click.version_option()
def cli() -> None:
    "python git client"  # noqa: D300, D403
    click.echo("Welcome to pygit!")


@cli.command(name="init", help="init an empty git repository")
def init():
    """Command description goes here."""
    DIRECTORY_NAME = ".git"
    DIRS_LIST = ["hooks", "info", "objects", "refs"]
    try:
        os.mkdir(f"{DIRECTORY_NAME}")
        print(f"Directory '{DIRECTORY_NAME}' created successfully.")
    except FileExistsError:
        print(f"Directory '{DIRECTORY_NAME}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{DIRECTORY_NAME}'.")
    # for file in FILES_LIST:
    with open(f"{DIRECTORY_NAME}/HEAD", "w") as f:
        f.write("ref: refs/heads/master")
    with open(f"{DIRECTORY_NAME}/config", "w") as f:
        f.write("")
    with open(f"{DIRECTORY_NAME}/description", "w") as f:
        f.write(
            "Unnamed repository; edit this file 'description' to name the repository."
        )

    for folder in DIRS_LIST:
        os.mkdir(f"{DIRECTORY_NAME}/{folder}")

    return "hello"
