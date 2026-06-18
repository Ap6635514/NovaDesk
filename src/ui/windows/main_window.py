import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NovaDesk")
        self.geometry("1200x700")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        label = ctk.CTkLabel(
            self,
            text="🚀 Welcome to NovaDesk",
            font=("Segoe UI", 28, "bold")
        )
        label.pack(expand=True)