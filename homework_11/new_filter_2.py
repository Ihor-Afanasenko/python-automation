from typing import Callable, Union


def new_filter_2(function: Callable, iterable: Union[tuple, list, set], argument: int) -> list:
    """
    Return a list those items of iterable for which function(item)
    is true.
    """

    if type(iterable) is set or type(iterable) is tuple:
        iterable = list(iterable)
    return function(iterable, argument)


def filter_more(iterable: list, argument: Union[int, float]) -> list:
    result = []
    for element in iterable:
        if element > argument:
            result.append(element)
    return result


def filter_less(iterable: list, argument: Union[int, float]) -> list:
    result = []
    for element in iterable:
        if element < argument:
            result.append(element)
    return result


def filter_equal(iterable: list, argument: Union[int, float, str]) -> list:
    result = []
    for element in iterable:
        if element == argument:
            result.append(element)
    return result


def filter_more_and_equal(iterable: list, argument: Union[int, float]) -> list:
    result = []
    for element in iterable:
        if element >= argument:
            result.append(element)
    return result


def filter_less_and_equal(iterable: Union[tuple, list, set], argument: Union[int, float]) -> list:
    result = []
    for element in iterable:
        if element <= argument:
            result.append(element)
    return result


def filter_not_equal(iterable: Union[tuple, list, set], argument: Union[int, float, str]) -> list:
    result = []
    for element in iterable:
        if element != argument:
            result.append(element)
    return result
