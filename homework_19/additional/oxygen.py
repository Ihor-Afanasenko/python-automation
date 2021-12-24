from hydroxide import Hydroxide
from hydrogen import Hydrogen


class Oxygen:
    def __init__(self) -> None:
        self.__atomic_weight = 16
        self.__valence = -2
        self.__chemical_symbol = 'O'
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

    @property
    def chemical_symbol(self):
        return self.__chemical_symbol

    @atomic_weight.setter
    def atomic_weight(self, atomic_weight: int):
        self.__atomic_weight = atomic_weight

    @valence.setter
    def valence(self, valence: int):
        self.__valence = valence

    @chemical_symbol.setter
    def chemical_symbol(self, chemical_symbol: int):
        self.__chemical_symbol = chemical_symbol

    def __mul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        self.chemical_symbol = self.__chemical_symbol + str(value)
        return self

    def __rmul__(self, value: int):
        self.atomic_weight = self.__atomic_weight * value
        self.valence = self.__valence * value
        self.chemical_symbol = self.__chemical_symbol + str(value)
        return self

    def __add__(self, elements: Hydrogen) -> Hydroxide:
        return Hydroxide(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence,
                         self.__chemical_symbol + elements.chemical_symbol)

    def __radd__(self, elements: Hydrogen) -> Hydroxide:
        return Hydroxide(self.__atomic_weight + elements.atomic_weight, self.__valence + elements.valence,
                         self.__chemical_symbol + elements.chemical_symbol)
