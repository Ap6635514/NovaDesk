import subprocess
import sys
from pathlib import Path


def run():

    root = Path(__file__).resolve().parents[3]

    print("🚀 Launching NovaDesk...\n")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app.app"
        ],
        cwd=root
    )