from pathlib import Path

from src.services.downloads.scanner import DownloadScanner

folder = Path.home() / "Downloads"

print("Scanning:", folder)
print("Exists:", folder.exists())

scanner = DownloadScanner()

results = scanner.scan(folder)

for category, files in results.items():
    print(f"{category}: {len(files)}")