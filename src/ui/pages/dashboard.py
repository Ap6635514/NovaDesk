import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 34, "bold")
        )
        title.pack(anchor="nw", padx=30, pady=(25, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Welcome back! Ready to get productive?",
            font=("Segoe UI", 16)
        )
        subtitle.pack(anchor="nw", padx=30)

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(fill="x", padx=30, pady=30)

        stats = [
            ("📁 Projects", "0"),
            ("📥 Downloads", "0"),
            ("🧹 Cleanups", "0"),
            ("🤖 AI Tasks", "0"),
        ]

        for text, value in stats:
            card = ctk.CTkFrame(cards, width=180, height=120)

            card.pack(side="left", padx=10)

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=text,
                font=("Segoe UI", 18, "bold")
            ).pack(pady=(18, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 36, "bold")
            ).pack()