from typing import List, Union


def shell_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements shell sort of the sequence.
    """

    gap = len(sequence) // 2
    while gap > 0:
        for i in range(gap, len(sequence)):
            temp = sequence[i]
            j = i
            while j >= gap and sequence[j - gap] > temp:
                sequence[j] = sequence[j - gap]
                j -= gap
            sequence[j] = temp
        gap = gap // 2
    return sequence
