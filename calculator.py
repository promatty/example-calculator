from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def calculate(op, a, b):
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    return operations[op](a, b)

