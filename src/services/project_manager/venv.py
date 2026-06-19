import subprocess
from pathlib import Path


class VirtualEnvironment:

    def create(self, project_path: Path):

        try:

            subprocess.run(
                ["python", "-m", "venv", ".venv"],
                cwd=project_path,
                check=True
            )

            return True

        except Exception:

            return False