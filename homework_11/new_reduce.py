from typing import Callable, Union


def new_reduce(function: Callable, sequence: Union[list, tuple]) -> Union[int, float, str, None]:
    """
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    If sequence is empty return None.
    """

    if not len(sequence):
        return None
    result = sequence[0]
    for element in range(1, len(sequence)):
        result = function(result, sequence[element])
    return result

