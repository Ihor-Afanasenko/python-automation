from typing import List, Union


def bubble_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements Bubble sort list and return sorted list.
    """

    n = len(sequence)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                already_sorted = False
        if already_sorted:
            break
    return sequence
