from typing import Callable, Union, Tuple, List, Set


def new_filter(function: Callable,
               iterable: Union[
                   List[Union[int, float, str]], Tuple[Union[int, float, str]], Set[Union[int, float, str]]]) -> List[
    Union[int, float, str]]:
    """
    Return a list yielding those items of iterable for which function(item)
    is true. If function is None, return empty list.
    """

    return [element for element in iterable if function(element)]
