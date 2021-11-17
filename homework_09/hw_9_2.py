from typing import Tuple


def square(len_side: int) -> Tuple[int, int, float]:
    """
    Function square get side length and return tuple with:
        perimeter of a square;
        area of a square;
        diagonal length
    """

    return 4 * len_side, len_side ** 2, len_side * 2 ** 0.5
