from pathlib import Path
import shutil

ROOT = Path.cwd()

deleted = 0

print("🧹 Cleaning Python cache...\n")

# Remove __pycache__ folders
for folder in ROOT.rglob("__pycache__"):
    shutil.rmtree(folder, ignore_errors=True)
    print(f"🗑 Removed: {folder}")
    deleted += 1

# Remove .pyc files
for file in ROOT.rglob("*.pyc"):
    try:
        file.unlink()
        print(f"🗑 Removed: {file}")
    except Exception:
        pass

print("\n==============================")
print(f"✅ Removed {deleted} cache folders")
print("==============================")