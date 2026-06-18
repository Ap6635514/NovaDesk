from pathlib import Path
from .file_types import FILE_TYPES


class DownloadScanner:

    def scan(self, folder):

        folder = Path(folder)

        print(f"📂 Scanning folder: {folder}")

        if not folder.exists():
            raise FileNotFoundError(f"Folder not found: {folder}")

        results = {}

        for category in FILE_TYPES:
            results[category] = []

        results["Others"] = []

        for file in folder.iterdir():

            print("Found:", file.name)

            if not file.is_file():
                continue

            extension = file.suffix.lower()

            found = False

            for category, extensions in FILE_TYPES.items():

                if extension in extensions:
                    print(f"   → {category}")
                    results[category].append(file)
                    found = True
                    break

            if not found:
                print("   → Others")
                results["Others"].append(file)

        return results