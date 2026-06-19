import customtkinter as ctk

from src.ui.themes.styles import SUCCESS_BUTTON


class SuccessButton(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(
            master,
            **SUCCESS_BUTTON,
            **kwargs
        )