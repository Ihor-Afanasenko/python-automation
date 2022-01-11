from custom_iterator import CustomIterator

if __name__ == '__main__':
    # E.g.
    iterator = CustomIterator((2, 4, 2, 5, 6, 5, 445), 4, 6)

    for element in iterator:
        print(element)
