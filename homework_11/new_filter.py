from typing import Callable, Union, Tuple, List, Set


def new_filter(function: Callable,
               iterable: Union[List[int, float, str], Tuple[int, float, str], Set[int, float, str]]) -> List[
    int, float, str]:
    """
    Return a list yielding those items of iterable for which function(item)
    is true. If function is None, return empty list.
    """

    return [element for element in iterable if function(element)]
