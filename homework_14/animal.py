from datetime import date


class Animal:
    """
    Class describing base animals
    """

    def __init__(
            self,
            name: str,
            kind: str,
            need_cage_volume: int,
            annual_expense: int,
            need_service_in_hour_for_day: int
    ) -> None:
        self.__name = name
        self.__kind = kind
        self.__need_cage_volume = need_cage_volume
        self.__annual_expense = annual_expense
        self.__need_service_in_hour_for_day = need_service_in_hour_for_day

    @property
    def name(self) -> str:
        return self.__name

    @property
    def kind(self) -> str:
        return self.__kind

    @property
    def need_cage_volume(self) -> int:
        return self.__need_cage_volume

    @property
    def annual_expense(self) -> int:
        return self.__annual_expense

    @property
    def need_service_in_hour_for_day(self) -> int:
        return self.__need_service_in_hour_for_day

    def calculate_service_for_year(self) -> int:
        days_year = (date(date.today().year, 12, 31) - date(date.today().year, 1, 1)).days + 1
        return days_year * self.__need_service_in_hour_for_day
