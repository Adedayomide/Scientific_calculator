"""
statusbar.py

Status bar widget for Scientific Calculator Pro.
"""

import customtkinter as ctk

from theme import Theme
from settings import (
    FONT_FAMILY,
    STATUS_FONT_SIZE
)


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(

            parent,

            fg_color=Theme.STATUS_BG,

            corner_radius=10

        )

        self.status_text = ctk.StringVar(
            value="Ready"
        )

        self._create_widgets()

    def _create_widgets(self):

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.label = ctk.CTkLabel(

            self,

            textvariable=self.status_text,

            anchor="w",

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=STATUS_FONT_SIZE

            ),

            text_color=Theme.TEXT_SECONDARY

        )

        self.label.grid(

            row=0,

            column=0,

            padx=12,

            pady=8,

            sticky="ew"

        )

    def set_status(self, message):

        """
        Update the displayed status.
        """

        self.status_text.set(str(message))

    def get_status(self):

        """
        Return the current status.
        """

        return self.status_text.get()

    def reset(self):

        """
        Restore the default status.
        """

        self.status_text.set("Ready")