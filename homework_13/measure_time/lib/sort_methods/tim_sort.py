from typing import List, Union

MINIMUM = 32


def find_minrun(n: int) -> int:
    """
    This function computes MINRUN value.
    """

    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort_for_tim_sort(sequence: List[Union[int, float, str]], left: int, right: int) -> List[
    Union[int, float, str]]:
    """
    This function implements insertion sort for tim sort of the sequence.
    """

    for i in range(left + 1, right + 1):
        element = sequence[i]
        j = i - 1
        while element < sequence[j] and j >= left:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = element
    return sequence


def merge(sequence: List[Union[int, float, str]], l: int, m: int, r: int):
    """
    This function implements merge parts of sequence.
    """

    sequence_length1 = m - l + 1
    sequence_length2 = r - m
    left = []
    right = []
    for i in range(0, sequence_length1):
        left.append(sequence[l + i])
    for i in range(0, sequence_length2):
        right.append(sequence[m + 1 + i])

    i = 0
    j = 0
    k = l

    while j < sequence_length2 and i < sequence_length1:
        if left[i] <= right[j]:
            sequence[k] = left[i]
            i += 1

        else:
            sequence[k] = right[j]
            j += 1

        k += 1

    while i < sequence_length1:
        sequence[k] = left[i]
        k += 1
        i += 1

    while j < sequence_length2:
        sequence[k] = right[j]
        k += 1
        j += 1


def tim_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements Timsort - a hybrid sort algorithm, its a standard sort algorithm in Python
    """

    n = len(sequence)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort_for_tim_sort(sequence, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(sequence, left, mid, right)

        size = 2 * size
    return sequence
