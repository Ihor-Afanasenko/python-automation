from hydroxide import Hydroxide
from hydrogen import Hydrogen


class Oxygen:
    def __init__(self) -> None:
        self.__atomic_weight = 16
        self.__valence = -2
        self.__atom_radius = 60

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            result += f'{key} => {value}\n'
        return result

    @property
    def atomic_weight(self):
        return self.__atomic_weight

    @property
    def valence(self):
        return self.__valence

    @atomic_weight.setter
    def atomic_weight(self, atomic_weight: int):
        self.__atomic_weight = atomic_weight

    @valence.setter
    def valence(self, valence: int):
        self.__valence = valence

    def __mul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        return self

    def __rmul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        return self

    def __add__(self, elements: Hydrogen) -> Hydroxide:
        return Hydroxide(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence)

    def __radd__(self, elements: Hydrogen) -> Hydroxide:
        return Hydroxide(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence)
