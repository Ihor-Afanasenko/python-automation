from homework_21.market.product import Product
from constant_type import Color, Shape, BiologicalType, Growth


class Apple(Product):
    """
    This class extends Product class and describe Apple
    """

    def __init__(self,
                 color: Color,
                 approximate_geometric_shape: Shape,
                 biological_type: BiologicalType,
                 growth: Growth
                 ) -> None:
        super().__init__(color, approximate_geometric_shape, biological_type, growth)

    def calculate_food_energy(self, weight: int) -> str:
        """
        Method gets weight in 1/100g and returns food energy 100g product in kcal
        """

        return f'{52*weight} kcal in {weight*100}g products'
