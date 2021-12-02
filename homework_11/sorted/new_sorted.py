import sort_methods as methods
from typing import Union, Callable, List, Tuple, Set, Dict


def use_tim_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.tim_sort(sequence)


def use_bubble_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.bubble_sort(sequence)


def use_quick_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.quicksort(sequence)


def use_shell_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.shell_sort(sequence)


def use_heap_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.heap_sort(sequence)


def use_insertion_sort(sequence: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    return methods.insertion_sort(sequence)


def new_sorted(sequence: Union[Tuple[Union[int, float, str]], List[Union[int, float, str, Dict]],
                               Set[Union[int, float, str]]], method: Callable, reverse=False, key=None) -> \
                                Union[List, str]:
    """
    This function gets sequence as tuple or list or set and method sort (use_tim_sort, use_bubble_sort,
    use_quicksort) and returns sorted list or error message if sequence other types.
    Also, function sorted list of dictionaries if key =='list_dict_by_pair' by key and divide
    every dictionary if it has more than one pair. Attribute reverse with value True
    changing sorting to descending order.
    """

    if type(sequence) is list or type(sequence) is set or type(sequence) is tuple and not key:
        sequence = list(sequence)
        result = method(sequence)
        result = result[::-1] if reverse else result
    elif type(sequence) is list and key == 'list_dict_by_pair':
        general_dict = {}
        for element in sequence:
            general_dict.update(element)
        result_list = []
        for key in method(list(general_dict.keys())):
            new_dict = {}
            new_dict.update({key: general_dict[key]})
            result_list.append(new_dict)
        result = result_list
    else:
        result = f"Not known type {type(sequence)} or key: {key}"

    return result
