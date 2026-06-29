"""
main.py

Entry point for Scientific Calculator Pro.
This file creates the application window and starts the UI.
"""

import customtkinter as ctk

from ui import CalculatorUI
from settings import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
    DEFAULT_THEME,
    COLOR_THEME
)


def configure_application():
    """
    Configure global CustomTkinter settings.
    """

    # Appearance: "Dark", "Light", or "System"
    ctk.set_appearance_mode(DEFAULT_THEME)

    # Theme: "blue", "green", "dark-blue"
    ctk.set_default_color_theme(COLOR_THEME)


def create_window():
    """
    Create and configure the main application window.
    """

    window = ctk.CTk()

    window.title(APP_NAME)

    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    window.minsize(
        MIN_WINDOW_WIDTH,
        MIN_WINDOW_HEIGHT
    )

    return window


def main():
    """
    Application entry point.
    """

    configure_application()

    window = create_window()

    CalculatorUI(window)

    window.mainloop()


if __name__ == "__main__":
    main()