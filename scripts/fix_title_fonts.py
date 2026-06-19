from pathlib import Path

ROOT = Path("src/ui/pages")

files = [
    "about.py",
    "projects.py",
    "settings.py",
    "workspace.py",
]

OLD = 'font=("Segoe UI", 32, "bold")'
NEW = "font=TITLE"

for filename in files:

    path = ROOT / filename

    text = path.read_text(encoding="utf-8")

    if OLD in text:
        text = text.replace(OLD, NEW)

        path.write_text(text, encoding="utf-8")

        print(f"✅ Updated {filename}")

print("\n🎉 Done!")