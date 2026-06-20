from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk
import os

from src.services.project_manager.creator import ProjectCreator
from src.services.settings import SettingsManager

from src.ui.themes.colors import TEXT_SECONDARY
from src.ui.themes.fonts import TITLE, BODY
from src.ui.themes.spacing import PAGE


class ProjectsPage(ctk.CTkFrame):

    def __init__(self, master, settings_manager=None):
        super().__init__(master)

        # ==================================
        # Settings
        # ==================================

        self.settings_manager = settings_manager or SettingsManager()
        self.settings = self.settings_manager.load()

        # ==================================
        # Default Project Folder
        # ==================================

        default_folder = self.settings.get("project_folder", "")

        if default_folder:
            self.folder = Path(default_folder)
        else:
            self.folder = Path.home() / "Projects"

        # ==========================
        # Title
        # ==========================

        ctk.CTkLabel(
            self,
            text="📁 Project Manager",
            font=TITLE
        ).pack(
            anchor="nw",
            padx=PAGE,
            pady=(30, 20)
        )

        # ==========================
        # Main Content
        # ==========================

        content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=PAGE
        )

        # ==========================
        # Project Name
        # ==========================

        ctk.CTkLabel(
            content,
            text="Project Name",
            font=BODY
        ).pack(anchor="w")

        self.name_entry = ctk.CTkEntry(
            content,
            width=450
        )

        self.name_entry.pack(
            anchor="w",
            pady=(5, 15)
        )

        # ==========================
        # Location
        # ==========================

        ctk.CTkLabel(
            content,
            text="Location",
            font=BODY
        ).pack(anchor="w")

        location_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        location_frame.pack(
            anchor="w",
            pady=(5, 15)
        )

        self.location_entry = ctk.CTkEntry(
            location_frame,
            width=340
        )

        self.location_entry.insert(
            0,
            str(self.folder)
        )

        self.location_entry.pack(
            side="left"
        )

        ctk.CTkButton(
            location_frame,
            text="📂 Browse",
            width=110,
            command=self.select_folder
        ).pack(
            side="left",
            padx=10
        )

        # ==========================
        # Framework
        # ==========================

        ctk.CTkLabel(
            content,
            text="Framework",
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
            width=260
        )

        self.framework.set(self.settings["framework"])

        self.framework.pack(
            anchor="w",
            pady=(5, 20)
        )

        # ==========================
        # Options
        # ==========================

        self.git_checkbox = ctk.CTkCheckBox(
            content,
            text="Initialize Git"
        )

        if self.settings["git"]:
            self.git_checkbox.select()

        self.git_checkbox.pack(anchor="w")

        self.venv_checkbox = ctk.CTkCheckBox(
            content,
            text="Create Virtual Environment"
        )

        if self.settings["venv"]:
           self.venv_checkbox.select()

        self.venv_checkbox.pack(
            anchor="w",
            pady=(5, 20)
        )

        # ==========================
        # Create Button
        # ==========================

        self.create_button = ctk.CTkButton(
            content,
            text="🚀 Create Project",
            width=220,
            height=42,
            command=self.create_project
        )

        self.create_button.pack(
            anchor="w",
            pady=(10, 20)
        )

        # ==========================
        # Status
        # ==========================

        self.status = ctk.CTkLabel(
            content,
            text="🟢 Ready",
            font=BODY,
            text_color=TEXT_SECONDARY
        )

        self.status.pack(anchor="w")

    # ==================================
    # Browse Folder
    # ==================================

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.folder = Path(folder)

            self.location_entry.delete(0, "end")
            self.location_entry.insert(0, folder)

    # ==================================
    # Create Project
    # ==================================

    def create_project(self):

        name = self.name_entry.get().strip()

        if not name:

            self.status.configure(
                text="❌ Please enter a project name.",
                text_color="red"
            )

            return

        creator = ProjectCreator()

        try:

            project = creator.create(
                project_name=name,
                location=self.location_entry.get(),
                language="Python",
                framework=self.framework.get(),
                use_git=bool(self.git_checkbox.get()),
                create_venv=bool(self.venv_checkbox.get())
            )

            self.status.configure(
                text=f"✅ Project '{project.name}' created successfully!",
                text_color="green"
            )

            try:
                os.startfile(project)
            except Exception:
                pass

        except Exception as e:

            self.status.configure(
                text=f"❌ {e}",
                text_color="red"
            )