from pathlib import Path
import shutil


class WorkspaceCleaner:

    def clean(self, results):

        deleted = 0

        for file in results["temp_files"]:

            try:
                file.unlink()
                deleted += 1
            except Exception:
                pass

        for folder in results["empty_folders"]:

            try:
                shutil.rmtree(folder)
                deleted += 1
            except Exception:
                pass

        return deleted