"""
toolbar.py

Top toolbar for Scientific Calculator Pro.
"""

import customtkinter as ctk

from theme import Theme
from settings import (
    BUTTON_FONT_SIZE,
    FONT_FAMILY
)


class Toolbar(ctk.CTkFrame):

    def __init__(self, parent, command):

        super().__init__(
            parent,
            fg_color=Theme.TOOLBAR_BG,
            corner_radius=12
        )

        self.command = command

        self._create_widgets()

    def _create_widgets(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.history_button = self._create_button(
            "History",
            "history"
        )

        self.history_button.grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="ew"
        )

        self.theme_button = self._create_button(
            "Theme",
            "theme"
        )

        self.theme_button.grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="ew"
        )

        self.clear_history_button = self._create_button(
            "Clear History",
            "clear_history"
        )

        self.clear_history_button.grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="ew"
        )

    def _create_button(self, text, action):

        button = ctk.CTkButton(

            self,

            text=text,

            command=lambda: self.command(action),

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=BUTTON_FONT_SIZE

            ),

            height=42

        )

        Theme.style_function_button(button)

        return button