from pathlib import Path
import shutil


class DownloadOrganizer:

    def organize(self, scan_results):

        for category, files in scan_results.items():

            destination = Path.home() / "Downloads" / category

            destination.mkdir(exist_ok=True)

            for file in files:

                try:
                    shutil.move(str(file), destination / file.name)
                except Exception:
                    pass