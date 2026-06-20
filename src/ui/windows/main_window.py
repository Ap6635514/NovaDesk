import customtkinter as ctk

from src.ui.components.sidebar import Sidebar

from src.ui.pages.dashboard import DashboardPage
from src.ui.pages.projects import ProjectsPage
from src.ui.pages.downloads import DownloadsPage
from src.ui.pages.workspace import WorkspacePage
from src.ui.pages.developer_tools import DeveloperToolsPage
from src.ui.pages.settings import SettingsPage
from src.ui.pages.about import AboutPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("NovaDesk")
        self.geometry("1400x800")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {
            "dashboard": DashboardPage(self.container),
            "projects": ProjectsPage(self.container),
            "downloads": DownloadsPage(self.container),
            "workspace": WorkspacePage(self.container),
            "developer_tools": DeveloperToolsPage(self.container),
            "settings": SettingsPage(self.container),
            "about": AboutPage(self.container),
        }

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("dashboard")

    def show_page(self, page_name):
        self.pages[page_name].tkraise()