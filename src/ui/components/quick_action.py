import customtkinter as ctk


class QuickAction(ctk.CTkButton):
    def __init__(self, master, text, command=None):
        super().__init__(
            master,
            text=text,
            command=command,
            width=170,
            height=45,
            corner_radius=12
        )