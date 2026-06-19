import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(self, master, title, value):
        super().__init__(
            master,
            width=180,
            height=120,
            corner_radius=15
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(18, 5))

        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 32, "bold")
        )

        self.value_label.pack()

    def update(self, value):
        self.value_label.configure(text=str(value))