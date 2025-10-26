from ui import get_input, show_result
from calculator import calculate

def main():
    op, a, b = get_input()
    result = calculate(op, a, b)
    show_result(result)

if __name__ == "__main__":
    main()

