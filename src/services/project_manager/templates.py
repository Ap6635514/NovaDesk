from pathlib import Path


def write(path: Path, content: str = ""):
    path.write_text(content, encoding="utf-8")


def create_python_project(project_path: Path, framework: str):

    folders = [
        "src",
        "docs",
        "assets",
        "tests"
    ]

    for folder in folders:
        (project_path / folder).mkdir(parents=True, exist_ok=True)

    # README
    write(
        project_path / "README.md",
        f"# {project_path.name}\n\nGenerated with NovaDesk 🚀\n"
    )

    # Requirements
    write(
        project_path / "requirements.txt",
        ""
    )

    # Git Ignore
    write(
        project_path / ".gitignore",
        """__pycache__/
*.pyc
.venv/
"""
    )

    # License
    write(
        project_path / "LICENSE",
        "MIT License"
    )

    # Framework Template

    if framework == "Tkinter":

        write(
            project_path / "src" / "main.py",
            """import tkinter as tk

root = tk.Tk()
root.title("New Project")
root.geometry("800x600")

root.mainloop()
"""
        )

    elif framework == "Flask":

        write(
            project_path / "src" / "app.py",
            """from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from NovaDesk!"

if __name__ == "__main__":
    app.run(debug=True)
"""
        )

    elif framework == "FastAPI":

        write(
            project_path / "src" / "main.py",
            """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from NovaDesk"}
"""
        )

    else:

        write(
            project_path / "src" / "main.py",
            """print("Hello World!")"""
        )