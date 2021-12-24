class Hydrogen:
    def __init__(self) -> None:
        self.__atomic_weight = 1
        self.__valence = -1
        self.__chemical_symbol = 'H'
        self.__atom_radius = 53

    def __str__(self) -> str:
        result = ''

        for key, value in self.__dict__.items():
            result += f'{key} => {value}\n'
        return result

    @property
    def atomic_weight(self) -> int:
        return self.__atomic_weight

    @property
    def valence(self) -> int:
        return self.__valence

    @property
    def chemical_symbol(self) -> str:
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
