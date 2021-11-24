def squared_even_numbers(length: int):
    """
    Function squares even numbers using a generator.
    Prints all calculated numbers.
    """

    def inner_generator(times: int):
        counter = 0

        while counter < times:
            if not counter & 1:
                yield counter ** 2
            counter += 1

    for counter in inner_generator(length):
        print(counter)


squared_even_numbers(1000000000)
