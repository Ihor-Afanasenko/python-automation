from typing import Union


def name_function(function):
    """
    This decorator returns the function name.
    """

    def decorator(arg_1, arg_2):
        print(f'Name function: {function.__name__}')
        function(arg_1, arg_2)

    return decorator


@name_function
def add_function(x: Union[int, float], y: Union[int, float]):
    """
    This function returns the sum of two elements.
    """

    print(f'Result {x + y}')


@name_function
def multi_function(x: Union[int, float], y: Union[int, float]):
    """
    This function returns the multiplication of two elements.
    """

    print(f'Result {x * y}')
