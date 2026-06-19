from pathlib import Path

ROOT = Path("src")

replacements = {
    'font=("Segoe UI", 30, "bold")': "font=TITLE",
    'font=("Segoe UI", 24, "bold")': "font=HEADING",
    'font=("Segoe UI", 22, "bold")': "font=HEADING",
    'font=("Segoe UI", 20, "bold")': "font=HEADING",
    'font=("Segoe UI", 18, "bold")': "font=SUBTITLE",
    'font=("Segoe UI", 18)': "font=SUBTITLE",
    'font=("Segoe UI", 16)': "font=BODY",
    'font=("Segoe UI", 15)': "font=BODY",
    'font=("Segoe UI", 14)': "font=BODY",

    "padx=30": "padx=PAGE",
    "padx=40": "padx=PAGE",

    "pady=20": "pady=SECTION",
    "pady=25": "pady=SECTION",
}


for file in ROOT.rglob("*.py"):

    text = file.read_text(encoding="utf-8")

    changed = False

    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            changed = True

    if changed:

        if "from src.ui.themes.fonts import *" not in text:
            text = (
                "from src.ui.themes.fonts import *\n"
                "from src.ui.themes.spacing import *\n"
                "from src.ui.themes.colors import *\n\n"
            ) + text

        file.write_text(text, encoding="utf-8")

        print("Updated:", file)

print("\n✅ Theme refactor complete!")