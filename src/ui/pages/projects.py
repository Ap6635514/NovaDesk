from src.ui.themes.fonts import *
from src.ui.themes.spacing import *
from src.ui.themes.colors import *

import customtkinter as ctk

class ProjectsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="📁 Projects",
            font=("Segoe UI", 32, "bold")
        ).pack(padx=PAGE, pady=30, anchor="nw")