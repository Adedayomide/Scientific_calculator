"""
display.py

Display widget for Scientific Calculator Pro.
"""

import customtkinter as ctk

from theme import Theme
from settings import (
    DISPLAY_FONT_SIZE,
    EXPRESSION_FONT_SIZE,
    FONT_FAMILY,
    DEFAULT_RESULT,
    DEFAULT_ANGLE_MODE
)


class Display(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=Theme.DISPLAY_BG,
            corner_radius=16,
            border_width=1,
            border_color=Theme.DISPLAY_BORDER
        )

        self.angle_mode = ctk.StringVar(
            value=DEFAULT_ANGLE_MODE
        )

        self.expression_var = ctk.StringVar(
            value=""
        )

        self.result_var = ctk.StringVar(
            value=DEFAULT_RESULT
        )

        self._create_widgets()

    def _create_widgets(self):

        self.grid_columnconfigure(0, weight=1)

        self.angle_label = ctk.CTkLabel(

            self,

            textvariable=self.angle_mode,

            anchor="e",

            text_color=Theme.TEXT_SECONDARY,

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=14,

                weight="bold"

            )

        )

        self.angle_label.grid(

            row=0,

            column=0,

            sticky="ew",

            padx=20,

            pady=(12, 0)

        )

        self.expression_label = ctk.CTkLabel(

            self,

            textvariable=self.expression_var,

            anchor="e",

            justify="right",

            text_color=Theme.TEXT_SECONDARY,

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=EXPRESSION_FONT_SIZE

            )

        )

        self.expression_label.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=20,

            pady=(5, 5)

        )

        self.result_label = ctk.CTkLabel(

            self,

            textvariable=self.result_var,

            anchor="e",

            justify="right",

            text_color=Theme.TEXT_PRIMARY,

            font=ctk.CTkFont(

                family=FONT_FAMILY,

                size=DISPLAY_FONT_SIZE,

                weight="bold"

            )

        )

        self.result_label.grid(

            row=2,

            column=0,

            sticky="ew",

            padx=20,

            pady=(0, 18)

        )

    def set_angle_mode(self, mode):

        self.angle_mode.set(mode)

    def get_angle_mode(self):

        return self.angle_mode.get()

    def set_expression(self, expression):

        self.expression_var.set(str(expression))

    def get_expression(self):

        return self.expression_var.get()

    def append(self, text):

        current = self.expression_var.get()

        self.expression_var.set(
            current + str(text)
        )

    def backspace(self):

        current = self.expression_var.get()

        if current:

            self.expression_var.set(
                current[:-1]
            )

    def clear_expression(self):

        self.expression_var.set("")

    def set_result(self, result):

        self.result_var.set(str(result))

    def get_result(self):

        return self.result_var.get()

    def clear_result(self):

        self.result_var.set(DEFAULT_RESULT)

    def clear(self):

        self.clear_expression()

        self.clear_result()