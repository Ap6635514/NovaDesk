from pathlib import Path

from src.services.project_manager.templates import (
    create_python_project
)

from src.services.project_manager.git_manager import (
    GitManager
)

from src.services.project_manager.venv import (
    VirtualEnvironment
)


class ProjectCreator:

    def __init__(self):

        self.git = GitManager()

        self.venv = VirtualEnvironment()

    def create(
        self,
        project_name,
        location,
        language,
        framework,
        use_git=True,
        create_venv=True
    ):

        project_path = Path(location) / project_name

        project_path.mkdir(
            parents=True,
            exist_ok=True
        )

        if language == "Python":

            create_python_project(
                project_path,
                framework
            )

        if use_git:

            self.git.initialize(project_path)

        if create_venv:

            self.venv.create(project_path)

        return project_path