from dog import Dog
from constant_type import Color, Fur


class Mastiff(Dog):
    """
    This class implement Mastiff dog that inheritance with Dog
    """

    def __init__(self,
                 name: str,
                 weight: int,
                 height: int,
                 color: Color,
                 fur: Fur,
                 gender: str,
                 age: float,
                 base_cost: float,
                 love_children: bool,
                 speed: int,
                 specific_face_color: Color
                 ) -> None:
        super().__init__(name, weight, height, color, fur, gender, age, base_cost, love_children, speed)
        self.__specific_face_color = specific_face_color

    @property
    def specific_face_color(self):
        """
        This specific face color mastiff dog
        """

        return self.__specific_face_color.name

    def bark(self) -> str:
        """
        This specific bark for mastiff dog
        """

        return "Af-af"

    def check_breed_purity(self, head_length: int, head_width: int) -> str:
        """
        This method determines breed purity mastiff
        """

        return f"{self.name} purebred mastiff" if head_width / head_length == 2 / 3 else f"{self.name} not purebred " \
                                                                                         f"mastiff "


if __name__ == "__main__":
    # E.g.
    mastiff_bob = Mastiff('Bob', 70, 75, Color.DEER, Fur.SHORT, 'female', 1, 2000, True, 20, Color.BLACK)
    print(mastiff_bob.base_cost)
    print(mastiff_bob.current_cost())
    print(mastiff_bob.love_children)
    print(mastiff_bob.specific_face_color)
    print(mastiff_bob.check_breed_purity(30, 20))
