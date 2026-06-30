"""
history_panel.py

Displays calculator history.
"""

import customtkinter as ctk

from theme import Theme
from settings import FONT_FAMILY


class HistoryPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            fg_color=Theme.HISTORY_BG,

            corner_radius=16,

            border_width=1,

            border_color=Theme.DISPLAY_BORDER

        )

        self._create_widgets()

    def _create_widgets(self):

        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(

            self,

            text="Calculation History",

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=18,

                weight="bold"

            )

        )

        self.title_label.grid(

            row=0,

            column=0,

            padx=15,

            pady=(15, 10),

            sticky="w"

        )

        self.history_box = ctk.CTkTextbox(

            self,

            wrap="none",

            border_width=0

        )

        self.history_box.grid(

            row=1,

            column=0,

            padx=15,

            pady=(0, 15),

            sticky="nsew"

        )

        self.history_box.configure(

            state="disabled"

        )

    def set_history(self, entries):

        """
        Replace the displayed history.
        """

        self.history_box.configure(

            state="normal"

        )

        self.history_box.delete(

            "1.0",

            "end"

        )

        if not entries:

            self.history_box.insert(

                "end",

                "No calculations yet."

            )

        else:

            for item in entries:

                expression = item["expression"]

                result = item["result"]

                self.history_box.insert(

                    "end",

                    f"{expression} = {result}\n"

                )

        self.history_box.configure(

            state="disabled"

        )

    def clear(self):

        self.set_history([])