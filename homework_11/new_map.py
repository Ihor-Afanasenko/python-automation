from typing import Callable, Union, Tuple, List, Set


def new_map(function: Callable, iterable: Union[Tuple[int, float, str], List[int, float, str], Set[int, float, str]]) -> \
        List[int, float, str]:
    """
    Make a list that computes the function using arguments from
    each of the iterables. Stops when the shortest iterable is exhausted.
    """

    return [function(element) for element in iterable]
