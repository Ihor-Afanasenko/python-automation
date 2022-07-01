"""
Let’s say I give you a list saved in a variable a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
Python that takes this list and makes a new list that has only the even elements of this list in it.
"""


def find_even_number_in_list(input_list: [int]) -> list: return [element for element in input_list if not element & 1]


# E.g.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(find_even_number_in_list(a))


# Implementation using lambda function
def find_even_number_in_list_use_lambda(input_list: [int]) -> list:
    return list(filter(lambda x: (not x & 1), input_list))


# E.g.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(find_even_number_in_list_use_lambda(a))
