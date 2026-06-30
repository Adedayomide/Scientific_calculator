"""
ui.py

Main user interface controller for
Scientific Calculator Pro.
"""

import customtkinter as ctk

from calculator import ScientificCalculator
from history import HistoryManager
from memory import MemoryManager

from utils import (
    normalize_expression,
    format_result,
    is_number,
    backspace,
    clamp_display
)

from widgets import (
    Display,
    Keypad,
    Toolbar,
    HistoryPanel,
    StatusBar
)


class CalculatorUI:

    def __init__(self, root):

        self.root = root

        self.calculator = ScientificCalculator()

        self.history = HistoryManager()

        self.memory = MemoryManager()

        self.expression = ""

        self.history_visible = False

        self._configure_window()

        self._create_layout()

        self._bind_keyboard()

        self.display.set_angle_mode(
            self.calculator.angle_mode
        )

        self.statusbar.reset()

    def _configure_window(self):

        self.root.grid_rowconfigure(
            1,
            weight=1
        )

        self.root.grid_columnconfigure(
            0,
            weight=1
        )

    def _create_layout(self):

        self.toolbar = Toolbar(
            self.root,
            self._toolbar_action
        )  

        self.toolbar.grid(
            row=0,
            column=0,
            padx=12,
            pady=(12, 6),
            sticky="ew"
        )

        self.content = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        self.content.grid(
            row=1,
            column=0,
            padx=12,
            pady=6,
            sticky="nsew"
        )

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        self.content.grid_columnconfigure(
            0,
            weight=1
        )

        self.content.grid_rowconfigure(
            0,
            weight=0
        )

        self.content.grid_rowconfigure(
            1,
            weight=1
        )


        self.display = Display(
            self.content
        )

        self.display.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0,10)
        )


        self.keypad = Keypad(
            self.content,
            self._button_pressed
        )

        self.keypad.grid(
            row=1,
            column=0,
            sticky="nsew"
        )


        self.history_panel = HistoryPanel(
            self.content
        )


        self.statusbar = StatusBar(
            self.root
        )

        self.statusbar.grid(
            row=2,
            column=0,
            padx=12,
            pady=(6,12),
            sticky="ew"
        )

    def _bind_keyboard(self):

        self.root.bind(

            "<Key>",

            self._key_pressed

        )

        self.root.bind(

            "<Return>",

            lambda event:
            self.calculate()

        )

        self.root.bind(

            "<KP_Enter>",

            lambda event:
            self.calculate()

        )

        self.root.bind(

            "<BackSpace>",

            lambda event:
            self.delete_last()

        )

        self.root.bind(

            "<Escape>",

            lambda event:
            self.clear()
        )

    def _key_pressed(self, event):

        key = event.char

        allowed = (

            "0123456789"

            "+"

            "-"

            "*"

            "/"

            "%"

            "("

            ")"

            "."

        )

        if key in allowed:

            self.append(key)
    
    def append(self, text):

        self.expression += str(text)

        self.display.set_expression(

            clamp_display(

                self.expression

            )

        )

    def clear(self):

        self.expression = ""

        self.display.clear()

        self.statusbar.reset()

    def delete_last(self):

        self.expression = backspace(

            self.expression

        )

        self.display.set_expression(

            self.expression

        )

    def _toolbar_action(

        self,

        action

    ):

        if action == "history":

            self.toggle_history()

        elif action == "theme":

            self.statusbar.set_status(

                "Theme switching will be added."

            )

        elif action == "clear_history":

            self.history.clear()

            self.history_panel.clear()

            self.statusbar.set_status(

                "History Cleared"

            )


    def toggle_history(self):

        if self.history_visible:

            self.history_panel.grid_remove()

            self.history_visible = False

        else:

            self.history_panel.grid(

                row=0,

                column=1,

                rowspan=2,

                padx=(12, 0),

                sticky="ns"

            )

            self.history_panel.set_history(

                self.history.get_all()

            )

            self.history_visible = True

    def _button_pressed(self, button):

        if button.isdigit():

            self.append(button)

            return

        if button == ".":

            self._append_decimal()

            return

        if button in ["+", "-", "×", "÷", "%"]:

            self._append_operator(button)

            return

        if button in ["(", ")"]:

            self.append(button)

            return

        actions = {

            "=": self.calculate,

            "C": self.clear,

            "⌫": self.delete_last,

            "DEG": self.toggle_angle_mode,

            "π": self.insert_pi,

            "e": self.insert_e,

            "±": self.change_sign,

            "sin": lambda: self.apply_function("sin"),

            "cos": lambda: self.apply_function("cos"),

            "tan": lambda: self.apply_function("tan"),

            "log": lambda: self.apply_function("log"),

            "ln": lambda: self.apply_function("ln"),

            "√": lambda: self.apply_function("square_root"),

            "x²": self.square,

            "x³": self.cube,

            "xʸ": self.power,

            "1/x": self.reciprocal,

            "!": self.factorial,

            "MC": self.memory_clear,

            "MR": self.memory_recall,

            "MS": self.memory_store,

            "M+": self.memory_add,

            "M-": self.memory_subtract

        }

        action = actions.get(button)

        if action:

            action()

    def _append_operator(self, operator_symbol):

        if not self.expression:

            return

        operators = ["+", "-", "×", "÷", "%"]

        if self.expression[-1] in operators:

            self.expression = self.expression[:-1]

        self.append(operator_symbol)


    def _append_decimal(self):

        if not self.expression:

            self.append("0.")

            return

        last_number = ""

        for character in reversed(self.expression):

            if character in "+-×÷%()":

                break

            last_number = character + last_number

        if "." not in last_number:

            self.append(".")

    def insert_pi(self):

        self.append("π")


    def insert_e(self):

        self.append("e")

    def toggle_angle_mode(self):

        mode = self.calculator.toggle_angle_mode()

        self.display.set_angle_mode(mode)

        self.statusbar.set_status(

            f"Angle Mode: {mode}"

        )

    def change_sign(self):

        if not self.expression:

            return

        try:

            value = float(

                normalize_expression(

                    self.expression

                )

            )

            value *= -1

            self.expression = format_result(value)

            self.display.set_expression(

                self.expression

            )

        except ValueError:

            self.statusbar.set_status(

                "Cannot change sign."

            )

    def apply_function(self, function_name):

        if not self.expression:

            return

        try:

            value = float(

                normalize_expression(

                    self.expression

                )

            )

            function = getattr(

                self.calculator,

                function_name

            )

            result = function(value)

            result = format_result(result)

            self.display.set_result(result)

            self.expression = str(result)

            self.display.set_expression(

                f"{function_name}({value})"

            )

        except Exception:

            self.display.set_result("Error")

            self.statusbar.set_status(

                "Invalid operation."

            )

    def square(self):

        self._apply_single_value(

            self.calculator.square

        )


    def cube(self):

        self._apply_single_value(

            self.calculator.cube

        )


    def reciprocal(self):

        self._apply_single_value(

            self.calculator.reciprocal

        )


    def factorial(self):

        self._apply_single_value(

            self.calculator.factorial

        )


    def _apply_single_value(self, operation):

        if not self.expression:

            return

        try:

            value = float(

                normalize_expression(

                    self.expression

                )

            )

            result = operation(value)

            result = format_result(result)

            self.expression = result

            self.display.set_expression(result)

            self.display.set_result(result)

        except Exception:

            self.display.set_result("Error")

            self.statusbar.set_status(

                "Calculation error."
            )

    def power(self):

        self.append("^")

    def memory_store(self):

        result = self.display.get_result()

        if is_number(result):

            self.memory.store(result)

            self.statusbar.set_status(

                "Memory Stored"

            )


    def memory_recall(self):

        self.append(

            self.memory.get_display_value()

        )

        self.statusbar.set_status(

            "Memory Recalled"

        )


    def memory_clear(self):

        self.memory.clear()

        self.statusbar.set_status(

            "Memory Cleared"

        )


    def memory_add(self):

        result = self.display.get_result()

        if is_number(result):

            self.memory.add(result)

            self.statusbar.set_status(

                "Added to Memory"

            )


    def memory_subtract(self):

        result = self.display.get_result()

        if is_number(result):

            self.memory.subtract(result)

            self.statusbar.set_status(

                "Subtracted from Memory"

            )

    def calculate(self):

        if not self.expression:
            return

        try:

            expression = normalize_expression(
                self.expression
            )

            result = self.calculator.evaluate(
                expression
            )

            result = format_result(result)

            self.display.set_result(result)

            self.history.add(
                self.expression,
                result
            )

            if self.history_visible:

                self.history_panel.set_history(
                    self.history.get_all()
                )

            self.statusbar.set_status(
                "Calculation Complete"
            )

            self.expression = str(result)

            self.display.set_expression(
                self.expression
            )

        except Exception:

            self.display.set_result("Error")

            self.statusbar.set_status(
                "Calculation Error"
            )


    def refresh_history(self):

        if self.history_visible:

            self.history_panel.set_history(
                self.history.get_all()
            )


    def show_history(self):

        self.history_visible = True

        self.history_panel.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=(12, 0),
            sticky="ns"
        )

        self.refresh_history()


    def hide_history(self):

        self.history_visible = False

        self.history_panel.grid_remove()


    # def toggle_history(self):

    #     if self.history_visible:

    #         self.hide_history()

    #     else:

    #         self.show_history()


    def reset(self):

        self.clear()

        self.history.clear()

        self.memory.clear()

        self.history_panel.clear()

        self.display.set_angle_mode(
            self.calculator.angle_mode
        )

        self.statusbar.set_status(
            "Calculator Reset"
        )


    def get_expression(self):

        return self.expression


    def set_expression(self, expression):

        self.expression = str(expression)

        self.display.set_expression(
            self.expression
        )


    def get_result(self):

        return self.display.get_result()


    def set_result(self, value):

        self.display.set_result(
            format_result(value)
        )


    def update_display(self):

        self.display.set_expression(
            self.expression
        )


    def quit(self):

        self.root.destroy()
    

