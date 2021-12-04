from typing import List, Union


def heapify(sequence: List[Union[int, float, str]], n: int, i: int) -> List[Union[int, float, str]]:
    """
    This function find subtree rooted with node i which is an index in sequence. n is size of heap.
    """

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and sequence[largest] < sequence[l]:
        largest = l
    if r < n and sequence[largest] < sequence[r]:
        largest = r
    if largest != i:
        sequence[i], sequence[largest] = sequence[largest], sequence[i]
        heapify(sequence, n, largest)
    return sequence


def heap_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """
    This function implements heap sort of the sequence.
    """

    n = len(sequence)

    for i in range(n // 2 - 1, -1, -1):
        heapify(sequence, n, i)

    for i in range(n - 1, 0, -1):
        sequence[i], sequence[0] = sequence[0], sequence[i]
        heapify(sequence, i, 0)
    return sequence
