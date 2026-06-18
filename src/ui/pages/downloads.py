import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

from src.services.downloads.scanner import DownloadScanner


class DownloadsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.scanner = DownloadScanner()

        self.folder = Path.home() / "Downloads"

        title = ctk.CTkLabel(
            self,
            text="📥 Downloads Organizer",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=(20, 10))

        self.path_label = ctk.CTkLabel(
            self,
            text=str(self.folder),
            font=("Segoe UI", 14)
        )
        self.path_label.pack()

        ctk.CTkButton(
            self,
            text="📂 Browse",
            command=self.select_folder
        ).pack(pady=10)

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
                self,
                text=f"{category}: 0",
                font=("Segoe UI", 18)
            )

            lbl.pack(anchor="w", padx=40)

            self.stats[category] = lbl

        ctk.CTkButton(
            self,
            text="🔍 Scan Folder",
            command=self.scan_folder
        ).pack(pady=20)

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.folder = Path(folder)
            self.path_label.configure(text=str(self.folder))

    def scan_folder(self):

        results = self.scanner.scan(self.folder)

        for category, files in results.items():
            self.stats[category].configure(
                text=f"{category}: {len(files)}"
            )