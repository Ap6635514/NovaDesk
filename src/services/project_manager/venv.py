import subprocess
import sys
from pathlib import Path


class VirtualEnvironment:

    def create(self, project_path: Path):

        try:

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "venv",
                    ".venv"
                ],
                cwd=project_path,
                check=True
            )

            return True

        except subprocess.CalledProcessError:

            return False