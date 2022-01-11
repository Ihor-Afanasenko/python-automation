from homework_21.market.product import Product
from homework_21.market.apple import Apple
from homework_21.market.banana import Banana
from homework_21.market.celery import Celery
from homework_21.market.strawberry import Strawberry
from constant_type import Color, Shape, BiologicalType, Growth


class Market:
    """
    Describes class with method to search Product depend on input parameters
    """

    def search_product(self) -> Product:
        """
        Factory method gets product parameters and returns Product depend on parameters
        """

        product_color = input('Enter product color in eating phase (green, red, yellow, white, pink): ')
        product_shape = input('Enter approximate geometric shape (sphere, cylinder, cone): ')
        product_biological_type = input('Input biological type (berry, herbaceous plant, fruit): ')
        if product_biological_type == 'herbaceous plant':
            product_biological_type = '_'.join(product_biological_type.split(' '))
        product_growth = input('Input where product growth (tree, shrub, herb): ')
        check_data = [product_color, product_shape, product_biological_type, product_growth]
        self.check_input_data(check_data)

        if self.is_apple_parameters(product_color, product_shape, product_biological_type, product_growth):
            return Apple(self.identify_color(product_color), Shape.SPHERE, BiologicalType.FRUIT, Growth.TREE)
        elif self.is_celery_parameters(product_color, product_shape, product_biological_type, product_growth):
            return Celery(self.identify_color(product_color), Shape.SPHERE, BiologicalType.HERBACEOUS_PLANT, Growth.HERB)
        elif self.is_banana_parameters(product_color, product_shape, product_biological_type, product_growth):
            return Banana(self.identify_color(product_color), Shape.CYLINDER, BiologicalType.BERRY, Growth.TREE)
        elif self.is_strawberry_parameters(product_color, product_shape, product_biological_type, product_growth):
            return Strawberry(self.identify_color(product_color), Shape.CONE, BiologicalType.BERRY, Growth.HERB)
        else:
            raise Exception('Can not find this product')

    def identify_color(self, product_color) -> Color:
        """
        Converts input product color to enum Color
        """
        
        if product_color.upper() == Color.YELLOW.name:
            return Color.YELLOW
        elif product_color.upper() == Color.RED.name:
            return Color.RED
        elif product_color.upper() == Color.GREEN.name:
            return Color.GREEN
        elif product_color.upper() == Color.WHITE.name:
            return Color.WHITE
        elif product_color.upper() == Color.PINK.name:
            return Color.PINK
        else:
            raise Exception('This color has not identified yet')

    def is_apple_parameters(self, product_color, product_shape, product_biological_type, product_growth) -> bool:
        """
        Method checks the entered parameters for compliance with the product Apple
        """

        return product_shape.upper() == Shape.SPHERE.name \
                and product_biological_type.upper() == BiologicalType.FRUIT.name \
                and product_growth.upper() == Growth.TREE.name \
                or product_color.upper() == Color.GREEN.name \
                or product_color.upper() == Color.YELLOW.name \
                or product_color.upper() == Color.RED.name

    def is_celery_parameters(self, product_color, product_shape, product_biological_type, product_growth) -> bool:
        """
        Method checks the entered parameters for compliance with the product Celery
        """

        return product_shape.upper() == Shape.SPHERE.name \
                and product_biological_type.upper() == BiologicalType.HERBACEOUS_PLANT.name \
                and product_growth.upper() == Growth.HERB.name \
                or product_color.upper() == Color.GREEN.name \
                or product_color.upper() == Color.WHITE.name

    def is_banana_parameters(self, product_color, product_shape, product_biological_type, product_growth) -> bool:
        """
        Method checks the entered parameters for compliance with the product Banana
        """

        return product_shape.upper() == Shape.CYLINDER.name \
                and product_biological_type.upper() == BiologicalType.BERRY.name \
                and product_growth.upper() == Growth.TREE.name \
                or product_color.upper() == Color.YELLOW.name \
                or product_color.upper() == Color.PINK.name

    def is_strawberry_parameters(self, product_color, product_shape, product_biological_type, product_growth) -> bool:
        """
        Method checks the entered parameters for compliance with the product Strawberry
        """

        return product_color.upper() == Color.RED.name \
                and product_shape.upper() == Shape.CONE.name \
                and product_biological_type.upper() == BiologicalType.BERRY.name \
                and product_growth.upper() == Growth.HERB.name

    def check_input_data(self, input_data: list[str]) -> None:
        """
        This method check user input data, if this data out of range raises exception
        """

        check_elements = 'green red yellow white pink sphere cylinder cone berry herbaceous_plant fruit tree shrub herb'
        for item in input_data:
            if item not in check_elements.split(' '):
                raise Exception(f"Your input not correct data {item}")
