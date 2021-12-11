class Director:
    """
    Class describing supervisor Zoo
    """

    def __init__(
            self,
            name: str,
            month_salary: int
    ) -> None:
        self.__name = name
        self.__month_salary = month_salary

    @property
    def name(self) -> str:
        return self.__name

    @property
    def month_salary(self) -> int:
        return self.__month_salary

    def calculate_year_salary(self) -> int:
        return self.__month_salary * 12
