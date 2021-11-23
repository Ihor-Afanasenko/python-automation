from typing import Callable, Union


def new_map(function: Callable, iterable: Union[tuple, list, set]) -> list:
    """
    Make a list that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted.
    """

    return [function(element) for element in iterable]
