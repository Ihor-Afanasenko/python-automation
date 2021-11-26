def squared_even_numbers_2(number: int):
    """
    Function squares even numbers using a generator.
    Prints all calculated numbers. More locally than squared_even_numbers.
    """

    for item in (element ** 2 for element in range(number) if not element & 1):
        print(item)


squared_even_numbers_2(1000000000)
