from typing import Callable, Union


def new_reduce_2(function: Callable, sequence: Union[list, tuple, set]) -> Union[int, float, str, None]:
    """
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    If sequence is empty return None.
    """

    if type(sequence) is set or type(sequence) is tuple:
        sequence = list(sequence)
    if not len(sequence):
        return None
    return function(sequence)


def add_two_elements(x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
    return x + y


def add_two(sequence: list) -> Union[int, float, str]:
    result = sequence[0]
    for element in range(1, len(sequence)):
        result = add_two_elements(result, sequence[element])
    return result


def multi_two(sequence: list) -> Union[int, float]:
    result = 1
    for element in sequence:
        result *= element
    return result
