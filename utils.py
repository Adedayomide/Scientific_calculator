"""
utils.py

Utility functions used throughout
Scientific Calculator Pro.
"""

from settings import (
    DECIMAL_PRECISION,
    MAX_DISPLAY_LENGTH
)


def normalize_expression(expression):

    replacements = {

        "×": "*",

        "÷": "/",

        "−": "-",

        "^": "**",

        "√": "sqrt",

        "π": "pi"

    }

    for old, new in replacements.items():

        expression = expression.replace(old, new)

    return expression


def format_result(value):
    """
    Format a result for display.
    """

    if isinstance(value, str):

        return value

    if isinstance(value, int):

        return str(value)

    if isinstance(value, float):

        value = round(value, DECIMAL_PRECISION)

        if value.is_integer():

            return str(int(value))

        return str(value)

    return str(value)


def is_number(value):
    """
    Check if a value can be converted to float.
    """

    try:

        float(value)

        return True

    except ValueError:

        return False


def clamp_display(text):
    """
    Prevent text from overflowing
    the calculator display.
    """

    text = str(text)

    if len(text) <= MAX_DISPLAY_LENGTH:

        return text

    return text[:MAX_DISPLAY_LENGTH - 3] + "..."


def safe_float(value):
    """
    Convert a value to float.
    Returns None if conversion fails.
    """

    try:

        return float(value)

    except ValueError:

        return None


def clean_expression(expression):
    """
    Remove unnecessary spaces.
    """

    return expression.strip()


def append_text(current, value):
    """
    Append text to an expression.
    """

    return f"{current}{value}"


def backspace(expression):
    """
    Remove the last character.
    """

    if not expression:

        return ""

    return expression[:-1]