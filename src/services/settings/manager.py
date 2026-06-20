import json
from pathlib import Path


class SettingsManager:

    def __init__(self):

        self.config_dir = Path("config")
        self.config_dir.mkdir(exist_ok=True)

        self.settings_file = self.config_dir / "settings.json"

        if not self.settings_file.exists():

            self.save({
                "theme": "Dark",
                "project_folder": "",
                "framework": "Tkinter",
                "git": True,
                "venv": True
            })

    def load(self):

        with open(self.settings_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, settings):

        with open(self.settings_file, "w", encoding="utf-8") as file:
            json.dump(
                settings,
                file,
                indent=4
            )