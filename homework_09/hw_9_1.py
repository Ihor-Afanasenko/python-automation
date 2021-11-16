def arithmetic(first_number: float, second_number: float, operation: str) -> float:
    """
    Function arithmetic gets two number and operation ('+', '-', '*', '/')
    return result operation with two number or
    if operation not correct message 'Not known operation: {operation}'
    """
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number
    else:
        result = f"Not known operation: {operation}"
    return result
