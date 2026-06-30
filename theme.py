"""
theme.py

Centralized color definitions and styling helpers
for Scientific Calculator Pro.
"""

import customtkinter as ctk


class Theme:

    # Colors

    WINDOW_BG = "#1E1E1E"

    DISPLAY_BG = "#252526"

    DISPLAY_BORDER = "#3C3C3C"

    TEXT_PRIMARY = "#FFFFFF"

    TEXT_SECONDARY = "#BDBDBD"

    NUMBER_BUTTON = "#2D2D30"

    FUNCTION_BUTTON = "#3A3D41"

    OPERATOR_BUTTON = "#2563EB"

    EQUAL_BUTTON = "#16A34A"

    CLEAR_BUTTON = "#DC2626"

    HOVER_NUMBER = "#3A3A3A"

    HOVER_FUNCTION = "#505357"

    HOVER_OPERATOR = "#1D4ED8"

    HOVER_EQUAL = "#15803D"

    HOVER_CLEAR = "#B91C1C"

    TOOLBAR_BG = "#202124"

    STATUS_BG = "#202124"

    HISTORY_BG = "#202124"

    CORNER_RADIUS = 12

    BUTTON_HEIGHT = 58

    BUTTON_WIDTH = 70

    DISPLAY_HEIGHT = 110

    @staticmethod
    def style_number_button(button):

        button.configure(

            fg_color=Theme.NUMBER_BUTTON,

            hover_color=Theme.HOVER_NUMBER,

            text_color=Theme.TEXT_PRIMARY,

            corner_radius=Theme.CORNER_RADIUS

        )

    @staticmethod
    def style_function_button(button):

        button.configure(

            fg_color=Theme.FUNCTION_BUTTON,

            hover_color=Theme.HOVER_FUNCTION,

            text_color=Theme.TEXT_PRIMARY,

            corner_radius=Theme.CORNER_RADIUS

        )

    @staticmethod
    def style_operator_button(button):

        button.configure(

            fg_color=Theme.OPERATOR_BUTTON,

            hover_color=Theme.HOVER_OPERATOR,

            text_color="white",

            corner_radius=Theme.CORNER_RADIUS

        )

    @staticmethod
    def style_equal_button(button):

        button.configure(

            fg_color=Theme.EQUAL_BUTTON,

            hover_color=Theme.HOVER_EQUAL,

            text_color="white",

            corner_radius=Theme.CORNER_RADIUS

        )

    @staticmethod
    def style_clear_button(button):

        button.configure(

            fg_color=Theme.CLEAR_BUTTON,

            hover_color=Theme.HOVER_CLEAR,

            text_color="white",

            corner_radius=Theme.CORNER_RADIUS

        )

    @staticmethod
    def create_section(parent):

        return ctk.CTkFrame(

            parent,

            fg_color="transparent"

        )

    @staticmethod
    def create_card(parent):

        return ctk.CTkFrame(

            parent,

            fg_color=Theme.DISPLAY_BG,

            corner_radius=16,

            border_width=1,

            border_color=Theme.DISPLAY_BORDER

        )