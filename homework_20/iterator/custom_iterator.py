from typing import Union, List, Tuple


class CustomIterator:
    """
    This class implement Custom Iteration with parameters sequence (list or tuple)
    start_index (int) and end_index (int) return iterator for subsequence relate to
    entered indexes
    """
    def __init__(self, sequence: Union[List, Tuple], start_index: int, end_index: int) -> None:
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_index = self.__start_index

    def __iter__(self):
        return self

    @property
    def next(self):
        return self.__next__()

    def __next__(self):
        if self.__current_index <= self.__end_index:
            element = self.__sequence[self.__current_index]
            self.__current_index += 1
            return element
        else:
            raise StopIteration
