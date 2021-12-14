import time
from typing import List, Callable
from random import randint
from lib import bubble_sort
from lib import heap_sort
from lib import insertion_sort
from lib import quick_sort
from lib import shell_sort
from lib import tim_sort


def measure_time(function):
    """
    This decorator returns function execution time.
    """

    def decorator(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f'Execution time for function {function.__name__}: {time.time() - start_time} seconds')
        return result

    return decorator


@measure_time
def simple_function(number: int) -> List[int]:
    return [element ** 2 for element in range(number)]


# E.g.
simple_function(10000)

# Another example measure times sorting method
randint_list = [randint(0, 10000) for element in range(10000)]


@measure_time
def sorting_methods(sequence: List[int], function: Callable) -> List[int]:
    return function(sequence)


def use_bubble_sort(sequence: List[int]) -> List[int]:
    return bubble_sort(sequence)


def use_heap_sort(sequence: List[int]) -> List[int]:
    return heap_sort(sequence)


def use_insertion_sort(sequence: List[int]) -> List[int]:
    return insertion_sort(sequence)


def use_quick_sort(sequence: List[int]) -> List[int]:
    return quick_sort(sequence)


def use_shell_sort(sequence: List[int]) -> List[int]:
    return shell_sort(sequence)


def use_tim_sort(sequence: List[int]) -> List[int]:
    return tim_sort(sequence)


methods_list = [use_bubble_sort, use_heap_sort, use_insertion_sort, use_quick_sort, use_shell_sort, use_tim_sort]

for method in methods_list:
    print(f"\nMethod name: {method.__name__}")
    sorting_methods(randint_list, method)
    print('*'*100)
