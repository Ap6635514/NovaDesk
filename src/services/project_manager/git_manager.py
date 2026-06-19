import subprocess
from pathlib import Path


class GitManager:

    def initialize(self, project_path: Path):

        try:
            subprocess.run(
                ["git", "init"],
                cwd=project_path,
                check=True
            )

            return True

        except Exception:

            return False