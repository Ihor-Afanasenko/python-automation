from typing import Union


def arithmetic(first_number: float, second_number: float, operation: str) -> Union[float, str]:
    """
    Function arithmetic gets two number and operation ('+', '-', '*', '/')
    return result operation with two number or
    if operation not correct message 'Not known operation: {operation}'
    """
    
    match operation:
        case '+':
            result = first_number + second_number
        case '-':
            result = first_number - second_number
        case '*':
            result = first_number * second_number
        case '/':
            result = first_number / second_number
        case _:
            result = f"Not known operation: {operation}"

    return result
