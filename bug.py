def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of division by zero
    if b == 0:
        return a #Should raise an error if b is 0
    return a / b

result = function_with_uncommon_error(5,0)
print(result) # prints 5, not an error