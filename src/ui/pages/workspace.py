from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from src.services.workspace import (
    WorkspaceScanner,
    WorkspaceCleaner,
    WorkspaceAnalyzer,
)

from src.ui.themes.colors import TEXT_SECONDARY
from src.ui.themes.fonts import TITLE, BODY
from src.ui.themes.spacing import PAGE


class WorkspacePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.folder = Path.home()

        self.scanner = WorkspaceScanner()
        self.cleaner = WorkspaceCleaner()
        self.analyzer = WorkspaceAnalyzer()

        self.results_data = None

        # ==================================================
        # Title
        # ==================================================

        ctk.CTkLabel(
            self,
            text="🧹 Workspace Cleaner",
            font=TITLE
        ).pack(
            anchor="nw",
            padx=PAGE,
            pady=(30, 20)
        )

        # ==================================================
        # Main Content
        # ==================================================

        content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=PAGE
        )

        # ==================================================
        # Workspace Folder
        # ==================================================

        ctk.CTkLabel(
            content,
            text="Workspace Folder",
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
            str(self.folder)
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

        # ==================================================
        # Scan Options
        # ==================================================

        self.temp_files = ctk.CTkCheckBox(
            content,
            text="Temporary Files"
        )
        self.temp_files.select()
        self.temp_files.pack(anchor="w")

        self.empty_folders = ctk.CTkCheckBox(
            content,
            text="Empty Folders"
        )
        self.empty_folders.select()
        self.empty_folders.pack(anchor="w")

        self.large_files = ctk.CTkCheckBox(
            content,
            text="Large Files"
        )
        self.large_files.select()
        self.large_files.pack(anchor="w")

        self.duplicate_files = ctk.CTkCheckBox(
            content,
            text="Duplicate Files"
        )
        self.duplicate_files.select()
        self.duplicate_files.pack(
            anchor="w",
            pady=(0, 25)
        )

        # ==================================================
        # Buttons
        # ==================================================

        button_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        button_frame.pack(anchor="w")

        self.scan_button = ctk.CTkButton(
            button_frame,
            text="🔍 Scan Workspace",
            width=220,
            height=42,
            command=self.scan_workspace
        )

        self.scan_button.pack(
            side="left",
            padx=(0, 15)
        )

        self.clean_button = ctk.CTkButton(
            button_frame,
            text="🧹 Clean Workspace",
            width=220,
            height=42,
            command=self.clean_workspace
        )

        self.clean_button.pack(side="left")

        # ==================================================
        # Results
        # ==================================================

        ctk.CTkLabel(
            content,
            text="Results",
            font=BODY
        ).pack(
            anchor="w",
            pady=(30, 10)
        )

        self.results = ctk.CTkTextbox(
            content,
            width=800,
            height=240
        )

        self.results.pack(
            fill="both",
            expand=True
        )

        self.results.insert(
            "end",
            "────────────────────────────────────────────\n\n"
            "Ready to scan your workspace.\n\n"
            "Click 'Scan Workspace' to begin.\n\n"
            "────────────────────────────────────────────"
        )

        # ==================================================
        # Status
        # ==================================================

        self.status = ctk.CTkLabel(
            content,
            text="🟢 Ready",
            font=BODY,
            text_color=TEXT_SECONDARY
        )

        self.status.pack(
            anchor="w",
            pady=15
        )

    # ==================================================
    # Browse Folder
    # ==================================================

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.folder = Path(folder)

            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder)

    # ==================================================
    # Scan Workspace
    # ==================================================

    def scan_workspace(self):

        folder = Path(
            self.folder_entry.get()
        )

        if not folder.exists():

            self.status.configure(
                text="❌ Folder not found.",
                text_color="red"
            )

            return

        self.status.configure(
            text="🟡 Scanning...",
            text_color="orange"
        )

        self.update_idletasks()

        self.results_data = self.scanner.scan(folder)

        summary = self.analyzer.summarize(
            self.results_data
        )

        self.results.delete(
            "1.0",
            "end"
        )

        self.results.insert(
            "end",
            summary
        )

        self.status.configure(
            text="✅ Scan Complete",
            text_color="green"
        )

    # ==================================================
    # Clean Workspace
    # ==================================================

    def clean_workspace(self):

        if self.results_data is None:

            self.status.configure(
                text="⚠ Please scan first.",
                text_color="orange"
            )

            return

        self.status.configure(
            text="🧹 Cleaning...",
            text_color="orange"
        )

        self.update_idletasks()

        deleted = self.cleaner.clean(
            self.results_data
        )

        self.results.insert(
            "end",
            f"\n\n✔ Deleted {deleted} items."
        )

        self.status.configure(
            text="✅ Workspace Cleaned",
            text_color="green"
        )