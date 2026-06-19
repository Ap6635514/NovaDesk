from src.ui.themes.fonts import *
from src.ui.themes.spacing import *
from src.ui.themes.colors import *

import customtkinter as ctk
from datetime import datetime


class WelcomeHeader(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning ☀️"
        elif hour < 17:
            greeting = "Good Afternoon 🌤"
        else:
            greeting = "Good Evening 🌙"

        title = ctk.CTkLabel(
            self,
            text=greeting,
            font=TITLE
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Ready to explore the cosmos today? 🌌",
            font=BODY
        )
        subtitle.pack(anchor="w")