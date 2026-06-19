from src.ui.themes.fonts import *
from src.ui.themes.spacing import *
from src.ui.themes.colors import *

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.master = master

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="🚀 NovaDesk",
            font=HEADING
        )

        title.pack(pady=(30, 25))

        buttons = [
            ("🏠 Dashboard", "dashboard"),
            ("📁 Projects", "projects"),
            ("📥 Downloads", "downloads"),
            ("🧹 Workspace", "workspace"),
            ("🤖 AI Tools", "ai"),
            ("⚙ Settings", "settings"),
            ("ℹ About", "about"),
        ]

        for text, page in buttons:
            ctk.CTkButton(
                self,
                text=text,
                width=180,
                height=40,
                command=lambda p=page: self.master.show_page(p)
            ).pack(pady=6)