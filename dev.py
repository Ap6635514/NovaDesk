import argparse

from src.cli.commands.run import run
from src.cli.commands.clean import clean
from src.cli.commands.project import project

VERSION = "1.0.0"


def main():

    parser = argparse.ArgumentParser(
        prog="NovaDesk",
        description="🌌 NovaDesk Developer CLI"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"NovaDesk CLI {VERSION}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    subparsers.add_parser(
        "run",
        help="Launch NovaDesk"
    )

    subparsers.add_parser(
        "clean",
        help="Clean Python cache"
    )

    subparsers.add_parser(
        "project",
        help="Create a new project"
    )

    commands = {
        "run": run,
        "clean": clean,
        "project": project,
    }

    args = parser.parse_args()

    if args.command:
        commands[args.command]()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()