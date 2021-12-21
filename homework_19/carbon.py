from methane import Methane
from hydrogen import Hydrogen


class Carbon:
    def __init__(self, valence) -> None:
        self.__atomic_weight = 12
        self.__valence = valence
        self.__atom_radius = 70

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

    def __add__(self, elements: Hydrogen) -> Methane:
        return Methane(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence)

    def __radd__(self, elements: Hydrogen) -> Methane:
        return Methane(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence)

    def __mul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        return self

    def __rmul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        return self
