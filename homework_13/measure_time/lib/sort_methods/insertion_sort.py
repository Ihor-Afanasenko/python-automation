from typing import List, Union


def insertion_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements insertion sort of the sequence.
    """

    for i in range(1, len(sequence)):
        j = i - 1
        next_element = sequence[i]
        while (sequence[j] > next_element) and (j >= 0):
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = next_element
    return sequence
