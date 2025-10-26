def get_input():
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))
    return op, a, b

def show_result(result):
    print(f"Result: {result}")

def check_operation(op):
    valid_operations = ['+', '-', '*', '/']
    if op not in valid_operations:
        raise ValueError(f"Invalid operation. Choose from {valid_operations}.")
    return True