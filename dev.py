import sys

from scripts.dev.commands.run import run
from scripts.dev.commands.clean import clean

VERSION = "0.1.0"


def help_menu():
    print(f"""
╔════════════════════════════════════════════╗
║            🌌 NovaDesk Developer CLI       ║
╚════════════════════════════════════════════╝

Version : {VERSION}

Usage:
    python dev.py <command>

Available Commands

    🚀 run         Launch NovaDesk
    🧹 clean       Clean Python cache
    🧪 test        Run tests
    📁 project     Project tools
    🌿 git         Git helper
    📦 build       Build executable
    ℹ version      Show CLI version
    ❓ help         Show this menu
""")


COMMANDS = {
    "run": run,
    "clean": clean,
}


def main():

    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1].lower()

    if command in ("help", "-h", "--help"):
        help_menu()
        return

    if command in ("version", "-v", "--version"):
        print(f"NovaDesk CLI v{VERSION}")
        return

    if command in COMMANDS:
        COMMANDS[command]()
    else:
        print(f"\n❌ Unknown command: {command}\n")
        help_menu()


if __name__ == "__main__":
    main()