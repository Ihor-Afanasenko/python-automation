from typing import List


def add_list(input_list: List[int]) -> List[int]:
    """
    This function add list for exist list and raise error when the list has more than 10 elements.
    """

    start_list = [1, 2, 3, 4, 5]
    result = start_list + input_list
    if len(result) > 10:
        raise Exception(f"The finally list has more then 10 elements - {len(result)}")
    return result


# E.g.
print(add_list([2, 45, 3, 3, 6, 5]))
