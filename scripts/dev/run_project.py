import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

print("🚀 Starting NovaDesk...")
print("Python:", sys.executable)
print("Working Directory:", ROOT)

subprocess.run(
    [
        sys.executable,
        "-m",
        "src.app.app"
    ],
    cwd=ROOT,
    check=True
)