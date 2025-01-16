def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of division by zero
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

result = function_with_uncommon_error(5,0)
print(result) # Raises ZeroDivisionError