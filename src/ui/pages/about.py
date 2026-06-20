import webbrowser
import customtkinter as ctk

from src.ui.themes.fonts import TITLE, BODY, SUBTITLE
from src.ui.themes.spacing import PAGE
from src.ui.themes.colors import TEXT_SECONDARY


class AboutPage(ctk.CTkFrame):

    VERSION = "1.0.0"

    def __init__(self, master):
        super().__init__(master)

        # =====================================
        # Title
        # =====================================

        ctk.CTkLabel(
            self,
            text="🌌 About NovaDesk",
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
        # Logo / Name
        # =====================================

        ctk.CTkLabel(
            content,
            text="NovaDesk",
            font=("Segoe UI", 36, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            content,
            text="Desktop Productivity Suite",
            font=SUBTITLE,
            text_color=TEXT_SECONDARY
        ).pack(anchor="w", pady=(0, 20))

        # =====================================
        # Information
        # =====================================

        info = f"""
Version: {self.VERSION}

Developer:
Abhishek Pandey

Built With:
• Python 3
• CustomTkinter

License:
MIT License

© 2026 Abhishek Pandey
"""

        ctk.CTkLabel(
            content,
            text=info,
            font=BODY,
            justify="left"
        ).pack(anchor="w")

        # =====================================
        # Buttons
        # =====================================

        button_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            pady=30
        )

        ctk.CTkButton(
            button_frame,
            text="🌐 GitHub",
            width=180,
            height=42,
            command=self.open_github
        ).pack(
            side="left",
            padx=(0, 15)
        )

        ctk.CTkButton(
            button_frame,
            text="📜 License",
            width=180,
            height=42,
            command=self.open_license
        ).pack(side="left")

        # =====================================
        # Footer
        # =====================================

        ctk.CTkLabel(
            content,
            text="Thank you for using NovaDesk ❤️",
            font=BODY,
            text_color=TEXT_SECONDARY
        ).pack(
            side="bottom",
            anchor="w",
            pady=20
        )

    # =====================================

    def open_github(self):
        webbrowser.open(
            "https://github.com/AP6635514/NovaDesk"
        )

    # =====================================

    def open_license(self):

        try:
            webbrowser.open("LICENSE")
        except Exception:
            pass