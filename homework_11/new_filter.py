from typing import Callable, Union


def new_filter(function: Callable, iterable: Union[tuple, list, set]) -> list:
    """
    Return a list yielding those items of iterable for which function(item)
    is true. If function is None, return empty list.
    """

    return [element for element in iterable if function(element)]
