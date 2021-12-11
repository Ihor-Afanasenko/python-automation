from typing import List
from animal import Animal


class Cage:
    """
    Describe base cage with animals
    """

    def __init__(
            self,
            name: str,
            animals_list: List[Animal],
            volume: int
    ) -> None:
        self.__name = name
        self.__animals_list = animals_list
        self.__volume = volume

    @property
    def name(self) -> str:
        return self.__name

    @property
    def animal_list(self) -> List[Animal]:
        return self.__animals_list

    @property
    def volume(self) -> int:
        return self.__volume

    def check_cage_overload(self) -> str:
        number_result = self.__volume - sum([animal.need_cage_volume for animal in self.__animals_list])
        if number_result < 0:
            result = f"In cage {self.__name} not enough {abs(number_result)} volume"
        elif number_result > 0:
            result = f"Cage {self.__name} has free {number_result} volume"
        else:
            result = f"Cage {self.__name} doesn't overloaded"
        return result

    def calculate_year_cage_cost(self) -> int:
        return sum([animal.annual_expense for animal in self.__animals_list])

    def calculate_year_cage_hour_service(self) -> int:
        return sum([animal.calculate_service_for_year() for animal in self.__animals_list])
