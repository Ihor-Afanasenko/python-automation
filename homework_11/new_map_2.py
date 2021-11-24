from typing import Callable, Union


def new_map_2(function: Callable, iterable: Union[tuple, list, set], argument: Union[None, int, float, str]) -> list:
    """
    Make a list that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted.
    """

    if type(iterable) is set or type(iterable) is tuple:
        iterable = list(iterable)
    return function(iterable, argument)


def multiple_element(iterable: list, argument: Union[None, int, float, str]) -> list:
    result = []
    for element in iterable:
        result.append(element * argument)
    return result


def division_element(iterable: list, argument: Union[None, int, float]) -> list:
    result = []
    for element in iterable:
        result.append(element / argument)
    return result


def exponention_element(iterable: list, argument: Union[None, int, float]) -> list:
    result = []
    for element in iterable:
        result.append(pow(element, argument))
    return result
