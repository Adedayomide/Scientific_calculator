"""
settings.py

Application-wide configuration values.
Changing values here affects the entire application.
"""

# --------------------------------------------------
# Application Information
# --------------------------------------------------

APP_NAME = "Scientific Calculator Pro"

APP_VERSION = "1.0.0"

AUTHOR = "Your Name"


# --------------------------------------------------
# Window Configuration
# --------------------------------------------------

WINDOW_WIDTH = 500

WINDOW_HEIGHT = 850

MIN_WINDOW_WIDTH = 420

MIN_WINDOW_HEIGHT = 700


# --------------------------------------------------
# Appearance
# --------------------------------------------------

# Options:
# "System"
# "Dark"
# "Light"

DEFAULT_THEME = "Dark"

# Built-in CustomTkinter themes:
# "blue"
# "green"
# "dark-blue"

COLOR_THEME = "blue"


# --------------------------------------------------
# Calculator Defaults
# --------------------------------------------------

DEFAULT_ANGLE_MODE = "DEG"

DEFAULT_RESULT = "0"


# --------------------------------------------------
# History
# --------------------------------------------------

MAX_HISTORY_ITEMS = 100


# --------------------------------------------------
# Display
# --------------------------------------------------

MAX_DISPLAY_LENGTH = 32

DECIMAL_PRECISION = 12


# --------------------------------------------------
# Fonts
# --------------------------------------------------

FONT_FAMILY = "Segoe UI"

DISPLAY_FONT_SIZE = 34

EXPRESSION_FONT_SIZE = 18

BUTTON_FONT_SIZE = 18

STATUS_FONT_SIZE = 13


# --------------------------------------------------
# Padding

WINDOW_PADDING = 12

BUTTON_PADDING = 6

DISPLAY_PADDING = 15