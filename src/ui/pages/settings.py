from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from src.services.settings import SettingsManager
from src.ui.themes.fonts import TITLE, BODY
from src.ui.themes.spacing import PAGE
from src.ui.themes.colors import TEXT_SECONDARY


class SettingsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.project_folder = Path.home() / "Projects"
        self.manager = SettingsManager()

        settings = self.manager.load()

        # =====================================
        # Title
        # =====================================

        ctk.CTkLabel(
            self,
            text="⚙️ Settings",
            font=TITLE
        ).pack(
            anchor="nw",
            padx=PAGE,
            pady=(30, 20)
        )

        content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=PAGE
        )

        # =====================================
        # Appearance
        # =====================================

        ctk.CTkLabel(
            content,
            text="Appearance",
            font=BODY
        ).pack(anchor="w")

        self.theme = ctk.CTkOptionMenu(
            content,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            width=220
        )

        self.theme.set(settings["theme"])

        self.theme.pack(
            anchor="w",
            pady=(5, 20)
        )

        # =====================================
        # Default Project Folder
        # =====================================

        ctk.CTkLabel(
            content,
            text="Default Project Folder",
            font=BODY
        ).pack(anchor="w")

        folder_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        folder_frame.pack(
            anchor="w",
            pady=(5, 20)
        )

        self.folder_entry = ctk.CTkEntry(
            folder_frame,
            width=420
        )

        self.folder_entry.insert(
            0,
            str(self.project_folder)
        )

        self.folder_entry.pack(side="left")

        ctk.CTkButton(
            folder_frame,
            text="📁 Browse",
            width=120,
            command=self.select_folder
        ).pack(
            side="left",
            padx=10
        )

        # =====================================
        # Default Framework
        # =====================================

        ctk.CTkLabel(
            content,
            text="Default Framework",
            font=BODY
        ).pack(anchor="w")

        self.framework = ctk.CTkOptionMenu(
            content,
            values=[
                "None",
                "Tkinter",
                "Flask",
                "FastAPI"
            ],
            width=220
        )

        self.framework.set("Tkinter")

        self.framework.pack(
            anchor="w",
            pady=(5, 20)
        )

        # =====================================
        # Options
        # =====================================

        self.git = ctk.CTkCheckBox(
            content,
            text="Initialize Git by default"
        )

        self.git.select()

        self.git.pack(anchor="w")

        self.venv = ctk.CTkCheckBox(
            content,
            text="Create Virtual Environment"
        )

        self.venv.select()

        self.venv.pack(
            anchor="w",
            pady=(5, 20)
        )

        # =====================================
        # Save Button
        # =====================================

        self.save_button = ctk.CTkButton(
            content,
            text="💾 Save Settings",
            width=220,
            height=42,
            command=self.save_settings
        )

        self.save_button.pack(
            anchor="w",
            pady=(10, 20)
        )

        # =====================================
        # Status
        # =====================================

        self.status = ctk.CTkLabel(
            content,
            text="🟢 Ready",
            font=BODY,
            text_color=TEXT_SECONDARY
        )

        self.status.pack(anchor="w")

    # =====================================

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.project_folder = Path(folder)

            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder)

    # =====================================

    def save_settings(self):

        # Backend will be connected next
        self.status.configure(
            text="✅ Settings Saved",
            text_color="green"
        )