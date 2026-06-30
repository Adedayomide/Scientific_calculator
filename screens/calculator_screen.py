from kivy.uix.boxlayout import BoxLayout

from calculator import ScientificCalculator


class CalculatorScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.calculator = ScientificCalculator()

        self.expression = ""


    def button_pressed(self, value):

        self.expression += str(value)

        self.ids.expression.text = self.expression


    def calculate(self):

        result = self.calculator.evaluate(self.expression)

        self.ids.result.text = str(result)

        self.expression = str(result)

        self.ids.expression.text = self.expression


    def scientific(self, operation):

        self.expression += operation + "("

        self.ids.expression.text = self.expression


    def toggle_angle_mode(self):

        mode = self.calculator.toggle_angle_mode()

        self.ids.mode.text = mode


    def clear(self):

        self.expression = ""

        self.ids.expression.text = ""

        self.ids.result.text = "0"


    def backspace(self):

        self.expression = self.expression[:-1]

        self.ids.expression.text = self.expression