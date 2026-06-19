from pathlib import Path
import shutil


def clean():

    root = Path(__file__).resolve().parents[3]

    removed = 0

    print("🧹 Cleaning NovaDesk cache...\n")

    EXCLUDED = {
        ".venv",
        ".git",
        ".idea",
        ".vscode",
        "node_modules",
    }

    for folder in root.rglob("__pycache__"):

        if any(part in EXCLUDED for part in folder.parts):
            continue

        shutil.rmtree(folder, ignore_errors=True)

        print("🗑", folder.relative_to(root))

        removed += 1

    for file in root.rglob("*.pyc"):

        if any(part in EXCLUDED for part in file.parts):
            continue

        try:
            file.unlink()
        except Exception:
            pass

    print("\n==========================")
    print(f"✅ Removed {removed} cache folders")
    print("==========================")