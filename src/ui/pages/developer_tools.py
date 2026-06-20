import customtkinter as ctk
from tkinter import messagebox
from src.services.developer_tools import (
    PasswordGenerator,
    UUIDGenerator,
    JSONFormatter,
    Base64Tool,
    HashTool,
    TextTools,
)
from src.ui.themes.fonts import TITLE, BODY
from src.ui.themes.spacing import PAGE


class DeveloperToolsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.password_generator = PasswordGenerator()
        self.uuid_generator = UUIDGenerator()
        self.json_formatter = JSONFormatter()
        self.base64_tool = Base64Tool()
        self.hash_tool = HashTool()
        self.text_tools = TextTools()
        # =====================================
        # Title
        # =====================================

        ctk.CTkLabel(
            self,
            text="🛠 Developer Tools",
            font=TITLE
        ).pack(
            anchor="nw",
            padx=PAGE,
            pady=(30, 20)
        )

        # =====================================
        # Tab View
        # =====================================

        self.tabs = ctk.CTkTabview(self)

        self.tabs.pack(
            fill="both",
            expand=True,
            padx=PAGE,
            pady=(0, PAGE)
        )

        self.tabs.add("Password")
        self.tabs.add("UUID")
        self.tabs.add("JSON")
        self.tabs.add("Base64")
        self.tabs.add("Hash")
        self.tabs.add("Text")

        self.build_password_tab()
        self.build_uuid_tab()
        self.build_json_tab()
        self.build_base64_tab()
        self.build_hash_tab()
        self.build_text_tab()

    def build_password_tab(self):

        tab = self.tabs.tab("Password")
        ctk.CTkLabel(
            tab,
            text="🔑 Password Generator",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            tab,
            text="Length"
        ).pack(
            anchor="w",
            padx=20
        )

        self.password_length = ctk.CTkOptionMenu(
            tab,
            values=[
                "8",
                "12",
                "16",
                "24",
                "32"
            ],
            width=120
        )

        self.password_length.set("16")

        self.password_length.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        self.password_output = ctk.CTkEntry(
            tab,
            width=500
        )

        self.password_output.pack(
            anchor="w",
            padx=20
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="Generate",
            width=150,
            command=self.generate_password
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=150,
            command=self.copy_password
        ).pack(side="left")
        
    def build_uuid_tab(self):

        tab = self.tabs.tab("UUID")
        ctk.CTkLabel(
            tab,
            text="🆔 UUID Generator",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.uuid_output = ctk.CTkEntry(
            tab,
            width=600
        )

        self.uuid_output.pack(
            anchor="w",
            padx=20
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="Generate",
            width=150,
            command=self.generate_uuid
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=150,
            command=self.copy_uuid
        ).pack(side="left")

    def generate_password(self):
        password = self.password_generator.generate(
            length=int(self.password_length.get())
        )

        self.password_output.delete(0, "end")
        self.password_output.insert(0, password)

    def copy_password(self):
        password = self.password_output.get()

        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            self.update()

    def generate_uuid(self):
        uuid_value = self.uuid_generator.generate()

        self.uuid_output.delete(0, "end")
        self.uuid_output.insert(0, uuid_value)

    def copy_uuid(self):
        uuid_value = self.uuid_output.get()

        if uuid_value:
            self.clipboard_clear()
            self.clipboard_append(uuid_value)
            self.update()

    def build_json_tab(self):

        tab = self.tabs.tab("JSON")

        ctk.CTkLabel(
            tab,
            text="📄 JSON Formatter",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20,10)
        )

        self.json_text = ctk.CTkTextbox(
            tab,
            width=800,
            height=250
        )

        self.json_text.pack(
            padx=20,
            fill="both",
            expand=True
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="Pretty",
            width=120,
            command=self.pretty_json
        ).pack(
            side="left",
            padx=(0,10)
        )

        ctk.CTkButton(
            button_frame,
            text="Minify",
            width=120,
            command=self.minify_json
        ).pack(
            side="left",
            padx=(0,10)
        )

        ctk.CTkButton(
            button_frame,
            text="Validate",
            width=120,
            command=self.validate_json
        ).pack(
            side="left",
            padx=(0,10)
        )

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=120,
            command=self.copy_json
        ).pack(side="left")

    def build_base64_tab(self):

        tab = self.tabs.tab("Base64")

        ctk.CTkLabel(
            tab,
            text="🔤 Base64 Encoder / Decoder",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.base64_text = ctk.CTkTextbox(
            tab,
            width=800,
            height=250
        )

        self.base64_text.pack(
            padx=20,
            fill="both",
            expand=True
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="Encode",
            width=120,
            command=self.encode_base64
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Decode",
            width=120,
            command=self.decode_base64
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=120,
            command=self.copy_base64
        ).pack(side="left")

    def build_hash_tab(self):

        tab = self.tabs.tab("Hash")

        ctk.CTkLabel(
            tab,
            text="🔐 Hash Generator",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.hash_text = ctk.CTkTextbox(
            tab,
            width=800,
            height=250
        )

        self.hash_text.pack(
            padx=20,
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            tab,
            text="Algorithm"
        ).pack(
            anchor="w",
            padx=20
        )

        self.hash_algorithm = ctk.CTkOptionMenu(
            tab,
            values=[
                "MD5",
                "SHA1",
                "SHA256",
                "SHA512"
            ],
            width=120
        )

        self.hash_algorithm.set("SHA256")

        self.hash_algorithm.pack(
            anchor="w",
            padx=20,
            pady=(5, 20)
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="Generate",
            width=120,
            command=self.generate_hash
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=120,
            command=self.copy_hash
        ).pack(side="left")

    def build_text_tab(self):

        tab = self.tabs.tab("Text")

        ctk.CTkLabel(
            tab,
            text="🔤 Text Utilities",
            font=BODY
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.text_text = ctk.CTkTextbox(
            tab,
            width=800,
            height=250
        )

        self.text_text.pack(
            padx=20,
            fill="both",
            expand=True
        )

        button_frame = ctk.CTkFrame(
            tab,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        ctk.CTkButton(
            button_frame,
            text="UPPER",
            width=120,
            command=self.upper_text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="lower",
            width=120,
            command=self.lower_text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Title",
            width=120,
            command=self.title_text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="snake_case",
            width=120,
            command=self.snake_text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="camelCase",
            width=120,
            command=self.camel_text
        ).pack(
            side="left",
            padx=(0, 10)
        )

        ctk.CTkButton(
            button_frame,
            text="Copy",
            width=120,
            command=self.copy_text
        ).pack(side="left")

    def pretty_json(self):
        try:
            text = self.json_text.get("1.0", "end")
            result = self.json_formatter.pretty(text)
            self.json_text.delete("1.0", "end")
            self.json_text.insert("1.0", result)
        except Exception as e:
            self.json_text.delete("1.0", "end")
            self.json_text.insert("1.0", str(e))

    def minify_json(self):
        try:
            text = self.json_text.get("1.0", "end")
            result = self.json_formatter.minify(text)
            self.json_text.delete("1.0", "end")
            self.json_text.insert("1.0", result)
        except Exception as e:
            self.json_text.delete("1.0", "end")
            self.json_text.insert("1.0", str(e))

    def validate_json(self):
        text = self.json_text.get("1.0", "end")
        valid, message = self.json_formatter.validate(text)
        messagebox.showinfo("Validation", message)

    def copy_json(self):
        text = self.json_text.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

    def encode_base64(self):
        try:
            text = self.base64_text.get("1.0", "end").strip()
            result = self.base64_tool.encode(text)
            self.base64_text.delete("1.0", "end")
            self.base64_text.insert("1.0", result)
        except Exception as e:
            self.base64_text.delete("1.0", "end")
            self.base64_text.insert("1.0", str(e))

    def decode_base64(self):
        try:
            text = self.base64_text.get("1.0", "end").strip()
            result = self.base64_tool.decode(text)
            self.base64_text.delete("1.0", "end")
            self.base64_text.insert("1.0", result)
        except Exception as e:
            self.base64_text.delete("1.0", "end")
            self.base64_text.insert("1.0", str(e))

    def copy_base64(self):
        text = self.base64_text.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

    def generate_hash(self):
        try:
            text = self.hash_text.get("1.0", "end").strip()
            algorithm = self.hash_algorithm.get()
            result = self.hash_tool.generate(text, algorithm)
            self.hash_text.delete("1.0", "end")
            self.hash_text.insert("1.0", result)
        except Exception as e:
            self.hash_text.delete("1.0", "end")
            self.hash_text.insert("1.0", str(e))

    def copy_hash(self):
        text = self.hash_text.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()

    def upper_text(self):
        text = self.text_text.get("1.0", "end").strip()
        result = self.text_tools.upper(text)
        self.text_text.delete("1.0", "end")
        self.text_text.insert("1.0", result)

    def lower_text(self):
        text = self.text_text.get("1.0", "end").strip()
        result = self.text_tools.lower(text)
        self.text_text.delete("1.0", "end")
        self.text_text.insert("1.0", result)

    def title_text(self):
        text = self.text_text.get("1.0", "end").strip()
        result = self.text_tools.title(text)
        self.text_text.delete("1.0", "end")
        self.text_text.insert("1.0", result)

    def snake_text(self):
        text = self.text_text.get("1.0", "end").strip()
        result = self.text_tools.snake(text)
        self.text_text.delete("1.0", "end")
        self.text_text.insert("1.0", result)

    def camel_text(self):
        text = self.text_text.get("1.0", "end").strip()
        result = self.text_tools.camel(text)
        self.text_text.delete("1.0", "end")
        self.text_text.insert("1.0", result)

    def copy_text(self):
        text = self.text_text.get("1.0", "end")
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update()
        