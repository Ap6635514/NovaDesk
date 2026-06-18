import customtkinter as ctk

class AboutPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="ℹ️ About NovaDesk",
            font=("Segoe UI", 32, "bold")
        ).pack(padx=30, pady=30, anchor="nw")