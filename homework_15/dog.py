from constant_type import Color, Fur


class Dog:
    """
    This class describe general dog
    """

    def __init__(
            self,
            name: str,
            weight: int,
            height: int,
            color: Color,
            fur: Fur,
            gender: str,
            age: float,
            base_cost: float,
            love_children: bool,
            speed: int
    ) -> None:
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__color = color
        self.__fur = fur
        self.__gender = gender
        self.__age = age
        self.__base_cost = base_cost
        self.__love_children = love_children
        self.__speed = speed

    @property
    def name(self) -> str:
        return self.__name

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def height(self) -> int:
        return self.__height

    @property
    def color(self) -> Color:
        return self.__color.name

    @property
    def fur(self) -> Fur:
        return self.__fur.name

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def age(self) -> float:
        return self.__age

    @property
    def base_cost(self) -> float:
        return self.__base_cost

    @base_cost.setter
    def base_cost(self, base_cost: float):
        self.__base_cost = base_cost

    @property
    def love_children(self) -> bool:
        return self.__love_children

    @property
    def speed(self) -> int:
        return self.__speed

    def bark(self) -> str:
        """
        Base dog bark
        """

        return "Woof!"

    def current_cost(self) -> float:
        """
        This method calculates current cost dog relate to age, gender and base_cost
        """

        if self.__gender == 'female' and self.__age < 5:
            self.base_cost = 2 * self.__base_cost
        if 0.1 > self.__age < 0.3:
            return self.__base_cost
        elif 0.3 > self.__age < 0.6:
            return self.__base_cost * 0.8
        elif 0.6 > self.__age > 2:
            return self.__base_cost * 0.7
        elif 2 > self.__age > 5:
            return self.__base_cost * 0.5
        elif 5 > self.__age > 10:
            return self.__base_cost * 0.4
        else:
            return self.__base_cost * 0.3
