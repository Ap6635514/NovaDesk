import customtkinter as ctk

from src.ui.components.welcome_header import WelcomeHeader
from src.ui.components.search_bar import SearchBar
from src.ui.components.stat_card import StatCard
from src.ui.components.quick_action import QuickAction


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # ==========================
        # Top Bar
        # ==========================

        topbar = ctk.CTkFrame(self, fg_color="transparent")
        topbar.grid(row=0, column=0, columnspan=2,
                    sticky="ew", padx=30, pady=(25, 10))

        title = ctk.CTkLabel(
            topbar,
            text="🚀 NovaDesk",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(side="left")

        SearchBar(topbar).pack(side="right")

        # ==========================
        # Welcome Header
        # ==========================

        welcome = WelcomeHeader(self)
        welcome.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=30,
            pady=20
        )

        # ==========================
        # Statistics
        # ==========================

        stats = ctk.CTkFrame(self, fg_color="transparent")
        stats.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=30
        )

        stats.grid_columnconfigure((0, 1, 2, 3), weight=1)

        cards = [
            ("📁 Projects", "12"),
            ("📥 Downloads", "248"),
            ("💾 Storage", "72 GB"),
            ("📊 Activity", "15"),
        ]

        for i, (title, value) in enumerate(cards):

            card = StatCard(
                stats,
                title,
                value
            )

            card.grid(
                row=0,
                column=i,
                padx=10,
                pady=10,
                sticky="ew"
            )

        # ==========================
        # Quick Actions
        # ==========================

        action_frame = ctk.CTkFrame(self)

        action_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=30,
            pady=25
        )

        heading = ctk.CTkLabel(
            action_frame,
            text="⚡ Quick Actions",
            font=("Segoe UI", 20, "bold")
        )

        heading.pack(anchor="w", padx=20, pady=(15, 10))

        buttons = ctk.CTkFrame(
            action_frame,
            fg_color="transparent"
        )

        buttons.pack(fill="x", padx=20, pady=(0, 20))

        QuickAction(
            buttons,
            "➕ New Project"
        ).pack(side="left", padx=8)

        QuickAction(
            buttons,
            "📥 Downloads"
        ).pack(side="left", padx=8)

        QuickAction(
            buttons,
            "🧹 Workspace"
        ).pack(side="left", padx=8)

        QuickAction(
            buttons,
            "🤖 AI"
        ).pack(side="left", padx=8)