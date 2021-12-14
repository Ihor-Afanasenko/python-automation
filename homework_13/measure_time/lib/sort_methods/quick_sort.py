from random import randint
from typing import List, Union


def quick_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements Quicksort list and return sorted list.
    """

    if len(sequence) < 2:
        return sequence

    low, same, high = [], [], []

    pivot = sequence[randint(0, len(sequence) - 1)]

    for item in sequence:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)
