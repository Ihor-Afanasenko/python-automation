import sort_methods as methods
from typing import Union, Callable


def use_tim_sort(sequence: list) -> list:
    return methods.tim_sort(sequence)


def use_bubble_sort(sequence: list) -> list:
    return methods.bubble_sort(sequence)


def use_quicksort(sequence: list) -> list:
    return methods.quicksort(sequence)


def new_sorted(sequence: Union[tuple, list, set], method: Callable, key=None) -> Union[list, str]:
    """
    This function gets sequence as tuple or list or set and method sort (use_tim_sort, use_bubble_sort,
    use_quicksort) and returns sorted list or error message if sequence other types.
    Also, function sorted list of dictionaries if key =='list_dict_by_pair' by key and divide
    every dictionary if it has more than one pair.
    """

    if type(sequence) is set or type(sequence) is tuple and not key:
        sequence = list(sequence)
        result = method(sequence)
    elif type(sequence) is list and key == 'list_dict_by_pair':
        general_dict = {}
        for el_dict in sequence:
            general_dict.update(el_dict)
        result_list = []
        for key in method(list(general_dict.keys())):
            new_dict = {}
            new_dict.update({key: general_dict[key]})
            result_list.append(new_dict)
        result = result_list
    else:
        result = f"Not known type {type(sequence)} or key: {key}"

    return result

