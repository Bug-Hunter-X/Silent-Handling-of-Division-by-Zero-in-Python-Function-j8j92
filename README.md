# Silent Handling of Division by Zero

This repository demonstrates an example of a Python function with an uncommon error: a division by zero that's silently handled instead of raising an exception. This can lead to unexpected and difficult-to-debug issues.

## Bug Description
The `function_with_uncommon_error` function is intended to handle the case of dividing by zero. However, the handling is incomplete and it only returns a if b is 0, but doesn't raise any error or warnings. This behavior can be problematic in applications where unexpected results can have serious consequences.

## Bug Solution
The solution provided in `bugSolution.py` addresses this issue by explicitly raising a `ZeroDivisionError` when `b` is zero. This ensures the code correctly handles exceptional cases. 