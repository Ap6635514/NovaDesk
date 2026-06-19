import customtkinter as ctk


class SearchBar(ctk.CTkEntry):
    def __init__(self, master):
        super().__init__(
            master,
            width=250,
            height=40,
            placeholder_text="🔍 Search..."
        )