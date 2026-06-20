from pathlib import Path


class WorkspaceScanner:

    LARGE_FILE_SIZE = 100 * 1024 * 1024

    TEMP_EXTENSIONS = {
        ".tmp",
        ".temp",
        ".log",
        ".bak",
        ".old",
        ".cache"
    }

    IGNORE_DIRS = {
        ".git",
        ".venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode",
        "AppData",
        "$Recycle.Bin",
        "Windows",
        "Program Files",
        "Program Files (x86)"
    }

    def scan(self, folder: Path):

        results = {
            "files": 0,
            "folders": 0,
            "large_files": [],
            "temp_files": [],
            "empty_folders": [],
        }

        for path in folder.rglob("*"):

            try:

                # Skip ignored folders
                if any(part in self.IGNORE_DIRS for part in path.parts):
                    continue

                if path.is_dir():

                    results["folders"] += 1

                    try:
                        if not any(path.iterdir()):
                            results["empty_folders"].append(path)
                    except (PermissionError, OSError):
                        pass

                elif path.is_file():

                    results["files"] += 1

                    size = path.stat().st_size

                    if size >= self.LARGE_FILE_SIZE:
                        results["large_files"].append({
                            "path": path,
                            "size": size
                        })

                    if path.suffix.lower() in self.TEMP_EXTENSIONS:
                        results["temp_files"].append(path)

            except (PermissionError, OSError, FileNotFoundError):
                continue

        return results