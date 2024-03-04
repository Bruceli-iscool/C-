"""Abstract Syntax Tree for C-"""
class Program:
    def __init__(self, function_def):
        self.function_def = function_def

class Function:
    def __init__(self, name, action):
        self.name = name
        self.action = action

class Return:
    def _init_(self, expression):
        self.expression = expression

class Constant:
    pass