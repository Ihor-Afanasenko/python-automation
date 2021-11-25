from typing import Callable, Union, Tuple, List, Set


def new_map_2(function: Callable, iterable: Union[Tuple[int, float, str], List[int, float, str], Set[int, float, str]],
              argument: Union[int, float, str]) -> List[int, float, str]:
    """
    Make a list that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted.
    """

    if type(iterable) is set or type(iterable) is tuple:
        iterable = list(iterable)
    return function(iterable, argument)


def multiple_element(iterable: List[int, float, str], argument: Union[int, float, str]) -> List[int, float, str]:
    result = []
    for element in iterable:
        result.append(element * argument)
    return result


def division_element(iterable: List[int, float], argument: Union[int, float]) -> List[float]:
    result = []
    for element in iterable:
        result.append(element / argument)
    return result


def exponential_element(iterable: List[int, float], argument: Union[int, float]) -> List[int, float, str]:
    result = []
    for element in iterable:
        result.append(pow(element, argument))
    return result
