from src.ui.themes.fonts import *
from src.ui.themes.spacing import *
from src.ui.themes.colors import *

import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path

from src.services.downloads.scanner import DownloadScanner
from src.services.downloads.organizer import DownloadOrganizer


class DownloadsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.scanner = DownloadScanner()
        self.organizer = DownloadOrganizer()

        self.folder = Path.home() / "Downloads"
        self.scan_results = {}

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="📥 Downloads Organizer",
            font=TITLE
        )
        title.pack(pady=(20, 10))

        # ==========================
        # Folder Path
        # ==========================

        self.path_label = ctk.CTkLabel(
            self,
            text=str(self.folder),
            font=BODY
        )
        self.path_label.pack(pady=(0, 15))

        # ==========================
        # Buttons
        # ==========================

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="📂 Browse Folder",
            width=180,
            command=self.select_folder
        ).grid(row=0, column=0, padx=8)

        ctk.CTkButton(
            button_frame,
            text="🔍 Scan Folder",
            width=180,
            command=self.scan_folder
        ).grid(row=0, column=1, padx=8)

        ctk.CTkButton(
            button_frame,
            text="📁 Organize Files",
            width=180,
            fg_color="#16a34a",
            hover_color="#15803d",
            command=self.organize_files
        ).grid(row=0, column=2, padx=8)

        # ==========================
        # Statistics Section
        # ==========================

        stats_frame = ctk.CTkFrame(self)
        stats_frame.pack(fill="x", padx=PAGE, pady=SECTION)

        heading = ctk.CTkLabel(
            stats_frame,
            text="📊 Scan Results",
            font=HEADING
        )
        heading.pack(anchor="w", padx=20, pady=(15, 10))

        self.stats = {}

        categories = [
            "Documents",
            "Images",
            "Videos",
            "Music",
            "Archives",
            "Programs",
            "Others"
        ]

        for category in categories:

            lbl = ctk.CTkLabel(
                stats_frame,
                text=f"{category}: 0",
                font=SUBTITLE
            )

            lbl.pack(anchor="w", padx=35, pady=2)

            self.stats[category] = lbl

        # ==========================
        # Status
        # ==========================

        self.status = ctk.CTkLabel(
            self,
            text="Ready",
            font=BODY
        )

        self.status.pack(pady=15)

    # ==================================

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.folder = Path(folder)
            self.path_label.configure(text=str(self.folder))

    # ==================================

    def scan_folder(self):

        self.status.configure(text="🔍 Scanning...")

        self.scan_results = self.scanner.scan(self.folder)

        for category, files in self.scan_results.items():
            self.stats[category].configure(
                text=f"{category}: {len(files)}"
            )

        self.status.configure(text="✅ Scan Complete")

    # ==================================

    def organize_files(self):

        if not self.scan_results:

            messagebox.showwarning(
                "Warning",
                "Please scan a folder first."
            )

            return

        self.organizer.organize(self.scan_results)

        self.status.configure(
            text="✅ Files Organized Successfully"
        )

        messagebox.showinfo(
            "Success",
            "Downloads organized successfully!"
        )