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
            font=("Segoe UI", 30, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Ready to explore the cosmos today? 🌌",
            font=("Segoe UI", 16)
        )
        subtitle.pack(anchor="w")