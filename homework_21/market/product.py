from abc import ABC, abstractmethod
from constant_type import Color, Shape, BiologicalType, Growth


class Product(ABC):
    """
    This class describes abstract Product with abstract method calculate_food_energy
     that implemented in descendants classes
    """

    def __init__(self,
                 color: Color,
                 approximate_geometric_shape: Shape,
                 biological_type: BiologicalType,
                 growth: Growth
                 ) -> None:
        self.__color = color.name
        self.__approximate_geometric_shape = approximate_geometric_shape.name
        self.__biological_type = biological_type.name
        self.__growth = growth.name

    def __str__(self):
        result = ''

        for key, value in self.__dict__.items():
            result += f'{key} => {value}\n'
        return result

    @property
    def color(self) -> Color:
        return self.__color.name

    @property
    def approximate_geometric_shape(self) -> Shape:
        return self.__approximate_geometric_shape.name

    @property
    def biological_type(self) -> BiologicalType:
        return self.__biological_type.name

    @property
    def growth(self) -> Growth:
        return self.__growth.name

    @abstractmethod
    def calculate_food_energy(self, weight: int) -> int:
        ...

