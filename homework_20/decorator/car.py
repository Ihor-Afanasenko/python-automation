from modification import Modification


@Modification("Update brake system")
@Modification("Change wheel")
@Modification("Replacement pads")
@Modification("Install gas equipment")
class Car:
    """
    The class described a car with parameters:
    mark, model, manufacture year, power,
    last modification - relates to value Decorate (Modification),
    modifications - list all modifications in Decorates (Modification)
    """

    def __init__(self, mark: str, model: str, manufacture_year: int, power: int) -> None:
        self.__mark = mark
        self.__model = model
        self.__manufacture_year = manufacture_year
        self.__power = power
        self.__last_modification = self.last_modification if hasattr(Car, f'_{Car.__name__}__last_modification') else None
        self.__modifications = self.modifications if hasattr(Car, f'_{Car.__name__}__modifications') else None

    @property
    def last_modification(self) -> str:
        return self.__last_modification

    @property
    def modifications(self) -> list:
        return self.__modifications

    def __str__(self):
        result = ''

        for key, value in self.__dict__.items():
            key_without_class = str(key).split('__')[1]
            result += f'{key_without_class} => {value}\n'
        return result


if __name__ == '__main__':
    # E.g.
    car = Car('Mitsubishi', 'Outlander', 2010, 227)
    print(car)
    print(car.last_modification)
    print(car.modifications)
