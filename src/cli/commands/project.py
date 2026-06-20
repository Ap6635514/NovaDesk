from pathlib import Path

from src.services.project_manager.creator import ProjectCreator


def project():

    print("\n🌌 NovaDesk Project Creator\n")

    name = input("Project Name: ").strip()

    location = input(
        f"Location [{Path.cwd()}]: "
    ).strip()

    if not location:
        location = str(Path.cwd())

    print("\nLanguage")

    print("1. Python")

    language_choice = input("> ")

    language = "Python"

    print("\nFramework")

    print("1. None")
    print("2. Tkinter")
    print("3. Flask")
    print("4. FastAPI")

    framework_choice = input("> ")

    frameworks = {
        "1": "None",
        "2": "Tkinter",
        "3": "Flask",
        "4": "FastAPI"
    }

    framework = frameworks.get(
        framework_choice,
        "None"
    )

    use_git = input(
        "\nInitialize Git? (y/n): "
    ).lower() == "y"

    create_venv = input(
        "Create Virtual Environment? (y/n): "
    ).lower() == "y"

    creator = ProjectCreator()

    project_path = creator.create(
        project_name=name,
        location=location,
        language=language,
        framework=framework,
        use_git=use_git,
        create_venv=create_venv
    )

    print("\n✅ Project Created!")
    print(project_path)