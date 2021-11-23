from random import randint


def quicksort(sequence: list) -> list:
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
    return quicksort(low) + same + quicksort(high)


def bubble_sort(sequence: list) -> list:
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


def insertion_sort(sequence: list, left: int, right: int) -> list:
    """
    This function implements insertion sort of the sequence.
    """

    for i in range(left + 1, right + 1):
        element = sequence[i]
        j = i - 1
        while element < sequence[j] and j >= left:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = element
    return sequence


def merge(sequence: list, l: int, m: int, r: int):
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


def tim_sort(sequence: list) -> list:
    """
    This function implements Timsort - a hybrid sort algorithm, its a standard sort algorithm in Python
    """

    n = len(sequence)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(sequence, start, end)

    size = minrun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(sequence, left, mid, right)

        size = 2 * size
    return sequence
