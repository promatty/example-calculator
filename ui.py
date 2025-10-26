def get_input():
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))
    return op, a, b

def show_result(result):
    print(f"Result: {result}")

