import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.grid_rowconfigure(8, weight=1)

        title = ctk.CTkLabel(
            self,
            text="🚀 NovaDesk",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=(30, 25))

        buttons = [
            "🏠 Dashboard",
            "📁 Projects",
            "📥 Downloads",
            "🧹 Workspace",
            "🤖 AI Tools",
            "⚙ Settings",
            "ℹ About"
        ]

        for name in buttons:
            btn = ctk.CTkButton(
                self,
                text=name,
                width=180,
                height=40,
                corner_radius=10
            )
            btn.pack(pady=6)