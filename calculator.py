"""
calculator.py

Scientific calculator engine.
Contains all mathematical operations.
"""

import ast
import math
import operator

from settings import DEFAULT_ANGLE_MODE


class ScientificCalculator:

    def __init__(self):

        self.angle_mode = DEFAULT_ANGLE_MODE

        self.operators = {

            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.USub: operator.neg

        }

    def set_angle_mode(self, mode):

        if mode in ("DEG", "RAD"):
            self.angle_mode = mode

    def toggle_angle_mode(self):

        if self.angle_mode == "DEG":
            self.angle_mode = "RAD"
        else:
            self.angle_mode = "DEG"

        return self.angle_mode

    def evaluate(self, expression):

        allowed = {

            "__builtins__": {},

            "sin": self.sin,
            "cos": self.cos,
            "tan": self.tan,

            "asin": self.asin,
            "acos": self.acos,
            "atan": self.atan,

            "sqrt": self.square_root,

            "log": self.log,

            "ln": self.ln,

            "abs": self.absolute,

            "factorial": self.factorial,

            "floor": self.floor,

            "ceil": self.ceil,

            "exp": self.exponential,

            "pow": self.power,

            "pi": self.pi,

            "e": self.e

        }

        try:

            return eval(expression, allowed)

        except Exception:

            return "Error"

    def _evaluate(self, node):

        if isinstance(node, ast.Constant):

            return node.value

        if isinstance(node, ast.Num):

            return node.n

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)

            right = self._evaluate(node.right)

            operation = self.operators[type(node.op)]

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):

            operand = self._evaluate(node.operand)

            operation = self.operators[type(node.op)]

            return operation(operand)

        raise ValueError("Unsupported Expression")

    def _angle(self, value):

        if self.angle_mode == "DEG":
            return math.radians(value)

        return value

    def sin(self, value):

        return math.sin(self._angle(value))

    def cos(self, value):

        return math.cos(self._angle(value))

    def tan(self, value):

        return math.tan(self._angle(value))

    def asin(self, value):

        result = math.asin(value)

        if self.angle_mode == "DEG":
            return math.degrees(result)

        return result

    def acos(self, value):

        result = math.acos(value)

        if self.angle_mode == "DEG":
            return math.degrees(result)

        return result

    def atan(self, value):

        result = math.atan(value)

        if self.angle_mode == "DEG":
            return math.degrees(result)

        return result

    def log(self, value):

        return math.log10(value)

    def ln(self, value):

        return math.log(value)

    def square(self, value):

        return value ** 2

    def cube(self, value):

        return value ** 3

    def power(self, base, exponent):

        return base ** exponent

    def square_root(self, value):

        return math.sqrt(value)

    def reciprocal(self, value):

        return 1 / value

    def factorial(self, value):

        return math.factorial(int(value))

    def absolute(self, value):

        return abs(value)

    def percentage(self, value):

        return value / 100

    def exponential(self, value):

        return math.exp(value)

    def floor(self, value):

        return math.floor(value)

    def ceil(self, value):

        return math.ceil(value)

    @property
    def pi(self):

        return math.pi

    @property
    def e(self):

        return math.e