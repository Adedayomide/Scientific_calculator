from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from screens.calculator_screen import CalculatorScreen


class ScientificCalculatorApp(App):

    def build(self):

        Window.clearcolor = (0.12, 0.12, 0.12, 1)

        Builder.load_file("kv/calculator.kv")

        return CalculatorScreen()


if __name__ == "__main__":
    ScientificCalculatorApp().run()