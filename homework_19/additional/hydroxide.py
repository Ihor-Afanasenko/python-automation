class Hydroxide:
    def __init__(self, atomic_weight: int, valence: int, chemical_symbol: str) -> None:
        self.__atomic_weight = atomic_weight
        self.__valence = valence
        self.__chemical_symbol = chemical_symbol

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
