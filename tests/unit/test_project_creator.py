from pathlib import Path

from src.services.project_manager.creator import ProjectCreator

creator = ProjectCreator()

project = creator.create(
    project_name="NovaTest",
    location=str(Path.home() / "Desktop"),
    language="Python",
    framework="Tkinter",
    use_git=True,
    create_venv=True
)

print("✅ Created:", project)