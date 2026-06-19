import customtkinter as ctk

from src.ui.themes.styles import BUTTON


class NovaButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            **BUTTON,
            **kwargs
        )