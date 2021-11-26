from typing import Callable, Union, Tuple, List, Set


def new_filter_2(function: Callable,
                 iterable: Union[
                     Tuple[Union[int, float, str]], List[Union[int, float, str]], Set[Union[int, float, str]]],
                 argument: Union[int, float]) -> \
        List[Union[int, float, str]]:
    """
    Return a list those items of iterable for which function(item)
    is true.
    """

    if type(iterable) is set or type(iterable) is tuple:
        iterable = list(iterable)
    return function(iterable, argument)


def filter_more(iterable: List[Union[int, float]], argument: Union[int, float]) -> List[Union[int, float]]:
    result = []
    for element in iterable:
        if element > argument:
            result.append(element)
    return result


def filter_less(iterable: List[Union[int, float]], argument: Union[int, float]) -> List[Union[int, float]]:
    result = []
    for element in iterable:
        if element < argument:
            result.append(element)
    return result


def filter_equal(iterable: List[Union[int, float, str]], argument: Union[int, float, str]) -> List[
    Union[int, float, str]]:
    result = []
    for element in iterable:
        if element == argument:
            result.append(element)
    return result


def filter_more_and_equal(iterable: List[Union[int, float]], argument: Union[int, float]) -> List[Union[int, float]]:
    result = []
    for element in iterable:
        if element >= argument:
            result.append(element)
    return result


def filter_less_and_equal(iterable: List[Union[int, float]], argument: Union[int, float]) -> List[Union[int, float]]:
    result = []
    for element in iterable:
        if element <= argument:
            result.append(element)
    return result


def filter_not_equal(iterable: List[Union[int, float, str]], argument: Union[int, float, str]) -> List[
    Union[int, float]]:
    result = []
    for element in iterable:
        if element != argument:
            result.append(element)
    return result
