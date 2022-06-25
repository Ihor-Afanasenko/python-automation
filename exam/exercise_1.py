"""
Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8,
9, 10, 11, 12, 13] and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this
point - we’ll get to it soon)
"""

# Base implementation

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def find_common_elements_between_lists(list_1: list[int], list_2: list[int]) -> list[int]:
    result = []
    for element_1 in list_1:
        for element_2 in list_2:
            if element_1 == element_2:
                result.append(element_1)
    return list(set(result))


# E.g.


print(find_common_elements_between_lists(a, b))

# Extras 1

import random


def get_random_min_element() -> int:
    return int(random.random() * 10)


def get_random_max_element() -> int:
    return int(random.random() * 1000)


def get_random_list_size(min_element: int, max_element: int) -> int:
    return random.randint(min_element, max_element)


def generate_random_list(min_element: int, max_element: int) -> list[int]:
    if min_element > max_element:
        min_element, max_element = max_element, min_element
    result_list = []
    for _ in range(get_random_list_size(min_element, max_element)):
        result_list.append(random.randint(min_element, max_element))
    return result_list


# E.g.
# Generate random lists

first_random_list = generate_random_list(get_random_min_element(), get_random_max_element())
second_random_list = generate_random_list(get_random_min_element(), get_random_max_element())

print(find_common_elements_between_lists(first_random_list, second_random_list))


# Extras 2


def find_common_elements_between_lists_in_line(list_1: list[int], list_2: list[int]):
    return list(set([element_1 for element_1 in list_1 for element_2 in list_2 if element_1 == element_2]))


# E.g.
first_random_list = generate_random_list(get_random_min_element(), get_random_max_element())
second_random_list = generate_random_list(get_random_min_element(), get_random_max_element())

print(find_common_elements_between_lists_in_line(first_random_list, second_random_list))
