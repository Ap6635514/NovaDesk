import customtkinter as ctk

from src.ui.components.sidebar import Sidebar
from src.ui.pages.dashboard import DashboardPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("NovaDesk")

        self.geometry("1400x800")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content = DashboardPage(self)
        self.content.grid(row=0, column=1, sticky="nsew")