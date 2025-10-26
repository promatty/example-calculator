from add import add

def multiply(a, b):
    result = 0
    is_negative = b < 0
    iterations = abs(b)
    
    for _ in range(iterations):
        result = add(result, a)
    
    return -result if is_negative else result

