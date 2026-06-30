"""
keypad.py

Calculator keypad widget.
"""

import customtkinter as ctk

from theme import Theme
from settings import (
    BUTTON_FONT_SIZE,
    FONT_FAMILY
)


class Keypad(ctk.CTkFrame):

    def __init__(self, parent, command):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.command = command

        self.layout = [

            ["MC", "MR", "MS", "M+", "M-"],

            ["DEG", "(", ")", "⌫", "C"],

            ["sin", "cos", "tan", "√", "%"],

            ["log", "ln", "π", "e", "!"],

            ["x²", "x³", "xʸ", "1/x", "±"],

            ["7", "8", "9", "÷", ""],

            ["4", "5", "6", "×", ""],

            ["1", "2", "3", "-", ""],

            ["0", ".", "=", "+", ""]

        ]

        self._create_grid()

    def _create_grid(self):

        rows = len(self.layout)
        columns = len(self.layout[0])

        self.configure(
            height=650
        )

        self.grid_propagate(False)

        for row in range(rows):
            self.grid_rowconfigure(
                row,
                weight=1,
                minsize=60
            )

        for column in range(columns):
            self.grid_columnconfigure(
            column,
            weight=1,
            minsize=70
        )

        for row_index, row in enumerate(self.layout):

            for column_index, text in enumerate(row):

                if text == "":

                    spacer = ctk.CTkFrame(
                        self,
                        fg_color="transparent"
                    )

                    spacer.grid(
                        row=row_index,
                        column=column_index,
                        padx=4,
                        pady=4,
                        sticky="nsew"
                    )

                    continue

                button = ctk.CTkButton(

                    self,

                    text=text,

                    command=lambda value=text:
                    self.command(value),

                    height=Theme.BUTTON_HEIGHT,

                    width=Theme.BUTTON_WIDTH,

                    font=ctk.CTkFont(

                        family=FONT_FAMILY,

                        size=BUTTON_FONT_SIZE,

                        weight="bold"

                    )

                )

                self._style_button(
                    button,
                    text
                )

                button.grid(

                    row=row_index,

                    column=column_index,

                    padx=4,

                    pady=4,

                    sticky="nsew"

                )

    def _style_button(self, button, text):

        numbers = {

            "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", "."
        }

        operators = {

            "+", "-", "×", "÷", "="
        }

        functions = {

            "sin",
            "cos",
            "tan",
            "log",
            "ln",
            "√",
            "π",
            "e",
            "!",
            "%",
            "x²",
            "x³",
            "xʸ",
            "1/x",
            "±",
            "(",
            ")",
            "DEG"
        }

        memory = {

            "MC",
            "MR",
            "MS",
            "M+",
            "M-"
        }

        if text == "=":

            Theme.style_equal_button(button)

        elif text == "C":

            Theme.style_clear_button(button)

        elif text in operators:

            Theme.style_operator_button(button)

        elif text in functions:

            Theme.style_function_button(button)

        elif text in memory:

            Theme.style_function_button(button)

        elif text == "⌫":

            Theme.style_function_button(button)

        elif text in numbers:

            Theme.style_number_button(button)

        else:

            Theme.style_number_button(button)